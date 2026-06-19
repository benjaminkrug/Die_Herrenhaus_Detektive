# KDP-Upload — Schritt-für-Schritt-Anleitung (Band 3: Die zweite Quelle)

> Alle Werte sind fertig zum Kopieren. Quelle: `KDP_Metadaten_Band3.md`.
> Reihenfolge folgt dem echten KDP-Workflow. Hake jeden Schritt ab.

---

## Vorbereitung (vor dem Login)

- [ ] **Manuskript** bereit: `Band_3/Linear/Manuskript.docx` (6×9, ~21.157 Wörter)
- [ ] **Cover** bereit: `Band_3/Cover/cover_vorderseite_1.png` (E-Book) bzw. Full-Cover-PDF (Druck)
- [ ] Entscheide: Veröffentlichst du **E-Book (Kindle)**, **Taschenbuch (Print)** oder **beides**?
      → Empfehlung wie Band 1/2: **beides** (zwei getrennte KDP-Einträge, gleiche Metadaten).

---

## TEIL A — Kindle E-Book

### Schritt 1: Neues Kindle-eBook anlegen
- [ ] KDP → „Bookshelf" → **+ Create** → **Kindle eBook**.

### Schritt 2: Sprache, Titel, Untertitel
- [ ] **Sprache:** Deutsch
- [ ] **Buchtitel** (Titelfeld, 52 Zeichen):
      ```
      Die Herrenhaus-Detektive – Band 3: Die zweite Quelle
      ```
- [ ] **Untertitel** (132 Zeichen):
      ```
      Detektiv-Krimi für Kinder ab 8 | Kurze Kapitel, große Spannung im verbotenen Wald – mit Geheimnis, Mut, Freundschaft und Schatzsuche
      ```

### Schritt 3: Reihe (Series)
- [ ] **Series-Name:** `Die Herrenhaus-Detektive`
- [ ] **Reihen-Nummer:** `3`
      → Wichtig: exakt gleicher Series-Name wie Band 1/2, sonst werden sie nicht gruppiert.

### Schritt 4: Autor
- [ ] **Verfasser:** Vorname `Benjamin`, Nachname `Krug`
      → exakt wie Band 1/2 (sonst getrennte Autorenseiten).

### Schritt 5: Beschreibung
- [ ] **Buchbeschreibung** einfügen (Text aus `KDP_Metadaten_Band3.md` Abschnitt 4).
      → Tipp: KDP erlaubt einfaches HTML (fett, Listen). Den **fetten Hook** und die
      **Bullet-Listen** als HTML formatieren (oder im KDP-Editor die B/Listen-Buttons nutzen).
- [ ] OFFENE ENTSCHEIDUNG: Soll der Satz „auch einzeln lesbar" rein? (siehe Metadaten-Datei).

### Schritt 6: Verlag / Rechte / Keywords
- [ ] **Verlag (optional):** leer lassen oder wie Band 1/2.
- [ ] **Veröffentlichungsrechte:** „Ich besitze die Urheberrechte …"
- [ ] **7 Keywords** (je ein Feld) — exakt diese, alle ≤50 Zeichen:
      1. `kinderkrimi ab 8 kurze kapitel lesemuffel`
      2. `detektivgeschichte kinder ab 8 spannend grusel`
      3. `spannende bücher für kinder ab 10 zum selberlesen`
      4. `kinderroman 8 9 10 jahre jungen mädchen abenteuer`
      5. `geschenk junge mädchen 8 9 10 jahre buch`
      6. `detektiv buch kinder rätsel geheimnis schatz`
      7. `kinderbuch wald abenteuer mut freundschaft`

### Schritt 7: Kategorien (bis zu 3)
- [ ] Exakt die Band-2-Kombination wählen:
      1. `Kinderbücher › Detektiv- & Kriminalgeschichten`
      2. `Kinderbücher › Heranwachsen & Soziales Umfeld › Freundschaft & Schule › Freundschaft`
      3. `Kinderbücher › Belletristik › Bücher mit Kapiteleinteilung & Lesebücher › Erstes Lesealter`

### Schritt 8: Altersempfehlung
- [ ] **Alter:** von `8` bis `10` (bzw. 8+ wie Band 1/2 eingestellt).

### Schritt 9: Manuskript & Cover hochladen
- [ ] **Manuskript:** `Manuskript.docx` hochladen → Online-Vorschau prüfen
      (Kapitel-Umbrüche, Inhaltsverzeichnis-Links klicken, Sonderzeichen ä/ö/ü checken).
- [ ] **Cover:** E-Book-Cover (Vorderseite) hochladen.
- [ ] **ISBN:** Für E-Book NICHT nötig (Amazon vergibt ASIN automatisch).

### Schritt 10: Preis & Veröffentlichung
- [ ] **KDP Select** (optional): wie bei Band 1/2 entscheiden.
- [ ] **Preis:** wie Band 1/2 (Reihen-Konsistenz). Marktplatz: Amazon.de primär.
- [ ] **Veröffentlichen** klicken → 24–72 h Prüfung.

---

## TEIL B — Taschenbuch (Print)  ⚠️ braucht den Buchrücken

> Erst NACH der finalen Seitenzahl machen. Beim Print-Setup zeigt KDP dir die echte Seitenzahl —
> DIESE Zahl in `resize_cover_kdp.py` eintragen und den Buchrücken final bauen.

### Schritt 1: Paperback anlegen
- [ ] Bei Band 3 auf der Bookshelf → **+ Create** → **Paperback**
      (oder beim E-Book „Create Paperback" wählen → übernimmt Titel/Beschreibung).

### Schritt 2–8: Metadaten
- [ ] Identisch zu Teil A (Titel, Untertitel, Reihe, Autor, Beschreibung, 7 Keywords, Kategorien).

### Schritt 9: Print-Optionen
- [ ] **ISBN:** kostenlose KDP-ISBN zuweisen lassen → **diese ISBN dann ins Impressum**
      (`create_manuscript.py`, Platzhalter „(wird vergeben)" ersetzen) → Manuskript NEU generieren.
- [ ] **Format:** 6×9 Zoll (15,24 × 22,86 cm), weißes Papier.
- [ ] **Manuskript:** das Print-`Manuskript.docx` hochladen.

### Schritt 10: Cover (Full-Cover-PDF)
- [ ] KDP zeigt jetzt die **finale Seitenzahl** an → notieren.
- [ ] In `Band_2/Cover/resize_cover_kdp.py` Kopie für Band 3: `PAGE_COUNT` = diese Seitenzahl.
- [ ] Full-Cover bauen (Vorderseite + Rücken + Rückseite). Rückenbreite = Seitenzahl × 0,002252 Zoll.
- [ ] Full-Cover-PDF hochladen → KDP-Vorschau prüfen (Rücken-Text mittig? Barcode-Feld frei?).

### Schritt 11: Preis & Veröffentlichung
- [ ] Druckkosten beachten (KDP zeigt Mindestpreis). Preis wie Band 1/2-Logik.
- [ ] **Veröffentlichen** → Prüfung.

---

## NACH der Veröffentlichung

- [ ] **Reihe prüfen:** Stehen Band 1, 2, 3 auf einer Serienseite zusammen? (sonst Series-Name checken)
- [ ] **A+ Content** hinzufügen (Vorlage `_Gemeinsam/A_Plus_Content_Konzept.md`) — Cross-Selling Band 1→2→3.
- [ ] **PPC-Kampagnen** aufsetzen (eigene Keyword-Datei, analog Band-1-`keyword_liste.md`).
- [ ] Nach 2–4 Wochen: KDP-Reports prüfen (welche Kategorie bringt Badge? welche Keywords ranken?).

---

## Offene Punkte, die du noch entscheiden/liefern musst

1. **„Einzeln lesbar"-Satz** in der Beschreibung: rein (Mittelweg) oder raus?
2. **Preis** für Band 3 (E-Book + Print) — an Band 1/2 anlehnen.
3. **ISBN** (nur Print) — beim Upload von KDP zuweisen lassen, dann ins Impressum.
4. **Finale Seitenzahl** (nur Print) — von KDP beim Upload, dann Buchrücken bauen.
