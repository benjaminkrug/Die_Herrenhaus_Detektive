"""
Keyword-Analyse fuer Band 1 INTERAKTIV (Spielbuch/CYOA).
Andere Kategorisierung als das lineare Buch!
"""
import re
from pathlib import Path

# === 1. Magnet Text parsen ===
magnet_file = Path(r"C:\Users\krugb\OneDrive\Desktop\GMBH\Projekte\Buecher\Die_Schattenjaeger\7.txt")
magnet_keywords = {}

with open(magnet_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip()
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

# === 2. Filtern ===
negative_patterns = [
    # Format/Medium
    "hörbuch", "audible", "kindle unlimited", "ebook",
    "dvd", "film", "serie", "cd ",
    # Alter falsch
    "ab 12", "ab 13", "ab 14", "ab 15", "ab 16",
    "jugendbuch", "jugendliche", "teenager", "erwachsene",
    "baby", "kleinkind",
    # Genre falsch
    "thriller", "horror", "krimi erwachsene", "true crime",
    "manga", "anime", "pokemon", "minecraft",
    "kochen", "backen", "basteln", "häkeln",
    # Format falsch
    "malbuch", "ausmalbuch", "stickerbuch", "wimmelbuch",
    "schulbuch", "lehrbuch", "lernhilfe", "übungsheft",
    "tagebuch", "freundebuch",
    # Sprache
    "französisch", "spanisch", "italienisch", "englisch", "english",
    # Spielzeug (nicht Spielbuch!)
    "lego", "playmobil", "polly pocket", "hot wheels", "barbie",
    "ferngesteuer", "rc auto", "electric bike", "ebike", "e bike",
    "gravitrax", "perplexus", "murmelbahn", "klemmbausteine",
    "spardose", "sofortbildkamera", "mikroskop",
    "uno extreme", "brettspiel", "videospiel", "kartenspiel",
    # Irrelevante Marken/Shows
    "icrimax", "youtube", "spy x family", "beast games",
    "krass klassenfahrt",
    # Sonstiges
    "kostenlos", "gratis",
]

negative_exact = {
    "exit game", "exit games", "exit spiel", "exit 8",
    "cool kids", "kids", "drei", "die drei", "die dre",
    "rush", "lol", "boys", "spiele", "spielzeug",
    "das buch", "der junge", "die kinder",
    "hexen", "ben hur",
}

def has_wrong_age(kw):
    wrong_ages = [
        " ab 1", " ab 2", " ab 3", " ab 4", " ab 5", " ab 6",
        " ab 11", " ab 12", " ab 13", " ab 14",
        "1 jahr", "2 jahr", "3 jahr", "4 jahr", "5 jahr", "6 jahr",
        "11 jahr", "12 jahr", "13 jahr", "14 jahr",
        "1 jähri", "2 jähri", "3 jähri", "4 jähri", "5 jähri", "6 jähri",
        "11 jähri", "12 jähri", "13 jähri",
        "1. klasse", "1 klasse", "2. klasse", "2 klasse",
        "mädchen 2", "mädchen 3", "mädchen 4", "mädchen 5",
        "mädchen 6", "mädchen 11", "mädchen 12",
        "junge 2", "junge 3", "junge 4", "junge 5", "junge 6",
    ]
    for wa in wrong_ages:
        if wa in kw:
            if "1000 gefahren" in kw or "spielbuch" in kw or "escape" in kw:
                return False
            return True
    return False

def is_relevant(kw):
    if kw in negative_exact:
        return False
    for neg in negative_patterns:
        if neg in kw:
            return False
    if len(kw) < 3:
        return False
    if has_wrong_age(kw):
        return False
    return True

filtered = {kw: vol for kw, vol in magnet_keywords.items() if is_relevant(kw)}
removed = len(magnet_keywords) - len(filtered)
print(f"Nach Filterung: {len(filtered)} Keywords ({removed} entfernt)")

# === 3. Kategorisieren (INTERAKTIV-spezifisch!) ===
categories = {
    "A_Spielbuch_CYOA": [],        # Spielbuch, du entscheidest, 1000 Gefahren
    "B_Escape_Raetsel": [],        # Escape, Rätsel, Mitmachkrimi
    "C_Detektiv_Krimi": [],        # Detektiv/Krimi Keywords (Überschneidung mit Linear)
    "D_Lesemotivation": [],        # Lesemuffel, kurze Kapitel, spannendes Buch
    "E_Konkurrenz_Serien": [],     # Bekannte Serien/Autoren
    "F_Geschenk": [],              # Geschenk-Keywords mit Alter 7-10
    "G_LongTail": [],              # Sonstige relevante Long-Tail
    "Z_Unsicher": [],              # Manuell pruefen
}

# Spielbuch/CYOA Patterns
spielbuch_patterns = [
    "spielbuch", "1000 gefahren", "tausend gefahren",
    "du entscheidest", "entscheide selbst", "interaktiv",
    "mehrere enden", "multiple enden", "verschiedene enden",
    "choose your own", "cyoa",
    "abenteuer spielbuch", "entscheidung",
    "mitmach", "mitmachbuch",
]

# Escape/Rätsel Patterns
escape_patterns = [
    "escape", "rätsel", "rätselbuch", "quiz",
    "ratekrimi", "knobel", "code", "geheim",
    "schnitzeljagd",
]

# Detektiv/Krimi
detektiv_patterns = [
    "detektiv", "krimi", "krimis", "kinderkrimi",
    "mystery", "ermittl", "tatort", "spurensuche",
]

# Lesemotivation
lesemotivation_patterns = [
    "lesemuffel", "lesen motivieren", "nicht gerne lesen",
    "kurze kapitel", "spannendes kinderbuch", "spannend",
    "leseförderung", "lesefaul", "leselust",
    "erstleser",
]

# Bekannte Serien/Konkurrenten
konkurrenz_serien = [
    "1000 gefahren", "tausend gefahren",
    "das buch mit dem fluch", "bitte nicht öffnen",
    "vorsicht bissig",
    "drei fragezeichen", "drei ???", "3 fragezeichen",
    "sherlock", "die olchis", "olchi",
    "das kleine böse buch", "rico oskar",
    "cornelia funke", "david walliams",
    "knickerbockerbande", "lassemaja",
    "magisches baumhaus",
    "warrior cats", "woodwalker",
    "die kleine hexe", "petronella",
]

# Geschenk
geschenk_patterns = [
    "geschenk", "geburtstag", "weihnacht", "ostern",
    "nikolaus", "adventskalender",
]

for kw, vol in sorted(filtered.items(), key=lambda x: x[1], reverse=True):
    categorized = False

    # Konkurrenz-Serien zuerst (damit "1000 gefahren" nicht in Spielbuch landet)
    for pattern in konkurrenz_serien:
        if pattern in kw:
            # "1000 gefahren" ist AUCH Spielbuch — in beide? Nein, in Konkurrenz
            categories["E_Konkurrenz_Serien"].append((kw, vol))
            categorized = True
            break
    if categorized:
        continue

    # Spielbuch/CYOA
    for pattern in spielbuch_patterns:
        if pattern in kw:
            categories["A_Spielbuch_CYOA"].append((kw, vol))
            categorized = True
            break
    if categorized:
        continue

    # Geschenk (nur mit Alter 7-10)
    for pattern in geschenk_patterns:
        if pattern in kw:
            has_target_age = any(a in kw for a in [
                "7 jahre", "8 jahre", "9 jahre", "10 jahre",
                "7 jähri", "8 jähri", "9 jähri", "10 jähri",
            ])
            has_book = any(b in kw for b in ["buch", "bücher"])
            if has_target_age or has_book:
                categories["F_Geschenk"].append((kw, vol))
                categorized = True
            break
    if categorized:
        continue

    # Escape/Rätsel
    for pattern in escape_patterns:
        if pattern in kw:
            categories["B_Escape_Raetsel"].append((kw, vol))
            categorized = True
            break
    if categorized:
        continue

    # Detektiv/Krimi
    for pattern in detektiv_patterns:
        if pattern in kw:
            categories["C_Detektiv_Krimi"].append((kw, vol))
            categorized = True
            break
    if categorized:
        continue

    # Lesemotivation
    for pattern in lesemotivation_patterns:
        if pattern in kw:
            categories["D_Lesemotivation"].append((kw, vol))
            categorized = True
            break
    if categorized:
        continue

    # Rest — nur behalten wenn Buch/Kind-Bezug
    has_book = any(b in kw for b in [
        "buch", "bücher", "lesen", "lese", "geschichte", "roman", "band ",
    ])
    has_kid = any(k in kw for k in [
        "kinder", "kids", "junge", "mädchen", "ab 8", "ab 9", "ab 10", "ab 7",
        "jahre", "klasse",
    ])
    if has_book or has_kid:
        if len(kw.split()) >= 3:
            categories["G_LongTail"].append((kw, vol))
        else:
            categories["Z_Unsicher"].append((kw, vol))

# === 3b. Manuelle Ergaenzungen (bewiesene/erwartete Top-Keywords) ===
manual_additions = [
    # Spielbuch/CYOA
    ("spielbuch kinder ab 8", 100),
    ("spielbuch kinder ab 10", 100),
    ("spielbuch detektiv kinder", 80),
    ("interaktives detektivbuch kinder", 80),
    ("buch du entscheidest kinder", 80),
    ("kinderbuch du entscheidest", 80),
    ("abenteuer spielbuch kinder ab 8", 80),
    ("buch mit mehreren enden kinder", 80),
    ("buch wo man entscheidet kinder", 80),
    # Escape/Mitmach
    ("escape buch kinder ab 8", 80),
    ("escape room buch kinder ab 8", 80),
    ("mitmachkrimi kinder ab 8", 80),
    ("ratekrimi kinder ab 8", 80),
    ("detektiv rätsel kinder", 80),
    # Lesemuffel
    ("buch für jungs die nicht gerne lesen", 60),
    ("bücher für lesemuffel", 60),
    ("spannendes kinderbuch ab 8", 80),
    ("spannendes buch für kinder ab 8", 80),
]

for kw, vol in manual_additions:
    already_exists = any(kw == existing[0] for cat in categories.values() for existing in cat)
    if not already_exists:
        # Categorize
        if any(p in kw for p in spielbuch_patterns):
            categories["A_Spielbuch_CYOA"].append((kw, vol))
        elif any(p in kw for p in escape_patterns):
            categories["B_Escape_Raetsel"].append((kw, vol))
        elif any(p in kw for p in detektiv_patterns):
            categories["C_Detektiv_Krimi"].append((kw, vol))
        elif any(p in kw for p in lesemotivation_patterns):
            categories["D_Lesemotivation"].append((kw, vol))
        else:
            categories["G_LongTail"].append((kw, vol))

# === 4. Output ===
output_file = Path(r"c:\Users\krugb\OneDrive\Desktop\GMBH\Projekte\Buecher\Die_Herrenhaus_Detektive\keyword_liste_interaktiv.md")

campaign_info = {
    "A_Spielbuch_CYOA": "Kampagne 1: Exact Match, Gebot 0,12 EUR — Kernzielgruppe Spielbuch-Kaeufer",
    "B_Escape_Raetsel": "Kampagne 2: Broad Match, Gebot 0,07 EUR — Escape/Raetsel-Liebhaber",
    "C_Detektiv_Krimi": "Kampagne 2: Broad Match, Gebot 0,07 EUR — Detektiv/Krimi Genre",
    "D_Lesemotivation": "Kampagne 3: Broad Match, Gebot 0,05 EUR — Eltern suchen Lesemotivation",
    "E_Konkurrenz_Serien": "Kampagne 4: Broad/Product Targeting, Gebot 0,10 EUR — Auf Konkurrenz-Seiten",
    "F_Geschenk": "Kampagne 5: Broad Match, Gebot 0,05 EUR — Geschenk-Sucher",
    "G_LongTail": "Kampagne 6: Phrase Match, Gebot 0,06 EUR — Nischen-Keywords",
    "Z_Unsicher": "Manuell pruefen — relevante in andere Kategorien verschieben",
}

with open(output_file, "w", encoding="utf-8") as f:
    f.write("# Keyword-Liste: Band 1 INTERAKTIV (Spielbuch)\n\n")
    f.write("Erstellt: 2026-03-11\n")
    f.write(f"Quelle: Magnet ({len(magnet_keywords)} KW)\n")
    f.write(f"Nach Filterung: {len(filtered)} Keywords\n\n")

    for cat_name, keywords in categories.items():
        if not keywords:
            continue
        keywords.sort(key=lambda x: x[1], reverse=True)

        f.write(f"---\n\n## {cat_name} ({len(keywords)} Keywords)\n")
        f.write(f"**{campaign_info.get(cat_name, '')}**\n\n")
        f.write("| Keyword | Suchvolumen |\n")
        f.write("|---|---|\n")
        for kw, vol in keywords:
            f.write(f"| {kw} | {vol} |\n")
        f.write("\n")

    total = sum(len(v) for v in categories.values())
    f.write("---\n\n## Zusammenfassung\n\n")
    for cat_name, keywords in categories.items():
        f.write(f"- **{cat_name}**: {len(keywords)} Keywords\n")
    f.write(f"- **Gesamt**: {total} Keywords\n")

print(f"\nOK: Keyword-Liste geschrieben: {output_file}")
print(f"\nZusammenfassung:")
for cat_name, keywords in categories.items():
    print(f"  {cat_name}: {len(keywords)} Keywords")
print(f"  GESAMT: {sum(len(v) for v in categories.values())}")
