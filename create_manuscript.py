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

# KDP Taschenbuch 5x8 Zoll (12.7 x 20.32 cm) - gängiges Kinderbuchformat
PAGE_WIDTH = Cm(12.7)
PAGE_HEIGHT = Cm(20.32)

# Kapitel-Dateinamen in der richtigen Reihenfolge
CHAPTER_FILES = [
    f"Die_Herrenhaus_Detektive_Band1_Kapitel{i}.md" for i in range(1, 20)
]

# Kapiteltitel extrahieren
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
    paragraph_format.space_after = Pt(4)
    paragraph_format.line_spacing = Pt(15)

    # Seitenformat (5x8 Zoll)
    section = doc.sections[0]
    section.page_width = PAGE_WIDTH
    section.page_height = PAGE_HEIGHT
    section.top_margin = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(1.8)
    section.right_margin = Cm(1.5)

    return doc


def add_page_break(doc):
    """Fügt einen Seitenumbruch ein."""
    doc.add_page_break()


def add_blank_page(doc):
    """Fügt eine leere Seite ein."""
    doc.add_page_break()
    p = doc.add_paragraph()
    p.text = ""


def add_title_page(doc):
    """Erstellt die Titelseite."""
    # Leerraum oben
    for _ in range(6):
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
    p.paragraph_format.space_after = Pt(24)

    # Buchtitel
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Das verbotene Herrenhaus")
    run.font.size = Pt(18)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(48)

    # Leerraum
    for _ in range(4):
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
        "© [JAHR] [AUTORENNAME]",
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
        "Orte und Ereignisse sind frei erfunden. Jede Ähnlichkeit",
        "mit tatsächlichen Personen, lebend oder verstorben,",
        "ist rein zufällig.",
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

    for _ in range(8):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("[Für ...]")
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.name = 'Georgia'


def add_table_of_contents(doc):
    """Erstellt das Inhaltsverzeichnis."""
    add_page_break(doc)

    # Überschrift
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Inhalt")
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(24)

    # Kapiteleinträge
    for i in range(1, 20):
        title = CHAPTER_TITLES.get(i, f"Kapitel {i}")
        if i == 19:
            label = f"Epilog — {title}"
        else:
            label = f"Kapitel {i} — {title}"

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(label)
        run.font.size = Pt(10)
        run.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.left_indent = Cm(0.5)


def parse_markdown_chapter(filepath):
    """Liest eine Markdown-Kapiteldatei und gibt den reinen Text zurück."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Entferne die Buch-Header (# Die Herrenhaus-Detektive, ## Band 1, ---)
    lines = content.split('\n')
    chapter_started = False
    chapter_lines = []

    for line in lines:
        # Suche nach der Kapitel-Überschrift
        if line.startswith('# Kapitel') or line.startswith('# Epilog'):
            chapter_started = True
            continue  # Überschrift überspringen (wird separat formatiert)

        if chapter_started:
            chapter_lines.append(line)

    return '\n'.join(chapter_lines)


def add_chapter(doc, chapter_num, title, content):
    """Fügt ein Kapitel zum Dokument hinzu."""
    add_page_break(doc)

    # Leerraum oben (ca. 1/3 Seite)
    for _ in range(4):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(8)

    # Kapitelnummer
    if chapter_num == 19:
        label = "Epilog"
    else:
        label = f"Kapitel {chapter_num}"

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(label)
    run.font.size = Pt(12)
    run.font.name = 'Georgia'
    run.font.color.rgb = RGBColor(100, 100, 100)
    p.paragraph_format.space_after = Pt(4)

    # Kapiteltitel
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(title)
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(24)

    # Kapitelinhalt
    paragraphs = content.split('\n')
    for para_text in paragraphs:
        para_text = para_text.strip()

        # Leerzeilen -> kleiner Abstand
        if not para_text:
            continue

        # Horizontale Trennlinien (---) als Szenen-Trenner
        if para_text == '---':
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run("* * *")
            run.font.size = Pt(11)
            run.font.name = 'Georgia'
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(12)
            continue

        # Markdown-Header innerhalb des Kapitels überspringen
        if para_text.startswith('#'):
            continue

        # Kursiv-Text behandeln (*text*)
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.first_line_indent = Cm(0.5)

        # Zerlege Text in kursive und normale Teile
        parts = re.split(r'(\*[^*]+\*)', para_text)
        for part in parts:
            if part.startswith('*') and part.endswith('*') and len(part) > 2:
                # Kursiver Text
                run = p.add_run(part[1:-1])
                run.font.italic = True
                run.font.name = 'Georgia'
                run.font.size = Pt(11)
            else:
                run = p.add_run(part)
                run.font.name = 'Georgia'
                run.font.size = Pt(11)

        # Dialog-Absätze: kein Einzug bei direkter Rede (beginnt mit „)
        if para_text.startswith('„') or para_text.startswith('"'):
            p.paragraph_format.first_line_indent = Cm(0.5)


def add_end_page(doc):
    """Erstellt die Schlussseite."""
    add_page_break(doc)

    for _ in range(6):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Ende von Band 1")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(24)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Die Herrenhaus-Detektive kehren zurück in")
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
    p.paragraph_format.space_after = Pt(24)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Danke fürs Lesen!")
    run.font.size = Pt(12)
    run.font.name = 'Georgia'


def add_about_author_page(doc):
    """Erstellt die Über-den-Autor-Seite."""
    add_page_break(doc)

    for _ in range(3):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Über den Autor")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(24)

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
