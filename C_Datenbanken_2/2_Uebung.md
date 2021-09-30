# Übungen 

## Datenintegrität 1

### Übung 1: Datenintegrität und Konsistenz

Sie haben den Auftrag ein Datenmodell zur Speicherung von unterschiedlichen Sozialen Schlüssel-Indikatoren für schweizerische Gemeinden zu überprüfen. Hierbei werden jedes Jahr Datenwerte auf Basis einer Gemeinde erhoben. Diese sollen später in der Datenbank gespeichert und ausgewertet werden können. Wichtig hierbei ist, dass die Daten später in einer Karte visualisiert werden können. Deshalb ist es notwendig, dass Gemeinde-Geometrien ebenfalls in der Datenbank gespeichert werden sollen. Ebenfalls ist es sinnvoll bestimmte Indikatoren auch für den gesamten Kanton hochzurechnen und als Karte darzustellen zu können.
Sie bekommen als erste Grundlage folgendes Datenbankmodell vom Auftraggeber gestellt. Leider gibt es in diesem Modell ein paar Konsistenzfehler.

![](figures/Übung_Datenbanken2.jpg)

Untersuchen Sie das Datenmodell auf Konsistenzfehler und Korrigieren Sie diese. Lesen Sie den Aufgabentext aufmerksam und schauen sich die Abbildung an und entwickeln Sie daraus ein passendes logisches Datenmodell, welches alle Regeln der Datenintegrität einhält. Es muss nicht perfekt sein. Es geht in dieser Übung darum etwas Erfahrung im Lesen von gegebenen Modellen zu bekommen.

## Arbeiten mit Server Datenbanken in ArcGIS Pro und pgAdmin 2

### Übung 2: Datenbankverbindung zum Server in pgAdmin herstellen

In den nächsten Übungen wollen wir eine Beispiel Datenbank mit dem dort bereits implementierten Datenbankmodell abfragen. Hierzu müssen wir in einem ersten Schritt eine Verbindung zum PostgreSQL/PostGIS Datenbankserver herstellen. Hierfür nutzen wir das Datenbank-Administrations-Werkzeug pgAdmin.

1. Starten Sie pgAdmin.
2. Im Dashboard klicken Sie auf NEW Server und geben die folgenden Verbindungsparameter ein:
3. Register General: Name: svma-s-01323_waelder_studentNr. Verwenden Sie dabei die Nr. Ihres zugewiesenen Benutzers (siehe {numref}`figure-pgadmin1`)
4. Register Connection  (siehe {numref}`figure-pgadmin2`):
    - Host name/address: svma-s-01323.zhaw.ch
    - Port: 5432
    - Maintenance database: waelder
    - Username: studentNr (Verwenden Sie hier Ihren zugewiesenen Anmeldenamen)
    - Passwort: (Verwenden Sie hier Ihr zugewiesenes Passwort)
5. Alle anderen Einstellungen können belassen werden. Speichern Sie mit Klick auf Save.
6. Lassen Sie sich nicht davon verunsichern, dass es bereits einige Einträge hat. Da auf dem Server bereits andere Datenbanken installiert sind, sehen Sie auch diese. Navigieren Sie zu unserer Datenbank "waelder" und verschaffen sich einen Überblick über die vorhandenen Tabellen.
7. Verwenden Sie für alle folgenden Übungen diese Datenbankverbindung, wenn nichts anderes angegeben  (siehe {numref}`figure-pgadmin3`).

![](figures/screenshot_pgadmin.jpg)

![](figures/screenshot_pgadmin2.jpg)

![](figures/screenshot_pgadmin2.jpg)

### Übung 3: Verbindung zur PostgreSQL/PostGIS Datenbank mit ArcGIS Pro herstellen

Nachdem die Datenbank erstellt wurde und eine Verbindung über pgadmin eingerichtet wurde, benötigen wir auch eine Verbindung von ArcGIS Pro zu der Datenbank.

1. Starten Sie ArcGIS Pro und erstellen ein neues Projekt mit dem Namen "Datenbankzugriff"
2. Öffnen Sie das Catalog-Fenster oder das Register Catalog und wählen Sie "Databases" (siehe {numref}`figure-connect1`)
3. Im Kontextmenü (rechte Maustaste) kann eine neue Datenbankverbindung zur Server Datenbank hergestellt werden  (siehe {numref}`figure-connect2`).
    - Databases -> Kontextmenü -> New Database Connection
4. Geben Sie im Database Connection Fenster die notwendigen Verbindungsparameter ein  (siehe {numref}`figure-connect3`).
    - Database Platform: PostgreSQL
    - Instance: svma-s-01323.zhaw.ch
    - Authentication Type: Database authentication
    - User Name: studentNr (Verwenden Sie hier Ihren zugewiesenen Anmeldenamen)
    - Password: (Verwenden Sie hier Ihr zugewiesenes Passwort)
    - Database: waelder
5. Ein Klick auf OK stellt die Verbindung zur Datenbank her.
6. Sie können der Datenbankverbindung noch einen sinnvollen Namen geben. Es empfiehlt sich eine Kombination aus dem Servernamen, der verbundenen Datenbank und dem Benutzer. Z.B. "svma-s-01323_waelder_student1"
7. Unter dem Eintrag "Databases" im Catalog gibt es jetzt eine neue Datenbankverbindung zur Datenbank  (siehe {numref}`figure-connect4`).

![](figures/screenshot_connect1.jpg)

![](figures/screenshot_connect2.jpg)

![](figures/screenshot_connect3.jpg)

![](figures/screenshot_connect4.jpg)

### Übung 4: Datenbank Schemata für ArcGIS Pro Benutzer

Nachdem die Datenbank erstellt wurde und alle Verbindungen eingerichtet sind, ist die Datenbank startklar. ArcGIS pro nutzt für die Daten jeweils ein eigenes Schema. Das Schema hat dabei den Namen des Datenbank Admin Users.

1. Starten Sie pgAdmin
2. Stellen Sie wieder die Verbindung mit der Datenbank "waelder" her und öffnen Sie die Eigenschaften mit Klick auf das kleine Plus-Zeichen.
3. Navigieren Sie zum Eintrag Schemas. Dort sind 4 Einträge zu sehen. Ein Schema ist eine Art abgeschlossener Namensraum für die Datenhaltung. Es empfiehlt sich thematisch zusammenpassende Tabellen in einem gemeinsamen Schema zu speichern. Für die meisten Datenbank-Anwendungen genügt es aber alle Tabellen im default Schema "public" zu erstellen. Für den Zugriff über ArcGIS wurde aber durch das Werkzeug "Create Database User" ein spezielles Schema mit dem Namen des Database Users erstellt. Dies ist notwendig damit auch ArcGIS Pro auf die Daten zugreifen und diese verwalten kann. Das entsprechende Schema bekommt dabei immer den Namen des Admin Datenbankbenutzers. In diesem Fall "arcgispro_editor". Sie können dort z.B. auch ein Schema mit Namen "sde" vom Geodatenbank-Administrator sehen (siehe {numref}`figure-uebung4-1`).
4. Öffnen Sie das public Schema. Hier gibt es bereits Einträge. Hier werden die zugehörigen Informationen der Datenbank, wie Sichten, Funktionen usw. zugänglich gemacht. Interessant ist zunächst aber nur der Eintrag "Tables (3)". In Klammern ist immer die Anzahl der vorhandenen Datenbanktabellen angegeben. Wie wir sehen gibt es default-Tabellen, welche bereits erstellt wurden. Die Tabelle "spatial_ref_sys" enthält z.B. alle Koordinatensysteme. Die Tabelle "sde_spatial_references" ist eine Hilfstabelle für Koordinatensysteme von ArcGIS Pro. Löschen Sie diese beiden Tabellen NIEMALS. Ohne diese Tabellen sind bestimmte Funktionen nicht mehr ausführbar.  (siehe {numref}`figure-uebung4-2`)
5. Hinweis, falls Sie einmal selber Tabellen erstellen sollten: Es empfiehlt sich alle räumlichen Tabellen direkt in ArcGIS Pro zu erstellen. Dadurch entscheidet ArcGIS Pro selbstständig über die korrekten Datentypen und Geometrietypen. Alle anderen Tabellen sowie Fremdschlüssel usw. können auch in pgadmin erstellt werden. Alle Tabellen wurden im ArcGIS Pro Schema "arcgispro_editor" erstellt.

![](figures/screenshot_uebung4_1.jpg)

![](figures/screenshot_uebung4_2.jpg)

### Übung 5: Datenbankschema prüfen

Für die kommenden Übungen nutzen wir die Datenbank "waelder" auf unserem Server. Den Zugriff haben wir in den vorigen Übungen eingerichtet. Um einen Überblick zu bekommen, lesen Sie das folgende Datenbankschema und machen sich mit den Tabellen, Attributen und Abhängigkeiten vertraut. Da Sie jetzt alle gemeinsam dieselben Tabellen bearbeiten, gibt es in jeder Tabelle jeweils ein Feld "id_erfasser". Sobald Sie Tabellen mit Daten befüllen, schreiben Sie bitte immer jeweils Ihre studentNr in das Feld "id_erfasser", damit die Einträge später unterscheidbar sind.

![](figures/screenshot_uebung5.jpg)

### Übung 6: Datenimport in die Datenbank über pgAdmin

Da jetzt alle Tabellen vorliegen sollen diese noch mit ein paar Beispiel-Daten gefüllt werden. Auch hier bietet es sich an räumliche Objekte (Geometrien) mit Hilfe von ArcGIS Pro zu erfassen. Nicht-räumliche Objekte können meist sogar schneller über SQL importiert werden.

1. Starten Sie pgAdmin und verbinden mit der Datenbank "waelder" im schema "arcgispro_editor".
2. Öffnen Sie anschliessend den SQL Editor von pgadmin. Sie finden das so genannte Query Tool im Kontextmenü des Schemas oder in der Menüleiste oben unter Tools -> Query Tool
3. Importieren Sie mit Hilfe eines SQL Statements eine Tierart in die Tabelle "tierarten".
4. Da Sie jetzt alle gemeinsam und gleichzeitig Daten in dieselbe Tabelle einfüllen und Sie die Einträge noch unterscheiden wollen, fügen Sie unter id_erfasser jeweils ihre zugewiesene studentNr ein.
5. Benutzen Sie dazu das INSERT Statement und tippen es in das Query Tool (siehe {numref}`figure-uebung6-1`)
    - INSERT INTO arcgispro_editor.tierarten (id_tierart,name_tierart,id_erfasser) Values (DEFAULT,’Bär’, studentNr);
    - Hinweis: DEFAULT ist ein SQL Befehlswort, welches den Zähler für die id_tierart automatisch auf den nächsten freien Wert setzt. So kann die id_tierart automatisch fortlaufend hochnummeriert werden. Sie dürfen natürlich irgendein Tier in die Datenbank einfüllen.
    - Schliessen Sie die Eingabe mit Klick auf Execute (kleiner Blitz) ab.
6. HINWEIS: Achten Sie darauf, dass Text immer in einfache Anführungszeichen (Das Zeichen auf der ?-Taste) gesetzt werden muss. Beachten Sie ausserdem die Punktschreibweise, dabei muss der Name des Schemas "arcgispro_editor" immer mit Punkt verbunden vor dem Namen der Tabelle angegeben werden. Jedes Statement wird mit Semikolon abgeschlossen.
7. Lassen Sie sich den Inhalt der Tabelle ausgeben. Dies können Sie über ein SELECT SQL Statement ausführen (siehe {numref}`figure-uebung6-2`).
    - ```SQL 
      SELECT * FROM arcgispro_editor.tierarten;
      ```
8. Sie können erkennen, dass ihr Tier mit Ihrer studentNr als id_erfasser in die Tabelle eingetragen wurde. Vermutlich sehen Sie auch bereits Einträge Ihrer Mit-Studierenden.
9. Navigieren Sie im Browser von pgAdmin zur Tabelle "tierarten".
10. Über das Kontextmenü können ebenfalls die Inhalte der Tabelle angezeigt werden  (siehe {numref}`figure-uebung6-3`).
11. Es öffnet sich automatisch das Query Tool und die Inhalte der Tabelle werden angezeigt. HINWEIS: Auf diese Weise kann immer nur die komplette Tabelle angezeigt werden. Filter oder sonstige Einschränkungen müssen als SQL Statement abgesetzt werden.

![](figures/screenshot_uebung6_1.jpg)

![](figures/screenshot_uebung6_2.jpg)

![](figures/screenshot_uebung6_3.jpg)

### Übung 7: Datenimport in die Datenbank mit einer SQL-Datei

Jedes SQL Statement kann in einer Datei abgespeichert werden. Dadurch lassen sich bequem z.B. gleich mehrere Daten in die Datenbank einlesen.
1. Starten Sie pgAdmin und verbinden mit der Datenbank "waelder" im schema "arcgispro_editor".
2. Öffnen Sie das Query Tool.
3. Laden Sie die Datei "tierarten.sql" [aus dem Moodle](https://moodle.zhaw.ch/mod/resource/view.php?id=1273633) und speichern Sie in Ihrem Ordner.
4. Öffnen Sie die Datei in einem beliebigen Texteditor und ändern das Wort "studentNr" in Ihre studentNr ab. Denken Sie sich ausserdem ein paar andere Tierarten aus und schreiben diese ebenfalls in die Datei (siehe {numref}`figure-uebung7-1`). 
5. Über das kleine Ordner Symbol (Im Menü des Query Tools links oben) kann eine SQL-Datei geladen werden. Laden Sie die geänderte "tierarten.sql" Datei in pgAdmin  (siehe {numref}`figure-uebung7-2`).
6. Select lädt den Inhalt der Datei ins Query Tool  (siehe {numref}`figure-uebung7-3`).
7. Schliessen Sie die Eingabe mit Klick auf Execute (kleiner Blitz) ab.
8. Schauen Sie sich erneut den Inhalt der Tabelle "tierarten" an. Die Tabelle sollte jetzt die eigenen Tierarten plus ein paar Einträge Ihrer Mit-Studierenden enthalten.

![](figures/screenshot_uebung7_1.jpg)

![](figures/screenshot_uebung7_2.jpg)

![](figures/screenshot_uebung7_3.jpg)

### Übung 8: Geometrieimport in die Datenbank

Herkömmliche GIS Methoden zum Erstellen und Importieren von Geometrien ins GIS sollten Ihnen aus dem GIS Basic Modul bereits bekannt sein. Auch in ArcGIS Pro können natürlich Geometrien z.B. über ein Shapefile in eine Geodatenbank importiert werden. Ausserdem können Geometrien z.B. aus einem Luftbild digitalisiert und direkt in der Geodatenbank gespeichert werden.

1. Laden Sie die Datei "waelder.zip" [aus dem Moodle](https://moodle.zhaw.ch/mod/resource/view.php?id=1273635) und entpacken Sie die Dateien. Es handelt sich um ein Shapefile mit einigen Wäldern.
2. Starten Sie ArcGIS Pro und laden das Projekt "Datenbankzugriff".
3. Fügen Sie das Shapefile ein und erfassen Sie mit dem Digitalisierungsmöglichkeiten von ArcGIS Pro zusätzlich ein paar eigene fehlende Wälder.
4. Öffnen Sie die Attributtabelle.
5. Erfassen Sie im Feld "id_erfasser" wiederum Ihre zugewiesene studentNr (Nur die Zahl). Alle weiteren Attribute können Sie beliebig erfassen. Denken Sie sich einfach etwas aus.
6. Importieren Sie die Daten anschliessend folgendermassen in die Feature Class "waelder" in der Datenbank auf dem Server.
7. Kontextmenü der Feature Class "waelder" -> Load Data (siehe {numref}`figure-uebung8-1`)
    - Input Dataset: Shapefile “waelder”
    - Target Dataset: waelder.arcgispro_editor.waelder
    - Schema Type: Use the Field Map to reconcile schema differences (Shapefiles können nur Spaltenbezeichnungen mit 10 Zeichen speichern. Alles andere wird abgeschnitten. Das Attribut "beschreibung" ist deshalb in der Datenbank als "beschreibung" gespeichert, im Shapefile aber nur als "beschreibu". Dies hat zur Folge, dass das Schema beider Feature Classes nicht gleich ist. Aus diesem Grund muss hier explizit die Übereinstimmung der Spalten bestimmt werden. Das gleiche gilt für das Feld "id_erfasser" bzw. "id_erfasse".
8. Erstellen Sie eine neue Karte in ArcGIS Pro und laden Sie die Feature Class "waelder" aus der Server Datenbank.
9. Sie haben jetzt die Wälder in die Datenbank importiert.
10. Schauen Sie sich die Wälder auch in pgAdmin an. Machen Sie hierzu eine Select Abfrage im Query Tool. In der Ergebnis Tabelle sehen Sie in der Geometry-Spalte ein kleines Augen-Symbol. Dies öffnet den "Geometry Viewer". Sie sollten auch dort die Geometrien der importierten Wälder sehen.

![](figures/screenshot_uebung8_1.jpg)

![](figures/screenshot_uebung8_2.jpg)

![](figures/screenshot_uebung8_3.jpg)

## Versionierung und Mehrbenutzerbetrieb in ArcGIS Pro 18