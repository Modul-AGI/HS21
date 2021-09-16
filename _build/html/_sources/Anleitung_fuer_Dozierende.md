# Anleitung für Dozierende

Um Änderungen an diesem Dokument machen zu können, braucht man erstmal einen Github Account. Dieser ist gratis und kann hier erstellt werden: https://github.com/signup

Meldet nach der Erstellung euren Github Nutzername an Nils: Er wird euch auf dem Repository ("Repo") freischalten.

Danach könnt ihr bestehende Einträge zu verändern und auch neue Inhalte hinzufügen. Um inhalte zu verändern navigiert ihr auf der Webseite (modul-agi.github.io) zum entsprechenden Eintrag und klickt dort auf Github Logo oben rechts (Katzen-Symbol) > *Vorschlagen zum bearbeiten*. Nun könnt ihr eure Änderungen im Online Editor auf Github.com vornehmen. Anders als mit Word, arbeiten wir hier in einer Markup Sprache, d.h. wir programmieren quasi den Inhalt in einem Textfile.

### Text

- Kursiv: Wörter, die mit \* umgeben werden, sind Kursiv (also `*kursiv*` wird zu *kursiv*)
- Fett: Wörter die mit doppelten \* umgeben werden, sind Fett (also `**fett**` wird zu **fett**)
- Hyperlinks: Um einen hyperlink wird folgenermassen erstellt: `[angezeigter text](www.example.com)` (wird zu [angezeigter text](https://www.example.com))
- Überschriften: Überschriften werden mit vorangestelltem `#` erstellt (Unterkapitel mit `##`, `###` etc)


### Tabellen

Um eine Tabelle einzufügen muss man nachstehender Konvention folgen. 

````
```{list-table} Beschreibung der Tabelle (optional)
:header-rows: 1
:name: meinetabelle1

* - Title Spalte 1
  - Titel Spalte 2
* - Inhalt erste Zeile
  - und noch ein weiterer Inhalt
```
````

Dies sieht dann so aus:

```{list-table} Beschreibung der Tabelle (optional)
:header-rows: 1
:name: meinetabelle1

* - Title Spalte 1
  - Titel Spalte 2
* - Inhalt erste Zeile
  - und noch ein weiterer Inhalt
```

Hinweise: 

- Um einen Querverweis auf die obige Tabelle zu machen verwendet man folgende Konvention: ``{numref}`meinetabelle1` ``, dies wird dann in {numref}`meinetabelle1` konvertiert.
- `:name:` sollte dabei für jede Tabelle angepasst werden und eindeutig sein
- Diese sogenannten "Backticks" sind auf der Tastatur rechts neben dem Fragezeichen, dabei muss Schift gedrückt gehalten und mit einem Leerschlag abgeschlossen werden.

[^backticks]: 

### Bilder 

Um Bilder einzufügen muss man diese erstmals auf Github hochladen. Dafür wählt man auf Github.com den "Parent Folder" des Dokuments, wo das Bild hin soll und dort dann *Add file > Upload file*. Dann kann man das Bild auf zwei verschiedene Arten ins Dokument einfügen, je nach dem ob man Bildunterschriften / Querverweise braucht oder nicht.

#### Ohne Bildunterschrift und Querverweis

Wenn man das Bild ohne Bildunterschrift einfügen möchte ist das Einfügen sehr knackig und sehr ähnlich, wie wenn man URLs einfügt: `![](bild.jpg)`. Dabei ist der Pfad relativ zum Dokument zu verstehen.

#### Mit Bildunterschfit und allenfalls Querverweis

Um ein Bild mit Bildunterschfit einzufügen und auch die Möglichkeit zu haben, darauf zu verlinken (Querverweis), ist es etwas komplizierter und ähnlich wie bei Tabellen. Aauch hier sollte `:name:` für jede Abbildung angepasst werden und eindeutig sein:


````
```{figure} zhaw_lsfm_iunr_blau.jpg
:name: zhaw-logo

Logo der ZHAW
```
````

Wird dann zu:

```{figure} zhaw_lsfm_iunr_blau.jpg
:name: zhaw-logo

Logo der ZHAW
```

Genau wie auf Tabellen verweist man folgendermasssen auf Bilder im Text: ``{numref}`zhaw-logo` `` (dies wird dann zu {numref}`zhaw-logo`).


### Übungsziele

Um "Übungsziele" festzu legen verwendet man folgender Syntax:

````
```{admonition} Übungsziele
:class: attention
- Ziel 1
- Ziel 2
- Ziel 3
```
````

Dies wird dann zu:

```{admonition} Übungsziele
:class: attention
- Ziel 1
- Ziel 2
- Ziel 3
```
