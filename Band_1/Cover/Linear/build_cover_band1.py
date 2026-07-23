# -*- coding: utf-8 -*-
"""
Baut das KDP-Full-Cover fuer Band 1 (5 x 8 Zoll, 300 dpi, weisses Papier).

Unterschied zum Band-3-Skript: Dort wurde ein FERTIGES Full-Cover skaliert und
zentriert beschnitten -- dabei verrutscht der Buchruecken, sobald die Seitenzahl
sich aendert. Hier werden Rueckseite, Ruecken und Vorderseite PIXELGENAU an ihre
KDP-Positionen gesetzt. Der Ruecken wird direkt gesetzt (Text auf Flaeche), dafuer
braucht es kein Bildmodell.

Erzeugt zusaetzlich das E-Book-Cover (1600 x 2560, Verhaeltnis 1:1,6 -- ein
ANDERER Beschnitt als der Druck, nicht bloss kleiner).

Aufruf:
    python build_cover_band1.py
"""
import io
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# EINSTELLUNGEN
# --------------------------------------------------------------------------
FRONT = os.path.join(BASE, "front_band1.png")   # Vorderseite MIT Typografie
BACK = os.path.join(BASE, "back_band1.png")     # Rueckseite MIT Typografie

# !! Vor dem finalen Lauf durch die ECHTE Seitenzahl aus dem KDP-Previewer
#    ersetzen. Die Schaetzung (150) ist grob -- Band 1 hat ~29.000 Woerter auf 5x8.
PAGE_COUNT = 150
PAGE_COUNT_IS_ESTIMATE = True

DPI = 300
BLEED = 0.125          # Zoll, rundherum aussen
TRIM_W, TRIM_H = 5.0, 8.0
SPINE_FACTOR = 0.002252   # weisses Papier (creme: 0.0025)

# Ruecken
SPINE_BG = (0x12, 0x18, 0x1E)     # tiefes Blaugrau
GOLD = (0xD8, 0xB4, 0x6C)
CREME = (0xE0, 0xD4, 0xAC)
SPINE_NUMBER = "1"
SPINE_TITLE = "Das verbotene Herrenhaus"
SPINE_SERIES = "DIE HERRENHAUS-DETEKTIVE"
SPINE_AUTHOR = "Benjamin Krug"

# Schrift: Georgia liegt auf Windows; sonst eine beliebige Serife eintragen.
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\georgia.ttf",
    r"C:\Windows\Fonts\georgiab.ttf",
    r"C:\Windows\Fonts\times.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
]

OUT_FULL_PNG = os.path.join(BASE, "Band1_Cover_KDP_5x8_300dpi.png")
OUT_FULL_PDF = os.path.join(BASE, "Band1_Cover_KDP_5x8_300dpi.pdf")
OUT_EBOOK = os.path.join(BASE, "Band1_Cover_eBook_1600x2560.png")


# --------------------------------------------------------------------------
def load_font(size):
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    print("  ! Keine Serifen-Schrift gefunden -- Ruecken wird mit Standardfont gesetzt.")
    return ImageFont.load_default()


def fit_panel(path, w, h):
    """Skaliert proportional bis die Flaeche gefuellt ist, dann zentrierter Crop.

    Nie verzerren -- KDP-Cover mit gestauchten Gesichtern fallen sofort auf.
    """
    im = Image.open(path).convert("RGB")
    sw, sh = im.size
    scale = max(w / sw, h / sh)
    nw, nh = round(sw * scale), round(sh * scale)
    im = im.resize((nw, nh), Image.LANCZOS)
    left, top = (nw - w) // 2, (nh - h) // 2
    return im.crop((left, top, left + w, top + h))


def draw_spine(w, h):
    """Setzt den Buchruecken: Nummer / Titel / Serie / Autor, von unten nach oben."""
    # Waagerecht aufbauen (Laenge = Buchhoehe), am Ende um 90 Grad drehen.
    strip = Image.new("RGB", (h, w), SPINE_BG)
    d = ImageDraw.Draw(strip)

    safe = round(0.0625 * DPI)          # 1,6 mm KDP-Mindestabstand zu den Kanten
    usable = w - 2 * safe
    if usable < 30:
        print("  ! Ruecken zu schmal fuer Text (%d px nutzbar) -- bleibt leer." % usable)
        return strip.rotate(90, expand=True)

    def centered(text, font, fill, x_center):
        bb = d.textbbox((0, 0), text, font=font)
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        d.text((x_center - tw / 2, (w - th) / 2 - bb[1]), text, font=font, fill=fill)
        return tw

    # Groessen an der nutzbaren Ruckenbreite ausrichten
    f_num = load_font(max(14, int(usable * 0.85)))
    f_title = load_font(max(12, int(usable * 0.55)))
    f_series = load_font(max(9, int(usable * 0.30)))
    f_author = load_font(max(10, int(usable * 0.38)))

    # x laeuft hier entlang der Buchhoehe. Gedreht wird im Uhrzeigersinn
    # (rotate(-90)), dabei wandert x = 0 nach OBEN und der waagerechte Text
    # laeuft danach von oben nach unten.
    #
    # NACHGEMESSEN an Band 2 und Band 3: beide Ruecken laufen von OBEN NACH
    # UNTEN. (Das Band-3-Konzeptdokument behauptet "von unten nach oben,
    # deutsche Konvention" -- das Cover macht es anders. Massgeblich ist das
    # gedruckte Buch, sonst steht Band 1 im Regal falsch herum.)
    centered(SPINE_NUMBER, f_num, GOLD, int(h * 0.12))
    centered(SPINE_TITLE, f_title, CREME, int(h * 0.40))
    centered(SPINE_SERIES, f_series, GOLD, int(h * 0.62))
    centered(SPINE_AUTHOR, f_author, CREME, int(h * 0.88))

    return strip.rotate(-90, expand=True)


def main():
    for p in (FRONT, BACK):
        if not os.path.exists(p):
            print("FEHLT: %s" % p)
            print("       Erst die Illustrationen erzeugen und Typografie setzen,")
            print("       siehe Cover_Konzept_Band1.md, Abschnitt 10.")
            return

    spine_in = PAGE_COUNT * SPINE_FACTOR
    total_w_in = TRIM_W + BLEED + spine_in + TRIM_W + BLEED
    total_h_in = TRIM_H + 2 * BLEED

    TW, TH = round(total_w_in * DPI), round(total_h_in * DPI)
    panel_w = round((TRIM_W + BLEED) * DPI)
    spine_w = TW - 2 * panel_w

    print("Band 1 -- Full-Cover")
    print("  Seitenzahl:  %d %s" % (PAGE_COUNT,
                                    "(SCHAETZUNG!)" if PAGE_COUNT_IS_ESTIMATE else ""))
    print("  Ruecken:     %.3f Zoll = %.1f mm = %d px" % (spine_in, spine_in * 25.4, spine_w))
    print("  Gesamt:      %d x %d px  (%.3f x %.3f Zoll)" % (TW, TH, total_w_in, total_h_in))

    canvas = Image.new("RGB", (TW, TH), (0, 0, 0))
    canvas.paste(fit_panel(BACK, panel_w, TH), (0, 0))
    canvas.paste(draw_spine(spine_w, TH), (panel_w, 0))
    canvas.paste(fit_panel(FRONT, panel_w, TH), (panel_w + spine_w, 0))

    canvas.save(OUT_FULL_PNG, dpi=(DPI, DPI))
    print("  -> %s" % os.path.basename(OUT_FULL_PNG))

    try:
        import img2pdf
        with open(OUT_FULL_PDF, "wb") as f:
            f.write(img2pdf.convert(
                OUT_FULL_PNG,
                layout_fun=img2pdf.get_layout_fun(
                    (img2pdf.in_to_pt(total_w_in), img2pdf.in_to_pt(total_h_in))
                )
            ))
        print("  -> %s" % os.path.basename(OUT_FULL_PDF))
    except ImportError:
        print("  ! img2pdf fehlt (pip install img2pdf) -- PDF uebersprungen.")

    # E-Book: 1:1,6 statt 1:1,5 -> eigener Beschnitt, nicht bloss kleiner
    fit_panel(FRONT, 1600, 2560).save(OUT_EBOOK)
    print("  -> %s (E-Book, 1:1,6)" % os.path.basename(OUT_EBOOK))

    if PAGE_COUNT_IS_ESTIMATE:
        print()
        print("  ACHTUNG: PAGE_COUNT ist geschaetzt. Vor dem KDP-Upload durch die")
        print("           echte Seitenzahl aus dem Previewer ersetzen und")
        print("           PAGE_COUNT_IS_ESTIMATE = False setzen.")


if __name__ == "__main__":
    main()
