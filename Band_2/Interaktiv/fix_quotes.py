#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_quotes.py — Vereinheitlicht Dialog-Anfuehrungszeichen auf den Buch-Standard.

Buch-Standard (Mehrheit der Abschnitte): OEFFNEND „ (U+201E) + SCHLIESSEND
gerade " (U+0022), also  „Text".

Einige Abschnitte weichen ab: sie oeffnen ebenfalls mit geradem " statt „.
Dieses Skript wandelt NUR das oeffnende gerade " in „ um; das schliessende
gerade " bleibt. Ergebnis entspricht dem Buch-Standard „Text".

Oeffnend vs. schliessend: ein gerades " ist OEFFNEND, wenn davor Zeilenanfang,
Leerzeichen, ( oder Gedankenstrich steht — sonst SCHLIESSEND. Bereits
vorhandene „ (U+201E) bleiben unangetastet.

Nutzung:
  python fix_quotes.py            # Dry-Run (zeigt betroffene Dateien)
  python fix_quotes.py --write    # anwenden
"""

import re
import sys
from pathlib import Path

BASE = Path(__file__).parent / "Abschnitte"
OPEN_Q = "„"       # U+201E
STRAIGHT = '"'     # U+0022

# Oeffnendes gerades ": am Zeilenanfang oder nach Leerzeichen/Klammer.
# WICHTIG: KEIN Gedankenstrich (—) als Trigger! Nach — steht oft eine
# ABGEBROCHENE Rede, die geschlossen wird ("...erwärmt —"), kein neues
# Zitat. Ein „ nach — waere falsch.
OPENING_RE = re.compile(r'(^|[\s(*>])"')


def convert(text: str):
    # nur oeffnende gerade Quotes -> „
    new, n = OPENING_RE.subn(lambda m: m.group(1) + OPEN_Q, text)
    return new, n


def main():
    write = "--write" in sys.argv
    total = 0
    files_changed = 0
    for f in sorted(BASE.glob("Abschnitt_*.md")):
        text = f.read_text(encoding="utf-8")
        if STRAIGHT not in text:
            continue
        new, n = convert(text)
        if n == 0:
            continue
        # Nur schreiben, wenn sich wirklich oeffnende Quotes fanden
        files_changed += 1
        total += n
        print(f"  {f.name}: {n} oeffnende Quotes -> „")
        if write:
            f.write_text(new, encoding="utf-8")
    print(f"\nDateien geaendert: {files_changed} | oeffnende Quotes ersetzt: {total}")
    if not write:
        print("(DRY-RUN — nichts geschrieben. Mit --write anwenden.)")


if __name__ == "__main__":
    main()
