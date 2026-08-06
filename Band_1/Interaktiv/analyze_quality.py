#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ad-hoc-Qualitaetsanalyse fuer Herrenhaus-Detektive Band 1 Interaktiv.
Misst pro Abschnitt: Woerter, Dialog-Anteil, Dialogverben, lange Saetze,
Format (Weiter/EP/Ende). Kein Anspruch auf Perfektion - Entscheidungshilfe."""
import re, glob, os, collections

ABSCHNITTE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Abschnitte")

DIALOG_VERBS = ["flüsterte","sagte","rief","murmelte","zischte","fragte","meinte",
                "hauchte","raunte","antwortete","brummte","stammelte","keuchte",
                "erklärte","wisperte","stöhnte","jammerte","schrie","lachte"]

def count_words(t): return len(re.findall(r"\b\w+\b", t))

def dialog_ratio(t):
    # Woerter innerhalb deutscher Anfuehrungszeichen „..."
    inside = re.findall('„([^"“]*)["“]', t)
    dw = sum(count_words(x) for x in inside)
    tw = count_words(t)
    return (dw/tw*100) if tw else 0

def long_sentences(t):
    # grobe Satztrennung
    sents = re.split(r"[.!?…]+", t)
    longs = [s.strip() for s in sents if count_words(s) > 15]
    return len(longs)

rows = []
verb_total = collections.Counter()
for path in sorted(glob.glob(os.path.join(ABSCHNITTE, "*.md"))):
    name = os.path.basename(path)
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    # Navigation/Trenner fuer Wortzahl grob rausnehmen
    body = re.sub(r"^#.*$", "", raw, flags=re.M)
    body = re.sub(r"^\*→.*$", "", body, flags=re.M)
    body = re.sub(r"^---.*$", "", body, flags=re.M)
    w = count_words(body)
    dr = dialog_ratio(body)
    ls = long_sentences(body)
    verbs = collections.Counter()
    for v in DIALOG_VERBS:
        c = len(re.findall(r"\b"+v+r"\b", raw, flags=re.I))
        if c: verbs[v]+=c; verb_total[v]+=c
    fl = verbs.get("flüsterte",0)
    has_ep = "**" in raw and ("Abschnitt" in raw)
    rows.append((name, w, round(dr), ls, fl, sum(verbs.values())))

print("=== PRO ABSCHNITT ===")
print(f"{'Datei':<32}{'Wört':>5}{'Dlg%':>6}{'>15W':>6}{'flü':>5}{'Verb':>6}")
for r in sorted(rows, key=lambda x:x[1]):
    print(f"{r[0]:<32}{r[1]:>5}{r[2]:>6}{r[3]:>6}{r[4]:>5}{r[5]:>6}")

print("\n=== AGGREGAT ===")
ws = [r[1] for r in rows]
drs = [r[2] for r in rows]
print(f"Abschnitte: {len(rows)}")
print(f"Ø Wörter: {sum(ws)//len(ws)}  Min: {min(ws)}  Max: {max(ws)}")
print(f"Ø Dialog%: {sum(drs)//len(drs)}")
print(f"Abschnitte mit Dialog < 30%: {sum(1 for d in drs if d<30)}")
print(f"Abschnitte mit >2 langen Sätzen: {sum(1 for r in rows if r[3]>2)}")
print(f"Abschnitte mit flüsterte >=2: {sum(1 for r in rows if r[4]>=2)}")
print("\n=== DIALOGVERBEN GESAMT ===")
for v,c in verb_total.most_common():
    print(f"  {v:<14}{c}")
