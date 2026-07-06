#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Schablonen-/Anti-KI-Analyse fuer Herrenhaus B1 Interaktiv.
Zaehlt wiederkehrende Formel-Wendungen, die Text 'nach KI' klingen lassen:
gleiche Koerperreaktionen, Fuellsatz-Muster, Dialog-Tics, Satzanfang-Monotonie."""
import re, glob, os, collections

ABSCHNITTE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Abschnitte")

# Phrasen-Schablonen (Regex, case-insensitiv). Gruppiert nach Typ.
SCHABLONEN = {
    # Koerperreaktions-Klischees (KI liebt sie)
    "verschränkte die Arme":   r"verschränkte? (die )?arme",
    "Kribbeln/kribbelte":      r"kribbel",
    "Herz klopfte/pochte":     r"herz (klopfte|pochte|schlug|raste|hämmerte)",
    "Schauer über den Rücken": r"schauer .{0,15}rücken|kalter schauer",
    "Gänsehaut":               r"gänsehaut",
    "Magen/Bauch zog sich":    r"(magen|bauch) zog sich",
    # schluckte NUR als Angst-Beat; woertliches Schlucken (Bissen/Schluck/Waffel)
    # ausschliessen (False-Positive-Test 2026-07-05: 1 Treffer "Bissen Waffel").
    "schluckte":               r"\bschluckte\b(?!\s+(den\s+letzten|einen)?\s*\w*(bissen|schluck|waffel|wasser|limo))",
    "Atem stockte/anhalten":   r"atem stockte|hielt (den )?atem|luft anhalten",
    "Knoten im Bauch":         r"knoten im (bauch|magen)",
    "Nackenhaare":             r"nackenhaar",
    "rollte mit den Augen":    r"rollte (mit )?(den )?augen|augen rollen",
    "Puls raste":              r"puls (raste|hämmerte)",
    # Dialog-Tics
    "flüsterte":               r"\bflüsterte\b",
    "hauchte":                 r"\bhauchte\b",
    # Fuellsatz-/Uebergangs-Muster
    "'Einen Moment lang'":     r"einen (moment|augenblick) lang",
    "'Für einen Moment'":      r"für einen (moment|augenblick)",
    "'Dann, plötzlich'":       r"dann,? plötzlich|plötzlich,? ",
    "'Und dann'":              r"\bund dann\b",
    "'Sekundenlang'":          r"sekundenlang|minutenlang",
    "'Etwas stimmte nicht'":   r"etwas (stimmte|war) nicht",
    "'Es war, als ob'":        r"es war,? als (ob|würde)",
    "'konnte nicht glauben'":  r"konnte .{0,10}nicht glauben",
    "'Stille.'-Einwortsatz":   r"(?m)^\s*Stille\.\s*$",
}

def count_words(t): return len(re.findall(r"\b\w+\b", t))

per_phrase = collections.Counter()
per_file_hits = collections.defaultdict(list)
sent_starts = collections.Counter()
total_words = 0
total_sents = 0

for path in sorted(glob.glob(os.path.join(ABSCHNITTE, "*.md"))):
    name = os.path.basename(path)
    if not name.startswith("Abschnitt_") or "Einleitung" in name:
        continue
    raw = open(path, encoding="utf-8").read()
    body = re.sub(r"^#.*$|^\*→.*$|^---.*$|^\*\*.*$", "", raw, flags=re.M)
    total_words += count_words(body)
    for label, pat in SCHABLONEN.items():
        n = len(re.findall(pat, raw, flags=re.I))
        if n:
            per_phrase[label] += n
            per_file_hits[label].append((name, n))
    # Satzanfaenge (Monotonie-Check: wie oft beginnen Saetze mit 'Er/Sie/Jonas/Mila/Ben')
    for s in re.split(r"(?<=[.!?])\s+", body):
        s = s.strip()
        if not s: continue
        total_sents += 1
        first = re.match(r"[„\"]?(\w+)", s)
        if first:
            sent_starts[first.group(1).lower()] += 1

print(f"Gemessen: {total_words} Wörter, {total_sents} Sätze (94 Story-Abschnitte)\n")

print("=== SCHABLONEN-HÄUFIGKEIT (gesamt) ===")
print(f"{'Schablone':<32}{'ges':>5}{'/10k W':>8}  Top-Dateien")
for label, n in per_phrase.most_common():
    per10k = round(n / total_words * 10000, 1)
    tops = sorted(per_file_hits[label], key=lambda x:-x[1])[:3]
    topstr = ", ".join(f"{f.replace('Abschnitt_','').replace('.md','')}×{c}" for f,c in tops if c>=2)
    print(f"{label:<32}{n:>5}{per10k:>8}  {topstr}")

print("\n=== SATZANFANG-MONOTONIE (Top 15) ===")
print("Wie oft beginnt ein Satz mit demselben Wort? (Ich/Er/Sie/Namen = Subjekt-Monotonie)")
for w, c in sent_starts.most_common(15):
    pct = round(c/total_sents*100, 1)
    print(f"  {w:<14}{c:>5}  ({pct}%)")
