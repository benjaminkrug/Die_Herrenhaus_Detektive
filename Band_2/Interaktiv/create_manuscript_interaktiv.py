"""
Erstellt ein KDP-fertiges Word-Dokument aus den interaktiven Abschnitt-Dateien.
Serie: "Dein Fall -- Du entscheidest!"
Band 2: "Das Geheimnis des Brunnens"

Verwendung:
    python create_manuscript_interaktiv.py
"""
import re
import os
import random
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.section import WD_SECTION_START
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ============================================================
# Konfiguration
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ABSCHNITTE_DIR = os.path.join(BASE_DIR, "Abschnitte")
OUTPUT_FILE = os.path.join(BASE_DIR, "Dein_Fall_Du_entscheidest_Das_Geheimnis_des_Brunnens.docx")

PAGE_WIDTH = Cm(12.7)   # 5 Zoll
PAGE_HEIGHT = Cm(20.32)  # 8 Zoll

# Abschnitte durchmischen? (Print: True, damit Leser nicht einfach weiterblaettern)
SHUFFLE_SECTIONS = True

# Nummern-Mapping: Original-ID -> Neue (gescramblte) ID
# Wird in main() befuellt wenn SHUFFLE_SECTIONS = True
SECTION_MAP = {}

# Illustrationen
ILLUSTRATIONS_DIR = os.path.join(BASE_DIR, "Illustrationen")

# Mapping: Original-Abschnitt-ID -> Liste von Illustrations-Nummern
# Illustration 1 (Karte: Eichenhain mit Gangsystem) wird als eigene Seite vor den Abschnitten eingefuegt
ILLUSTRATION_MAP = {
    "1": [2],          # Ab. 1 (Start) -> Illustration 2 (Brief am Brunnen)
    "3": [3],          # Ab. 3 -> Illustration 3 (Geheimtinte)
    "7": [4],          # Ab. 7 (Entscheidungspunkt) -> Illustration 4 (Vier Wege)
    "11": [5],         # Ab. 11 (Metalltuer) -> Illustration 5 (Vier Symbole)
    "12": [6],         # Ab. 12 (Knopf leuchtet) -> Illustration 6 (Goldener Knopf)
    "17": [7],         # Ab. 17 (Hinab) -> Illustration 7 (Abstieg)
    "25b": [8],        # Ab. 25b (Brunnen-Kammer) -> Illustration 8
    "46": [9],         # Ab. 46 (Wasserfall) -> Illustration 9
    "47": [10],        # Ab. 47 (Wandmalereien) -> Illustration 10
    "79b": [11],       # Ab. 79b (Initialen) -> Illustration 11 (Frau Bergmann)
    "80": [12],        # Ab. 80 (Truhe) -> Illustration 12
    "93": [13],        # Ab. 93 (Winters Anruf) -> Illustration 13
    "56": [14],        # Ab. 56 (Brunnen fliesst) -> Illustration 14
    "200": [15],       # Ab. 200 (Geheim-Ende) -> Illustration 15 (Winters Rueckkehr)
}

ILLUSTRATION_WIDTH = Cm(8.0)


# ============================================================
# Hilfsfunktionen
# ============================================================

def get_section_files():
    """Findet alle Abschnitt-Dateien und gibt sie sortiert zurueck."""
    files = []
    for f in os.listdir(ABSCHNITTE_DIR):
        if f.startswith("Abschnitt_") and f.endswith(".md"):
            files.append(f)

    def sort_key(filename):
        name = filename.replace("Abschnitt_", "").replace(".md", "")
        if name == "00_Einleitung":
            return (-1, "")
        match = re.match(r"(\d+)(\w*)", name)
        if match:
            return (int(match.group(1)), match.group(2))
        return (999, name)

    files.sort(key=sort_key)
    return files


def section_id_from_filename(filename):
    """Extrahiert die Abschnitt-ID aus dem Dateinamen (z.B. '7', '43b').
    Fuehrende Nullen werden entfernt (01 -> 1, 07 -> 7)."""
    name = filename.replace("Abschnitt_", "").replace(".md", "")
    if name == "00_Einleitung":
        return "einleitung"
    # Fuehrende Nullen entfernen fuer konsistente IDs
    match = re.match(r'0*(\d+\w*)', name)
    if match:
        return match.group(1)
    return name


def bookmark_for(section_id):
    """Erzeugt einen Bookmark-Namen fuer eine Abschnitt-ID."""
    return f"abschnitt_{section_id}"


def create_section_mapping(section_files):
    """Erstellt ein deterministisches Mapping: Original-ID -> Neue Nummer.

    Abschnitt 1 bleibt als 1 (wird in der Einleitung referenziert).
    Alle anderen bekommen neue, durchgemischte Nummern (2..N).
    Sub-Abschnitte (16b, 26b, 43b etc.) bekommen einfache Nummern.
    """
    all_ids = []
    for f in section_files:
        sid = section_id_from_filename(f)
        if sid != "einleitung":
            all_ids.append(sid)

    other_ids = [sid for sid in all_ids if sid != "1"]

    # Sortiere deterministisch (Zahl, dann Buchstabe)
    def id_sort_key(sid):
        m = re.match(r'(\d+)(\w*)', sid)
        return (int(m.group(1)), m.group(2)) if m else (999, sid)

    other_ids.sort(key=id_sort_key)

    # Neue Nummern: 2 bis N+1
    new_numbers = list(range(2, len(other_ids) + 2))

    # Deterministisch mischen (fester Seed fuer Reproduzierbarkeit)
    rng = random.Random(2027)
    rng.shuffle(new_numbers)

    mapping = {"1": "1"}
    for old_id, new_num in zip(other_ids, new_numbers):
        mapping[old_id] = str(new_num)

    return mapping


def map_section_id(old_id):
    """Gibt die gescramblte Abschnitt-Nummer zurueck."""
    if not SHUFFLE_SECTIONS or not SECTION_MAP:
        return old_id
    return SECTION_MAP.get(old_id, old_id)


def replace_section_numbers(text):
    """Ersetzt alle 'Abschnitt X' im Text durch gescramblte Nummern."""
    if not SHUFFLE_SECTIONS or not SECTION_MAP:
        return text

    def replacer(m):
        old_id = m.group(1)
        new_id = map_section_id(old_id)
        return f"Abschnitt {new_id}"

    return re.sub(r'Abschnitt\s+(\d+\w?)', replacer, text)


def get_illustration_path(number):
    """Gibt den Dateipfad fuer eine Illustrations-Nummer zurueck."""
    # Mit Leerzeichen (Standard: "Illustration 1.png")
    path = os.path.join(ILLUSTRATIONS_DIR, f"Illustration {number}.png")
    if os.path.exists(path):
        return path
    # Ohne Leerzeichen (z.B. "Illustration13.png")
    path = os.path.join(ILLUSTRATIONS_DIR, f"Illustration{number}.png")
    if os.path.exists(path):
        return path
    return None


def add_illustration(doc, number):
    """Fuegt eine Illustration zentriert ins Dokument ein."""
    path = get_illustration_path(number)
    if not path:
        print(f"    WARNUNG: Illustration {number} nicht gefunden!")
        return

    doc.add_picture(path, width=ILLUSTRATION_WIDTH)
    pic_para = doc.paragraphs[-1]
    # KRITISCH: Line Spacing auf SINGLE setzen, sonst clippt Word das Bild
    # auf die 14pt EXACTLY Zeilenhoehe des Normal-Styles
    pic_para.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    pic_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pic_para.paragraph_format.space_before = Pt(6)
    pic_para.paragraph_format.space_after = Pt(6)


# ============================================================
# Dokument-Setup
# ============================================================

def setup_document():
    """Erstellt das Dokument mit KDP-Formatierung."""
    doc = Document()

    style = doc.styles['Normal']
    font = style.font
    font.name = 'Georgia'
    font.size = Pt(12)
    font.color.rgb = RGBColor(0, 0, 0)
    pf = style.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    pf.line_spacing = 1.35
    pf.widow_control = True

    h1 = doc.styles['Heading 1']
    h1.font.name = 'Georgia'
    h1.font.size = Pt(16)
    h1.font.bold = True
    h1.font.color.rgb = RGBColor(0, 0, 0)
    h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h1.paragraph_format.space_before = Pt(20)
    h1.paragraph_format.space_after = Pt(14)
    h1.paragraph_format.page_break_before = False

    sec = doc.sections[0]
    sec.page_width = PAGE_WIDTH
    sec.page_height = PAGE_HEIGHT
    sec.top_margin = Cm(1.6)
    sec.bottom_margin = Cm(1.6)
    sec.left_margin = Cm(2.3)   # Erhoehter Bundsteg fuer Bindung (~250+ Seiten)
    sec.right_margin = Cm(1.3)

    doc.settings.element.append(OxmlElement('w:mirrorMargins'))

    # Recto/Verso Kopfzeilen aktivieren (dokumentweit)
    doc.settings.element.append(OxmlElement('w:evenAndOddHeaders'))

    # Front Matter: Erste Seite ohne Header/Footer (Schmutztitel)
    sec.different_first_page_header_footer = True

    # Front Matter: KEIN Footer (keine Seitenzahlen)
    footer = sec.footer
    footer.is_linked_to_previous = False
    # Footer bleibt leer

    # Front Matter: KEINE Kopfzeilen
    header_odd = sec.header
    header_odd.is_linked_to_previous = False
    # Header bleiben leer

    header_even = sec.even_page_header
    header_even.is_linked_to_previous = False
    # Header bleiben leer

    return doc


# ============================================================
# XML-Hilfsfunktionen (Bookmarks & Hyperlinks)
# ============================================================

def add_bookmark(paragraph, name):
    """Fuegt einen Bookmark zu einem Absatz hinzu."""
    bm_id = str(abs(hash(name)) % 100000)
    start = OxmlElement('w:bookmarkStart')
    start.set(qn('w:id'), bm_id)
    start.set(qn('w:name'), name)
    end = OxmlElement('w:bookmarkEnd')
    end.set(qn('w:id'), bm_id)
    paragraph._p.insert(0, start)
    paragraph._p.append(end)


def _make_hyperlink_run(text, bold=False, italic=False, underline=True,
                        font_size=Pt(12)):
    """Erstellt ein w:r Element fuer einen Hyperlink."""
    run_el = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')

    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), 'Georgia')
    rFonts.set(qn('w:hAnsi'), 'Georgia')
    rPr.append(rFonts)

    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), str(int(font_size.pt * 2)))
    rPr.append(sz)

    if bold:
        rPr.append(OxmlElement('w:b'))
    if italic:
        rPr.append(OxmlElement('w:i'))
    if underline:
        u = OxmlElement('w:u')
        u.set(qn('w:val'), 'single')
        rPr.append(u)

    run_el.append(rPr)
    t = OxmlElement('w:t')
    t.text = text
    t.set(qn('xml:space'), 'preserve')
    run_el.append(t)

    return run_el


def add_hyperlink(paragraph, anchor, text, **kwargs):
    """Fuegt einen internen Hyperlink zu einem Absatz hinzu."""
    hl = OxmlElement('w:hyperlink')
    hl.set(qn('w:anchor'), anchor)
    hl.append(_make_hyperlink_run(text, **kwargs))
    paragraph._p.append(hl)


def add_paragraph_shading(paragraph, color="F0F0F0"):
    """Fuegt einem Absatz eine Hintergrund-Schattierung hinzu."""
    pPr = paragraph._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), color)
    pPr.append(shd)


def add_paragraph_borders(paragraph, color="AAAAAA", size="4"):
    """Fuegt einem Absatz obere und untere Rahmenlinie hinzu."""
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    for side in ('top', 'bottom'):
        border = OxmlElement(f'w:{side}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), size)
        border.set(qn('w:space'), '4')
        border.set(qn('w:color'), color)
        pBdr.append(border)
    pPr.append(pBdr)


def _add_pageref_field(paragraph, bookmark_name, font_size=Pt(9)):
    """Fuegt ein PAGEREF-Feld ein (zeigt die Seitenzahl eines Bookmarks)."""
    run1 = paragraph.add_run()
    run1.font.name = 'Georgia'
    run1.font.size = font_size
    fld_begin = OxmlElement('w:fldChar')
    fld_begin.set(qn('w:fldCharType'), 'begin')
    run1._r.append(fld_begin)

    run2 = paragraph.add_run()
    run2.font.name = 'Georgia'
    run2.font.size = font_size
    instr = OxmlElement('w:instrText')
    instr.text = f' PAGEREF {bookmark_name} '
    instr.set(qn('xml:space'), 'preserve')
    run2._r.append(instr)

    run3 = paragraph.add_run()
    run3.font.name = 'Georgia'
    run3.font.size = font_size
    fld_end = OxmlElement('w:fldChar')
    fld_end.set(qn('w:fldCharType'), 'end')
    run3._r.append(fld_end)


# ============================================================
# Text-Rendering mit Markdown-Erkennung
# ============================================================

def _add_run(p, text, bold=False, italic=False):
    """Fuegt einen formatierten Run hinzu."""
    if not text:
        return
    run = p.add_run(text)
    run.font.name = 'Georgia'
    run.font.size = Pt(12)
    if bold:
        run.font.bold = True
    if italic:
        run.font.italic = True


def _render_text_with_links(p, text, bold=False, italic=False):
    """Rendert Text und macht 'Abschnitt X' zu klickbaren Links.
    Fuegt Seitenzahlen per PAGEREF hinzu (fuer Print).
    Wenn SHUFFLE_SECTIONS aktiv: ersetzt Nummern durch gescramblte Werte."""
    last = 0
    for m in re.finditer(r'Abschnitt\s+(\d+\w?)', text):
        before = text[last:m.start()]
        if before:
            _add_run(p, before, bold=bold, italic=italic)
        old_sid = m.group(1)
        new_sid = map_section_id(old_sid)
        display_text = f"Abschnitt {new_sid}"
        add_hyperlink(p, bookmark_for(new_sid), display_text,
                      bold=bold, italic=italic)
        # Seitenzahl anfuegen: " (S. XX)"
        _add_run(p, " (S.\u00a0", bold=bold, italic=italic)
        _add_pageref_field(p, bookmark_for(new_sid), font_size=Pt(12))
        _add_run(p, ")", bold=bold, italic=italic)
        last = m.end()

    remaining = text[last:]
    if remaining:
        _add_run(p, remaining, bold=bold, italic=italic)


def render_markdown_line(p, text):
    """Rendert eine Zeile mit **bold**, *italic* und Abschnitt-Links."""
    parts = re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*)', text)

    for part in parts:
        if not part:
            continue
        if part.startswith('**') and part.endswith('**'):
            _render_text_with_links(p, part[2:-2], bold=True)
        elif part.startswith('*') and part.endswith('*'):
            _render_text_with_links(p, part[1:-1], italic=True)
        else:
            _render_text_with_links(p, part)


# ============================================================
# Seiten-Bausteine
# ============================================================

def add_half_title_page(doc):
    """Erstellt die Schmutztitelseite (Half-Title)."""
    for _ in range(8):
        doc.add_paragraph().paragraph_format.space_after = Pt(12)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Das Geheimnis des Brunnens")
    run.font.size = Pt(16)
    run.font.name = 'Georgia'
    run.font.italic = True


def add_title_page(doc):
    """Erstellt die Titelseite."""
    doc.add_page_break()
    for _ in range(5):
        doc.add_paragraph().paragraph_format.space_after = Pt(12)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Dein Fall \u2014 Du entscheidest!")
    run.font.size = Pt(22)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(12)

    # Dekorative Linie
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\u2500\u2500\u2500\u2500\u2500\u2500\u2500")
    run.font.size = Pt(10)
    run.font.name = 'Georgia'
    run.font.color.rgb = RGBColor(170, 170, 170)
    p.paragraph_format.space_after = Pt(12)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Das Geheimnis des Brunnens")
    run.font.size = Pt(18)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(10)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Ein interaktiver Detektiv-Krimi mit 18 Enden")
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(6)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("4 Wege. 18 Enden. 26 Entscheidungen.")
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(10)

    for _ in range(5):
        doc.add_paragraph().paragraph_format.space_after = Pt(12)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Benjamin Krug")
    run.font.size = Pt(14)
    run.font.name = 'Georgia'


def add_impressum_page(doc):
    """Erstellt die Impressum-Seite."""
    doc.add_page_break()
    for _ in range(2):
        doc.add_paragraph()

    lines = [
        "Dein Fall \u2014 Du entscheidest!",
        "Das Geheimnis des Brunnens",
        "Ein interaktiver Detektiv-Krimi mit 18 Enden",
        "",
        "\u00a9 2026 Benjamin Krug",
        "Alle Rechte vorbehalten.",
        "",
        "ISBN: TODO",  # TODO: ISBN eintragen
        "Independently published",
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
    """Erstellt die Widmungsseite."""
    doc.add_page_break()
    for _ in range(6):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(
        "F\u00fcr alle Kinder, die tiefer graben\n"
        "\u2014 und nie aufh\u00f6ren zu fragen."
    )
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.name = 'Georgia'


def add_character_page(doc):
    """Erstellt die Charakter-Vorstellungsseite."""
    doc.add_page_break()
    doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Deine Begleiter")
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(20)

    characters = [
        ("Jonas (10)",
         "Der Anf\u00fchrer der Herrenhaus-Detektive. Neugierig und aufmerksam. "
         "Stellt die richtigen Fragen zur richtigen Zeit."),
        ("Mila (10)",
         "Mutig und ungeduldig. Immer bereit, den ersten Schritt "
         "zu machen. Ihr Lieblingsspruch: \u201eJetzt oder nie!\u201c"),
        ("Ben (10)",
         "Tr\u00e4gt immer seine rote M\u00fctze. Hat vor allem Angst \u2014 "
         "aber wenn es drauf ankommt, rettet er die Lage. "
         "Wieder."),
    ]

    for name, desc in characters:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(name)
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(4)

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run("\u2500\u2500\u2500")
        run.font.size = Pt(8)
        run.font.color.rgb = RGBColor(170, 170, 170)
        run.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(4)

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(desc)
        run.font.size = Pt(11)
        run.font.italic = True
        run.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(16)
        p.paragraph_format.left_indent = Cm(1.5)
        p.paragraph_format.right_indent = Cm(1.5)


def add_intro_page(doc):
    """Erstellt die Einleitungsseite ('Wie dieses Buch funktioniert')."""
    doc.add_page_break()

    filepath = os.path.join(ABSCHNITTE_DIR, "Abschnitt_00_Einleitung.md")
    if not os.path.exists(filepath):
        print("  WARNUNG: Abschnitt_00_Einleitung.md nicht gefunden!")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')

    for line in lines:
        stripped = line.strip()

        if not stripped:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(4)
            continue

        if stripped.startswith('#'):
            title_text = stripped.lstrip('#').strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(title_text)
            run.font.size = Pt(18)
            run.font.bold = True
            run.font.name = 'Georgia'
            p.paragraph_format.space_after = Pt(14)
            add_bookmark(p, bookmark_for("einleitung"))
            continue

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(2)
        render_markdown_line(p, stripped)


def add_village_map_page(doc):
    """Fuegt die Gangsystem-Karte (Illustration 1) als eigene Seite ein."""
    doc.add_page_break()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Karte von Eichenhain")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(10)

    add_illustration(doc, 1)


def add_section_index(doc, total_sections):
    """Erstellt ein kompaktes Abschnitt-Verzeichnis mit Seitenzahlen."""
    doc.add_page_break()

    # Titel
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Abschnitt-Verzeichnis")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(4)

    # Hinweis
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Finde hier die Seite f\u00fcr jeden Abschnitt.")
    run.font.size = Pt(10)
    run.font.italic = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(14)

    # Tabelle ohne Rahmen (5 Spalten)
    cols = 5
    rows = (total_sections + cols - 1) // cols

    table = doc.add_table(rows=rows, cols=cols)

    # Rahmen entfernen
    tblPr = table._tbl.tblPr
    if tblPr is None:
        tblPr = OxmlElement('w:tblPr')
        table._tbl.insert(0, tblPr)
    borders = OxmlElement('w:tblBorders')
    for border_name in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'none')
        border.set(qn('w:sz'), '0')
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), 'auto')
        borders.append(border)
    tblPr.append(borders)

    for i in range(total_sections):
        num = i + 1
        row_idx = i // cols
        col_idx = i % cols
        cell = table.cell(row_idx, col_idx)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)

        # Abschnitt-Nummer (fett)
        run = p.add_run(f"{num:>2} ")
        run.font.name = 'Georgia'
        run.font.size = Pt(9)
        run.font.bold = True

        # Punkte
        run = p.add_run("\u00b7\u00b7\u00b7 ")
        run.font.name = 'Georgia'
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(170, 170, 170)

        # Seitenzahl via PAGEREF
        _add_pageref_field(p, bookmark_for(str(num)), font_size=Pt(9))


def add_body_section_break(doc):
    """Fuegt einen Abschnittswechsel ein: Front Matter -> Body.

    Startet eine neue Word-Section mit:
    - Seitennummerierung ab 1
    - Footer mit zentrierter Seitenzahl
    - Recto/Verso-Kopfzeilen
    """
    new_sec = doc.add_section(WD_SECTION_START.NEW_PAGE)

    # Seitenformat kopieren
    new_sec.page_width = PAGE_WIDTH
    new_sec.page_height = PAGE_HEIGHT
    new_sec.top_margin = Cm(1.6)
    new_sec.bottom_margin = Cm(1.6)
    new_sec.left_margin = Cm(2.3)
    new_sec.right_margin = Cm(1.3)

    # Seitennummerierung bei 1 starten
    sectPr = new_sec._sectPr
    pgNumType = OxmlElement('w:pgNumType')
    pgNumType.set(qn('w:start'), '1')
    sectPr.append(pgNumType)

    # Footer: zentrierte Seitenzahl
    footer = new_sec.footer
    footer.is_linked_to_previous = False
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER

    run1 = fp.add_run()
    fld_begin = OxmlElement('w:fldChar')
    fld_begin.set(qn('w:fldCharType'), 'begin')
    run1._r.append(fld_begin)

    run2 = fp.add_run()
    instr = OxmlElement('w:instrText')
    instr.text = ' PAGE '
    instr.set(qn('xml:space'), 'preserve')
    run2._r.append(instr)

    run3 = fp.add_run()
    fld_end = OxmlElement('w:fldChar')
    fld_end.set(qn('w:fldCharType'), 'end')
    run3._r.append(fld_end)

    for r in fp.runs:
        r.font.name = 'Georgia'
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(170, 170, 170)

    # Ungerade Seiten (rechts): Serientitel
    header_odd = new_sec.header
    header_odd.is_linked_to_previous = False
    hp_odd = header_odd.paragraphs[0]
    hp_odd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = hp_odd.add_run("Dein Fall \u2014 Du entscheidest!")
    run.font.name = 'Georgia'
    run.font.size = Pt(8)
    run.font.color.rgb = RGBColor(170, 170, 170)
    run.font.italic = True

    # Gerade Seiten (links): Buchtitel
    header_even = new_sec.even_page_header
    header_even.is_linked_to_previous = False
    hp_even = header_even.paragraphs[0]
    hp_even.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = hp_even.add_run("Das Geheimnis des Brunnens")
    run.font.name = 'Georgia'
    run.font.size = Pt(8)
    run.font.color.rgb = RGBColor(170, 170, 170)
    run.font.italic = True


# ============================================================
# Story-Abschnitte
# ============================================================

def add_story_section(doc, section_id, filepath):
    """Fuegt einen Story-Abschnitt zum Dokument hinzu."""
    doc.add_page_break()

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Header extrahieren, Rest als Content
    lines = content.split('\n')
    header = ""
    content_lines = []
    header_found = False

    for line in lines:
        if not header_found and line.strip().startswith('#'):
            header = line.strip().lstrip('#').strip()
            header_found = True
            continue
        if header_found:
            content_lines.append(line)

    # Neue (gescramblte) ID fuer Header und Bookmark
    new_id = map_section_id(section_id)

    # Leerraum oben (~2cm)
    for _ in range(3):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)

    # "A B S C H N I T T" -- gesperrt, grau, zentriert
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("A B S C H N I T T")
    run.font.name = 'Georgia'
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(120, 120, 120)
    p.paragraph_format.space_after = Pt(2)

    # Abschnitt-Nummer -- gross, fett, zentriert + Bookmark
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(new_id)
    run.font.name = 'Georgia'
    run.font.size = Pt(22)
    run.font.bold = True
    p.paragraph_format.space_after = Pt(4)
    add_bookmark(p, bookmark_for(new_id))

    # Dekorative Linie
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\u2500\u2500\u2500")
    run.font.name = 'Georgia'
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(120, 120, 120)
    p.paragraph_format.space_after = Pt(12)

    # Illustrationen einfuegen (nach Header, vor Text)
    if section_id in ILLUSTRATION_MAP:
        for ill_num in ILLUSTRATION_MAP[section_id]:
            add_illustration(doc, ill_num)

    # Pfeile normalisieren
    text = '\n'.join(content_lines)
    text = text.replace('-->', '\u2192')
    content_lines = text.split('\n')

    # Zeilen in Gruppen aufteilen (getrennt durch Leerzeilen)
    groups = []
    current = []
    for line in content_lines:
        stripped = line.strip()
        if not stripped:
            if current:
                groups.append(current)
                current = []
            continue
        if stripped.startswith('#'):
            continue
        current.append(stripped)
    if current:
        groups.append(current)

    # Gruppen rendern (mit Drop Cap + Einzug-Tracking)
    first_text_group = True
    after_separator = False

    for group in groups:
        is_sep = (len(group) == 1 and group[0] == '---')

        _render_group(doc, group,
                      drop_cap=(first_text_group and not is_sep),
                      no_indent=((first_text_group or after_separator)
                                 and not is_sep))

        if is_sep:
            after_separator = True
        else:
            if first_text_group:
                first_text_group = False
            after_separator = False

    # Abschnitt-Ende-Ornament
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run("\u2500 \u25c6 \u2500")
    run.font.name = 'Georgia'
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(170, 170, 170)


def _render_group(doc, group, drop_cap=False, no_indent=False):
    """Rendert eine Gruppe von Zeilen als Absatz/Absaetze."""

    # Szenen-Trenner
    if len(group) == 1 and group[0] == '---':
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run("\u2726")
        run.font.size = Pt(12)
        run.font.name = 'Georgia'
        run.font.color.rgb = RGBColor(120, 120, 120)
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(12)
        return

    # Navigation: "-> Weiter bei Abschnitt X"
    if len(group) == 1 and re.match(r'^\u2192\s*Weiter bei', group[0]):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        # Arrow -> durch Dreieck ersetzen
        nav_text = group[0].replace('\u2192', '\u25B6')
        render_markdown_line(p, nav_text)
        for run in p.runs:
            run.font.bold = True
            run.font.size = Pt(13)
        add_paragraph_shading(p, "F0F0F0")
        return

    # Einzelne Bold-Zeile (Entscheidung oder ENDE)
    if len(group) == 1 and group[0].startswith('**') and group[0].endswith('**'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        render_markdown_line(p, group[0])
        add_paragraph_shading(p, "F0F0F0")
        return

    # Einzelne Italic-Zeile (Situations-Text)
    if (len(group) == 1
            and group[0].startswith('*')
            and not group[0].startswith('**')
            and group[0].endswith('*')):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(6)
        render_markdown_line(p, group[0])
        add_paragraph_borders(p)
        return

    # Alle Zeilen Bold (Mehrfach-Entscheidungsblock)
    if all(l.startswith('**') and l.endswith('**') for l in group):
        for i, line in enumerate(group):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            render_markdown_line(p, line)
            add_paragraph_shading(p, "F0F0F0")
        return

    # Alle Zeilen Italic (z.B. Ende-Hinweis)
    if all(l.startswith('*') and not l.startswith('**') and l.endswith('*')
           for l in group):
        for line in group:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            render_markdown_line(p, line)
        return

    # Normaler Text: Zeilen zusammenfuegen
    joined = " ".join(group)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)

    if no_indent:
        p.paragraph_format.first_line_indent = Cm(0)
    else:
        p.paragraph_format.first_line_indent = Cm(0.5)

    if drop_cap and joined:
        # Drop Cap: erster Buchstabe gross
        first_char = joined[0]
        rest = joined[1:]
        dc_run = p.add_run(first_char)
        dc_run.font.name = 'Georgia'
        dc_run.font.size = Pt(28)
        dc_run.font.bold = True
        if rest:
            render_markdown_line(p, rest)
    else:
        render_markdown_line(p, joined)


# ============================================================
# End-Seiten
# ============================================================

def add_discoveries_page(doc):
    """Erstellt die 'Deine Entdeckungen' Sammelseite."""
    doc.add_page_break()

    # Titel
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Deine Entdeckungen")
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(14)

    # -- Enden --
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Wie viele Enden hast du gefunden?")
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(10)

    endings = [
        ("ENDE 206", "Die versiegelte Wahrheit"),
        ("ENDE 207", "Der versperrte Weg"),
        ("ENDE 208", "Die Quelle von Eichenhain"),
        ("ENDE 209", "Der Brief aus der Tiefe"),
        ("ENDE 210", "Die vergessene Urkunde"),
        ("ENDE 211", "Der Brunnen flie\u00dft"),
        ("ENDE 212", "Verlaufen"),
        ("ENDE 213", "Ohne Lisbeth"),
        ("ENDE 214", "Lisbeths Tr\u00e4nen"),
        ("ENDE 215", "Die halbe Wahrheit"),
        ("ENDE 216", "Winters Anruf"),
        ("ENDE 217", "Fast alles"),
        ("ENDE 218", "Kein Empfang"),
        ("ENDE 219", "Nicht dabei"),
        ("ENDE 220", "Meiers Geheimnis"),
        ("ENDE 221", "Der eigene Weg"),
        ("ENDE 222", "Eichenhain"),
        ("ENDE 223", "Stille am Kirchplatz"),
    ]

    for code, name in endings:
        p = doc.add_paragraph()
        run = p.add_run(f"\u2610  {code}")
        run.font.size = Pt(10)
        run.font.name = 'Georgia'
        run.font.small_caps = True
        run2 = p.add_run(f" \u2014 \u201e{name}\u201c")
        run2.font.size = Pt(10)
        run2.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.left_indent = Cm(1.5)

    # Zaehler
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("_____ / 18 Enden gefunden!")
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(14)

    # Trenner
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\u2726")
    run.font.size = Pt(12)
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(10)

    # -- Geheime Orte --
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Geheime Orte")
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(8)

    places = [
        "Den Brief ge\u00f6ffnet",
        "Die Geheimtinte entdeckt",
        "Frau Bergmanns Geschichte geh\u00f6rt",
        "Die Metallt\u00fcr ge\u00f6ffnet",
        "Das Gangsystem betreten",
        "Die nat\u00fcrliche Quelle gefunden",
        "Die Zeitkapsel ge\u00f6ffnet",
        "Durch den Brunnen aufgestiegen",
        "Die zweite Karte entdeckt",
        "Winter am Telefon gesprochen",
    ]

    for place in places:
        p = doc.add_paragraph()
        run = p.add_run(f"\u2610  {place}")
        run.font.size = Pt(10)
        run.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.left_indent = Cm(1.5)

    # Abschluss-Tipp
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run("Tipp: Vier Enden sind besonders gut.")
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.name = 'Georgia'

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Findest du die vier perfekten Wege?")
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.name = 'Georgia'


def add_detective_notes_page(doc):
    """Erstellt 2 Seiten fuer Detektiv-Notizen."""
    doc.add_page_break()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Deine Detektiv-Notizen")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(6)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Schreib hier deine Hinweise und Entdeckungen auf!")
    run.font.size = Pt(10)
    run.font.italic = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(14)

    for page in range(2):
        if page > 0:
            doc.add_page_break()
        for _ in range(20):
            p = doc.add_paragraph()
            # Untere Linie per Border
            pPr = p._p.get_or_add_pPr()
            pBdr = OxmlElement('w:pBdr')
            bottom = OxmlElement('w:bottom')
            bottom.set(qn('w:val'), 'single')
            bottom.set(qn('w:sz'), '4')
            bottom.set(qn('w:space'), '1')
            bottom.set(qn('w:color'), 'CCCCCC')
            pBdr.append(bottom)
            pPr.append(pBdr)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.left_indent = Cm(0.3)
            p.paragraph_format.right_indent = Cm(0.3)


def add_about_author_page(doc):
    """Erstellt die 'Ueber den Autor' Seite."""
    doc.add_page_break()
    for _ in range(2):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\u00dcber den Autor")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(14)

    bio_lines = [
        ("Benjamin Krug schreibt Geschichten, die Kinder nicht mehr "
         "aus der Hand legen k\u00f6nnen."),
        "",
        ("Wenn er nicht gerade an seinem Schreibtisch sitzt und sich "
         "neue Geheimnisse f\u00fcr Jonas, Mila und Ben ausdenkt, "
         "erkundet er am liebsten alte Geb\u00e4ude "
         "und stellt sich vor, welche Geschichten sie erz\u00e4hlen w\u00fcrden."),
        "",
        ("Er lebt in Deutschland und glaubt fest daran, "
         "dass jedes Kind ein Detektiv ist \u2014 "
         "man muss nur genau genug hinschauen."),
    ]

    for line in bio_lines:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if line:
            run = p.add_run(line)
            run.font.size = Pt(11)
            run.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Cm(1.0)
        p.paragraph_format.right_indent = Cm(1.0)


def add_acknowledgments_page(doc):
    """Erstellt die Danksagung."""
    doc.add_page_break()
    for _ in range(3):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Danksagung")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(14)

    thanks_text = (
        "Danke an alle kleinen und gro\u00dfen Testleser, "
        "die dieses Buch besser gemacht haben. "
        "Und an dich \u2014 weil du dich getraut hast, "
        "tiefer zu graben."
    )

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(thanks_text)
    run.font.size = Pt(11)
    run.font.italic = True
    run.font.name = 'Georgia'
    p.paragraph_format.left_indent = Cm(1.5)
    p.paragraph_format.right_indent = Cm(1.5)


def add_review_request_page(doc):
    """Erstellt die Rezensions-Bitte."""
    doc.add_page_break()
    for _ in range(2):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Eine kleine Bitte")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(6)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\u2605 \u2605 \u2605 \u2605 \u2605")
    run.font.size = Pt(14)
    run.font.name = 'Georgia'
    run.font.color.rgb = RGBColor(200, 160, 50)
    p.paragraph_format.space_after = Pt(20)

    review_lines = [
        ("Wenn dir das Buch gefallen hat, w\u00fcrde ich mich riesig "
         "\u00fcber eine kurze Bewertung auf Amazon freuen."),
        "",
        ("Ein paar Worte reichen v\u00f6llig \u2014 zum Beispiel, was dir "
         "am besten gefallen hat oder welche Figur dein Liebling ist."),
        "",
        ("Jede Bewertung hilft mir, noch mehr Abenteuer "
         "f\u00fcr dich zu schreiben!"),
    ]

    for line in review_lines:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if line:
            run = p.add_run(line)
            run.font.size = Pt(12)
            run.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Cm(1.0)
        p.paragraph_format.right_indent = Cm(1.0)

    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Danke! \u2764")
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(10)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\u2014 Benjamin")
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.name = 'Georgia'


def add_band3_teaser(doc):
    """Erstellt die Vorschau auf Band 3."""
    doc.add_page_break()
    doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Bald erh\u00e4ltlich")
    run.font.size = Pt(12)
    run.font.name = 'Georgia'
    run.font.color.rgb = RGBColor(120, 120, 120)
    p.paragraph_format.space_after = Pt(4)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Dein Fall \u2014 Du entscheidest!")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(4)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Band 3")
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(14)

    teaser_lines = [
        "Die Karte zeigt ein zweites X.",
        "Irgendwo im Wald hinter Eichenhain.",
        "",
        "Winter hat die zweite Quelle nie gefunden.",
        "Aber Jonas, Mila und Ben haben die Karte.",
        "",
        "Und diesmal wartet jemand auf sie.",
        "Jemand, der schon viel l\u00e4nger sucht.",
        "",
        "Das dritte Abenteuer beginnt bald.",
    ]

    for line in teaser_lines:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if line:
            run = p.add_run(line)
            run.font.name = 'Georgia'
            run.font.size = Pt(12)
            run.font.italic = True
        p.paragraph_format.space_after = Pt(4)


def add_series_overview_page(doc):
    """Erstellt die Serienuebersicht."""
    doc.add_page_break()
    doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Mehr Abenteuer von Benjamin Krug")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(20)

    series = [
        ("Dein Fall \u2014 Du entscheidest!",
         "Gleiche Charaktere, gleiches Geheimnis \u2014 aber DU bestimmst, "
         "was passiert. 4 Wege, 18 Enden, 26 Entscheidungen.",
         ["Band 1: Das verbotene Herrenhaus",
          "Band 2: Das Geheimnis des Brunnens"]),
        ("Die Herrenhaus-Detektive",
         "Niemand darf das alte Herrenhaus betreten. "
         "Aber Jonas, Mila und Ben finden einen Schl\u00fcssel \u2014 "
         "und hinter der verschlossenen T\u00fcr wartet ein Geheimnis.",
         ["Band 1: Das verbotene Herrenhaus",
          "Band 2: Das Geheimnis des Brunnens",
          "Band 3: Erscheint bald!"]),
        ("Die Chrono-Agenten",
         "Drei Kinder. Ein Tablet, das die Zeit \u00f6ffnet. "
         "Und ein Countdown, der nicht aufh\u00f6rt zu laufen.",
         ["Band 1: Der Code von 1945"]),
    ]

    for i, (title, desc, bands) in enumerate(series):
        if i > 0:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run("\u2014 \u2014 \u2014")
            run.font.size = Pt(10)
            run.font.name = 'Georgia'
            run.font.color.rgb = RGBColor(120, 120, 120)
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(10)

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(title)
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.name = 'Georgia'
        p.paragraph_format.space_after = Pt(6)

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(desc)
        run.font.size = Pt(10)
        run.font.name = 'Georgia'
        run.font.italic = True
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.left_indent = Cm(0.8)
        p.paragraph_format.right_indent = Cm(0.8)

        if bands:
            for band in bands:
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run(band)
                run.font.size = Pt(10)
                run.font.name = 'Georgia'
                p.paragraph_format.space_after = Pt(2)

    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Alle B\u00fccher auf Amazon erh\u00e4ltlich!")
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.name = 'Georgia'


# ============================================================
# Main
# ============================================================

def main():
    print("Erstelle interaktives KDP-Manuskript (Band 2)...")
    doc = setup_document()

    # === FRONT MATTER (ohne Seitenzahlen, ohne Kopfzeilen) ===
    print("  Schmutztitel")
    add_half_title_page(doc)

    print("  Titelseite")
    add_title_page(doc)

    print("  Impressum")
    add_impressum_page(doc)

    print("  Widmung")
    add_dedication_page(doc)

    print("  Charaktere")
    add_character_page(doc)

    print("  Einleitung")
    add_intro_page(doc)

    print("  Karte")
    add_village_map_page(doc)

    # Abschnitte sammeln
    section_files = get_section_files()

    # Story-Dateien (ohne Einleitung)
    story_files = [f for f in section_files
                   if section_id_from_filename(f) != "einleitung"]

    if SHUFFLE_SECTIONS:
        # Nummern-Mapping erstellen
        global SECTION_MAP
        SECTION_MAP = create_section_mapping(section_files)

        # Nach NEUER Nummer sortieren (wie 1000 Gefahren: Buch geht 1,2,3...)
        def new_num_sort_key(filename):
            sid = section_id_from_filename(filename)
            new_id = map_section_id(sid)
            return int(new_id)

        ordered_files = sorted(story_files, key=new_num_sort_key)

        # Mapping ausgeben
        print("  Nummern-Mapping (Original -> Neu):")
        for old_id in sorted(SECTION_MAP.keys(),
                             key=lambda x: (len(x), x)):
            print(f"    {old_id:>4s} -> {SECTION_MAP[old_id]:>3s}")
        print(f"  ({len(SECTION_MAP)} Abschnitte gescrambled)")
    else:
        ordered_files = story_files

    # Abschnitt-Verzeichnis (letztes Front Matter)
    print("  Abschnitt-Verzeichnis")
    add_section_index(doc, len(ordered_files))

    # === ABSCHNITTSWECHSEL: Front Matter -> Body ===
    print("  Abschnittswechsel (Seitennummerierung startet bei 1)")
    add_body_section_break(doc)

    # === BODY (Seitenzahlen ab 1, Kopfzeilen aktiv) ===
    total_words = 0
    section_count = 0

    for filename in ordered_files:
        sid = section_id_from_filename(filename)
        new_sid = map_section_id(sid)
        filepath = os.path.join(ABSCHNITTE_DIR, filename)
        print(f"  Abschnitt {sid} -> {new_sid}")
        add_story_section(doc, sid, filepath)
        section_count += 1

        with open(filepath, 'r', encoding='utf-8') as f:
            total_words += len(f.read().split())

    # === BACK MATTER ===
    print("  Deine Entdeckungen")
    add_discoveries_page(doc)

    print("  Detektiv-Notizen")
    add_detective_notes_page(doc)

    print("  Ueber den Autor")
    add_about_author_page(doc)

    print("  Band 3 Vorschau")
    add_band3_teaser(doc)

    print("  Serienuebersicht")
    add_series_overview_page(doc)

    print("  Rezensions-Bitte")
    add_review_request_page(doc)

    print("  Danksagung")
    add_acknowledgments_page(doc)

    # Speichern
    doc.save(OUTPUT_FILE)
    print(f"\nManuskript erstellt: {OUTPUT_FILE}")
    print(f"  {section_count} Abschnitte")
    print(f"  ~{total_words:,} Woerter gesamt")
    if SHUFFLE_SECTIONS:
        print("  Reihenfolge: durchgemischt (SHUFFLE_SECTIONS = True)")


if __name__ == "__main__":
    main()
