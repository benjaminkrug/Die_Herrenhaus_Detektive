#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_graph.py — Prueft die CYOA-Verzweigungslogik von Band 1 automatisch.

Liest graph.yaml (via build_graph_yaml.py generiert) und prueft:
  1. Kaputte Referenzen  — zeigt jede Wahl/jeder Weiter-Link auf einen
     existierenden Abschnitt?
  2. Verwaiste Abschnitte — wird jeder Abschnitt von irgendwo erreicht?
     (ausser Start '1' und dem Geheim-Ende via Codewort)
  3. Pfade ohne Ende      — endet jeder begehbare Pfad an einem Ende?
  4. Dangling             — gibt es Abschnitte ohne jeglichen Ausgang,
     die kein Ende sind?
  5. Dateien              — existiert jede referenzierte .md-Datei?
  6. Enden-Erreichbarkeit — ist jedes Ende ueber mind. einen Pfad erreichbar?

Anders als das Schattenjaeger-Skript: Herrenhaus ERLAUBT Konvergenz (mehrere
Pfade fuehren zusammen), daher keine Time-Cave-Konvergenz-Warnung.

Nutzung:
  python validate_graph.py            # baut graph.yaml neu, dann Pruefung
  python validate_graph.py --no-build # nur pruefen (vorhandene graph.yaml)

Exit-Code 0 = keine Fehler, 1 = Fehler gefunden.
"""

import sys
import io
import subprocess
from pathlib import Path

# Windows-Konsole auf UTF-8 (Pfeile, Umlaute)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

try:
    import yaml
except ImportError:
    print("FEHLER: pyyaml fehlt. Installieren: pip install pyyaml")
    sys.exit(1)

BASE = Path(__file__).parent
GRAPH = BASE / "graph.yaml"
ABSCHNITTE = BASE / "Abschnitte"
START = "1"


def targets_of(node: dict) -> list:
    out = []
    for c in node.get("choices", []):
        out.append(c["target"])
    if node.get("next"):
        out.append(node["next"])
    return out


def find_paths(sections: dict):
    """Alle Pfade vom Start bis zu Ende/Sackgasse (Zyklen werden gebrochen)."""
    endings = {sid for sid, s in sections.items() if s.get("type") == "ending"}
    paths = []
    stack = [(START, [START])]
    max_steps = 200
    while stack:
        cur, path = stack.pop()
        node = sections.get(cur)
        if node is None:
            paths.append(path)          # kaputter Link -> Pfad bricht ab
            continue
        if cur in endings:
            paths.append(path)
            continue
        tgts = targets_of(node)
        if not tgts:
            paths.append(path)          # dangling
            continue
        for t in tgts:
            if t in path:               # Zyklus (z.B. Dead-End-Loop) -> nicht weiter
                continue
            if len(path) >= max_steps:
                continue
            stack.append((t, path + [t]))
    return paths, endings


def validate():
    data = yaml.safe_load(GRAPH.read_text(encoding="utf-8"))
    sections = data["sections"]
    ids = set(sections.keys())
    errors, warnings = [], []

    endings = {sid for sid, s in sections.items() if s.get("type") == "ending"}
    print("=== Band 1 CYOA — Graph-Validierung ===")
    print(f"Abschnitte: {len(sections)}  |  Enden: {len(endings)}")
    by_cluster = {}
    for s in sections.values():
        by_cluster[s.get("cluster", "?")] = by_cluster.get(s.get("cluster", "?"), 0) + 1
    print("  Nach Cluster: " + ", ".join(f"{k}={v}" for k, v in sorted(by_cluster.items())))
    print()

    # 1. Kaputte Referenzen + Referenz-Sammlung
    referenced = set()
    for sid, node in sections.items():
        for t in targets_of(node):
            referenced.add(t)
            if t not in ids:
                errors.append(f"Abschnitt {sid}: Verweis auf nicht-existierenden Abschnitt {t}")
    broken = sum(1 for e in errors if "nicht-existierenden" in e)
    print(f"--- 1. Kaputte Referenzen: {broken}")

    # 2. Verwaiste Abschnitte
    orphans = []
    for sid in sorted(ids):
        if sid == START:
            continue
        if sid in referenced:
            continue
        node = sections[sid]
        # Geheim-Ende (Codewort) ist gewollt nicht ueber Graph-Kante erreichbar
        if node.get("codewort_system"):
            continue
        orphans.append(sid)
    print(f"--- 2. Verwaiste Abschnitte: {len(orphans)}")
    for sid in orphans:
        warnings.append(f"Abschnitt {sid} ('{sections[sid].get('title','?')[:35]}') "
                        f"wird von keinem anderen Abschnitt referenziert")

    # 3./4. Pfade
    paths, endings = find_paths(sections)
    ending_paths = [p for p in paths if p[-1] in endings]
    bad_paths = [p for p in paths if p[-1] not in endings]
    print(f"--- 3. Vollstaendige Pfade (zu einem Ende): {len(ending_paths)}")
    print(f"--- 4. Pfade ohne Ende / dangling: {len(bad_paths)}")
    seen_bad_tips = set()
    for p in bad_paths:
        tip = p[-1]
        if tip in seen_bad_tips:
            continue
        seen_bad_tips.add(tip)
        node = sections.get(tip)
        if node is None:
            errors.append(f"Pfad endet an nicht-existierendem Abschnitt {tip} "
                          f"(von {p[-2] if len(p) > 1 else '?'})")
        else:
            errors.append(f"Pfad endet ohne Ende bei Abschnitt {tip} "
                          f"('{node.get('title','?')[:35]}', type={node.get('type')})")

    # 5. Dateien
    missing = []
    for sid, node in sections.items():
        f = node.get("file")
        if f and not (ABSCHNITTE / f).exists():
            missing.append(f"{sid}: {f}")
    print(f"--- 5. Fehlende Dateien: {len(missing)}")
    for m in missing:
        errors.append(f"Datei fehlt: {m}")

    # 6. Enden-Erreichbarkeit
    reached = {p[-1] for p in ending_paths}
    unreached = []
    for sid in sorted(endings):
        if sid in reached:
            continue
        if sections[sid].get("codewort_system"):
            warnings.append(f"Geheim-Ende {sid} nur per Codewort erreichbar (gewollt)")
        else:
            unreached.append(sid)
    print(f"--- 6. Nicht erreichbare Enden: {len(unreached)}")
    for sid in unreached:
        errors.append(f"Ende {sid} ('{sections[sid].get('title','?')[:35]}') "
                      f"ist ueber keinen Pfad erreichbar")

    # Enden-Uebersicht
    print("\n--- Enden ---")
    for sid in sorted(endings, key=lambda x: sections[x].get("ending_id", 0)):
        s = sections[sid]
        n = sum(1 for p in ending_paths if p[-1] == sid)
        star = "★" * s.get("stars", 0)
        flag = " [Codewort]" if s.get("codewort_system") else ""
        print(f"  ENDE {s.get('ending_id','?')} {star:5s} '{s.get('title','?')[:34]}' "
              f"— {n} Pfad(e){flag}")

    # Zusammenfassung
    print("\n" + "=" * 50)
    if errors:
        print(f"[FEHLER] {len(errors)}:")
        for e in errors:
            print(f"  - {e}")
    if warnings:
        print(f"[WARNUNG] {len(warnings)}:")
        for w in warnings:
            print(f"  - {w}")
    if not errors and not warnings:
        print("[OK] Alle Pruefungen bestanden — 0 Fehler, 0 Warnungen.")
    elif not errors:
        print(f"[OK] Keine Fehler ({len(warnings)} Warnung(en)).")
    else:
        print(f"[FEHLER] {len(errors)} Fehler, {len(warnings)} Warnung(en).")

    return len(errors) == 0


def main():
    if "--no-build" not in sys.argv:
        r = subprocess.run([sys.executable, str(BASE / "build_graph_yaml.py")],
                           capture_output=True, text=True, encoding="utf-8")
        sys.stdout.write(r.stdout)
        if r.returncode != 0:
            sys.stderr.write(r.stderr)
            sys.exit(1)
        print()
    ok = validate()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
