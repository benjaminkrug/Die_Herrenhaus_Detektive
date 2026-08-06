# Überarbeitungsplan — Herrenhaus-Detektive Band 1 Interaktiv

**Ziel:** Band 1 Interaktiv auf denselben Reifegrad wie Band 2 bringen —
inhaltlich UND werkzeugtechnisch. Referenz: [Interaktiv_Master_Blueprint.md](../../_Gemeinsam/Interaktiv_Master_Blueprint.md).

**Grundhaltung (aus Memory [[arbeitsweise-feinschliff]]):** Vor jedem Fix
besprechen + begründen. Nur echte Verbesserungen. Nicht über-optimieren. Was
schon gut ist, bleibt.

---

## 0 — Ist-Zustand (gemessen, nicht geraten)

Alle Zahlen aus einer maschinellen Analyse der 96 Dateien am **05.07.2026**.

| Merkmal | Band 1 Interaktiv | Bewertung |
|---------|-------------------|-----------|
| Abschnitte | 96 (94 Story + 2 Meta) | ok, aber weniger als B2 (127) |
| Wörter gesamt | **~31.000** | ⚠️ dünn (B2 ≈ 43.000; Blueprint-Ziel 40–55k) |
| Ø Wörter/Abschnitt | 314 | ✅ im Zielband (280–350) |
| Kürzeste Abschnitte | 143–200 W (12 Stück) | ⚠️ Ausbau-Kandidaten |
| Lange Sätze (>15 W) | praktisch **0** | ✅ Sprache ist sauber |
| Anführungszeichen | einheitlich `„…"` | ✅ Serien-Schema korrekt |
| Umlaute | echte Umlaute, **0** ae/oe/ue-Mischung | ✅ sauber |
| EP-Format | **fett** `→ Abschnitt X` | ✅ korrekt (kein B2-Killerfehler sichtbar) |
| **"flüsterte"** | **83×**, 19 Abschnitte mit ≥2× | ❌ Varianz-Kur nötig |
| "sagte" | 422× | ⚠️ dominiert, aber ok wenn Rest variiert |
| Dialog-Anteil (Messwert) | Ø 22 %, 72/96 unter 30 % | ⚠️ *Messwert unterschätzt* — manuell prüfen |
| **graph.yaml** | **fehlt** | ❌ kein Tooling vorhanden |
| **validate_graph.py** | **fehlt** | ❌ tote Enden nicht ausgeschlossen |
| **QA-Dokumentation** | **fehlt** (nur Abschnitt_Map.md) | ❌ |
| Codewort-/Geheimende-System | fehlt | ✅ **soll fehlen** (bewusst kein Geheimende) |
| **Schablonen / "KI-Klang"** | flüsterte 83×, verschränkte Arme 16×, Herz klopfte 17× … | ❌ Entschablonisierung nötig |

**Kernbefund:** Band 1 ist erzählerisch bereits gut (Sprache sauber, EPs korrekt,
Umlaute sauber). Es fehlen (a) die **Werkzeug-Pipeline**, die B2 nachträglich
bekam, (b) die **Entschablonisierung** (menschlicher Klang statt KI-Formeln) und
(c) ein **Kontinuitäts-/Story-Logik-Check**, den B1 Interaktiv laut Git-Historie
nie hatte (B2 hatte dafür einen eigenen Cross-Error-Report). Optional (d) der
Ausbau auf B2-Umfang. Die Orthografie-Baustellen von B2 (Quotes, Umlaute)
existieren in B1 **nicht** — das spart eine ganze Phase. Ein
Codewort-/Geheimende-System ist **nicht vorgesehen** und soll auch nicht ergänzt
werden.

**Wichtige Ehrlichkeits-Notiz zum Dialog-Messwert:** Der Wert "22 %" zählt nur
Wörter *innerhalb* der Anführungszeichen. Sprecher-Tags ("sagte Mila"),
Reaktionen und Handlungsbeats zwischen Repliken zählen nicht mit. Der Band-2-
Report stellte genau fest, dass diese Metrik "unterschätzt". → **Der Dialog-
Anteil wird NICHT blind hochgeschraubt.** Erst manuell lesen, dann entscheiden.

---

## Phase 1 — Tooling nachrüsten (höchste Priorität, risikoärmste Wirkung)

*Warum zuerst:* Der Validator ist die einzige Absicherung gegen **unerreichbare
Enden**. In B2 fand er einen kritischen Fehler, den 3 manuelle Prüfrunden
übersehen hatten. Bei B1 hat **niemand** je maschinell geprüft, ob alle 14 Enden
erreichbar sind. Das ist das größte unbekannte Risiko.

### 1.1 `graph.yaml` erzeugen
- [ ] `build_graph_yaml.py` aus B2 nach B1 kopieren und an B1-Struktur anpassen
      (96 statt 127 Abschnitte, 14 statt 18 Enden, Cluster A–D, keine
      Brunnen-Kammer, andere Abschnitts-IDs).
- [ ] Quelle der Wahrheit ist die vorhandene [Abschnitt_Map.md](Abschnitt_Map.md)
      (Cluster A 11–32, B 41–59, C 66–86, D 91–105, Enden 106–119).
- [ ] Jeden Abschnitt typisieren: story / choice / bottleneck / branch /
      converge / dead_end / ending.

### 1.2 `validate_graph.py` einrichten & auf 0 Fehler bringen
- [ ] Validator aus B2 kopieren.
- [ ] Laufen lassen. **Erwartung: Es werden Fehler auftauchen**, die bisher
      niemand gesehen hat. Jeden einzeln bewerten:
  - Verwaiste/unerreichbare Enden → **kritisch**, sofort fixen.
  - Tote Verweise (target zeigt ins Leere) → kritisch.
  - Dead-Ends ohne Rücksprung → fixen.
- [ ] Ziel: `validate_graph.py` = **0 Fehler**.

### 1.3 `analyze_quality.py` einrichten
- [ ] Analyse-Skript kopieren (misst Wortzahl, Dialog, flüsterte-Alarm, Sätze).
- [ ] Einmal laufen lassen, Ergebnis als `Qualitaets_Analyse.md` ablegen
      (analog B2).

*Verhältnis zu Phase 2/3:* Die Abschnittslisten in Phase 2 und 3 stammen bereits
aus einer Vorab-Messung (05.07.2026) und sind **vorläufig belastbar**. Die
Analyse hier dient dazu, sie zu **bestätigen und ggf. zu ergänzen** (z. B. wenn
`analyze_quality.py` Dialog-/Sensorik-Schwächen findet, die die reine
Wortzählung nicht sah) — nicht, um bei null anzufangen. Falls die Zahlen
abweichen, gilt der frische Report.

**Ergebnis Phase 1:** B1 hat dieselbe Absicherung wie B2. Tote Enden
ausgeschlossen. *Dies ist der wichtigste Schritt und sollte NICHT übersprungen
werden, auch wenn alles andere optional bliebe.*

---

## Phase 2 — Entschablonisierung / Menschlicher Klang (der Anti-KI-Kern)

*Warum das die wichtigste inhaltliche Phase ist:* Das übergeordnete Ziel ist,
dass der Text **nicht "nach KI" klingt**, sondern menschlich geschrieben wirkt.
Dieselbe Kur brachte in Band 2 den größten Stil-Gewinn — der B2-Report schätzt
den Effekt auf ~7,8 → ~8,4/10 (**Schätzung, nicht neu gemessen**; B2 wurde nach
der Kur nicht erneut durchbewertet). Wichtig ist der Mechanismus, nicht die
Zahl: Der "klingt nach KI"-Eindruck verschwand **ohne Neuschreiben**, nur durch
Diversifizieren wiederkehrender Formel-Wendungen. B1 hat dasselbe Problem, teils
schlimmer. Details/Regeln: Blueprint Abschnitt 2.3b.

KI-Prosa verrät sich durch **vier Schablonen-Typen** (alle in B1 gemessen am
05.07.2026 mit `schablonen_analyse.py`, das im Ordner liegt). Reihenfolge der
Bearbeitung von auffällig → subtil:

**Grundprinzip (aus [[arbeitsweise-feinschliff]]):** Ersetzungen IMMER
kontextbewusst, NIE global. Eine Wendung an ihrem stärksten Moment darf bleiben
— es geht darum, die *Wiederholung* aufzubrechen, nicht die Wendung zu
verbieten. Vor jeder Runde besprechen.

### 2.0 Skript zuerst absichern (Pflicht vor Phase 2)

`schablonen_analyse.py` ist eine Regex-Zählung — sie kann falsch liegen. **Bevor
die Zahlen als Arbeitsgrundlage dienen, einen False-Positive-Test machen**
(so wie der B2-Prozess bei jedem Fix-Skript "0 False Positives" verifizierte):
- [ ] Für 2–3 Muster je ~10 Treffer im echten Text nachschlagen. Prüfen:
      Ist jeder Treffer wirklich die gemeinte Schablone?
      (Bekannte Fallen: `Herz schlug` fängt evtl. "Herz schlug vor Freude" statt
      Angst; `schluckte` fängt evtl. wörtliches Schlucken; die
      Satzanfang-Statistik zählt **auch Sätze innerhalb von Dialogen** mit — die
      "Er 5,3 %" ist also nach oben verzerrt.)
- [ ] Wo ein Muster zu viele Fehltreffer hat: Regex verfeinern ODER die Zahl im
      Plan als "grob, manuell gegenprüfen" markieren, nicht blind als Ziel nehmen.

*Konsequenz:* Die Prozent-Zahl bei Satzanfang-Monotonie (2.4) ist bereits als
verzerrt bekannt — dort zählt nur die *Tendenz*, nicht der genaue Wert.

### 2.1 Typ 1: Dialog-Tics — "flüsterte" (83×, gravierendste)

Regel: **max. 1× "flüsterte" pro Szene** (nicht stumpf pro Datei — ein langer
Abschnitt kann zwei getrennte Szenen enthalten). Behalten wird pro Flüster-Moment
das eine, wo echtes Flüstern dramaturgisch sitzt (Angst/Geheimnis/Nähe).

*Beispiel für die Szenen-Regel:* Abschnitt_03 (667 W) hat 4× "flüsterte", aber
verteilt über zwei Szenen (Gruselgeschichte am Tag / Schatten im Fenster nachts).
Ziel dort ist **~2** (eines pro Szene), nicht 1 — pauschales Runterdrücken auf 1
wäre falsch.

Die 19 Häufungs-Abschnitte (≥2×) — abhakbare Liste (Spalte "lang?" markiert
Abschnitte >500 W, die getrennt auf Szenen geprüft werden):

| Abschnitt | flüsterte × | Wörter | lang? | Ziel |
|-----------|:-----------:|:------:|:-----:|:----:|
| Abschnitt_03 | **4** | 667 | ⚠️ 2 Szenen | ~2 |
| Abschnitt_17 | 3 | 304 | – | 1 |
| Abschnitt_18 | 3 | 332 | – | 1 |
| Abschnitt_20 | 3 | 323 | – | 1 |
| Abschnitt_25 | 3 | 350 | – | 1 |
| Abschnitt_26 | 3 | 368 | – | 1 |
| Abschnitt_94 | 3 | 255 | – | 1 |
| Abschnitt_07 | 2 | 351 | – | 1 |
| Abschnitt_14 | 2 | 182 | – | 1 |
| Abschnitt_21 | 2 | 218 | – | 1 |
| Abschnitt_23 | 2 | 209 | – | 1 |
| Abschnitt_24 | 2 | 200 | – | ≤1 |
| Abschnitt_46 | 2 | 497 | prüfen | 1 |
| Abschnitt_59 | 2 | 338 | – | 1 |
| Abschnitt_69 | 2 | 368 | – | 1 |
| Abschnitt_72 | 2 | 341 | – | 1 |
| Abschnitt_96 | 2 | 275 | – | 1 |
| Abschnitt_99b | 2 | 355 | – | 1 |
| Abschnitt_103 | 2 | 514 | prüfen | 1 |

**Vorgehen pro Abschnitt** (NICHT stumpf ersetzen):
- [ ] Bei den 3 langen Abschnitten (03, 46, 103): erst Szenen abgrenzen, dann
      **max. 1× pro Szene**. Bei allen kurzen: max. 1× gesamt.
- [ ] Für die übrigen Vorkommen: passenderes Verb (sagte / murmelte / raunte /
      brummte / keuchte) ODER das Sprecher-Tag ganz streichen, wenn der Kontext
      klar ist (oft die beste Lösung — weniger ist mehr).
- [ ] Ersetzung zur Figur passend: Ben nervös (stammelte, keuchte), Mila
      bestimmt (sagte, zischte), Jonas ruhig (sagte, murmelte).
- [ ] Ziel danach: "flüsterte" gesamt **unter ~40** (B2 liegt bei 58 bei mehr
      Text). Mit `schablonen_analyse.py` gegenprüfen.

### 2.2 Typ 2: Körperreaktions-Klischees (dieselbe Emotion immer gleich)

Gemessene B1-Häufigkeit — jede beschreibt letztlich Angst/Anspannung:

| Schablone | B1-Ist | Ziel |
|-----------|:------:|------|
| `Herz klopfte/pochte/raste` | **17×** | ~5–6× |
| `verschränkte die Arme` | **16×** | ~5–6× |
| `schluckte` | **15×** | ~5–6× |
| `Atem stockte / hielt den Atem` | 11× | ~5× |
| `Kribbeln / kribbelte` | 10× | ~4× |
| `Magen/Bauch zog sich zusammen` | 3× | ok |

- [ ] Angst/Anspannung auf **verschiedene** Körperzeichen verteilen: feuchte
      Hände, trockener Mund, Beine wie Blei, Ohren rauschen, Zähne
      zusammenbeißen, Gänsehaut, Frösteln …
- [ ] Nicht jede Emotion MUSS körperlich sein — manchmal reicht eine Handlung
      oder ein kurzer Satz. (Über-Beschreibung ist selbst ein KI-Tic.)
- [ ] `verschränkte die Arme` ist Milas Signature-Geste — bewusst 4–5× für ihre
      stärksten Trotz-Momente aufsparen, nicht als Default-Reaktion streuen.

### 2.3 Typ 3: Füll-Übergänge (Weichmacher, die nichts sagen)

| Schablone | B1-Ist | Aktion |
|-----------|:------:|--------|
| `Und dann` (Satzanfang) | **17×** | meist streichbar |
| `plötzlich / Dann, plötzlich` | 4× | fast immer streichbar |
| `Für einen Moment / Einen Moment lang` | 3× | prüfen |
| `Stille.` (Einwort-Satz) | 5× | 2–3 behalten, Rest variieren |

- [ ] "Und dann" und "plötzlich" testweise streichen — die Handlung ist fast
      immer spannender ohne sie (das Überraschende überrascht mehr, wenn es
      nicht angekündigt wird).

### 2.4 Typ 4: Satzanfang-Monotonie (das KI-Stakkato)

B1-Ist: Sätze beginnen mit `Er` 5,3 %, `Jonas` 4,6 %, `Ben` 2,5 %, `Sie` 2,1 %,
`Mila` 1,9 % — fast jeder 6. Satz startet mit einem Figuren-Subjekt. Das erzeugt
das typische "Subjekt-Verb, Subjekt-Verb"-Muster.

- [ ] In den dialogärmeren, beschreibenden Passagen Satzanfänge variieren: mit
      einem Ort, einem Geräusch, einem Objekt, einem Nebensatz beginnen — nicht
      immer mit dem Namen.
- [ ] *Abgrenzung:* Kurze Subjekt-Verb-Sätze sind für 8-Jährige richtig und
      gewollt (Serien-Regel: 8–12 Wörter). Es geht NICHT um komplexere Sätze,
      sondern nur darum, die *Anfänge* abwechslungsreicher zu machen. Nicht
      über-optimieren — Zielgruppe schlägt Eleganz.

### 2.5 Gesamt-Kontrolle
- [ ] `schablonen_analyse.py` erneut laufen lassen. Alle vier Typen sollten
      spürbar gesunken sein (Häufungs-Dateien verschwunden).
- [ ] *Abgrenzung:* "sagte" (422×) muss NICHT unter einen Zielwert — es ist das
      unsichtbare Default-Verb. Nur Monotonie-Nester (3+ in Folge) aufbrechen.

---

## Phase 3 — Inhaltlicher Feinschliff (selektiv, nach analyze-Report)

*Warum selektiv:* B1s Sprache ist bereits sauber. Hier wird NICHT flächendeckend
umgeschrieben, sondern gezielt an den schwächsten Stellen nachgebessert. Die
Auswahl folgt dem `analyze_quality.py`-Report aus Phase 1.3.

### 3.1 Zu kurze Abschnitte prüfen (12 Kandidaten < 200 W)

Reihenfolge nach Kürze:

| Abschnitt | Wörter | Typ (laut Map) | Aktion |
|-----------|:------:|----------------|--------|
| Abschnitt_12 | 143 | Cluster A, Tor/Katze/Lücke | lesen → evtl. +Sensorik/Ben-Moment |
| Abschnitt_13 | 153 | EP-A1 | lesen → Übergang oder echtes Ereignis? |
| Abschnitt_26b | 165 | Dead End (Hämmern) | Dead Ends dürfen kürzer sein — evtl. ok |
| Abschnitt_82 | 175 | Cluster C, Bürgermeister liest | lesen |
| Abschnitt_85 | 177 | Ende ★★★ | Enden brauchen Sensorik-Check (s. 3.2) |
| Abschnitt_52 | 181 | Cluster B, Meier nachts | lesen |
| Abschnitt_14 | 182 | EP-A2 | lesen |
| Abschnitt_26c | 186 | Dead End | evtl. ok |
| Abschnitt_15 | 190 | Cluster A, Archiv/Code | lesen |
| Abschnitt_28 | 197 | EP-A8 | lesen |
| Abschnitt_24 | 200 | Cluster A, Tunnelkarte | Dialog nur 4 % → prüfen |
| Abschnitt_58 | 202 | Ende ★★★ | Sensorik-Check |

- [ ] Jeden lesen. **Nur ausbauen, wenn ein echtes Ereignis/Sinneseindruck/
      Charaktermoment fehlt.** Ein funktionierender kurzer Abschnitt bleibt kurz
      (Blueprint: "Short chapters are better than padded ones").
- [ ] Dead Ends (26b, 26c) dürfen kürzer sein — nur prüfen, ob der Rücksprung
      klar ist.

### 3.2 Sensorik in den 14 Enden (systematischer B2-Schwachpunkt)

Enden von B1: 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119.

- [ ] Jedes Ende lesen. Prüfen: hat es **mindestens 1 Geruch + 1 Klang + 1
      Temperatur/Körpergefühl**? (Das ist die B2-Lehre: Enden sind sensorisch am
      schwächsten, besonders die oberirdischen Dorfplatz-/Gemeindesaal-Szenen.)
- [ ] Wo es fehlt: 2–3 Sätze ergänzen. Kein Umbau, nur Anreicherung.
- [ ] Besonders die 4 ★★★★-Enden (108, 111, 114, 116) verdienen den vollen
      Sensorik-Standard — sie sind die Belohnungs-Enden.

### 3.3 Dialog-Anteil — manuell, nicht per Metrik

- [ ] Die 10 Abschnitte mit dem niedrigsten *gemessenen* Dialog UND wenig
      Handlung lesen (Kandidaten aus Report: 24 (4 %), 99 (5 %), 75 (6 %),
      24b (7 %), 26 (8 %), 21b (9 %), 45 (10 %)).
- [ ] Pro Abschnitt entscheiden: Ist das eine bewusste Atmosphäre-/Fund-Szene
      (dann Dialog OK, evtl. nur ein kurzer Austausch ergänzen) oder ein
      Übergang, der lebendiger werden sollte?
- [ ] **Nicht** mechanisch Dialog einfügen, um eine Prozentzahl zu treffen.

### 3.4 Ben-Klugmomente & Mila-Unsicherheit pro Cluster

- [ ] Prüfen: Hat Ben in **jedem** Cluster (A/B/C/D) mindestens einen
      klugen/mutigen Moment? (In B2 sind das die bestbewerteten Abschnitte.)
- [ ] Hat Mila mindestens 1× im Buch einen Moment der Unsicherheit/Zurückhaltung?
- [ ] Wo eine Figur flach bleibt: einen bestehenden Beat umakzentuieren (kein
      neuer Abschnitt nötig).

---

## Phase 4 — Kontinuitäts- & Enden-Logik-Check (eigene Fehlerklasse!)

*Warum eigene Phase:* Die Phasen 1–3 prüfen **Sprache, Struktur, Klang** — aber
NICHT die **Story-Logik**. Das ist eine komplett andere Fehlerklasse. In B2 gab
es dafür einen eigenen `Cross_Error_Report` mit Faktenfehlern (Timeline,
Gegenstände, Vorwissen). Für B1 Interaktiv wurde eine solche Prüfung laut
Git-Historie **nie durchgeführt**.

*Gute Nachricht:* Das Prüf-Werkzeug existiert bereits. `Cluster_Konsistenz.md`
(im Abschnitte-Ordner) ist eine ausgezeichnete Referenz — globale Fakten
(Schlüssel am **Brunnen**, nicht am Zaun), pro Cluster "was die Kinder
wissen/nicht wissen", und eine Liste häufiger Fehlerquellen. **Aber niemand hat
systematisch geprüft, ob die 96 Abschnitte diese Referenz einhalten.** Genau das
ist diese Phase.

### 4.1 Cross-Cluster-Wissenslecks
- [ ] Für jeden Cluster: Verrät ein Abschnitt Wissen, das nur auf einem *anderen*
      Weg erworben wird? (Beispiel laut Referenz: Wasser-Details dürfen NICHT in
      Cluster A auftauchen.) Die Cluster sind unabhängig.
- [ ] Gegenstände: Hat ein Kind je einen Gegenstand, den es auf diesem Pfad nie
      gefunden hat?

### 4.2 Vorwissen-Artikel & Wiederholungs-Sprache
- [ ] Die in der Referenz markierten Erstbesuch-Abschnitte prüfen — vor allem:
  - **Abschnitt 53** (Cluster B): Kinder betreten das Herrenhaus zum ERSTEN Mal
    → kein "wie vorher/diesmal/wieder", Gemälde mit *unbestimmtem* Artikel.
  - **Abschnitt 105** (Cluster D, Bad Ending): Kinder waren NIE im Herrenhaus
    → kein "wir waren schon drin", keine "gefundenen Sachen".
- [ ] Bestimmte Artikel, die Vorwissen suggerieren ("das Archiv") wo es das erste
      Mal erwähnt wird.

### 4.3 Falsche Figuren-Zitate
- [ ] Krüger sagt im gemeinsamen Start NUR "Räume, die man nicht sieht" +
      "Bleibt weg". Prüfen, dass kein Cluster ihm Zitate in den Mund legt, die er
      dort nie gesagt hat (z. B. über die Mühle).

### 4.4 Enden-Logik (14 Enden faktisch konsistent?)
- [ ] Jedes der 14 Enden gegenlesen: Passt es zum Pfad, über den man es erreicht?
      Werden nur Gegenstände/Wissen vorausgesetzt, die auf diesem Weg erworben
      wurden? (Das ist die inhaltliche Ergänzung zur *strukturellen*
      Erreichbarkeitsprüfung aus Phase 1.2.)

### 4.5 Illustrationsbezüge
- [ ] Es gibt 15 Illustrationen (`Illustrationen/`). Falls Phase 3/Umfang
      Abschnitte umstellt oder Szenen ändert: prüfen, dass kein Bild jetzt zu
      einer Szene gehört, die nicht mehr dort steht.

*Abgrenzung:* Kein Neuschreiben. Diese Phase findet und fixt **Widersprüche**,
sie verbessert nicht die Prosa (das war Phase 2/3).

---

## Bewusst NICHT enthalten: Codewort-System & Geheimes Ende

**Entscheidung des Autors (05.07.2026): Band 1 bekommt KEIN geheimes Ende und
kein Codewort-System.** Anders als Band 2 (Abschnitt 200, ★★★★★) verzichtet
Band 1 bewusst darauf.

- [ ] Sicherstellen, dass **kein** Codewort in die ★★★★-Enden eingebaut wird.
- [ ] Sicherstellen, dass die **Einleitung / Meta-Seite kein** solches System
      verspricht (Abschnitt_00_Einleitung prüfen).
- [ ] graph.yaml: **kein** Abschnitt 200, keine Codewort-Warnung nötig.

*Hinweis für den Blueprint:* Das Codewort-System bleibt dort als **Kann-Option**
für künftige Bände dokumentiert, ist aber kein Reihen-Standard.

---

## Phase 5 — Umfang-Angleichung (optional, größte Arbeit)

B1 hat ~31k Wörter, B2 ~43k. Der Unterschied kommt v. a. aus **31 weniger
Abschnitten** (96 vs. 127) — nicht aus dünneren Abschnitten (Ø-Wortzahl ist
vergleichbar).

▶ ENTSCHEIDUNG offen: **Muss B1 auf B2-Umfang wachsen?**
- **Dafür:** einheitliches Leseerlebnis über die Reihe, mehr Content pro Preis.
- **Dagegen:** B1 funktioniert erzählerisch; 30 neue Abschnitte sind sehr viel
  Arbeit und bergen Konsistenzrisiko. "Nicht über-optimieren" (Memory).
- **Empfehlung:** **Nicht** künstlich aufblähen. Wenn Ausbau, dann gezielt: die
  in Phase 3.1 als "zu dünn, Ereignis fehlt" identifizierten Abschnitte + evtl.
  1–2 Bonus-Verzweigungen pro Cluster (Wiederspielbarkeit), nicht 30 Abschnitte
  auf Vorrat.

---

## Phase 6 — Abschluss

- [ ] Korrekturlese-Runde: je einen ★★★★-Pfad pro Cluster + gemeinsamer Start
      (1–7) manuell lesen. Sucht Tippfehler, Dash-Quotes, Kontinuitätslöcher,
      die Skripte nicht sehen.
- [ ] `validate_graph.py` final = 0 Fehler.
- [ ] `analyze_quality.py` + `schablonen_analyse.py` final (Zielwerte s.
      Definition of Done).
- [ ] **Reihenfolge kritisch:** ERST alle Textänderungen (Phase 2–5) fertig,
      DANN kompilieren. Jede Textänderung nach dem Kompilieren ist im `.docx`
      unsichtbar, bis neu kompiliert wird.
- [ ] Manuskript neu kompilieren (`create_manuscript_interaktiv.py`), Scrambling-
      Verweise prüfen.
- [ ] graph.yaml final gegen die geänderten Dateien abgleichen (IDs bleiben,
      aber Titel/Typen können sich durch Edits verschoben haben).
- [ ] Kontinuität in [Author_Info.md](../../Author_Info.md) und Memory
      ([[band1-interaktiv-todo]]) aktualisieren.
- [ ] `Cluster_Konsistenz.md` gegen finalen Stand abgleichen.

---

## Definition of Done (woran wir erkennen, dass B1 fertig ist)

*Fehlte in der ersten Fassung — "auf B2-Niveau bringen" ist kein messbares Ziel,
zumal B2 selbst nur 7,7/10 mit dokumentierten Schwächen ist. Konkrete Kriterien:*

**Struktur (hart, nicht verhandelbar):** — ✅ ALLE ERFÜLLT
- [x] `validate_graph.py` = 0 Fehler
- [x] Alle 14 Enden strukturell erreichbar (Phase 1) UND inhaltlich pfad-konsistent (Phase 4.4)
- [x] Jede Sackgasse hat einen funktionierenden Rücksprung

**Klang / Anti-KI:** — teils erfüllt, 1 begründete Abweichung
- [x] Top-Körperreaktions-Schablonen: verschränkte Arme 15→**10** (Mila 12→6),
      Herz schlug schneller 5→**2**, schluckte auf **14** bereinigt ✅
- [x] "Und dann sah er es" (wortgleiche Formel) 3→**0** ✅
- [~] **"flüsterte" gesamt 83 → 76** (Ziel war <40). **BEWUSSTE ABWEICHUNG:**
      Der strengere Maßstab (nur echte Nah-Dopplungen ≤6 Zeilen / inhaltlich
      falsche Verben ändern) zeigte, dass die restlichen ~76 an legitimen Stellen
      sitzen (heimliches Eindringen, Schock, Entdeckung). Das Ziel <40 wäre nur
      mit mechanischer Kosmetik erreichbar gewesen (Signalverb → bedeutungsgleiche
      Umschreibung) — genau das, was das Buch schlechter macht. Autor-Entscheidung
      2026-07-05: Qualität vor Zahlenziel. 3 Dateien behalten begründet 3× (03=2
      Szenen; 26/94=Ehrfurcht/heimliches Spähen).

**Inhalt:** — ✅ ERFÜLLT
- [x] Kein Cross-Cluster-Wissensleck (Phase 4.1); Krüger-Zitat-Fehler in 41 behoben (4.3)
- [x] Enden-Logik: alle 14 pfad-konsistent (Phase 4.4). *(Erstbesuch 53/105 waren
      B2-Referenz; B1-Äquivalent 105 in 4.4 mitgeprüft.)*
- [x] Ben hat in A+B klare Klugmomente, in C+D passend emotionale Rolle;
      Mila-Unsicherheit mehrfach belegt (03, 43b, 84, 96, 99) (Phase 3.4)

**Verzichtet (bewusst NICHT im DoD):**
- Dialog-Anteil-Prozentzahl (Metrik unzuverlässig — nur manuell geprüft, Phase 3.3)
- Gesamtwortzahl auf 43k (Umfang-Ausbau Phase 5 übersprungen)
- Geheimes Ende (gestrichen)
- Satzanfang-Monotonie (Phase 2.4: kein echtes Problem, bewusst kein Eingriff)

---

## Reihenfolge-Empfehlung & Aufwand

*Aufwand in groben Arbeitssitzungen à ~2 h — Erfahrungswert, keine Garantie.
Dient der Reihenfolge, nicht der Abrechnung.*

| Phase | Was | Aufwand | Priorität |
|-------|-----|---------|-----------|
| **1** | Tooling nachrüsten + erste Analyse | ~1–2 Sitzungen | **MUSS** — Risiko tote Enden |
| **2** | Entschablonisierung (19 flüsterte + 3 weitere Typen, ~30–35 Abschnitte berührt) | ~3–4 Sitzungen | **HOCH** — Kern der Qualität |
| **3** | Feinschliff Sensorik/Kürze/Dialog (~26 Abschnitte prüfen, davon Teilmenge ändern) | ~2–3 Sitzungen | HOCH |
| **4** | Kontinuitäts- & Enden-Logik-Check (96 Abschnitte gegen Referenz, gezielt) | ~2 Sitzungen | **HOCH** — eigene Fehlerklasse |
| 5 | Umfang-Ausbau (nur bei Bedarf) | ~4+ Sitzungen | OPTIONAL (eher nein) |
| **6** | Korrekturlesen + kompilieren | ~1 Sitzung | **MUSS** (Abschluss) |

**Empfohlener Scope** (bester Aufwand/Nutzen): **Phase 1 + 2 + 3 + 4 + 6.** Das
bringt B1 auf sauberen, menschlich klingenden, strukturell UND inhaltlich
geprüften Stand. Phase 5 nur bei explizitem Wunsch nach mehr Umfang.

**Kein geheimes Ende / Codewort** — bewusst gestrichen (s. o.).

---

## Offene Fragen an den Autor (vor Start zu klären)

1. **Phase 5 (Umfang):** B1 auf ~43k ausbauen oder bei ~31k belassen?
   (Empfehlung: belassen, nur gezielt die zu dünnen Abschnitte aus Phase 3.1.)
2. **Anführungszeichen:** B1 nutzt bereits `„…"` — bleibt so (Serien-Konvention),
   im Gegensatz zu Schattenjägers `»«`. (Nur zur Bestätigung.)

*Geklärt (05.07.2026): Kein Codewort/Geheimende. Anti-KI-Kur ist als Phase 2
fest eingeplant.*
