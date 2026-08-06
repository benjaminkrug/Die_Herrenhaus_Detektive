# PLAN — Band 5 (Finale) + Brücke zu Serie 2

## Die Herrenhaus-Detektive, Band 5 (Arbeitstitel: „Das vollständige Wappen")

> Zweck: der verbindliche Fahrplan für das **Finale** der Reihe — und die
> Leitplanken für **Serie 2 danach**. Aufgebaut auf der Band-4-Pipeline, die sehr
> gut funktioniert hat, mit den drei Zusätzen, die ein Finale (statt eines
> Mittelbands) braucht.
>
> Grundlage: `Band_4/Linear/Serienbogen_Band4_5.md` (die verbindliche Richtung).
> Arbeitsweise wie immer: **vor jedem Eingriff besprechen + begründen, nur echte
> Verbesserungen, nicht über-optimieren.**

---

## 0. Der revidierte Fahrplan (Phase 0–8)

Rückgrat = Band-4-Pipeline. **Fett = Finale-Zusatz gegenüber Band 4.**

| Phase | Was | Ergebnis |
|-------|-----|----------|
| **0. Konzept** | Grundentscheidungen klären — **inkl. dramatischem Motor als Pflicht** und **Serie-2-Tür** | Richtung steht |
| **1. Story-Outline** | 19 Kapitel, 4 Akte, jede Entscheidung begründet; **das Ende bewusst designen** | `Story_Outline.md` |
| **1.5 Kanon-Prüfung** ⭐NEU | alle relevanten Fakten aus Band 1–4 zusammenziehen (Ensemble + 4 Gründerfamilien + Kanon), damit Band 5 nichts widerspricht | `Kanon_Check_Band5.md` |
| **2. Welt & Figuren** | leichter als Band 4 (kein neuer Ort): **Zustand von Eichenhain heute + Ensemble-Auffrischung** | `Welt_und_Figuren.md` |
| **3. Serien-Abschluss-Audit** ⭐ERWEITERT | **serienweit**, nicht buchintern: jeder offene Faden aus Band 1–4 → wo Band 5 ihn schließt | `Setup_Payoff_Tracker.md` |
| **4. Szenenplanung** | Kapitel für Kapitel, Handwerks-Regeln R1–R7 | `Detaillierte_Szenenplanung.md` |
| **5. Schreiben** | Akt für Akt, nach jedem Akt QA-Analyse | 19 Kapitel |
| **6. QA** | `qa_messung.py` + `schablonen_analyse.py` + Menschlichkeits-Checkliste (aus Band 4 übernehmen) | Messwerte |
| **7. Kontinuität** | `Author_Info.md`-Tracker füllen (Master-Referenz für Serie 2) | Tracker |
| **8. Produktion** | Manuskript (Muster-A-Köpfe, QR, Impressum), Cover (großer Titel), KDP — **statt „nächster Band"-Leseprobe eine Serien-Abschluss-Seite** | druckfertig |

### Warum die drei Zusätze (Begründung)

- **1.5 Kanon-Prüfung:** Band 5 nutzt das ganze Ensemble + vier Gründerfamilien +
  vier Bücher Kanon. `Author_Info.md` ist riesig. Ein vergessener/widersprochener
  Kanon-Punkt im Finale ist der Kardinalfehler. Band 4 kam mit wenig Altlast aus
  (neuer Ort) — das Heimspiel-Finale nicht.
- **3. Serien-Abschluss-Audit:** Ein Finale zahlt die **ganze Serie** aus, nicht
  nur sich selbst. Der Tracker muss jeden offenen Faden aus Band 1–4 führen (Liste
  in Abschnitt 2), sonst bleibt einer offen.
- **Motor als Pflicht (Phase 0/1):** Der Serienbogen warnt selbst — *„reine
  Auflösung ohne Spannung trägt keine 19 Kapitel."* Band 4 hatte den Countdown.
  Band 5 braucht einen eigenen Motor, sonst wird's ein flaches Münzen-Einsammeln.

---

## 1. Phase-0-Entscheidungen (zu klären, BEVOR die Outline entsteht)

Analyse + Empfehlung je Punkt — **entschieden wird mit dem Autor.**

1. **Dramatischer Motor.** ✅ **ENTSCHIEDEN: Riss in der Dorfgemeinschaft.**
   Der Fund spaltet Eichenhain — wem gehört das Erbe der Gründer? Die Nachfahren
   (Meier, Bergmann, Winter …) geraten aneinander; die Kinder müssen das Ensemble
   zusammenhalten und versöhnen. Figuren-getrieben, kein Bösewicht. Zahlt alle
   Gründerfamilien aus und bringt sie an einen Tisch.
2. **Nele.** ✅ **ENTSCHIEDEN: Nele zieht nach Eichenhain.** Stärkster Abschluss
   ihres Bogens UND Serie-2-Brückenkopf (Kanon für Wiederkehrer, Neuling für neue
   Leser). Als Außenseiterin ohne Anteil an der Familien-Rivalität kann sie
   zugleich der klare, neutrale Blick im Riss sein.
3. **Was öffnet das vollständige Wappen?** ✅ **ENTSCHIEDEN: Zuflucht + Hüter
   (Fusion).** Die Gründer waren selbst Flüchtige (aus Sternbach). Sie gründeten
   Eichenhain als **Ort, der Menschen aufnimmt** — und wurden zugleich betraut,
   etwas zu **bewahren** (die Heilquelle / das, was den Ort besonders macht). Die
   Aufgabe: den Ort ein Zuhause halten UND das Anvertraute schützen. *Details
   (was genau bewahrt wird, wie das Wappen es öffnet) in Phase 1.*
4. **Die Serie-2-Tür.** ⭐
   *Festgelegt mit dem Autor (siehe Abschnitt 3):* Band 5 schließt die Handlung
   **vollständig**, lässt aber am Ende **emotional** eine Tür einen Spalt offen —
   ein Flüstern, kein Cliffhanger, **keine Information, die Serie 2 braucht.**

---

## 1b. Konzept-Kern Band 5 (aus den Phase-0-Entscheidungen — Saat für die Outline)

**Der Satz:** Das vollständige Wappen enthüllt, dass die Gründer Eichenhain als
**Zuflucht und als Hüter-Auftrag** schufen — und dass das Erbe nie zum Besitzen
gedacht war, sondern zum gemeinsamen Tragen.

### ⭐ Umlagerung (Uniqueness-Fix, mit Autor entschieden)

**Der Motor ist keine Objekt-Jagd, sondern eine menschliche Frage:**

> **Gehört die fünfte Familie — Nele — wirklich dazu?**

Grund: „Sammle die drei Münzen" würde Band 2 wiederholen (dort: sammle die vier
Familien-Erbstücke). Deshalb dienen die **Münzen/das Wappen als Beweisstücke** in
einer größeren Frage, sie sind nicht die Struktur.

- **Der Riss** dreht sich nicht nur ums Geld/Erbe, sondern um **einen Menschen:**
  Ein Teil des Dorfes sträubt sich gegen Nele — die Ahrens *blieben zurück*,
  während „unsere" Familien gründeten (und standen in der alten Sternbach-Geschichte
  auf der „anderen Seite"). Nimmt Eichenhain sie auf?
- **Das Zuflucht-Thema wird aktiv statt historisch:** nicht „früher war Eichenhain
  eine Zuflucht", sondern *jetzt*: „Sind wir es noch?" → derselbe Serie-2-Motor
  „beschützen/handeln", schon in Band 5 lebendig.
- **Ein Herz statt zwei Stränge:** Mystery (Münzen/Wappen) und Emotion
  (Nele/Zugehörigkeit) sind **eine** Sache.
- **Der Tiefpunkt** ist nicht „die letzte Münze fehlt", sondern **„Nele will gehen,
  weil das Dorf sie nicht will."**
- **Die Wende ist eine Wahl, kein Beweis** (Band-4-Prinzip: die Großmutter wird
  von ihrer Enkelin umgestimmt, nicht vom Stein). Belonging kann man nicht
  beweisen — nur wählen.
- **Meier trägt den Ensemble-Bogen der ganzen Serie:** Band 1 Antagonist (sperrt
  die Kinder aus) → Band 2 stolzer Gründer-Erbe → Band 5: *sein Stolz* ist es, der
  sich zuerst gegen die fünfte Familie sträubt — und *seine* Wahl, Nele
  aufzunehmen, vollendet den Bogen. Der Mann, der einst aussperrte, nimmt auf.

**Wie alles ineinandergreift:**
- **Der Riss** (wem gehört das Erbe?) ist der Motor. Er löst sich nicht durch ein
  Machtwort, sondern **weil der Fund selbst zeigt: eine Aufgabe kann man nicht
  besitzen, nur gemeinsam tragen.** Die vier Nachfahren-Familien (Meier,
  Bergmann, Hoffmann, Winter) müssen von „meins" zu „unseres".
- **Die drei fehlenden Münzen + das fünfte Zeichen** sind der Detektiv-Weg dahin:
  Jede Münze sitzt bei einer Nachfahren-Familie; das fünfte Zeichen gehört den
  **Ahrens** — Neles Linie. Erst alle fünf zusammen vervollständigen das Wappen.
- **Nele** ist der Schlüssel und der Beweis: die letzte Sternbach-Nachfahrin
  kommt nach Eichenhain — dorthin, das ihre Vorfahren mitgegründet haben. **Das
  Aufnehmen der Heimatlosen, das die Gründer als Aufgabe hinterließen, geschieht
  im Finale leibhaftig.** Voller Kreis: Sternbachs Familien gründeten Eichenhain;
  die letzte Sternbacherin kommt heim.
- **Serie-1-Bogen schließt:** Haus → Dorf → Herkunft → **Sinn** (wozu das alles).
- **Serie-2-Keim (nur Flüstern):** Die Kinder erben die Hüter-Aufgabe. Serie 2 =
  sie leben sie („beschützen"). Band 5 baut das NICHT mechanisch auf — es hallt
  nur im Epilog nach.

**Verknüpfung mit dem ganzen Wasser-Motiv der Reihe:** Heilquelle (Band 1,
Gründungsmythos „Gegründet an der Heilquelle — Seit 1712"), Brunnen/erste Quelle
(Band 2), zweite Quelle (Band 3), versunkenes Sternbach (Band 4). Das „Anvertraute"
in Phase 1 sollte an diesen roten Faden andocken — noch offen, aber der Kandidat
liegt nahe (die Quelle als das, was Eichenhain hütet).

> **Wachpunkt Ton:** kein Pathos, keine Predigt. Die „Aufgabe" muss für 8-10-
> Jährige greifbar und konkret bleiben (ein Ort, eine Handlung, eine Geste) — wie
> die Münze in Band 4 die abstrakte „Schuld" greifbar machte.

---

## 2. Serien-Abschluss-Audit — was Band 5 schließen MUSS (serienweit)

> Wird in Phase 3 zum vollständigen `Setup_Payoff_Tracker.md`. Hier die
> Startliste der offenen Fäden aus Band 1–4.

- [ ] **Die drei fehlenden Pfand-Münzen.** Vier Familien → vier Münzen. Winters
      (Jonas') wurde in Band 4 zurückgegeben. Bergmann / Hoffmann / Meier fehlen.
- [ ] **Bergmann/Hoffmann + Karls Ring** (liegen seit Band 2 still) — zurückholen.
- [ ] **Das fünfte Zeichen / das vollständige Wappen.** Band 4 endet mit *„da
      müssten eigentlich fünf sein"*. Vier Symbole (Baum/Kreuz/Ring/Blume), fünf
      Familien (Ahrens = fünfte). Das ist der Titel — zieht die Ahrens/Nele ins
      Finale.
- [ ] **Wozu Eichenhain gegründet wurde** — die Finalfrage (Punkt 1.3).
- [ ] **Nele:** vom Gast zur Zugehörigen (falls sie kommt).
- [ ] **Die Erwachsenen-Bögen abrunden** (Winter, Holzer, Meier, Krüger, Frau
      Bergmann) — das Ensemble bekommt seinen Abschluss.

**Regel:** Kein Punkt „teilweise". Wer Band 5 nie kauft, muss ein abgeschlossenes
Band 4 gelesen haben; wer Band 5 liest, ein abgeschlossenes **Serien-Finale.**

---

## 3. Brücke zu Serie 2 (Leitplanken — jetzt festgehalten)

> Vom Autor gewünscht: **Serie 2 muss ohne Serie 1 lesbar sein — und Serie-1-Leser
> sollen trotzdem Lust auf Serie 2 haben.** Beides gleichzeitig geht mit einer
> Regel.

### Die Grundregel
**Serie 2 braucht Serie 1 nie zum Verstehen — Serie 1 macht Serie 2 nur reicher.**
Jeder Bezug ist **Dessert, nie die Hauptspeise.** Sobald eine Verbindung
*notwendig* wird, um der Handlung zu folgen, ist die Eigenständigkeit gebrochen.

### Die drei Hebel
1. **Neuling als Leser-Stellvertreter** (wie Jonas in Serie 1). *Empfehlung: Nele*
   — Kanon, aber Außenseiterin in Eichenhain; sie lernt das Dorf frisch = perfektes
   Onboarding für neue Leser, und ihr Zuzug ist zugleich die emotionale Brücke.
2. **Neuer Motor / andere Geschmacksrichtung.** Serie 1 = *die Vergangenheit
   ausgraben*. Serie 2 = *in der Gegenwart beschützen/handeln* (die geerbte
   Aufgabe). Frisch genug zum Alleinstehen, sichtbare Weiterentwicklung für Treue.
3. **Die Brücke ist emotional, nicht informativ.** Serie-1-Leser sahen die Kinder
   die Pflicht **verdienen**; neue Leser akzeptieren „sie haben eine Aufgabe" als
   Prämisse. Dieselbe Tatsache, zwei Tiefen. Serie 2 Buch 1 stellt die Aufgabe
   **komplett neu** vor, ohne Rückblick-Pflicht.

### Was das für Band 5 heißt
Band 5 baut Serie 2 **nicht mechanisch auf.** Es schließt Serie 1 schön ab; die
geerbte Aufgabe hallt im Epilog nach — als Vorausdeutung, nicht als Haken.

> **Später (nach Band 5, wenn Serie-2-Richtung steht):** eigenes
> `Serienuebergang_1_zu_2.md` mit dieser Regel + „was Serie 2 erben darf, was es
> neu erklären MUSS". Und: die **Produktions-Pipeline** (create_manuscript,
> build_cover, build_qr_rezension, QA-Skripte, Cover-Prompt-Vorlagen) ist für
> Serie 2 wiederverwendbar — nicht bei null bauen. Cross-Promo über die „Mehr
> Abenteuer von Benjamin Krug"-Seite ist schon angelegt.

---

## 4. Was Band 5 vom Serienbogen ERBT (verbindlich, nicht neu verhandeln)

Aus `Band_4/Linear/Serienbogen_Band4_5.md`, Abschnitt 3 — Band 4 hat diese Dinge
bewusst NICHT angefasst, damit das Finale sie einlöst:
1. Die drei übrigen Pfand-Münzen.
2. Wozu die Gründer Eichenhain gegründet haben.
3. Die Bergmann/Hoffmann-Fäden.
4. Sternbach ist erzählt + versunken — **Band 5 spielt nicht dort** (Heimspiel in
   Eichenhain).

---

## 5. Pflege

- Ändert sich beim Schreiben etwas an Bogen oder Serie-2-Brücke: hier eintragen,
  nicht im Kopf behalten.
- Abschnitt 2 abhaken, sobald der Faden im Text tatsächlich geschlossen ist.
- Vor „Band 5 fertig": Abschnitt 2 vollständig abgehakt; Serie-2-Tür geprüft
  (Handlung geschlossen, nur emotionales Flüstern offen).
