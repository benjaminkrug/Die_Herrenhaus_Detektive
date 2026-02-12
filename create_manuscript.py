"""
Erstellt ein KDP-fertiges Word-Dokument aus den Markdown-Kapiteldateien.
"""
import re
import os
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Pfade
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KAPITEL_DIR = os.path.join(BASE_DIR, "Kapitel")
OUTPUT_FILE = os.path.join(BASE_DIR, "Die_Herrenhaus_Detektive_Band1_Manuskript.docx")

# KDP Taschenbuch 5x8 Zoll (12.7 x 20.32 cm) - Kinderbuchformat
PAGE_WIDTH = Cm(12.7)
PAGE_HEIGHT = Cm(20.32)

# Kapitel-Dateinamen in der richtigen Reihenfolge
CHAPTER_FILES = [
    f"Die_Herrenhaus_Detektive_Band1_Kapitel{i}.md" for i in range(1, 20)
]

# Kapiteltitel
CHAPTER_TITLES = {
    1: "Der Blick zum Hügel",
    2: "Das alte Gerücht",
    3: "Der erste Beweis",
    4: "Das verbotene Tor",
    5: "Die geheime Botschaft",
    6: "Das knarrende Treppenhaus",
    7: "Die falsche Spur",
    8: "Das Rätsel der Symbole",
    9: "Die nächtliche Begegnung",
    10: "Der Verdächtige",
    11: "Die geheime Karte",
    12: "Der verschlossene Keller",
    13: "Eingeschlossen",
    14: "Die Wahrheit über den Spuk",
    15: "Belauscht",
    16: "Die ganze Wahrheit",
    17: "Der letzte Wille",
    18: "Meiers Geschichte",
    19: "Ein neues Geheimnis",
}


def setup_document():
    """Erstellt das Dokument mit KDP-Formatierung."""
    doc = Document()

    # Standard-Style anpassen
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Georgia'
    font.size = Pt(11)
    font.color.rgb = RGBColor(0, 0, 0)

    paragraph_format = style.paragraph_format
    paragraph_format.space_before = Pt(0)
    paragraph_format.space_after = Pt(0)
    paragraph_format.line_spacing = Pt(14)

    # Seitenformat (5x8 Zoll)
    section = doc.sections[0]
    section.page_width = PAGE_WIDTH
    section.page_height = PAGE_HEIGHT
    section.top_margin = Cm(1.6)
    section.bottom_margin = Cm(1.6)
    # Innen (Buchrücken): groesser wegen Bindung, Aussen: kleiner
    section.left_margin = Cm(2.0)   # Innenseite (Gutter)
    section.right_margin = Cm(1.3)  # Aussenseite

    # Spiegel-Raender aktivieren (gerade/ungerade Seiten spiegeln)
    doc.settings.element.append(OxmlElement('w:mirrorMargins'))

    return doc


def add_page_break(doc):
    """Fuegt einen Seitenumbruch ein."""
    doc.add_page_break()


def add_title_page(doc):
    """Erstellt die Titelseite."""
    # Leerraum oben
    for _ in range(4):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(12)

    # Serientitel
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Die Herrenhaus-Detektive")
    run.font.size = Pt(22)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(8)

    # Band
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Band 1")
    run.font.size = Pt(14)
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(20)

    # Buchtitel
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Das verbotene Herrenhaus")
    run.font.size = Pt(18)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(40)

    # Leerraum
    for _ in range(3):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(12)

    # Autor-Platzhalter
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("[AUTORENNAME]")
    run.font.size = Pt(14)
    run.font.name = 'Georgia'


def add_impressum_page(doc):
    """Erstellt die Impressum-Seite."""
    add_page_break(doc)

    for _ in range(2):
        doc.add_paragraph()

    lines = [
        "Die Herrenhaus-Detektive, Band 1: Das verbotene Herrenhaus",
        "",
        "\u00a9 [JAHR] [AUTORENNAME]",
        "Alle Rechte vorbehalten.",
        "",
        "Independently published",
        "",
        "Lektorat: [NAME]",
        "Korrektorat: [NAME]",
        "Coverdesign: [NAME]",
        "Satz und Layout: [NAME]",
        "",
        "ISBN: [ISBN-NUMMER]",
        "",
        "Dieses Buch ist ein Werk der Fiktion. Namen, Personen,",
        "Orte und Ereignisse sind frei erfunden. Jede \u00c4hnlichkeit",
        "mit tats\u00e4chlichen Personen, lebend oder verstorben,",
        "ist rein zuf\u00e4llig.",
    ]

    for line in lines:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        if line:
            run = p.add_run(line)
            run.font.size = Pt(8)
            run.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(2)


def add_dedication_page(doc):
    """Erstellt eine optionale Widmungsseite."""
    add_page_break(doc)

    for _ in range(6):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("[F\u00fcr ...]")
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.name = 'Georgia'


def add_table_of_contents(doc):
    """Erstellt das Inhaltsverzeichnis."""
    add_page_break(doc)

    # Ueberschrift
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Inhalt")
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(18)

    # Kapiteleintraege
    for i in range(1, 20):
        title = CHAPTER_TITLES.get(i, f"Kapitel {i}")
        if i == 19:
            label = f"Epilog \u2014 {title}"
        else:
            label = f"Kapitel {i} \u2014 {title}"

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(label)
        run.font.size = Pt(10)
        run.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Cm(0.5)


def parse_markdown_chapter(filepath):
    """Liest eine Markdown-Kapiteldatei und gibt den reinen Text zurueck."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Entferne die Buch-Header (# Die Herrenhaus-Detektive, ## Band 1, ---)
    lines = content.split('\n')
    chapter_started = False
    chapter_lines = []

    for line in lines:
        # Suche nach der Kapitel-Ueberschrift
        if line.startswith('# Kapitel') or line.startswith('# Epilog'):
            chapter_started = True
            continue  # Ueberschrift ueberspringen (wird separat formatiert)

        if chapter_started:
            chapter_lines.append(line)

    return '\n'.join(chapter_lines)


def add_text_to_paragraph(p, text):
    """Fuegt Text mit Kursiv-Erkennung zum Absatz hinzu."""
    parts = re.split(r'(\*[^*]+\*)', text)
    for part in parts:
        if part.startswith('*') and part.endswith('*') and len(part) > 2:
            run = p.add_run(part[1:-1])
            run.font.italic = True
            run.font.name = 'Georgia'
            run.font.size = Pt(11)
        else:
            run = p.add_run(part)
            run.font.name = 'Georgia'
            run.font.size = Pt(11)


def add_chapter(doc, chapter_num, title, content):
    """Fuegt ein Kapitel zum Dokument hinzu."""
    add_page_break(doc)

    # Leerraum oben (kompakt)
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(10)

    # Kapitelnummer
    if chapter_num == 19:
        label = "Epilog"
    else:
        label = f"Kapitel {chapter_num}"

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(label)
    run.font.size = Pt(11)
    run.font.name = 'Georgia'
    run.font.color.rgb = RGBColor(100, 100, 100)
    p.paragraph_format.space_after = Pt(2)

    # Kapiteltitel
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(title)
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(10)

    # Kapitelinhalt - Zeilen zu Absatzgruppen zusammenfassen
    # Leerzeilen im Markdown trennen Absatzgruppen
    # Zeilen INNERHALB einer Gruppe werden per Soft-Break (Shift+Enter)
    # in EINEN Word-Absatz gepackt -> drastisch weniger Absaetze
    lines = content.split('\n')

    # Zeilen in Gruppen aufteilen (getrennt durch Leerzeilen)
    groups = []
    current_group = []

    for line in lines:
        stripped = line.strip()

        if not stripped:
            if current_group:
                groups.append(current_group)
                current_group = []
            continue

        # Markdown-Header ueberspringen
        if stripped.startswith('#'):
            continue

        current_group.append(stripped)

    if current_group:
        groups.append(current_group)

    # Jede Gruppe als einen fliessenden Absatz ausgeben
    is_first = True  # Erster Absatz nach Kapitelstart: keine Einrueckung

    for group in groups:
        # Szenen-Trenner (---)
        if len(group) == 1 and group[0] == '---':
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run("* * *")
            run.font.size = Pt(11)
            run.font.name = 'Georgia'
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            is_first = True  # Nach Szenen-Trenner: naechster Absatz ohne Einrueckung
            continue

        # Zeilen zu Fliesstext zusammenfuegen
        joined_text = " ".join(group)

        # Absatz erstellen
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(0)

        add_text_to_paragraph(p, joined_text)
        is_first = False


def add_end_page(doc):
    """Erstellt die Schlussseite."""
    add_page_break(doc)

    for _ in range(5):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Ende von Band 1")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(20)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Die Herrenhaus-Detektive kehren zur\u00fcck in")
    run.font.size = Pt(11)
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(8)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Band 2: [Titel]")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.italic = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(20)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Danke f\u00fcrs Lesen!")
    run.font.size = Pt(12)
    run.font.name = 'Georgia'


def add_about_author_page(doc):
    """Erstellt die Ueber-den-Autor-Seite."""
    add_page_break(doc)

    for _ in range(3):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\u00dcber den Autor")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(20)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("[Hier kommt deine Autorenbeschreibung hin.]")
    run.font.size = Pt(11)
    run.font.italic = True
    run.font.name = 'Georgia'


def main():
    print("Erstelle KDP-Manuskript...")
    doc = setup_document()

    # 1. Titelseite
    print("  Titelseite")
    add_title_page(doc)

    # 2. Impressum
    print("  Impressum")
    add_impressum_page(doc)

    # 3. Widmung (optional)
    print("  Widmung")
    add_dedication_page(doc)

    # 4. Inhaltsverzeichnis
    print("  Inhaltsverzeichnis")
    add_table_of_contents(doc)

    # 5. Kapitel
    for i, filename in enumerate(CHAPTER_FILES, 1):
        filepath = os.path.join(KAPITEL_DIR, filename)
        if not os.path.exists(filepath):
            print(f"  {filename} nicht gefunden, ueberspringe...")
            continue

        title = CHAPTER_TITLES.get(i, f"Kapitel {i}")
        print(f"  Kapitel {i}: {title}")

        content = parse_markdown_chapter(filepath)
        add_chapter(doc, i, title, content)

    # 6. Ende-Seite
    print("  Ende-Seite")
    add_end_page(doc)

    # 7. Ueber den Autor
    print("  Ueber den Autor")
    add_about_author_page(doc)

    # Speichern
    doc.save(OUTPUT_FILE)
    print(f"\nManuskript erstellt: {OUTPUT_FILE}")

    # Statistiken
    total_words = 0
    for i, filename in enumerate(CHAPTER_FILES, 1):
        filepath = os.path.join(KAPITEL_DIR, filename)
        if os.path.exists(filepath):
            content = parse_markdown_chapter(filepath)
            words = len(content.split())
            total_words += words
            print(f"  Kapitel {i:2d}: ~{words:,} Woerter")

    print(f"\n  Gesamt: ~{total_words:,} Woerter in 19 Kapiteln")


if __name__ == "__main__":
    main()
