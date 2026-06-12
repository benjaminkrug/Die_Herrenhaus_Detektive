# Konsistenz-Fixes Log -- Band 2 Interaktiv

Stand: 2026-03-02

---

## Runde 1 (Session 1): Qualitaetsanalyse

13 Fixes aus erster Qualitaetsanalyse (Score 8.5/10).
Hauptaenderungen: Cliffhanger verstaerkt, Dialog-Anteil erhoeht, Ben-Humor ergaenzt.

---

## Runde 2 (Session 2): Cross-Cluster Konsistenz

14 Fixes aus systematischer Cross-Cluster-Analyse mit 3 parallelen Agenten.

| # | Fehler | Dateien | Aenderung |
|---|--------|---------|-----------|
| F1 | Gruendungsjahr 1823/1743 → 1712 | Ab. 23, 81, 95, 104 | Alle Jahresangaben auf 1712 vereinheitlicht |
| F2 | Brunnen-Datum falsch | Ab. 31 | "Erbaut 1823" → "Erbaut 1712. Versiegelt 1953." |
| F3 | Muenzen 12 → 6 | Ab. 102 | "Zwoelf Stueck" → "Sechs Stueck" |
| F4 | Falsche Symbole | Ab. 49, 54 | "Baum, Hammer, Berg, Stern" → "Stern, Baum, Kreuz, Ring" |
| F5 | Kreuz-Besitz falsch | Ab. 99 | "meiner Mutter" → "Frau Bergmanns Vater" |
| F6 | Ring-Aufbewahrung | Ab. 16 | Sideboard/Kaestchen → Halskette |
| F7 | Truhe-Deckel falsch | Ab. 101 | "Herrenhaus-Wappen" → "Vier Symbole im Kreis" |
| F8 | Muenzen-Beschreibung | Ab. 49 | Generische Beschreibung → "Baum/Stern" |
| F9 | Multi-Entry Ab. 57 | Ab. 57 | Truhe-Oeffnungsmechanik ergaenzt |
| F10 | Urkunde-Wappen | Ab. 23 | "Loewe und Eiche" → "vier Eichen" |
| F11 | Zeitangaben "zweihundert" | Ab. 25b, 30, 32, 102 | → "dreihundert" |
| F12 | Kanonische Fakten | Cluster_Konsistenz.md | Tabelle mit 9 Fakten ergaenzt |
| F13 | Restliches "1823" | Ab. 104 | "1823" → "1712" + "Versiegelt 1953" |
| F14 | "vor hundert Jahren" | Ab. 102 | → "vor dreihundert Jahren" |

---

## Runde 3 (Session 3): Tiefenanalyse

15 Fixes aus erweiterter Analyse (Charakter, Zeitablauf, Geografie, Dialog, Wissens-Lecks).

### KRITISCH (4)

| # | Fehler | Datei(en) | Aenderung |
|---|--------|-----------|-----------|
| K1 | Brunnen "Gebaut 1953" | Ab. 02 Z.45 | "Gebaut 1953" → "Versiegelt 1953" |
| K2 | Quellwasser warm statt kalt | Ab. 73 Z.13+17, Ab. 80 Z.37 | "warm/Warm" → "Eiskalt" (Cluster C an A/B/D angepasst) |
| K3 | Meier-Bauprojekt Wissensleck (Cluster B) | Ab. 45 Z.33, Ab. 47 Z.31, Ab. 54 Z.35+45-59 | Bauprojekt-Referenzen entfernt, durch allgemeine Formulierungen ersetzt |
| K4 | Falsches Symbol gedrueckt | Ab. 49 Z.3 | "Jonas drueckte den Stern" → "den Ring" (letztes Symbol) |

### MODERAT (6)

| # | Fehler | Datei(en) | Aenderung |
|---|--------|-----------|-----------|
| M1 | 5x "zweihundert" bei Gruendungsreferenz | Ab. 24 Z.33, Ab. 28 Z.27, Ab. 29 Z.11, Ab. 32 Z.21, Ab. 58 Z.47 | "zweihundert/Hundert" → "dreihundert" |
| M2a | Brunnen-Seal "hundert Jahre" | Ab. 56 Z.7, Ab. 56 Z.62 | "seit hundert Jahren" → "seit siebzig Jahren" / "nach Jahrzehnten" |
| M2b | Gruender-Werkstatt "hundert" | Ab. 26b Z.35 | "Vor hundert Jahren" → "Vor dreihundert Jahren" |
| M2c | Quelle unfindbar "hundert" | Ab. 99b Z.43, Ab. 200 Z.97+123 | "hundert/fuenfzig" → "siebzig/dreihundert" |
| M3 | Wetter: Sonne statt Wolken in C/D | Ab. 66 Z.31, Ab. 91 Z.31 | "Sonne/Nachmittagslicht" → "dunkle Wolken/Wind" |
| M4 | Kreuz: Jackentasche statt Kette | Ab. 14 Z.19-21 | Jackentasche+Seidenpapier → Silberkette unter Hemd |

### KLEIN (3)

| # | Fehler | Datei(en) | Aenderung |
|---|--------|-----------|-----------|
| M5 | Bergmann Stock fehlt im Stamm | Ab. 05 Z.11 | "In der rechten Hand ein Stock mit Silberknauf" ergaenzt |
| N1 | Bergmann Haar "grau" statt "weiss" | Ab. 67c Z.19 | "Graues" → "Weisses" |
| N4 | Cluster_Konsistenz.md unvollstaendig | Cluster_Konsistenz.md | 5 neue kanonische Fakten ergaenzt (Temperatur, Kreuz, Zeitreferenzen) |

### NICHT GEFIXT (bewusst beibehalten)

| # | Thema | Grund |
|---|-------|-------|
| M6 | Enden-Zaehlung "18" | Korrekt: 18 Enden vorhanden (206-223) |
| N2 | Ben "Kappe ab sonst nie" zu oft | Stilmittel, kein inhaltlicher Fehler |
| N3 | Katze Tuerschwelle vs Fensterbank | Minimaler Detail-Unterschied, akzeptabel |

---

## Runde 4 (Session 3, Fortsetzung): Tiefenanalyse II

3 Agenten parallel: CYOA-Links, NPC+Objekte, Zahlen/Zeit.

### Ergebnis: Fast alles sauber

- **CYOA-Links**: SAUBER (null kaputte Links, null verwaiste Abschnitte, null Dead-Ends)
- **NPC-Konsistenz**: SAUBER (Krueger, Meier, Bergmann alle konsistent)
- **Zahlen/Zeit**: SAUBER (keine falschen Daten mehr)
- **Band 1 Referenzen**: SAUBER

### 1 Fix

| # | Fehler | Datei | Aenderung |
|---|--------|-------|-----------|
| R4-1 | Meier sagt "Winters Siegel" (Bronzesiegel gehoert Meier, nicht Winter) | Ab. 106 Z.37 | "Winters Siegel?" → "Das Siegel meines Vaters?" |

---

## Runde 5 (Session 3, Fortsetzung): Szenen-Logik, Schreibstil, Enden

3 Agenten parallel: Szenen-Logik + Plotloecher, Schreibstil-Regeln, Enden-Qualitaet + Codewort-Platzierung.

### HOCH (5 Fixes)

| # | Fehler | Datei(en) | Aenderung |
|---|--------|-----------|-----------|
| H1 | Truhe verschwindet beim Schacht-Aufstieg | Ab. 27 Z.49 | "Den Rucksack" → "Den Rucksack und die Truhe" |
| H2 | Meiers Feuerwehr-Deadline vergessen | Ab. 28 Z.33 | Meier-Dialog ergaenzt: "Noch fuenf Minuten, und ich haette die Feuerwehr gerufen!" |
| H3 | Codewort-Puzzle Logik unklar (4 Woerter → 2 zusammen) | Hinweisseite Z.7 | "lies sie hintereinander" → "Zwei davon ergeben zusammen ein Wort" |
| H4 | 4x identischer Ben-Spruch "ganz schlechtes Gefuehl" | Ab. 42 Z.9, Ab. 66 Z.13 | "Gefuehl" → "Mein Bauch dreht sich" / "Meine Haende zittern" (Ab. 06+104 als Bookend behalten) |
| H5 | 3x Passiv-Konstruktionen | Ab. 04 Z.23, Ab. 52 Z.13, Ab. 106 Z.53 | Aktiv umgeschrieben (Ab. 104 Tafeltext bewusst belassen) |

### MITTEL (5 Fixes)

| # | Fehler | Datei(en) | Aenderung |
|---|--------|-----------|-----------|
| M1 | Bergmann greift an Kette, Ring aber schon weggegeben | Ab. 103 Z.21 | "griff sie an ihre Kette" → "griff sie an ihre leere Kette" |
| M2 | Codewort STERN im Absatz vergraben | Ab. 84 Z.21 | STERN in eigenen Absatz mit Zeilenumbruechen |
| M3 | Ende 220 Sterne-Formatierung inline statt separate Zeile | Ab. 59c Z.61 | Sterne auf eigene Zeile verschoben |
| M4 | Abstrakte Emotion "Ein Gefuehl, dass..." | Ab. 105 Z.13 | "Ein Gefuehl, dass er etwas uebersehen hatte" → "Sein Magen zog sich zusammen. Er hatte etwas uebersehen." |
| M5 | Regen→Sonnenschein in Cluster C Ausgang | Ab. 82 Z.23+25+27 | "Sonnenlicht/Sonne" → "Tageslicht/Luft" + "Der Regen hatte aufgehoert" |

### NIEDRIG (5 Fixes)

| # | Fehler | Datei(en) | Aenderung |
|---|--------|-----------|-----------|
| N1 | Jonas Knie-Verletzung verschwindet | Ab. 22 Z.21 | "Seine Knie wurden weich" → "Sein Knie pochte noch vom Sturz. Aber das war ihm jetzt egal." |
| N2 | Ben hat unerklarte 2. Taschenlampe | Ab. 07 Z.5 | "Bens Handy daneben — fuer extra Licht" ergaenzt |
| N5 | Schwacher Cliffhanger Ab. 17 | Ab. 17 Z.35 | "Irgendwo in der Dunkelheit fiel ein Stein. Dann war es still." ergaenzt |
| N6a | Ben untercharakterisiert in Ab. 100 | Ab. 100 Z.33 | Ben-Quip ergaenzt: "Wobei — ich bin mutiger. Ich bin wenigstens hier." |
| N6b | Ben untercharakterisiert in Ab. 101b | Ab. 101b Z.29 | Ben-Quip ergaenzt: "Wie ein Passwort aus einem Videospiel." |

### NICHT GEFIXT (bewusst beibehalten)

| # | Thema | Grund |
|---|-------|-------|
| N3 | Map.md Enden-Zaehlung "18" | Korrekt: 18 Enden total (206-223 = 18 Nummern) |
| N4 | Ende 210 strukturell in Choice eingebettet | Niedrige Prioritaet, funktioniert inhaltlich |
| H4b | Ab. 104 Ben-Spruch "schlechtes Gefuehl" | Bewusst beibehalten als Bookend-Callback zum Finale (★★★★-Ende) |
| H5b | Ab. 104 Passiv auf Bronzetafel | Passiv ist bei formalen Inschriften angemessen |

---

## Runde 6 (Session 4): Inventar-Logik, Vokabular, Emotionen

3 Agenten parallel: Dialog-Stimmen+Wortwiederholungen+Satzlaengen, Objekt-Tracking+Inventar, Emotionen+Schreibstil-Regeln+Vokabular.

Dialog-Stimmen: **0 Verstoesse** — alle Charaktere sprechen konsistent.

### HOCH — Inventar-Logik (4 Fixes)

| # | Fehler | Datei(en) | Aenderung |
|---|--------|-----------|-----------|
| H1 | Jonas' Handy nie etabliert (ganzer Cluster D betroffen) | Ab. 07 Z.5 | "Jonas' Handy fuer Notfaelle" ergaenzt |
| H2 | Milas Taschenmesser+Rucksack aus dem Nichts | Ab. 07 Z.33 | "griff ihren Rucksack. Taschenmesser, Kreide, Seil" ergaenzt |
| H3 | 5 Glasflaschen werden zu 2 ohne Erklaerung | Ab. 45 Z.34 | "Jonas steckte zwei Flaschen in seinen Rucksack" ergaenzt |
| H4 | Bens "Taschenlampe" statt Handy-Licht | Ab. 25b Z.5 | "Seine Taschenlampe" → "Sein Handylicht" |

### MITTEL — Vokabular + Emotionen (9 Fixes)

| # | Fehler | Datei(en) | Aenderung |
|---|--------|-----------|-----------|
| M1 | Abstrakte Emotion "fuehlt es sich anders an" | Ab. 11 Z.3 | → "kribbelte es in seinem Bauch" |
| M2 | Abstrakte Emotion "Hoffnung herausfloss" | Ab. 92 Z.43 | → "Seine Schultern sackten zusammen" |
| M3 | Passiv "wurden gesichert" | Ab. 104 Z.15 | → "Sie sicherten die Gaenge" |
| M4a | "ehrfuerchtig" — schwieriges Wort | Ab. 29 Z.3 | → "Wie in einer Kirche" |
| M4b | "ehrfuerchtig" — schwieriges Wort | Ab. 101 Z.13 | → "Als wuerde er beten" |
| M5 | "dokumentieren/Archivieren" | Ab. 105 Z.15 | → "aufschreiben/Wegschliessen" |
| M6 | "Mineralien reflektierten" im Erzaehltext | Ab. 80 Z.7 | → "Glaenzende Steine warfen das Licht zurueck" |
| M6b | "Mineralien" im Erzaehltext | Ab. 101 Z.11 | → "Stein und nassem Moos" |
| M7 | "ignorierte" — Fremdwort | Ab. 16b Z.7 | → "hoerte nicht auf ihn" |
| M8a | "Widerwillig" — schwieriges Wort | Ab. 13c Z.35 | → "Er wollte nicht. Aber er tat es." |
| M8b | "Widerwillig" — schwieriges Wort | Ab. 87 Z.21 | → "Sie wollte nicht. Aber sie kam mit." |

### NIEDRIG (3 Fixes)

| # | Fehler | Datei(en) | Aenderung |
|---|--------|-----------|-----------|
| N1 | "Taschenlampen" Plural falsch | Ab. 43c Z.7 | → "Ihre Lampen" |
| N2 | Rohr-Zeichnungen nie eingepackt | Ab. 50 Z.39 | "Ben rollte die Zeichnungen zusammen" ergaenzt |
| N3 | Satzlaenge >15 Woerter (Ben-Dialog) | Ab. 66 Z.25 | Satz gekuerzt und aufgeteilt |

### NICHT GEFIXT (bewusst beibehalten)

| # | Thema | Grund |
|---|-------|-------|
| — | Dialog-Stimmen | 0 Verstoesse gefunden |
| — | "einstimmig" Ab. 04 | Ben erklaert es sofort ("Alle waren dafuer") |
| — | "Mineralien" in Ben-Dialog | Ben liest von Flasche ab — Kontext mildert |
| — | "historisch"/"Denkmalamt" | Handlungsrelevant, nicht ersetzbar |
| — | Wortwiederholungen ("Wasser" 8x) | Thematisch bedingt |
| — | Ab. 70b Satzlaenge ~18 Woerter | Historisches Zitat, borderline |
| — | Dialog <40% in Ende-Abschnitten | Epilog-Charakter rechtfertigt Beschreibung |

---

## Runde 7 (Session 5): Komplette Leser-Pfade (Story-Logik & Kontinuitaet)

Neuer Ansatz: 5 Agenten lesen komplette Pfade wie ein Kind-Leser, Abschnitt fuer Abschnitt.
Fokus: Story-Logik-Brueche, doppelte Beschreibungen, Wissens-Leaks zwischen Abschnitten.

### HOCH (4 Fixes)

| # | Fehler | Datei(en) | Aenderung |
|---|--------|-----------|-----------|
| H1 | Ring-Einsetz-Szene fehlt komplett (4. Gegenstand) | Ab. 16 Z.53 | 8 Zeilen Ring-Einsetzen vor "---" ergaenzt (Klick, 4 Linien, Tuer oeffnet) |
| H2 | Mila fragt "Wer war Karl?" obwohl sie ihn laengst kennt | Ab. 29 Z.41 | "Wer war Karl?" → "Wie war er?" |
| H3 | "Kruegers Warnung" nur auf einem von zwei Pfaden | Ab. 99 Z.19 | "Kruegers Warnung." → "Die Schaufel. Die frische Erde." |
| H4 | "Drei Kinder damals" — historisch nur zwei (Karl+Lisbeth) | Ab. 200 Z.51 | → "Zwei Kinder am Brunnen, damals. Ein Mann allein in den Gaengen, spaeter." |

### MITTEL (8 Fixes)

| # | Fehler | Datei(en) | Aenderung |
|---|--------|-----------|-----------|
| M1 | Redundanz "Aber er tat es. Aber er hatte es getan." (Bug aus R6) | Ab. 13c Z.35 | "Aber er hatte es getan." entfernt |
| M2 | Drei Abzweigungen + Luftzug-Widerspruch (mittler/links) | Ab. 17 Z.29-33 | "Drei Abzweigungen" und Ben-Dialog+Luftzug entfernt (Wahl ist in Ab. 18) |
| M3 | Bergmann reagiert wie beim 1. Besuch | Ab. 16 Z.11 | "Ihr seid die Kinder vom Herrenhaus" → "Da seid ihr wieder." |
| M4 | Kruegers Kueche riecht unterschiedlich (Kaffee vs Pfeifentabak) | Ab. 96b Z.3 | "Pfeifentabak und altem Holz" → "Kaffee und alten Buechern" |
| M5 | Kammer in Ab. 80 klingt wie Neueintritt (ist schon in Ab. 79b betreten) | Ab. 80 Z.3 | "Die Kammer war gross. Groesser als Jonas erwartet hatte." → "Jonas leuchtete weiter." |
| M6 | Gleiche Kammer klingt wie neuer Raum in Ab. 101b | Ab. 101b Z.5 | "Der Gang oeffnete sich." → "Jonas leuchtete die Waende ab." |
| M7 | Passiv "eingepraegt" im Erzaehltext | Ab. 101 Z.19 | "waren...eingepraegt" → "Vier Symbole bildeten einen Kreis" |
| M8 | Mila beruehrt Wand zweimal in 4 Zeilen | Ab. 17 Z.23 | Erste Wand-Beruehrung entfernt, Dialog erhalten |

### NIEDRIG (3 Fixes)

| # | Fehler | Datei(en) | Aenderung |
|---|--------|-----------|-----------|
| N1 | "heiser" Dopplung in aufeinanderfolgenden Abschnitten | Ab. 101b Z.3 | "heiser" → "rau" |
| N2 | "Wasser in der Rinne stieg" identischer Satz in Ab. 25/25b | Ab. 25b Z.53 | → "Das Wasser stieg auch hier." |
| N3 | Handy wechselt von Lautsprecher zu Ohr ohne Erklaerung | Ab. 100 Z.29 | "Jonas nahm das Handy vom Lautsprecher." ergaenzt |

### NICHT GEFIXT (bewusst beibehalten)

| # | Thema | Grund |
|---|-------|-------|
| — | Truhe oeffnet sich in jedem Cluster anders | CYOA-Design: verschiedene Pfade zeigen verschiedene Aspekte |
| — | Quellen-Beschreibung variiert zwischen Clustern | Verschiedene Teile des Wassersystems |
| — | Winter kennt Jonas' Nummer in Ab. 84 (Cluster C) | 3 Wochen Epilog — Krueger kann sie weitergegeben haben |
| — | HAIN-Codewort sichtbar in Ab. 104 | Gewollt — ★★★★-Ende-Codewort |
| — | "Youtube" in Ab. 25 | Bewusst moderner Ben-Humor |
| — | Umlaut-Encoding (ae/oe/ue) | Projektweites Design |

---

## Gesamtstatistik

| Runde | Fixes | Betroffene Dateien |
|-------|-------|-------------------|
| Runde 1 | 13 | ~20 Abschnitte |
| Runde 2 | 14 | 15 Abschnitte + Cluster_Konsistenz.md |
| Runde 3 | 15 | 18 Abschnitte + Cluster_Konsistenz.md |
| Runde 4 | 1 | 1 Abschnitt |
| Runde 5 | 15 | 16 Abschnitte + Hinweisseite |
| Runde 6 | 16 | 17 Abschnitte |
| Runde 7 | 15 | 13 Abschnitte |
| **Gesamt** | **89** | |

---

## Kanonische Fakten (aktueller Stand)

| Fakt | Wert |
|------|------|
| Gruendungsjahr | 1712 |
| Versiegelung | 1953 (~siebzig Jahre her) |
| Zeitreferenz Gruendung | ~dreihundert Jahre |
| Muenzen | 6 Stueck |
| Symbole | Stern, Baum, Kreuz, Ring |
| Familien | Stern=Winter, Baum=Meier, Kreuz=Bergmann, Ring=Hoffmann |
| Familien-Gegenstaende | Goldener Knopf (Winter), Bronzesiegel (Meier), Silberkreuz (Bergmann/Krueger), Messingring (Hoffmann/Bergmann) |
| Kreuz-Herkunft | Ernst Bergmann (E.B.), Frau Bergmanns Vater |
| Kreuz bei Krueger | An duenner Silberkette unter dem Hemd |
| Ring bei Bergmann | An Halskette |
| Quellwasser | Eiskalt |
| Truhe-Deckel | 4 Symbole im Kreis, Stern in der Mitte |
| Urkunde-Wappen | Vier Eichen |
| Enden | 18 total (206-223), davon 222 = Geheimende |
| Codwoerter | EICHE (208) + QUELLE (211) + STERN (214) + HAIN (216) = EICHENHAIN → 222 |
