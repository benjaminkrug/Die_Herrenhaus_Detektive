# -*- coding: utf-8 -*-
"""
Erzeugt die Rezensions-QR-Codes fuer die Herrenhaus-Detektive-Reihe.

Jeder Code fuehrt DIREKT auf das Amazon-Bewertungsformular des jeweiligen Bandes
(nicht nur auf die Produktseite) -- wie bei der Geisterspuerer-Reihe.

* JEDER erzeugte Code wird nach dem Schreiben mit OpenCV WIEDER EINGELESEN und
  gegen die Soll-URL geprueft. Ein QR-Code, der im gedruckten Buch ins Leere
  fuehrt, waere nicht mehr korrigierbar -- deshalb hier keine Annahme, sondern
  eine Messung.

* ACHTUNG ASIN: Die Gegenprobe prueft nur, dass der Code die richtige URL
  ENTHAELT. Ob die ASIN auf das richtige Produkt zeigt, kann nur der Autor
  pruefen -- die erzeugte URL im Browser oeffnen und schauen, ob die
  Bewertungsseite des richtigen Bandes (Taschenbuch) erscheint.

Verwendung:
    python build_qr_rezension.py          # alle Baende mit bekannter ASIN
    python build_qr_rezension.py --force  # vorhandene ueberschreiben
"""
import os
import sys

import qrcode
import cv2
from PIL import Image

_ROOT = os.path.dirname(os.path.abspath(__file__))

# ASINs (aus Band-3-Keyword-Recherche). VOR DEM DRUCK pruefen, dass es die
# TASCHENBUCH-ASIN ist und die URL auf die richtige Bewertungsseite fuehrt.
ASIN = {
    1: "B0GNZDSLSH",   # Das verbotene Herrenhaus
    2: "B0GV3LJ1W9",   # Das Geheimnis des Brunnens
    3: "B0H5B5WSP5",   # Die zweite Quelle
    4: "B0HBWVMTS2",   # Das versunkene Dorf
}

URL_MUSTER = "https://www.amazon.de/review/create-review?asin={asin}"


def pfad(band: int) -> str:
    # Cover-Ordner je Band (Band 1/2 haben Linear-Unterordner)
    for sub in ("Cover/Linear", "Cover"):
        d = os.path.join(_ROOT, f"Band_{band}", sub)
        if os.path.isdir(d):
            return os.path.join(d, f"qr_rezension_band{band}.png")
    return os.path.join(_ROOT, f"Band_{band}", "Cover", f"qr_rezension_band{band}.png")


def dekodiere(png_pfad: str):
    img = cv2.imread(png_pfad)
    if img is None:
        return None
    data, _, _ = cv2.QRCodeDetector().detectAndDecode(img)
    return data or None


def erzeuge(band: int, ueberschreiben: bool = False) -> bool:
    ziel = pfad(band)
    soll_url = URL_MUSTER.format(asin=ASIN[band])

    if os.path.exists(ziel) and not ueberschreiben:
        if dekodiere(ziel) == soll_url:
            print(f"  Band {band}: existiert und stimmt -- unveraendert  ({soll_url})")
            return True
        print(f"  Band {band}: existiert, Inhalt weicht ab -- mit --force neu bauen")
        return False

    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # 15 % Fehlertoleranz
        box_size=12,
        border=4,          # stiller Rand ist im Druck Pflicht, sonst unscannbar
    )
    qr.add_data(soll_url)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").save(ziel)

    ist = dekodiere(ziel)
    if ist != soll_url:
        print(f"  Band {band}: !! GEGENPROBE FEHLGESCHLAGEN")
        print(f"             erwartet: {soll_url}")
        print(f"             gelesen : {ist!r}")
        return False

    w, h = Image.open(ziel).size
    print(f"  Band {band}: erzeugt + gegengelesen OK  ({w}x{h} px)  {soll_url}")
    return True


def main():
    ueberschreiben = "--force" in sys.argv
    print("=" * 70)
    print("Rezensions-QR-Codes -- Die Herrenhaus-Detektive")
    print("=" * 70)
    ok = True
    for band in sorted(ASIN):
        if not erzeuge(band, ueberschreiben):
            ok = False
    print()
    print("WICHTIG: Erzeugte URL(s) im Browser oeffnen und pruefen, ob die")
    print("         richtige Taschenbuch-Bewertungsseite erscheint.")
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
