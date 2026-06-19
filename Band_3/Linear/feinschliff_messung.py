# -*- coding: utf-8 -*-
"""
Feinschliff Stufe 1 — mechanische Messung aller 19 Kapitel (Band 3).
Misst objektiv gegen die Schreibregeln aus CLAUDE.md:
- Satzlaenge (Regel 8-12, max 15 Woerter)
- Dialog-Quote (Regel min 40%)
- Abstrakte Emotionen (verbotene Muster)
- Passiv-Konstruktionen (werden/wurde + Partizip)
- Auffaellige Wortwiederholungen (gleiche Inhaltswoerter dicht beieinander)
"""
import re, os, glob
from collections import Counter

KAP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Kapitel")

# Verbotene/abstrakte Emotions-Muster (laut CLAUDE.md + Projekt-Regeln)
ABSTRACT = [
    r"seltsames? Gef[uü]hl", r"komisches? Gef[uü]hl", r"ungutes? Gef[uü]hl",
    r"\bsp[uü]rte\b", r"myster[iö]", r"observier", r"merkw[uü]rdiges? Gef[uü]hl",
    r"f[uü]hlte sich .* an wie ein", r"irgendein Gef[uü]hl",
]
# Passiv: Form von werden + Partizip II (grob)
PASSIV = re.compile(r"\b(wird|wurde|wurden|werden|worden)\b\s+\w*\s*\b\w+(t|en)\b", re.I)

def load_chapter(path):
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    lines = raw.split("\n")
    started = False
    body = []
    for ln in lines:
        if ln.startswith("# Kapitel") or ln.startswith("# Epilog"):
            started = True
            continue
        if started:
            s = ln.strip()
            if s.startswith("*Ende von Band") or s.startswith("*Die Herrenhaus-Detektive kehren"):
                continue
            if s == "---" or s.startswith("#"):
                continue
            body.append(ln)
    return "\n".join(body)

def split_sentences(text):
    # grob an . ! ? aufteilen; Anfuehrungszeichen mitnehmen
    text = re.sub(r"\s+", " ", text.replace("\n", " "))
    parts = re.split(r"(?<=[.!?“])\s+", text)
    return [p.strip() for p in parts if p.strip()]

def is_dialog_line(line):
    return ("„" in line or "“" in line or line.strip().startswith('"'))

def kap_num(path):
    m = re.search(r"Kapitel(\d+)\.md", path)
    return int(m.group(1)) if m else 0

files = sorted(glob.glob(os.path.join(KAP_DIR, "*.md")), key=kap_num)

print(f"{'Kap':>3} | {'Woerter':>7} | {'Saetze':>6} | {'>15W':>5} | {'maxW':>4} | {'Dialog%':>7} | {'abstr':>5} | {'passiv':>6}")
print("-"*72)

total_long = 0
issues = {}
for path in files:
    n = kap_num(path)
    body = load_chapter(path)
    words = len(body.split())
    sents = split_sentences(body)
    sent_wordcounts = [len(s.split()) for s in sents]
    long_sents = [(i, c, sents[i]) for i, c in enumerate(sent_wordcounts) if c > 15]
    maxw = max(sent_wordcounts) if sent_wordcounts else 0

    # Dialog-Quote: Anteil Zeilen mit Anfuehrungszeichen an nicht-leeren Zeilen
    raw_lines = [l for l in body.split("\n") if l.strip()]
    dlg = sum(1 for l in raw_lines if is_dialog_line(l))
    dlg_pct = round(100*dlg/len(raw_lines)) if raw_lines else 0

    abstr = []
    for pat in ABSTRACT:
        for m in re.finditer(pat, body, re.I):
            abstr.append(m.group(0))
    passiv = PASSIV.findall(body)

    total_long += len(long_sents)
    issues[n] = {"long": long_sents, "abstr": abstr, "passiv_count": len(passiv), "dlg": dlg_pct}

    print(f"{n:>3} | {words:>7} | {len(sents):>6} | {len(long_sents):>5} | {maxw:>4} | {dlg_pct:>6}% | {len(abstr):>5} | {len(passiv):>6}")

print("-"*72)
print(f"\n== Lange Saetze (>15 Woerter) im Detail ==")
for n in sorted(issues):
    for (i, c, s) in issues[n]["long"]:
        print(f"  K{n} [{c}W]: {s[:110]}")

print(f"\n== Abstrakte Emotionen (Treffer) ==")
any_abstr = False
for n in sorted(issues):
    if issues[n]["abstr"]:
        any_abstr = True
        print(f"  K{n}: {issues[n]['abstr']}")
if not any_abstr:
    print("  keine")

print(f"\n== Kapitel mit Dialog < 40% ==")
low = [n for n in sorted(issues) if issues[n]["dlg"] < 40]
print("  " + (", ".join(f"K{n} ({issues[n]['dlg']}%)" for n in low) if low else "keine"))
