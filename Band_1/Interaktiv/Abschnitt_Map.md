# Verzweigungsdiagramm -- "Dein Fall -- Du entscheidest! Das verbotene Herrenhaus" (CYOA)

## Legende

- **→** = "Weiter bei Abschnitt..."
- **EP** = Entscheidungspunkt
- **★** = Ende-Qualität (1-4 Sterne)
- **[DE]** = Dead End (Loop zurück)

---

## Architektur: 4 Story-Cluster

```
              START (Abschnitte 1-7, gemeinsam)
                         |
                    EP-MAIN (Abschnitt 7)
              /       |          |          \
         CLUSTER A  CLUSTER B  CLUSTER C  CLUSTER D
         "Geisterhaus" "Wasser"  "Detektive" "Brief"
         (11-32)     (41-59)    (66-86)     (91-105)
         4 Enden     3 Enden    4 Enden     3 Enden
```

---

## Gemeinsamer Start (Abschnitte 1-7)

| Nr | Inhalt | Weiter |
|----|--------|--------|
| 1 | Jonas zieht nach Eichenhain. Herrenhaus auf dem Hügel. | → 2 |
| 2 | Trifft Mila und Ben. Gruselgeschichten. | → 3 |
| 3 | Schatten im Fenster! "Der Geist von Winter!" | → 4 |
| 4 | Nächster Morgen. Erzählen von Winter. Goldgerüchte. | → 5 |
| 5 | Zum Brunnen. Krüger sitzt da. | → 6 |
| 6 | Krüger warnt: "Bleibt weg." | → 7 |
| 7 | Abend. Kerzenlicht im Haus. SMS an Mila. | **EP-MAIN** |

**EP-MAIN — Was tun wir jetzt?**
> - Direkt zum Herrenhaus → **Abschnitt 11** (Cluster A)
> - Die alte Mühle untersuchen → **Abschnitt 41** (Cluster B)
> - Im Dorf Informationen sammeln → **Abschnitt 66** (Cluster C)
> - Krüger nachlaufen → **Abschnitt 91** (Cluster D)

---

## Cluster A: "Das Geisterhaus" (Abschnitte 11-32)

**Tonalität:** Grusel/Horror
**Nebengeheimnis:** Spuk = Winters Rätsel-Test (Werkstatt!)
**8 Entscheidungspunkte, 4 Enden**

| Nr | Inhalt | Weiter |
|----|--------|--------|
| 11 | Zum Hügel. Zaun. Kerzenlicht. | → 12 |
| 12 | W-Schlüssel passt nicht ans Tor. Rascheln → Katze. Zaun-Lücke. | → 13 |
| 13 | Durch die Lücke. Fußspuren. Offenes Fenster. | **EP-A1** |
| 14 | Goldener Knopf. Vorhang bewegt sich. | **EP-A2** |
| 14b | Schuppen. Foto + Archiv-Hinweis. | → 15 |
| 15 | Archiv: Tagebuch, Code (T-d-M / S-s-N / T-e-L). | → 16 |
| 15b | Direkt ins Haus → Gemälde gesehen. | → 15 |
| 16 | Code analysiert. Grundriss: Raum ohne Eingang. | → 17 |
| 17 | Ins Haus. Fußspuren. DRAHT unter Diele! | **EP-A3** |
| 18 | Treppe hoch. Kerzenwachs. SEILZUG-Mechanismus! Geheimraum: Uhr, Symbol. | → 19 |
| 18b | Erdgeschoss. Küche. Zugemauerte Kellertür. | → 18 |
| 19 | Gemälde-Mechanismus → KLICK → Keller-Grundriss. Schritte! Tür fällt zu. Flucht. | → 20 |
| 20 | Nacht-Besuch. Mondlicht. Zweiter Grundriss (Tunnel!). Mantelperson! | **EP-A4** |
| 21 | Versteckt. Person untersucht Gemälde, geht zur Mühle. | → 22 |
| 21b | Fliehen. Eimer-Crash. Person → Mühle. | → 22 |
| 22 | Morgen. Meier verdächtig (Lehm). Im Laden nervös, lügt. | **EP-A5** |
| 23 | Keller. Steintreppe. 4 Räume. Fußspuren. | **EP-A6** |
| 24 | Letzter Raum. Geheimfach → Tunnelkarte. W-Schlüssel passt! | → 25 |
| 24b | Umkehren. Nächster Morgen. | → 24 |
| 25 | Tunnel. Spinnen. Tropfwasser. Eisentür. KRACH — eingesperrt! | **EP-A7** |
| 26 | Ruhe. Eisentür → SCHATZKAMMER. Truhe. Ben: "Tür-eins-Licht!" Zweite Tür! | → 27 |
| 26b | [DE] Hämmern, Panik → Ben hat trotzdem Idee. Schatzkammer + Truhe. | → 27 |
| 26c | [DE] Zurück durch Tunnel → Kellertür verriegelt → vorwärts. | → 25 |
| 27 | **WERKSTATT!** Baupläne Spuk-Mechanismen. Tagebuch: "Wer mutig ist..." Ausgang Mühle. | → 28 |
| 28 | Zurück durchs Haus. Spuk entlarvt. Kaffee. Meier kommt! | **EP-A8** |
| 29 | Verstecken + belauschen. Krüger erscheint. Volle Wahrheit. Werkstatt erklärt → Meier LACHT. | **Ende 108** ★★★★ |
| 30 | Herausspringen. Meier gesteht teilweise. Werkstatt nie entdeckt. | **Ende 106** ★★★ |
| 31 | Fliehen. Krüger hilft Tage später. Nicht allein geschafft. | **Ende 107** ★★★ |
| 32 | Von EP-A5: Meier konfrontiert → Eltern angerufen. Hausarrest. | **Ende 119** ★★ |

**EP-A1** Durch die Lücke (→14) / Zum Schuppen (→14b→15)
**EP-A2** Ins Dorfarchiv (→15) / Direkt ins Haus (→15b) / Meier konfrontieren (→32)
**EP-A3** Treppe hoch (→18) / Erdgeschoss (→18b)
**EP-A4** Verstecken (→21) / Fliehen (→21b→22)
**EP-A5** Keller durchsuchen (→23) / Meier konfrontieren (→32)
**EP-A6** Weitergehen (→24) / Umkehren (→24b→24)
**EP-A7** Ruhe bewahren (→26) / Hämmern (→26b) / Zurück (→26c)
**EP-A8** Versteckt bleiben (→29) / Herausspringen (→30) / Fliehen (→31)

---

## Cluster B: "Das Wasser-Abenteuer" (Abschnitte 41-59)

**Tonalität:** Abenteuer/Action
**Nebengeheimnis:** Unterirdische Quelle = Brunnen-Wahrheit
**6 Entscheidungspunkte, 3 Enden**

| Nr | Inhalt | Weiter |
|----|--------|--------|
| 41 | Mühlenruine. Eingestürztes Dach. Efeu. Bach. | → 42 |
| 42 | Hinter Mauer: Lehm-Spuren. Anderer Stein. | **EP-B1** |
| 43 | Stein verschieben → Tunnel! Kalt. Feucht. WASSER! "Ein Fluss!" | → 44 |
| 43b | [DE] Morgen wiederkommen. Nachts: Licht in der Mühle. | → 42 |
| 44 | Abzweigung! Links: Eisentür. Rechts: Wassergeräusch, blaues Schimmern. | **EP-B2** |
| 45 | RECHTS: Wasserfall! Riesige Höhle! Unterirdischer See! WANDMALEREIEN! | → 46 |
| 46 | Wandmalereien: Menschen an Quelle. Glas-Flaschen (Winter 1989). Karte: Quelle = Brunnen! | → 47 |
| 47 | Zurück. Eisentür. Code-Mechanismus. Kerzenhalterung — keine Kerze! | **EP-B3** |
| 48 | Ben: Feuerzeug! Mila: Kerzenstummel! KLICK → Tür öffnet! | → 49 |
| 48b | [DE] Zurück ins Dorf. Archiv: Tagebuch + Code. Mit Kerze zurück. | → 49 |
| 49 | SCHATZKAMMER! Archive. Ordner "Wasserversorgung Eichenhain." | → 50 |
| 50 | Truhe: Münzen, Ringe, Uhr, Testament. Mappe "Wahrheit über den Brunnen." | **EP-B4** |
| 51 | Ben versteht die Rohr-Zeichnungen! "Wenn man HIER gräbt..." | → 52 |
| 52 | Nachts. Meier geht ins Haus. | **EP-B5** |
| 53 | Warten → ins Haus → "Der Tunnel verbindet alles!" Quelle = größtes Geheimnis. | → 55 |
| 54 | Meier konfrontieren. Wasserproben zeigen. Er erstarrt. | → 55 |
| 55 | Krüger am Brunnen. "Ihr wisst von der Quelle." | → 56 |
| 56 | Bürgermeister. Truhe + Brunnen-Pläne. Ingenieur gerufen. | **EP-B6** |
| 57 | 3 Wochen später: WASSER! Brunnen fließt! Dorf feiert. Ben dreht den Hahn. | **Ende 111** ★★★★ |
| 58 | Nur Truhe übergeben. Brunnen-Pläne nicht verstanden. | **Ende 110** ★★★ |
| 59 | Meier gefolgt → im Tunnel erwischt → Wasser-Tunnel → pitschnass raus. | **Ende 109** ★★ |

**EP-B1** Stein verschieben (→43) / Morgen wiederkommen (→43b)
**EP-B2** Nach rechts, zum Wasser (→45) / Zur Eisentür (→47)
**EP-B3** Code versuchen (→48) / Zurück ins Dorf (→48b)
**EP-B4** Ben liest die Pläne (→51) / Pläne mitnehmen (→58)
**EP-B5** Warten, dann reingehen (→53) / Meier konfrontieren (→54) / Meier folgen (→59)
**EP-B6** Alles zeigen inkl. Brunnen (→57) / Nur Truhe übergeben (→58)

---

## Cluster C: "Die Dorf-Detektive" (Abschnitte 66-86)

**Tonalität:** Krimi/Detektiv
**Nebengeheimnis:** Winter zu Unrecht beschuldigt → Rehabilitierung
**7 Entscheidungspunkte, 4 Enden**

| Nr | Inhalt | Weiter |
|----|--------|--------|
| 66 | "Wir brauchen Fakten." Ben: "Endlich ein Plan, bei dem ich nicht sterbe." | → 67 |
| 67 | Meiers Laden. Eis. Beiläufige Fragen. Verschüttet fast die Milch. | → 68 |
| 68 | Frau Becker: "Winter war ein guter Mann. Aber es gab einen Prozess..." | **EP-C1** |
| 69 | ARCHIV: Tagebuch! Code! Zeitungsartikel: "Dorfkassierer des Diebstahls beschuldigt." | → 71 |
| 70 | Bürgermeister: "Gesperrte Akte. Stempel 1994." | → 71 |
| 71 | Abend. Jonas grübelt. Dieb oder Opfer? | **EP-C2** |
| 72 | MEIER BEOBACHTEN: 3 Tage. Ben mit Fernglas. Meier kommt AUS DER ERDE! "Tunnel!" | → 75 |
| 73 | KRÜGER FRAGEN: "Ihr wisst vom Prozess? Fast alles. Aber nicht die Wahrheit." | → 76 |
| 74 | ZUM HAUS: Mit Vorwissen schnell zum Gemälde. Meier steht hinter ihnen! | **EP-C3** |
| 75 | Zur Mühle. Meiers Spuren. Tunnel. SCHATZKAMMER! Ordner "Prozessunterlagen 1994." | → 79 |
| 76 | Krüger nimmt sie zur Mühle. Tunnel. Schatzkammer. | → 79 |
| 77 | Ehrlich: Zeigen Meier alles. Er kooperiert. | → 80 |
| 78 | Fliehen! Nie die volle Wahrheit. | **Ende 112** ★★ |
| 79 | Truhe + Winters VERTEIDIGUNGSBRIEF. Quittungen. Fotos der 3 echten Diebe. | **EP-C4** |
| 80 | Bens Frage: "Warum hat niemand die Quittungen gesehen?" | → 81 |
| 81 | Mila: DIE Quittung. 5.000 Mark zurückgezahlt. Obwohl unschuldig. | **EP-C5** |
| 82 | Bürgermeister liest Winters Verteidigung — zum ersten Mal. | → 83 |
| 83 | Gemeinderatssitzung. Hartmanns Enkel entschuldigt sich. Winter FREIGESPROCHEN. | → 84 |
| 84 | 3 Monate später: "Heinrich-Winter-Weg." Mila zieht das Tuch. Ben isst Eis. | **Ende 114** ★★★★ |
| 85 | Beweise aufheben, aber nicht zum Bürgermeister. Formelle Rehabilitation steht aus. | **Ende 113** ★★★ |
| 86 | Aufgegeben. Am Bach gespielt. Andere lösen den Fall. | **Ende 115** ★ |

**EP-C1** Ins Archiv (→69) / Zum Bürgermeister (→70)
**EP-C2** Meier beobachten (→72) / Krüger nochmal fragen (→73) / Zum Haus gehen (→74) / Aufgeben (→86)
**EP-C3** Ehrlich sein (→77) / Fliehen (→78)
**EP-C4** Beweise zum Bürgermeister (→80) / Beweise aufheben (→85)
**EP-C5** Zum Bürgermeister (→82) / Aufheben (→85)

---

## Cluster D: "Krügers Brief" (Abschnitte 91-105)

**Tonalität:** Drama/Emotion
**Nebengeheimnis:** Krügers ungeöffneter Brief = Vergebung
**5 Entscheidungspunkte, 3 Enden**

| Nr | Inhalt | Weiter |
|----|--------|--------|
| 91 | "Herr Krüger! Warten Sie!" Erwähnt Tunnel + Mühle. | → 92 |
| 92 | Nächster Tag. Krügers Cottage. Blumen im Garten. | **EP-D1** |
| 93 | Anklopfen. Tee. Alte Möbel. Fotos an der Wand. | → 95 |
| 94 | Durchs Fenster spähen. Fotoalbum: Krüger + Winter als junge Männer! | → 95 |
| 95 | Krüger: "Winter war mein bester Freund. Wie Brüder. Beim Prozess war ich feige." | **EP-D2** |
| 96 | "Wir sind die Richtigen!" Jonas zeigt W-Schlüssel. Krügers Hände zittern. | → 98 |
| 97 | Sanft: "Sie vermissen ihn." "Jeden Tag. Der Brunnen war unser Treffpunkt." | → 98 |
| 98 | Schublade: BRIEF. Vergilbt. Ungeöffnet. 30 Jahre. "Ich hatte Angst." | **EP-D3** |
| 99 | "Öffnen Sie ihn." Mila hält den Umschlag. Krüger liest. "Vergib dir selbst." | → 100 |
| 99b | "Wir öffnen ihn zusammen." Am Brunnen. Laut vorgelesen. | → 100 |
| 100 | Krüger weint. Dann: "Kommt. Ich zeige euch alles." Mühle. Tunnel. Schatzkammer. | → 101 |
| 101 | Schatzkammer. Krüger: "Alles noch da." Truhe. | → 102 |
| 102 | Truhe: Münzen, Ringe, Uhr, Testament. Jonas liest vor. Ben schluchzt. | **EP-D4** |
| 103 | Meier holen. Drei-Wege-Gespräch. Meier weint. Krüger vergibt sich. Brief am Brunnen. | **Ende 116** ★★★★ |
| 104 | Zum Bürgermeister. Formell. Krüger allein am Brunnen. Aber lächelnd. | **Ende 117** ★★★ |
| 105 | Nicht zu Krüger → Denkmalamt war schneller. Brief nie geöffnet. | **Ende 118** ★★ |

**EP-D1** Anklopfen (→93) / Durchs Fenster spähen (→94) / Zum Haus gehen (→105)
**EP-D2** "Wir sind die Richtigen!" (→96) / Sanfter Ansatz (→97)
**EP-D3** "Öffnen Sie ihn." (→99) / "Zusammen öffnen." (→99b)
**EP-D4** Meier dazuholen (→103) / Zum Bürgermeister (→104)

---

## Alle 14 Enden — Übersicht

| # | Name | Cluster | ★ | Einzigartig |
|---|------|---------|---|-------------|
| 108 | "Das Rätsel-Museum" | A | ★★★★ | Werkstatt entdeckt, Meier lacht, Haus = Museum |
| 106 | "Gut, aber..." | A | ★★★ | Truhe ohne Werkstatt |
| 107 | "Mit Hilfe" | A | ★★★ | Krüger hilft, nicht allein geschafft |
| 119 | "Hausarrest" | A | ★★ | Erwischt. Ben: "Ich hab nichts getan!" |
| 111 | "Der Brunnen fließt" | B | ★★★★ | Brunnen repariert! Ben dreht den Hahn |
| 110 | "Die Truhe" | B | ★★★ | Truhe ja, Brunnen-Pläne nicht verstanden |
| 109 | "Pitschnass" | B | ★★ | Im Wasser-Tunnel verlaufen |
| 114 | "Heinrich-Winter-Weg" | C | ★★★★ | Winter rehabilitiert, Straße benannt |
| 113 | "Beweise, aber..." | C | ★★★ | Beweise gefunden, Rehabilitation steht aus |
| 112 | "Die Flucht" | C | ★★ | Geflohen, nie die Wahrheit |
| 115 | "Am Bach gespielt" | C | ★ | Aufgegeben, andere lösen es |
| 116 | "Krügers Tränen" | D | ★★★★ | Brief, Vergebung, emotional |
| 117 | "Der offizielle Weg" | D | ★★★ | Formell gelöst |
| 118 | "Zu spät" | D | ★★ | Nicht bei Krüger, Halbwissen |

---

## Metriken

| Metrik | Wert |
|--------|------|
| Abschnitte gesamt | ~105 |
| Wörter gesamt | ~38.000-42.000 |
| Enden | 14 |
| Entscheidungspunkte | ~26 |
| Content pro Durchlauf | ~18-25% |
| Story-Cluster | 4 |
| Perfekte Enden | 4 (eines pro Cluster) |
