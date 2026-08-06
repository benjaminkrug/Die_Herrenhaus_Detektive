#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QA-Messung -- Band 4 (Die Herrenhaus-Detektive)

Mechanische Messung gegen die Schreibregeln aus CLAUDE.md.
Zusammenfuehrung von Band_3/Linear/feinschliff_messung.py und _dlg_check.py,
plus zwei Pruefungen, die bisher fehlten (Kapitellaenge, Cliffhanger).

GRUNDREGEL (PLAN_Band4.md Abschnitt 6.0):
    Dieses Skript liefert KANDIDATEN, keine Urteile.
    Kein Zielwert ist eine Huerde. Nichts wird automatisch geaendert.
    "Geprueft, bleibt so" ist ein vollwertiges Ergebnis.

Aufruf:
    python qa_messung.py                 # Band_4/Linear/Kapitel
    python qa_messung.py <verzeichnis>   # z.B. zur Kalibrierung an Band 3
"""
import re, os, sys, glob, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ---------------------------------------------------------------- Regeln
MIN_W, MAX_W = 900, 1500          # PLAN_Band4 Abschnitt 4
MAX_W_KAP3   = 1550               # dokumentierte Ausnahme (nur Kapitel 3)
SATZ_MAX     = 15                 # CLAUDE.md: max 15 Woerter

# DIALOG -- zwei Werte, und das ist wichtig:
#   CLAUDE.md fordert 40 %. Gemessen an Woertern erreicht das FERTIGE, vom Autor
#   abgenommene Band 3 aber nur 29 % im Schnitt (Spanne 16-50 %); 16 von 19
#   Kapiteln liegen unter 40. Verifiziert gegen Band_3/Linear/_dlg_check.py --
#   identische Zahlen, die Messung ist also korrekt.
#   Folge: 40 % als Flag wuerde fast jedes Kapitel markieren = Rauschen.
#   Deshalb wird gegen die PRAXIS der Reihe geflaggt, die Regel bleibt als
#   Referenz sichtbar.
DIALOG_REGEL    = 40              # CLAUDE.md (Referenz)
DIALOG_BAND3    = 29              # Praxis Band 3 (Schnitt)
DIALOG_FLAG     = 20              # darunter: deutlich dialogaermer als die Reihe

# Verbotene abstrakte Emotionen (CLAUDE.md: koerperlich, nie abstrakt)
ABSTRAKT = [
    r"seltsames? Gef[uü]hl", r"komisches? Gef[uü]hl", r"ungutes? Gef[uü]hl",
    r"merkw[uü]rdiges? Gef[uü]hl", r"\bsp[uü]rte\b", r"myster[iö]", r"observier",
    r"f[uü]hlte sich .{0,20} an wie ein", r"irgendein Gef[uü]hl",
]
PASSIV = re.compile(r"\b(wird|wurde|wurden|werden|worden)\b\s+\w*\s*\b\w+(t|en)\b", re.I)

# CLIFFHANGER -- KEINE Heuristik mehr.
#   Erster Versuch mit Mustern (Fragezeichen, Ausruf, direkte Rede am Schluss,
#   "ploetzlich") markierte 16 von 19 Band-3-Kapiteln als verdaechtig -- obwohl
#   Band 3 durchgehend Cliffhanger hat. 84 % Fehlalarm = wertlos.
#   Grund: Ein Cliffhanger ist SEMANTISCH, nicht syntaktisch. "Und dann brach
#   der Stein" hat kein Satzzeichen, das ihn verraet.
#   Deshalb: Das Skript druckt die letzten Zeilen jedes Kapitels untereinander.
#   Neunzehn Schluesse auf einem Bildschirm -- in zwei Minuten mit dem Auge
#   geprueft. Das UNTERSTUETZT das Lesen, statt es vorzutaeuschen.

OPEN_Q = "„"                 # „
CLOSE_Q = "[\"“]"            # " oder "


def kapnum(p):
    m = re.search(r"Kapitel(\d+)", os.path.basename(p))
    return int(m.group(1)) if m else 0


def load(path):
    """Kapiteltext ohne Ueberschriften, Trenner und Nachspann."""
    raw = open(path, encoding="utf-8").read().split("\n")
    started, body = False, []
    for ln in raw:
        if ln.startswith("# Kapitel") or ln.startswith("# Epilog"):
            started = True
            continue
        if not started:
            continue
        s = ln.strip()
        if s.startswith("*Ende von Band") or s.startswith("*Die Herrenhaus"):
            continue
        if s == "---" or s.startswith("#"):
            continue
        body.append(ln)
    return "\n".join(body)


def saetze(text):
    # Markdown-Auszeichnung entfernen, BEVOR getrennt wird.
    # Sonst haengt "...fragen soll.*" mit dem Folgesatz zusammen (der Punkt wird
    # vom Sternchen verdeckt) -- das erzeugt Phantom-Saetze von 20+ Woertern.
    t = re.sub(r"[*_]{1,2}", "", text)
    t = re.sub(r"\s+", " ", t.replace("\n", " "))
    return [p.strip() for p in re.split(r"(?<=[.!?“\"])\s+", t) if p.strip()]


def dialog_prozent(text):
    """WORT-Methode (nicht Zeilen!) -- siehe PLAN_Band4 Abschnitt 6.A.

    feinschliff_messung.py zaehlte ZEILEN mit Anfuehrungszeichen; eine Zeile mit
    einem einzigen zitierten Wort galt damit voll als Dialog. Das ueberschaetzt
    den Anteil systematisch.
    """
    gesamt = len(text.split())
    if not gesamt:
        return 0
    drin = re.findall(OPEN_Q + r"(.*?)" + CLOSE_Q, text, flags=re.S)
    return round(100 * sum(len(d.split()) for d in drin) / gesamt)


def schluss(text, zeilen=2):
    """Letzte Zeilen -- zum Selberlesen, nicht zum Automatisch-Bewerten."""
    return [l.strip() for l in text.split("\n") if l.strip()][-zeilen:]


def main(kapdir):
    files = sorted(glob.glob(os.path.join(kapdir, "*.md")), key=kapnum)
    if not files:
        print("Keine Kapitel in %s -- noch nichts geschrieben." % kapdir)
        return

    print("QA-MESSUNG  --  %s\n" % kapdir)
    print("%3s %7s %6s %5s %5s %7s %6s %6s %s"
          % ("Kap", "Woerter", "Saetze", ">15W", "maxW", "Dialog", "abstr", "passiv", ""))
    print("-" * 62)

    lang, dlg, alle_probleme, schluesse = [], [], {}, {}
    for f in files:
        n = kapnum(f)
        body = load(f)
        w = len(body.split())
        s = saetze(body)
        laengen = [len(x.split()) for x in s]
        zu_lang = [(i, c) for i, c in enumerate(laengen) if c > SATZ_MAX]
        d = dialog_prozent(body)
        abstr = [m.group(0) for pat in ABSTRAKT for m in re.finditer(pat, body, re.I)]
        pas = PASSIV.findall(body)

        lang.append(w); dlg.append(d)
        obergrenze = MAX_W_KAP3 if n == 3 else MAX_W
        flags = []
        if w < MIN_W:            flags.append("kurz")
        if w > obergrenze:       flags.append("lang")
        if d < DIALOG_FLAG:      flags.append("dialogarm")
        alle_probleme[n] = {"lang": zu_lang, "abstr": abstr, "saetze": s}
        schluesse[n] = schluss(body)

        print("%3d %7d %6d %5d %5d %6d%% %6d %6d %s"
              % (n, w, len(s), len(zu_lang), max(laengen) if laengen else 0,
                 d, len(abstr), len(pas),
                 ("<< " + " ".join(flags)) if flags else ""))

    print("-" * 62)
    print("Kapitel: %d | Woerter gesamt: %d | Schnitt: %d"
          % (len(files), sum(lang), sum(lang) // len(lang)))
    print("Kapitellaenge: min %d, max %d  (Fenster %d-%d, Kap 3 bis %d)"
          % (min(lang), max(lang), MIN_W, MAX_W, MAX_W_KAP3))
    print("Dialog: min %d%%, max %d%%, Schnitt %d%%"
          % (min(dlg), max(dlg), sum(dlg) // len(dlg)))
    print("   Referenz: CLAUDE.md fordert %d%% | Band 3 (fertig) liegt bei %d%%"
          % (DIALOG_REGEL, DIALOG_BAND3))
    print("   Geflaggt wird erst unter %d%% -- sonst nur Rauschen." % DIALOG_FLAG)

    print("\n=== KAPITELSCHLUESSE -- selbst lesen, kein Automat ===")
    print("Pflicht laut CLAUDE.md: Cliffhanger in JEDEM Kapitel (ausser Epilog).")
    for n in sorted(schluesse):
        print("  K%-3d %s" % (n, " / ".join(schluesse[n])[:88]))

    print("\n=== LANGE SAETZE (>%d Woerter) -- Kandidaten, keine Fehler ===" % SATZ_MAX)
    for n in sorted(alle_probleme):
        for i, c in alle_probleme[n]["lang"][:3]:
            print("  K%-3d %2dW  %s" % (n, c, alle_probleme[n]["saetze"][i][:90]))

    print("\n=== ABSTRAKTE EMOTIONEN (CLAUDE.md: koerperlich statt abstrakt) ===")
    leer = True
    for n in sorted(alle_probleme):
        for a in alle_probleme[n]["abstr"][:5]:
            print("  K%-3d %s" % (n, a)); leer = False
    if leer:
        print("  keine")

    print("\nHinweis: Diese Ausgabe nennt Stellen zum Anschauen, keine Fehler.")


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "Kapitel"))
