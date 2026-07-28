"""
Erstellt ein KDP-fertiges Word-Dokument aus den Markdown-Kapiteldateien fuer Band 4.
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
OUTPUT_FILE = os.path.join(BASE_DIR, "Manuskript.docx")

# Rezensions-QR-Code (fuehrt direkt zum Amazon-Bewertungsformular).
# Erzeugt + gegengelesen von ../../build_qr_rezension.py (ASIN B0HBWVMTS2).
QR_REZENSION = os.path.join(BASE_DIR, "..", "Cover", "qr_rezension_band4.png")

# KDP Taschenbuch 6x9 Zoll (15.24 x 22.86 cm) - wie Band 2
PAGE_WIDTH = Cm(15.24)
PAGE_HEIGHT = Cm(22.86)

# Kapitel-Dateinamen in der richtigen Reihenfolge
CHAPTER_FILES = [
    f"Die_Herrenhaus_Detektive_Band4_Kapitel{i}.md" for i in range(1, 20)
]

# Kapiteltitel
CHAPTER_TITLES = {
    1: "Der Brief",
    2: "Der Mann, der vierzig Jahre gesucht hat",
    3: "Der Graue See",
    4: "Die erste Regel am See",
    5: "Drei Wellen und ein Stern",
    6: "Die Frau, die die Geschichte hütet",
    7: "Der Weg über den Hang",
    8: "Vier Häuser",
    9: "Die, die geblieben ist",
    10: "Waffenstillstand",
    11: "Das fünfte Haus",
    12: "Das Andenken",
    13: "Was ein Pfand ist",
    14: "Die Mühle",
    15: "Was Nele wusste",
    16: "Die Namen auf den Steinen",
    17: "Der Stein",
    18: "Was man zurückgibt",
    19: "Zurück in Eichenhain",
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

    # Heading 1 Style = Kapiteltitel (Kindle erkennt Heading 1 als Kapitel).
    # Muster A: groesser (17pt) und mehr Luft nach unten (22pt).
    h1_style = doc.styles['Heading 1']
    h1_font = h1_style.font
    h1_font.name = 'Georgia'
    h1_font.size = Pt(17)
    h1_font.bold = True
    h1_font.color.rgb = RGBColor(0, 0, 0)
    h1_format = h1_style.paragraph_format
    h1_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h1_format.space_before = Pt(0)
    h1_format.space_after = Pt(22)
    h1_format.page_break_before = False  # Wir machen den Seitenumbruch manuell

    # Heading 2 Style = Kapitelnummer (gesperrte graue Versalien, Muster A).
    h2_style = doc.styles['Heading 2']
    h2_font = h2_style.font
    h2_font.name = 'Georgia'
    h2_font.size = Pt(11)
    h2_font.bold = False
    h2_font.color.rgb = RGBColor(90, 90, 90)
    h2_format = h2_style.paragraph_format
    h2_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h2_format.space_before = Pt(0)
    h2_format.space_after = Pt(14)

    # Seitenformat (5x8 Zoll)
    section = doc.sections[0]
    section.page_width = PAGE_WIDTH
    section.page_height = PAGE_HEIGHT
    section.top_margin = Cm(1.6)
    section.bottom_margin = Cm(1.6)
    # Innen (Buchruecken): groesser wegen Bindung, Aussen: kleiner
    section.left_margin = Cm(2.0)   # Innenseite (Gutter)
    section.right_margin = Cm(1.3)  # Aussenseite

    # Spiegel-Raender aktivieren (gerade/ungerade Seiten spiegeln)
    doc.settings.element.append(OxmlElement('w:mirrorMargins'))

    return doc


def add_bookmark(paragraph, bookmark_name):
    """Fuegt einen Bookmark zu einem Absatz hinzu (fuer TOC-Verlinkung)."""
    bookmark_start = OxmlElement('w:bookmarkStart')
    bookmark_start.set(qn('w:id'), str(hash(bookmark_name) % 100000))
    bookmark_start.set(qn('w:name'), bookmark_name)

    bookmark_end = OxmlElement('w:bookmarkEnd')
    bookmark_end.set(qn('w:id'), str(hash(bookmark_name) % 100000))

    paragraph._p.insert(0, bookmark_start)
    paragraph._p.append(bookmark_end)


def add_hyperlink(paragraph, bookmark_name, text, font_name='Georgia', font_size=Pt(10)):
    """Fuegt einen internen Hyperlink (zu einem Bookmark) in einen Absatz ein."""
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('w:anchor'), bookmark_name)

    run_element = OxmlElement('w:r')

    rPr = OxmlElement('w:rPr')
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rPr.append(rFonts)

    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), str(int(font_size.pt * 2)))
    rPr.append(sz)

    run_element.append(rPr)

    text_element = OxmlElement('w:t')
    text_element.text = text
    text_element.set(qn('xml:space'), 'preserve')
    run_element.append(text_element)

    hyperlink.append(run_element)
    paragraph._p.append(hyperlink)


def add_page_break(doc):
    """Fuegt einen Seitenumbruch ein."""
    doc.add_page_break()


def set_tracking(run, points):
    """Sperrung (letter-spacing) in Punkten auf einen Run legen."""
    rpr = run._element.get_or_add_rPr()
    sp = OxmlElement('w:spacing')
    sp.set(qn('w:val'), str(int(points * 20)))  # Wert in Twips (1/20 pt)
    rpr.append(sp)


def add_title_page(doc):
    """Erstellt die Titelseite."""
    # Leerraum oben
    for _ in range(6):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(16)

    # Serientitel
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Die Herrenhaus-Detektive")
    run.font.size = Pt(22)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.line_spacing = Pt(32)
    p.paragraph_format.space_after = Pt(24)

    # Band
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Band 4")
    run.font.size = Pt(14)
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(36)

    # Buchtitel
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Das versunkene Dorf")
    run.font.size = Pt(18)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.line_spacing = Pt(28)
    p.paragraph_format.space_after = Pt(60)

    # Leerraum
    for _ in range(3):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(16)

    # Autor
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Benjamin Krug")
    run.font.size = Pt(14)
    run.font.name = 'Georgia'


def add_impressum_page(doc):
    """Erstellt die Impressum-Seite."""
    add_page_break(doc)

    for _ in range(2):
        doc.add_paragraph()

    lines = [
        "Die Herrenhaus-Detektive, Band 4: Das versunkene Dorf",
        "",
        "© 2026 Benjamin Krug",
        "Alle Rechte vorbehalten.",
        "",
        "Independently published",
        "",
        "ISBN: ###ISBN_BAND4###",
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
    """Erstellt die Widmungsseite."""
    add_page_break(doc)

    for _ in range(6):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(
        "Für alle, die etwas zurückgeben —\n"
        "auch wenn es lange her ist."
    )
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.name = 'Georgia'


def add_table_of_contents(doc):
    """Erstellt das Inhaltsverzeichnis mit klickbaren Hyperlinks."""
    add_page_break(doc)

    # Ueberschrift
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Inhalt")
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(18)

    # Kapiteleintraege als Hyperlinks
    for i in range(1, 20):
        title = CHAPTER_TITLES.get(i, f"Kapitel {i}")
        if i == 19:
            label = f"Epilog — {title}"
        else:
            label = f"Kapitel {i} — {title}"

        bookmark_name = f"kapitel_{i}"

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        add_hyperlink(p, bookmark_name, label)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Cm(0.5)


def parse_markdown_chapter(filepath):
    """Liest eine Markdown-Kapiteldatei und gibt den reinen Text zurueck."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Entferne die Buch-Header (# Die Herrenhaus-Detektive, ## Band X, ---)
    lines = content.split('\n')
    chapter_started = False
    chapter_lines = []

    for line in lines:
        # Suche nach der Kapitel-Ueberschrift
        if line.startswith('# Kapitel') or line.startswith('# Epilog'):
            chapter_started = True
            continue  # Ueberschrift ueberspringen (wird separat formatiert)

        if chapter_started:
            # Stoppe vor Schluss-Markierungen am Dateiende
            stripped = line.strip()
            if (stripped.startswith('*Ende von Band')
                    or stripped.startswith('*Die Herrenhaus-Detektive kehren')):
                continue
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

    # "Sink": echter Leerraum-Absatz, damit der Kapitelkopf nach unten einrueckt
    # (~2,5 cm). Bewusst NICHT ueber space_before der ersten Zeile geloest --
    # Word verwirft Abstand am Seitenanfang. Der leere Absatz wird zuverlaessig
    # gedruckt.
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_before = Pt(0)
    spacer.paragraph_format.space_after = Pt(56)

    # Kapitelnummer (Heading 2): gesperrte graue Versalien
    if chapter_num == 19:
        label = "EPILOG"
    else:
        label = f"KAPITEL {chapter_num}"

    p = doc.add_heading(label, level=2)
    if p.runs:
        set_tracking(p.runs[0], 2.6)

    # Kapiteltitel als Heading 1 mit Bookmark (fuer navigierbares TOC)
    bookmark_name = f"kapitel_{chapter_num}"
    p = doc.add_heading(title, level=1)
    add_bookmark(p, bookmark_name)

    # Kapitelinhalt - Zeilen zu Absatzgruppen zusammenfassen
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
    is_first = True

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
            is_first = True
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
    """Erstellt die emotionale Schlussseite mit Dank und Ueberleitung zu Band 4."""
    add_page_break(doc)

    for _ in range(3):
        doc.add_paragraph()

    # Ende-Markierung
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Ende von Band 4")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(30)

    # Emotionaler Moment — direkte Ansprache
    lines = [
        "Hat dir das Buch gefallen?",
        "",
        "Jonas, Mila und Ben sind vierhundert Kilometer weit gefahren.",
        "Sie haben Sternbach gefunden, bevor das Wasser zurückkam.",
        "Die Münze liegt jetzt da, wo sie hingehört.",
        "Dreihundert Jahre zu spät — aber sie liegt da.",
        "",
        "Vier Mulden waren in den Stein gehauen.",
        "Zwei sind gefüllt.",
        "",
        "Und über der Haustür in Eichenhain sitzen vier Zeichen im Stein.",
        "Baum. Kreuz. Ring. Blume.",
        "",
        "Fünf Familien haben in Sternbach gewohnt.",
        "",
        "Bist du bereit, die nächste Seite umzublättern?",
    ]

    for line in lines:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if line:
            run = p.add_run(line)
            run.font.size = Pt(12)
            run.font.name = 'Georgia'
            if line == "Hat dir das Buch gefallen?":
                run.font.bold = True
                run.font.size = Pt(14)
            if line == "Bist du bereit, die nächste Seite umzublättern?":
                run.font.bold = True
                run.font.italic = True
        p.paragraph_format.space_after = Pt(2)


def add_review_request_page(doc):
    """Erstellt die Rezensions-Bitte-Seite."""
    add_page_break(doc)

    for _ in range(2):
        doc.add_paragraph()

    # Ueberschrift
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Eine kleine Bitte")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(6)

    # Sternchen-Deko
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("★ ★ ★ ★ ★")
    run.font.size = Pt(14)
    run.font.name = 'Georgia'
    run.font.color.rgb = RGBColor(200, 160, 50)
    p.paragraph_format.space_after = Pt(20)

    # Text der Bitte
    review_lines = [
        ("Wenn dir das Buch gefallen hat, würde ich mich riesig "
         "über eine kurze Bewertung auf Amazon freuen."),
        "",
        ("Ein paar Worte reichen völlig — zum Beispiel, was dir am besten "
         "gefallen hat oder welche Figur dein Liebling ist."),
        "",
        ("Jede Bewertung hilft mir, noch mehr Abenteuer "
         "für dich zu schreiben!"),
    ]

    for line in review_lines:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if line:
            run = p.add_run(line)
            run.font.size = Pt(11)
            run.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Cm(1.0)
        p.paragraph_format.right_indent = Cm(1.0)

    # QR-Code direkt zum Amazon-Bewertungsformular
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Einfach den Code scannen und eine Bewertung dalassen:")
    run.font.size = Pt(11)
    run.font.italic = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(8)

    if os.path.isfile(QR_REZENSION):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        # Normal-Stil hat EXAKTEN Zeilenabstand (Pt(14)) -- wuerde das Bild
        # abschneiden. Fuer den Bild-Absatz auf einfachen Zeilenabstand.
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        p.add_run().add_picture(QR_REZENSION, width=Inches(1.5))

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run("(Handykamera auf den Code halten – "
                        "der Link öffnet sich von selbst.)")
        run.font.size = Pt(9)
        run.font.italic = True
        run.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(10)
    else:
        print(f"  WARNUNG: QR-Code nicht gefunden: {QR_REZENSION}")

    # Abschluss
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Danke! ❤")
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(10)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("— Benjamin")
    run.font.size = Pt(11)
    run.font.italic = True
    run.font.name = 'Georgia'


def add_band5_teaser(doc):
    """Erstellt die Vorschau fuer Band 5."""
    add_page_break(doc)

    doc.add_paragraph()

    # Ueberschrift
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Vorschau")
    run.font.size = Pt(11)
    run.font.name = 'Georgia'
    run.font.color.rgb = RGBColor(100, 100, 100)
    p.paragraph_format.space_after = Pt(4)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Die Herrenhaus-Detektive, Band 5")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(20)

    # Atmosphaerischer Teaser-Text
    teaser_lines = [
        "Jonas' Tasche ist leer.",
        "Zum ersten Mal seit einem Jahr.",
        "",
        "Vier Familien sind aus Sternbach fortgegangen.",
        "Jede nahm eine Münze mit.",
        "Eine davon liegt jetzt wieder im Stein.",
        "",
        "Drei sind noch irgendwo.",
        "",
        "Und über der Haustür des Herrenhauses",
        "sitzen vier Zeichen im Stein.",
        "Baum. Kreuz. Ring. Blume.",
        "",
        "Fünf Familien haben in Sternbach gewohnt.",
        "Da müssten eigentlich fünf sein.",
        "",
        "Manche Geschichten enden nicht.",
        "Sie warten nur auf jemanden,",
        "der mutig genug ist, die nächste Seite umzublättern.",
    ]

    for line in teaser_lines:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if line:
            run = p.add_run(line)
            run.font.size = Pt(11)
            run.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.left_indent = Cm(0.8)
        p.paragraph_format.right_indent = Cm(0.8)

    # Szenen-Trenner
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("* * *")
    run.font.size = Pt(11)
    run.font.name = 'Georgia'
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(14)

    # Hook-Fragen
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(
        "Wo sind die drei anderen Münzen?\n"
        "Wem gehört das fünfte Zeichen?\n"
        "Und wozu wurde Eichenhain wirklich gegründet?"
    )
    run.font.size = Pt(11)
    run.font.name = 'Georgia'
    run.font.italic = True
    p.paragraph_format.space_after = Pt(16)

    # Call to Action
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Die Herrenhaus-Detektive, Band 5")
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(4)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Erscheint bald!")
    run.font.size = Pt(12)
    run.font.name = 'Georgia'
    run.font.bold = True


def _add_series_block(doc, title, description, band_info=None):
    """Hilfsfunktion: Fuegt einen Serien-Block zur Uebersicht hinzu."""
    # Serientitel
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(title)
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(6)

    # Beschreibung
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(description)
    run.font.size = Pt(10)
    run.font.name = 'Georgia'
    run.font.italic = True
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.left_indent = Cm(0.8)
    p.paragraph_format.right_indent = Cm(0.8)

    # Bandliste (optional)
    if band_info:
        for band in band_info:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(band)
            run.font.size = Pt(10)
            run.font.name = 'Georgia'
            p.paragraph_format.space_after = Pt(2)


def add_series_overview_page(doc):
    """Erstellt die Serienuebersicht mit Cross-Verweisen."""
    add_page_break(doc)

    doc.add_paragraph()

    # Seitentitel
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Mehr Abenteuer von Benjamin Krug")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(20)

    # --- Serie 1: Die Herrenhaus-Detektive ---
    _add_series_block(
        doc,
        "Die Herrenhaus-Detektive",
        "Niemand darf das alte Herrenhaus betreten. "
        "Aber Jonas, Mila und Ben finden einen Schlüssel — "
        "und hinter der verschlossenen Tür wartet ein Geheimnis, "
        "das seit dreißig Jahren niemand lüften durfte. "
        "Spannendes Detektivabenteuer ab 8 Jahren.",
        band_info=[
            "Band 1: Das verbotene Herrenhaus",
            "Band 2: Das Geheimnis des Brunnens",
            "Band 3: Die zweite Quelle",
            "Band 4: Das versunkene Dorf",
            "Band 5: Erscheint bald!",
        ],
    )

    # Trenner
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("— — —")
    run.font.size = Pt(10)
    run.font.name = 'Georgia'
    run.font.color.rgb = RGBColor(150, 150, 150)
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(10)

    # --- Serie 2: Die Chrono-Agenten ---
    _add_series_block(
        doc,
        "Die Chrono-Agenten",
        "Drei Kinder. Ein Tablet, das die Zeit öffnet. "
        "Und ein Countdown, der nicht aufhört zu laufen. "
        "Leo, Mila und Ben sind Agenten wider Willen — "
        "geschickt in die gefährlichsten Momente der Geschichte, "
        "um zu retten, was jemand zerstören will. "
        "Ihr Gegner heißt Codex. Und er kennt ihre Namen. "
        "Für alle, die Geschichte spannend finden — "
        "und wissen wollen, was passiert, wenn man sie verändert.",
    )

    # Trenner
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("— — —")
    run.font.size = Pt(10)
    run.font.name = 'Georgia'
    run.font.color.rgb = RGBColor(150, 150, 150)
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(10)

    # --- Serie 3: Die Geisterspuerer ---
    _add_series_block(
        doc,
        "Die Geisterspürer",
        "In Gravenstedt sind die Toten nicht still. "
        "Nora (12) und Theo (10) ziehen in eine alte Wohnung — "
        "und finden einen Hund, der Geister spürt. "
        "Jetzt müssen sie die Wahrheit hinter einer "
        "zweihundert Jahre alten Lüge aufdecken. "
        "Bevor es zu spät ist. "
        "Gruselig-lustiges Abenteuer ab 10 Jahren.",
        band_info=[
            "Band 1: Das Haus, das flüstert",
        ],
    )

    # Abschluss
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Alle Bücher auf Amazon erhältlich!")
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.name = 'Georgia'


def main():
    print("Erstelle KDP-Manuskript fuer Band 4...")
    doc = setup_document()

    # 1. Titelseite
    print("  Titelseite")
    add_title_page(doc)

    # 2. Impressum
    print("  Impressum")
    add_impressum_page(doc)

    # 3. Widmung
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

    # 6. Ende-Seite (emotionaler Moment)
    print("  Ende-Seite")
    add_end_page(doc)

    # 7. Rezensions-Bitte
    print("  Rezensions-Bitte")
    add_review_request_page(doc)

    # 8. Band 5 Vorschau
    print("  Band 5 Vorschau")
    add_band5_teaser(doc)

    # 9. Serienuebersicht
    print("  Serienuebersicht")
    add_series_overview_page(doc)

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
