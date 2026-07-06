# Qualitäts-Analyse — Die Herrenhaus-Detektive Band 1 Interaktiv

**Datum:** 2026-07-05
**Erzeugt von:** `validate_graph.py`, `analyze_quality.py`, `schablonen_analyse.py`
**Zweck:** Referenz für die Überarbeitung ([Ueberarbeitungsplan_Band1_Interaktiv.md](Ueberarbeitungsplan_Band1_Interaktiv.md)).
Maschinelle Messung — Metriken sind Frühwarnung, kein Urteil. Manuell gegenprüfen.

---

## 1. Struktur-Validierung (Phase 1.2) — BESTANDEN

```
validate_graph.py: 0 Fehler, 0 Warnungen
```

| Prüfung | Ergebnis |
|---------|----------|
| Abschnitte (Dateien) | 94 Story + 2 Meta (Einleitung, Cluster_Konsistenz) |
| Enden | **14** (106–119), alle erreichbar |
| Kaputte Referenzen | 0 |
| Verwaiste Abschnitte | 0 |
| Vollständige Pfade zu einem Ende | 217 |
| Pfade ohne Ende / dangling | **0** |
| Fehlende Dateien | 0 |
| Nicht erreichbare Enden | **0** |

**→ Kein einziges totes Ende. Das größte unbekannte Risiko ist ausgeschlossen.**

### Cluster-Verteilung
| Cluster | Abschnitte |
|---------|-----------|
| START (1–7) | 7 |
| A — Das Geisterhaus (11–32) | 29 |
| B — Das Wasser (41–59) | 21 |
| C — Die Dorf-Detektive (66–86) | 21 |
| D — Krügers Brief (91–105) | 16 |

### Enden-Übersicht (mit Pfad-Häufigkeit)
| Ende | ★ | Titel | Pfade |
|------|---|-------|-------|
| 108 | ★★★★ | Das Rätsel-Museum | 48 |
| 106 | ★★★ | Gut, aber... | 48 |
| 107 | ★★★ | Mit Hilfe | 48 |
| 119 | ★★ | Hausarrest | 12 |
| 111 | ★★★★ | Der Brunnen fließt | 8 |
| 110 | ★★★ | Die Truhe | 12 |
| 109 | ★★ | Pitschnass | 4 |
| 114 | ★★★★ | Heinrich-Winter-Weg | 6 |
| 113 | ★★★ | Beweise, aber... | 10 |
| 112 | ★★ | Die Flucht | 2 |
| 115 | ★ | Am Bach gespielt | 2 |
| 116 | ★★★★ | Krügers Tränen | 8 |
| 117 | ★★★ | Der offizielle Weg | 8 |
| 118 | ★★ | Zu spät | 1 |

*Beobachtung:* Cluster A dominiert (48 Pfade je Ende) — es ist der "Haupt"-Weg.
Die ★-Verteilung ist gesund (4× ★★★★, breites Spektrum bis ★).

### Format-Inkonsistenz — BEHOBEN (Phase 3.5)
6 Dateien nutzten `→ **Weiter bei Abschnitt X**` (Pfeil+fett) statt des
Standards `*→ Weiter bei Abschnitt X*` (kursiv, 25 Dateien):
14b, 15b, 18b, 21b, 24b, 26c. **Alle 6 auf Kursiv-Standard vereinheitlicht**
(26c behält „Zurück zu" als korrekte Rücksprung-Semantik). Validator 0 Fehler.

> **Phase-6.3-Entscheidung: Kompiler NICHT anfassen.** Die Navigations-Box
> (`create_manuscript_interaktiv.py` Z. 920, fett + grauer Hintergrund + ▶)
> matcht nur `→ Weiter bei`; die kursiven `*→ Weiter bei…*`-Zeilen rendern als
> schlichte kursive Zeile. **Verifiziert per `git show HEAD`:** Das kursive
> Format war bereits im letzten Commit so (Abschnitt_01 = `*→ Weiter bei
> Abschnitt 2*`) — also der etablierte, veröffentlichte Zustand, NICHT durch die
> Überarbeitung verursacht. Regex zu ändern wäre ein neues Feature (kosmetisch),
> keine Fehlerkorrektur → außerhalb Scope, Regressionsrisiko ohne echten Nutzen.
> Rendering in 6.4 gegengeprüft.

---

## 2. Prosa-Grundmetriken (Phase 1.3)

| Metrik | Wert | Bewertung |
|--------|------|-----------|
| Wörter gesamt (Story) | ~28.800 | ⚠️ dünner als B2 (~43k) |
| Ø Wörter/Abschnitt | 314 | ✅ im Zielband 280–350 |
| Min / Max | 139 / 720 | Meta-Seite / Abschnitt_03 |
| Lange Sätze (>15 W) | **≈0** | ✅ Sprache sehr sauber |
| Dialog-Anteil (Messwert) | Ø 22 %, 72/96 < 30 % | ⚠️ *Metrik unterschätzt* — manuell prüfen |

**Warnung zum Dialog-Wert:** Zählt nur Wörter *innerhalb* der Anführungszeichen.
Sprecher-Tags und Reaktionen zählen nicht mit. Nicht als hartes Ziel nehmen.

---

## 3. Schablonen / "KI-Klang" (Phase 2 — der Kern)

Gemessen mit `schablonen_analyse.py` über 94 Story-Abschnitte (28.794 Wörter).

### 3.1 Dialog-Tics
| Verb | Anzahl | Ziel |
|------|:------:|:----:|
| sagte | 422 | Default, ok (nur Nester lösen) |
| **flüsterte** | **83** | **< 40** |
| fragte | 81 | ok |
| murmelte | 15 | ok |

**flüsterte-Häufungen (≥2× pro Datei), 19 Abschnitte:**
03(4), 17(3), 18(3), 20(3), 25(3), 26(3), 94(3), 07(2), 14(2), 21(2), 23(2),
24(2), 46(2), 59(2), 69(2), 72(2), 96(2), 99b(2), 103(2).
*(03, 46, 103 sind lang → pro Szene prüfen, nicht pauschal auf 1.)*

### 3.2 Körperreaktions-Klischees
| Schablone | Anzahl | Ziel |
|-----------|:------:|:----:|
| Herz klopfte/pochte | 17 | ~5–6 |
| verschränkte die Arme | 16 | ~5–6 (Milas Geste, gezielt aufsparen) |
| schluckte | 14 | ~5–6 |

> **False-Positive-Test (Phase 2.0, 2026-07-05):**
> - `Herz klopfte/schlug`: 17 Treffer, **0 Fehltreffer** — alle echte Anspannung.
>   Auffällig: „Herz schlug schneller" allein ~6× (Wort-für-Wort-Wiederholung).
> - `schluckte`: 1 Fehltreffer entfernt („den letzten Bissen Waffel", Absch. 67).
>   Korrekt jetzt **14**. Regex im Skript um Ausschluss ergänzt.
> - `Satzanfang „Er"`: von 396 Treffern stehen ~37 (9 %) in Dialogzeilen →
>   Wert leicht überhöht, aber 359 im Erzähltext bleiben ein echtes Thema.
> **Fazit:** Skript-Zahlen sind belastbar. Muster-Präzision hoch.
| Atem stockte / hielt den Atem | 11 | ~5 |
| Kribbeln / kribbelte | 10 | ~4 |
| Magen/Bauch zog sich | 3 | ok |

### 3.3 Füll-Übergänge
| Schablone | Anzahl | Aktion |
|-----------|:------:|--------|
| "Und dann" (Satzanfang) | 17 | meist streichbar |
| "Stille." (Einwort) | 5 | 2–3 behalten |
| plötzlich | ~5 | fast immer streichbar |
| "Für einen Moment" | 3 | prüfen |

### 3.4 Satzanfang-Monotonie
Sätze beginnen mit: Er 5,3 % · Jonas 4,6 % · Ben 2,5 % · Sie 2,1 % · Mila 1,9 %.
Fast jeder 6. Satz startet mit Figuren-Subjekt → "Subjekt-Verb"-Stakkato.
*(Wert nach oben verzerrt — zählt auch Dialog-Sätze. Nur Tendenz nehmen.)*

> **Phase-2.4-Entscheidung (2026-07-05): KEIN Eingriff — bewusst.** Prüfung ergab
> **0** Dreier-Ketten gleicher Satzanfänge im ganzen Buch und nur **29 Zweier-Paare
> von 4891 Erzählzeilen (0,6 %)**. Die auffälligsten "Er…Er"-Paare sind bewusste
> **Anaphern** (z. B. 104 "Er sah nicht auf den Boden. / Er sah in den Himmel.";
> 14 "Er wollte keine Gerüchte. / Er wollte Fakten.") — rhetorische Figuren, die
> man NICHT anfasst. Die "359× Er"-Zahl ist die gesunde Grundstruktur eines
> Leseanfänger-Buchs, keine Häufung. Umbau würde Lesbarkeit für 8-Jährige senken.
> → Metrik-Kosmetik ohne Leserwert, daher ausgelassen.

---

## 4. Was gut ist (nicht anfassen)

- **Struktur:** makellos — 0 Validierungsfehler, alle Enden erreichbar.
- **Sprache:** kurze Sätze, kein Passiv-Problem, quasi keine Überlängen.
- **Orthografie:** Umlaute + Quotes bereits einheitlich (spart die B2-Fix-Phase).
- **Enden-Design:** 14 Enden, gesunde ★-Verteilung, gute Wiederspielbarkeit.

## 5. Was zu tun ist (Priorität)

1. **Phase 2 — Entschablonisierung:** flüsterte 83→<40, Körperreaktions-Klischees
   halbieren, Füll-Übergänge streichen, Satzanfänge variieren.
2. **Phase 3 — Feinschliff:** kurze Abschnitte + Enden-Sensorik + Format der 6
   Weiter-bei-Ausreißer.
3. **Phase 4 — Kontinuität:** 96 Abschnitte gegen `Cluster_Konsistenz.md`.

*Details: [Ueberarbeitungsplan_Band1_Interaktiv.md](Ueberarbeitungsplan_Band1_Interaktiv.md).*
