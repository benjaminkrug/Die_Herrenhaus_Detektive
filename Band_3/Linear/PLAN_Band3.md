# Arbeitsplan -- Band 3

## Die Herrenhaus-Detektive, Band 3 (Arbeitstitel: "Die zweite Quelle")

> Dieser Plan beschreibt **nur das Schreiben des Buchs** (Linear-Version).
> Cover, Publishing, Interaktiv-Version und Marketing sind bewusst NICHT enthalten.
> Vorgehen identisch zu Band 2 -- gleiche Dateien, gleiche Reihenfolge, gleiche Qualitaetsregeln.

------------------------------------------------------------------------

## 1. Warum dieser Plan so aussieht (Begruendung)

Ich habe Band 2 als Referenz genommen, weil du "gleiches Vorgehen" willst.
Band 2 bestand aus **5 Datei-Typen**, die in einer bestimmten Reihenfolge entstehen.
Jeder Typ hat eine klare Funktion fuer Konsistenz / Spannung / Qualitaet:

**Standard-Dateien (wie Band 1+2 -- Linear brauchte nur diese 3 Planungsdateien):**

| # | Datei | Funktion | Sorgt fuer ... |
|---|-------|----------|----------------|
| 1 | `Author_Info.md` (Abschnitt "BAND 3" anhaengen) | Continuity-Tracker: Zeitlinie, Gegenstaende, Wissen der Kinder, neue Figur | **Konsistenz** -- kein Widerspruch zu Band 1+2 |
| 2 | `Band_3/Linear/Story_Outline.md` | Dramaturgisches Geruest: 4 Akte, 19 Kapitel, je 1 Cliffhanger-Satz | **Spannungsbogen** ueber das ganze Buch |
| 3 | `Band_3/Linear/Detaillierte_Szenenplanung.md` | Pro Kapitel: Szene 1-4 + Cliffhanger | **Szenen-Dramaturgie**, kein Leerlauf |
| 6 | `Band_3/Linear/Kapitel/...Kapitel1-19.md` | Die eigentlichen 19 Kapitel-Texte | Das **Buch** selbst |
| 7 | `Band_3/Linear/create_manuscript.py` | Kompiliert Kapitel -> `Manuskript.docx` | **Auslieferbares** Manuskript |

**Zusatz-Dateien (NEU fuer Band 3 -- fangen neue Komplexitaet ab, die Band 2 nicht hatte):**

| # | Datei | Funktion | Sorgt fuer ... |
|---|-------|----------|----------------|
| 4 | `Band_3/Linear/Welt_und_Figuren.md` | Wald-Geografie, Einsturz-Geologie, Foerster-Steckbrief + Wissensstand | **Raeumlich-physische Konsistenz** ueber 19 Kapitel |
| 5 | `Band_3/Linear/Setup_Payoff_Tracker.md` | Tabelle: Hinweis gesaet -> aufgeloest in Kap X | **Faires Detektiv-Spiel** (Tschechows Gewehr) |

*Begruendung Zusatzdateien:* Band 3 fuehrt mit Wald + Quelle + Foerster mehr neue
Welt-Mechanik ein als Band 2 (dort nur eine Person, Frau Bergmann). Die Analyse-
Dateien aus Band 2 existierten NUR in der Interaktiv-Version (96 Abschnitte). Fuer
19 lineare Kapitel waeren die meisten davon Buerokratie -- diese 2 sind die einzigen,
die echten Mehrwert bringen.

**Begruendung der Reihenfolge:** Erst Continuity (1), damit nichts den bisherigen
Kanon bricht. Dann das grobe Geruest (2), dann die feine Szenenplanung (3) --
so wird jeder Cliffhanger im naechsten Kapitel aufgeloest, BEVOR Prosa entsteht.
Die Zusatz-Dateien (4, 5) werden PARALLEL dazu gefuellt (nicht vorab erfunden).
Erst danach die Kapitel (6). Die `.docx`-Kompilierung (7) kommt zuletzt, weil sie
nur fertigen Text buendelt.

------------------------------------------------------------------------

## 2. Inhaltliche Ausgangslage (steht bereits fest -- aus Band 2 gesaet)

Aus `Author_Info.md` (Z. 436-440) und Band-2-Epilog ist der Serienhaken verbindlich:

- **Die zweite Quelle** liegt im **Wald hinter Eichenhain** (zweites X auf der Geheimtinte-Karte).
- **Heinrich Winter** will nach Hause kommen, bittet die Kinder um Hilfe bei der letzten Suche.
- Warnung (zweimal gesetzt): *"Der Wald hat seine eigenen Geheimnisse."* / *"Der Wald ist gross. Und alt."*

**Offene Fragen, die Band 3 beantworten MUSS** (damit die Serie sauber schliesst/weitergeht):
1. Was ist die zweite Quelle?
2. Warum ist Winter WIRKLICH verschwunden -- suchte er sie?
3. Was zeigt die Karte noch, das die Kinder nicht gesehen haben?
4. Kommt Winter nach Hause?

### Festgelegte Konzept-Entscheidungen (geprueft & bestaetigt)

1. **Die zweite Quelle = Gefahr fuers Dorf, Typ Boden/Einsturz.**
   Die zweite Quelle untergraebt langsam den Boden. Der Dorfbrunnen (oder ein
   Gebaeude) droht einzustuerzen. **Kindgerecht:** Sachschaden, KEIN Mensch kommt
   zu Schaden. Erstmals tickt eine Uhr in der GEGENWART (anders als Band 1+2, wo
   die Bedrohung in der Vergangenheit lag). Knuepft physikalisch an Band 2 an
   (Regen = Einsturz), aber neuer Schauplatz Wald.

2. **Winter kehrt im Finale (Akt 4) zurueck.**
   AUFLAGE: Seine Rueckkehr muss kausal noetig sein -- er weiss etwas, das nur er
   weiss (er suchte die Quelle jahrelang), und seine Rueckkehr ist FOLGE der
   Kinder-Leistung (Band-2-Versprechen: "Vielleicht komme ich nach Hause. Wenn
   ihr mir helft." = Bedingung, die Band 3 einloesen muss).

3. **Neue Figur: der alte Waldhueter/Foerster -- Typ "Beschuetzer-Hindernis".**
   Muerrisch, jagt die Kinder zuerst aus dem Wald (aktives Hindernis), weil er
   WEISS, dass der Boden ueber der Quelle einsturzgefaehrdet ist. Schuetzt sie,
   nicht das Geheimnis. Wird dann Verbuendeter. Bewusst KEIN zweiter Frau-Bergmann
   (aktiv statt passiv-schweigender Zeuge). Verzahnt Figur + Gefahr kausal.

4. **5 Baende geplant -> Band 3 saet Hook fuer Band 4: "Groesser werden".**
   Band 3 loest die zweite Quelle + Winters Rueckkehr. Saet dann an: das Geheimnis
   der vier Gruenderfamilien / des Wappens reicht UEBER Eichenhain hinaus. Nutzt
   bestehenden Kanon (Author_Info Z. 442-448, die vier Familien) -- kein Fremdkoerper.

------------------------------------------------------------------------

## 3. Qualitaets-/Konsistenz-Regeln (uebernommen, nicht neu erfunden)

Aus `CLAUDE.md` + `Author_Info.md` + `_Gemeinsam/Schreibstil_Regeln.md`:

- Saetze 8-12 Woerter (max 15), Absaetze 3-5 Zeilen, viel Weissraum
- Dialog mind. 40-50 % pro Kapitel
- 3. Person, nah an Jonas, kein Praeteritum-Passiv
- Konkrete Woerter, Emotionen koerperlich ("Herz klopfte"), nie abstrakt
- **Jedes** Kapitel endet mit Cliffhanger; naechstes Kapitel loest ihn SOFORT auf (kein Zeitsprung)
- Ben: aengstlich+witzig, ABER mind. 1 mutiger/kluger Moment pro Buch (Signature-Move)
- Mila: mutig, darf aber verletzlich sein; Jonas fragt, Mila treibt, Ben bremst
- Kapitellaenge Band 3: **1.200-1.400 Woerter** (wie Band 2, nicht wie Band 1)
- Umfang: **18 Kapitel + 1 Epilog = 19**, jeder Band-2-Hook wird eingeloest

------------------------------------------------------------------------

## 4. Konkrete Arbeitsschritte (Phasen)

### Phase 0 -- Konzept-Entscheidungen -- ERLEDIGT
Die 4 Grundsatz-Entscheidungen sind getroffen und geprueft (siehe Abschnitt 2).
Der Spannungsbogen kann jetzt festgelegt werden.

### Phase 1 -- Continuity erweitern
`Author_Info.md`: neuen Abschnitt **"BAND 3"** anhaengen (analog zu "BAND 2"):
Ausgangslage, evtl. neue Figur(en), Charakter-Entwicklung Band 3, leerer
Kontinuitaets-Tracker (wird beim Schreiben gefuellt), offene Fragen fuer Band 4/Serienende.

### Phase 2 -- Story_Outline.md
`Band_3/Linear/Story_Outline.md`: Zielumfang, 4-Akt-Modell, Ausgangslage,
das zentrale Geheimnis (was die zweite Quelle WIRKLICH ist), neue Figur(en),
**19 Kapitel** mit je 1 Cliffhanger-Satz, Charakter-Entwicklungs-Tabelle, Band-4-Hook.

### Phase 3 -- Detaillierte_Szenenplanung.md
`Band_3/Linear/Detaillierte_Szenenplanung.md`: pro Kapitel **Szene 1-4 + Cliffhanger**.
Hier wird geprueft: Loest Kapitel N+1 den Cliffhanger von Kapitel N sofort auf?

### Phase 4 -- Kapitel schreiben (19 Dateien)
`Band_3/Linear/Kapitel/Die_Herrenhaus_Detektive_Band3_KapitelX.md`.
Reihenfolge 1->19. Nach jedem Kapitel: Continuity-Tracker in `Author_Info.md` updaten.
Commit-Format: `Kapitel X erweitert (~XXXX Woerter)`.

### Phase 5 -- Manuskript kompilieren
`Band_3/Linear/create_manuscript.py` (aus Band 2 kopieren, Titel/Pfade anpassen)
-> erzeugt `Band_3/Linear/Manuskript.docx`.

------------------------------------------------------------------------

## 5. Risiken & Wachpunkte beim Schreiben (aus der Pruefung)

Die Grundsatz-Entscheidungen stehen (Abschnitt 2). Beim Ausarbeiten von Outline
und Kapiteln auf diese vier Fallen achten:

1. **Ton-Falle "Gefahr".** Zielgruppe 8-10, CLAUDE.md: "nie aengstigend". Die
   Einsturzgefahr IMMER als abwendbaren Sachschaden zeigen, nie als Lebensgefahr
   fuer Menschen. Spannung aus dem Wettlauf, nicht aus Bedrohung.

2. **Winter-Rueckkehr muss verdient sein.** Er darf nicht "auch noch" auftauchen.
   Im Finale braucht er eine Funktion, die nur er erfuellt (sein Suchwissen).

3. **Waldhueter != Frau-Bergmann-Klon.** Aktiv (jagt/hilft), nicht passiv
   (schweigt/erinnert). Pruefen: Treibt er die Handlung, oder erzaehlt er nur?

4. **Band-4-Hook nicht ueberladen.** "Groesser werden" ueber das Wappen nur
   ANDEUTEN, nicht aufloesen -- sonst Kanon-Schulden fuer Band 4.

------------------------------------------------------------------------

## 6. Was dieser Plan bewusst NICHT enthaelt
- Cover, Klappentext, KDP-Setup, Keywords, A+ Content
- Interaktiv-Version (Abschnitte/Verzweigungen)
- Illustrationen

Diese folgen -- wie bei Band 1+2 -- erst NACH dem fertigen Linear-Manuskript.
