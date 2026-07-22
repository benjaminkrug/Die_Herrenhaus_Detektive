# Menschlichkeits-Checkliste -- Band 4

> **Kein Skript.** Die Merkmale, die Text kuenstlich wirken lassen, sind nicht
> zaehlbar. Diese Liste wird **nach jedem Akt** durchgegangen (Kap 1-5, 6-10,
> 11-15, 16-19), zusammen mit `qa_messung.py` und `schablonen_analyse.py`.
>
> **Grundregel (`PLAN_Band4.md` 6.0):** Kandidaten, keine Urteile.
> **"Geprueft, bleibt so" ist ein vollwertiges Ergebnis** und wird notiert.

------------------------------------------------------------------------

## Die sechs Fragen

### 1. Loest sich jede Szene sauber auf?
Wenn am Ende jeder Szene alles ordentlich liegt, klingt es konstruiert.
**Echte Szenen lassen Reste zurueck** -- eine Frage, die keiner beantwortet,
ein Streit, der nicht ausgeht, jemand, der beleidigt bleibt.

### 2. Sprechen alle im selben Rhythmus?
Gleiche Satzlaenge, gleiche Bauweise, nur andere Woerter = **eine Stimme mit
vier Namen.**
**Groesstes Risiko in Band 4: Mila und Nele.** Beide sind direkt, beide geben
nicht nach. Unterscheidung laut Kanon: **Mila ist laut und stuermt vor, Nele ist
leise und war schon da.** Wenn man ihre Zeilen tauschen koennte, ohne dass es
auffaellt, ist etwas falsch.

### 3. Kommen Emotionen immer in derselben Reihenfolge?
Ereignis -> Koerperreaktion -> Dialog, Kapitel fuer Kapitel, ist ein Muster,
das auffaellt. **Reihenfolge variieren, manchmal einen Teil weglassen.**
Manchmal reagiert jemand gar nicht -- das ist auch eine Reaktion.

### 4. Hat jedes Kapitel dieselbe Form?
Gleiche Szenenzahl, gleicher Aufbau, gleiche Laenge = **Formular.**
Dafuer ist das breite Fenster (900-1.500) da, und dafuer variiert die
Szenenzahl in der Planung zwischen 2 und 4.
*Wachpunkt: Akt 3 hat fuenfmal 3 Szenen -- die einzige Formular-Auffaelligkeit
der Planung. Beim Schreiben pruefen, ob ein Kapitel auf 2 oder 4 will.*

### 5. Missversteht jemals jemand jemanden?
**Der staerkste Einzelindikator.**
Echte Kinder reden aneinander vorbei, unterbrechen, antworten auf etwas
anderes, sagen Belangloses. **KI-Dialog ist immer effizient:** jede Zeile
transportiert Information, jede Antwort passt zur Frage.
**Mindestens eine Stelle pro Kapitel, an der das NICHT so ist.**

### 6. Reagiert jemand, der gerade nicht dran ist?
In KI-Text handelt immer nur, wer gerade spricht.
**Ben, der die Muetze tiefer zieht, waehrend Mila redet**, ist der billigste
und wirksamste Gegenmittel-Satz. Er ist zugleich eine der erlaubten
Verlaengerungen (`PLAN_Band4.md` Abschnitt 4).

------------------------------------------------------------------------

## Referenzwerte aus Band 3 (gemessen, nicht geschaetzt)

> Band 3 ist fertig, geprueft und vom Autor abgenommen. **Das ist der
> Qualitaetsmassstab der Reihe** -- nicht ein theoretischer Zielwert.
> Ermittelt mit denselben zwei Skripten am 2026-07-21.

### Umfang und Struktur

| Groesse | Band 3 (fertig) | Band 4 (geplant) |
|---------|:---------------:|:----------------:|
| Woerter gesamt | **21.071** | ~24.100 |
| Kapitel | 19 | 19 |
| Schnitt pro Kapitel | **1.109** | ~1.270 |
| Kuerzestes / laengstes | 1.004 / 1.265 | 950 / 1.550 |

> **BEFUND:** Band 4 ist rund **3.000 Woerter (14 %) laenger** geplant als sein
> Vorgaenger, und die Spanne ist deutlich breiter. Die Breite ist Absicht
> (Formular vermeiden). **Der Zuwachs ist es nicht** -- beim Schreiben zuerst
> bei Kap 3 (1.550), Kap 13 (1.500) und Kap 14 (Richtung 1.000) straffen.

### Sprache

| Groesse | Band 3 | Bemerkung |
|---------|:------:|-----------|
| Dialoganteil (Wort-Methode) | **29 %** (16-50) | CLAUDE.md fordert 40 % -- **das fertige Band 3 erreicht das nicht.** Deshalb flaggt `qa_messung.py` erst unter 20 %, sonst nur Rauschen |
| Saetze ueber 15 Woerter | 0-5 je Kapitel | die meisten Kapitel: 0 |
| Laengster Satz | 12-23 Woerter | |
| Abstrakte Emotionen | 8 im ganzen Buch | sehr sauber |

### Varianz (der eigentliche KI-Indikator)

| Groesse | Band 3 | Lesart |
|---------|:------:|--------|
| Satzlaengen-Streuung | **2.5** (min 2.0) | darunter = monoton |
| Absatz-Streuung | **7.6** (min 5.8) | |
| Dialogverben je Kapitel | **5.9** (min 3) | wenige = eintoenig |
| Haeufigster Satzanfang | "er" mit **6,8 %** | darueber = Subjekt-Monotonie |

### Schablonen-Praxis (pro 10.000 Woerter)

| Schablone | Band 3 |
|-----------|:------:|
| "fluesterte" | 12,8 |
| "Und dann" | 8,1 |
| "Herz klopfte/pochte" | 5,7 |
| "Fuer einen Moment" | 4,3 |
| "Dann, ploetzlich" | 4,3 |

> **So liest man diese Tabelle:** Nicht "Band 4 muss darunter bleiben".
> Sondern: **Deutliche Ausreisser nach oben sind Kandidaten.** Band 3 ist
> erschienen und gut -- diese Werte sind erlaubt.

------------------------------------------------------------------------

## Ablauf pro Akt

1. `python qa_messung.py` -- Regeln, Laengen, Kapitelschluesse selbst lesen
2. `python schablonen_analyse.py` -- Floskeln und Varianz
3. Diese sechs Fragen durchgehen
4. **Ergebnisse notieren, auch die Nicht-Aenderungen.**
   *"Geprueft, bleibt so -- Begruendung X"* ist ein Ergebnis und verhindert,
   dass dieselbe Stelle dreimal diskutiert wird.

------------------------------------------------------------------------

## Warum es diese Liste ueberhaupt gibt

Aus der Band-1-Interaktiv-Ueberarbeitung: Dort war das Ziel "fluesterte unter
40". Es wurde **bewusst nicht erreicht** (Endstand 76), weil die verbleibenden
Vorkommen im Kontext richtig sassen. Mechanisch weiterzudruecken haette
bedeutet, ein praezises Verb gegen eine bedeutungsgleiche Umschreibung zu
tauschen -- **das Buch waere schlechter geworden.** In 3 von 5 Pruefteilen war
"kein Eingriff" die richtige Entscheidung.

**Die Zahlen sagen, wo man hinsehen soll. Diese Liste sagt, worauf.**
Entschieden wird beim Lesen.
