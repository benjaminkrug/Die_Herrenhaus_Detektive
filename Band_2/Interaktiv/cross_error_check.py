"""
Cross-Error-Detektion fuer Band 2 Interaktiv.
Prueft alle Abschnitte auf Konsistenz-Fehler zwischen Clustern.

Verwendung:
    python cross_error_check.py
"""
import os
import re
import sys
import io
from collections import defaultdict

# Windows-Konsole auf UTF-8 setzen
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ABSCHNITTE_DIR = os.path.join(BASE_DIR, "Abschnitte")

# ============================================================
# Cluster-Zuordnung
# ============================================================

COMMON_START = {"1", "2", "3", "4", "5", "6", "7"}

CLUSTER_A = {
    "11", "12", "13", "13b", "13c", "14", "14b", "14c", "15", "16",
    "16b", "17", "18", "18b", "19", "20", "20b", "21", "22", "23", "24",
    "24b", "25", "25b", "26", "26b", "27", "28", "29", "30", "31",
    "32", "33", "34"
}

CLUSTER_B = {
    "41", "42", "43", "43b", "44", "45", "45b", "45c", "45d", "45e",
    "46", "47", "48", "48b", "49", "50", "50b", "51", "52", "53", "54",
    "55", "56", "57", "58", "59", "59b", "59c"
}

CLUSTER_C = {
    "66", "67", "67b", "67c", "67d", "68", "69", "70", "70b", "71", "72",
    "72b", "72c", "73", "74", "75", "76", "77", "78", "79", "79b",
    "80", "81", "82", "83", "84", "85", "86"
}

CLUSTER_D = {
    "91", "92", "93", "94", "95", "96", "96b", "97", "98", "99", "99b",
    "99c", "99d", "99e", "100", "101", "101b", "102", "103", "104",
    "105", "106"
}

# Easter Egg (kein Cluster, erreichbar ueber Codewoerter aus allen 4-Stern-Enden)
EASTER_EGG = {"200"}

ALL_SECTIONS = COMMON_START | CLUSTER_A | CLUSTER_B | CLUSTER_C | CLUSTER_D | EASTER_EGG


def get_cluster(section_id):
    """Gibt den Cluster-Namen fuer eine Abschnitt-ID zurueck."""
    if section_id in COMMON_START:
        return "START"
    if section_id in CLUSTER_A:
        return "A"
    if section_id in CLUSTER_B:
        return "B"
    if section_id in CLUSTER_C:
        return "C"
    if section_id in CLUSTER_D:
        return "D"
    if section_id in EASTER_EGG:
        return "EASTER_EGG"
    return "UNBEKANNT"


# ============================================================
# Wissens-Regeln: Was darf wo NICHT vorkommen
# ============================================================

# Begriffe die NUR in bestimmten Clustern vorkommen duerfen
CLUSTER_EXCLUSIVE_TERMS = {
    # Cluster A exklusiv
    "A": [
        (r"Flut\w*\s+(?:in|der)\s+Kammer", "Flut-Szene nur in Cluster A"),
        (r"Wasser\s+stieg.*Rinne", "Steigende Rinne nur in Cluster A"),
    ],
    # Cluster B exklusiv
    "B": [
        (r"Glasflasche", "Glasflaschen sind nur in Cluster B bekannt"),
        (r"Wasserprobe", "Wasserproben nur in Cluster B"),
        (r"Rohr-Zeichnung", "Rohr-Zeichnungen nur in Cluster B (Ben)"),
        (r"Brunnen\s+flie.t", "Brunnen reparieren nur in Cluster B"),
        (r"Wasserfall", "Wasserfall nur in Cluster B"),
        (r"unterirdisch\w*\s+Fluss", "Unterirdischer Fluss nur in Cluster B"),
    ],
    # Cluster C exklusiv
    "C": [
        (r"Karl\w*\s+Ring", "Karls Ring-Geschichte nur in Cluster C"),
        (r"70\s+Jahre", "70 Jahre Schweigen nur in Cluster C"),
        (r"Lisbeth\w*\s+Traenen", "Lisbeths Traenen nur in Cluster C"),
        (r"K\.B\.\s*\+\s*L\.B\.", "Karls Initialen nur in Cluster C"),
        (r"Fotoalbum", "Fotoalbum nur in Cluster C"),
    ],
    # Cluster D exklusiv
    "D": [
        (r"zweite\s+Karte", "Zweite Karte NUR in Cluster D"),
        (r"zweite\w*\s+Quelle", "Zweite Quelle NUR in Cluster D"),
        (r"Winter\s+r[ui][ef]t?\s+an", "Winter-Anruf NUR in Cluster D"),
        (r"Winter\s+am\s+Telefon", "Winter am Telefon NUR in Cluster D"),
        (r"Winter\s+erkl.rt", "Winter erklaert NUR in Cluster D"),
    ],
}

# Begriffe die im gemeinsamen Start NICHT vorkommen duerfen
START_FORBIDDEN = [
    (r"Metalltuer\s+ge.ffnet", "Metalltuer wird im Start nicht geoeffnet"),
    (r"Gaenge\s+betreten", "Gaenge werden im Start nicht betreten"),
    (r"Zeitkapsel", "Zeitkapsel ist im Start unbekannt"),
    (r"Quelle\s+gefunden", "Quelle ist im Start unbekannt"),
    (r"Glasflasche", "Glasflaschen sind im Start unbekannt"),
    (r"zweite\s+Karte", "Zweite Karte ist im Start unbekannt"),
]

# ============================================================
# Vorwissen-Fehler: Bestimmte Artikel suggerieren Vorwissen
# ============================================================

# In Clustern wo Orte zum ERSTEN MAL besucht werden:
# unbestimmter Artikel ("ein", "eine") statt bestimmter ("der", "die", "das")
FIRST_VISIT_CHECKS = {
    # In Cluster B betreten sie die Gaenge zum ersten Mal anders (durch Muehle)
    "B": [
        (r"die\s+Metalltuer", "In Cluster B kennen sie die Metalltuer nicht"),
    ],
    # In Cluster C ohne Frau Bergmann kennen sie den Weg nicht
    "C": [
        # OK - sie kennen die Gaenge nicht direkt
    ],
}


# ============================================================
# Verweis-Pruefung
# ============================================================

def check_section_references(section_id, text):
    """Prueft ob alle 'Abschnitt X' Verweise auf existierende Abschnitte zeigen."""
    errors = []
    for m in re.finditer(r'Abschnitt\s+(\d+\w?)', text):
        ref_id = m.group(1)
        if ref_id not in ALL_SECTIONS:
            errors.append(
                f"Verweis auf nicht-existierenden Abschnitt {ref_id}"
            )
    return errors


def check_cross_cluster_references(section_id, text):
    """Prueft ob Verweise nur auf erlaubte Cluster zeigen."""
    errors = []
    cluster = get_cluster(section_id)

    for m in re.finditer(r'Abschnitt\s+(\d+\w?)', text):
        ref_id = m.group(1)
        ref_cluster = get_cluster(ref_id)

        # Vom Start darf man in alle Cluster verweisen (EP-MAIN)
        if cluster == "START":
            continue

        # Innerhalb eines Clusters ist OK
        if ref_cluster == cluster:
            continue

        # Verweis zurueck zum Start ist OK
        if ref_cluster == "START":
            continue

        errors.append(
            f"Cross-Cluster-Verweis: Abschnitt {section_id} (Cluster {cluster}) "
            f"verweist auf Abschnitt {ref_id} (Cluster {ref_cluster})"
        )

    return errors


# ============================================================
# Stil-Pruefung
# ============================================================

def check_sentence_length(section_id, text):
    """Prueft ob Saetze die maximale Laenge ueberschreiten."""
    warnings = []
    # Nur Prosa-Text pruefen (keine Markdown-Formatierung)
    clean = re.sub(r'\*\*[^*]+\*\*', '', text)  # Bold entfernen
    clean = re.sub(r'\*[^*]+\*', '', clean)       # Italic entfernen
    clean = re.sub(r'#.*', '', clean)              # Headers entfernen
    clean = re.sub(r'---', '', clean)              # Separator entfernen

    sentences = re.split(r'[.!?](?:\s|$)', clean)
    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue
        # Dialog-Tags ignorieren
        if sent.startswith('\u201e') or sent.startswith('"'):
            continue
        words = sent.split()
        if len(words) > 15:
            warnings.append(
                f"Langer Satz ({len(words)} Woerter): \"{sent[:60]}...\""
            )

    return warnings


def check_dialog_ratio(section_id, text):
    """Prueft ob der Dialoganteil mindestens 30% betraegt."""
    warnings = []
    lines = text.split('\n')
    total_lines = 0
    dialog_lines = 0

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped == '---':
            continue
        if stripped.startswith('*'):
            continue
        total_lines += 1
        if '\u201e' in stripped or '\u201c' in stripped or '"' in stripped:
            dialog_lines += 1

    if total_lines > 5:  # Nur bei laengeren Abschnitten pruefen
        ratio = dialog_lines / total_lines
        if ratio < 0.35:
            warnings.append(
                f"Niedriger Dialoganteil: {ratio:.0%} "
                f"({dialog_lines}/{total_lines} Zeilen)"
            )

    return warnings


# ============================================================
# Passiv-Erkennung
# ============================================================

PASSIVE_PATTERNS = [
    r'wurde\s+\w+t\b',
    r'wurden\s+\w+t\b',
    r'wird\s+\w+t\b',
    r'werden\s+\w+t\b',
    r'ist\s+\w+t\s+worden',
    r'war\s+\w+t\s+worden',
]


def check_passive_voice(section_id, text):
    """Prueft auf Passiv-Konstruktionen."""
    warnings = []
    for pattern in PASSIVE_PATTERNS:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            # Falsch-Positive filtern
            match_text = m.group(0)
            if any(fp in match_text.lower() for fp in
                   ['wurde blass', 'wurde rot', 'wurde still',
                    'wurde laut', 'wurde dunkel', 'wurde hell',
                    'wurde kalt', 'wurde warm', 'wurde nass',
                    'wurde eng', 'wurde weit', 'wurde schmal',
                    'wurde ernst', 'wurde hart', 'wurde feucht',
                    'wurden feucht', 'wurden weit', 'wird zeit',
                    'werden gesichert', 'wurden gesichert']):
                continue
            warnings.append(
                f"Moegliches Passiv: \"{match_text}\""
            )

    return warnings


# ============================================================
# Krueger-Zitat-Pruefung
# ============================================================

# Krueger sagt im Start NUR: "Bleibt weg" + "Manche Haeuser haben Raeume, die man nicht sieht"
KRUEGER_START_QUOTES = [
    "Bleibt weg",
    "Manche Häuser haben Räume",
    "Räume, die man nicht sieht",
]


def check_krueger_quotes(section_id, text):
    """Prueft ob Krueger-Zitate zum richtigen Cluster passen."""
    errors = []
    cluster = get_cluster(section_id)

    # In Nicht-D-Clustern: Krueger darf nicht ueber die zweite Quelle reden
    if cluster != "D":
        if re.search(r'Kr.ger.*zweite\s+Quelle', text, re.IGNORECASE):
            errors.append(
                "Krueger weiss NICHTS von der zweiten Quelle (nur Winter in Cluster D)"
            )

    return errors


# ============================================================
# Frau Bergmann Pruefung
# ============================================================

def check_bergmann_knowledge(section_id, text):
    """Prueft ob Frau Bergmann-Details nur in Cluster C vorkommen."""
    errors = []
    cluster = get_cluster(section_id)

    if cluster not in ("C", "START"):
        # In anderen Clustern darf Frau Bergmanns Geschichte nicht detailliert sein
        if re.search(r'Bergmann.*erz.hlt', text, re.IGNORECASE):
            errors.append(
                "Frau Bergmann erzaehlt ihre Geschichte nur in Cluster C"
            )
        if re.search(r'Karl\s+und\s+Lisbeth', text, re.IGNORECASE):
            errors.append(
                "Karl und Lisbeth Details nur in Cluster C"
            )

    return errors


# ============================================================
# Check 9: ENDE-Konsistenz
# ============================================================

def check_endings(sections):
    """Prueft alle Enden auf Konsistenz: eindeutige Nummern, Shortcuts, Codewoerter."""
    errors = []
    warnings = []
    ende_numbers = {}

    for sid, text in sections.items():
        m = re.search(r'ENDE\s+(\d+)', text)
        if not m:
            continue

        ende_num = m.group(1)

        # Eindeutigkeit
        if ende_num in ende_numbers:
            errors.append(
                f"ENDE {ende_num} doppelt vergeben: "
                f"Abschnitt {ende_numbers[ende_num]} und {sid}"
            )
        ende_numbers[ende_num] = sid

        # Replay-Shortcuts
        has_vorne = "Von vorne" in text
        has_direkt = "Direkt zur Entscheidung" in text
        if not has_vorne or not has_direkt:
            warnings.append(
                f"Abschnitt {sid}: ENDE {ende_num} ohne Replay-Shortcuts"
            )

        # Stern-Rating zaehlen
        stars = text.count("\u2605")

        # 4-Stern-Enden: Bonus-Wissen + Codewort
        if stars == 4:
            if "Bonus-Wissen" not in text:
                warnings.append(
                    f"Abschnitt {sid}: 4\u2605-Ende ohne Bonus-Wissen-Hint"
                )
            if not re.search(r'\*\*\*\w+\.\*\*\*', text):
                warnings.append(
                    f"Abschnitt {sid}: 4\u2605-Ende ohne fett+kursives Codewort"
                )

    return errors, warnings


# ============================================================
# Check 10: Erreichbarkeit (BFS)
# ============================================================

def check_reachability(sections):
    """BFS von Abschnitt 1 — prueft ob alle Abschnitte erreichbar sind."""
    errors = []

    # Navigations-Graph bauen
    graph = defaultdict(set)
    for sid, text in sections.items():
        for m in re.finditer(r'Abschnitt\s+(\d+\w?)', text):
            ref = m.group(1)
            if ref in sections:
                graph[sid].add(ref)

    # BFS von "1"
    visited = set()
    queue = ["1"]
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)

    # Nicht erreichbare Abschnitte
    for sid in sorted(sections.keys(), key=lambda x: (len(x), x)):
        if sid not in visited and sid != "200":
            errors.append(f"Abschnitt {sid} nicht erreichbar von Abschnitt 1")

    return errors


# ============================================================
# Check 11: Dead-End-Erkennung
# ============================================================

def check_dead_ends(sections):
    """Prueft ob Nicht-ENDE-Abschnitte Ausgangs-Links haben."""
    errors = []
    for sid, text in sections.items():
        has_ende = bool(re.search(r'ENDE\s+\d+', text))
        has_nav = bool(re.search(r'Abschnitt\s+\d+\w?', text))
        if not has_ende and not has_nav:
            errors.append(
                f"Abschnitt {sid}: Weder ENDE noch Navigations-Link (Dead End)"
            )
    return errors


# ============================================================
# Check 12: Verbotene Woerter
# ============================================================

FORBIDDEN_WORDS = [
    (r'mysteri.s', "mysterioes → seltsam"),
    (r'observier', "observieren → beobachten"),
    (r'komplex', "komplex → schwierig"),
    (r'residier', "residieren → wohnen"),
    (r'Atmosph.re', "Atmosphaere → Stimmung"),
    (r'philosoph', "philosophisch → zu abstrakt"),
    (r'melanchol', "melancholisch → traurig"),
    (r'signifikan', "signifikant → wichtig"),
    (r'implizier', "implizieren → andeuten"),
    (r'analysier', "analysieren → untersuchen"),
    (r'demonstrier', "demonstrieren → zeigen"),
    (r'irritier', "irritieren → verwirren"),
    (r'konstatier', "konstatieren → feststellen"),
    (r'absurd', "absurd → verrueckt"),
    (r'bizarr', "bizarr → seltsam"),
    (r'kurios', "kurios → merkwuerdig"),
]


def check_forbidden_words(section_id, text):
    """Prueft auf verbotene abstrakte/schwierige Woerter."""
    warnings = []
    for pattern, suggestion in FORBIDDEN_WORDS:
        if re.search(pattern, text, re.IGNORECASE):
            warnings.append(f"Verbotenes Wort: {suggestion}")
    return warnings


# ============================================================
# Check 13: Abstrakte Emotionen
# ============================================================

ABSTRACT_EMOTION_PATTERNS = [
    (r'f.hlte\s+sich', "Abstrakte Emotion: 'fuehlte sich' → physische Reaktion"),
    (r'hatte\s+ein\w*\s+(?:seltsam|komisch|merkw.rdig)\w*\s+Gef.hl',
     "Abstrakte Emotion: 'hatte ein Gefuehl' → physische Reaktion"),
    (r'sp.rte\s+ein\s+seltsam', "Abstrakte Emotion: 'spuerte ein seltsames' → konkret"),
    (r'empfand\b', "Abstrakte Emotion: 'empfand' → physische Reaktion"),
    (r'(?:war|wurde)\s+(?:sehr\s+)?nerv.s\b',
     "Abstrakte Emotion: 'war nervoes' → 'Seine Haende zitterten'"),
]


def check_abstract_emotions(section_id, text):
    """Prueft auf abstrakte Emotionsbeschreibungen."""
    warnings = []
    for pattern, msg in ABSTRACT_EMOTION_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            warnings.append(msg)
    return warnings


# ============================================================
# Check 14: Abschnitt-Laenge
# ============================================================

def check_section_length(section_id, text):
    """Prueft ob Abschnitte zu kurz oder zu lang sind."""
    warnings = []

    # Nur Prosa zaehlen (Markdown entfernen)
    clean = re.sub(r'#.*', '', text)
    clean = re.sub(r'---', '', clean)
    clean = re.sub(r'\*\*[^*]+\*\*', '', clean)
    clean = re.sub(r'\*[^*]+\*', '', clean)
    clean = re.sub(r'^\s*$', '', clean, flags=re.MULTILINE)

    words = clean.split()
    word_count = len(words)

    if word_count < 80:
        warnings.append(f"Sehr kurzer Abschnitt: {word_count} Woerter")
    elif word_count > 700:
        warnings.append(f"Sehr langer Abschnitt: {word_count} Woerter")

    return warnings


# ============================================================
# Check 15: Charakter-Praesenz
# ============================================================

def check_character_presence(section_id, text):
    """Prueft ob mindestens 2 der 3 Hauptcharaktere erwaehnt werden."""
    warnings = []

    # Nur Prosa vor ENDE pruefen
    ende_pos = text.find("ENDE")
    check_text = text[:ende_pos] if ende_pos > 0 else text

    words = check_text.split()
    if len(words) < 150:
        return warnings

    chars_present = 0
    if re.search(r'\bJonas\b', check_text):
        chars_present += 1
    if re.search(r'\bMila\b', check_text):
        chars_present += 1
    if re.search(r'\bBen\b', check_text):
        chars_present += 1

    if chars_present < 2:
        warnings.append(
            f"Nur {chars_present}/3 Hauptcharaktere erwaehnt "
            f"(Jonas/Mila/Ben)"
        )

    return warnings


# ============================================================
# Check 16: Ben-Humor/Angst
# ============================================================

BEN_PATTERNS = [
    r'Kappe',
    r'M.tze',
    r'schluckte',
    r'wich\s+zur.ck',
    r'Augen\s+wurden\s+weit',
    r'Gummi',
    r'Eis\b',
    r'Kuchen',
    r'Idee',
    r'bemerkt',
    r'sah\s+es',
    r'grinste',
    r'st.hnte',
    r'murmelte',
]


def check_ben_moments(section_id, text):
    """Prueft ob Ben in laengeren Abschnitten typische Momente hat."""
    warnings = []

    ende_pos = text.find("ENDE")
    check_text = text[:ende_pos] if ende_pos > 0 else text

    words = check_text.split()
    if len(words) < 200:
        return warnings

    if not re.search(r'\bBen\b', check_text):
        return warnings

    has_pattern = False
    for pattern in BEN_PATTERNS:
        # Pruefen ob Pattern in Bens Naehe vorkommt (im selben Abschnitt)
        if re.search(pattern, check_text, re.IGNORECASE):
            has_pattern = True
            break

    if not has_pattern:
        warnings.append(
            "Ben erwaehnt aber ohne typisches Muster "
            "(Kappe, Humor, Angst, Cleverness)"
        )

    return warnings


# ============================================================
# Check 17: Formatierungs-Konsistenz
# ============================================================

def check_formatting(section_id, text):
    """Prueft ENDE-Formatierung auf Konsistenz."""
    warnings = []

    # ENDE-Zeile pruefen
    ende_match = re.search(r'ENDE\s+\d+\s*(.{0,5})', text)
    if ende_match:
        after = ende_match.group(1)
        if '--' in after and '\u2014' not in after:
            warnings.append(
                "ENDE-Zeile: '--' statt em dash '\u2014'"
            )
        if '"' in text[ende_match.start():ende_match.start()+80]:
            line = text[ende_match.start():text.find('\n', ende_match.start())]
            if '"' in line and '\u201e' not in line:
                warnings.append(
                    'ENDE-Zeile: gerade Anfuehrungszeichen statt \u201e\u201c'
                )

    # Navigations-Links pruefen
    if '->' in text:
        warnings.append("Navigations-Link: '->' statt '\u2192'")

    return warnings


# ============================================================
# Hauptprogramm
# ============================================================

def load_sections():
    """Laedt alle Abschnitt-Dateien."""
    sections = {}
    if not os.path.exists(ABSCHNITTE_DIR):
        print(f"FEHLER: Verzeichnis nicht gefunden: {ABSCHNITTE_DIR}")
        return sections

    # Verwaiste Abschnitte (aus Flow entfernt, Datei noch vorhanden)
    ORPHANED = {"Abschnitt_87.md"}

    for f in os.listdir(ABSCHNITTE_DIR):
        if not f.startswith("Abschnitt_") or not f.endswith(".md"):
            continue
        if "Einleitung" in f or "Konsistenz" in f or "Hinweisseite" in f:
            continue
        if f in ORPHANED:
            continue

        # ID extrahieren
        name = f.replace("Abschnitt_", "").replace(".md", "")
        match = re.match(r'0*(\d+\w*)', name)
        if match:
            sid = match.group(1)
        else:
            sid = name

        filepath = os.path.join(ABSCHNITTE_DIR, f)
        with open(filepath, 'r', encoding='utf-8') as fh:
            sections[sid] = fh.read()

    return sections


def check_completeness(sections):
    """Prueft ob alle erwarteten Abschnitte vorhanden sind."""
    errors = []
    for sid in sorted(ALL_SECTIONS, key=lambda x: (len(x), x)):
        if sid not in sections:
            errors.append(f"Abschnitt {sid} fehlt!")
    return errors


def main():
    print("=" * 60)
    print("Cross-Error-Detektion: Band 2 Interaktiv")
    print("=" * 60)
    print()

    sections = load_sections()
    print(f"Geladene Abschnitte: {len(sections)}")
    print(f"Erwartete Abschnitte: {len(ALL_SECTIONS)}")
    print()

    all_errors = []
    all_warnings = []

    # 1. Vollstaendigkeit pruefen
    print("[1/17] Vollstaendigkeit...")
    missing = check_completeness(sections)
    all_errors.extend([("FEHLEND", e) for e in missing])
    print(f"  {len(missing)} fehlende Abschnitte")

    # 2. Verweis-Pruefung
    print("[2/17] Verweise...")
    ref_errors = 0
    for sid, text in sections.items():
        for err in check_section_references(sid, text):
            all_errors.append((f"Abschnitt {sid}", err))
            ref_errors += 1
    print(f"  {ref_errors} Verweis-Fehler")

    # 3. Cross-Cluster-Verweise
    print("[3/17] Cross-Cluster-Verweise...")
    cc_errors = 0
    for sid, text in sections.items():
        for err in check_cross_cluster_references(sid, text):
            all_errors.append((f"Abschnitt {sid}", err))
            cc_errors += 1
    print(f"  {cc_errors} Cross-Cluster-Fehler")

    # 4. Cluster-exklusive Begriffe
    print("[4/17] Cluster-exklusive Begriffe...")
    excl_errors = 0
    for sid, text in sections.items():
        cluster = get_cluster(sid)
        for excl_cluster, terms in CLUSTER_EXCLUSIVE_TERMS.items():
            if cluster == excl_cluster or cluster == "START" or cluster == "EASTER_EGG":
                continue
            for pattern, msg in terms:
                if re.search(pattern, text, re.IGNORECASE):
                    all_errors.append((f"Abschnitt {sid} (Cluster {cluster})", msg))
                    excl_errors += 1
    print(f"  {excl_errors} Exklusivitaets-Fehler")

    # 5. Start-Verbote
    print("[5/17] Start-Verbote...")
    start_errors = 0
    for sid in COMMON_START:
        if sid not in sections:
            continue
        for pattern, msg in START_FORBIDDEN:
            if re.search(pattern, sections[sid], re.IGNORECASE):
                all_errors.append((f"Abschnitt {sid} (START)", msg))
                start_errors += 1
    print(f"  {start_errors} Start-Verbot-Fehler")

    # 6. Krueger + Bergmann
    print("[6/17] Charakter-Konsistenz (Krueger/Bergmann)...")
    char_errors = 0
    for sid, text in sections.items():
        for err in check_krueger_quotes(sid, text):
            all_errors.append((f"Abschnitt {sid}", err))
            char_errors += 1
        for err in check_bergmann_knowledge(sid, text):
            all_errors.append((f"Abschnitt {sid}", err))
            char_errors += 1
    print(f"  {char_errors} Charakter-Fehler")

    # 7. Stil-Pruefung
    print("[7/17] Stil (Satzlaenge, Dialog, Passiv)...")
    style_warnings = 0
    for sid, text in sections.items():
        for w in check_sentence_length(sid, text):
            all_warnings.append((f"Abschnitt {sid}", w))
            style_warnings += 1
        for w in check_dialog_ratio(sid, text):
            all_warnings.append((f"Abschnitt {sid}", w))
            style_warnings += 1
        for w in check_passive_voice(sid, text):
            all_warnings.append((f"Abschnitt {sid}", w))
            style_warnings += 1
    print(f"  {style_warnings} Stil-Warnungen")

    # 8. Vorwissen-Artikel
    print("[8/17] Vorwissen-Artikel...")
    fv_errors = 0
    for sid, text in sections.items():
        cluster = get_cluster(sid)
        if cluster in FIRST_VISIT_CHECKS:
            for pattern, msg in FIRST_VISIT_CHECKS[cluster]:
                if re.search(pattern, text, re.IGNORECASE):
                    all_errors.append((f"Abschnitt {sid}", msg))
                    fv_errors += 1
    print(f"  {fv_errors} Vorwissen-Fehler")

    # 9. ENDE-Konsistenz
    print("[9/17] ENDE-Konsistenz...")
    ende_errors, ende_warnings = check_endings(sections)
    all_errors.extend([(f"ENDE", e) for e in ende_errors])
    all_warnings.extend([(f"ENDE", w) for w in ende_warnings])
    print(f"  {len(ende_errors)} Fehler, {len(ende_warnings)} Warnungen")

    # 10. Erreichbarkeit
    print("[10/17] Erreichbarkeit (BFS von Abschnitt 1)...")
    reach_errors = check_reachability(sections)
    all_errors.extend([("ERREICHBARKEIT", e) for e in reach_errors])
    print(f"  {len(reach_errors)} nicht erreichbare Abschnitte")

    # 11. Dead-End-Erkennung
    print("[11/17] Dead-End-Erkennung...")
    dead_errors = check_dead_ends(sections)
    all_errors.extend([("DEAD-END", e) for e in dead_errors])
    print(f"  {len(dead_errors)} Dead Ends")

    # 12. Verbotene Woerter
    print("[12/17] Verbotene Woerter...")
    vocab_warnings = 0
    for sid, text in sections.items():
        for w in check_forbidden_words(sid, text):
            all_warnings.append((f"Abschnitt {sid}", w))
            vocab_warnings += 1
    print(f"  {vocab_warnings} verbotene Woerter")

    # 13. Abstrakte Emotionen
    print("[13/17] Abstrakte Emotionen...")
    emotion_warnings = 0
    for sid, text in sections.items():
        for w in check_abstract_emotions(sid, text):
            all_warnings.append((f"Abschnitt {sid}", w))
            emotion_warnings += 1
    print(f"  {emotion_warnings} abstrakte Emotionen")

    # 14. Abschnitt-Laenge
    print("[14/17] Abschnitt-Laenge...")
    length_warnings = 0
    for sid, text in sections.items():
        for w in check_section_length(sid, text):
            all_warnings.append((f"Abschnitt {sid}", w))
            length_warnings += 1
    print(f"  {length_warnings} Laenge-Warnungen")

    # 15. Charakter-Praesenz
    print("[15/17] Charakter-Praesenz (Jonas/Mila/Ben)...")
    char_warnings = 0
    for sid, text in sections.items():
        for w in check_character_presence(sid, text):
            all_warnings.append((f"Abschnitt {sid}", w))
            char_warnings += 1
    print(f"  {char_warnings} Praesenz-Warnungen")

    # 16. Ben-Humor/Angst
    print("[16/17] Ben-Humor/Angst...")
    ben_warnings = 0
    for sid, text in sections.items():
        for w in check_ben_moments(sid, text):
            all_warnings.append((f"Abschnitt {sid}", w))
            ben_warnings += 1
    print(f"  {ben_warnings} Ben-Muster-Warnungen")

    # 17. Formatierungs-Konsistenz
    print("[17/17] Formatierungs-Konsistenz...")
    fmt_warnings = 0
    for sid, text in sections.items():
        for w in check_formatting(sid, text):
            all_warnings.append((f"Abschnitt {sid}", w))
            fmt_warnings += 1
    print(f"  {fmt_warnings} Format-Warnungen")

    # Ergebnis
    print()
    print("=" * 60)
    print(f"ERGEBNIS: {len(all_errors)} Fehler, {len(all_warnings)} Warnungen")
    print("=" * 60)

    if all_errors:
        print()
        print("FEHLER:")
        for loc, msg in sorted(all_errors):
            print(f"  [{loc}] {msg}")

    if all_warnings:
        print()
        print("WARNUNGEN:")
        for loc, msg in sorted(all_warnings):
            print(f"  [{loc}] {msg}")

    if not all_errors and not all_warnings:
        print()
        print("Keine Fehler oder Warnungen gefunden!")

    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
