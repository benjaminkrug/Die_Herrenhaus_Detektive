#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_umlaute.py — Vereinheitlicht ASCII-Umlaute (ae/oe/ue/ss) zu echten
Umlauten (ä/ö/ü/ß) in den Abschnitt-Dateien.

FAK-H001: 105 von 128 Dateien mischen ASCII und echte Umlaute. Das ist im
gedruckten Buch sichtbar. Ziel: durchgaengig echte Umlaute (wie Shared Start
und Band 1).

Sicherheit: ss->ß wird NICHT automatisch gemacht (zu fehleranfaellig:
'Wasser', 'Fluss', 'muss', 'dass', 'Strasse' vs 'straße' — deutsche
ss/ß-Regel braucht Wortwissen). Nur ae/oe/ue->ä/ö/ü, und NUR fuer Woerter,
die nicht in der EXCEPTIONS-Liste stehen (echte Buchstabenfolge ue/ae/oe).

Nutzung:
  python fix_umlaute.py            # Dry-Run: zeigt, was sich aendern wuerde
  python fix_umlaute.py --write    # schreibt die Aenderungen
"""

import re
import sys
from pathlib import Path
from collections import Counter

BASE = Path(__file__).parent / "Abschnitte"

# Woerter, in denen ae/oe/ue eine ECHTE Buchstabenfolge ist (kein Umlaut).
# Kleingeschrieben verglichen; deckt Flexionsformen ueber Praefix-Match ab,
# wo eindeutig (siehe SAFE_PREFIXES).
EXCEPTIONS = {
    # -ue- echt
    "quelle", "quellen", "quellwasser", "heilquelle",
    "abenteuer", "abenteuerfilm", "abenteuern",
    "neu", "neue", "neuer", "neues", "neuen", "neuem",
    "euer", "eure", "euren", "eurem", "eurer", "euch",
    "bauen", "bauten", "gebauten", "erbauen",
    "hauen", "gehauen", "behauenem", "draufhauen",
    "schauen", "zuschauen", "anschauen",
    "genau", "genauer", "genauso", "genaue", "genauen",
    "zuerst", "quer", "querab",
    "gedauert", "dauert", "dauerte", "dauern", "andauernd",
    "steuer", "steuern", "abenteuerlich",
    "bereue", "bereuen",
    "feuer", "feuers",
    "teuer", "teure",
    "kauend", "kauen",
    "mauer", "mauern", "steinmauern", "rueckwand",  # Mauer echt (rueckwand faelschlich? -> siehe unten)
    # -ae- echt
    "israel", "michael", "raphael",
    "graue", "grauem", "grauer", "graues",  # grau + Endung (Grau, nicht grä)
    "raue", "rauem", "rauer", "raues",       # rau + Endung
    "blaue", "blaues", "blauem", "blauen", "blauer",
    "schlaue", "genaue",
    # -oe- echt (selten im Deutschen)
    "poesie",
    # -ue- als u+ell (visuell, aktuell, individuell, manuell)
    "visuell", "visuelle", "aktuell", "aktuelle", "individuell", "manuell",
}

# Woerter, die trotz Praefix-Match NICHT als Ausnahme gelten sollen
# (z.B. 'neuer' ist Ausnahme, aber 'neugier' nicht relevant). Leer lassen,
# EXCEPTIONS ist exakt-match.

WORD_RE = re.compile(r"[A-Za-zäöüßÄÖÜ]+")

# Kern-Regel: 'ue'->'ü' etc. NUR wenn dem Paar kein weiterer Vokal
# unmittelbar vorausgeht. Denn 'aue/aeu/eue/oue' sind echte Diphthong-
# Folgen (bauen, Mauer, Feuer, trauen, Augenbrauen), kein Umlaut-Ersatz.
# Beispiele die geschuetzt bleiben: Vertrauen, Feuerwehr, schauen, Quelle
# (qu+e), Abenteuer (eu+er). Beispiele die ersetzt werden: Tuer->Tür,
# Haende->Hände (kein Vokal vor ue/ae).
UML = {"ue": "ü", "ae": "ä", "oe": "ö", "Ue": "Ü", "Ae": "Ä", "Oe": "Ö"}
PAIR_RE = re.compile(r"(?<![aeiouäöüAEIOUÄÖÜqQ])(ue|ae|oe|Ue|Ae|Oe)")

# Versalien (Ausrufe wie "MUESSEN"): UE/AE/OE -> Ü/Ä/Ö, gleiche Diphthong-/q-
# Schutzregel. Schuetzt QUELLE (q davor), VISUELLE/AUSSER (Vokal davor).
UML_CAPS = {"UE": "Ü", "AE": "Ä", "OE": "Ö"}
CAPS_PAIR_RE = re.compile(r"(?<![AEIOUÄÖÜQ])(UE|AE|OE)")


# Eindeutige ss->ß-Faelle (nach langem Vokal/Diphthong). Bewusst kurz und
# exakt gehalten — kein automatisches ss->ß (Wasser, muss, Fluss bleiben ss).
SS_FIX = {
    "weiss": "weiß", "weisst": "weißt",
    "füssen": "füßen", "füsse": "füße",
    "sass": "saß", "sassen": "saßen",
    "fliesst": "fließt", "fliessen": "fließen",
    "dreissig": "dreißig", "siebenunddreissig": "siebenunddreißig",
    "grösser": "größer", "grösse": "größe", "grössere": "größere",
    "grösseren": "größeren", "grösster": "größter",
    "grüsse": "grüße", "begrüsst": "begrüßt", "grüsst": "grüßt", "grüssen": "grüßen",
    "süss": "süß", "süssem": "süßem", "süsse": "süße", "süsser": "süßer",
    "gleichmässig": "gleichmäßig",
    "draussen": "draußen",
    # weitere eindeutige ß-Faelle (nach langem Vokal/Diphthong)
    "schliesslich": "schließlich", "wegschliessen": "wegschließen",
    "fuss": "fuß",
    "gross": "groß", "grosse": "große", "grossen": "großen",
    "grossem": "großem", "grosser": "großer", "grossartig": "großartig",
    "liess": "ließ", "liessen": "ließen",
    "weisses": "weißes", "weissen": "weißen", "weisse": "weiße", "weisser": "weißer",
    "heiss": "heiß", "heisst": "heißt", "heissen": "heißen", "heisse": "heiße",
    "stiess": "stieß", "stiessen": "stießen",
    "reissen": "reißen", "reisst": "reißt",
    "schweiss": "schweiß",
    "eingemeisselt": "eingemeißelt",
}


def _apply_ss(w: str) -> str:
    key = w.lower()
    if key in SS_FIX:
        fixed = SS_FIX[key]
        # Grossschreibung des Originals uebernehmen
        if w[:1].isupper():
            return fixed[:1].upper() + fixed[1:]
        return fixed
    return w


def convert_word(w: str) -> str:
    if w.lower() in EXCEPTIONS:
        return w
    # Versalien-Ausrufe (MUESSEN, KOENNEN) vor der normalen Regel behandeln
    if w.isupper() and len(w) > 1:
        w = CAPS_PAIR_RE.sub(lambda m: UML_CAPS[m.group(1)], w)
    else:
        w = PAIR_RE.sub(lambda m: UML[m.group(1)], w)
    # ss->ß nach Umlaut-Konvertierung (arbeitet auf ASCII-Rest)
    w = _apply_ss(w)
    # Tippfehler mitkorrigieren
    if w in TYPO_FIX:
        w = TYPO_FIX[w]
    return w


# Echte Tippfehler (keine Umlaut-Frage), die beim Durchlauf mitkorrigiert
# werden. Keys nach Umlaut-Konvertierung.
TYPO_FIX = {
    "flüsserte": "flüsterte",
    "Handfäche": "Handfläche",
    "Kühschrank": "Kühlschrank",
    "glückerte": "gluckerte",
}


def process_text(text: str):
    changes = Counter()

    def repl(m):
        w = m.group(0)
        nw = convert_word(w)
        if nw != w:
            changes[(w, nw)] += 1
        return nw

    new = WORD_RE.sub(repl, text)
    return new, changes


def main():
    write = "--write" in sys.argv
    files = sorted(BASE.glob("Abschnitt_*.md"))
    total = Counter()
    changed_files = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        new, changes = process_text(text)
        if changes:
            changed_files += 1
            total.update(changes)
            if write:
                f.write_text(new, encoding="utf-8")

    print(f"Dateien mit Aenderungen: {changed_files}/{len(files)}")
    print(f"Ersetzungen gesamt: {sum(total.values())}")
    print(f"Verschiedene Woerter: {len(total)}")
    print()
    print("Top-Ersetzungen (Kontrolle — sind hier False Positives dabei?):")
    for (w, nw), c in total.most_common(60):
        print(f"  {c:4d}  {w:22s} -> {nw}")
    if not write:
        print("\n(DRY-RUN — nichts geschrieben. Mit --write anwenden.)")


if __name__ == "__main__":
    main()
