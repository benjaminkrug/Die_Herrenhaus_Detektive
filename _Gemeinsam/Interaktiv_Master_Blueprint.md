# Interaktiv-Master-Blueprint — Die Herrenhaus-Detektive

**Zweck:** Verbindliche Vorlage für ALLE künftigen interaktiven Bände (CYOA) der
Reihe. Destilliert aus dem Best-of dreier bereits fertiger Bücher:

- **Herrenhaus Band 1 Interaktiv** ("Das verbotene Herrenhaus") — 96 Abschnitte, 14 Enden
- **Herrenhaus Band 2 Interaktiv** ("Das Geheimnis des Brunnens") — 127 Abschnitte, 18 Enden, QA 7.7/10
- **Die Schattenjäger / Geisterspürer CYOA Band 1** ("Das Haus, das flüstert") — 122 Abschnitte, mit graph.yaml + Analyse-Pipeline

**Grundprinzip dieses Dokuments:** Jede Regel unten hat eine *Begründung* aus
einem konkreten Befund. Nichts ist willkürlich. Wo sich die drei Referenzbücher
widersprechen, ist die Entscheidung markiert (▶ ENTSCHEIDUNG) und begründet.

---

## TEIL 0 — Woher die Regeln kommen (Evidenzbasis)

| Quelle | Was sie beisteuert | Beleg |
|--------|--------------------|-------|
| Schattenjäger B1 | **Architektur-Disziplin**: Zonen, Flaschenhälse, graph.yaml, moral_map, Analyse-Skripte, Ziel-Metriken pro Abschnittstyp | `graph.yaml` (103 Abschnitte, 10 Flaschenhälse, 17 EPs), `moral_map.md` (14 Themen), `analyze_quality.py`, `validate_graph_v2.py` |
| Herrenhaus B1 | **Cluster-Idee** (4 tonal getrennte Wege), Codewort-Ansatz noch nicht vorhanden | `Abschnitt_Map.md`: 4 Cluster A–D, je eigene Tonalität, 14 Enden mit ★-System |
| Herrenhaus B2 | **Reifste Umsetzung**: Brunnen-Kammer als geteilter Ort in allen Clustern, Geheimes Ende (★★★★★) per Codewort, 0 Pseudo-Entscheidungen, nachgerüstete graph.yaml | `Abschnitt_Map.md`, `Cross_Error_Report.md`, `Qualitaets_Analyse.md` (7.7/10) |

**Zentrale Lehre aus dem Vergleich:** Herrenhaus B1 und B2 sind erzählerisch
stark, aber B1 hat **kein Tooling** (keine graph.yaml, kein Validator, keine
QA-Doku). B2 hat das Tooling **nachträglich** bekommen — und der Validator fand
sofort einen **kritischen Fehler, den 3 manuelle Prüfrunden übersehen hatten**
(Ende 211 ★★★★ + Ende 209 ★★ waren für Leser *unerreichbar*, weil eine
Entscheidung im falschen Format stand). → **Tooling ist nicht optional. Es ist
die Versicherung gegen tote Enden.** Das ist die wichtigste einzelne Erkenntnis
für alle künftigen Bände.

---

## TEIL 1 — Architektur (die Skelett-Struktur)

### 1.1 Das 4-Cluster-Modell (bewährt, wird beibehalten)

```
              GEMEINSAMER START (7–8 Abschnitte)
                         │
                    EP-MAIN (4 Wege)
              ┌──────────┼──────────┬──────────┐
          CLUSTER A   CLUSTER B  CLUSTER C   CLUSTER D
          Tonalität 1 Tonalität 2 Tonalität 3 Tonalität 4
              │          │          │           │
          4 Enden    4 Enden    4 Enden     4 Enden
              └──────────┴────┬─────┴───────────┘
                     GETEILTER ZIEL-ORT
              (in B2: die Brunnen-Kammer — alle 4 Wege
               führen dorthin, aber auf andere Weise)

    [ KANN-OPTION, pro Band einzeln entscheiden: ]
                    GEHEIMES ENDE (★★★★★)
                 nur über 4 Codewörter erreichbar
```

**Warum 4 Cluster und nicht Pfade wie bei Schattenjäger (A/B/C)?**
Schattenjäger verzweigt *entlang einer Zeitachse* (Prolog → Zone A–F, Pfade
laufen parallel durch dieselben Beats). Herrenhaus verzweigt *nach
Herangehensweise* (4 komplett getrennte Ermittlungswege). Beides funktioniert.
▶ ENTSCHEIDUNG: **Herrenhaus behält das 4-Cluster-Modell** — es ist die
Marken-Identität der Reihe und liefert stärkere Wiederspielbarkeit (jeder
Durchlauf fühlt sich wie eine andere Geschichte an), während Schattenjägers
Modell mehr geteilte Beats hat (effizienter, aber weniger Abwechslung pro
Re-Read).

### 1.2 Jeder Cluster braucht drei Dinge

1. **Eigene Tonalität** — damit sich die Wege unterscheiden. Bewährte Palette:
   - Cluster A: Spannung/Abenteuer (das "Action"-Gerüst)
   - Cluster B: Entdeckung (Natur, Wasser, Staunen)
   - Cluster C: Drama/Emotion (eine Zeitzeugin / eine Figur mit Geschichte)
   - Cluster D: Krimi/Mystery (eine abwesende Schlüsselfigur, Telefon, Rätsel)

   *Begründung:* In B2 ist Cluster C (Zeitzeugin, 7.8) der stärkste, weil die
   emotionale Tiefe (Bergmanns 70-Jahre-Geschichte) trägt. Cluster A/B (je 7.6)
   sind am schwächsten, weil sie sensorisch stark, aber emotional dünner sind.
   → **Jeder Band braucht mindestens einen Cluster mit einem emotionalen
   Herzstück (eine Figur mit echter Vergangenheit).**

2. **Ein Nebengeheimnis** — das nur auf diesem Weg gelöst wird. (B2: Cluster C
   löst "was Bergmann 1953 wirklich sah".) Belohnt Mehrfach-Leser.

3. **Einen geteilten Ziel-Ort** — alle Cluster münden in denselben Kern-Fund
   (B2: Brunnen-Kammer mit den 4 Wappen). *Begründung:* Das hält die
   Gesamtstory kohärent und verhindert, dass sich die 4 Wege zu vier
   verschiedenen Büchern auseinanderentwickeln.

### 1.3 Enden-System (verbindlich)

| Sterne | Anzahl/Band | Bedeutung |
|--------|-------------|-----------|
| ★★★★ | **4** | Ein "perfektes" Ende pro Cluster. |
| ★★★ | 4–6 | Gutes Ende, aber etwas fehlt (Truhe ja, Reparatur nein …) |
| ★★ | 4–6 | Teilerfolg / bitterer Beigeschmack |
| ★ | 1 | Das "Aufgeben"-Ende. Vollständig erzählt, aber melancholisch. |
| ★★★★★ | 0 oder 1 | **KANN-Option** — geheimes Ende, nur über 4 Codewörter. Siehe unten. |

**Gesamtzahl Enden:** 14 (B1) → 18 (B2). ▶ ENTSCHEIDUNG: **Ziel 16–18 pro
Band.** Mehr als 18 verwässert (Content-pro-Durchlauf sinkt unter 15 %); weniger
als 14 fühlt sich für den Preis dünn an.

**Codewort-System / Geheimes Ende — ausdrücklich OPTIONAL, pro Band zu
entscheiden.** Band 2 hat es (Abschnitt 200, ★★★★★); Band 1 hat es *nicht* und
soll es auch nicht bekommen. Es ist also **kein Reihen-Standard**, sondern eine
Idee, die man pro Band bewusst wählt oder verwirft.
- *Wenn ja:* Jedes ★★★★-Ende versteckt EIN Wort natürlich im Text (Gravur,
  Beschriftung, Foto-Rückseite). Die 4 Wörter führen zusammen zu einem geheimen
  Abschnitt. Stärkster Wiederspielbarkeits-Hebel — verwandelt "4 Enden lesen"
  in eine Schatzsuche.
- *Wenn nein:* völlig in Ordnung. Die 4 ★★★★-Enden funktionieren eigenständig;
  kein Wort muss versteckt werden, kein Abschnitt 200 existiert. Dann darf die
  Einleitung auch **kein** solches System versprechen.
- ▶ **Default-Empfehlung: pro Band offen lassen**, nicht automatisch einplanen.

### 1.4 Sackgassen (Dead Ends) — Regeln

- **Zweck:** eine Lehre vermitteln, ohne zu bestrafen. (Schattenjäger:
  "Sackgassen lehren, ohne zu bestrafen".)
- Jede Sackgasse endet mit einem **klaren Rücksprung** ("Das war keine gute
  Idee. Geh zurück zu Abschnitt X und entscheide anders.")
- Eine Sackgasse ist **keine** Strafe für "die falsche" Wahl, sondern zeigt eine
  Konsequenz und gibt sofort eine zweite Chance.
- Ziel: 3–7 Sackgassen pro Band.

### 1.5 Metrik-Zielwerte pro Band (verbindlich)

| Metrik | Zielwert | Quelle/Begründung |
|--------|----------|-------------------|
| Abschnitte gesamt | 100–130 | B1=96, B2=127. Unter 100 zu dünn für den Preis. |
| Wörter gesamt | 40.000–55.000 | B1≈31k (etwas dünn!), B2≈43k |
| Ø Wörter/Abschnitt | 280–350 | B2-Werte; Schattenjäger-Ziel 300–350 |
| Enden | 16–18 | s. o. |
| Entscheidungspunkte | 25–30 | B1≈26, B2≈29 |
| Pseudo-Entscheidungen | **0** | B2 erreichte 0 — Standard für alle Bände |
| Content pro Durchlauf | 15–22 % | genug Neues bei jedem Re-Read |
| ★★★★-Enden | 4 | eines pro Cluster (geheimes ★★★★★ nur, wenn Codewort-Option gewählt) |

---

## TEIL 2 — Schreibregeln (der Prosa-Standard)

Diese Regeln gelten *zusätzlich* zu den generellen Serien-Regeln in
[Schreibstil_Regeln.md](Schreibstil_Regeln.md) und [CLAUDE.md](../CLAUDE.md). Sie
sind auf das interaktive Format zugeschnitten.

### 2.1 Länge & Dichte

- **Ziel 280–350 Wörter pro Abschnitt.** Ein CYOA-Abschnitt ist kürzer als ein
  Linear-Kapitel (1.200–1.400), aber muss trotzdem eine vollständige Mini-Szene
  sein: Bewegung → Ereignis/Fund → Reaktion → Übergang/Weiche.
- **Untergrenze 200 Wörter.** Darunter fühlt sich der Abschnitt nach "Klick ins
  Leere" an. (Schattenjäger hatte viele 150–200-Wörter-Abschnitte als
  Schwäche markiert.)
- **Übergangsabschnitte** (nur "sie gingen von X nach Y") sind die häufigste
  Schwäche. B2-Abschnitt 17 war der schwächste im ganzen Buch, *weil* er ein
  reiner Übergang war. → **Jeder Abschnitt braucht mindestens ein eigenes
  Ereignis**, und sei es klein (ein Fund, ein Ben-Witz, ein Geräusch).

### 2.2 Dialog

- **Ziel 40 % Dialog-Anteil** (Serien-Regel). *Ehrliche Warnung:* automatische
  Messungen unterschätzen das systematisch, weil sie Sprecher-Tags und
  Reaktionen zwischen den Repliken nicht als "Dialog" zählen. → **Immer manuell
  gegenprüfen**, bevor man einen Abschnitt "aufdialogisiert".
- Bei atmosphärischen Szenen (Wasserfall, Dunkelheit, ein Fund) darf Dialog
  bewusst sinken — aber dann mindestens ein kurzer Austausch ("Siehst du das?"
  / "Wow.") gegen das stumme Staunen. *Begründung:* B2 markierte
  Naturszenen mit <30 % Dialog als "die Kinder staunen stumm" — ein kurzer
  Austausch belebt, ohne die Atmosphäre zu brechen.

### 2.3 Dialogverben — die Varianz-Regel (WICHTIG)

Das ist die häufigste handwerkliche Schwäche der Reihe.

- **"sagte" ist der Default und darf dominieren** — aber nicht erdrücken.
- **"flüsterte" ist ein Signal-Verb, kein Füll-Verb.** Es markiert einen echten
  Flüster-Moment (Angst, Geheimnis, Nähe). Wenn drei Figuren in einem Abschnitt
  "flüstern", flüstert niemand mehr — es wird zum Hintergrundrauschen.
- **Harte Grenze: max. 1× "flüsterte" pro Abschnitt** (Ausnahme: eine bewusst
  geflüsterte Szene, dann klar begründet).
- Vielfalt-Palette (erlaubt, sparsam): sagte, fragte, rief, murmelte, brummte,
  keuchte, raunte, zischte, stammelte, antwortete, meinte.
- **Verboten** (zu literarisch/abstrakt für 8-Jährige): entgegnete, erwiderte,
  konstatierte, replizierte, vernahm.

*Begründung mit Zahlen:* Herrenhaus B1 (unbearbeitet) hat **"flüsterte" 83×**
bei 96 Abschnitten — 19 Abschnitte mit ≥2×, einer mit 4×. Nach der Varianz-Kur
in B2 sank "flüsterte" auf 58× (bei mehr Text) und die Palette wurde breiter
(keuchte, raunte, brummte kamen dazu). B1 hat diese Kur noch NICHT durchlaufen.

### 2.3b Menschlicher Klang — Entschablonisierung (der Anti-KI-Standard)

**Das übergeordnete Ziel: Der Text darf nicht "nach KI klingen".** Er soll wie
von einem Menschen geschrieben wirken. Die Dialogverb-Regel (2.3) ist nur EIN
Teil davon — das Problem ist breiter. KI-Prosa verrät sich durch **wiederholte
Formel-Wendungen**: immer dieselbe Körperreaktion, dieselben Füll-Übergänge,
dieselbe Satzmelodie. Kinder merken das nicht bewusst, aber der Text fühlt sich
"glatt und leblos" an — und erwachsene Rezensenten/Käufer erkennen es sofort.

*Belegte Wirkung:* Genau diese Kur hob Herrenhaus B2 stilistisch von ~7,8 auf
~8,4/10 — **ohne Neuschreiben**, nur durch Diversifizieren der Schablonen. Der
"klingt nach KI"-Eindruck verschwand.

**Die vier Schablonen-Typen, die aktiv bekämpft werden** (mit gemessenen
B1-Werten als Warnung, was passiert, wenn man NICHT gegensteuert):

1. **Körperreaktions-Klischees** — dieselbe Emotion immer gleich körperlich.
   B1-Ist: `Herz klopfte/pochte` 17×, `verschränkte die Arme` 16×,
   `schluckte` 15×, `Atem stockte` 11×, `Kribbeln` 10×.
   → *Regel:* Eine Körperreaktion max. ~5–6× im ganzen Buch. Angst/Anspannung
   auf viele verschiedene Körperzeichen verteilen (feuchte Hände, trockener
   Mund, Beine wie Blei, Ohren rauschen, Zähne zusammenbeißen …). Und: nicht
   jede Emotion MUSS körperlich beschrieben werden — manchmal reicht eine
   Handlung oder ein Satz.

2. **Füll-Übergänge** — Satz-Weichmacher, die nichts sagen.
   B1-Ist: `Und dann` 17×, `Dann, plötzlich` / `plötzlich` 4×,
   `Für einen Moment` 3×, `Einen Moment lang`.
   → *Regel:* "Und dann" und "plötzlich" sind fast immer streichbar — die
   Handlung ist ohne sie spannender, nicht weniger.

3. **Dialog-Tics** — siehe 2.3 (flüsterte 83×). Gehört hier mit dazu.

4. **Satzanfang-Monotonie** — zu viele Sätze beginnen mit Subjekt (Er/Sie/Name).
   B1-Ist: Sätze starten mit `Er` 5,3 %, `Jonas` 4,6 %, `Ben` 2,5 %,
   `Sie` 2,1 %, `Mila` 1,9 % — zusammen beginnt fast jeder 6. Satz mit einem
   Figuren-Subjekt im Nominativ. Das erzeugt das typische "Subjekt-Verb,
   Subjekt-Verb"-Stakkato von KI-Kinderbüchern.
   → *Regel:* Satzanfänge variieren — mit einem Nebensatz, einem Ort, einem
   Geräusch, einem Objekt beginnen. Nicht jeder Satz mit dem Namen.

**Messbar mit `schablonen_analyse.py`** (liegt in `Band_1/Interaktiv/`) — zählt
alle vier Typen automatisch und nennt die Top-Häufungs-Dateien. Das ist die
Frühwarnung. Aber: **Ersetzungen immer kontextbewusst, nie global.** Eine
Wendung an ihrem stärksten Moment (der eine echte Herzklopf-Höhepunkt) darf
bleiben — es geht darum, die *Wiederholung* aufzubrechen, nicht die Wendung zu
verbieten.

### 2.4 Sensorik — das systematische Leck

B2s größte Schwäche (7.3/10). Das Muster ist reproduzierbar und muss aktiv
bekämpft werden:

> **Unterirdisch/eng = sensorisch stark. Oberirdisch/Dorfplatz = sensorisch
> flach.**

Sobald die Handlung an die Oberfläche kommt (Dorfplatz, Gemeindesaal, Küche),
verschwinden Gerüche, Temperaturen und Geräusche fast vollständig — **besonders
in den Enden**. Ein ★★★★-Ende (B2/31) beschrieb eine Bronzetafel und blauen
Himmel, aber *kein Vogelgezwitscher, keinen Grasgeruch, keine Sonnenwärme auf
der Haut*.

**Regel:** Jeder oberirdische Abschnitt und **jedes Ende** braucht mindestens
- 1 Geruch,
- 1 Klang,
- 1 Temperatur-/Körpergefühl.

Drei Sätze genügen. Emotionen bleiben immer körperlich ("Herz klopfte", nicht
"er war aufgeregt").

### 2.5 Charakter-Dreieck im CYOA

Jonas beobachtet · Mila drängt · Ben bremst — funktioniert in ~90 % der B2-Szenen.
Die zwei Fehler, die es kaputt machen:

1. **Ben nur als Angsthase.** Ben MUSS pro Cluster mindestens einen klugen/
   mutigen Moment haben (B2: 03 Geheimtinte, 25 Fließrichtung, 50b Rohr-Genie,
   72 Ring-Beobachtung). Diese Momente brechen das Klischee und sind unter den
   bestbewerteten Abschnitten des Buches.
2. **Mila nur als Draufgängerin.** Milas seltene Unsicherheiten (B2: 68, 78b —
   "Mila schweigt zum ersten Mal") geben ihr Tiefe. Mindestens 1× pro Band.

### 2.6 Format-Konventionen (technisch, aber kritisch)

- **Anführungszeichen: `„Text"`** (öffnend U+201E `„`, schließend gerades `"`).
  Das ist das Serien-Schema — NICHT die Guillemets `»«` von Schattenjäger.
  Konsequenz halten; ein Fix-Skript (`fix_quotes.py`) existiert in B2.
- **Umlaute: echte Umlaute + ß**, niemals ae/oe/ue/ss mischen. (`fix_umlaute.py`
  in B2.) B1 muss hierauf geprüft werden.
- **Abgebrochene Rede** endet mit schließendem Quote vor dem Gedankenstrich:
  `—"` nicht `—„`.
- **Weiter-Verweis (linear):** `*→ Weiter bei Abschnitt X*`
- **Entscheidungspunkt:** Muss im **fett**-Format mit klarer Zieladresse stehen:
  `**Option-Text → Abschnitt X**`. *Kritisch:* B2 hatte genau hier den Fehler,
  der zwei Enden unerreichbar machte (kursiv statt fett). → **Der Validator
  prüft das automatisch.**

---

## TEIL 3 — Themen / Moral-Map (das unsichtbare Rückgrat)

Übernommen aus Schattenjägers `moral_map.md` — Herrenhaus B1/B2 hatten keine
explizite Themenkarte, sollten aber eine bekommen.

**Grundregel: "Show, don't tell." Kein Thema wird ausgesprochen** ("Die Moral
ist …"). Die Lehre ergibt sich aus den **Konsequenzen** der Wahl.

Empfohlene Themen-Palette für Herrenhaus (Krimi/Freundschaft, kein Übernatürliches):

| # | Thema | Wie es sich in einer Wahl zeigt |
|---|-------|--------------------------------|
| 1 | Mut = Angst haben UND handeln | Mutige Option schneller, aber riskanter |
| 2 | Freundschaft/Team > Alleingang | Sackgassen beweisen es (allein scheitert) |
| 3 | Kritisches Denken statt Gerücht | Fakten prüfen schlägt erstem Impuls |
| 4 | Verantwortung übernehmen | Nicht weglaufen, auch wenn einfacher |
| 5 | Vorurteile überwinden | Die skurrile Nachbarin ernst nehmen zahlt sich aus |
| 6 | Ehrlichkeit ≠ immer klug (Kommunikation) | Wann sagt man Erwachsenen die Wahrheit? |
| 7 | Zuhören / Ältere ernst nehmen | Die Zeitzeugin öffnet sich nur dem Zuhörer |
| 8 | Geduld vs. Ungeduld | Warten kostet manchmal — Überstürzen auch |

**Checkliste pro Band** (aus Schattenjäger):
- [ ] Jede Entscheidung hat ≥1 zugeordnetes Thema
- [ ] Kein Thema wird direkt ausgesprochen
- [ ] Die Lehre ergibt sich aus Konsequenzen
- [ ] Sackgassen lehren ohne zu bestrafen
- [ ] Themen-Verteilung ausgewogen (kein Thema >6×, keines 0×)
- [ ] Humor nach jedem Grusel/Schreck (Sicherheitsnetz)

---

## TEIL 4 — Tooling-Pipeline (die Qualitätsversicherung)

**Nicht optional.** Das ist die Lehre aus dem B2-Fund. Reihenfolge:

### 4.1 `graph.yaml` — die Single Source of Truth

Maschinenlesbare Beschreibung aller Abschnitte: id, title, file, type
(story/choice/bottleneck/branch/converge/dead_end/ending), cluster, next-Ziel
ODER choices[] mit targets, ending_id + stars, dead_end return_to. Vorbild:
Schattenjäger `graph.yaml` und die nachgerüstete B2 `graph.yaml`.

### 4.2 `validate_graph.py` — muss 0 Fehler liefern

Prüft automatisch:
- **Erreichbarkeit:** Ist jeder Abschnitt vom Start aus erreichbar? (Fängt
  verwaiste Enden — der B2-Killerfehler.)
- **Tote Verweise:** Zeigt jedes target auf eine existierende Abschnitts-ID?
- **Enden-Vollständigkeit:** Hat jeder ending-Abschnitt einen stars-Wert?
- **Format:** Steht jede Entscheidung im korrekten `**… → Abschnitt X**`-Format?
- **Sackgassen:** Hat jede dead_end einen return_to?
- Erlaubte Warnung: das Codewort-Geheimende (per Design nicht "normal" erreichbar).

### 4.3 `analyze_quality.py` — die Prosa-Metriken

Pro Abschnitt: Wortzahl, Dialog-Anteil, Dialogverb-Verteilung (flüsterte-Alarm!),
lange Sätze (>15 Wörter), Passiv-Konstruktionen, verbotenes Vokabular,
Quote-/Umlaut-Konsistenz. **Wichtig:** Metriken sind Frühwarnung, kein Urteil —
immer manuell gegenprüfen (Dialog-% und Sensorik werden systematisch
unterschätzt).

### 4.3b `schablonen_analyse.py` — der Anti-KI-Check

Zählt die vier Schablonen-Typen aus 2.3b: Körperreaktions-Klischees,
Füll-Übergänge, Dialog-Tics und Satzanfang-Monotonie — mit Häufigkeit pro 10.000
Wörter und den Top-Häufungs-Dateien. Dient dazu, den "klingt nach KI"-Eindruck
messbar und gezielt abzubauen. **Kontextbewusst anwenden** (s. 2.3b), nicht
global ersetzen.

> **Regex-Skripte immer mit False-Positive-Test benutzen.** Alle Analyse-/Fix-
> Skripte sind Muster-Zählungen und können falsch treffen (die
> Satzanfang-Statistik zählt z. B. auch Dialog-Sätze mit → nach oben verzerrt).
> Der B2-Prozess verifizierte bei jedem Fix-Skript "0 False Positives" an einer
> Stichprobe, bevor er es anwandte. Das ist Pflicht, keine Kür.

### 4.4 Fix-Skripte (aus B2 wiederverwendbar)

- `fix_quotes.py` — vereinheitlicht auf `„Text"`
- `fix_umlaute.py` — echte Umlaute + ß, keine ae/oe/ue/ss-Mischung
- `build_graph_yaml.py` — generiert/aktualisiert graph.yaml aus den Dateien
- `create_manuscript_interaktiv.py` — kompiliert + verwürfelt die Reihenfolge
  (Scrambling), damit man nicht linear "durchblättern" kann

### 4.5 Kontinuitäts-/Story-Logik-Check — eigene Fehlerklasse

Skripte prüfen **Sprache und Struktur**, aber nicht die **Story-Logik**. Fakten
über Cluster hinweg, Vorwissen an Erstbesuch-Stellen, korrekte Figuren-Zitate,
pfad-konsistente Enden — das findet nur ein manueller Durchgang. Werkzeug dafür:
eine `Cluster_Konsistenz.md` (globale Fakten + pro Cluster "was die Kinder
wissen/nicht wissen" + typische Fehlerquellen) als **Referenz zum aktiven
Abgleich**, plus ein `Cross_Error_Report` wie in B2. Nicht mit der
*strukturellen* Erreichbarkeitsprüfung (4.2) verwechseln — die sagt nur, dass ein
Ende erreichbar ist, nicht dass es inhaltlich zum Pfad passt.

---

## TEIL 5 — Der Workflow für einen NEUEN interaktiven Band

1. **Konzept:** Kernfall + geteilter Ziel-Ort + 4 Cluster-Tonalitäten + das
   emotionale Herzstück (eine Figur mit Vergangenheit) festlegen.
2. **Struktur:** `Abschnitt_Map.md` schreiben — Cluster, EPs, Enden, ★-Verteilung,
   Sackgassen mit Rücksprüngen. **Hier entscheiden:** Codewort/Geheimende — ja
   oder nein? (Kann-Option, kein Automatismus.)
3. **Moral-Map:** Jeder EP bekommt ein Thema (verdeckt).
4. **Schreiben:** Abschnitt für Abschnitt nach den Regeln aus Teil 2. Nach jedem
   Cluster: Ben-Klugmoment + Mila-Unsicherheit + Sensorik-Check.
5. **graph.yaml bauen** (`build_graph_yaml.py`), **validieren** (`validate_graph.py`
   → 0 Fehler), **analysieren** (`analyze_quality.py` + `schablonen_analyse.py`
   → menschlicher Klang, keine Schablonen-Nester).
6. **Kontinuitäts-Check** (4.5): Alle Abschnitte gegen die `Cluster_Konsistenz.md`
   abgleichen — Cross-Cluster-Wissen, Vorwissen-Artikel, Enden-Logik.
7. **Korrekturlese-Runde:** Je einen ★★★★-Pfad pro Cluster + den Start manuell
   lesen. (Skripte finden keine Tippfehler/Dash-Quotes — Menschen schon.)
8. **Fix-Skripte** laufen lassen (Quotes, Umlaute), erneut validieren.
9. **Kompilieren + Scrambling** — ERST wenn alle Textänderungen fertig sind, sonst
   ist die Änderung im `.docx` unsichtbar. Verweise prüfen.
10. **Kontinuität** in Author_Info.md nachtragen.

---

## TEIL 6 — Was der jeweils NÄCHSTE Band besser machen soll (aus B2-Report)

1. **Oberirdische Szenen aktiver:** Gespräche während Handlungen (Laufen,
   Suchen, Reparieren), nicht nur im Sitzen.
2. **Mindestens ein Cluster, der NICHT am Zielort/unterirdisch spielt** — gegen
   die sensorische Monokultur (z. B. ein Dorf-Konflikt, eine Intrige).
3. **Expositions-Tunnel vermeiden:** max. 2 aufeinanderfolgende Erklär-Abschnitte
   (B2/Cluster D hatte 4 hintereinander: 95/96/96b/97).
4. **Pfad-Redundanz vermeiden:** kein Abschnitt darf zu >50 % wortgleich mit
   einem anderen sein (B2/99b ≈ 99 bestrafte Mehrfach-Leser).
5. **Enden sensorisch aufrüsten:** jedes Ende Geruch + Klang + Temperatur.

---

*Dieses Dokument ist die Referenz. Wenn ein künftiger Band davon abweicht, muss
die Abweichung begründet werden — nicht umgekehrt.*
