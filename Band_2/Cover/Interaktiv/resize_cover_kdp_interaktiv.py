#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resize_cover_kdp_interaktiv.py — bringt das generierte Full-Cover auf exakte
KDP-Maße für die INTERAKTIV-Ausgabe (5 x 8 Zoll, 300 dpi).

Basiert auf Band_2/Cover/resize_cover_kdp.py (Linear, 6x9), angepasst:
  - Format 5 x 8 Zoll (Interaktiv, wie Band 1 Interaktiv)
  - Eingabe direkt als PNG (nicht PDF)
  - Seitenzahl 195, weißes Papier

Ausgabe:
  - <name>_KDP_5x8_300dpi.png  (hochaufgelöst, exakte Maße)
  - <name>_KDP_5x8_300dpi.pdf  (druckfertig für KDP-Upload)
"""

from PIL import Image
import img2pdf
import os

# === EINSTELLUNGEN ===
BASE       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../Band_2/Cover
INPUT_PNG  = os.path.join(BASE, "cover_v1_band2_full_interaktiv.png")
OUT_BASE   = os.path.join(BASE, "Interaktiv", "Band2_Interaktiv_Cover_KDP_5x8_300dpi_460S")
DPI        = 300

# === KDP-ZIELMASSE ===
# Direkt vom KDP-Backend uebernommen (460 Seiten, 5x8, weiss): 11.286 x 8.250 Zoll.
# Zuverlaessiger als selbst rechnen -> genau diese Masse nutzen.
total_w_inch = 11.286
total_h_inch = 8.250

target_w = round(total_w_inch * DPI)   # 3386
target_h = round(total_h_inch * DPI)   # 2475

print(f"Format:      5 x 8 Zoll, 460 Seiten, weiss, {DPI} dpi")
print(f"KDP-Zielmass:{total_w_inch} x {total_h_inch} Zoll = {target_w} x {target_h} px")

# === LADEN & SKALIEREN ===
img = Image.open(INPUT_PNG).convert("RGB")
print(f"Original:    {img.width} x {img.height} px  (Verhaeltnis {img.width/img.height:.4f})")
print(f"Ziel-Verh.:  {target_w/target_h:.4f}")

img_resized = img.resize((target_w, target_h), Image.LANCZOS)

# === PNG speichern (mit korrektem DPI-Tag) ===
out_png = OUT_BASE + ".png"
img_resized.save(out_png, dpi=(DPI, DPI))
print(f"PNG:         {out_png}")

# === PDF speichern (exakte physische Maße) ===
out_pdf = OUT_BASE + ".pdf"
with open(out_pdf, "wb") as f:
    f.write(img2pdf.convert(
        out_png,
        layout_fun=img2pdf.get_layout_fun(
            (img2pdf.in_to_pt(total_w_inch), img2pdf.in_to_pt(total_h_inch))
        )
    ))
print(f"PDF:         {out_pdf}")
print("Fertig.")
