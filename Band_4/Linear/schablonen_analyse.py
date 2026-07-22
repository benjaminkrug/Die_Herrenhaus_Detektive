#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Schablonen- und Varianz-Analyse -- Band 4 (Die Herrenhaus-Detektive)

Portierung von Band_1/Interaktiv/schablonen_analyse.py (dort auf Abschnitte/,
hier auf Kapitel/), erweitert um die VARIANZ-Messung.

Warum die Erweiterung (PLAN_Band4.md Abschnitt 6.B):
    Das Alt-Skript zaehlt nur die HAEUFIGKEIT von Floskeln. Der eigentliche
    Verraeter von KI-Text ist aber GLEICHFOERMIGKEIT. Ein Kapitel, in dem jeder
    Satz neun Woerter hat, erfuellt jede Regel in CLAUDE.md und liest sich
    trotzdem maschinell.

GRUNDREGEL (PLAN_Band4.md 6.0): Kandidaten, keine Urteile.

Aufruf:
    python schablonen_analyse.py                 # Band_4/Linear/Kapitel
    python schablonen_analyse.py <verzeichnis>   # Kalibrierung, z.B. Band 3
"""
import re, os, sys, glob, io, collections, statistics

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ------------------------------------------------- Schablonen (aus Band 1)
# An echtem Text DIESER Serie kalibriert -- inkl. dokumentiertem
# False-Positive-Test bei "schluckte". Nicht neu erfinden.
SCHABLONEN = {
    # Koerperreaktions-Klischees
    "verschraenkte die Arme":  r"verschränkte? (die )?arme",
    "Kribbeln/kribbelte":      r"kribbel",
    "Herz klopfte/pochte":     r"herz (klopfte|pochte|schlug|raste|hämmerte)",
    "Schauer ueber den Ruecken": r"schauer .{0,15}rücken|kalter schauer",
    "Gaensehaut":              r"gänsehaut",
    "Magen/Bauch zog sich":    r"(magen|bauch) zog sich",
    "schluckte":               r"\bschluckte\b(?!\s+(den\s+letzten|einen)?\s*\w*(bissen|schluck|waffel|wasser|limo))",
    "Atem stockte/anhalten":   r"atem stockte|hielt (den )?atem|luft anhalten",
    "Knoten im Bauch":         r"knoten im (bauch|magen)",
    "Nackenhaare":             r"nackenhaar",
    "rollte mit den Augen":    r"rollte (mit )?(den )?augen|augen rollen",
    "Puls raste":              r"puls (raste|hämmerte)",
    # Dialog-Tics
    "fluesterte":              r"\bflüsterte\b",
    "hauchte":                 r"\bhauchte\b",
    # Fuellsatz-/Uebergangsmuster
    "'Einen Moment lang'":     r"einen (moment|augenblick) lang",
    "'Fuer einen Moment'":     r"für einen (moment|augenblick)",
    "'Dann, ploetzlich'":      r"dann,? plötzlich|plötzlich,? ",
    "'Und dann'":              r"\bund dann\b",
    "'Sekundenlang'":          r"sekundenlang|minutenlang",
    "'Etwas stimmte nicht'":   r"etwas (stimmte|war) nicht",
    "'Es war, als ob'":        r"es war,? als (ob|würde)",
    "'konnte nicht glauben'":  r"konnte .{0,10}nicht glauben",
    "'Stille.'-Einwortsatz":   r"(?m)^\s*Stille\.\s*$",
}

DIALOGVERBEN = ["sagte", "fragte", "rief", "flüsterte", "murmelte", "brummte",
                "meinte", "antwortete", "zischte", "stöhnte", "lachte", "schrie",
                "erklärte", "keuchte", "wisperte", "hauchte", "raunte",
                "stammelte", "jammerte", "seufzte", "nickte", "knurrte"]


def kapnum(p):
    m = re.search(r"Kapitel(\d+)", os.path.basename(p))
    return int(m.group(1)) if m else 0


def load(path):
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


def main(kapdir):
    files = sorted(glob.glob(os.path.join(kapdir, "*.md")), key=kapnum)
    if not files:
        print("Keine Kapitel in %s -- noch nichts geschrieben." % kapdir)
        return

    per_phrase = collections.Counter()
    per_file = collections.defaultdict(list)
    sent_starts = collections.Counter()
    total_words = total_sents = 0
    varianz = []

    for path in files:
        n = kapnum(path)
        raw = open(path, encoding="utf-8").read()
        body = load(path)
        words = len(body.split())
        total_words += words

        for label, pat in SCHABLONEN.items():
            c = len(re.findall(pat, raw, flags=re.I))
            if c:
                per_phrase[label] += c
                per_file[label].append((n, c))

        # Saetze
        flat = re.sub(r"\s+", " ", body)
        sents = [s.strip() for s in re.split(r"(?<=[.!?“\"])\s+", flat) if s.strip()]
        slen = [len(s.split()) for s in sents]
        total_sents += len(sents)
        for s in sents:
            m = re.match(r"[„\"]?(\w+)", s)
            if m:
                sent_starts[m.group(1).lower()] += 1

        # Absaetze (durch Leerzeile getrennt)
        paras = [p for p in re.split(r"\n\s*\n", body) if p.strip()]
        plen = [len(p.split()) for p in paras]

        # Dialogverben-Vielfalt
        verben = {v for v in DIALOGVERBEN if re.search(r"\b" + v + r"\b", raw, re.I)}

        varianz.append({
            "kap": n,
            "s_mit": statistics.mean(slen) if slen else 0,
            "s_std": statistics.pstdev(slen) if len(slen) > 1 else 0,
            "p_mit": statistics.mean(plen) if plen else 0,
            "p_std": statistics.pstdev(plen) if len(plen) > 1 else 0,
            "verben": len(verben),
        })

    print("SCHABLONEN- UND VARIANZ-ANALYSE  --  %s" % kapdir)
    print("Gemessen: %d Woerter, %d Saetze, %d Kapitel\n"
          % (total_words, total_sents, len(files)))

    print("=== A. SCHABLONEN (Haeufigkeit) ===")
    print("%-30s %5s %8s  %s" % ("Schablone", "ges", "/10k W", "Haeufungen (Kap x N)"))
    for label, c in per_phrase.most_common():
        per10k = round(c / total_words * 10000, 1)
        tops = sorted(per_file[label], key=lambda x: -x[1])[:3]
        top = ", ".join("K%dx%d" % (k, v) for k, v in tops if v >= 2)
        print("%-30s %5d %8s  %s" % (label, c, per10k, top))
    if not per_phrase:
        print("  keine Treffer")

    print("\n=== B. VARIANZ -- der eigentliche KI-Verraeter ===")
    print("Gleichfoermigkeit faellt auf, auch wenn jede Einzelregel erfuellt ist.")
    print("%3s %9s %9s %10s %9s %8s"
          % ("Kap", "SatzMit", "SatzStd", "AbsatzMit", "AbsatzStd", "DlgVerb"))
    print("-" * 56)
    for v in varianz:
        print("%3d %9.1f %9.1f %10.1f %9.1f %8d"
              % (v["kap"], v["s_mit"], v["s_std"], v["p_mit"], v["p_std"], v["verben"]))
    print("-" * 56)
    sstd = [v["s_std"] for v in varianz]
    pstd = [v["p_std"] for v in varianz]
    vb = [v["verben"] for v in varianz]
    print("Satzlaengen-Streuung: min %.1f  Schnitt %.1f   (klein = monoton)"
          % (min(sstd), statistics.mean(sstd)))
    print("Absatz-Streuung:      min %.1f  Schnitt %.1f"
          % (min(pstd), statistics.mean(pstd)))
    print("Dialogverben je Kap:  min %d    Schnitt %.1f   (wenige = eintoenig)"
          % (min(vb), statistics.mean(vb)))

    print("\n=== C. SATZANFANG-MONOTONIE (Top 12) ===")
    for w, c in sent_starts.most_common(12):
        print("  %-14s %5d  (%.1f%%)" % (w, c, 100 * c / total_sents))

    print("\nHinweis: Kandidaten, keine Urteile. Jeder Treffer wird im Kontext")
    print("gelesen und einzeln entschieden (PLAN_Band4.md Abschnitt 6.0).")


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "Kapitel"))
