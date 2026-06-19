# -*- coding: utf-8 -*-
import re, os, glob, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

KAP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Kapitel")
OPEN_Q, CLOSE_Q = chr(0x201E), chr(0x22)  # „ ... " (gerade ASCII-Quote)

def load(p):
    raw = open(p, encoding="utf-8").read().split("\n")
    started = False; body = []
    for ln in raw:
        if ln.startswith("# Kapitel") or ln.startswith("# Epilog"):
            started = True; continue
        if started:
            s = ln.strip()
            if s.startswith("*Ende von Band") or s.startswith("*Die Herrenhaus-Detektive kehren"): continue
            if s == "---" or s.startswith("#"): continue
            body.append(ln)
    return " ".join(body)

def kapnum(p): return int(re.search(r"Kapitel(\d+)", p).group(1))
files = sorted(glob.glob(os.path.join(KAP, "*.md")), key=kapnum)

pat = re.compile(OPEN_Q + r"(.*?)" + CLOSE_Q)
print("Kap | DialogWort% | (Dialog/Total)")
print("-"*40)
out = []
for p in files:
    t = load(p)
    total = len(t.split())
    dlg = pat.findall(t)
    dw = sum(len(d.split()) for d in dlg)
    pct = round(100*dw/total) if total else 0
    out.append((kapnum(p), pct))
    print(f"{kapnum(p):>3} | {pct:>3}%        | ({dw}/{total})")
print("-"*40)
low = [n for n,p in out if p < 40]
print("Unter 40%:", ", ".join(f"K{n}" for n in low) if low else "keine")
avg = round(sum(p for _,p in out)/len(out))
print("Durchschnitt:", f"{avg}%")
