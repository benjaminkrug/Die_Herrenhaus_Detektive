# -*- coding: utf-8 -*-
"""
Bringt das Band-3-Full-Cover auf KDP-Masse (6x9 Zoll, 300 dpi, weisses Papier).
Proportionale Skalierung + symmetrischer Center-Crop (KEINE Verzerrung).
PAGE_COUNT muss spaeter durch die ECHTE Seitenzahl aus dem KDP-Previewer ersetzt werden.
"""
from PIL import Image
import img2pdf, os

INPUT  = "DIE SCHATTENJAEGER_voll_v1.png"
OUT_PNG = "Band3_Cover_KDP_6x9_300dpi.png"
OUT_PDF = "Band3_Cover_KDP_6x9_300dpi.pdf"

DPI = 300
BLEED = 0.125
PW, PH = 6.0, 9.0
PAGE_COUNT = 105          # SCHAETZUNG - mit echter KDP-Seitenzahl ersetzen!
SPINE_FACTOR = 0.002252   # weisses Papier

spine = PAGE_COUNT * SPINE_FACTOR
total_w = PW + BLEED + spine + PW + BLEED
total_h = PH + BLEED + BLEED
TW = round(total_w * DPI)
TH = round(total_h * DPI)

print(f"Ziel: {TW} x {TH} px  | Spine {spine*25.4:.1f} mm  | {PAGE_COUNT} Seiten")

im = Image.open(INPUT).convert("RGB")
sw, sh = im.size
print(f"Quelle: {sw} x {sh}")

# proportional so skalieren, dass Zielflaeche komplett gefuellt ist (cover), dann zentriert croppen
scale = max(TW / sw, TH / sh)
nw, nh = round(sw * scale), round(sh * scale)
im2 = im.resize((nw, nh), Image.LANCZOS)

left = (nw - TW) // 2
top  = (nh - TH) // 2
im3 = im2.crop((left, top, left + TW, top + TH))
print(f"Skaliert auf {nw}x{nh}, Crop links/oben={left}/{top}  -> {im3.size}")

im3.save(OUT_PNG, dpi=(DPI, DPI))

with open(OUT_PDF, "wb") as f:
    f.write(img2pdf.convert(
        OUT_PNG,
        layout_fun=img2pdf.get_layout_fun(
            (img2pdf.in_to_pt(total_w), img2pdf.in_to_pt(total_h))
        )
    ))
print(f"Fertig: {OUT_PNG} + {OUT_PDF}")
