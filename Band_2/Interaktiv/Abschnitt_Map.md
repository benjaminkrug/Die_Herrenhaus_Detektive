# Verzweigungsdiagramm -- "Dein Fall -- Du entscheidest! Das Geheimnis des Brunnens" (CYOA)

## Legende

- **→** = "Weiter bei Abschnitt..."
- **EP** = Entscheidungspunkt
- **★** = Ende-Qualitaet (1-4 Sterne)
- **[DE]** = Dead End (Loop zurueck)

---

## Architektur: 4 Story-Cluster

```
              START (Abschnitte 1-7, gemeinsam)
                         |
                    EP-MAIN (Abschnitt 7)
              /       |          |          \
         CLUSTER A  CLUSTER B  CLUSTER C  CLUSTER D
         "Die Gaenge" "Wasser"  "Zeitzeugin" "Winters Geheimnis"
         (11-34)     (41-59c)   (66-87)      (91-106)
         4 Enden     4 Enden    4 Enden      4 Enden
```

---

## Gemeinsamer Start (Abschnitte 1-7)

| Nr | Inhalt | Weiter |
|----|--------|--------|
| 1 | 2-3 Wochen nach Band 1. Jonas am Brunnen. Renovierung laeuft. Brief mit rotem Wachssiegel. | → 2 |
| 2 | Bei Krueger. Brief oeffnen. "Unter dem Brunnen liegt der Eingang zum alten Gangsystem. 1953 versiegelt." | → 3 |
| 3 | Leeres Blatt Papier aus Band 1. Ben erinnert sich. Kerze → Geheimtinte: Karte des Gangsystems. | → 4 |
| 4 | Im Archiv mit Milas Oma. Zeitungsartikel: "Zwei Kinder einen Tag verschollen, 1953." Lisbeth Bergmann. | → 5 |
| 5 | Frau Bergmann am Kirchplatz. Erst schweigt sie. Dann: "Bleibt weg. Das Gangsystem ist gefaehrlich." | → 6 |
| 6 | Meier einbezogen. Alte Taschenlampe seines Vaters. "Mein Vater hat gesagt: Geh nie zum Brunnen." 4-Linien-Raetsel. | → 7 |
| 7 | Abend. Karte studieren. 4 moegliche Zugaenge. Die Metalltuer braucht 4 Gegenstaende. Regen zieht auf. | **EP-MAIN** |

**EP-MAIN — Wie kommen wir in die Gaenge?**
> - Die zweite Metalltuer im Tunnel → **Abschnitt 11** (Cluster A)
> - Den Muehlen-Eingang suchen → **Abschnitt 41** (Cluster B)
> - Erst Frau Bergmann ueberzeugen → **Abschnitt 66** (Cluster C)
> - Winter kontaktieren → **Abschnitt 91** (Cluster D)

---

## Cluster A: "Die Gaenge" (Abschnitte 11-32)

**Tonalitaet:** Spannung/Abenteuer
**Nebengeheimnis:** Das Gangsystem fuehrt direkt zur Zeitkapsel — aber es ist instabil
**8 Entscheidungspunkte, 4 Enden**

| Nr | Inhalt | Weiter |
|----|--------|--------|
| 11 | Zurueck ins Herrenhaus. In den Tunnel. Die zweite Metalltuer: 4 Linien + Stern. | → 12 |
| 12 | Jonas: "4 Linien = 4 Gruenderfamilien." Winters goldener Knopf einsetzen → erste Linie leuchtet. 3 fehlen. | **EP-A1** |
| 13 | Meier holen. Im Herrenhaus-Garten. Er zoegert: "Was hat das mit den Gaengen zu tun?" | → 13b |
| 13b | Meier will die Gaenge selbst sehen. "Mein Bauprojekt..." Er gibt widerwillig das Siegel. Zweite Linie. | → 13c |
| 13c | Meier bleibt draussen, wartet. Nervoes. "Wenn ihr in einer Stunde nicht zurueck seid, rufe ich die Feuerwehr." | → 15 |
| 14 | Krueger fragen. Er wird still. Greift an seine Kette. "Heinrich hat mir das hier gegeben." | → 14c |
| 14c | Krueger erzaehlt: "Winter hat die Gaenge 1989 kartiert. Er hat mir gesagt: Falls Kinder kommen..." Gibt Kreuz. Dritte Linie. | → 15 |
| 14b | Direkt probieren. Klopfen, druecken, nichts. Ben: "Ohne alle vier klappt das nie." | → 12 |
| 15 | 3 von 4 Linien leuchten. Der vierte Gegenstand: Karls Messingring. Nur Frau Bergmann hat ihn. | **EP-A2** |
| 16 | Bei Frau Bergmann. "Karl war mein Freund. Der Ring ist alles." Mila: "Wir bringen ihn zurueck." Sie gibt den Ring. | → 17 |
| 16b | Ohne Ring: andere Methode. Ben findet ein Stueck altes Metall im Schuppen. Passt FAST. Tuer oeffnet sich — klemmt. | → 17 |
| 17 | Alle 4 Gegenstaende eingesetzt (oder Improvisation). KLICK. Tuer schwingt auf. Treppe nach unten. Kalte Luft. | → 18 |
| 18 | Alte Gaenge. Niedrige Decken. Markierungen an Waenden: Pfeile, Symbole. Feucht. | **EP-A3** |
| 19 | Linker Gang. Wird enger. Wasser tropft. Rumpeln. EINSTURZ! Kein Zurueck. | → 21 |
| 20 | Rechter Gang. Breiter. Trockener. Fuehrt tiefer. Symbole an den Waenden werden groesser. | → 22 |
| 20b | [DE] Mittlerer Gang. Sackgasse nach 50 Metern. Zurueck zur Kreuzung. | → 18 |
| 21 | Panik. Ben atmet schnell. Jonas: "Die Pfeile! Immer dem Pfeil nach." Wasser sickert. Regen drueckt von oben. | **EP-A4** |
| 22 | Grosse Kammer. Zeichnungen an den Waenden: Baeume, Haeuser, Menschen. Steinsockel mit versiegelter Truhe. | → 23 |
| 23 | DIE ZEITKAPSEL! Truhe mit Herrenhaus-Wappen. Gruendungsurkunde, alte Muenzen, Brief der Gruenderfamilie. | **EP-A5** |
| 24 | Truhe mitnehmen. Weiter. Hoeren Wasser. Grosse Kammer: die natuerliche Quelle! Wasser aus dem Felsen. | → 25 |
| 24b | Nur Brief lesen. Truhe stehen lassen. Ohne Truhe weiter. Echte Konsequenz. | → 25b |
| 25 | Die Quelle! Weiter: ein alter Raum unter dem Brunnen. | → 25b |
| 25b | **BRUNNEN-KAMMER.** Vier Nischen, vier Familienwappen. Die Quelle sprudelt aus dem Felsen. Architektur der Gruender. | → **EP-A6** |
| 26 | Ben: "Frau Bergmann wurde unter dem BRUNNEN gefunden! Also gibt es einen Aufgang!" Er folgt dem Wasser. | → 27 |
| 26b | [DE] Zurueck zum Einsturz. Graben. Sinnlos. Ben hat dann doch die Idee. | → 26 |
| 27 | Rostige Leiter. Fuehrt nach oben. Steinplatte. Sie druecken. LICHT! Mitten auf dem Dorfplatz. Im Brunnen. | → 28 |
| 28 | Dorfbewohner starren. Krueger am Brunnenrand. Laechelt. "Ihr habt es gefunden." | **EP-A7** |
| 29 | Truhe bei Krueger oeffnen. Gruendungsurkunde + Brief: "Es gibt eine zweite Quelle." Frau Bergmann weint. | → 30 |
| 30 | Dorfversammlung. Krueger + Kinder praesentieren. Frau Bergmann steht auf und erzaehlt. Applaus. | **EP-A8** |
| 31 | Gaenge sichern. Brunnen wird Denkmal. Meier leitet Arbeiten. "Ich bin auch Gruenderfamilie." Winter ruft an. | **Ende 208** ★★★★ |
| 32 | Nur Truhe uebergeben. Gaenge bleiben versiegelt. Quelle nie gezeigt. | **Ende 206** ★★★ |
| 33 | Einsturz zu frueh. Flucht durch Seitengang. Draussen, aber ohne Truhe. | **Ende 207** ★★★ |
| 34a | Von EP-A2: Aufgeben. Aber Kinder versuchen 3 Tage, Ring zu finden. Bergmann oeffnet nicht. Opas Ringe passen nicht. Brief unter Tuer. | **EP-A2b** |
| 34 | Endgueltig aufgegeben. Metalltuer bleibt zu. Denkmalamt oeffnet spaeter. Kinder nicht dabei. | **Ende 219** ★★ |

**EP-A1** Meier um Hilfe bitten (→13) / Krueger fragen (→14) / Allein probieren (→14b)
**EP-A2** Frau Bergmann besuchen (→16) / Ohne Ring improvisieren (→16b) / Aufgeben (→34a)
**EP-A2b** Ein letztes Mal zu Bergmann (→16) / Endgueltig aufgeben (→34)
**EP-A3** Links (→19) / Rechts (→20) / Mitte (→20b)
**EP-A4** Pfeilen folgen, vorwaerts (→22) / Zurueck graben (→26b) / Schreien und warten (→33)
**EP-A5** Truhe mitnehmen (→24) / Nur Brief lesen (→24b)
**EP-A6** Bens Idee folgen (→26) / Zurueck versuchen (→26b)
**EP-A7** Alles bei Krueger zeigen (→29) / Direkt zum Buergermeister (→32)
**EP-A8** Gaenge sichern + Dorfversammlung (→31) / Truhe uebergeben, fertig (→32)

---

## Cluster B: "Das Wasser" (Abschnitte 41-59)

**Tonalitaet:** Entdeckung/Abenteuer
**Nebengeheimnis:** Der Muehlen-Eingang fuehrt zur unterirdischen Quelle — die Heilquelle des Dorfes
**7 Entscheidungspunkte, 4 Enden**

| Nr | Inhalt | Weiter |
|----|--------|--------|
| 41 | Zur Muehle. Band 1: Sie kennen den Tunnel. Aber hinter der Schatzkammer geht es weiter. | → 42 |
| 42 | Hinter der Schatzkammer: enge Spalte. Kalte Luft. Ein zweiter Tunnel, AELTER als Winters. | **EP-B1** |
| 43 | Durch die Spalte. Steinwaende. Tropfwasser. Der Gang fuehrt bergab. Karte pruefen: stimmt! | → 44 |
| 43b | Morgen wiederkommen. Nachts: Regen, Wasser laeuft aus Muehle. Muessen sofort los. | → 43c |
| 43c | Regenschaden: Spalte enger, nasser. Ben passt kaum durch. Arm aufgeschrammt. Echte Kosten fuer Warten. | → 44 |
| 44 | Grosse Hoehle. WASSER! Ein unterirdischer Fluss. Blaues Schimmern von Mineralien. | → 45 |
| 45 | Am Ufer: alte Glasflaschen (Winter 1989). Markierungen. Der Fluss fuehrt tiefer. | **EP-B2** |
| 46 | Dem Fluss folgen. Eng. Nass. Dann: RIESIGE KAMMER. Wasserfall! Natuerliche Quelle! | → 47 |
| 47 | Wandmalereien: Menschen an einer Quelle. Symbole der 4 Gruenderfamilien. "Das ist der Anfang von Eichenhain." | → 48 |
| 48 | Steinsockel. Versiegelte Truhe. Herrenhaus-Wappen. DIE ZEITKAPSEL! | **EP-B3** |
| 45b | Am Ufer bleiben. Trockener alter Gang hinter den Flaschen. Winters alter Weg! | → 45c |
| 45c | Winters Werkzeugkiste. Notizbuch mit Skizzen: "Karte der Quelle, 1989." Detaillierter als ihre Karte. | → 45d |
| 45d | Der Gang fuehrt zum gleichen Ort. Aber jetzt wissen sie MEHR als mit dem Fluss-Weg. | → 48 |
| 48b | [alt] Am Ufer Flaschen untersuchen. Winters Notizen: "Die Quelle heilt. Probe 47 bestaetigt." | → 48 |
| 49 | Truhe oeffnen. Gruendungsurkunde. Muenzen. Brief: "Eichenhain = Heilquelle." | → 50 |
| 50 | Ben untersucht die Rohr-Zeichnungen in der Truhe. | → 50b |
| 50b | **BRUNNEN-KAMMER.** Kinder folgen dem Fluss weiter. Alte Rohr-Anschluesse. Ben: "Wenn man HIER graebt, fliesst der Brunnen!" | **EP-B4** |
| 51 | Zurueck mit Truhe. Regen! Wasserstand steigt schnell. Tunnel wird eng. | **EP-B4b** |
| 52 | Ben: "Der Brunnen! Frau Bergmann wurde UNTER dem Brunnen gefunden. Da ist ein Ausgang!" | → 53 |
| 53 | Rostige Leiter. Steinplatte. Druecken. LICHT! Dorfplatz. Nasse Kinder im Brunnen. | → 54 |
| 54 | Krueger da. Truhe zeigen. Er weint. "Heinrich hat es gewusst. Die ganze Zeit." | **EP-B5** |
| 55 | Buergermeister + Ingenieur. Bens Rohr-Zeichnungen umsetzen. 3 Wochen spaeter: BRUNNEN FLIESST! | → 56 |
| 56 | Dorffest. Ben dreht den Hahn. Alle jubeln. Frau Bergmann laechelt. Winter ruft an. | **Ende 211** ★★★★ |
| 57 | Truhe bei Krueger. Brunnen-Plaene nicht umgesetzt. Meier kommt mit Pumpe und bietet Hilfe an. | **EP-B5b** |
| 57b | Meier pumpt Tunnel trocken. Kinder bergen Rohr-Plaene. Meier erkennt Reparierbarkeit. | → 55 |
| 58 | Tunnel wird zu eng im Regen. Zurueck durch die Muehle. Truhe zu schwer → nur Brief mitgenommen. | **Ende 209** ★★ |
| 59 | Von EP-B2: Nicht dem Fluss gefolgt. Seitengang. Eng. Feucht. | → 59b |
| 59b | Meiers Werkzeuge! Frische Spuren. Jemand war hier gestern. Schritte! | → 59c |
| 59c | Meier! Konfrontation im Tunnel. Er wollte den Brunnen allein reparieren. "Ich wollte es gut machen." | **Ende 220** ★★ |

**EP-B1** Durch die Spalte (→43) / Morgen wiederkommen (→43b)
**EP-B2** Dem Fluss folgen (→46) / Am Ufer bleiben — trockener Gang (→45b) / Seitengang nehmen (→59)
**EP-B3** Truhe oeffnen (→49) / Zurueck, Hilfe holen (→57)
**EP-B4** Zurueck mit Truhe (→51) / Rohr-Plaene mitnehmen, Truhe lassen (→57)
**EP-B4b** Bens Idee anhoeren (→52) / Zur Muehle zurueckrennen (→58)
**EP-B5** Brunnen-Plaene umsetzen (→55) / Erst Meier informieren (→57)
**EP-B5b** Meiers Hilfe annehmen (→57b) / Nein, Urkunde reicht (→Ende 210 ★★★)

---

## Cluster C: "Die Zeitzeugin" (Abschnitte 66-87)

**Tonalitaet:** Drama/Emotion
**Nebengeheimnis:** Frau Bergmanns Geschichte von 1953 — was sie wirklich gesehen hat
**7 Entscheidungspunkte, 4 Enden**

| Nr | Inhalt | Weiter |
|----|--------|--------|
| 66 | "Wir brauchen Frau Bergmann." Ben: "Die redet doch nicht mit uns." Mila: "Dann bringen wir sie zum Reden." | → 67 |
| 67 | Frau Bergmanns Haus. Blumen im Garten. Alte Fotos an den Waenden. | **EP-C1** |
| 67b | Die Kinder gehen weg. Jonas dreht sich um. Frau Bergmann steht am Fenster. Blickkontakt. | → 67c |
| 67c | Naechster Tag: Frau Bergmann klopft bei Jonas. "Ich habe nachgedacht." Sie will REDEN, nicht in die Gaenge. | → 67d |
| 67d | Kuechentisch. Frau Bergmann erzaehlt — teilweise. Nicht alles. Die Kinder erfahren nur die Haelfte. Der Brunnen. Die Angst. | **Ende 215** ★★ |
| 68 | Anklopfen. Tee. "Warum seid ihr hier?" Jonas zeigt die Karte. Frau Bergmann wird blass. | → 70 |
| 69 | Durchs Fenster. Fotoalbum auf dem Tisch: Junge Lisbeth + Karl im Wald. Der Brunnen im Hintergrund. | → 70 |
| 70 | "1953. Karl und ich. Wir haben den Eingang gefunden. Unter dem Brunnen." Sie zittert. | **EP-C2** |
| 71 | "Erzaehlen Sie weiter." — "Es war dunkel. Kalt. Wir sind gelaufen. Stundenlang." | → 73 |
| 72 | "Was haben Sie gesehen?" — Frau Bergmann steht auf. Holt eine Schachtel. Fotos. Briefe. | → 72b |
| 72b | Foto: Junge Lisbeth und Karl am Brunnen. Dahinter: junger Winter. "Die drei waren unzertrennlich." | → 72c |
| 72c | Brief von Karl an Lisbeth, 1954: "Ich habe die Truhe wieder gesehen. Wir muessen zurueck." Frau Bergmann weint. | → 73 |
| 73 | "Wir haben die Quelle getrunken. Das Wasser war warm. Es hat nach Erde geschmeckt." | → 74 |
| 74 | "Dann haben wir die Truhe gefunden. Aber wir konnten sie nicht oeffnen. Wir waren Kinder." | **EP-C3** |
| 75 | "Fuehren Sie uns hin!" — Frau Bergmann zoegert. Karls Ring. "Er hat ihn mir gegeben. An dem Tag." | → 77 |
| 76 | "Wir finden den Weg selbst." — Karte studieren. 3 Eingaenge. Einer beim Brunnen. | → 78 |
| 77 | Frau Bergmann steht auf. "Ich komme mit." Erste Mal seit 70 Jahren. | → 79 |
| 78 | Ohne Frau Bergmann zum Brunnen. Steinplatte finden. Hinunter. Verlaufen! | **EP-C4** |
| 78b | Zurueck zu Frau Bergmann. "Wir brauchen Hilfe." Bergmann kommt mit. | → 79 |
| 79 | Mit Frau Bergmann durch die Gaenge. Sie erinnert sich. "Links. Dann die zweite rechts." | → 79b |
| 79b | **BRUNNEN-KAMMER.** Frau Bergmann bleibt stehen. Karls Initialen an der Wand. "K.H. + L.B. 1953." Sie streicht ueber den Stein. "Genau hier haben wir gesessen." | → 80 |
| 80 | Die Quelle. Frau Bergmann weint. "Genau wie damals." Die Truhe steht noch da. | → 81 |
| 81 | Karls Ring passt ins Schloss der Truhe! KLICK. Gruendungsurkunde. Brief. Muenzen. | **EP-C5** |
| 82 | Zurueck. Frau Bergmann haelt die Urkunde. "70 Jahre. Endlich glaubt mir jemand." | → 83 |
| 83 | Dorfversammlung. Frau Bergmann erzaehlt ihre Geschichte. Traenen. Applaus. | → 84 |
| 84 | Der Buergermeister: "Lisbeth Bergmann hat Eichenhain sein Erbe zurueckgegeben." Gedenktafel am Brunnen. Winter ruft an. | **Ende 214** ★★★★ |
| 85 | Truhe gefunden, aber ohne Frau Bergmann. Sie erfaehrt es spaeter. Weint allein. | **Ende 213** ★★★ |
| 86 | Von EP-C4: In den Gaengen verlaufen. Frau Bergmann findet sie. Aber Truhe nicht erreicht. | **Ende 212** ★★ |
| 67e | Weggehen. Am Brunnen sitzen. Krueger kommt vorbei: "Lisbeth wartet seit 70 Jahren." Zweite Chance. | **EP-C1b** |
| 87 | Endgueltig losgelassen. Frau Bergmann sieht ihn hinter der Gardine. "Vorerst." | **Ende 223** ★ |

**EP-C1** Anklopfen (→68) / Durchs Fenster schauen (→69) / Aufgeben, morgen nochmal (→67b) / Loslassen, weggehen (→67e)
**EP-C1b** Doch zurueckgehen (→67b) / Endgueltig loslassen (→87)
**EP-C2** "Erzaehlen Sie weiter." (→71) / "Was haben Sie gesehen?" — Fotos + Briefe (→72)
**EP-C3** "Fuehren Sie uns hin!" (→75) / "Wir finden den Weg selbst." (→76)
**EP-C4** Zurueck zu Frau Bergmann (→78b→79) / Laut rufen und warten (→86)
**EP-C5** Zurueck mit Frau Bergmann (→82) / Truhe mitnehmen, allein zurueck (→85)

---

## Cluster D: "Winters Geheimnis" (Abschnitte 91-106)

**Tonalitaet:** Krimi/Mystery
**Nebengeheimnis:** Winter weiss mehr als alle denken — die zweite Quelle
**6 Entscheidungspunkte, 4 Enden**

| Nr | Inhalt | Weiter |
|----|--------|--------|
| 91 | "Winter hat den Brief geschrieben. Er weiss am meisten." Jonas sucht die Telefonnummer. | → 92 |
| 92 | Krueger hat Winters Nummer. "Er meldet sich nicht immer." Jonas ruft an. Es klingelt. Lange. | **EP-D1** |
| 93 | Winter geht ran! Kurzes Gespraech. "Ihr habt den Brief geoeffnet? Gut. Hoert zu." | → 95 |
| 94 | Mailbox. Jonas spricht drauf. Naechster Tag: Winter ruft ZURUECK. "Entschuldigung. Ich war im Wald." | → 95 |
| 95 | Winter erklaert: "Unter dem Brunnen liegt das Gangsystem der Gruenderfamilien. Ich habe den Zugang durch die Metalltuer gefunden." | **EP-D2** |
| 96 | "Wie kommen wir rein?" — Winter: "4 Gegenstaende der 4 Familien. Ich habe meinen Knopf hinterlassen. Meier, Krueger, Bergmann — fragt sie." | → 96b/98 |
| 96b | Jonas kennt die Tuer schon. Winter erklaert die Reihenfolge: Uhrzeigersinn. Sonst verriegelt 24h. | → 98 |
| 97 | "Was ist da unten?" — Winter: "Eine Zeitkapsel. Und die Heilquelle. Eichenhain wurde deswegen gegruendet." | → 98 |
| 98 | Winter: "Aber es gibt noch etwas. Auf der Karte — der Wasserfleck. Da war ein zweites X. Eine zweite Quelle. Im Wald. Ich habe sie nie gefunden." | **EP-D3** |
| 99 | "Wir holen erst die Zeitkapsel." — Gegenstaende sammeln. Meier: Siegel. Krueger: Kreuz. Frau Bergmann: Ring. | → 100 |
| 99b | "Erzaehlen Sie uns von der zweiten Quelle." — Winter: "Die Karte zeigt einen Weg durch den Wald. Aber ich war zu alt." | → 100 |
| 99c | Winter nicht vertrauen. "Das klingt zu einfach." Kinder gehen OHNE 4 Gegenstaende in die Gaenge. | → 99d |
| 99d | Metalltuer. Ohne Gegenstaende: nichts passiert. Seitengang entdeckt. Alte Werkzeuge. Kein Durchkommen. | → 99e |
| 99e | Zurueck. Jonas bereut. "Winter hat die Wahrheit gesagt." Hoffmanns Notizbuch gefunden! | **Ende 221** ★★★ |
| 100 | Metalltuer. 4 Gegenstaende einsetzen. KLICK. Treppe. Stuetzpfeiler fehlt. DECKENEINSTURZ! Sprint! Mila verletzt. | → 100b |
| 100b | Kein Zurueck. Winter panisch am Telefon. Links abbiegen. Fackelhalter. Zur Quelle. | → 101 |
| 101 | Die Quelle. Die Zeitkapsel. Truhe oeffnen mit Winters Anleitung. "Der Stern auf dem Deckel — drueckt ihn." | → 101b |
| 101b | **BRUNNEN-KAMMER.** Winter beschreibt am Telefon: "Vier Nischen. Vier Wappen. So war es 1989." Die Kinder finden alles genau so. Winters Stimme zittert. | → 102 |
| 102 | Gruendungsurkunde. Brief. Muenzen. Und: eine ZWEITE KARTE. "Das ist sie. Die zweite Quelle." | **EP-D4** |
| 103 | Zurueck. Dorfversammlung. Alles praesentiert. Winter hoert per Telefon zu. "Vielleicht komme ich bald nach Hause." | → 104 |
| 104 | Gedenktafel. Gaenge gesichert. Frau Bergmann erzaehlt. Und die zweite Karte liegt in Jonas' Rucksack. | **Ende 216** ★★★★ |
| 105 | Truhe uebergeben, zweite Karte absichtlich zurueckgelegt. Winter: "Die Rolle ist das Wichtigste." Rathaus verschlossen. | **Ende 217** ★★★ |
| 106 | Von EP-D1: Nie durchgekommen. Gaenge spaeter vom Denkmalamt geoeffnet. Kinder nicht dabei. | **Ende 218** ★★ |

**EP-D1** Nochmal anrufen (→93) / Nachricht hinterlassen (→94) / Aufgeben (→106)
**EP-D2** "Wie kommen wir rein?" (→96) / "Was ist da unten?" (→97)
**EP-D3** Erst Zeitkapsel holen (→99) / Mehr ueber zweite Quelle (→99b) / Winter nicht vertrauen (→99c)
**EP-D4** Alles praesentieren inkl. zweite Karte (→103) / Nur Truhe uebergeben (→105)

---

## Easter Egg: Geheimes Ende (Abschnitt 200)

**Konzept:** Jedes ★★★★-Ende enthaelt ein verstecktes Codewort. Wer alle 4 sammelt, kann zu Abschnitt 200.

**Die 4 Codewoerter (in den ★★★★-Enden versteckt):**
| Ende | Cluster | Codewort | Wo im Text |
|------|---------|----------|------------|
| 208 | A | EICHE | Gravur am Brunnenrand |
| 211 | B | QUELLE | Schrift auf dem Rohr |
| 214 | C | STERN | Rueckseite von Karls Foto |
| 216 | D | HAIN | Winter schreibt auf die Karte |

**Hinweis am Buchende (nach dem letzten Abschnitt):**
> *Du hast ein Ende erreicht. Aber hast du ALLE vier Woerter gefunden?*
> *Wenn du weisst, was EICHE + QUELLE + STERN + HAIN zusammen ergeben, gehe zu Abschnitt 200.*

| Nr | Inhalt | Weiter |
|----|--------|--------|
| 200 | Winter kommt WIRKLICH zurueck. Am Brunnen. Die Kinder treffen ihn. Er zeigt ihnen die Brunnen-Kammer persoenlich. Vier Familien versammeln sich. Brunnen wird restauriert. Dorffest. Winter bleibt. | **Ende 222** ★★★★★ |

---

## Alle 18 Enden — Uebersicht

| # | Name | Cluster | ★ | Einzigartig |
|---|------|---------|---|-------------|
| 208 | "Die Quelle von Eichenhain" | A | ★★★★ | Gaenge gesichert, Dorfversammlung, Winter ruft an. *Codewort: EICHE* |
| 206 | "Die versiegelte Wahrheit" | A | ★★★ | Truhe ja, Gaenge bleiben versiegelt |
| 207 | "Der versperrte Weg" | A | ★★★ | Einsturz, Flucht, ohne Truhe |
| 219 | "Nicht dabei" | A | ★★ | Aufgegeben, Denkmalamt spaeter |
| 211 | "Der Brunnen fliesst" | B | ★★★★ | Brunnen repariert! Ben dreht den Hahn. *Codewort: QUELLE* |
| 210 | "Die vergessene Urkunde" | B | ★★★ | Truhe ja, Brunnen-Plaene nicht umgesetzt |
| 209 | "Der Brief aus der Tiefe" | B | ★★ | Regen, Truhe zurueckgelassen |
| 220 | "Meiers Geheimnis" | B | ★★ | Seitengang → Meier-Konfrontation im Tunnel |
| 214 | "Lisbeths Traenen" | C | ★★★★ | Frau Bergmann fuehrt, 70 Jahre Befreiung. *Codewort: STERN* |
| 213 | "Ohne Lisbeth" | C | ★★★ | Truhe ohne Frau Bergmann |
| 212 | "Verlaufen" | C | ★★ | In Gaengen verlaufen, Frau Bergmann rettet |
| 215 | "Die halbe Wahrheit" | C | ★★ | Frau Bergmann erzaehlt teilweise, aber geht nicht mit |
| 216 | "Winters Anruf" | D | ★★★★ | Zweite Karte gefunden, Winter kommt heim. *Codewort: HAIN* |
| 217 | "Fast alles" | D | ★★★ | Truhe ja, zweite Karte uebersehen |
| 218 | "Kein Empfang" | D | ★★ | Winter nie erreicht |
| 221 | "Der eigene Weg" | D | ★★★ | Winter misstraut, Hoffmanns Notizbuch gefunden |
| 222 | "Eichenhain" | — | ★★★★★ | GEHEIMES ENDE. Nur ueber 4 Codewoerter erreichbar. Winter kommt heim. |
| 223 | "Stille am Kirchplatz" | C | ★ | Jonas klopft nicht. Frau Bergmann wartet hinter der Gardine. |

**Sterne-Verteilung:**
| Sterne | Anzahl | Enden |
|--------|--------|-------|
| ★★★★★ | 1 | 222 (geheim) |
| ★★★★ | 4 | 208, 211, 214, 216 |
| ★★★ | 6 | 206, 207, 210, 213, 217, 221 |
| ★★ | 6 | 209, 212, 215, 218, 219, 220 |
| ★ | 1 | 223 |

---

## Metriken

| Metrik | Wert |
|--------|------|
| Abschnitte gesamt | ~128 |
| Woerter gesamt | ~54.000-56.000 |
| Enden | 18 (inkl. 1 geheimes) |
| Entscheidungspunkte | ~29 |
| Content pro Durchlauf | ~15-22% |
| Story-Cluster | 4 |
| Perfekte Enden | 4 + 1 geheimes (★★★★★) |
| Pseudo-Entscheidungen | 0 |
| Brunnen-Kammer | Gemeinsamer Ort in allen 4 Clustern |

---

## Band-3-Hooks (in allen ★★★★-Enden gesaet)

- **Zweite Quelle** im Wald hinter Eichenhain (Karte mit zweitem X)
- **Winter kommt zurueck** ("Vielleicht komme ich bald nach Hause")
- **Die Karte zeigt mehr** als nur das Dorf
- **Warum Winter wirklich verschwand** — er suchte die zweite Quelle
- **Im geheimen Ende 222:** Winter kommt WIRKLICH heim — staerkster Hook fuer Band 3
