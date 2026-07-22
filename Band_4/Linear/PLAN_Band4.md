# Arbeitsplan -- Band 4

## Die Herrenhaus-Detektive, Band 4 (Arbeitstitel: "Das versunkene Dorf")

> Dieser Plan beschreibt **nur das Schreiben des Buchs** (Linear-Version).
> Cover, Publishing, Interaktiv-Version und Marketing sind bewusst NICHT enthalten.
> Vorgehen identisch zu Band 2 + 3 -- gleiche Dateien, gleiche Reihenfolge,
> gleiche Qualitaetsregeln.

------------------------------------------------------------------------

## 1. Dateien und Reihenfolge (uebernommen aus Band 3)

| # | Datei | Funktion | Sorgt fuer ... |
|---|-------|----------|----------------|
| 1 | `Author_Info.md` (Abschnitt "BAND 4" anhaengen) | Continuity-Tracker | **Konsistenz** zu Band 1-3 |
| 2 | `Band_4/Linear/Serienbogen_Band4_5.md` | Was Band 4 loest, was fuer Band 5 offen bleibt | **Kein Kanon-Schulden-Erbe** |
| 3 | `Band_4/Linear/Story_Outline.md` | 4 Akte, 19 Kapitel, je 1 Cliffhanger-Satz | **Spannungsbogen** |
| 4 | `Band_4/Linear/Welt_und_Figuren.md` | See-Geografie, Ruinen-Lageplan, Wasserstand, Figuren-Steckbriefe | **Raeumliche Konsistenz** |
| 5 | `Band_4/Linear/Setup_Payoff_Tracker.md` | Hinweis gesaet -> aufgeloest in Kap X | **Faires Detektiv-Spiel** |
| 6 | `Band_4/Linear/Detaillierte_Szenenplanung.md` | Pro Kapitel Szene 1-4 + Cliffhanger | **Szenen-Dramaturgie** |
| 7 | `Band_4/Linear/Kapitel/...Kapitel1-19.md` | Die 19 Kapiteltexte | Das **Buch** |
| 8 | `Band_4/Linear/qa_messung.py` | Mechanische Messung gegen die Schreibregeln | **Regel-Einhaltung** |
| 9 | `Band_4/Linear/schablonen_analyse.py` | Floskeln + Gleichfoermigkeit (Anti-KI) | **Menschlicher Klang** |
| 10 | `Band_4/Linear/Menschlichkeits_Checkliste.md` | Lesepruefung fuer das Unmessbare | **Was kein Skript sieht** |
| 11 | `Band_4/Linear/create_manuscript.py` | Kompiliert -> `Manuskript.docx` | **Auslieferbares** Manuskript |

**Neu gegenueber Band 3:** Datei 2 (Serienbogen). Begruendung: Band 5 ist das
Serien-FINALE -- danach gibt es keinen Hook mehr, in den man etwas verschieben
kann. Ohne vorher festgelegte Trennlinie verbrennt Band 4 entweder zu viel oder
laesst Band 5 mit unbezahlbaren Schulden zurueck. Der Bogen wird bewusst GROB
gehalten, weil Band 5 sich beim Schreiben von Band 4 noch aendern wird
(Autor-Entscheidung).

**Neu gegenueber Band 3 (Dateien 8-10):** Band 1-3 wurden erst NACH Fertigstellung
geprueft, und die Skripte lagen verstreut (Band 3 Linear: `feinschliff_messung.py`
+ `_dlg_check.py`; Band 1 Interaktiv: `schablonen_analyse.py`). Der Anti-KI-Check
existierte damit bisher NUR fuer die Interaktiv-Baende -- kein Linear-Band wurde je
damit gemessen. Fuer Band 4 wird beides zusammengefuehrt, auf `Kapitel/` portiert
und in den Schreibprozess eingehaengt (siehe Abschnitt 6).

**Zur Geografie-Datei (4):** Band 4 spielt erstmals ausserhalb von Eichenhain,
an einem Schauplatz, der sich im Verlauf des Buchs physisch VERAENDERT (der
Wasserstand sinkt und steigt wieder). Ohne festgehaltenen Lageplan + Pegelstand
pro Tag entstehen zwangslaeufig Widersprueche ("gestern war die Gasse noch
begehbar").

------------------------------------------------------------------------

## 2. Inhaltliche Ausgangslage (aus Band 3 gesaet -- verbindlich)

Aus `Author_Info.md` (Abschnitt Band 3, "Offene Fragen -- FUER BAND 4") und
`Band_3/Linear/Setup_Payoff_Tracker.md` Zeile 12:

- **Die MUENZE** in Jonas' Tasche: Eiche auf einer Seite, FREMDES Symbol auf der
  anderen (3 Wellen + 8-Spitzen-Stern). Zentraler Band-4-Anker.
- **Das Pergament** (bei Winter): unterer Rand abgerissen, bricht ab bei
  *"Die vier Familien kamen aus dem..."*. Die Muenze passt in die Luecke.
- **Winters Satz** (Band 3, Kap 18): *"Ich war nicht der Erste... ihr werdet
  nicht die Letzten sein."* -- muss in Band 4 eine Antwort bekommen.
- **Deutung der Kinder** (Band 3, Kap 18/19): Mila -- "Wasser, ein Meer oder
  grosser Fluss"; Jonas -- "der Stern zeigt einen Weg"; der Ort liegt "weit
  hinter den Huegeln".
- Winter ist zurueck und BLEIBT, Herrenhaus wieder bewohnt. Holzer ist
  Verbuendeter. Meier und Krueger sind etabliert. Die Kinder sind Ehrenbuerger
  und standen namentlich in der Zeitung (Band 3, Kap 17).

**Offene Fragen, die Band 4 beantworten MUSS:**
1. Woher kamen die vier Gruenderfamilien?
2. Was bedeutet das fremde Symbol (3 Wellen + 8-Spitzen-Stern)?
3. Wer hat ausser Winter noch gesucht?
4. Warum haben die vier ihren Herkunftsort verlassen?

------------------------------------------------------------------------

## 3. Festgelegte Konzept-Entscheidungen (mit Autor besprochen und bestaetigt)

### 3.1 Schauplatz: Das versunkene Dorf im See

Der Herkunftsort der Gruender ist **Sternbach**, ein Dorf, das vor rund 300
Jahren in einem See versunken ist. Heute heisst der See anders (der Name
"Sternbach" wurde nach der Flut aus dem Sprachgebrauch getilgt) -- das ist der
Grund, warum Winter ihn jahrzehntelang nicht finden konnte.

**Die Umkehrung (Kern der Entscheidung):** In Band 2 war Wasser das Geheimnis
unter dem Dorf, in Band 3 die Bedrohung fuer das Dorf. In Band 4 ist Wasser
**der Vorhang**. Ein heisser, trockener Sommer laesst den Seespiegel sinken.
Mauern, Gassen, Tuerschwellen und ein Kirchturm tauchen auf -- begehbar zum
ersten Mal seit Generationen.

*Begruendung:* Ein drittes "Wasser bedroht uns"-Buch waere Wiederholung. Gleiches
Element mit umgekehrter Polaritaet liest sich dagegen als bewusstes Serienmotiv.

### 3.2 Der Countdown: das Wasser kommt zurueck

Die Uhr tickt wie in Band 3 in der GEGENWART, aber ohne jede Menschengefahr:
Das Wasser steigt wieder (Ende der Trockenperiode / die Verwaltung schliesst die
Schleusen zum festgesetzten Termin). Danach ist Sternbach fuer Jahrzehnte weg.

**Kindgerecht:** Es besteht zu KEINEM Zeitpunkt Lebensgefahr. Der Einsatz ist
ein Zeitfenster, das sich schliesst -- Spannung aus dem Wettlauf, nicht aus
Bedrohung (CLAUDE.md, Band-3-Regel 5.1 uebernommen).

**Zwei Uhren gleichzeitig:** der steigende Pegel UND die Rivalin, die schneller
ist. Das erzeugt Widerstand in jedem Kapitel, ohne dass Gefahr erfunden werden
muss.

### 3.3 Das Kern-Geheimnis: die fuenfte Familie

Das Wappen von Eichenhain hat VIER Symbole. In Sternbach taucht ein fuenftes
auf: drei Wellen und der achtzackige Stern. Es gehoerte einer fuenften Familie,
die **geblieben ist**, als die anderen vier gingen.

Am See wird die Geschichte seit 300 Jahren andersherum erzaehlt:
*"Die vier haben uns im Stich gelassen. Sind nachts weg. Haben das Dorf
absaufen lassen."*

**Die Wahrheit, die die Kinder beweisen:** Die vier Familien gingen nicht
heimlich und nicht aus Feigheit. Sie zogen los, um **Hilfe und hoeher gelegenes
Land zu holen**, und liessen ein Pfand zurueck -- das Versprechen zurueckzukehren.
Sie kamen zu spaet; das Wasser war schneller. Die fuenfte Familie wartete am
Turm und hat sich seither verraten geglaubt.

*Warum diese Variante:* Sie macht das Serienwappen rueckwirkend zu einer Luege
durch Auslassung -- ein Twist, der auf Band 1-3 aufsetzt, ohne einen Buchstaben
daran zu aendern. Verworfen wurden: (a) "Kirchturm mit Truhe" = Zeitkapsel aus
Band 2 mit nassen Fuessen, Motor stirbt in Akt 2; (b) "das Dorf wurde absichtlich
geflutet" = macht die Gruender rueckwirkend zu Mitwissern und vergiftet Band 1-3.

### 3.4 Der Payoff der Muenze: sie ist kein Hinweis, sie ist ein Pfand

Jede der vier Familien liess beim Aufbruch **eine Muenze** zurueck -- als
Versprechen zurueckzukommen. Jonas traegt seit Band 3 eine davon.

Das Buch endet damit, dass Jonas sie **zurueckgibt**. 300 Jahre zu spaet, aber
er gibt sie zurueck.

*Begruendung:* Damit ist der letzte Gegenstand aus Band 3 keine Wegbeschreibung,
sondern eine Schuld, die eingeloest wird. Das ist der emotionale Zielpunkt des
ganzen Buchs -- er steht VOR der Outline fest, alles andere laeuft darauf zu.

### 3.5 Neue Figur: Nele Ahrens (11) -- die Rivalin

**Die zentrale Neuerung von Band 4.** Kein muerrischer Erwachsener (das war
Holzer in Band 3), sondern ein gleichaltriges Kind.

- Nachfahrin der fuenften Familie, lebt am See, kennt Wasser und Ruinen genau.
- Sucht seit Beginn des trockenen Sommers selbst -- ist den dreien an
  Ortskenntnis ueberlegen und meist einen Schritt voraus.
- **Verlauf (mit Autor festgelegt): erst feindselig, dann falsche Verbuendete.**
  1. *Territorial* ("das ist unser See, verschwindet") -- aktives Hindernis.
  2. *Waffenstillstand*, sie hilft, wird Teil der Gruppe.
  3. *Sie fuehrt sie bei EINER Sache bewusst in die Irre* -- aus Angst vor dem,
     was die drei beweisen koennten. Das Auffliegen ist der TIEFPUNKT in Akt 3.
  4. *Wende*: Sie entscheidet, dass der Streit ihrer Ururgrosseltern nicht ihrer
     ist -- und gehoert am Ende dazu.

*Warum ein Maedchen:* bringt das Team auf 2:2 und oeffnet Milas staerkste
Entwicklung -- sie trifft zum ersten Mal auf jemanden, der schneller und sturer
ist als sie.

*Warum diese Konfliktform:* Die Kinder muessen eine FIGUR lesen, nicht nur
Spuren. Das ist detektivisch reicher als ein reiner Wettlauf und liefert einen
echten Wendepunkt statt 15 Kapitel gleichbleibendem Ton.

### 3.6 Der Reise-Rahmen: der Fall kommt zu ihnen

Ausloeser ist ein **Brief an die Kinder**. In Band 3 (Kap 17) stand ihr Bericht
namentlich in der Zeitung -- jemand am See liest davon und schreibt ihnen:
*"Ich habe von euch gelesen. Bei uns ist etwas aufgetaucht, und niemand hier
will darueber reden."*

Winter erkennt das Symbol im Brief und faehrt sie in den Sommerferien hin.

*Begruendung:* Zum ersten Mal werden die drei **als Detektive angefragt** -- der
natuerliche Serien-Aufstieg fuer Band 4, und er zahlt Band 3 aus, statt einen
Zufall zu erfinden.

**Winters Rolle (Wachpunkt):** Er hat in Band 3 das Finale gerettet. In Band 4
ist er Tueroeffner, nicht Loeser -- vor Ort gebunden mit Erwachsenen-Angelegen-
heiten (Verwaltung, Archiv, Pegeltermine). Die Kinder ermitteln allein.
**Regel: Winter darf keinen einzigen Hinweis fuer die Kinder finden.**

### 3.7 Zeit und Alter

- **Sommer nach Band 3** (Band 3 endete im Herbst) -- also rund 10 Monate spaeter,
  Sommerferien. Erster Band ausserhalb von Eichenhain.
- **ENTSCHIEDEN (2026-07-18): Jonas, Mila und Ben bleiben 10** -- in Band 4 und
  in allen weiteren Baenden. Das Alter waechst NICHT mit. Vollstaendige
  Begruendung als Kanon-Regel in `Author_Info.md`, Abschnitt Charakterprofile.
  Kurz: Das Alter traegt keinen Handlungspunkt, ein mitwachsendes Alter setzt
  Lesereihenfolge voraus (die Reihe wirbt aber mit "jeder Band in sich
  abgeschlossen"), und es erzeugt Buchhaltung fuer jeden kuenftigen Band.
- **Nele Ahrens ist 11** -- das einzige leicht aeltere Kind.

------------------------------------------------------------------------

## 4. Qualitaets-/Konsistenz-Regeln (uebernommen, nicht neu erfunden)

Aus `CLAUDE.md` + `Author_Info.md` + `_Gemeinsam/Schreibstil_Regeln.md`:

- Saetze 8-12 Woerter (max 15), Absaetze 3-5 Zeilen, viel Weissraum
- Dialog mind. 40-50 % pro Kapitel
- 3. Person, nah an Jonas, kein Passiv
- Konkrete Woerter, Emotionen koerperlich ("Herz klopfte"), nie abstrakt
- **Jedes** Kapitel endet mit Cliffhanger; das naechste loest ihn SOFORT auf
- Ben: aengstlich + witzig, ABER mind. 1 mutiger/kluger Signature-Moment
- Mila: mutig, darf verletzlich sein; Jonas fragt, Mila treibt, Ben bremst
- Kapitellaenge Band 4: **900-1.500 Woerter** (Autor-Entscheidung -- bewusst
  breiter als Band 2 + 3, wo 1.200-1.400 galt)
- **AUSNAHME (Autor-Entscheidung, Phase 5): Kapitel 3 darf bis 1.550.**
  Harte Grenze, kein Freibrief -- "minimal nach oben" darf beim Schreiben nicht
  zu 1.700 werden. Begruendung: Kap 3 traegt Ankunft, Winters Namen, Countdown,
  Bens Ablass-Erklaerung, Mini-Entscheidung, Rauschen-Saat und Silhouette; alles
  ist verzahnt, nichts laesst sich streichen, ohne anderswo ein Loch zu reissen.
  **Fuer alle uebrigen Kapitel gilt 1.500 weiterhin als Obergrenze.**
- Umfang: **18 Kapitel + 1 Epilog = 19**, ca. 21.000-23.000 Woerter

### Zur Kapitellaenge: das breitere Fenster ist eine Erlaubnis, kein Ziel

Das Fenster 900-1.500 existiert, damit ein Kapitel so lang sein darf, wie sein
Inhalt es braucht. Ein straffes Verfolgungs-Kapitel darf 950 Woerter haben. Ein
Kapitel, das einen neuen Schauplatz oeffnet, darf 1.450 haben.

**Daraus folgt fuer die Nacharbeit die wichtigste Regel:**

> Ein Kapitel wird NIE verlaengert, um eine Zahl zu erreichen.
> Es wird verlaengert, wenn beim Lesen etwas FEHLT.

**Legitime Verlaengerung** (verteilt in kleinen Portionen ueber das Kapitel,
nicht als ein angehaengter Block):

- **Welt lebendig machen:** was riecht, klingt, knirscht, tropft an diesem Ort.
  Der Schauplatz Sternbach traegt das besonders -- nasser Stein, Schlamm,
  Muschelschalen an einer Hauswand, Fische in einer Gasse.
- **Kurze koerperliche Beats** zwischen Dialogzeilen: wohin jemand schaut,
  was die Haende tun, wer einen Schritt zurueckgeht.
- **Eine Figur reagiert, die gerade nicht dran ist** -- Ben zieht die Muetze
  tiefer, waehrend Mila redet. Das ist gleichzeitig ein Anti-KI-Mittel
  (siehe Abschnitt 6.C).
- **Eine Nebenbemerkung, die nichts vorantreibt**, aber jemanden charakterisiert.
- **Ein Sinneseindruck, der spaeter zum Hinweis wird** (schlaegt zwei Fliegen:
  Laenge + faires Detektivspiel).

**Verbotene Verlaengerung** (= Fuellmaterial, sofort streichen):

- Zusammenfassen, was der Leser gerade gelesen hat
- Eine Figur wiederholt in eigenen Worten, was eine andere eben sagte
- Gefuehle ausbuchstabieren, die die Handlung schon gezeigt hat
- Adjektiv-Ketten und ausgeschmueckte Beschreibungen ohne Funktion
- Dialogzeilen, die nur Zeilen sind ("Okay." -- "Gut." -- "Also los.")

**Pruefung nach jeder Verlaengerung:** Streiche den neuen Satz probeweise wieder.
Fehlt danach etwas? Wenn nein, war es Fuellmaterial.

*Begruendung:* Die Aufforderung "mach das Kapitel laenger" erzeugt zuverlaessig
Leerlauf, weil Aufblaehen der einfachste Weg zur Zahl ist. Genau diese Falle war
in Band 1 Interaktiv der Grund, Phase 5 (Umfang-Ausbau 30k->43k) bewusst NICHT
zu machen. Das Fenster wird nach unten voll genutzt, bevor irgendwo gestreckt wird.
- Jeder Band-3-Hook wird eingeloest (siehe Abschnitt 2)

------------------------------------------------------------------------

## 5. Arbeitsschritte (Phasen)

### Phase 0 -- Konzept-Entscheidungen -- ERLEDIGT
Schauplatz, Countdown, Kern-Geheimnis, Muenzen-Payoff, Rivalin und Reise-Rahmen
sind mit dem Autor geklaert (Abschnitt 3).

### Phase 1 -- Serienbogen Band 4/5
`Band_4/Linear/Serienbogen_Band4_5.md`: Trennlinie festlegen -- was Band 4 loest,
was bewusst fuer das Finale offen bleibt. Band 5 nur als grobe Richtung
(aenderbar).

### Phase 2 -- Continuity erweitern
`Author_Info.md`: Abschnitt **"BAND 4"** anhaengen (analog Band 2/3): Ausgangslage,
neue Figuren, Charakter-Entwicklung, leerer Kontinuitaets-Tracker, offene Fragen
fuer Band 5.

### Phase 3 -- Welt_und_Figuren.md
See-Geografie, Lageplan der Ruinen, **Pegelstand pro Tag** (kritisch fuer
Konsistenz), Steckbriefe Nele + Familie Ahrens + Sternbach-Historie.

### Phase 4 -- Story_Outline.md
4-Akt-Modell, 19 Kapitel mit je 1 Cliffhanger-Satz, Charakter-Entwicklungs-
Tabelle, Band-5-Hook.

### Phase 5 -- Detaillierte_Szenenplanung.md
Pro Kapitel Szene 1-4 + Cliffhanger. Pruefung: Loest Kapitel N+1 den Cliffhanger
von Kapitel N sofort auf?

### Phase 6 -- QA-Werkzeuge bereitstellen (VOR dem ersten Kapitel)
`qa_messung.py` + `schablonen_analyse.py` + `Menschlichkeits_Checkliste.md`
anlegen (Abschnitt 6). Bewusst VOR Phase 7: Die Werkzeuge muessen stehen, bevor
Text da ist -- sonst werden sie nachtraeglich an den vorhandenen Text angepasst,
statt ihn zu pruefen.

### Phase 7 -- Kapitel schreiben (19 Dateien), aktweise mit QA
`Band_4/Linear/Kapitel/Die_Herrenhaus_Detektive_Band4_KapitelX.md`, Reihenfolge
1->19. Nach jedem Kapitel: Continuity-Tracker + Setup/Payoff-Tracker aktualisieren.
Commit-Format: `Kapitel X erweitert (~XXXX Woerter)`.

**Nach jedem Akt (Kap 1-5, 6-10, 11-14, 15-19) den QA-Durchlauf aus Abschnitt 6.**
Nicht erst am Buchende.

### Phase 8 -- Schluss-Durchlauf
Kompletter QA-Durchlauf ueber alle 19 Kapitel (faengt akt-uebergreifende
Wiederholungen, die pro Akt unsichtbar bleiben) + Setup/Payoff-Tracker
vollstaendig abgehakt + Serienbogen Abschnitt 2/3 verifiziert.

### Phase 9 -- Manuskript kompilieren
`create_manuscript.py` aus Band 3 kopieren, Titel/Pfade anpassen
-> `Band_4/Linear/Manuskript.docx`.

------------------------------------------------------------------------

## 6. Qualitaetssicherung (NEU in Band 4)

> Band 1-3 wurden erst nach Fertigstellung geprueft. Das hatte eine Folge, die in
> der Band-1-Interaktiv-Ueberarbeitung deutlich wurde: Am fertigen Buch bleiben
> nur noch Wort-Tausche uebrig -- und genau die fuehlten sich falsch an. Deshalb
> laeuft die Pruefung in Band 4 **nach jedem Akt**, solange Funde noch strukturell
> und billig zu beheben sind.

### 6.0 Die Grundregel (wichtiger als jedes Werkzeug)

> **Die Skripte liefern Kandidaten, keine Urteile.**
> Kein Zielwert ist eine Huerde. Nichts wird automatisch geaendert.
> Jeder Treffer wird im Kontext gelesen und einzeln entschieden.

*Begruendung -- das ist die teuer bezahlte Lehre aus Band 1 Interaktiv:* Dort war
das Ziel "fluesterte unter 40". Es wurde bewusst NICHT erreicht (Endstand 76),
weil die verbleibenden Vorkommen im Kontext richtig sassen. Mechanisch
weiterzudruecken haette bedeutet, ein praezises Verb gegen eine bedeutungsgleiche
Umschreibung zu tauschen -- das Buch waere schlechter geworden. Drei Aenderungen
wurden damals zurueckgenommen. In 3 von 5 Pruefteilen war "kein Eingriff" die
richtige Entscheidung.

**Praktische Konsequenz:** Ein QA-Bericht endet nie mit "X Fehler gefunden",
sondern mit "X Stellen zum Anschauen". Und "geprueft, bleibt so" ist ein
vollwertiges, zu dokumentierendes Ergebnis.

### 6.A `qa_messung.py` -- mechanische Regel-Messung

Zusammenfuehrung von `Band_3/Linear/feinschliff_messung.py` und
`Band_3/Linear/_dlg_check.py`, portiert auf Band 4. Misst pro Kapitel:

- Satzlaenge: Anzahl Saetze > 15 Woerter, laengster Satz
- **Dialoganteil (Wort-Methode, min. 40 %)**
- Abstrakte Emotionen ("spuerte", "seltsames Gefuehl", ...) -- verbotene Muster
- Passiv-Konstruktionen
- **Kapitellaenge gegen das 900-1.500-Fenster** (neu)
- **Cliffhanger vorhanden?** (neu -- Heuristik, siehe unten)

**Zwei bewusste Korrekturen an den Alt-Skripten:**

1. **Dialogmessung vereinheitlicht auf die Wort-Methode.** `feinschliff_messung.py`
   zaehlt ZEILEN, die ein Anfuehrungszeichen enthalten -- eine Zeile mit einem
   einzigen zitierten Wort zaehlt damit voll als Dialog. Das ueberschaetzt den
   Anteil systematisch. `_dlg_check.py` zaehlt Woerter innerhalb der
   Anfuehrungszeichen und ist die richtige Methode.

   **ABER: Die 40-%-Regel ist ein RICHTWERT, kein Muss (Autor-Entscheidung).**
   Kalibrierung an Band 3 ergab: Das fertige, abgenommene Buch liegt bei
   **29 % im Schnitt** (Spanne 16-50 %), **16 von 19 Kapiteln unter 40 %**.
   Gegengeprueft mit dem Original-Skript -- identische Zahlen, die Messung
   stimmt. **Die Reihe erreicht die eigene 40-%-Vorgabe also nie** und liest
   sich trotzdem dialogreich (viele kurze Zeilen, wenig Beschreibung).
   *Folge:* `qa_messung.py` flaggt erst **unter 20 %** -- alles andere waere
   Rauschen. Die 40 % bleiben als Referenz in der Ausgabe sichtbar.

2. ~~**Cliffhanger-Pruefung ergaenzt.**~~ **VERWORFEN nach der Kalibrierung an
   Band 3 (Autor-Entscheidung).** Die Heuristik (Fragezeichen, Ausruf, direkte
   Rede am Schluss, "ploetzlich") markierte **16 von 19 Band-3-Kapiteln** als
   verdaechtig -- obwohl Band 3 durchgehend Cliffhanger hat. **84 % Fehlalarm =
   wertlos.**
   *Grund:* Ein Cliffhanger ist **semantisch, nicht syntaktisch**. "Und dann
   brach der Stein" hat kein Satzzeichen, das ihn verraet.
   **Ersatz:** `qa_messung.py` druckt die **letzten Zeilen jedes Kapitels**
   untereinander -- 19 Schluesse auf einem Bildschirm, in zwei Minuten mit dem
   Auge geprueft. **Das unterstuetzt das Lesen, statt es vorzutaeuschen.**

### 6.B `schablonen_analyse.py` -- Floskeln und Gleichfoermigkeit (Anti-KI)

Portierung von `Band_1/Interaktiv/schablonen_analyse.py` von `Abschnitte/` auf
`Kapitel/`. Die dort hinterlegten ~24 Schablonen sind an echtem Text DIESER
Serie kalibriert (inkl. dokumentiertem False-Positive-Test bei "schluckte") --
sie werden uebernommen, nicht neu erfunden.

**Erweiterung um Varianz-Messung.** Begruendung: Das Alt-Skript zaehlt nur
HAEUFIGKEIT von Floskeln. Der eigentliche Verraeter von KI-Text ist aber
**Gleichfoermigkeit**. Ein Kapitel, in dem jeder Satz 9 Woerter hat, erfuellt
jede Regel in CLAUDE.md und liest sich trotzdem maschinell. Deshalb zusaetzlich:

- **Streuung der Satzlaengen** pro Kapitel (nicht nur Mittelwert)
- **Streuung der Absatzlaengen**
- **Vielfalt der Dialogverben** pro Kapitel (wie viele verschiedene?)
- **Verteilung der Satzanfaenge** (Subjekt-Monotonie: "Er ... Er ... Jonas ...")

Bewusst ausgeschlossen (mit Begruendung):

- **Kommerzielle KI-Detektoren.** Sie messen im Kern Vorhersagbarkeit. Ein
  Kinderbuch mit 8-12-Wort-Saetzen und einfachem Wortschatz ist per Konstruktion
  vorhersagbar -- ein Detektor wuerde dauerhaft anschlagen, und zwar fuer genau
  die Eigenschaften, die die Zielgruppe braucht. Falsches Instrument.
- **Ein numerischer Gesamt-Score.** Laedt zum Optimieren auf die Zahl ein --
  der Band-1-Fehler in Reinform (siehe 6.0).

### 6.C `Menschlichkeits_Checkliste.md` -- die Lesepruefung

Kein Skript. Die Merkmale, die Text wirklich kuenstlich wirken lassen, sind
nicht zaehlbar. Pro Akt durchgehen:

1. **Loest sich jede Szene sauber auf?** Wenn nichts unordentlich liegen bleibt,
   klingt es konstruiert. Echte Szenen lassen Reste zurueck.
2. **Sprechen alle im selben Rhythmus?** Gleiche Satzlaenge, gleiche Bauweise,
   nur andere Woerter = eine Stimme mit vier Namen. Mila und Nele sind hier das
   groesste Risiko (siehe Wachpunkt 5).
3. **Kommen Emotionen immer in derselben Reihenfolge?** Ereignis -> Koerper-
   reaktion -> Dialog, Kapitel fuer Kapitel, ist ein Muster, das auffaellt.
   Reihenfolge bewusst variieren, manchmal einen Teil weglassen.
4. **Hat jedes Kapitel dieselbe Form?** Gleiche Szenenzahl, gleicher Aufbau,
   gleiche Laenge = Formular. Das breitere 900-1.500-Fenster (Abschnitt 4)
   ist auch dafuer da.
5. **Missversteht jemals jemand jemanden?** -- **Der staerkste Einzelindikator.**
   Echte Kinder reden aneinander vorbei, unterbrechen, antworten auf etwas
   anderes, sagen Belangloses. KI-Dialog ist immer effizient: jede Zeile
   transportiert Information, jede Antwort passt zur Frage. Mindestens eine
   Stelle pro Kapitel, an der das NICHT so ist.
6. **Reagiert jemand, der gerade nicht dran ist?** In KI-Text handelt immer nur,
   wer gerade spricht. Ben, der die Muetze tiefer zieht, waehrend Mila redet,
   ist der billigste und wirksamste Gegenmittel-Satz.
7. **Stehen die Figuren still, waehrend sie reden?** *(ergaenzt nach Kapitel 1)*
   Der haeufigste Einzelfehler. Ueber sechs Dialogzeilen ohne eine echte
   Handlung = sprechende Koepfe. **Und: Wenn ein Kapitel zu kurz geraet, fehlt
   fast immer Koerper, nicht Inhalt.**
8. **Erklaert der Erzaehler irgendwo eine Figur?** *(ergaenzt nach Kapitel 1)*
   "Das war seine andere Stimme, die, mit der er manchmal recht hatte" -- solche
   Saetze sind Erwachsenenprosa. Die Figur handelt, der Leser schliesst.

> **Die Schreib-Regeln zur Vorbeugung (R1-R6) stehen am Anfang von
> `Detaillierte_Szenenplanung.md`** -- dort, wo beim Schreiben hingesehen wird.
> Diese Liste hier prueft hinterher.

------------------------------------------------------------------------

## 6.D Dokumenten-Synchronitaet (Autor-Auflage, verbindlich)

> **Die Planungsdokumente sind die Pruefinstanz fuer die Story. Sie sind nur
> etwas wert, wenn sie aktuell sind.**

**Regel:** Eine inhaltliche Aenderung wird **nie in nur einem Dokument**
vorgenommen. Betroffen sind immer:

| Dokument | Was dort stehen muss |
|----------|----------------------|
| `Story_Outline.md` | Kapitelinhalt, Cliffhanger, Zeitleiste, Abschnitt 0 |
| `Detaillierte_Szenenplanung.md` | Szenen, Wortzahl, Wer-treibt, Wachpunkte |
| `Setup_Payoff_Tracker.md` | jede neue Saat + ihr Payoff |
| `Welt_und_Figuren.md` | Geografie, Pegel, Figurendetails |
| `Author_Info.md` | nur bei KANON (Gegenstaende, Figuren, Serienfakten) |

**Warum das als Regel dasteht (teuer gelernt):**
1. Fehler A1/A2 in der Outline entstanden, weil zehn Runden lang chirurgisch
   editiert und nie das Ganze gegengelesen wurde.
2. Beim Beheben von Befund 2 kam heraus, dass die **Szenenplanung schon in zwei
   Punkten gegen die Outline stand**, ohne dass es jemand gemerkt hatte
   (Ortsname im Brief; Aushang am Gemeindehaus statt im Gasthof). Beide
   Widersprueche waren in Phase 5 stillschweigend entstanden.

**Praktisch:**
- Nach jeder Aenderungsrunde: das geaenderte Dokument **komplett** gegenlesen,
  nicht nur die geaenderte Stelle.
- Bei Widerspruch zwischen zwei Dokumenten: **nicht automatisch das neuere
  gewinnen lassen.** Erst pruefen, welche Fassung inhaltlich besser ist --
  bei Befund 2 war das zweimal die Szenenplanung, aber aus sachlichen Gruenden,
  nicht wegen des Datums.
- **Die Zeitleiste (`Story_Outline.md` 2b) ist die Autoritaet fuer alle
  Tages- und Pegelangaben.** Kapiteltexte werden gegen sie geprueft, nie
  umgekehrt.

------------------------------------------------------------------------

## 7. Risiken & Wachpunkte beim Schreiben

1. **Winter darf nicht loesen.** Er hat Band 3 gerettet. Findet er hier auch nur
   einen Hinweis, schrumpfen die Kinder. Pruefung pro Kapitel: Wer hat die
   Entdeckung gemacht?

2. **"Altes Unrecht + Versoehnung" war schon dreimal der Motor** (Band 1, 2, 3).
   Der Unterschied muss spuerbar sein: Hier wird die falsche Geschichte **aktiv
   verteidigt**, nicht beschwiegen -- und versoehnt wird auf KINDER-Ebene, nicht
   zwischen Erwachsenen. Wenn eine Szene sich wie Frau Bergmann anfuehlt: streichen.

3. **Nele darf nicht zur Verraeterin werden.** Ihre Irrefuehrung entspringt Angst,
   nicht Bosheit -- und muss im Rueckblick nachvollziehbar sein. Der Leser soll
   beim Auffliegen "oh nein" denken, nicht "die war von Anfang an gemein".
   Faires Spiel: mindestens zwei Vorzeichen VOR dem Tiefpunkt saeen.

4. **Kein Ertrinken, keine Lebensgefahr.** Der Schauplatz ist Wasser und Schlamm.
   Steigender Pegel = Zeitdruck, nie Todesgefahr. Ein nasser Schuh ist die
   Obergrenze der koerperlichen Folgen.

5. **Fuenf Kinder-Namen sind viel.** Nele muss klar profiliert sein
   (Sprechweise, Tick, Aeusseres), sonst verschwimmt sie mit Mila. Sie ist
   NICHT die zweite Mila: Mila ist laut und stuermt vor, Nele ist leise,
   beobachtet und weiss Dinge, die sie nicht sagt.

6. **Band-5-Hook nicht ueberladen.** Band 5 ist das Finale -- kein weiterer Hook
   danach. Siehe `Serienbogen_Band4_5.md`.

------------------------------------------------------------------------

7. **Das breitere Laengenfenster darf nicht zum Streckmittel werden.** 900-1.500
   ist eine Erlaubnis, kein Ziel (Abschnitt 4). Wenn ein Kapitel bei 1.050 alles
   erzaehlt hat, ist es fertig. Verlaengert wird nur, wo beim Lesen etwas fehlt --
   und dann in kleinen Portionen ueber das ganze Kapitel verteilt, nie als Block.

------------------------------------------------------------------------

## 8. Was dieser Plan bewusst NICHT enthaelt

- Cover, Klappentext, KDP-Setup, Keywords, A+ Content
- Interaktiv-Version (Abschnitte/Verzweigungen)
- Illustrationen

Diese folgen -- wie bei Band 1-3 -- erst NACH dem fertigen Linear-Manuskript.
