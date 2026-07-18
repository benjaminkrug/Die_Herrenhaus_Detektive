# Cross-Error-Report -- "Das Geheimnis des Brunnens" (CYOA)

**Datum:** 2026-02-28 (Audit) / 2026-03-01 (Fixes)
**Pruefer:** Claude (manuell)
**Version:** Git-Branch `claude/analyze-project-xMhy3`
**Abschnitte geprueft:** 120 von 120
**Stand:** Fixes abgeschlossen — 30 von 46 Findings behoben

---

## NACHTRAG 2026-07-02: graph.yaml-Nachruestung + Feinschliff

Diese Runde ruestet eine maschinenlesbare `graph.yaml` (Single Source of
Truth) + `validate_graph.py` nach (Vorbild Schattenjaeger-CYOA). Der
Validator fand automatisch Fehler, die die 3 manuellen Runden uebersehen
hatten.

**Neu gefunden & behoben:**

- **STRUKTUR-F001 (kritisch):** Abschnitt 50b hatte die EP-B4-Entscheidung
  im falschen Format (kursiv `*→ ...*` statt fett `**... → Abschnitt X**`).
  Folge: Abschnitt 51 verwaist → 52/53/54 + **ENDE 211 „Der Brunnen fließt"
  (★★★★)** und **ENDE 209 „Der Brief aus der Tiefe" (★★)** waren fuer Leser
  UNERREICHBAR. Fix: 50b auf Standard-Entscheidungsformat umgestellt.
- **NAV-F002 (Update):** Abschnitt 48b war NICHT mehr verwaist (45 verlinkte
  darauf), aber inhaltlich doppelt redundant (dupliziert 45 + die 59→Meier-
  Kette). Entscheidung: Option in 45 entfernt, 48b geloescht. Kein
  Inhaltsverlust.
- **FAK-H001 (behoben):** Umlaut-Chaos (105/128 Dateien mischten ae/oe/ue/ss
  mit echten Umlauten). Skriptgestuetzt vereinheitlicht auf echte Umlaute +
  ß, verlustfrei (0 False Positives). Inkl. Versalien (MUESSEN→MÜSSEN) und
  4 Tippfehlern (flüsserte→flüsterte u.a.). Skript: `fix_umlaute.py`.
- **END (behoben):** Enden-Trenner `--`→`—` bei ENDE 212 + 214.
- **QUOTE (behoben):** 166 oeffnende gerade Quotes `"`→`„` in 37 Dateien →
  durchgaengiges Buch-Schema `„Text"`. Skript: `fix_quotes.py`.

**Geprueft, bewusst KEIN Eingriff** (nicht ueber-optimieren):
- Dialog-Anteil 46/69/80: 69=50%, 46/80=36% mit dramaturgisch bewusster
  Stille (Wasserfall-Ehrfurcht / Bergmann-Wiederkehr). Report war veraltet.
- KON 2→3 Ortssprung, KON Rucksack: uebliches Kinderbuch-Tempo, kein Loch.
- Sensorik: 4 auffaelligste Abschnitte (1/58/92/98) gelesen — alle stark;
  Metrik hatte unterschaetzt. Bottleneck-Check: alle 3 Kern-Beats in allen
  4 Clustern praesent.

**Endstand:** `validate_graph.py` = 0 Fehler (1 gewollte Warnung: Geheim-Ende
per Codewort). Manuskript neu kompiliert (127 Abschnitte, ~43.000 Woerter),
Scrambling-Verweise konsistent.

### Korrekturlese-Runde (alle 4 Cluster + Start gelesen)

Manuelles Durchlesen je eines ★★★★-Pfads pro Cluster + gemeinsamer Start.
Gefundene Fehlerklassen (Skripte konnten sie nicht sehen), alle behoben:

- **Dash-Quote (34× in 28 Dateien):** `—„` → `—“`. Abgebrochene Rede wurde
  faelschlich mit oeffnendem statt schliessendem Quote beendet
  (Nebeneffekt des Quote-Fixes; Ursache in `fix_quotes.py` korrigiert:
  `—` triggert kein oeffnendes Quote mehr).
- **Tippfehler `rausperte` → `räusperte` (6×)** in 57, 57b, 72c, 99, 101b, 106.
- **Restliche ss→ß (33× in 26 Dateien):** Fuss→Fuß, gross→groß, liess→ließ,
  heiss→heiß, schliesslich→schließlich, stiess→stieß u.a. (SS_FIX erweitert).
- **`--` im Fliesstext (4×):** → `—` in 25b, 71, 86.

Kontrolliert, KEIN Fehler (grammatikalisch korrekt): „sie sie" in 69/85
(Subjekt-Objekt). Alle 4 Cluster inhaltlich stimmig, Cliffhanger sitzen,
Charakter-Dynamik konsistent. Finale docx-Kontrolle: 0 Rest-Fehler.

### Stil-Runde: Varianz-Kur gegen „klingt nach KI" (2026-07-02)

Messung ergab ueberstrapazierte Schablonen (begrenzte, durchrotierte Palette
an Verben/Gesten/Koerper-Reaktionen — der staerkste „KI-Klang"-Tell).
Kontextbewusst diversifiziert (kuratierte Exakt-Matches, kein globales
Replace; emotional starke Stellen blieben, Wiederholungen variiert):

- **`flüsterte` 102 → 58** (Dichte jetzt 1 pro ~690 Wörter, organisch). Ersatz
  gemischt: sagte leise, raunte, fragte, las, murmelte, hauchte — je nach
  Kontext. „ins Ohr flüstern"-Konstruktionen aufgeloest.
- **`verschränkte die Arme` (Mila) 30 → 11.** Rest → wechselnde Gesten
  (Kinn heben/recken, Fäuste ballen, Kopf schütteln, Stirn runzeln,
  Schultern zucken, Hände in die Hüften).
- **`Kribbeln` 21 → 11.** Rest → Magen zog sich zusammen, Herz schlug
  schneller, Gänsehaut, Schauer, Unruhe, Wärme.
- **`murmelte` nach der Kur entzerrt (38 → 34, keine Haeufung 2+/Abschnitt).**

Kontrolle: kein Ersatz wurde zur neuen Schablone (alle neuen Gesten 1 pro
5000+ Wörter). `schluckte` (23) bewusst gelassen — figurenuebergreifend
verteilt und variiert, kein Muster. Graph nach ~60 Edits: 0 Fehler.
Neu kompiliert (~43.000 Wörter).

**Stil-Score-Effekt:** von ~7,8 auf geschaetzt ~8,4/10 (der „KI-Klang"-
Hauptschwachpunkt behoben, ohne Neuschreiben).

---

## Zusammenfassung

| Kategorie | FEHLER | WARNUNG | HINWEIS | BEHOBEN |
|-----------|--------|---------|---------|---------|
| 1. Navigation (NAV) | 1 | 0 | 0 | 2 |
| 2. Cluster-Isolation (ISO) | 0 | 0 | 0 | 0 |
| 3. Story-Kontinuitaet (KON) | 0 | 1 | 2 | 12 |
| 4. Brunnen-Kammer (BRK) | 0 | 0 | 0 | 2 |
| 5. Charakter-Verhalten (CHR) | 0 | 2 | 1 | 0 |
| 6. Enden-Format (END) | 0 | 0 | 0 | 7 |
| 7. Fakten-Konsistenz (FAK) | 0 | 0 | 1 | 10 |
| 8. Wissens-Bonus (BON) | 0 | 0 | 1 | 0 |
| 9. Entscheidungspunkte (ENT) | 0 | 0 | 0 | 1 |
| 10. Band-3-Hooks (B3H) | 0 | 0 | 0 | 1 |
| **GESAMT** | **1** | **3** | **5** | **35** |
| | *(Autor-Entscheidung)* | *(Dialog-Anteile, Rucksack)* | *(Stil)* | |

---

## Schweregrade

- **FEHLER**: Leser blockiert, Geschichte widerspricht sich, Kernregel verletzt. MUSS behoben werden.
- **WARNUNG**: Potenzielle Verwirrung, fragwuerdige Konsistenz, Qualitaetsproblem. SOLLTE behoben werden.
- **HINWEIS**: Stilistischer Hinweis, Optimierungsvorschlag. KANN behoben werden.

---

## Teil 1: Audit-Protokoll

| Datum | Abschnitte | Kategorie | Pruefer | Status |
|-------|-----------|-----------|---------|--------|
| 2026-02-28 | 1-7 | Kat.7 Fakten-Baseline | Claude | Abgeschlossen |
| 2026-02-28 | 31-34, 56-58, 59c | Kat.6 Enden (A+B) | Claude | Abgeschlossen |
| 2026-02-28 | 67d, 84-87, 99e, 104-106 | Kat.6 Enden (C+D) | Claude | Abgeschlossen |
| 2026-02-28 | 200, Hinweisseite, Einleitung | Kat.6 Easter Egg | Claude | Abgeschlossen |
| 2026-02-28 | 11-30, 18b | Kat.1-5,8-9 Cluster A | Claude | Abgeschlossen |
| 2026-02-28 | 41-55, 59-59b, 45e, 48b | Kat.1-5,8 Cluster B | Claude | Abgeschlossen |
| 2026-02-28 | 66-83, 70b | Kat.1-5,8 Cluster C | Claude | Abgeschlossen |
| 2026-02-28 | 91-103, 96b | Kat.1-5,8 Cluster D | Claude | Abgeschlossen |
| 2026-02-28 | 25b, 50b, 79b, 101b, 200 | Kat.4 Brunnen-Kammer-Vergleich | Claude | Abgeschlossen |

---

## Teil 2: Findings

---

### 1. Navigation (NAV)

#### FEHLER

##### NAV-F001: Abschnitt 26b verlinkt falsch (→27 statt →26) — BEHOBEN (2026-03-01)
- **Abschnitt:** 26b (Cluster A, Dead-End-Loop)
- **Problem:** Leser ueberspringt Abschnitt 26 (Bens Brunnen-Deduktion).
- **Fix:** Link in 26b von →27 auf →26 geaendert.

##### NAV-F002: Abschnitt 48b ist verwaist — OFFEN (Autor-Entscheidung)
- **Abschnitt:** 48b (Cluster B, als `[alt]` in Map markiert)
- **Problem:** Kein Abschnitt verlinkt auf 48b. Inhalt: Winters Glasflaschen mit Proben-Etiketten.
- **Empfehlung:** Datei als Reserve-Content behalten. Bei Bedarf von 45b oder 45d verlinken.

#### WARNUNG

##### NAV-W001: Abschnitt 51 — undokumentierter EP — BEHOBEN (2026-03-01)
- **Fix:** EP-B4b in Abschnitt_Map.md eingefuegt: "Bens Idee (→52) / Zur Muehle zurueck (→58)". Cluster-B EP-Zahl auf 7 korrigiert.

---

### 2. Cluster-Isolation (ISO)

**Alle 4 Cluster sind sauber.** Keine verbotenen Wissens-Leaks gefunden.

---

### 3. Story-Kontinuitaet (KON)

#### FEHLER

##### KON-F001: Rucksack-Widerspruch in Abschnitt 200 — BEHOBEN (2026-03-01)
- **Problem:** Karte in Winters Rucksack vs. Jonas' Rucksack.
- **Fix:** Winter gibt Jonas die Karte explizit: "Er zog eine gefaltete Karte aus seinem Rucksack und drueckte sie Jonas in die Hand."

##### KON-F002: Abschnitt 15 — Merge fuer Krueger-Pfad kaputt — BEHOBEN (2026-03-01)
- **Problem:** Krueger-Pfad-Leser hat nur 2 Gegenstaende, Merge bei 15 erwartet 3.
- **Fix:** 13c: Krueger wartet am Tunnel mit Bergmanns Silberkreuz (Meier hat ihn gerufen). 14c: Meier gibt Siegel auf dem Weg zum Herrenhaus. Beide Pfade kommen jetzt mit 3 Gegenstaenden bei 15 an.

##### KON-F003: Abschnitt 17 — Ring-Einsetzszene fehlt — BEHOBEN (2026-03-01)
- **Problem:** Alle Gegenstaende hatten Einsetz-Szenen ausser dem Ring.
- **Fix:** Ring-Einsetzszene am Anfang von Abschnitt 17 eingefuegt: Jonas drueckt Karls Ring in die letzte Vertiefung, vierte Linie leuchtet messingfarben auf, Metalltuer schwingt auf.

##### KON-F004: Abschnitt 48 — Wandmalerei-Referenz fuer Trockentunnel-Leser — BEHOBEN (2026-03-01)
- **Problem:** Trockentunnel-Leser haben Malereien nie gesehen, Text referenziert sie als bekannt.
- **Fix:** Text geaendert: Jonas sieht sich um, entdeckt die Wandmalereien, leuchtet sie ab → Malereien werden direkt in 48 eingefuehrt statt referenziert.

##### KON-F005 + KON-F006: Cluster C — Allein-Pfad komplett kaputt — BEHOBEN (2026-03-01)
- **Problem:** Abschnitte 80-82 setzen Bergmanns Anwesenheit voraus. Auf dem Allein-Pfad ist sie nicht da, und die Kinder haben den Ring nicht.
- **Fix:** Neuer Abschnitt 78b erstellt: Kinder verirren sich (78), erkennen dass sie Hilfe brauchen, gehen zurueck zu Bergmann. Sie klopfen an ihre Tuer, kleinlaut. Bergmann kommt mit, fuehrt sie. Abschnitt 78 Option 1 umgeleitet: "Zurueck zu Frau Bergmann" → 78b → 79. Abschnitte 80-82 bleiben unveraendert (Bergmann ist jetzt immer dabei).

##### KON-F007: Cluster D — Winters Widerspruch (nie reingegangen vs. 1989 drin gewesen) — BEHOBEN (2026-03-01)
- **Problem:** Winter sagt in 95 "nie reingegangen", aber in 101b beschreibt er seinen Besuch 1989.
- **Fix:** Abschnitt 95 umgeschrieben: Winter sagt "einmal reingegangen. Allein. Nachts." und erklaert warum er niemandem davon erzaehlt hat. Gruenderfamilien-Liste ebenfalls korrigiert (Krueger→Hoffmann).

##### KON-F008: Cluster D — 99b→100 ueberspringt Gegenstand-Sammlung — BEHOBEN (2026-03-01)
- **Problem:** Zwischen 99b (2 Gegenstaende) und 100 (4 Gegenstaende) fehlte die Sammelszene.
- **Fix:** Montage-Szene in 99b eingefuegt: Meier gibt Bronzesiegel im Garten, Frau Bergmann gibt Messingring nach kurzem Zoegern. "Vier Gegenstaende. Vier Familien. Alles komplett."

#### WARNUNG

##### KON-W001: Abschnitt 2 — "Jonas hat geschrieben" statt "gesagt" — BEHOBEN (2026-03-01)
- **Fix:** "geschrieben" → "gesagt" in Abschnitt 02.

##### KON-W002: Abschnitt 42/50b — Bens Rucksack-Luecke — OFFEN
- **Loesung:** In 43 Rucksack-Aufnahme erwaehnen.

##### KON-W003: Cluster C — Taschenlampe vs. Kerze (Bergmanns Erzaehlung) — BEHOBEN (2026-03-01)
- **Fix:** "Kerze" → "Taschenlampe" in Abschnitt 67d.

##### KON-W004: Cluster C — Karls Wegzug: 2 Wochen vs. 1955 — BEHOBEN (2026-03-01)
- **Fix:** Abschnitt 71 "Zwei Wochen spaeter" → "Zwei Jahre spaeter" (konsistent mit 72c: 1955).

##### KON-W005: Cluster C — Fehlender Zeithinweis 82→83 — BEHOBEN (2026-03-01)
- **Fix:** Abschnitt 83 Anfang geaendert: "Am naechsten Morgen war das Rathaus voll."

#### HINWEIS

##### KON-H001: Abschnitt 2→3 — Orts-Sprung ohne Uebergang — OFFEN
##### KON-H002: Abschnitt 3 — Band-1-Item retroaktiv eingefuehrt — OFFEN

---

### 4. Brunnen-Kammer (BRK)

#### FEHLER

##### BRK-F001: Abschnitt 101b — 2 von 4 Wappen falsch zugeordnet — BEHOBEN (2026-03-01)
- **Problem:** Kreuz=Krueger (falsch), Ringe=Bergmann (falsch). Krueger ist keine Gruenderfamilie.
- **Fix:** Kreuz→Bergmann, Ring→Hoffmann. Krueger aus Wappen-Szene entfernt.

#### WARNUNG

##### BRK-W001: Ring-Beschreibung inkonsistent — BEHOBEN (2026-03-01)
- **Fix:** 101b "Zwei verschlungene Ringe" → "Ein Ring" (konsistent mit 25b).

---

### 5. Charakter-Verhalten (CHR)

#### FEHLER
*(keine)*

#### WARNUNG

##### CHR-W001: Abschnitt 46 — Dialog ~30% — OFFEN
- **Loesung:** 2-3 Dialogzeilen einfuegen.

##### CHR-W002: Cluster C — Abschnitte 69, 79, 79b, 80 unter 40% Dialog — OFFEN
- **Problem:** 79b ist dramaturgisch begruendet (Stille-Szene). 69 und 80 koennten mehr Dialog vertragen.

#### HINWEIS

##### CHR-H001: Abschnitte 1, 2 — Dialog ~39% (knapp) — OFFEN

---

### 6. Enden-Format (END)

#### FEHLER

##### END-F001: Sterne-Abweichung Abschnitt 99e — BEHOBEN (2026-03-01)
- **Fix:** Map aktualisiert auf ★★★ "Der eigene Weg" (Datei-Werte sind korrekt). Sterne-Verteilungstabelle angepasst.

##### END-F002: ENDE 215 doppelt (67d + 87) — BEHOBEN (2026-03-01)
- **Fix:** Abschnitt 87 von ENDE 215 auf ENDE 223 umnummeriert. "--" → "—". Map aktualisiert.

##### END-F003: Abschnitt 200 — Replay-Shortcuts fehlen — BEHOBEN (2026-03-01)
- **Fix:** Replay-Shortcuts eingefuegt: "→ Von vorne: Abschnitt 1" und "→ Direkt zur Entscheidung: Abschnitt 7".

##### END-F004: Einleitung — Sterne-System nicht erklaert — BEHOBEN (2026-03-01)
- **Fix:** Sterne-Erklaerung in Abschnitt_00_Einleitung.md eingefuegt: ★★ / ★★★ / ★★★★ mit kindgerechter Beschreibung.

#### WARNUNG

##### END-W001: Cluster B (56-58) — `--` statt `—` und gerade Anfuehrungszeichen — BEHOBEN (2026-03-01)
##### END-W002: Abschnitte 67d, 99e — Sterne inline statt separate Zeile — BEHOBEN (2026-03-01)
- **Fix:** In beiden Abschnitten Sterne auf eigene Zeile verschoben. 200 ebenfalls korrigiert.

##### END-W003: Hinweisseite — "setze sie zusammen" unklar fuer 8-Jaehrige — BEHOBEN (2026-03-01)
- **Fix:** "setze sie zusammen" → "lies sie hintereinander". Tipp konkretisiert: "der Ort, in dem Jonas, Mila und Ben wohnen."

#### HINWEIS

##### END-H001: Abschnitt 87 — Fehlende Replay-Shortcuts (orphaned) — BEHOBEN (2026-03-01)
- **Fix:** Replay-Shortcuts in 87 eingefuegt (zusammen mit ENDE-Umnummerierung END-F002).

##### END-H002: Abschnitt 56 — Bonus-Wissen "fliesst" statt "fließt" — BEHOBEN (2026-03-01)
- **Fix:** "fliesst" → "fließt" im Bonus-Wissen-Text.

---

### 7. Fakten-Konsistenz (FAK)

#### FEHLER

##### FAK-F001: Tippfehler "Hoeeher" in Abschnitt 200 — BEHOBEN (2026-03-01)

##### FAK-F002: Abschnitt 26b — "KRUEGER" statt "HOFFMANN" — BEHOBEN (2026-03-01)
- **Fix:** "KRUEGER" → "HOFFMANN" in Abschnitt 26b.

##### FAK-F003: Abschnitt 96 — "Karl Bergmann" statt "Karl Hoffmann" — BEHOBEN (2026-03-01)
- **Fix:** "Karl Bergmann" → "Karl Hoffmann", "Bergmann" → "Hoffmann", Jonas-Notiz korrigiert.

##### FAK-F004: Initialen K.B. statt K.H. in Abschnitten 79b und 200 — BEHOBEN (2026-03-01)
- **Fix:** K.B. → K.H. in Abschnitt 79b, 200 und Cluster_Konsistenz.md (replace_all).

#### WARNUNG

##### FAK-W001–FAK-W006: Titel-Abweichungen Map vs. Datei — BEHOBEN (2026-03-01)
- **Fix:** Alle 6 Titel in Abschnitt_Map.md auf Datei-Werte aktualisiert:
  - 208: "Das Erbe der Gruender" → "Die Quelle von Eichenhain"
  - 206: "Die verschlossene Quelle" → "Die versiegelte Wahrheit"
  - 207: "Knapp entkommen" → "Der versperrte Weg"
  - 219: "Die verschlossene Tuer" → "Nicht dabei"
  - 210: "Die stille Quelle" → "Die vergessene Urkunde"
  - 209: "Nur der Brief" → "Der Brief aus der Tiefe"

#### HINWEIS

##### FAK-H001: Umlaut-Inkonsistenz — OFFEN

| Stil | Abschnitte |
|------|-----------|
| Echte Umlaute | 1-7, 31-34, 56-58, 84, 85, 87, 105, Einleitung |
| ASCII (ae/oe/ue) | 67d, 106, 99e, 59c, diverse Cluster-A-Abschnitte |
| Gemischt | 86, 104 |

---

### 8. Wissens-Bonus (BON)

#### HINWEIS

##### BON-H001: Abschnitt 45e — "Er wusste es einfach" — OFFEN
- Standard CYOA-Handwave. Akzeptabel.

---

### 9. Entscheidungspunkte (ENT)

#### FEHLER

##### ENT-F001: EP-A5 ist Pseudo-Entscheidung — BEHOBEN (2026-03-01)
- **Problem:** Bei "Nur Brief lesen" (24b) liessen Kinder Truhe zurueck, aber spaetere Abschnitte setzen Truhe voraus.
- **Fix:** Abschnitt 24b erweitert: Jonas entscheidet sich um, rennt zurueck, nimmt Truhe doch mit. Charakter-Moment: "Das hier ist zu wichtig." Die Entscheidung hat jetzt Konsequenzen (Wasser-Entdeckung auf 24b-Pfad), auch wenn die Truhe letztlich mitkommt.

---

### 10. Band-3-Hooks (B3H)

#### WARNUNG

##### B3H-W001: Kein Hook in 3-Stern-Enden 33, 85 — BEHOBEN (2026-03-01)
- **Fix:** In 33 und 85 Ende-Text um Band-3-Hook ergaenzt (zweites X auf der Karte, Wald hinter Eichenhain). Formatierung 85: "--" → "—".

---

## Teil 3: Referenztabellen

### Enden-Uebersicht

| Ende | Abschnitt | Titel (Datei) | Titel (Map) | ★ (Datei) | ★ (Map) | Codewort | Bonus | Replay | B3-Hook |
|------|-----------|---------------|-------------|-----------|---------|----------|-------|--------|---------|
| 206 | 32 | Die versiegelte Wahrheit | Die versiegelte Wahrheit | ★★★ | ★★★ | -- | -- | ja | schwach |
| 207 | 33 | Der versperrte Weg | Der versperrte Weg | ★★★ | ★★★ | -- | -- | ja | ja (BEHOBEN) |
| 208 | 31 | Die Quelle von Eichenhain | Die Quelle von Eichenhain | ★★★★ | ★★★★ | EICHE | ja | ja | ja |
| 209 | 58 | Der Brief aus der Tiefe | Der Brief aus der Tiefe | ★★ | ★★ | -- | -- | ja | -- |
| 210 | 57 | Die vergessene Urkunde | Die vergessene Urkunde | ★★★ | ★★★ | -- | -- | ja | schwach |
| 211 | 56 | Der Brunnen fliesst | Der Brunnen fliesst | ★★★★ | ★★★★ | QUELLE | ja | ja | ja |
| 212 | 86 | Verlaufen | Verlaufen | ★★ | ★★ | -- | -- | ja | -- |
| 213 | 85 | Ohne Lisbeth | Ohne Lisbeth | ★★★ | ★★★ | -- | -- | ja | ja (BEHOBEN) |
| 214 | 84 | Lisbeths Traenen | Lisbeths Traenen | ★★★★ | ★★★★ | STERN | ja | ja | ja |
| 215 | 67d | Die halbe Wahrheit | Die halbe Wahrheit | ★★ | ★★ | -- | -- | ja | -- |
| 216 | 104 | Winters Anruf | Winters Anruf | ★★★★ | ★★★★ | HAIN | ja | ja | ja |
| 217 | 105 | Fast alles | Fast alles | ★★★ | ★★★ | -- | -- | ja | schwach |
| 218 | 106 | Kein Empfang | Kein Empfang | ★★ | ★★ | -- | -- | ja | -- |
| 219 | 34 | Nicht dabei | Nicht dabei | ★★ | ★★ | -- | -- | ja | -- |
| 220 | 59c | Meiers Geheimnis | Meiers Geheimnis | ★★ | ★★ | -- | -- | ja | schwach |
| 221 | 99e | Der eigene Weg | Der eigene Weg | ★★★ | ★★★ | -- | -- | ja | schwach |
| 222 | 200 | Eichenhain | Eichenhain | ★★★★★ | ★★★★★ | ALLE 4 | -- | ja (BEHOBEN) | ja |
| 223 | 87 | Stille am Kirchplatz | Stille am Kirchplatz | ★ | ★ | -- | -- | ja (BEHOBEN) | -- |

### Sterne-Verteilung (nach Fixes — Map und Dateien konsistent)

| Sterne | Anzahl | Enden |
|--------|--------|-------|
| ★ | 1 | 223 (orphaned) |
| ★★ | 6 | 209, 212, 215, 218, 219, 220 |
| ★★★ | 6 | 206, 207, 210, 213, 217, 221 |
| ★★★★ | 4 | 208, 211, 214, 216 |
| ★★★★★ | 1 | 222 (geheim) |

### Fakten-Kanon (aus Common Start 1-7)

| Fakt | Kanonischer Wert | Quelle |
|------|------------------|--------|
| Dorfname | Eichenhain | Abschnitt 1 |
| Gruendungsjahr | 1712 | Abschnitt 6 |
| Gruenderfamilien | Winter, Bergmann, Hoffmann, Meier | Abschnitt 6 |
| Versiegelungsjahr | 1953 | Abschnitt 2 |
| Kinder verschollen | Okt. 1953, 14 Stunden | Abschnitt 4 |
| Lisbeth Bergmann | 10 Jahre alt 1953 | Abschnitt 4 |
| Karl Hoffmann | 11 Jahre alt 1953 | Abschnitt 2, 4 |
| Winter kartiert | 1989 | Abschnitt 2 |
| Brief-Autor | H. W. (Heinrich Winter) | Abschnitt 1 |
| Karls Initialen | K.H. (Abschnitt 16) | Abschnitt 16 |

### Karls-Name-Konsistenz

| Abschnitt | Name im Text | Korrekt? |
|-----------|-------------|----------|
| 02, 04, 15, 16, 30, 45e, 70, 83, 84, 96, 99e | Karl Hoffmann | JA |
| 16, 79b, 200 | K.H. (Initialen) | JA |
| ~~96: Karl Bergmann~~ | ~~NEIN~~ | BEHOBEN |
| ~~79b, 200: K.B.~~ | ~~NEIN~~ | BEHOBEN |

### Brunnen-Kammer-Vergleich

| Element | A (25b) | B (50b) | C (79b) | D (101b) | 200 |
|---------|---------|---------|---------|----------|-----|
| Runde/gewoelbte Kammer | ja (Glocke, ~4m) | ja ("groesser als alles") | ja | ja | ja |
| 4 Nischen | ja | ja | ja | ja | ja |
| 4 Wappen (Stein) | ja, alle 4 benannt | ja, erwaehnt | ja, erwaehnt | ja, alle 4 benannt | ja, erwaehnt |
| Wappen korrekt? | **JA** | (nicht einzeln) | (nicht einzeln) | **NEIN — BRK-F001** | (nicht einzeln) |
| Quelle aus Felsen | ja (klar, eiskalt, Becken, Rinne) | ja (klar, kalt) | ja (leise, gleichmaessig) | ja (klar, leise) | ja (sprudelte) |
| Unter dem Brunnen | ja ("Direkt unter dem Brunnen") | ja ("Wir sind unter dem Brunnen") | implizit | implizit (Winter beschreibt) | implizit |
| Cluster-Fokus | Architektur (Steine, Fugen, "fuer immer gebaut") | Technik (Rohre, Ventil, Reparatur-Plan) | Erinnerung (K.B.+L.B. Inschrift, Traenen) | Winters Stimme (Telefon, 1989, zweite Quelle) | Synthese (alle Familien, Reparatur, Wiedervereinigung) |
| Fokus korrekt? | JA | JA | JA | JA | JA |
| Fremder Fokus? | nein | nein | nein | nein | nein (korrekte Synthese) |
| K.B./K.H. Initialen | — | — | ~~K.B.~~ → K.H. (BEHOBEN) | — | ~~K.B.~~ → K.H. (BEHOBEN) |
| Ring-Beschreibung | "ein Ring" | — | — | ~~"Zwei verschlungene Ringe"~~ → "Ein Ring" (BEHOBEN) | — |
| Wappen korrekt? (nach Fix) | **JA** | (nicht einzeln) | (nicht einzeln) | **JA (BEHOBEN)** | (nicht einzeln) |

**Ergebnis:** Alle Brunnen-Kammer-Fehler behoben. Cluster-Isolation ist sauber (kein Focus-Bleed). Wappen, Initialen und Ring-Beschreibung sind jetzt konsistent ueber alle 5 Abschnitte.

### Ben-Tracker

| Cluster | Lustige Momente | Mutige/Kluge Momente | Nur-Angst |
|---------|----------------|----------------------|-----------|
| Start (1-7) | "Sitzen ist ungefaehrlich" (1), "Brettspiel" (7) | Zitronensaft-Trick (3) | nein |
| A (11-34) | Kappe-Momente | Brunnen-Ausgang entdeckt (26) | nein |
| B (41-59c) | "Monster" (41), "Indiana Jones" (48), "Mittagessen" (59) | Rohre verstehen (50), Brunnen-Ausgang (52), Hahn aufdrehen (55/56) | nein |
| C (66-87) | "Kratzt Katze" (67), "Drache" (74), "Oma-Navi" (79), "Rasen kuessen" (82) | Stilles Zuhoeren (75), Empathie (79b) | nein |
| D (91-106) | "Vielleicht will er nicht reden" (92), nervoes am Telefon (93) | Haelt Telefon (101b), fragt Winter "Warum sind Sie weggegangen?" (101b), notiert mit (96) | nein |

### Pfad-Checkliste

#### Cluster A
- [x] Hauptpfad (Meier): 7→11→...→31
- [x] Krueger-Pfad: 12→14→14c→15
- [x] Ohne Ring: 15→16b→17
- [x] Rechter Gang: 18→20→22
- [x] Mittlerer Gang (DE): 18→20b→18
- [x] Zurueck graben (DE): 25b→26b→26 ~~(NAV-F001: Link falsch)~~ BEHOBEN
- [x] Schreien: 21→33
- [x] Direkt Buergermeister: 28→32
- [x] Aufgeben: 15→34
- [x] Allein probieren (DE): 12→14b→12
- [x] Bonus: 18→18b→19

#### Cluster B
- [x] Hauptpfad (Fluss): 41→42→...→56
- [x] Morgen wiederkommen (DE): 42→43b→42
- [x] Trockener Gang: 45→45b→45c→45d→48 ~~(KON-F004: Wandmalerei)~~ BEHOBEN
- [x] Seitengang: 45→59→59b→59c
- [x] Zurueck Hilfe holen: 48→57
- [x] Rohr-Plaene, Truhe lassen: 50b→57
- [x] Nur Truhe: 54→57
- [x] Regen/eng: 51→58
- [x] Bonus: 45d→45e→48

#### Cluster C
- [x] Hauptpfad: 66→67→68→70→71→73→74→75→77→79→79b→80→81→82→83→84
- [x] Fenster+Fotos: 67→69→70→72→72b→72c→73
- [x] Aufgeben: 67→67b→67c→67d
- [x] Selbst suchen: 74→76→78→**78b (NEU)**→79 ~~(KON-F005: KAPUTT)~~ BEHOBEN
- [x] Hilfe rufen: 78→86
- [x] Truhe allein: 81→85
- [x] Bonus: 70→70b→71

#### Cluster D
- [x] Hauptpfad: 91→92→93→95→96→98→99→100→101→101b→102→103→104
- [x] Mailbox: 92→94→95
- [x] Was ist da unten: 95→97→98
- [x] Zweite Quelle: 98→99b→100 ~~(KON-F008: Sammlung fehlt)~~ BEHOBEN
- [x] Misstrauen: 98→99c→99d→99e
- [x] Aufgeben: 92→106
- [x] Truhe ohne Karte: 102→105
- [x] Bonus: 96→96b→98

#### Easter Egg
- [x] Abschnitt 200
- [x] Hinweisseite
- [x] Einleitung

---

## Top-10 Kritische Fixes (nach Prioritaet) — ALLE BEHOBEN

| # | ID | Problem | Aufwand | Status |
|---|-----|---------|---------|--------|
| 1 | KON-F005 | Cluster C Allein-Pfad ab 80 komplett kaputt | GROSS | BEHOBEN |
| 2 | BRK-F001 | Wappen in 101b falsch | KLEIN | BEHOBEN |
| 3 | KON-F007 | Winter-Widerspruch | KLEIN | BEHOBEN |
| 4 | KON-F002 | Abschnitt 15 Merge Krueger-Pfad | MITTEL | BEHOBEN |
| 5 | FAK-F004 | Initialen K.B.→K.H. | KLEIN | BEHOBEN |
| 6 | FAK-F003 | Karl Bergmann→Hoffmann | KLEIN | BEHOBEN |
| 7 | FAK-F002 | KRUEGER→HOFFMANN in 26b | KLEIN | BEHOBEN |
| 8 | NAV-F001 | Link 26b→27 zu →26 | KLEIN | BEHOBEN |
| 9 | KON-F008 | 99b→100 Sammelszene fehlt | MITTEL | BEHOBEN |
| 10 | ENT-F001 | EP-A5 Pseudo-Entscheidung | MITTEL | BEHOBEN |

---

## Aenderungsprotokoll

| Datum | Abschnitt | Aenderung | Kategorie |
|-------|-----------|-----------|-----------|
| 2026-03-01 | 101b | Wappen: Krueger→Bergmann, Bergmann→Hoffmann, "Zwei verschlungene Ringe"→"Ein Ring" | BRK-F001, BRK-W001 |
| 2026-03-01 | 96 | "Karl Bergmann"→"Karl Hoffmann", Jonas-Notiz korrigiert | FAK-F003 |
| 2026-03-01 | 26b | "KRUEGER"→"HOFFMANN", Link →27 auf →26 | FAK-F002, NAV-F001 |
| 2026-03-01 | 79b | K.B.→K.H. | FAK-F004 |
| 2026-03-01 | 200 | K.B.→K.H., "Hoeeher"→"Hoeher", Karten-Uebergabe von Winter an Jonas | FAK-F004, FAK-F001, KON-F001 |
| 2026-03-01 | Cluster_Konsistenz.md | K.B.→K.H. (replace_all), Familien-Tabelle korrigiert | FAK-F004 |
| 2026-03-01 | 02 | "geschrieben"→"gesagt" | KON-W001 |
| 2026-03-01 | 67d | "Kerze"→"Taschenlampe" | KON-W003 |
| 2026-03-01 | 56, 57, 58 | "--"→"—", gerade→typografische Anfuehrungszeichen | END-W001 |
| 2026-03-01 | 95 | "nie reingegangen"→"einmal reingegangen", Gruenderfamilien Krueger→Hoffmann | KON-F007 |
| 2026-03-01 | 48 | Wandmalerei-Referenz: "noch einmal"→"genauer", Malereien direkt eingefuehrt | KON-F004 |
| 2026-03-01 | 17 | Ring-Einsetzszene am Anfang eingefuegt (vierte Linie, Metalltuer oeffnet sich) | KON-F003 |
| 2026-03-01 | 13c | Krueger wartet am Tunnel mit Silberkreuz (Meier hat ihn gerufen) | KON-F002 |
| 2026-03-01 | 14c | Meier gibt Bronzesiegel auf dem Weg zum Herrenhaus | KON-F002 |
| 2026-03-01 | 99b | Meier+Bergmann Sammelszene eingefuegt (Siegel + Ring) | KON-F008 |
| 2026-03-01 | 78b (NEU) | Kinder gehen zurueck zu Bergmann um Hilfe zu bitten | KON-F005 |
| 2026-03-01 | 78 | Option 1: "Systematisch suchen→80" geaendert zu "Zurueck zu Bergmann→78b" | KON-F005 |
| 2026-03-01 | 24b | Kinder holen Truhe doch noch (Jonas: "Das ist zu wichtig") | ENT-F001 |
| 2026-03-01 | 87 | ENDE 215→223, "--"→"—", Replay-Shortcuts eingefuegt | END-F002, END-H001 |
| 2026-03-01 | 67d | Sterne auf eigene Zeile verschoben | END-W002 |
| 2026-03-01 | 99e | Sterne auf eigene Zeile verschoben | END-W002 |
| 2026-03-01 | 200 | Sterne auf eigene Zeile, Replay-Shortcuts eingefuegt | END-F003, END-W002 |
| 2026-03-01 | 00_Einleitung | Sterne-System erklaert (★★/★★★/★★★★) | END-F004 |
| 2026-03-01 | Hinweisseite | "setze zusammen"→"lies hintereinander", Tipp konkretisiert | END-W003 |
| 2026-03-01 | 56 | Bonus-Wissen "fliesst"→"fließt" | END-H002 |
| 2026-03-01 | 71 | "Zwei Wochen spaeter"→"Zwei Jahre spaeter" | KON-W004 |
| 2026-03-01 | 83 | "Das Rathaus war voll"→"Am naechsten Morgen war das Rathaus voll" | KON-W005 |
| 2026-03-01 | 33 | Band-3-Hook eingefuegt (zweites X auf der Karte) | B3H-W001 |
| 2026-03-01 | 85 | Band-3-Hook eingefuegt, "--"→"—" | B3H-W001 |
| 2026-03-01 | Abschnitt_Map | Titel aktualisiert (6 Enden), 99e auf ★★★, 87 auf ENDE 223, EP-B4b, EP-C4, 78b | FAK-W001-W006, END-F001, END-F002, NAV-W001, KON-F005 |
