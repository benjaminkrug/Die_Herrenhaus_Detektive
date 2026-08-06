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
OUTPUT_FILE = os.path.join(BASE_DIR, "Manuskript.docx")

# Rezensions-QR-Code (fuehrt direkt zum Amazon-Bewertungsformular).
# Erzeugt + gegengelesen von ../../build_qr_rezension.py
QR_REZENSION = os.path.join(BASE_DIR, "..", "Cover", "Linear",
                            "qr_rezension_band1.png")

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
    # Innen (Buchrücken): groesser wegen Bindung, Aussen: kleiner
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
    # Normal-Stil hat EXAKTEN Zeilenabstand (14pt) -- bei grossem, umbrechendem
    # Titel wuerden die zwei Zeilen sonst uebereinander liegen. Einfacher
    # (mitwachsender) Zeilenabstand fuer alle grossen Titelzeilen.
    p.paragraph_format.line_spacing = 1.0
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
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_after = Pt(40)

    # Leerraum
    for _ in range(3):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(12)

    # Autor-Platzhalter
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
        "Die Herrenhaus-Detektive, Band 1: Das verbotene Herrenhaus",
        "",
        "\u00a9 2026 Benjamin Krug",
        "Alle Rechte vorbehalten.",
        "",
        "Independently published",
        "",
        "ISBN: 9798248089956",
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
    run = p.add_run("F\u00fcr alle Kinder, die gerne Geheimnisse l\u00fcften.")
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
            label = f"Epilog \u2014 {title}"
        else:
            label = f"Kapitel {i} \u2014 {title}"

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

    # "Sink": echter Leerraum-Absatz, damit der Kapitelkopf nach unten einrueckt.
    # 44pt (statt 56pt wie Band 4), weil die 5x8-Seite kleiner ist -- so bleibt
    # der Einzug proportional gleich. Bewusst NICHT ueber space_before der ersten
    # Zeile (Word verwirft Abstand am Seitenanfang).
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_before = Pt(0)
    spacer.paragraph_format.space_after = Pt(44)

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
    """Erstellt die emotionale Schlussseite mit Dank und Ueberleitung."""
    add_page_break(doc)

    for _ in range(3):
        doc.add_paragraph()

    # Ende-Markierung
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Ende von Band 1")
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(30)

    # Emotionaler Moment — direkte Ansprache
    lines = [
        "Hat dir das Buch gefallen?",
        "",
        "Jonas, Mila und Ben freuen sich,",
        "dass du sie auf ihrem Abenteuer begleitet hast!",
        "",
        "Aber die Geschichte ist noch nicht vorbei \u2026",
        "",
        "Unter dem Dorfbrunnen wartet ein neues Geheimnis.",
        "Ein versiegelter Brief muss ge\u00f6ffnet werden.",
        "Und jemand im Dorf schweigt seit 70 Jahren.",
        "",
        "Bist du bereit f\u00fcr das n\u00e4chste Abenteuer?",
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
            if line == "Bist du bereit f\u00fcr das n\u00e4chste Abenteuer?":
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
    run = p.add_run("\u2605 \u2605 \u2605 \u2605 \u2605")
    run.font.size = Pt(14)
    run.font.name = 'Georgia'
    run.font.color.rgb = RGBColor(200, 160, 50)
    p.paragraph_format.space_after = Pt(20)

    # Text der Bitte
    review_lines = [
        ("Wenn dir das Buch gefallen hat, w\u00fcrde ich mich riesig "
         "\u00fcber eine kurze Bewertung auf Amazon freuen."),
        "",
        ("Ein paar Worte reichen v\u00f6llig \u2014 zum Beispiel, was dir am besten "
         "gefallen hat oder welche Figur dein Liebling ist."),
        "",
        ("Jede Bewertung hilft mir, noch mehr Abenteuer "
         "f\u00fcr dich zu schreiben!"),
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
        # Normal-Stil hat EXAKTEN Zeilenabstand (Pt(14)) -- der wuerde das Bild
        # abschneiden. Fuer den Bild-Absatz auf einfachen (mitwachsenden)
        # Zeilenabstand umstellen.
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        p.add_run().add_picture(QR_REZENSION, width=Inches(1.5))

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run("(Handykamera auf den Code halten \u2013 "
                        "der Link \u00f6ffnet sich von selbst.)")
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
    run = p.add_run("Danke! \u2764")
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.name = 'Georgia'
    p.paragraph_format.space_after = Pt(10)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\u2014 Benjamin")
    run.font.size = Pt(11)
    run.font.italic = True
    run.font.name = 'Georgia'


BAND2_KAPITEL1 = os.path.join(
    BASE_DIR, "..", "..", "Band_2", "Linear", "Kapitel",
    "Die_Herrenhaus_Detektive_Band2_Kapitel1.md")

# Bis hierhin (einschliesslich) laeuft die Leseprobe -- Cliffhanger: das Siegel
# ist gebrochen, alle halten den Atem an, bevor der Brief gelesen wird.
BAND2_LESEPROBE_ENDE = "Mila beugte sich vor."


def _lade_band2_leseprobe():
    """Liest den ECHTEN Anfang von Band 2, Kapitel 1 -- Titel + Text bis zum
    Cliffhanger. Kein abgetippter Text: die Leseprobe bleibt automatisch
    synchron mit dem geschriebenen Band 2."""
    with open(BAND2_KAPITEL1, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    titel = "Der versiegelte Brief"
    prosa, gestartet, fertig = [], False, False
    for line in lines:
        m = re.match(r"^# Kapitel\s+1\s*[-—]+\s*(.+)$", line.strip())
        if m:
            titel = m.group(1).strip()
            gestartet = True
            continue
        if gestartet and not fertig:
            prosa.append(line)
            if line.strip() == BAND2_LESEPROBE_ENDE:
                fertig = True
                break

    gruppen, aktuell = [], []
    for line in prosa:
        t = line.strip().replace(" -- ", " — ")   # sauberer Gedankenstrich
        if not t:
            if aktuell:
                gruppen.append(aktuell); aktuell = []
        elif t == "---":
            if aktuell:
                gruppen.append(aktuell); aktuell = []
            gruppen.append("BREAK")
        else:
            aktuell.append(t)
    if aktuell:
        gruppen.append(aktuell)
    return titel, gruppen


def add_band2_teaser(doc):
    """Vorschau auf Band 2: echte Leseprobe aus dem geschriebenen Kapitel 1."""
    add_page_break(doc)
    doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("LESEPROBE")
    run.font.size = Pt(11); run.font.name = "Georgia"
    run.font.color.rgb = RGBColor(100, 100, 100)
    set_tracking(run, 2.6)
    p.paragraph_format.space_after = Pt(4)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Die Herrenhaus-Detektive, Band 2")
    run.font.size = Pt(13); run.font.name = "Georgia"
    p.paragraph_format.space_after = Pt(2)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Das Geheimnis des Brunnens")
    run.font.size = Pt(18); run.font.bold = True; run.font.name = "Georgia"
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_after = Pt(18)

    titel, gruppen = _lade_band2_leseprobe()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("KAPITEL 1")
    run.font.size = Pt(11); run.font.name = "Georgia"
    run.font.color.rgb = RGBColor(90, 90, 90)
    set_tracking(run, 2.6)
    p.paragraph_format.space_after = Pt(6)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(titel)
    run.font.size = Pt(15); run.font.bold = True; run.font.name = "Georgia"
    p.paragraph_format.space_after = Pt(16)

    for gruppe in gruppen:
        if gruppe == "BREAK":
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run("* * *")
            run.font.size = Pt(11); run.font.name = "Georgia"
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            continue
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(0)
        add_text_to_paragraph(p, " ".join(gruppe))

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("[ … ]")
    run.font.size = Pt(12); run.font.name = "Georgia"
    run.font.color.rgb = RGBColor(120, 120, 120)
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(14)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(
        "Was verbirgt sich unter dem Brunnen?\n"
        "Wer schweigt seit 70 Jahren — und warum?\n"
        "Und was steht in Winters versiegeltem Brief?"
    )
    run.font.size = Pt(11); run.font.italic = True; run.font.name = "Georgia"
    p.paragraph_format.space_after = Pt(16)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Das Geheimnis des Brunnens")
    run.font.size = Pt(13); run.font.bold = True; run.font.name = "Georgia"
    p.paragraph_format.space_after = Pt(4)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Jetzt auf Amazon erhältlich!")
    run.font.size = Pt(12); run.font.bold = True; run.font.name = "Georgia"


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
        "Aber Jonas, Mila und Ben finden einen Schl\u00fcssel \u2014 "
        "und hinter der verschlossenen T\u00fcr wartet ein Geheimnis, "
        "das seit drei\u00dfig Jahren niemand l\u00fcften durfte. "
        "Spannendes Detektivabenteuer ab 8 Jahren.",
        band_info=[
            "Band 1: Das verbotene Herrenhaus",
            "Band 2: Das Geheimnis des Brunnens",
            "Band 3: Erscheint bald!",
        ],
    )

    # Trenner
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\u2014 \u2014 \u2014")
    run.font.size = Pt(10)
    run.font.name = 'Georgia'
    run.font.color.rgb = RGBColor(150, 150, 150)
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(10)

    # --- Serie 2: Die Chrono-Agenten ---
    _add_series_block(
        doc,
        "Die Chrono-Agenten",
        "Drei Kinder. Ein Tablet, das die Zeit \u00f6ffnet. "
        "Und ein Countdown, der nicht aufh\u00f6rt zu laufen. "
        "Leo, Mila und Ben sind Agenten wider Willen \u2014 "
        "geschickt in die gef\u00e4hrlichsten Momente der Geschichte, "
        "um zu retten, was jemand zerst\u00f6ren will. "
        "Ihr Gegner hei\u00dft Codex. Und er kennt ihre Namen. "
        "F\u00fcr alle, die Geschichte spannend finden \u2014 "
        "und wissen wollen, was passiert, wenn man sie ver\u00e4ndert.",
    )

    # Trenner
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\u2014 \u2014 \u2014")
    run.font.size = Pt(10)
    run.font.name = 'Georgia'
    run.font.color.rgb = RGBColor(150, 150, 150)
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(10)

    # --- Serie 3: Die Geisterspuerer ---
    _add_series_block(
        doc,
        "Die Geistersp\u00fcrer",
        "In Gravenstedt sind die Toten nicht still. "
        "Nora (12) und Theo (10) ziehen in eine alte Wohnung \u2014 "
        "und finden einen Hund, der Geister sp\u00fcrt. "
        "Jetzt m\u00fcssen sie die Wahrheit hinter einer "
        "zweihundert Jahre alten L\u00fcge aufdecken. "
        "Bevor es zu sp\u00e4t ist. "
        "Gruselig-lustiges Abenteuer ab 10 Jahren.",
        band_info=[
            "Band 1: Das Haus, das fl\u00fcstert",
        ],
    )

    # Abschluss
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Alle B\u00fccher auf Amazon erh\u00e4ltlich!")
    run.font.size = Pt(11)
    run.font.bold = True
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

    # 6. Ende-Seite (emotionaler Moment)
    print("  Ende-Seite")
    add_end_page(doc)

    # 7. Rezensions-Bitte
    print("  Rezensions-Bitte")
    add_review_request_page(doc)

    # 8. Band 2 Leseprobe
    print("  Band 2 Leseprobe")
    add_band2_teaser(doc)

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
