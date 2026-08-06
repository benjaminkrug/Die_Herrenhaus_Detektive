# ChatGPT Rückseiten-Prompt — Band 2 INTERAKTIV
## „Das Geheimnis des Brunnens – Dein Fall, Du entscheidest!"

> **Basiert 1:1 auf dem erprobten Band-3-Rückseiten-Rezept** (`Band_3/Cover/Cover_Konzept_Band3.md`,
> Abschnitt 2C) — das Muster, das die schöne Band-3-Rückseite erzeugt hat: **vollflächiges
> dunkles Hintergrundbild, Text vollflächig darüber** (NICHT Bild unten / Text oben getrennt).
>
> **Der Trick, warum es funktioniert:** Prompt-Rahmen auf Englisch (DALL·E versteht das besser),
> aber der eigentliche TEXT bleibt deutsch und wird exakt vorgegeben. Ein „subtle dark overlay"
> in der Bildmitte hält den Text überall lesbar. Jeder Satz auf eigener Zeile = sauberes Layout.
>
> **Vorgehen in ChatGPT:**
> 1. Band-2-Vordercover als **Stil-Referenz anhängen** (`Band_2/Cover/Cover_Buch_2.png`).
> 2. Prompt unten 1:1 einfügen.
> 3. **4–6 Varianten** erzeugen, beste mit korrekt geschriebenem Text wählen.
> 4. Text Wort für Wort prüfen (Umlaute!).

---

## PROMPT (kopieren — Band-2-Vordercover als Referenz anhängen):

```
Bitte erzeuge die fertige BUCH-RÜCKSEITE (back cover) als EIN Hochformat-Bild (portrait,
Seitenverhältnis 5:8), mit dem kompletten Text sauber und korrekt direkt im Bild gerendert.
Es ist die Rückseite zum selben Buch wie das angehängte Referenz-Cover (Band 2 dieser
deutschen Kinderbuch-Detektivreihe). Übernimm exakt den Kunststil, die Farbwelt und die
Stimmung des Referenz-Covers. Benutze genau diese Beschreibung:

ART STYLE: a finished professional back cover of a German children's detective-adventure
novel, target age 8-10. Semi-realistic, richly painted digital illustration, identical in
style, palette and rendering to the attached reference cover: deep atmospheric night blues,
a cobblestone village square, a soft warm-golden glow as a single accent light, cinematic,
mysterious yet warm and inviting — absolutely NOT scary, NOT horror. Portrait orientation,
taller than wide.

BACKGROUND (must stay dark, calm and simple so the text is perfectly readable):
A softly blurred dark village square at night seen from a distance. The old round stone
well sits low in the center-background, glowing faintly warm-golden — the same magical glow
as on the reference cover. Half-timbered houses with warm lit windows and, on a hill far
behind, the dark manor house under a full moon, all softly blurred. Low drifting mist. The
whole CENTER of the cover is calm and darkened (like a subtle dark overlay) so that text
placed on top is easy to read. No people, no animals, no objects in the foreground.

TEXT — render every word EXACTLY as written, correctly spelled, in clean readable classic
serif lettering, warm off-white / cream color, high contrast against the dark background,
all lines horizontal and centered, with generous spacing between the blocks. Place the text
in this vertical order from top to bottom:

TOP (small, letter-spaced, all caps):
DIE HERRENHAUS-DETEKTIVE

HEADLINE below it (larger, bold, two short lines):
Manche Geheimnisse
liegen tiefer, als man denkt.

MAIN BLURB in the middle (normal size, each sentence on its own short line, do NOT merge
into one paragraph, leave a little space between lines):
Unter dem alten Brunnen von Eichenhain
liegt ein vergessenes Gangsystem.
Seit 1953 versiegelt.

Jonas, Mila und Ben wollen wissen,
was dort unten verborgen ist.

Und diesmal entscheidest DU,
welchen Weg die drei nehmen.
Vier Wege. Achtzehn Enden.
Jede Entscheidung zählt.

CLOSING LINE (slightly larger, italic):
Dein Fall — du entscheidest!

FOOTER (small, two short lines):
Interaktiver Detektiv-Krimi ab 8 Jahren.
Kurze Kapitel, große Spannung.

BOTTOM-RIGHT CORNER: leave a clean empty light-grey rectangle, about 4 cm wide and 2 cm
tall, completely free of artwork and text — reserved blank space for the printed barcode.

IMPORTANT: spell every German word exactly as given above, including the umlauts ä, ö, ü
and the dash. Keep all text inside the safe area, away from the outer edges. Do NOT invent
or add any extra words, letters, numbers, logos or signatures. Do NOT include: people,
monsters, ghosts, scary faces, blood, glowing eyes, modern elements, cars, phones, neon
colors, manga or anime style, flat cartoon style.
```

---

## Checkliste nach der Generierung
- [ ] JEDES deutsche Wort korrekt? Besonders: „Geheimnisse", „Eichenhain", „Gangsystem",
      „versiegelt", „entscheidest", „zählt". → sonst nachfassen (siehe unten).
- [ ] Hintergrund dunkel & ruhig, Text überall gut lesbar (cremeweiß auf dunkel)?
- [ ] Stil passt zur Vorderseite / Reihe (gleiche Farbwelt, Brunnen-Glühen)?
- [ ] KEINE Kinder / keine Figuren im Vordergrund (die gehören auf die Front)?
- [ ] Unten rechts das freie graue Barcode-Rechteck vorhanden?

## Nachfass-Prompt, falls Text falsch (an ChatGPT):
> „Der Text ist an einer Stelle falsch geschrieben. Behalte Bild und Layout exakt bei und
> schreibe den Text exakt so, mit korrekten Umlauten: [betroffene Zeile korrekt eintippen].
> Keine anderen Wörter oder Zahlen im Bild."

---

## KDP-technisch
- Rückseite wird Teil des **Full-Cover-PDFs** (Rückseite + Buchrücken + Vorderseite in einem),
  **5×8 Zoll, 300 dpi** (⚠️ NICHT 6×9 — Interaktiv ist 5×8).
- ChatGPT liefert max. ~1024×1638 px (5:8). Für Druck auf ~1500×2400 px hochskalieren.
- Buchrücken-Breite = finale Seitenzahl × 0,0025 Zoll (cremefarben) bzw. × 0,002252 (weiß) —
  erst nach dem Interior-Upload bei KDP ablesbar.
- Der **vollständige** Amazon-Klappentext (länger, für die Produktseite) steht separat in
  `Band_2/Publishing/Buchbeschreibung_Band2_Interaktiv_KDP.html` — dort als echter Text
  eingegeben und immer fehlerfrei.
```
