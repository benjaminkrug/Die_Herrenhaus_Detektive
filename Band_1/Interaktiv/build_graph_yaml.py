#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_graph_yaml.py — Generiert graph.yaml aus den Abschnitt-*.md-Dateien.

Die graph.yaml ist die maschinenlesbare Single Source of Truth der
Verzweigungslogik (nach Vorbild der Schattenjaeger-CYOA). Sie wird NICHT
von Hand gepflegt, sondern aus den Story-Dateien generiert — so koennen
Text und Graph nicht auseinanderlaufen.

Erkannte Zeilen-Formate am Ende einer Abschnitt-Datei:
  - Linear:      *-> Weiter bei Abschnitt X*            -> next: X
  - Entscheidung: **Text -> Abschnitt X**               -> choices[].target
  - Bonus:       **Bonus: ... -> Abschnitt X**          -> choices[].target (bonus)
  - Replay:      *-> Von vorne: Abschnitt 1*            -> IGNORIERT
                 *-> Direkt zur Entscheidung: Abschnitt 7*  -> IGNORIERT
  - Ende:        **ENDE NNN - "Titel"**                 -> type: ending

Nutzung:
  python build_graph_yaml.py            # schreibt graph.yaml
  python build_graph_yaml.py --print    # nur auf stdout, nicht schreiben
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FEHLER: pyyaml fehlt. Installieren: pip install pyyaml")
    sys.exit(1)

BASE = Path(__file__).parent
ABSCHNITTE = BASE / "Abschnitte"

# --- Cluster-Zuordnung nach Abschnitt-Nummernbereich (aus Abschnitt_Map.md) ---
# Band 1: Enden (106-119) sind KEINE eigenen Dateien, sondern **ENDE**-Marker
# innerhalb der regulaeren Abschnitte (z.B. Ende 118 liegt in Abschnitt 105).
# Hoechste Datei-Nummer ist daher 105. Kein Abschnitt >=200 (bewusst kein
# Geheim-Ende/Codewort-System, anders als Band 2).
def cluster_of(sid: str) -> str:
    """Ordnet eine Abschnitt-ID ihrem Story-Cluster zu."""
    num = int(re.match(r"\d+", sid).group())
    if sid == "00" or num <= 7:
        return "START"
    if 11 <= num <= 32:
        return "A"          # Das Geisterhaus
    if 41 <= num <= 59:
        return "B"          # Das Wasser-Abenteuer
    if 66 <= num <= 86:
        return "C"          # Die Dorf-Detektive
    if 91 <= num <= 105:
        return "D"          # Kruegers Brief
    return "?"

# --- Zeilen-Muster ---
# Replay-Shortcuts: keine Story-Kante, sondern "nochmal spielen"-Links.
RE_REPLAY = re.compile(
    r"(Von vorne|Von Anfang|Direkt zur Entscheidung)\s*:?\s*Abschnitt\s+(\d+[a-e]?)",
    re.IGNORECASE)
# Linearer Weiter-Link (kursiv, mit Pfeil): *-> Weiter bei Abschnitt X*
RE_LINEAR = re.compile(
    r"^\*.*?(?:Weiter bei|Weiter mit)\s+Abschnitt\s+(\d+[a-e]?)", re.IGNORECASE)
# Format-agnostischer Weiter-/Zurueck-Link. Band 1 nutzt ZWEI Schreibweisen:
#   Variante A (25 Dateien):  *→ Weiter bei Abschnitt X*        (kursiv, Stern vorne)
#   Variante B (6 Dateien):   → **Weiter bei Abschnitt X**      (Pfeil vorne, fett)
#                             → **Zurück zu Abschnitt X**
# Diese Regex erkennt beide, egal mit welchem Zeichen die Zeile beginnt. Sie
# matcht bewusst nur echte lineare Navigation ("Weiter bei/mit", "Zurück zu"),
# nicht Entscheidungsoptionen.
RE_WEITER = re.compile(
    r"(?:Weiter bei|Weiter mit|Zurück zu|Zurueck zu)\s+Abschnitt\s+(\d+[a-e]?)",
    re.IGNORECASE)
# Fett gedruckte Entscheidungs-/Bonus-Option: **... Abschnitt X**
RE_CHOICE = re.compile(r"^\*\*(.+?)\*\*\s*$")
RE_CHOICE_TARGET = re.compile(r"Abschnitt\s+(\d+[a-e]?)\s*$")
# Zusaetzliche Weiter-Links ohne "Weiter bei" (z.B. "Zurueck versuchen: Abschnitt 26b")
RE_KURSIV_TARGET = re.compile(
    r"^\*.*?Abschnitt\s+(\d+[a-e]?)\s*\*?\s*$")
# Ende-Marker
RE_ENDE = re.compile(r"\*\*ENDE\s+(\d+)\s*[—–-]\s*(.+?)\*\*")
RE_STARS = re.compile(r"^(★+)\s*$", re.MULTILINE)


def normalize_sid(sid: str) -> str:
    """Fuehrende Nullen bei numerischem Teil entfernen: '01' -> '1', '07' -> '7'.

    Noetig, weil die Dateien 'Abschnitt_01.md' heissen, der Text aber auf
    'Abschnitt 1' verweist. Ohne Normalisierung meldet der Validator falsche
    kaputte Links. '13b' bleibt '13b'.
    """
    m = re.match(r"(\d+)([a-e]?)$", sid)
    if not m:
        return sid
    return str(int(m.group(1))) + m.group(2)


def sid_from_filename(name: str) -> str:
    """Abschnitt_13b.md -> '13b', Abschnitt_01.md -> '1'."""
    m = re.match(r"Abschnitt_(\d+[a-e]?)", name)
    return normalize_sid(m.group(1)) if m else name


def parse_section(path: Path):
    """Parst eine Abschnitt-Datei zu einem Graph-Knoten-Dict."""
    sid = sid_from_filename(path.name)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Titel = erste Zeile nach dem "# Abschnitt N"-Header, sonst Dateiname
    title = None

    node = {
        "file": path.name,
        "cluster": cluster_of(sid),
        "type": "story",
        "choices": [],
        "next": None,
    }

    # Ende erkennen
    m_ende = RE_ENDE.search(text)
    if m_ende:
        node["type"] = "ending"
        node["ending_id"] = int(m_ende.group(1))
        title = m_ende.group(2).strip().strip('„"" ')
        stars = RE_STARS.search(text)
        if stars:
            node["stars"] = len(stars.group(1))
        # Band 1: kein Codewort-/Geheim-Ende-System (bewusst) -> kein Sonderfall.

    # Zeilen durchgehen: Links sammeln
    replay_targets = set()
    for raw in lines:
        line = raw.strip()
        if not line:
            continue

        # Replay-Shortcuts zuerst herausfiltern (nie Story-Kante)
        if RE_REPLAY.search(line):
            for m in RE_REPLAY.finditer(line):
                replay_targets.add(m.group(2))
            continue

        # Linearer Weiter-/Zurueck-Link (format-agnostisch, beide Band-1-Varianten).
        # VOR dem Choice-Block, damit "→ **Weiter bei Abschnitt X**" nicht faelschlich
        # als Entscheidungsoption zaehlt. Greift nur bei "Weiter bei/mit"/"Zurueck zu",
        # nicht bei echten Entscheidungen ("... → Abschnitt X").
        mw = RE_WEITER.search(line)
        if mw and mw.group(1) not in replay_targets:
            node["next"] = mw.group(1)
            continue

        # Fett gedruckte Entscheidungsoption
        mc = RE_CHOICE.match(line)
        if mc:
            inner = mc.group(1)
            mt = RE_CHOICE_TARGET.search(inner)
            if mt and not inner.upper().startswith("ENDE"):
                node["choices"].append({
                    "text": inner.strip(),
                    "target": mt.group(1),
                })
            continue

        # Kursiver linearer Weiter-Link
        if line.startswith("*"):
            ml = RE_LINEAR.match(line)
            if ml:
                node["next"] = ml.group(1)
                continue
            # generischer kursiver Abschnitt-Link (Zurueck versuchen etc.)
            mk = RE_KURSIV_TARGET.match(line)
            if mk and mk.group(1) not in replay_targets:
                node["next"] = mk.group(1)
                continue

    # Titel-Fallback: erste echte Prosa-Zeile
    if not title:
        for raw in lines:
            s = raw.strip()
            if s and not s.startswith("#") and not s.startswith("*") \
                    and not s.startswith("---"):
                title = (s[:50] + "…") if len(s) > 50 else s
                break
    node["title"] = title or path.name

    # Typ verfeinern
    if node["type"] != "ending":
        if len(node["choices"]) >= 1:
            node["type"] = "choice"
        elif node["next"] is not None:
            node["type"] = "story"
        else:
            node["type"] = "dangling"   # kein Ausgang -> Validator meldet

    # Aufraeumen: leere Felder entfernen
    if not node["choices"]:
        del node["choices"]
    if node["next"] is None:
        del node["next"]
    return sid, node


def build():
    files = sorted(ABSCHNITTE.glob("Abschnitt_*.md"))
    sections = {}
    for f in files:
        # Nur nummerierte Story-Abschnitte. Einleitung/Hinweisseite/Konsistenz
        # sind Meta-Seiten ohne Graph-Kanten -> ueberspringen.
        if not re.match(r"Abschnitt_\d", f.name):
            continue
        if "Einleitung" in f.name:
            continue
        sid, node = parse_section(f)
        sections[sid] = node

    endings = [s for s in sections.values() if s["type"] == "ending"]
    graph = {
        "metadata": {
            "title": "Das verbotene Herrenhaus — Entscheidungsbuch",
            "series": "Die Herrenhaus-Detektive",
            "band": 1,
            "start": "1",
            "total_sections": len(sections),
            "endings": len(endings),
            "generated_by": "build_graph_yaml.py",
        },
        "sections": sections,
    }
    return graph


def main():
    graph = build()
    dump = yaml.safe_dump(graph, allow_unicode=True, sort_keys=True,
                          default_flow_style=False, width=100)
    if "--print" in sys.argv:
        print(dump)
        return
    out = BASE / "graph.yaml"
    out.write_text(dump, encoding="utf-8")
    meta = graph["metadata"]
    print(f"graph.yaml geschrieben: {out}")
    print(f"  Abschnitte: {meta['total_sections']}  |  Enden: {meta['endings']}")


if __name__ == "__main__":
    main()
