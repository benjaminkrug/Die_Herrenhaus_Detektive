# Cover-Konzept — Band 2: Das Geheimnis des Brunnens

> Reihen-Look wie Band 1/3/4, **großer Goldtitel** (~35-40 % Höhe) mit
> Sicherheitsrand. KDP-Taschenbuch **6 × 9 Zoll**, 300 dpi, weißes Papier.
> Full-Cover baut `build_cover_band2.py` aus `front_band2.png` + `back_band2.png`.
>
> Gleiche zwei Regeln wie bei Band 1, damit es nicht dieselben Fehler gibt:
> 1. **Front:** Text mit Sicherheitsrand (≥10 % Seiten, ≥7 % oben, ≥6 % unten) —
>    sonst läuft der Titel in den Beschnitt.
> 2. **Back:** Layout-Zonen (Text oben, untere 16 % + Ecke unten rechts frei für
>    den Barcode).

---

## Prompt A — VORDERSEITE (mit Text, großer Titel, Sicherheitsrand)

> Referenzbild anhängen: die **Band-1-Front** (`vorderseite_1.png`) für den
> einheitlichen Reihen-Look, oder das bisherige Band-2-Cover für die
> Brunnen-Komposition. Kinder = dieselben drei.

```
Erzeuge ein fertiges Buch-Vordercover im Hochformat (portrait, Seitenverhaeltnis 2:3), mit dem Titeltext direkt und korrekt im Bild. Halte dich an Stil, Malweise
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
- The UPPER ~42% is calm, darker night sky - room for the title (title inside the
  side margins, not edge to edge).
- The LOWER ~58% holds the scene.

SCENE: night in an old village square with cobblestones and half-timbered houses.
In the centre foreground stands a round old stone WELL, and from inside the well
rises a soft warm-golden glow - the focal point and the mystery. A full moon and
soft clouds in the sky. On a wooded hill in the background stands a large old dark
manor house with a few lit windows. Three 10-year-old children stand close
together with their BACKS to us, leaning over the glowing well, looking down into
it. A black cat sits nearby on a bench.

THE THREE CHILDREN (seen from behind, same kids as the reference cover):
- LEFT - MILA: a girl, dark hair in a ponytail, hoodie.
- CENTER - JONAS: a boy, brown messy hair, a backpack, holding an old map.
- RIGHT - BEN: a boy, a little shorter, wearing a bright RED BASEBALL CAP
  (clearly visible, essential recurring detail), holding a small flashlight.

TEXT ON THE COVER (spell every word EXACTLY, clean warm-gold serif lettering,
high contrast, ALL of it inside the safe margin described above):
- Top, small, letter-spaced caps: DIE HERRENHAUS-DETEKTIVE
- Just below, smaller, with a short dash each side: - BAND 2 -
- The MAIN TITLE, large and dominant but clearly within the side margins, in two
  lines of bold golden letters:
  DAS GEHEIMNIS
  DES BRUNNENS
- Bottom centre, above the bottom margin: Benjamin Krug

The main title should be large - about 35% of the cover height - BUT it must NEVER
be wider than 80% of the cover, and it must keep clear empty space on the left and
right of every line. If in doubt, make the title smaller rather than let it touch
the edges. Spell every word exactly. Do NOT add
any other words, letters or numbers. Do NOT include: monsters, ghosts, skeletons,
scary faces, glowing eyes, blood, modern elements, cars, phones, neon colours,
manga or cartoon style.
```

**Nachfass-Satz, falls der Titel zu breit ist:** *„Der Titel beruehrt noch den
Rand. Mach ihn kleiner und lasse auf beiden Seiten mindestens 10% freien Himmel."*

---

## Prompt B — RÜCKSEITE (mit Text, Layout-Zonen, echte Umlaute)

> Referenzbild anhängen: die neue Band-2-Front (sobald erstellt).
> **Echte Umlaute** — nicht ae/oe/ue (Lehre aus Band 1). 4-6 Varianten, Text
> Wort für Wort prüfen (Rätsel, Rückweg, öffnen, verändert, älter, darüber,
> stürzt).

```
Erzeuge die komplette BUCH-RÜCKSEITE als Hochformat-Bild (portrait, Seitenverhältnis 2:3), mit dem gesamten Text sauber und korrekt im Bild.
Übernimm Kunststil, Farbwelt und Stimmung des angehängten Vordercovers.

ART STYLE: finished professional back cover, semi-realistic richly painted
digital illustration, deep atmospheric dusk, for a German children's
detective-adventure novel age 8-10. Mysterious but warm, NOT scary.

BACKGROUND (dark, calm, simple, so the text is perfectly readable): an old dark
underground tunnel / cavern with rough stone walls, a faint warm-golden glowing
underground spring winding along the floor, a small old treasure chest faintly
visible on a rock ledge to the right. The whole UPPER and CENTRE stays dark and
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
Sie haben den Brunnen geöffnet.
Darunter liegt ein Geheimnis, das älter ist als das Dorf.

BODY (normal, small gaps between the groups):
Drei Wochen nach ihrem ersten Abenteuer öffnen Jonas, Mila und
Ben einen versiegelten Brief von Herrn Winter. Was darin steht,
verändert alles.

Unter dem Dorfbrunnen liegt ein uraltes Gangsystem. Versiegelt
seit 1953. Und eine alte Frau schweigt seit siebzig Jahren darüber.

Doch als die drei tiefer graben, stürzt der Tunnel hinter ihnen ein.
Kein Rückweg. Kein Licht. Und das Wasser steigt.

CLOSING LINE (slightly larger, warm gold): Was hat Lisbeth damals in der
Dunkelheit gesehen?

FOOTER (small): Ein Rätsel-Abenteuer zum Mitraten. Für clevere Kinder ab 8
Jahren.

Spell every German word exactly, including ä, ö, ü. Keep text clear of the
bottom-right corner. Do NOT add extra words. Do NOT include people, monsters,
scary faces, modern elements, neon colours, cartoon style.
```

---

## Technik

- Format **6 × 9 Zoll**, Bleed 0,125", weißes Papier.
- **Seitenzahl noch offen** — echte Zahl aus dem KDP-Previewer holen (Schätzung
  im Skript: 150). `build_cover_band2.py`: `PAGE_COUNT` setzen,
  `PAGE_COUNT_IS_ESTIMATE = False`, dann Wrap bauen.
- Sollmaß hängt von der Seitenzahl ab; bei ~154 S. ≈ 12,597 × 9,250".

## Ablauf

1. Prompt A → neue Front (Ränder + Rechtschreibung prüfen), als `front_band2.png`.
2. Prompt B → neue Rückseite (Umlaute + Barcode-Ecke prüfen), als `back_band2.png`.
3. Echte Seitenzahl aus dem Previewer → `PAGE_COUNT` in `build_cover_band2.py`.
4. Ich baue den Wrap und prüfe Maße + Ränder nach.
