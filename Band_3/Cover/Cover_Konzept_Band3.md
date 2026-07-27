# Cover-Konzept — Band 3: Die zweite Quelle (Neufassung, großer Titel)

> Reihen-Look wie Band 1/2/4, **großer Goldtitel** (~35 % Höhe) mit
> Sicherheitsrand. KDP-Taschenbuch **6 × 9 Zoll**, 300 dpi, weißes Papier.
> Full-Cover baut `build_cover_band3.py` aus `front_band3.png` + `back_band3.png`.
>
> *(Die alte Fassung dieses Dokuments — ChatGPT-Prompts, 6×9-Einschritt — steht in
> der Git-Historie. Neu: getrennte Panels + Build-Skript + großer Titel wie
> Band 1/2, weil das Cover jetzt ins vereinheitlichte Format soll.)*
>
> Motiv bleibt das bewährte Band-3-Bild (Waldrand, leuchtende Quelle) — nur im
> 2:3-Format mit großem Titel und geprüften Rändern.

---

## Prompt A — VORDERSEITE (mit Text, großer Titel, Sicherheitsrand)

> Referenzbild anhängen: die **bisherige Band-3-Front** (Waldrand-Motiv) oder eine
> andere Reihen-Front. Kinder = dieselben drei.

```
Erzeuge ein fertiges Buch-Vordercover im Hochformat (portrait, Seitenverhaeltnis
2:3), mit dem Titeltext direkt und korrekt im Bild. Halte dich an Stil, Malweise
und Farbwelt des angehaengten Referenz-Covers (dieselbe Reihe) - dieselben drei
Kinder, dieselbe atmosphaerische Daemmerung, derselbe goldene Titel-Look.

SAFE MARGINS (CRITICAL - the outer edges get trimmed when the book is printed):
- The WHOLE title must fit inside the central 80% of the width. There MUST be
  clearly visible empty background - at least the width of two big letters -
  to the LEFT of the leftmost letter AND to the RIGHT of the rightmost letter of
  every single title line. The title NEVER touches or approaches the side edges.
- Keep ALL other text too - series line, band number, author - inside the same
  central safe area: at least 10% of the width free on the LEFT and RIGHT, at
  least 7% of the height free at the TOP, at least 6% at the BOTTOM.
- NO letter of any text may touch or reach an outer edge.
- Better a slightly smaller title with clear margins than a big title that
  touches the edge. When in doubt, shrink the title.
- The illustration still fills the whole image to the edges; only the TEXT stays
  inside the safe margin.

Semi-realistic, richly painted digital illustration for a German children's
detective-adventure series, target age 8-10. Deep atmospheric dusk, cinematic,
mysterious but warm and inviting - NOT scary, NOT horror.

COMPOSITION (portrait, taller than wide):
- The UPPER ~40% is calm, darker dusk sky and high treetops - room for the title
  (title inside the side margins, not edge to edge).
- The LOWER ~60% holds the scene.

SCENE: dusk at the edge of a huge, ancient dark forest. Three 10-year-old
children stand close together with their BACKS to us, at the start of a narrow
earthy path that winds between enormous old oak and beech trunks deeper into the
woods. Deep among the dark trees, a hidden forest spring glows with a soft
warm-golden and silvery-blue light between the trunks - the magical focal point
that draws the eye. Early autumn: a few yellow and orange leaves on the branches
and on the ground. Low evening mist, long soft shadows. At the edge of the path
stands an old crooked weathered wooden sign with the German words
"Betreten verboten".

THE THREE CHILDREN (seen from behind, same kids as the reference cover):
- LEFT - MILA: a girl, dark hair in a ponytail, hoodie.
- CENTER - JONAS: a boy, brown messy hair, a backpack.
- RIGHT - BEN: a boy, a little shorter, wearing a bright RED BASEBALL CAP
  (clearly visible, essential recurring detail), a backpack, half a step behind.

TEXT ON THE COVER (spell every word EXACTLY, clean warm-gold serif lettering,
high contrast, ALL of it inside the safe margin described above):
- Top, small, letter-spaced caps: DIE HERRENHAUS-DETEKTIVE
- Just below, smaller, with a short dash each side: - BAND 3 -
- The MAIN TITLE, large and dominant but clearly within the side margins, in two
  lines of bold golden letters:
  DIE ZWEITE
  QUELLE
- Bottom centre, above the bottom margin: Benjamin Krug

The main title should be large - about 35% of the cover height - BUT it must NEVER
be wider than 80% of the cover, and it must keep clear empty space on the left and
right of every line. If in doubt, make the title smaller rather than let it touch
the edges. Spell every word exactly. Do NOT add any other words, letters or
numbers. Do NOT include: monsters, ghosts, skeletons, scary faces, glowing eyes,
blood, modern elements, cars, phones, neon colours, manga or cartoon style.
```

**Nachfass-Satz, falls der Titel zu breit ist:** *„Der Titel beruehrt noch den
Rand. Mach ihn kleiner und lasse auf beiden Seiten mindestens 10% freien Himmel."*

---

## Prompt B — RÜCKSEITE (mit Text, Layout-Zonen, echte Umlaute)

> Referenzbild anhängen: die neue Band-3-Front (sobald erstellt).
> **Echte Umlaute** — nicht ae/oe/ue. 4-6 Varianten, Text Wort für Wort prüfen
> (Wald, Bäumen, mürrischer Förster, bändigen, Rätsel, Für).

```
Erzeuge die komplette BUCH-RÜCKSEITE als Hochformat-Bild (portrait,
Seitenverhältnis 2:3), mit dem gesamten Text sauber und korrekt im Bild.
Übernimm Kunststil, Farbwelt und Stimmung des angehängten Vordercovers.

ART STYLE: finished professional back cover, semi-realistic richly painted
digital illustration, deep atmospheric dusk, for a German children's
detective-adventure novel age 8-10. Mysterious but warm, NOT scary.

BACKGROUND (dark, calm, simple, so the text is perfectly readable): a softly
blurred dark ancient forest at dusk seen from a distance, a few tall tree trunks
at the left and right edges framing the image like a vignette, low drifting mist
near the ground, and deep in the centre-background a small faint warm-golden glow
of a hidden spring between the trees. The whole UPPER and CENTRE stays dark and
calm so the text is easy to read.

LAYOUT AND SAFE ZONES (CRITICAL - the printed barcode goes bottom-right):
- Keep ALL text within the UPPER 78% of the height. The BOTTOM 16% stays empty.
- The BOTTOM-RIGHT CORNER (right 40% x bottom 20%) must be clean empty
  background, NO text - a barcode will be printed there.
- Keep every line at least 6% away from the edges.

TEXT - render every word EXACTLY, correctly spelled, INCLUDING the German umlauts
ä, ö, ü. Warm cream / off-white serif, centred, top to bottom:

TOP (small, letter-spaced caps): DIE HERRENHAUS-DETEKTIVE

HEADLINE (larger, bold, two short lines):
Niemand geht in den Wald.
Nicht seit langer Zeit.

BODY (normal, small gaps between the groups):
Doch auf der alten Karte gibt es ein zweites X, tief zwischen den
Bäumen. Und am Brunnen zeigt sich ein nasser Riss.

Jonas, Mila und Ben sind sich sicher: Hier stimmt etwas nicht.

Im Wald wartet eine zweite Quelle, die niemand je gefunden hat.
Finden die drei sie nicht rechtzeitig, versinkt das ganze Dorf.

CLOSING LINE (slightly larger, warm gold): Was verbirgt der Wald seit
Jahrhunderten?

FOOTER (small): Ein Detektiv-Abenteuer zum Mitraten. Für clevere Kinder ab 8
Jahren.

Spell every German word exactly, including ä, ö, ü. Keep text clear of the
bottom-right corner. Do NOT add extra words. Do NOT include people, monsters,
scary faces, modern elements, neon colours, cartoon style.
```

---

## Technik

- Format **6 × 9 Zoll**, Bleed 0,125", weißes Papier. Panels im Verhältnis **2:3**.
- **Seitenzahl noch offen** — echte Zahl aus dem KDP-Previewer (Schätzung im
  Skript: 150). `build_cover_band3.py`: `PAGE_COUNT` setzen,
  `PAGE_COUNT_IS_ESTIMATE = False`, dann Wrap bauen.
- Sollmaß hängt von der Seitenzahl ab.

## Vollständiger Klappentext für die Amazon-Produktseite

```
Niemand geht in den Wald. Nicht seit langer, langer Zeit.

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
Jeder Band ist in sich abgeschlossen und kann einzeln gelesen werden.

Spannend, lustig und voller Mut — für alle Spürnasen ab 8 Jahren.
```

## Ablauf

1. Prompt A → neue Front (Ränder + Rechtschreibung prüfen), als `front_band3.png`.
2. Prompt B → neue Rückseite (Umlaute + Barcode-Ecke prüfen), als `back_band3.png`.
3. Echte Seitenzahl aus dem Previewer → `PAGE_COUNT` in `build_cover_band3.py`.
4. Ich baue den Wrap und prüfe Maße + Ränder nach.
