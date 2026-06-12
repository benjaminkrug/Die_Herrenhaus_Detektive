# Illustrationen Band 2 Interaktiv — Prompts fuer ChatGPT (DALL-E)

---

## Die 15 Illustrationen — Uebersicht

| Nr. | Szene | Abschnitt | Typ |
|-----|-------|-----------|-----|
| 1 | Karte: Eichenhain mit Gangsystem | Einband/erste Seite | Karte |
| 2 | Der Brief am Brunnen | Ab. 1 | Establishing Shot |
| 3 | Die Geheimtinte | Ab. 3 | Entdeckung/Magie |
| 4 | Vier Wege — der Entscheidungspunkt | Ab. 7 | Entscheidungspunkt |
| 5 | Die Metalltuer mit den vier Symbolen | Ab. 11 | Detail/Close-up |
| 6 | Der goldene Knopf leuchtet | Ab. 12 | Schluesselmechanik |
| 7 | Hinab in die Dunkelheit | Ab. 17 | Atmosphaere |
| 8 | Die Brunnen-Kammer | Ab. 25b | Cluster A Hoehepunkt |
| 9 | Der unterirdische Wasserfall | Ab. 46 | Cluster B Hoehepunkt |
| 10 | Die Wandmalereien und die Truhe | Ab. 47 | Cluster B Entdeckung |
| 11 | Frau Bergmann und die Initialen | Ab. 79b | Cluster C Hoehepunkt |
| 12 | Die Truhe oeffnet sich | Ab. 80/81 | Cluster C Schatz |
| 13 | Winters Stimme | Ab. 93 | Cluster D Hoehepunkt |
| 14 | Der Brunnen fliesst | Ab. 56/84/200 | Aufloesung |
| 15 | Winters Rueckkehr | Ab. 200 | Geheim-Ende |

## ILLUSTRATION_MAP (fuer create_manuscript_interaktiv.py)

```python
ILLUSTRATION_MAP = {
    "1": [2],          # Ab. 1 (Start) → Illustration 2 (Brief am Brunnen)
    "3": [3],          # Ab. 3 → Illustration 3 (Geheimtinte)
    "7": [4],          # Ab. 7 (Entscheidungspunkt) → Illustration 4
    "11": [5],         # Ab. 11 (Metalltuer) → Illustration 5
    "12": [6],         # Ab. 12 (Knopf leuchtet) → Illustration 6
    "17": [7],         # Ab. 17 (Hinab) → Illustration 7
    "25b": [8],        # Ab. 25b (Brunnen-Kammer) → Illustration 8
    "46": [9],         # Ab. 46 (Wasserfall) → Illustration 9
    "47": [10],        # Ab. 47 (Wandmalereien) → Illustration 10
    "79b": [11],       # Ab. 79b (Initialen) → Illustration 11
    "80": [12],        # Ab. 80 (Truhe) → Illustration 12
    "93": [13],        # Ab. 93 (Winters Anruf) → Illustration 13
    "56": [14],        # Ab. 56 (Brunnen fliesst) → Illustration 14
    "200": [15],       # Ab. 200 (Geheim-Ende) → Illustration 15
}
```

Illustration 1 (Karte) wird als eigene Seite VOR allen Abschnitten platziert.

---

## Stil-Vorgabe (bei JEDEM Prompt voranstellen)

> **Stil-Prefix (immer zuerst einfuegen):**
> "Black and white pen-and-ink illustration for a German children's detective book, target age 8-10. Style: detailed crosshatching, atmospheric shadows, slightly spooky but not scary. Similar to classic 'Die drei Fragezeichen' or 'Emil und die Detektive' interior illustrations. No color. No manga. No cartoon. Realistic proportions for children aged 10. Consistent art style across all illustrations."

---

## Illustration 1: Karte — Eichenhain mit Gangsystem

**Wo im Buch:** Innenseite des Einbands oder erste Seite

**Prompt:**
```
[Stil-Prefix einfuegen]

A hand-drawn cross-section map showing the village of "Eichenhain" ABOVE GROUND and an ancient tunnel system BELOW GROUND. The map should look old and hand-drawn, like a treasure map, with worn parchment texture. The cross-section creates a split view: the top half shows the village, the bottom half shows underground passages.

ABOVE GROUND (top half):
- Center: "Marktplatz" with a circular stone fountain ("Brunnen") and a massive 300-year-old oak tree ("Die alte Eiche"). The fountain is DRY — no water flows
- North of the square: A small shop labeled "Meiers Laden"
- East: "Rathaus" (town hall)
- South: A narrow house labeled "Jonas' Haus"
- West: A church labeled "Kirche", nearby a small house with flower boxes labeled "Frau Bergmanns Haus"
- Northeast on a hill: A large manor house labeled "Das Herrenhaus" — now with scaffolding and workers on the facade (renovation in progress)
- Northwest at forest edge: A half-collapsed old mill labeled "Alte Muehle" next to a stream
- A dense forest on the western horizon, labeled "Der Wald" with a small question mark

BELOW GROUND (bottom half, shown in cutaway):
- A network of hand-carved stone tunnels connecting beneath the village
- The tunnels radiate from a central round chamber directly beneath the Brunnen, labeled "Brunnen-Kammer"
- In the Brunnen-Kammer: a small spring symbol (water drops) and four tiny shield symbols in a circle
- One tunnel leads northeast to beneath the Herrenhaus
- One tunnel leads northwest to beneath the Alte Muehle
- A heavy metal door symbol (four horizontal lines + star) marks the entrance from the Herrenhaus tunnel
- Dotted lines show unexplored or collapsed passages
- A second "X" mark in the forest area, labeled "???" with an arrow pointing off the map

DECORATIVE ELEMENTS:
- A compass rose in the top-right corner
- Title at the top in decorative handwriting: "EICHENHAIN — Ueber und unter der Erde"
- Four small shield emblems in the bottom corners: Star (Winter), Tree (Meier), Cross (Bergmann), Ring (Hoffmann)
- The underground section should be darker, with crosshatching suggesting earth and rock
- Small arrows in the tunnels suggesting direction of water flow

Do NOT include: modern buildings, cars, highways, bright colors, any text other than the German labels specified, 3D rendering effects.
```

---

## Illustration 2: Der Brief am Brunnen

**Wo im Buch:** Beginn der Geschichte (bei Abschnitt 1)

**Prompt:**
```
[Stil-Prefix einfuegen]

Three children at an old stone fountain in a small German village square. Bright midday sunshine. The fountain is DRY — no water, just old mossy stone. A massive old oak tree provides dappled shade overhead.

JONAS (center): A 10-year-old boy sitting on the edge of the fountain wall. Brown medium-length slightly messy hair, t-shirt and jeans, backpack beside him. He holds a heavy paper envelope in both hands, staring at it with wide eyes and slightly open mouth. On the envelope: a clearly visible RED WAX SEAL (show through heavy crosshatching density to make it stand out in B/W). The seal shows a star symbol pressed into the wax.

MILA (left): A 10-year-old girl with a long thick braid over one shoulder. She is leaning forward eagerly, one hand reaching toward the envelope, the other hand on Jonas' shoulder. Her face shows intense curiosity and impatience — eyebrows up, eyes locked on the seal. Athletic build, sneakers with distinctive laces.

BEN (right): A 10-year-old boy, slightly shorter, wearing a RED BASEBALL CAP (shown through distinctive crosshatching). He sits on the fountain edge slightly further back, eating something (crumbs on his shirt). He leans in to look at the envelope but his expression mixes curiosity with skepticism — one eyebrow raised, mouth full.

BACKGROUND:
- The manor house ("Herrenhaus") visible on a hill behind them, now with SCAFFOLDING on the facade and WORKERS carrying boards — it is being renovated
- Small village houses with flower boxes lining the square
- The village looks peaceful and sunlit
- The fountain stone is weathered, with moss in the cracks, but clearly no water has flowed here in decades

The scene captures the OPENING MOMENT — a mysterious letter has arrived, three weeks after their first adventure. Everything begins again at the well.

Do NOT include: water in the fountain, modern cars, other children, adults in the foreground, dark/scary atmosphere. The mood is bright curiosity, not fear.
```

---

## Illustration 3: Die Geheimtinte

**Wo im Buch:** Abschnitt 3 — Die Entdeckung der versteckten Karte

**Prompt:**
```
[Stil-Prefix einfuegen]

Three children in a small bedroom, gathered around a desk. A candle burns on the desk — the ONLY light source. The room is Jonas' bedroom: simple, with some unpacked moving boxes still against the wall. Evening/night — the window shows darkness outside.

BEN (center of action): A 10-year-old boy with a red baseball cap (cap sitting crooked on his head). He holds a yellowed sheet of paper carefully over the candle flame with BOTH HANDS. His hands are perfectly steady — no trembling. His expression is one of rare confidence and concentration. He is in his element. The paper is held at a careful distance from the flame — not too close, not too far.

ON THE PAPER: Brown lines are appearing as if by magic. The lines form a MAP — tunnels, passages, crossings, rooms. The word "ANFANG" is visible near an X mark at the bottom. In one corner of the paper: a small symbol of four lines and a star, with the tiny word "Tuer" next to it. One section of the map has a WATER STAIN — a brown, blurred spot where the lines disappear (an incomplete section).

JONAS (left, leaning over the desk): Eyes wide, mouth slightly open. He is leaning forward with intense focus on the appearing map lines. One hand grips the edge of the desk. His face is illuminated by warm candlelight from below, creating dramatic shadows.

MILA (right, standing): Her braid hangs over her shoulder. Her eyes are huge — the moment of realization. One hand covers her mouth. She is looking at the map as if seeing something impossible. Her other hand points at the appearing lines.

ON THE DESK (visible in candlelight):
- Winter's letter (already opened, envelope with broken red wax seal)
- An old treasure map (from the previous adventure)
- A small golden button (Winter's golden button — glinting in the candlelight)
- A brass candlestick with a lit candle

ATMOSPHERE: The candle creates a warm, golden cone of light on the three faces and the paper. The rest of the room fades into deep shadow. This is the MAGIC MOMENT — secret ink revealing hidden knowledge. Three children alone with a discovery. The feeling of "the adventure is real."

Do NOT include: modern desk lamps, computer screens, bright overhead lighting, adults, phones as light source, any supernatural glow from the paper itself.
```

---

## Illustration 4: Vier Wege — Der Entscheidungspunkt

**Wo im Buch:** Abschnitt 7 — Die vier Moeglichkeiten

**Prompt:**
```
[Stil-Prefix einfuegen]

Three children in a small bedroom (Jonas' room). The secret-ink map is spread out on the desk, held flat by the golden button in one corner and a flashlight in another. EVENING — through the window behind them, dark storm clouds are gathering. The first raindrops hit the glass.

JONAS (center, standing at the desk): Looking down at the map with his finger tracing four different marked positions. His expression is serious and conflicted — he must choose. His brown hair is slightly messy. He wears a simple t-shirt. His posture leans forward over the map, shoulders tense with decision-making weight.

MILA (left, sitting on the bed): Her legs are crossed, arms crossed in her characteristic pose. A backpack sits open next to her on the bed — visible inside: a pocketknife, a coil of rope, and chalk. She is looking at Jonas with sharp, impatient eyes. One foot taps impatiently. Her expression says: "Pick one. Now."

BEN (right, sitting on the floor): He leans against the wall beneath the window. Rain streaks the glass behind him. His red baseball cap is pushed back on his head. He looks slightly uncomfortable — chin in his hands, elbows on his knees. His expression is a mix of resignation and hope that they'll pick the safest option.

FOUR DIRECTIONS suggested by the map on the desk (visible as brown lines on yellowed paper):
- The tunnel system leading from the Herrenhaus (northeast direction on the map)
- A path toward the mill (northwest)
- A house symbol (Frau Bergmann's house, west)
- A telephone symbol with a question mark (Winter, far away)

THROUGH THE WINDOW: Storm clouds rolling in. Dark grey sky. Wind bending tree branches. The manor house visible on the distant hill with scaffolding. Lightning is NOT visible (no lightning), but the sky looks threatening.

ON THE DESK beside the map: Meier's flashlight (old, metallic), Ben's phone, Jonas' phone, the golden button

ATMOSPHERE: The calm before the storm — literally and figuratively. The moment of choice. Rain begins. Time pressure builds. Four paths, one decision. The room feels intimate and safe, but the weather outside signals danger ahead.

Do NOT include: arrows or text overlays on the illustration, adults, bright daylight, the room being dark (there is still room light on), other rooms visible.
```

---

## Illustration 5: Die Metalltuer mit den vier Symbolen

**Wo im Buch:** Abschnitt 11 — Die Entdeckung der zweiten Tuer

**Prompt:**
```
[Stil-Prefix einfuegen]

Close-up view of a massive metal door in an underground tunnel. The door fills most of the frame. It is ancient, made of dark metal with green patina (shown through varying crosshatching density). No handle. No keyhole.

IN THE CENTER OF THE DOOR: Four HORIZONTAL LINES arranged vertically (one above the other, like four dashes stacked). Each line has a small ROUND INDENTATION at its right end — a socket-like depression sized for a small object. BENEATH the four lines: a FIVE-POINTED STAR engraved into the metal.

NEXT TO EACH LINE, scratched into the metal in TINY letters barely visible:
- Top line: W.
- Second line: M.
- Third line: B.
- Fourth line: H.
(Winter, Meier, Bergmann, Hoffmann — the four founding families)

A FLASHLIGHT BEAM from the lower left illuminates the door and its details. The beam creates a bright cone on the metal surface while the surrounding tunnel walls fade into darkness.

A CHILD'S HAND (Jonas') reaches from the bottom-right corner toward the top indentation. In his other hand (partially visible at bottom-left): a small GOLDEN BUTTON that glints in the flashlight beam. The button is clearly the right size and shape for the round indentation. The hand is small against the massive door — emphasizing scale.

DOOR SURFACE DETAILS:
- Green patina and dark oxidation on the metal (shown through layered crosshatching patterns)
- No decorative rivets (this is different from Band 1's iron door)
- The surface is smooth where hands have touched it over centuries (around the indentations)
- Condensation droplets on the cold metal surface
- The rock walls of the tunnel visible at the edges of the frame — rough-hewn, hand-carved stone with chisel marks

ATMOSPHERE: Standing before a locked puzzle. The door is a test designed by the village founders. Four families, four keys, one door. The reader understands: this door won't open without all four pieces.

Do NOT include: a glowing symbol, magical runes, the door being open or ajar, any text other than the four tiny letters (W. M. B. H.), full bodies of children, bright overall lighting.
```

---

## Illustration 6: Der goldene Knopf leuchtet

**Wo im Buch:** Abschnitt 12 — Die erste Linie aktiviert sich

**Prompt:**
```
[Stil-Prefix einfuegen]

Underground tunnel scene. The massive metal door from Illustration 5 is visible, but now viewed from slightly further back to show three children in front of it. The focus is on the MECHANISM ACTIVATING.

THE DOOR: The same dark metal door with four horizontal lines and star. The FIRST LINE (top) now GLOWS — shown through dense white space/reverse crosshatching to suggest warm golden light emanating from behind the metal. The glow creates a halo effect around the first line. Heat seems to radiate from it. The other three lines remain dark and empty.

JONAS (center, closest to door): He has just pushed the golden button into the first indentation and turned it a quarter-turn clockwise. His right hand is still on the button. His left hand is pressed flat against the door surface — he FEELS the warmth. His face is illuminated by the golden glow from the first line. His expression: awe, wonder, slight fear. Eyes wide. Mouth slightly open.

MILA (behind Jonas, to the left): She has stepped forward and is TOUCHING the glowing first line with her fingertips. Her expression shows intense curiosity — she says "Warm." Her braid hangs over her shoulder. The glow from the line illuminates her hand and face from below.

BEN (further back, to the right): He has taken ONE STEP BACK from the door. His red baseball cap is pulled low. His eyes are wide with shock. His posture is leaning away from the door — the instinct to retreat. But he hasn't run. One hand grips his backpack strap.

LIGHTING: The flashlight beam from Jonas' dropped-or-held flashlight provides general illumination. But the KEY light source is now the GLOWING FIRST LINE — it creates warm light that illuminates the children's faces from the front, creating a dramatic contrast with the dark tunnel behind them.

THREE DARK EMPTY INDENTATIONS below the glowing line are clearly visible — three pieces still missing. The visual message: one down, three to go.

ATMOSPHERE: The mechanism WORKS. Ancient technology coming alive after centuries. Wonder mixed with the unknown. What happens when all four lines glow?

Do NOT include: all four lines glowing, the door being open, electrical wiring, modern technology, supernatural creatures, complete darkness (the glow provides light).
```

---

## Illustration 7: Hinab in die Dunkelheit

**Wo im Buch:** Abschnitt 17 — Der Abstieg in die Gaenge

**Prompt:**
```
[Stil-Prefix einfuegen]

Three children descending a steep stone staircase carved into rock, leading deep underground. The perspective is from BELOW, looking UP at the children as they descend toward the viewer. This creates a dramatic angle where the staircase towers above.

THE STAIRCASE:
- Narrow stone steps carved from raw rock — ancient, worn smooth in the center from centuries of feet
- The walls press close on both sides — barely wider than a person
- Moisture glistens on the stone walls, catching the flashlight beam
- The ceiling is low — Jonas (tallest) nearly touches it
- Above the children: the rectangular opening of the metal door, now OPEN, with faint light from the tunnel behind it — their only connection to the surface
- Below: the stairs disappear into complete blackness where the viewer stands

JONAS (front/lowest on stairs): Leading the way down, holding a flashlight in his right hand. The beam points down past his feet into the darkness below. His left hand touches the wet wall for balance. His face shows determination mixed with apprehension — jaw set, eyes focused downward. He is counting steps in his head.

MILA (middle): Close behind Jonas. One hand on the wall, the other near Jonas' shoulder. Her braid swings as she descends. Her expression is alert and fascinated — "Riecht wie ein Regentag im Wald. Nur aelter." She looks at the chisel marks on the walls.

BEN (rear/highest on stairs): His red cap almost brushes the low ceiling. He descends carefully, one hand gripping the wall tightly, the other clutching his backpack strap. His eyes are wide but he is NOT panicking — there is reluctant courage on his face. His posture shows he wishes he were somewhere else, but he keeps going.

THE DARKNESS BELOW: Complete blackness beneath the lowest visible step. The flashlight beam cuts into it but reveals only more stairs disappearing into nothing. This is the THRESHOLD — from here, there is no quick way back.

WATER DETAILS: Individual drops of water on the walls, catching the flashlight like tiny stars. A thin rivulet running down the wall along the stairs. The sound of dripping somewhere deeper.

ATMOSPHERE: The descent into the unknown. Claustrophobic but compelling. Three small children entering an ancient world beneath their village. The contrast between the faint light above (safety) and total darkness below (adventure) is the core tension.

Do NOT include: monsters, skeletons, spiders, magical light, a visible bottom to the staircase, rails or banisters, modern construction materials.
```

---

## Illustration 8: Die Brunnen-Kammer

**Wo im Buch:** Abschnitt 25b — Das Herz von Eichenhain

**Prompt:**
```
[Stil-Prefix einfuegen]

A circular underground chamber, approximately 4 meters high with a bell-shaped vaulted ceiling. This is the HEART of the story — the Brunnen-Kammer (Fountain Chamber) directly beneath the village well.

THE CHAMBER:
- Round, smooth stone walls — clearly hand-built with care (not natural cave)
- The ceiling curves upward like the inside of a bell or dome
- Stone joints are precise and tight despite centuries of moisture — master craftsmanship
- The floor is smooth polished stone

CENTER OF THE CHAMBER: A natural SPRING. Clear, ice-cold water spouts from bare rock into a STONE BASIN. The basin is ancient — hand-carved, smooth-edged. From the basin, a narrow stone channel (Rinne) in the floor carries water away. The water glimmers and catches the flashlight beam.

FOUR NICHES in the walls, evenly spaced around the chamber. Each niche contains a CARVED STONE CREST (Wappen):
- NICHE 1 (facing viewer): A STAR — beneath it carved: "WINTER"
- NICHE 2 (right): A TREE WITH FOUR BRANCHES — "MEIER"
- NICHE 3 (far side): A CROSS — "BERGMANN"
- NICHE 4 (left): A RING — "HOFFMANN"
Each crest is deeply and carefully carved — high-quality medieval stonework.

THE THREE CHILDREN:
- JONAS (center-right): Kneeling at the stone basin, his RIGHT HAND submerged in the water up to the wrist. His face shows the shock of the ice-cold water — eyes squeezed, sharp intake of breath — but also AWE. Drops of water glisten on his raised left hand. His flashlight lies on the basin edge, pointing upward, creating dramatic uplighting.
- MILA (left, near the niches): Standing with her back to the viewer, tracing the TREE crest with her fingertips. Her head is tilted in wonder. Her posture is unusually soft — no crossed arms. This is a moment of genuine awe for her.
- BEN (right, in the middle of the chamber): Standing with his phone light raised, slowly spinning to take in the whole chamber. His red cap is pushed back. His mouth is open. His phone light creates a second beam that sweeps across the ceiling.

LIGHTING: Two light sources — Jonas' flashlight (pointing up from the basin, creating dramatic shadows on the ceiling) and Ben's phone light (sweeping the walls). The combination creates crosscrossing beams that reveal different parts of the chamber. The water in the basin catches and reflects both lights.

ATMOSPHERE: Sacred discovery. This chamber was built by the village founders. The spring has flowed for centuries, forgotten beneath the village. The children are the first to see it in 70 years. The mood is REVERENCE — like entering a cathedral. Not scary, not action — pure wonder.

Do NOT include: treasure chests (not here), monsters, supernatural glow, water flooding the floor (the water is still contained in the basin and channel), any damage or collapse, bright overhead lighting.
```

---

## Illustration 9: Der unterirdische Wasserfall

**Wo im Buch:** Abschnitt 46 — Die riesige Kammer unter der Muehle

**Prompt:**
```
[Stil-Prefix einfuegen]

A massive underground chamber — as large as a gymnasium. The ceiling disappears into darkness above. This is the biggest space the children have encountered underground.

THE WATERFALL (center, dominating the image): Water CRASHES from a rock ledge approximately 5 meters high into a natural basin below. The waterfall is powerful — spray and mist fill the air. Water droplets catch the flashlight beam like diamonds. The sound would be thunderous. White water foam churns in the basin below the falls.

Below the waterfall: a CONSTRUCTED CHANNEL with straight, carved edges. Someone built this — directing the water flow deliberately. This is not pure nature; it's ancient engineering combined with natural water.

THE THREE CHILDREN (foreground, small against the massive chamber):
- JONAS (left): Standing with flashlight raised HIGH, beam sweeping across the waterfall and the chamber walls. His face is tilted upward in absolute awe. His mouth is open. The flashlight beam reveals the WALL PAINTINGS (see below). Spray from the waterfall mists his hair and clothes.
- MILA (center): She has dropped to her KNEES at the edge of the constructed channel. One hand is in the water. She studies the straight carved edges of the channel with sharp analytical eyes. She is in detective mode even in this moment of wonder — "Das fliesst nicht zufaellig. Jemand hat das gebaut."
- BEN (right): Standing with his mouth wide open. His red baseball cap is DAMP from the spray. Both arms hang at his sides. He is simply overwhelmed. For once, no joke, no complaint — just genuine speechless wonder. Spray glistens on his cap and shirt.

WALL PAINTINGS (partially visible in the flashlight beam on the far wall):
- Faded BROWN AND RED OCHRE colors on grey stone
- Small human figures standing around a water source, some kneeling, some holding bowls/vessels
- The paintings are clearly VERY old — primitive/folk art style
- Only partially visible — the flashlight reveals a section, while the rest fades into shadow
- Hint of FOUR SYMBOLS among the paintings (star, tree, cross, ring — but small and partially obscured)

ATMOSPHERE: The discovery of something ancient and magnificent. The waterfall's power contrasts with the delicate old paintings. The children are tiny against this underground cathedral. This is the moment the story shifts from "treasure hunt" to "discovering forgotten history." The water has been here for centuries, and someone ancient harnessed it.

LIGHTING: Single flashlight beam creating a dramatic cone of light on the waterfall and wall. Spray from the waterfall creates a misty, ethereal quality in the air. The rest of the vast chamber disappears into complete darkness above and to the sides.

Do NOT include: stalactites/stalagmites, bats, glowing crystals, fantasy elements, bright overall lighting, the children looking scared (they are in AWE, not fear), modern elements.
```

---

## Illustration 10: Die Wandmalereien und die Truhe

**Wo im Buch:** Abschnitt 47 — Der Anfang von Eichenhain

**Prompt:**
```
[Stil-Prefix einfuegen]

Underground chamber wall, viewed straight-on as if the viewer is standing in the chamber. The flashlight illuminates a section of rock wall covered in ANCIENT PAINTINGS, and in a NICHE below, a CHEST on a stone pedestal.

THE WALL PAINTINGS (upper two-thirds of the image):
- Painted directly on grey stone in BROWN and RED OCHRE pigments — faded but clearly visible
- SCENE DEPICTED: Small human figures gathered around a water source. Some kneel. Some hold bowls or vessels to collect water. Water is shown as flowing curved lines.
- BELOW THE FIGURES: Four large SYMBOLS in a row, each carefully painted:
  - A STAR (five points)
  - A TREE with four branches
  - A CROSS
  - A RING (circle)
- The paintings look HUNDREDS of years old — paint is faded, flaking in spots, but the images are unmistakable
- The painting style is primitive/folk art — simple but expressive figures

THE NICHE AND CHEST (lower third of image):
- A natural niche in the rock wall, partially hidden behind a rock outcrop
- Inside the niche: a STONE PEDESTAL (like a rough altar)
- On the pedestal: a CHEST. Dark wood. Metal bindings (bands of iron around the wood). On the lid: FOUR SYMBOLS arranged in a circle — Star, Tree, Cross, Ring — matching the wall paintings above. In the center of the circle: a keyhole or lock mechanism.
- The chest is covered in a thin layer of DUST — undisturbed for decades
- The chest is closed

JONAS (right side of image): Standing with the flashlight in one hand and the SECRET INK MAP in the other. He holds the map UP next to the wall paintings, COMPARING them. His face shows the moment of CONNECTION — the map symbols match the ancient paintings. His eyes dart between map and wall. His jaw is set in concentration.

MILA (left side, partially behind the rock outcrop): She has just spotted the chest in the niche. Her body language shows the moment of discovery — she is stepping forward, one hand extended toward the chest, the other grabbing Jonas' arm to get his attention. Her mouth is open, forming the word "Jonas!"

BEN (behind Jonas): Looking at the paintings with his cap pushed back, his expression showing genuine fascination mixed with disbelief. He is counting the symbols with his finger pointed at the wall. "Die haben das Dorf wegen der Quelle gebaut?"

LIGHTING: Flashlight from Jonas' hand creates a bright pool on the wall paintings and spills down onto the chest. The niche is partially shadowed. The rest of the chamber recedes into darkness.

ATMOSPHERE: History revealed. The wall paintings are the ORIGIN STORY of Eichenhain — four families, one spring, one village. The chest is the physical legacy. The children are connecting past and present.

Do NOT include: the chest being open, gold spilling out, supernatural light, modern graffiti, bright overhead lighting, any damage to the paintings beyond natural aging.
```

---

## Illustration 11: Frau Bergmann und die Initialen

**Wo im Buch:** Abschnitt 79b — K.H. + L.B. 1953

**Prompt:**
```
[Stil-Prefix einfuegen]

An underground chamber. The emotional heart of the story. An elderly woman stands before a stone wall, her hand touching CARVED INITIALS. Three children stand behind her, witnessing a 70-year-old wound being healed.

THE WALL AND INITIALS (center of the image, the key visual element):
- Rough grey stone wall of the underground chamber
- Carved into the stone at approximately chest height: "K.H. + L.B. 1953"
- The letters are scratched/carved simply — done by a CHILD with a pointed stone, not by a mason
- The carving is shallow but clearly legible after 70 years
- The stone around the initials is slightly darker — worn smooth from being touched

FRAU BERGMANN (center, closest to wall):
- An elderly woman, approximately 85 years old. Small, thin, white hair tied back in a bun
- Round glasses on her face, glinting in the flashlight light
- She stands with her RIGHT HAND pressed flat against the carved initials — her fingers spread over the letters "K.H."
- Her left hand holds a SILVER-TOPPED WALKING CANE, but the cane is nearly forgotten — she leans toward the wall, not on the cane
- Her expression: tears streaming down her left cheek, but she does NOT wipe them away. Her eyes are closed or half-closed. Her lips are pressed together. This is grief and joy and memory all at once. Seventy years of silence breaking.
- She wears a simple coat, practical shoes
- Her posture is simultaneously fragile and strong — she is reliving the moment when Karl carved their names here as children

THE THREE CHILDREN (behind Frau Bergmann, slightly to the right):
- JONAS (closest to Bergmann): Standing still. His flashlight is lowered respectfully — the beam points at the floor, casting indirect upward light on the wall. His face shows a lump in his throat — tight jaw, glistening eyes. He understands what this means.
- BEN (behind Jonas): He has taken off his RED BASEBALL CAP and holds it in both hands against his chest. This is extraordinary — Ben NEVER removes his cap. His face is red, his eyes wet. He is trying not to cry. His lower lip trembles slightly.
- MILA (next to Ben): She stands motionless. Her arms are at her sides — NOT crossed. Her hand rests on Ben's shoulder. Her expression is solemn and deeply moved. She bites her lip.

THE CHAMBER (background):
- Four niches with carved crests visible in the shadows (Star, Tree, Cross, Ring)
- Water source: spring water visible spilling from rock into a stone basin — the sound of gentle water
- The ceiling curves upward like a dome
- The flashlight creates dramatic shadows — most of the chamber is in shadow, with the wall and Bergmann illuminated

ATMOSPHERE: The most emotional illustration in the book. A woman returns to the place where she was last happy as a child, 70 years ago. The carved initials are proof: Karl was here. She was here. It was real. The three children witness history and loss and love — and they understand it. The water flows gently in the background, unchanged by time.

Do NOT include: bright lighting, cheerful expressions, action/adventure elements, other adults, damage to the initials, the chamber looking scary or threatening. This is a SACRED moment, not a scary one.
```

---

## Illustration 12: Die Truhe oeffnet sich

**Wo im Buch:** Abschnitt 80/81 — Der Schatz der Gruenderfamilien

**Prompt:**
```
[Stil-Prefix einfuegen]

Underground chamber at the natural spring. Focus on the CHEST being opened on a stone pedestal. The spring and waterfall are visible in the background.

THE CHEST (center, main focus):
- A heavy, dark wooden chest on a rough stone pedestal (like an altar)
- Metal bindings of iron around the wood — old, slightly rusted
- The LID is being pushed OPEN — hinges squeaking, visible rust on the hinges
- The STAR AND FOUR LINES emblem is visible on the outside of the lid (now tilted up)
- A thin DUST LAYER disturbed where hands have touched the chest

INSIDE THE CHEST (revealed as the lid opens):
- A bed of RED VELVET (show through dense crosshatching contrast — the fabric is old but still soft)
- FOLDED PARCHMENT DOCUMENTS — yellowed, heavy paper, with visible wax seals
- A LETTER on thicker brown paper — handwritten
- SIX OLD COINS arranged in a small group — dated 1712 (the number should be tiny but suggested)
- An old WACHSSIEGEL (wax seal stamp) — bronze, with the star emblem

FRAU BERGMANN (left of chest): She KNEELS beside the pedestal — Mila helps support her elbow. Bergmann's right hand holds a small BRASS RING with the letter "H" engraved on it (Hoffmann's ring). She has just used it as a key — the ring fits into the chest's lock mechanism. Her face shows overwhelmed emotion — the ring she has worn for 70 years finally fulfilled its purpose. Tears on her cheeks but a SMILE forming — the first real smile.

JONAS (right of chest): He is leaning into the chest, one hand carefully lifting the top parchment document. His flashlight is tucked under his arm, beam angled into the chest. His face shows AWE — wide eyes, careful hands. He reads by flashlight — the document reveals the founding charter.

MILA (behind Frau Bergmann): Supporting Bergmann's arm with one hand. Her other hand is near her mouth in surprise. Her eyes are locked on the chest contents. Her braid hangs forward as she leans in.

BEN (behind Jonas): He peers over Jonas' shoulder into the chest. His red cap is pushed back. His mouth forms a silent "wow." He points at the coins — "1712!" His expression is pure amazement without his usual humor.

BACKGROUND: The spring is visible — water spilling from rock into the stone basin. The chamber walls curve upward. The flashlight and the opening of the chest create warm, intimate lighting on the group. The rest of the chamber is shadowed.

ATMOSPHERE: The payoff. The treasure is not gold and jewels — it's HISTORY. Documents, the founding charter, old coins from the year the village was established. Frau Bergmann's ring — worn for 70 years as a keepsake — turns out to be the KEY. The feeling is reverence, connection to the past, and the satisfaction of a mystery solved.

Do NOT include: overflowing gold, fantasy treasure, bright overhead lighting, the chamber looking threatening, the chest being very large (it is modest-sized, perhaps 40x30cm), supernatural elements.
```

---

## Illustration 13: Winters Stimme

**Wo im Buch:** Abschnitt 93 — Der Anruf bei Heinrich Winter

**Prompt:**
```
[Stil-Prefix einfuegen]

Interior of an old man's kitchen. Warm, cozy, modest. Four people are gathered around a TELEPHONE on a wooden kitchen table. The scene captures the moment a long-awaited phone call finally connects.

THE KITCHEN (Kruegers Kueche):
- Small, old-fashioned German kitchen
- Wooden table in the center with a checked tablecloth
- A wall clock ticking (visible on the wall)
- Coffee cups on the table (used, with dark coffee)
- Old books stacked on a shelf
- The room smells of coffee and old books (suggest through warm, lived-in details)
- A window showing RAIN outside — heavy rain streaking down the glass
- Warm indoor lighting (ceiling lamp creating soft overall light)

THE TELEPHONE (center of table):
- Jonas' smartphone lies flat on the table, set to SPEAKERPHONE
- The screen is illuminated, showing an active call
- The phone is the focal point — all four people lean toward it

JONAS (front-left, closest to phone): Sitting on a wooden chair, leaned forward with his elbows on the table. His face is inches from the phone. His expression: intense concentration, dry mouth, slight trembling. He has just said his name. He is waiting for Winter's response. His hands grip the table edge. Tension radiates from his posture.

MILA (front-right): She sits next to Jonas, her chair pulled close. She has just made a hand gesture to Jonas (arm extended, palm facing him — "Keep talking!"). Her eyes are locked on the phone. Her expression is sharp, alert — ready to jump in if needed. Her braid hangs forward over the table.

BEN (behind Jonas): Standing behind Jonas' chair, leaning over. His red cap is on straight for once. He holds his breath — his cheeks are slightly puffed, eyes wide. Both hands grip the back of Jonas' chair. He is frozen in the moment of anticipation.

KRUEGER (far side of table, facing viewer): An elderly man, approximately 75-80, white hair, thin. He sits in his usual chair with a wooden walking cane leaning against the table beside him. His expression is the most emotional in the scene — his EYES GLISTEN with tears that haven't fallen yet. His mouth is slightly open. He is hearing his old friend's voice for the first time in years. His hands lie flat on the table, trembling slightly. A coffee cup sits untouched beside him.

ATMOSPHERE: The moment of RECONNECTION. An old man's voice comes through a tiny phone speaker and fills a kitchen. Four people lean toward it as if it were a fire. The rain outside creates isolation — the world is just this kitchen, these people, this voice. The tension is not danger but ANTICIPATION and EMOTION. Will Winter help? Will he come back? Everything hangs on this conversation.

Do NOT include: a landline phone (it's Jonas' smartphone on speaker), modern kitchen appliances prominently featured, other people, darkness/scary elements, the phone screen showing a specific interface.
```

---

## Illustration 14: Der Brunnen fliesst

**Wo im Buch:** Abschnitt 56/84/200 — Die Aufloesung (verwendet beim haeufigsten Pfad)

**Prompt:**
```
[Stil-Prefix einfuegen]

A village square CELEBRATION. Bright sunshine. The stone fountain in the center of the square is FLOWING WITH WATER for the first time in 70 years. The entire village has gathered.

THE FOUNTAIN (center, main focus):
- The old stone circular fountain that has been DRY throughout the entire story — NOW FLOWING
- Clear, cold water rises in the basin and spills over the rim in gentle cascades
- Water catches the sunlight, sparkling
- The massive old oak tree towers above, dappled sunlight through the leaves
- Children (village children, not the main three) splash their hands in the water, laughing
- Colorful GARLANDS strung between the oak tree branches and the nearby houses
- A small BRONZE PLAQUE visible on the fountain wall (text not readable, but clearly new and polished)

THE THREE CHILDREN (foreground, sitting on the fountain edge):
- JONAS (center): Sitting on the fountain wall where he sat in Illustration 2 with the letter — COMPLETING THE CIRCLE. His feet dangle. Water splashes near his shoes. He looks CONTENT — a rare peaceful smile. No tension, no anxiety. He has done it. His backpack sits at his feet.
- MILA (left of Jonas): Sitting close to him. For once, her arms are NOT crossed. One hand trails in the flowing water. Her expression is soft — genuine happiness without her usual edge. Her braid is over her shoulder.
- BEN (right of Jonas): Sitting with his legs swinging. Red cap tilted back at a jaunty angle. He has a piece of CAKE in one hand and CRUMBS on his shirt. His grin is enormous and genuine — pure satisfied joy. His other hand gives a thumbs-up to someone off-screen.

BACKGROUND VILLAGERS (not the focus, but present):
- FRAU BERGMANN: Small elderly figure with cane, standing at the fountain. She places FLOWERS on the stone rim. Her face is peaceful.
- KRUEGER: Standing nearby, arms folded. SMILING — a gentle, rare smile. His cane is beside him.
- MEIER: Larger figure, wiping his hands on work pants, standing proudly. He helped repair the pipes.
- Other villagers: adults talking, children playing, a table with cake and drinks visible
- A GRILL somewhere (suggest through a wisp of smoke)

BUNTING AND DECORATION: Colorful garlands, a small banner (not readable), chairs and tables set up around the square. Lemonade bottles on a table. A radio (suggested, not prominent) playing music.

ATMOSPHERE: Pure JOY and RESOLUTION. The dry fountain — the symbol of the village's loss — now flows again. Community celebration. The mystery is solved. The village is healed. Warm summer afternoon light bathes everything. This is the HAPPY ENDING the reader earns.

Do NOT include: rain, dark clouds, the manor house prominently featured, any sense of danger or mystery, nighttime, modern city elements, the three children looking worried or tense.
```

---

## Illustration 15: Winters Rueckkehr — Das Geheime Ende

**Wo im Buch:** Abschnitt 200 — ENDE 222 "Eichenhain" (★★★★★)

**Prompt:**
```
[Stil-Prefix einfuegen]

An autumn morning at the village well. Golden and red leaves swirl in the air. Five people stand at the fountain. This is the ULTIMATE ENDING — the secret ending earned by collecting all four code words. The most emotional and complete scene in the book.

THE SETTING:
- The village well on the Dorfplatz — NOW flowing with clear water (it was restored)
- AUTUMN: Golden oak leaves, red leaves, some falling. Warm morning sunlight, low angle. Long golden shadows on the cobblestones.
- The old bench beside the fountain
- The massive old oak tree with autumn coloring — gold, red, orange against blue sky
- The path leading from the forest to the village is visible behind Winter

THE FIVE PEOPLE (main composition):

CENTER — THE REUNION: KRUEGER and WINTER embrace. Two old men holding each other. This is the EMOTIONAL CENTER of the image.
- WINTER (left in embrace): Thin, upright, grey hair, glasses pushed up on his forehead. A RUCKSACK on one shoulder (he just arrived from a long journey). His eyes are CLOSED. His expression is relief and homecoming — decades of searching are over. He wears a simple jacket, hiking boots. His arms wrap around Krueger tightly.
- KRUEGER (right in embrace): White-haired, slightly stooped, his cane has FALLEN TO THE GROUND beside him (he dropped it to run to Winter). His shoulders SHAKE with silent emotion. His face is buried in Winter's shoulder. His hands grip Winter's jacket.

LEFT — FRAU BERGMANN: Standing at the fountain rim, a few steps from the two men. Small, old, upright despite her age. Her silver-topped cane in one hand. Her other hand is pressed against her heart. Her eyes GLISTEN — tears forming but not falling yet. Her expression is complicated: joy, grief for Karl who never came back, relief that Winter did. She has just spoken: "Du bist zurueckgekommen."

RIGHT FOREGROUND — THE THREE CHILDREN watching the reunion:
- JONAS: Standing still, one hand on the fountain wall. His expression is solemn pride — he made this happen. His mouth is closed, his eyes are shining. He holds a FOLDED MAP in his other hand.
- MILA: Next to Jonas, biting her lip to hold back tears. Her arms are at her sides. She stands close to Jonas — team.
- BEN: His red cap is IN HIS HANDS (removed out of respect — just like in Illustration 11). He holds the cap with both hands against his chest. His face shows honest emotion — no jokes, no fear. Just a 10-year-old boy witnessing something he'll never forget.

FAR RIGHT — MEIER arrives last, walking into the scene from the right edge. He carries TOOLS in his hands (as always). He is the fourth family joining. His expression shows quiet belonging — he finally feels like part of the community.

AUTUMN LEAVES: Leaves drift in the air between the figures. A few golden leaves rest on the fountain wall and the ground. The leaves create movement and warmth in the scene.

LIGHTING: Low autumn morning sun from the left, creating warm golden light on faces and long shadows on the cobblestones. The light catches the water in the fountain and the falling leaves. Everything is bathed in warmth.

ON THE BENCH (detail): A compass and a folded leather MAP lie on the bench — Winter brought them. The compass is old, brass, scratched from 37 years of use in underground tunnels. These will be passed to Jonas. The next adventure waits.

ATMOSPHERE: HOMECOMING. Reunion. Forgiveness. Legacy. Four families at the well for the first time in decades. The fountain flows. The village is whole. The reader who found all four code words (EICHE, QUELLE, STERN, HAIN) is rewarded with the TRUE ending — not just adventure, but human connection across generations. This illustration should make the reader cry (in a good way).

Do NOT include: summer foliage (it is AUTUMN with colored leaves), darkness, rain, scary elements, the manor house prominently visible, modern vehicles, large crowds (this is an intimate reunion, not a festival — the festival comes later in the text). The tone is intimate and personal, not public celebration.
```

---

## Zusammenfassung: Verteilung

| Bereich | Illustrationen | Nummern |
|---------|---------------|---------|
| Gemeinsam/Eroeffnung | 4 | 1 (Karte), 2 (Brief), 3 (Geheimtinte), 4 (Entscheidung) |
| Cluster A: Die Gaenge | 4 | 5 (Metalltuer), 6 (Knopf leuchtet), 7 (Hinab), 8 (Brunnen-Kammer) |
| Cluster B: Das Wasser | 2 | 9 (Wasserfall), 10 (Wandmalereien + Truhe) |
| Cluster C: Die Zeitzeugin | 2 | 11 (Initialen), 12 (Truhe oeffnet) |
| Cluster D: Winters Geheimnis | 1 | 13 (Winters Stimme) |
| Enden | 2 | 14 (Brunnen fliesst), 15 (Winters Rueckkehr) |
| **Gesamt** | **15** | |

## Hinweise zur Nutzung

1. **Stil-Prefix**: Den Stil-Prefix IMMER als ersten Satz einfuegen, damit alle 15 Bilder konsistent aussehen.
2. **Reihenfolge**: Am besten erst die Band-1-Charakterbilder als Referenz nutzen (Illustration 3 aus Band 1 zeigt Jonas, Mila, Ben). Dann Band 2 Illustration 2 (Brief am Brunnen) generieren als neues Referenzbild, da die Kinder jetzt 3 Wochen aelter/vertrauter wirken sollen.
3. **Band-1-Konsistenz**: Die Kinder muessen IDENTISCH aussehen wie in Band 1 — gleiche Haare, gleiche Kleidung (Jonas: braune Haare, T-Shirt, Rucksack; Mila: Zopf, Turnschuhe mit bunten Schnuersenkeln; Ben: rote Kappe, etwas kleiner).
4. **Korrekturen**: Wenn ein Bild nicht passt, den Prompt wiederholen mit dem Zusatz "Make the following changes: [spezifische Aenderung]".
5. **Format**: Fuer Buchdruck: Hochformat (portrait), mindestens 2000x3000 Pixel, 300 DPI.
6. **Konsistenz**: Nach dem ersten Bild ChatGPT bitten: "Keep this exact art style for all following illustrations."

