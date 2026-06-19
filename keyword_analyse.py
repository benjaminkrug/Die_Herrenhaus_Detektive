"""
Keyword-Analyse: Cerebro CSV + Magnet Text zusammenführen,
filtern und in Kampagnen-Gruppen aufteilen.
"""
import csv
import re
from pathlib import Path

# === 1. Cerebro CSV parsen ===
cerebro_file = Path(r"C:\Users\krugb\Downloads\DE_AMAZON_cerebro_3551189889_2026-03-11.csv")
cerebro_keywords = {}

# Try multiple encodings
for enc in ["utf-8-sig", "utf-8", "latin-1", "cp1252"]:
    try:
        with open(cerebro_file, "r", encoding=enc) as f:
            reader = csv.DictReader(f)
            for row in reader:
                kw = row.get("Keyword Phrase", "").strip().lower()
                if not kw:
                    # Try first column directly
                    first_key = list(row.keys())[0] if row.keys() else ""
                    kw = row.get(first_key, "").strip().lower()
                try:
                    vol_str = row.get("Suchvolumen", "0")
                    if not vol_str:
                        vol_str = "0"
                    vol = int(vol_str.replace(".", "").replace(",", ""))
                except (ValueError, AttributeError):
                    vol = 0
                if kw and len(kw) > 2 and vol >= 0:
                    cerebro_keywords[kw] = vol
        if cerebro_keywords:
            print(f"Cerebro: {len(cerebro_keywords)} Keywords geladen (encoding: {enc})")
            break
    except (UnicodeDecodeError, UnicodeError):
        continue

print(f"Cerebro: {len(cerebro_keywords)} Keywords geladen")

# === 2. Magnet Text parsen ===
magnet_file = Path(r"c:\Users\krugb\OneDrive\Desktop\GMBH\Projekte\Buecher\Die_Herrenhaus_Detektive\1.txt")
magnet_keywords = {}

with open(magnet_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip()
    # Check if next line is "Plan abonnieren" — then current line is a keyword
    if (i + 1 < len(lines) and "Plan abonnieren" in lines[i + 1]
        and line
        and not line.startswith("Plan")
        and not line.startswith("Filter")
        and not line.startswith("Cerebro")
        and not line.startswith("Export")
        and not line.startswith("Anpassen")
        and not line.startswith("Daten")
        and not re.match(r'^[\d.,>%]+$', line)
        and len(line) > 2):

        kw = line.lower().strip()
        # Try to get search volume from the numbers after "Plan abonnieren" blocks
        # Pattern: keyword, Plan abonnieren, empty, Plan abonnieren, empty, number(IQ), number(vol), ...
        vol = 0
        for j in range(i+1, min(i+10, len(lines))):
            val = lines[j].strip().replace(".", "").replace(",", "")
            if val.startswith(">"):
                val = val[1:]
            if val.isdigit() and int(val) > 10:
                vol = int(val)
                break
        magnet_keywords[kw] = vol
    i += 1

print(f"Magnet: {len(magnet_keywords)} Keywords geladen")

# === 3. Zusammenführen & Deduplizieren ===
all_keywords = {}
for kw, vol in cerebro_keywords.items():
    all_keywords[kw] = vol
for kw, vol in magnet_keywords.items():
    if kw not in all_keywords or vol > all_keywords[kw]:
        all_keywords[kw] = vol

print(f"Gesamt (dedupliziert): {len(all_keywords)} Keywords")

# === 4. Filtern ===
# Negative/irrelevante Keywords rausfiltern
negative_patterns = [
    # Format/Medium
    "hörbuch", "audible", "kindle unlimited", "kindle kostenlose", "ebook",
    "dvd", "film", "serie", "cd ", " cd",
    # Alter falsch
    "ab 12", "ab 13", "ab 14", "ab 15", "ab 16",
    "jugendbuch", "jugendliche", "teenager", "erwachsene",
    "baby", "kleinkind", "ab 1 ", "ab 2 ", "ab 3 ", "ab 4 ",
    # Genre falsch
    "thriller", "horror", "krimi erwachsene", "true crime",
    "manga", "anime", "pokemon", "minecraft",
    "kochen", "backen", "basteln", "häkeln", "stricken",
    # Format falsch
    "malbuch", "ausmalbuch", "stickerbuch", "wimmelbuch",
    "schulbuch", "lehrbuch", "lernhilfe", "übungsheft",
    "tagebuch", "freundebuch", "poesiealbum",
    # Sprache
    "französisch", "spanisch", "italienisch", "englisch", "english",
    # Spielzeug/Nicht-Buch
    "lego", "playmobil", "polly pocket", "hot wheels", "barbie",
    "ferngesteuer", "rc auto", "electric bike", "ebike", "e bike",
    "e bikes", "electric bikes", "mountain bike", "bicycle", "bike",
    "gravitrax", "perplexus", "murmelbahn", "klemmbausteine",
    "spardose", "sofortbildkamera", "mikroskop", "roboter",
    "ritterburg spielzeug", "bruder fahrzeuge", "mould king",
    "uno extreme", "brettspiel", "videospiel",
    # Irrelevante Marken/Shows
    "icrimax", "youtube", "spy x family", "beast games",
    "krass klassenfahrt",
    # Sonstiges irrelevant
    "magnetisches bruch", "flip 7", "rush hour",
    "ina müller", "rachel bright",
    # Irrelevante Buch-Themen
    "das schönste mädchen", "beschäftigung kinder restaurant",
    "autofahrt kinder beschäftigung", "beschäftigung autofahrt",
    "fantastischer wald", "drachenzähmen", "ruperts tage",
    "comic", "comics",
    "was ist was",  # Sachbuch, nicht Fiction
    "wissen für clevere",
    "reisespiele", "urlaub kinder",
    "kostenlos",  # Freebie-Sucher
]

# Exakte Matches die komplett raus sollen
negative_exact = {
    "exit game", "exit games", "exit spiel", "exit 8", "exit einsteiger",
    "cool kids", "kids", "drei", "die drei", "die dre", "die un",
    "rush", "tarantula", "lol", "boys", "spiele", "spielzeug",
    "das buch", "der junge", "die kinder", "3 jahre", "8 jahre", "ab 8",
    "hexen", "ben hur",
}

def has_wrong_age(kw):
    """Filtert Keywords mit falscher Altersgruppe (nicht 7-10)."""
    wrong_ages = [
        " ab 1", " ab 2", " ab 3", " ab 4", " ab 5", " ab 6",
        " ab 11", " ab 12", " ab 13", " ab 14",
        "1 jahr", "2 jahr", "3 jahr", "4 jahr", "5 jahr", "6 jahr",
        "11 jahr", "12 jahr", "13 jahr", "14 jahr",
        "1 jähri", "2 jähri", "3 jähri", "4 jähri", "5 jähri", "6 jähri",
        "11 jähri", "12 jähri", "13 jähri",
        "1. klasse", "1 klasse", "2. klasse", "2 klasse",
        "erstleser", "leseanfänger",
        "mädchen 2", "mädchen 3", "mädchen 4", "mädchen 5",
        "mädchen 6", "mädchen 11", "mädchen 12",
        "junge 2", "junge 3", "junge 4", "junge 5", "junge 6",
        "kind 2", "kind 3",
    ]
    for wa in wrong_ages:
        if wa in kw:
            # Ausnahme: "drei fragezeichen kids 2. klasse" hat konvertiert!
            if "fragezeichen" in kw or "detektiv" in kw or "krimi" in kw:
                return False
            return True
    return False

def is_relevant(kw):
    """Prueft ob ein Keyword relevant ist fuer Kinderkrimi ab 8-10."""
    if kw in negative_exact:
        return False
    for neg in negative_patterns:
        if neg in kw:
            return False
    if len(kw) < 3:
        return False
    if has_wrong_age(kw):
        return False
    # Keywords mit nur 1 Wort und ohne Buch-Bezug sind meistens irrelevant
    if len(kw.split()) == 1:
        relevant_singles = [
            "detektiv", "krimi", "kinderkrimi", "geheimnis",
            "kinderbuch", "kinderbücher", "abenteuer", "grusel",
            "knickerbockerbande", "leserabe", "spielbuch",
        ]
        if not any(r in kw for r in relevant_singles):
            return False
    return True

filtered = {kw: vol for kw, vol in all_keywords.items() if is_relevant(kw)}
removed = len(all_keywords) - len(filtered)
print(f"Nach Filterung: {len(filtered)} Keywords ({removed} entfernt)")

# === 5. Kategorisieren ===
categories = {
    "A_Exact_Gewinner": [],      # Direkte Detektiv/Krimi Keywords
    "B_Broad_Genre": [],         # Genre-verwandte Keywords
    "C_Broad_Geschenk": [],      # Geschenk/Anlass Keywords
    "D_Phrase_LongTail": [],     # Long-Tail 3+ Wörter
    "E_Autoren_Serien": [],      # Bekannte Autoren/Serien (Product Targeting)
    "Z_Unsicher": [],            # Manuell prüfen
}

# Bekannte Autoren/Serien
autoren_serien = [
    "drei fragezeichen", "drei ???", "3 fragezeichen", "tkkg", "fünf freunde",
    "5 freunde", "knickerbockerbande", "lassemaja", "tiger team",
    "cornelia funke", "enid blyton", "thomas brezina", "carlo meier",
    "sherlock", "agatha christie", "die olchis", "olchi",
    "das kleine böse buch", "rico oskar", "gregs tagebuch",
    "willow", "woodwalker", "warrior cats", "harry potter",
    "gina mayer", "david walliams", "rüdiger bertram",
    "nicole feller", "johanna lindemann", "anja janotta",
    "murdle", "super lesbar",
    "die kleine hexe", "petronella", "magisches baumhaus",
    "ronja räubertochter", "robin hood",
    "die jagd nach dem magischen detektivkoffer",
    "detektivbüro lassemaja", "detektivgeschichten mit pepe",
]

# Direkte Treffer (Detektiv/Krimi für Kinder) — NUR mit Buch-Bezug
direkt_patterns = [
    "detektiv", "krimi", "krimis", "kinderkrimi",
    "geheimnis", "mystery",
    "ermittl", "tatort", "verdächt", "spurensuche",
]

# Rätsel/Spiel-Keywords OHNE Buch-Bezug rausfiltern
nicht_buch_patterns = [
    "spiel", "game", "set ", " set", "puzzle",
    "rätselblock", "rätselheft", "kreuzworträtsel",
    "rätselspiele", "detektiv set", "detektiv spiele",
    "murder mystery",
]

# Geschenk/Anlass
geschenk_patterns = [
    "geschenk", "geburtstag", "weihnacht", "ostern",
    "nikolaus", "adventskalender", "mitbringsel",
    "schulanfang", "einschulung", "schultüte",
]

for kw, vol in sorted(filtered.items(), key=lambda x: x[1], reverse=True):
    categorized = False

    # Autoren/Serien
    for pattern in autoren_serien:
        if pattern in kw:
            categories["E_Autoren_Serien"].append((kw, vol))
            categorized = True
            break
    if categorized:
        continue

    # Geschenk — nur mit Buch-Bezug ODER spezifisch Alter 8-10 + Junge/Mädchen
    for pattern in geschenk_patterns:
        if pattern in kw:
            has_book = any(b in kw for b in ["buch", "bücher", "lesen"])
            has_target_age = any(a in kw for a in [
                "8 jahre", "9 jahre", "10 jahre",
                "8 jähri", "9 jähri", "10 jähri",
            ])
            has_close_age = any(a in kw for a in ["7 jahre", "7 jähri"])
            if has_book:
                categories["C_Broad_Geschenk"].append((kw, vol))
                categorized = True
            elif has_target_age:
                categories["C_Broad_Geschenk"].append((kw, vol))
                categorized = True
            elif has_close_age:
                categories["C_Broad_Geschenk"].append((kw, vol))
                categorized = True
            # Generische "geschenke kinder" ohne Alter → skip
            break
    if categorized:
        continue

    # Erst prüfen: ist es ein Nicht-Buch Keyword (Spiel, Puzzle, etc.)?
    is_nicht_buch = any(p in kw for p in nicht_buch_patterns)
    if is_nicht_buch:
        # Nur behalten wenn "buch" oder "bücher" auch drin ist
        if "buch" not in kw and "bücher" not in kw and "geschichte" not in kw:
            continue

    # Direkte Detektiv/Krimi Keywords
    for pattern in direkt_patterns:
        if pattern in kw:
            if len(kw.split()) >= 3:
                # Long-Tail Detektiv/Krimi → A (unsere besten Keywords)
                categories["A_Exact_Gewinner"].append((kw, vol))
            else:
                categories["B_Broad_Genre"].append((kw, vol))
            categorized = True
            break
    if categorized:
        continue

    # Genre-verwandt (Kinderbuch, Abenteuer, etc.)
    genre_patterns = [
        "kinderbuch", "kinderbücher", "kinder buch",
        "abenteuer", "spannung", "spannend",
        "buch ab 8", "buch ab 9", "buch ab 10",
        "bücher ab 8", "bücher ab 9", "bücher ab 10",
        "bücher junge", "bücher mädchen",
        "buch junge", "buch mädchen",
        "leseanfänger", "erstleser", "leserabe",
        "klasse", "grundschule",
        "grusel", "gruselig",
        "escape", "code",
    ]
    for pattern in genre_patterns:
        if pattern in kw:
            if len(kw.split()) >= 3:
                categories["D_Phrase_LongTail"].append((kw, vol))
            else:
                categories["B_Broad_Genre"].append((kw, vol))
            categorized = True
            break
    if categorized:
        continue

    # Rest — nur behalten wenn Buch-Bezug erkennbar
    has_book_signal = any(b in kw for b in [
        "buch", "bücher", "lesen", "lese", "lesestoff",
        "geschichte", "roman", "band ", "bestseller",
        "taschenbuch",
    ])
    has_kid_signal = any(k in kw for k in [
        "kinder", "kids", "junge", "mädchen", "ab 8", "ab 9", "ab 10",
        "ab 7", "jahre", "klasse", "grundschule",
    ])
    if has_book_signal or has_kid_signal:
        if len(kw.split()) >= 3:
            categories["D_Phrase_LongTail"].append((kw, vol))
        else:
            categories["Z_Unsicher"].append((kw, vol))
    # Alles ohne Buch/Kind-Bezug wird verworfen (nicht in Liste)

# === 5b. Manuelle Ergänzungen aus Search Term Report (bewiesene Gewinner) ===
proven_winners = [
    ("detektiv buch kinder ab 7", 100),
    ("detektiv buch kinder ab 8", 100),
    ("detektiv buch kinder ab 9", 100),
    ("detektiv bücher kinder ab 9", 100),
    ("krimis für kinder ab 8", 100),
    ("krimis für kinder ab 10", 100),
    ("kinderkrimi ab 8", 200),
    ("kinderkrimi ab 8 jahre", 150),
    ("kinderkrimi ab 10", 150),
    ("kinderkrimis ab 8", 150),
    ("kinderkrimis ab 10", 150),
    ("detektivgeschichten ab 8 jahre", 138),
    ("detektivgeschichten kinder ab 8", 100),
    ("gruselgeschichten für kinder ab 10", 100),
    ("spannende bücher für kinder ab 8", 100),
    ("spannende bücher für kinder ab 10", 100),
    ("detektiv buch kinder", 100),
    ("krimi für kinder", 100),
    ("kinderkrimi buch", 100),
    ("detektivbuch kinder", 100),
]
for kw, vol in proven_winners:
    # Nur hinzufügen wenn nicht schon in einer anderen Kategorie
    already_exists = any(kw == existing[0] for cat in categories.values() for existing in cat)
    if not already_exists:
        categories["A_Exact_Gewinner"].append((kw, vol))

# === 6. Output ===
output_file = Path(r"c:\Users\krugb\OneDrive\Desktop\GMBH\Projekte\Buecher\Die_Herrenhaus_Detektive\keyword_liste.md")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("# Keyword-Liste: Die Herrenhaus-Detektive Band 1\n\n")
    f.write(f"Erstellt: 2026-03-11\n")
    f.write(f"Quellen: Cerebro ({len(cerebro_keywords)} KW) + Magnet ({len(magnet_keywords)} KW)\n")
    f.write(f"Gesamt dedupliziert: {len(all_keywords)} → Nach Filterung: {len(filtered)}\n\n")

    for cat_name, keywords in categories.items():
        if not keywords:
            continue
        keywords.sort(key=lambda x: x[1], reverse=True)

        # Kampagnen-Empfehlung
        if cat_name == "A_Exact_Gewinner":
            empfehlung = "Kampagne 1: Exact Match, Gebot 0,10-0,15€"
        elif cat_name == "B_Broad_Genre":
            empfehlung = "Kampagne 2: Broad Match, Gebot 0,05-0,08€"
        elif cat_name == "C_Broad_Geschenk":
            empfehlung = "Kampagne 3: Broad Match, Gebot 0,05-0,08€"
        elif cat_name == "D_Phrase_LongTail":
            empfehlung = "Kampagne 5: Phrase Match, Gebot 0,05-0,07€"
        elif cat_name == "E_Autoren_Serien":
            empfehlung = "Kampagne 4: Product Targeting oder Broad Match, Gebot 0,08-0,12€"
        else:
            empfehlung = "Manuell prüfen — relevante nach B oder D verschieben"

        f.write(f"---\n\n## {cat_name} ({len(keywords)} Keywords)\n")
        f.write(f"**{empfehlung}**\n\n")
        f.write(f"| Keyword | Suchvolumen |\n")
        f.write(f"|---|---|\n")
        for kw, vol in keywords:
            f.write(f"| {kw} | {vol} |\n")
        f.write(f"\n")

    # Zusammenfassung
    total = sum(len(v) for v in categories.values())
    f.write(f"---\n\n## Zusammenfassung\n\n")
    for cat_name, keywords in categories.items():
        f.write(f"- **{cat_name}**: {len(keywords)} Keywords\n")
    f.write(f"- **Gesamt**: {total} Keywords\n")

print(f"\nOK: Keyword-Liste geschrieben: {output_file}")
print(f"\nZusammenfassung:")
for cat_name, keywords in categories.items():
    print(f"  {cat_name}: {len(keywords)} Keywords")
print(f"  GESAMT: {sum(len(v) for v in categories.values())}")
