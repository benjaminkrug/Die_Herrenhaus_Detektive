# Cover-Konzept — Band 1: Das verbotene Herrenhaus

> Reihen-Look wie Band 3/4, aber **großer Goldtitel** (~35-40 % Höhe, Band-1-
> Identität). KDP-Taschenbuch **5 × 8 Zoll**, 300 dpi, weißes Papier.
> Full-Cover baut `build_cover_band1.py` aus `front_band1.png` + `back_band1.png`.

---

## Wichtig: Sicherheitsrand (der Grund für die Prompt-Korrektur)

Die erste Front hatte den großen Titel **bis an den rechten Rand** laufen — im
KDP-Previewer kreuzte „HERRENHAUS" die rote Sicherheitslinie. Beim Druck wird
außen beschnitten; Text im Randbereich wird angeschnitten. **Alle Texte müssen
mit klarem Abstand innerhalb der Ränder sitzen** (Seiten, oben, unten). Die
Illustration darf bis zum Rand laufen, nur der Text nicht.

Konkrete Freiränder (im generierten Bild): **≥10 % links/rechts, ≥7 % oben,
≥6 % unten.**

---

## Prompt A — VORDERSEITE (mit Text, großer Titel, KORRIGIERTE Ränder) ★

> Referenzbild anhängen: die bisherige Band-1-Front `vorderseite_1.png`
> (für Stil, Kinder und den Gold-Titel-Look).

```
Erzeuge ein fertiges Buch-Vordercover im Hochformat (portrait, Seitenverhaeltnis
5:8), mit dem Titeltext direkt und korrekt im Bild. Halte dich an Stil, Malweise
und Farbwelt des angehaengten Referenz-Covers (die bisherige Band-1-Front) -
dieselben drei Kinder, dieselbe atmosphaerische Daemmerung, derselbe goldene
Titel-Look.

SAFE MARGINS (CRITICAL - the outer edges get trimmed when the book is printed):
- Keep ALL text - the series line, the band number, the main title and the
  author name - inside a central safe area. Leave a clear empty margin on EVERY
  side: at least 10% of the width free on the LEFT and RIGHT edges, at least 7%
  of the height free at the TOP, at least 6% at the BOTTOM.
- NO letter may touch or reach an outer edge. The big title must NOT run edge to
  edge - leave clear dark sky on BOTH sides of every title line.
- The illustration (sky, manor, gate, children) still fills the whole image to
  the edges; only the TEXT must stay inside the safe margin.

Semi-realistic, richly painted digital illustration for a German children's
detective-adventure series, target age 8-10. Deep atmospheric dusk, cinematic,
mysterious but warm and inviting - NOT scary, NOT horror.

COMPOSITION (portrait, taller than wide):
- The UPPER ~42% is calm, darker dusk sky - room for the title (but the title
  stays inside the side margins, not edge to edge).
- The LOWER ~58% holds the scene.

SCENE: dusk at the edge of an old forbidden manor estate. On a low hill stands a
large old dark manor house (Herrenhaus) with many dark windows - and exactly ONE
window glowing warm golden, the focal point and the mystery. A crescent moon and
soft clouds in the sky. In the foreground an old wrought-iron gate stands half
open; on the right gate post hangs a weathered wooden sign with the German words
"Betreten verboten". Three 10-year-old children stand close together with their
BACKS to us, just inside the gate, looking up at the manor. A soft flashlight
beam and faint footprints lead from the children toward the house.

THE THREE CHILDREN (seen from behind, same kids as the reference cover):
- LEFT - MILA: a girl, dark hair in a ponytail, hoodie.
- CENTER - JONAS: a boy, brown messy hair, a backpack.
- RIGHT - BEN: a boy, a little shorter, wearing a bright RED BASEBALL CAP
  (clearly visible, essential recurring detail), pointing toward the sign.

TEXT ON THE COVER (spell every word EXACTLY, clean warm-gold serif lettering,
high contrast, ALL of it inside the safe margin described above):
- Top, small, letter-spaced caps: DIE HERRENHAUS-DETEKTIVE
- Just below, smaller, with a short dash each side: - BAND 1 -
- The MAIN TITLE, large and dominant but clearly within the side margins, in two
  lines of bold golden letters:
  DAS VERBOTENE
  HERRENHAUS
- Bottom centre, above the bottom margin: Benjamin Krug

The main title should be large - about 35 to 40% of the cover height - BUT it must
keep clear space to the left and right edges. If in doubt, make the title a little
smaller rather than let it touch the edges. Spell every word exactly. Do NOT add
any other words, letters or numbers. Do NOT include: monsters, ghosts, skeletons,
scary faces, glowing eyes, blood, modern elements, cars, phones, neon colours,
manga or cartoon style.
```

**Nachfass-Satz, falls der Titel immer noch zu breit ist:**
*„Der Titel beruehrt noch den rechten Rand. Mach den Titel kleiner und lasse auf
beiden Seiten deutlich mehr freien Himmel - mindestens 10% Abstand zu jeder
Seitenkante."*

---

## Prompt B — RÜCKSEITE (mit Text) — bereits gelöst

> Die aktuelle `rueckseite_1.png` sitzt korrekt (Text innerhalb der Ränder,
> Barcode-Ecke frei, echte Umlaute, Rechtschreibung geprüft). **Kein Neubau
> nötig.** Der verwendete Prompt steht analog zu Band 4 Prompt B2 mit dem Block
> „LAYOUT AND SAFE ZONES" (Text im oberen 78 %, untere 16 % frei, Ecke unten
> rechts frei für den Barcode).

Klappentext (fertig, korrekt): Headline „Das Haus auf dem Hügel ist verboten. /
Niemand darf dort hin. / Aber nachts brennt Licht hinter den Fenstern." + drei
Absätze + goldene Schlusszeile „Wer steckt dahinter? Und was versteckt sich im
Keller?" + Footer „Ein Detektiv-Abenteuer zum Mitraten. Für clevere Kinder ab 8
Jahren."

---

## Technik

- Format **5 × 8 Zoll**, Bleed 0,125", weißes Papier.
- **Echte Seitenzahl: 191** (aus KDP-Previewer). Rücken = 191 × 0,002252 =
  **0,430" = 10,9 mm**. Full-Cover-Sollmaß **10,680 × 8,250" = 3204 × 2475 px**.
- `build_cover_band1.py`: `PAGE_COUNT = 191`, `PAGE_COUNT_IS_ESTIMATE = False`.
- **Wenn sich der Textumfang ändert**, ändert sich die Seitenzahl → `PAGE_COUNT`
  neu setzen und Wrap neu bauen, sonst KDP-Fehler „erwartete Covergröße …".

## Ablauf für die Front-Korrektur

1. Prompt A (oben) → neue Front mit Rändern, 4-6 Varianten.
2. Prüfen: Titel **berührt keine Kante**, Rechtschreibung, rote Kappe sichtbar.
3. Als `vorderseite_1.png` (oder `_2`) ablegen → ich kopiere sie auf
   `front_band1.png` und baue den Wrap neu.
