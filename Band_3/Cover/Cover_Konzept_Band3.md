# Cover-Konzept – Band 3: Die zweite Quelle

> Ziel: Cover im einheitlichen Reihen-Look (wie Band 1 & 2), KDP-Taschenbuch **6 × 9 Zoll**, 300 dpi.
> Reihenfolge: Erst **Front-Cover-Illustration** generieren (dieses Dokument).
> Das druckfertige **Full-Cover-PDF** (Vorder- + Rücken + Buchrücken) entsteht ERST nach
> dem Feinschliff – die Buchrücken-Breite hängt von der finalen Seitenzahl ab
> (siehe Abschnitt "KDP-Specs" unten).

---

## 1. Bild-Idee (Motiv)

Band 3 spielt erstmals **im Wald**. Das Cover muss sofort sagen:
*„Diesmal geht es raus aus dem Dorf – in den verbotenen Wald."*

**Kern-Motiv:** Die drei Kinder (Jonas, Mila, Ben) stehen **von hinten** am Rand eines
dunklen, uralten Waldes – wir schauen mit ihnen hinein (genau wie auf dem Band-2-Cover
zum Brunnen). Vor ihnen ein schmaler Pfad zwischen riesigen Stämmen. Tief im Wald
**glimmt geheimnisvoll die zweite Quelle** als warmer Lichtpunkt – der Blickfang.
Stimmung: **Dämmerung**, geheimnisvoll, abenteuerlich, einladend – **nicht gruselig**.
Stil & Farbwelt = **Band-2-Reihen-Look** (siehe `Band_2/Cover/Cover_Buch_2.png`).

**Kanon-Anker (müssen erkennbar sein, konsistent zur Geschichte):**
- **Ben** trägt eine **rote Mütze** (Reihen-Markenzeichen).
- Die drei sind **ca. 10 Jahre alt**, als Team zusammenstehend.
- Es ist **Spätsommer/früher Herbst**: erste gelbe Blätter.
- Ein **altes, schiefes Schild „Betreten verboten"** am Wegrand (Kap. 1–2).
- Optional klein im Hintergrund: ein **Schimmer von Wasser / eine Quelle** zwischen den Bäumen.

---

## 2. Die zwei Cover-Prompts (KDP-ready, Text IM Bild)

> **Du bekommst zwei getrennte Prompts:**
> **2A = Vorderseite** (mit Titel, Serie, „Band 3", Autor im Bild) ·
> **2B = Buchrücken** (mit „3", Titel, Serie, Autor im Bild).
> Beide im Band-2-Reihen-Look (halb-realistisch, Dämmerung, leuchtende Quelle,
> Kinder von hinten).
>
> ⚠️ **Drei Dinge, die du wissen musst, damit es WIRKLICH KDP-tauglich ist:**
> 1. **Auflösung:** ChatGPT liefert max. 1024×1792 px. Für 6×9-DRUCK (300 dpi)
>    brauchst du ~1875×2775 px. → Generiere das Bild, dann **einmal hochskalieren**
>    (z. B. mit dem Skript [`resize_cover_kdp.py`](../../Band_2/Cover/resize_cover_kdp.py)
>    von Band 2). Fürs **E-Book** reicht 1024×1792 direkt.
> 2. **Text-im-Bild ist Glückssache bei DALL·E:** Lange deutsche Wörter werden manchmal
>    falsch geschrieben. → **Generiere 3–4 Varianten** und nimm die mit korrekter Schrift.
>    Prüfe Buchstabe für Buchstabe: „HERRENHAUS-DETEKTIVE", „Die zweite Quelle",
>    „Benjamin Krug".
> 3. **Vorderseite und Buchrücken sind getrennte Bilder** und werden erst beim
>    Full-Cover-PDF zusammengesetzt (nach dem Feinschliff, wenn die Rückenbreite feststeht).

### So gehst du in ChatGPT vor:

1. **Lade das Band-2-Cover als Referenz hoch:** `Band_2/Cover/Cover_Buch_2.png`.
   → für gleichen Stil, gleiche Farbwelt, gleiche drei Kinder.
2. Kopiere **2A** komplett (deutscher Block) in eine Nachricht + das Referenzbild.
3. 3–4 Varianten erzeugen, beste mit korrekter Schrift wählen.
4. Danach dasselbe mit **2B** (Buchrücken).

---

### ▶ 2A — VORDERSEITE (copy-paste, Text ist im Bild)

```
Bitte erzeuge ein fertiges Buch-Vordercover als Hochformat-Bild (portrait, 1024×1792
Pixel), mit Titeltext direkt im Bild. Halte dich exakt an Stil, Farbwelt und die drei
Kinder aus dem angehängten Referenz-Cover (Band 2 dieser Buchreihe) — es sind dieselben
drei Kinder, nur die Szene ändert sich: diesmal am Rand eines verbotenen Waldes.
Verwende diesen Prompt:

Finished front book cover, semi-realistic richly painted digital illustration for a
German children's detective-adventure series, target age 8-10. Same art style, palette
and rendering as the attached reference cover: deep atmospheric colors, soft glow,
cinematic dusk light, one warm glowing light source as the focal point. Warm,
mysterious, adventurous, inviting — NOT scary.

COMPOSITION: portrait orientation, taller than wide. We stand BEHIND the three children
and look with them into the forest. The forest fills the lower two thirds. The UPPER
THIRD is darker calm dusk sky and high treetops, kept simple and uncluttered, with room
for the title text.

SCENE: dusk at the edge of a huge, ancient forest. Three 10-year-old children stand
close together with their backs to us, facing the trees, about to step onto a narrow
earthy path that winds between enormous old oak and beech trunks deeper into the woods.
Deep among the dark trees, a hidden forest spring glows with a soft warm-golden and
silvery-blue light between the trunks — the magical focal point that draws the eye, the
same kind of warm glow as the well in the reference cover. Early autumn: a few yellow
and orange leaves on the branches and on the ground. Long soft shadows, low evening mist.

THE THREE CHILDREN (seen from behind, same kids as the reference cover):
- CENTER — JONAS: a 10-year-old boy, brown slightly messy hair, a backpack on his back.
- LEFT — MILA: a 10-year-old girl with dark hair, athletic, leaning slightly forward.
- RIGHT — BEN: a 10-year-old boy, a little shorter, wearing a bright RED BASEBALL CAP
  (clearly visible — important recurring detail), a backpack on his back, half a step
  behind the others.

At the edge of the path stands an old crooked weathered wooden sign with the faded
German words "Betreten verboten".

TEXT ON THE COVER (spell every word exactly, clean readable serif lettering, well
integrated into the artwork, high contrast so it is readable as a small thumbnail):
- Top, smaller, in one line: "DIE HERRENHAUS-DETEKTIVE"
- Just below it, smaller: "BAND 3"
- Large main title across the upper third, in two lines:
  "Die zweite" / "Quelle"
- Bottom center, smaller: "Benjamin Krug"

Make sure all text is spelled correctly and clearly legible. Do NOT add any other words
or letters. Do NOT include: monsters, ghosts, scary faces, blood, glowing eyes, modern
elements, cars, phones, neon colors, manga or anime style, flat cartoon style.
```

---

### ▶ 2B — BUCHRÜCKEN / SPINE (copy-paste, Text ist im Bild)

> Der Buchrücken ist ein **schmales, hohes** Bild. Endgültige Breite hängt von der
> Seitenzahl ab (siehe Abschnitt 3b) — generiere ihn final erst nach dem Feinschliff.
> Für einen ersten Entwurf reicht der Prompt schon jetzt.

```
Bitte erzeuge das Buchrücken-Bild (book spine) für denselben Band, als sehr schmales,
hohes Hochformat-Bild (tall narrow vertical strip). Halte dich exakt an Stil und
Farbwelt des angehängten Referenz-Covers (Band 2 dieser Buchreihe). Verwende diesen
Prompt:

A tall narrow book spine for a German children's detective-adventure series, same art
style, colors and mood as the attached reference cover: deep atmospheric dusk colors,
soft warm glow. The background is a simple dark forest texture (a few tree trunks, soft
mist, a faint warm glowing light low down) — calm and not too busy, so the text stays
readable. Vertical strip composition.

TEXT ON THE SPINE (spell every word exactly, clean readable serif lettering, high
contrast, all text rotated 90 degrees to read from bottom to top as on a German book
spine):
- Near the TOP: a large number "3"
- In the MIDDLE, the main title: "Die zweite Quelle"
- Right next to it, smaller: "DIE HERRENHAUS-DETEKTIVE"
- Near the BOTTOM, small: "Benjamin Krug"

Keep all text comfortably away from the left and right edges (safe margin). Make sure
every word is spelled correctly and clearly legible. Do NOT add any other words. Do NOT
include: people, faces, monsters, modern elements, neon colors, manga or cartoon style.
```

---

### Nach der Generierung — KDP-fertig machen (kurz)

- **3–4 Varianten** erzeugen, beste mit **korrekt geschriebenem Text** wählen.
- **Vorderseite hochskalieren** auf ~1875×2775 px (6×9 @ 300 dpi) fürs Druck-Taschenbuch;
  fürs E-Book reicht das Originalbild.
- **Figuren passen nicht zu Band 2?** Nachfassen: *„Behalte exakt dieselben drei Kinder
  wie im Referenz-Cover: gleiche Frisuren, gleiche rote Baseball-Cap bei Ben, gleiche
  Rucksäcke. Ändere nur die Szene zum Waldrand."*
- **Text falsch geschrieben?** Nachfassen: *„Der Titel ist falsch geschrieben. Schreibe
  exakt: DIE HERRENHAUS-DETEKTIVE / BAND 3 / Die zweite Quelle / Benjamin Krug."*

---

### ▶ 2C — RÜCKSEITE / BACK COVER — EIN finaler Prompt, alles in einem

> Das ist der **eine** copy-paste-Prompt für die komplette Rückseite (Hintergrund +
> kompletter Klappentext + Barcode-Feld). Vorgehen: Band-2-Cover als Referenz anhängen,
> Block 1:1 einfügen, 4–6 Varianten erzeugen, beste ansehen, dann selbst iterieren.

```
Bitte erzeuge die fertige BUCH-RÜCKSEITE (back cover) als EIN Hochformat-Bild (portrait,
Seitenverhältnis 2:3, 1024×1536 Pixel), mit dem kompletten Text sauber und korrekt direkt
im Bild gerendert. Es ist die Rückseite zum selben Buch wie das angehängte Referenz-Cover
(Band 2 dieser deutschen Kinderbuch-Detektivreihe). Übernimm exakt den Kunststil, die
Farbwelt und die Stimmung des Referenz-Covers. Benutze genau diese Beschreibung:

ART STYLE: a finished professional back cover of a German children's detective-adventure
novel, target age 8-10. Semi-realistic, richly painted digital illustration, identical in
style, palette and rendering to the attached reference cover: deep atmospheric dusk blues
and greens, a dark forest, soft warm-golden glow as a single accent light, cinematic,
mysterious yet warm and inviting — absolutely NOT scary, NOT horror. Portrait orientation,
taller than wide.

BACKGROUND (must stay dark, calm and simple so the text is perfectly readable):
A softly blurred dark forest at dusk seen from a distance. A few tall tree trunks at the
left and right edges frame the cover like a vignette. Low drifting mist near the ground.
Deep in the center-background, far between the trees, a small faint warm-golden glow of a
hidden spring — the same kind of magical glow as on the reference cover. The whole CENTER
of the cover is calm and darkened (like a subtle dark overlay) so that text placed on top
is easy to read. No people, no animals, no objects in the foreground.

TEXT — render every word EXACTLY as written, correctly spelled, in clean readable classic
serif lettering, warm off-white / cream color, high contrast against the dark background,
all lines horizontal and centered, with generous spacing between the blocks. Place the
text in this vertical order from top to bottom:

TOP (small, letter-spaced, all caps):
DIE HERRENHAUS-DETEKTIVE

HEADLINE below it (larger, bold, two short lines):
Niemand geht in den Wald.
Nicht seit langer Zeit.

MAIN BLURB in the middle (normal size, each sentence on its own short line, do NOT merge
into one paragraph, leave a little space between lines):
Doch auf der alten Karte gibt es ein zweites X.
Tief zwischen den Bäumen.
Und am Brunnen zeigt sich ein nasser Riss.

Jonas, Mila und Ben sind sich sicher:
Hier stimmt etwas nicht.

Im Wald wartet eine zweite Quelle.
Eine, die niemand je gefunden hat.
Finden die drei sie nicht rechtzeitig,
versinkt das ganze Dorf im Wasser.

CLOSING LINE (slightly larger, italic):
Das dritte große Abenteuer der Herrenhaus-Detektive.

FOOTER (small):
Spannend, lustig und voller Mut — für alle Spürnasen ab 8 Jahren.

BOTTOM-RIGHT CORNER: leave a clean empty light-grey rectangle, about 4 cm wide and 2 cm
tall, completely free of artwork and text — reserved blank space for the printed barcode.

IMPORTANT: spell every German word exactly as given above, including the umlauts ä, ö, ü
and the dash. Keep all text inside the safe area, away from the outer edges. Do NOT invent
or add any extra words, letters, numbers, logos or signatures. Do NOT include: monsters,
ghosts, scary faces, blood, glowing eyes, modern elements, cars, phones, neon colors,
manga or anime style, flat cartoon style.
```

> **KDP-Hinweis:** Auch die Rückseite fürs Druck-Taschenbuch auf ~1875×2775 px
> (6×9 @ 300 dpi) hochskalieren. Den **vollständigen** Klappentext findest du in
> Abschnitt 4 — er ist v. a. für die **Amazon-Produktbeschreibung** gedacht (dort wird
> er als echter Text eingegeben und ist immer fehlerfrei).

---

## 3. Titel-Typografie (Vorderseite)

Gleiche Hierarchie wie Band 1 & 2:

| Element | Text | Platzierung |
|---|---|---|
| Serientitel (klein, oben) | **DIE HERRENHAUS-DETEKTIVE** | oberer Rand |
| Band-Marker | **BAND 3** | unter Serientitel |
| Haupttitel (groß) | **Die zweite Quelle** | oberes Drittel, über dem Wald |
| Autor (unten) | **Benjamin Krug** | unterer Rand |

- Schrift/Farben **identisch zur Reihe** halten (gleiche Font-Familie wie Band 1/2 Cover).
- Titel gut lesbar als **Thumbnail** (Amazon zeigt das Cover sehr klein!): hoher Kontrast,
  Titel-Text mit dunklem Schimmer/Outline gegen den hellen Himmel im oberen Drittel.

---

## 3b. Buchrücken (Spine)

> Der Buchrücken ist beim **gedruckten** Buch das, was im Regal sichtbar ist – bei einer
> Reihe muss er **exakt wie Band 1 & 2 aufgebaut** sein (gleiche Anordnung, gleiche Fonts,
> gleiche Farbflächen), nur Band-Nummer und Titel ändern sich. Käufer erkennen die Reihe
> am Rücken.

### Aufbau (von oben nach unten), identisch zur Reihe:

| Position | Inhalt | Hinweis |
|---|---|---|
| oben | **3** (Band-Nummer, groß) | gleiche Stelle/Größe wie „1"/„2" bei Band 1/2 |
| Mitte | **Die zweite Quelle** (Haupttitel) | quer gedreht (Leserichtung von unten nach oben) |
| Mitte | **DIE HERRENHAUS-DETEKTIVE** (Serientitel, kleiner) | über oder unter dem Titel, wie Reihe |
| unten | **Benjamin Krug** | Autorenname, klein |

### Gestaltungsregeln (Reihen-Konsistenz):

- **Hintergrundfarbe des Rückens** an Band 1 & 2 anlehnen, aber für Band 3 einen
  **eigenen, klar unterscheidbaren Farbton** wählen (so erkennt man die Reihe als Set,
  aber jeden Band einzeln). Vorschlag passend zum Wald-Motiv: **tiefes Waldgrün** oder
  **dunkles Moosgrün** – falls Band 1 & 2 schon Grün nutzen, stattdessen ein warmes
  **Herbst-Ocker/Braun**. → Vor dem Festlegen kurz die Rücken von Band 1 & 2 vergleichen.
- **Schrift quer** (um 90° gedreht), Leserichtung wie bei deutschen Büchern üblich
  (Kopf nach links / von unten nach oben lesbar) – **genau wie Band 1 & 2**, nicht anders.
- **Sicherheitsabstand**: KDP verlangt min. **0,0625 Zoll (1,6 mm)** Abstand von Text zu
  beiden Rücken-Kanten. Bei schmalem Rücken (siehe Breite unten) Schrift entsprechend klein.
- **Nur wenn der Rücken breit genug ist** (Faustregel KDP: ab ~130 Seiten / ~0,3 Zoll),
  darf Text auf den Rücken. Band 3 hat ~21.000 Wörter → das wird locker erreicht
  (Band 2 hatte 158 Seiten). Trotzdem erst nach finaler Seitenzahl setzen.

### Buchrücken-Breite (rechnerisch)

Die Breite ergibt sich aus der **finalen Seitenzahl** (steht erst nach dem Feinschliff fest):

- Weißes Papier: `Breite [Zoll] = Seitenzahl × 0,002252`
- Cremefarbenes Papier: `Breite [Zoll] = Seitenzahl × 0,0025`

Beispiel (zur Orientierung, wie Band 2 mit 158 Seiten, weißes Papier):
`158 × 0,002252 = 0,356 Zoll ≈ 9,0 mm` Rücken.

→ Sobald die echte Seitenzahl feststeht, in dieses Dokument eintragen und den Rücken
darauf auslegen. Das Skript [`resize_cover_kdp.py`](../../Band_2/Cover/resize_cover_kdp.py)
berechnet die Rückenbreite bereits automatisch aus `PAGE_COUNT`.

---

## 4. Rückseiten-Text (Klappentext)

> Kurz, spannend, mit offener Frage am Ende. Für 8–10-Jährige + kaufende Eltern.

```
Niemand geht in den Wald.
Nicht seit langer, langer Zeit.

Aber auf der alten Karte gibt es ein zweites X — tief zwischen den Bäumen.
Und am Brunnen im Dorf zeigt sich ein nasser Riss, der nicht von selbst kommt.

Jonas, Mila und Ben sind sich sicher: Hier stimmt etwas nicht.
Im Wald wartet eine zweite Quelle. Eine, die niemand je gefunden hat.
Und wenn die Kinder sie nicht rechtzeitig bändigen, droht das ganze Dorf
im Wasser zu versinken.

Doch der Wald hat seine eigenen Geheimnisse.
Einen mürrischen Förster, der jeden wegjagt.
Einen Boden, der unter den Füßen nachgibt.
Und einen alten Mann, der endlich nach Hause kommen will …

Das dritte große Abenteuer der Herrenhaus-Detektive.

Spannend, lustig und voller Mut — für alle Spürnasen ab 8 Jahren.
```

**Optionale Zusatz-Zeile unten (Reihen-Hinweis):**
*„Jeder Band ist in sich abgeschlossen und kann einzeln gelesen werden."*

---

## 5. KDP-Specs (für das spätere Full-Cover-PDF)

Format wie Band 2: **6 × 9 Zoll**, **300 dpi**, Beschnitt **0,125 Zoll** rundherum.

- Vorderseite + Buchrücken + Rückseite in **einer** Datei (Full-Cover).
- **Buchrücken-Breite** = Seitenzahl × Faktor:
  - Weißes Papier: `Seitenzahl × 0,002252 Zoll`
  - Cremefarbenes Papier: `Seitenzahl × 0,0025 Zoll`
- **Die Seitenzahl steht erst nach dem Feinschliff fest** → Buchrücken erst dann final.
- Das Band-2-Skript [`resize_cover_kdp.py`](../../Band_2/Cover/resize_cover_kdp.py)
  kann 1:1 für Band 3 übernommen werden – nur `INPUT_PDF`, `OUTPUT_PDF` und
  `PAGE_COUNT` (finale Seitenzahl laut KDP-Vorschau) anpassen.

**Gesamtbreite (px)** = (6 + 0,125 + Buchrücken + 6 + 0,125) × 300
**Gesamthöhe (px)** = (9 + 0,125 + 0,125) × 300 = **2738 px**

---

## 6. Nächste Schritte

1. **Front-Cover-Illustration** mit dem Prompt aus Abschnitt 2 generieren
   (mehrere Varianten; Band-2-Cover als Stil-Referenz anhängen).
2. Beste Variante wählen → Titel-Typografie (Abschnitt 3) daraufsetzen.
3. **E-Book-Cover** (nur Vorderseite) exportieren.
4. Nach dem **Feinschliff** + finaler Seitenzahl: Full-Cover-PDF bauen
   (Rückseiten-Text aus Abschnitt 4 + Buchrücken aus Abschnitt 3b) und mit
   `resize_cover_kdp.py` auf KDP-Maße bringen.
