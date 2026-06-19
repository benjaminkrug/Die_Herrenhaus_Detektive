from pdf2image import convert_from_path
from PIL import Image
import img2pdf
import os

# === EINSTELLUNGEN ===
INPUT_PDF  = r"Band_2/Cover/Band 2Cover_full_v1 (1).pdf"
OUTPUT_PDF = r"Band_2/Cover/Band2_Cover_KDP_6x9_300dpi.pdf"
PAGE_COUNT = 158          # Tatsaechliche Seitenanzahl laut KDP-Vorschau
PAPER      = "white"      # "white" oder "cream"
DPI        = 300

# === BERECHNUNGEN ===
BLEED      = 0.125        # Zoll Beschnitt rundherum
PAGE_W     = 6.0
PAGE_H     = 9.0
SPINE_FACTOR = 0.002252 if PAPER == "white" else 0.0025

spine_inch = PAGE_COUNT * SPINE_FACTOR
total_w_inch = PAGE_W + BLEED + spine_inch + PAGE_W + BLEED
total_h_inch = PAGE_H + BLEED + BLEED

target_w = round(total_w_inch * DPI)
target_h = round(total_h_inch * DPI)

print(f"Zielgroesse: {target_w} x {target_h} px")
print(f"Spine: {spine_inch:.3f} Zoll = {round(spine_inch * DPI)} px")

# === KONVERTIERUNG ===
pages = convert_from_path(INPUT_PDF, dpi=DPI)
img = pages[0]  # Full cover ist 1 Seite

print(f"Original-Groesse: {img.width} x {img.height} px")

# Auf KDP-Masse skalieren
img_resized = img.resize((target_w, target_h), Image.LANCZOS)

# Als temporaeres PNG speichern
tmp_png = OUTPUT_PDF.replace(".pdf", "_tmp.png")
img_resized.save(tmp_png, dpi=(DPI, DPI))

# Als PDF mit korrektem DPI speichern
with open(OUTPUT_PDF, "wb") as f:
    f.write(img2pdf.convert(
        tmp_png,
        layout_fun=img2pdf.get_layout_fun(
            (img2pdf.in_to_pt(total_w_inch),
             img2pdf.in_to_pt(total_h_inch))
        )
    ))

os.remove(tmp_png)
print(f"Fertig: {OUTPUT_PDF}")
