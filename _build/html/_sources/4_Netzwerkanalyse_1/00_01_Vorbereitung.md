
# Vorbereitung

Damit wir im ersten Teil von Netzwerkanalyse direkt loslegen können solltet ihr euch vorgängig mit QGIS vertraut machen. Dafür haben wir ein paar Übungen zusammengesetellt, die ihr als Vorbereitung auf Netzwerkanalyse I erledigen solltet.

```{admonition} Übungsziele
:class: attention
- QGIS herunterladen und Installieren
- QGIS starten und kennenlernen
- Modularer Aufbau von QGIS verstehen
- Plugins installieren und anwenden können
- Daten für Übungseinheit Netzwerkanalyse I vorbereiten
```

## Übung 1: QGIS installieren
Auf der QGIS Homepage [qgis.org](https://www.qgis.org/) finden Sie die aktuellen QGIS Versionen für Windows, Linux, Mac und weitere Betriebssysteme in 32 und 64 bit. Laden Sie den Standalone installer des "Longterm release (most stable)" QGIS Version herunter (aktuell 3.10), der für Ihre Architektur und Ihr Betriebssystem passt. Installieren Sie QGIS nach dem Download.


```{figure} figures/qgisVersion.jpg
:name: qgisVersion

QGIS Standalone Installer "Longterm release (most stable)" auf qgis.org
```
(chap-vorbereitung-aufstarten)=
## Übung 2: QGIS aufstarten
Nach der Installation starten Sie "QGIS Desktop 3.10.0 **with GRASS 7.8.0**". Der Zusatz "with GRASS" ist sehr wichtig, vor allem für die zukünftigen Aufgaben in Netzwerkanalyse I - III. Sollte den Link im Startmenü nicht verfügbar sein, können Sie die entsprechende exe-Datei auch an folgendem Ort finden: *C:\Program Files\QGIS 3.10\bin\qgis-bin-g7.exe*. Mit Rechtslick > an Startmenü anheften können Sie eine Verknüpfung mit der korrekten QGIS Version erstellen.

Wechseln Sie als erstes die Sprache des Userinterface auf Englisch _(Einstellungen -> Optionen -> Allgemein -> Benutzeroberflächenübersetzung)_.


```{figure} figures/qgisGrass.jpg
:width: 300px
:name: qgisgrass

Achtet beim Aufstarten unbedingt darauf, dass QGIS **mit GRASS** GIS gestartet wird
```

## Übung 3: Tutorials anschauen

Schauen Sie sich danach zum Einstieg einzelne Videos vom Youtube Nutzer [Marshal Mappers](https://www.youtube.com/channel/UCKwC9hcJr-4mgsNUeJzMAvA/videos) an. Erkunden Sie die Videos bis Sie die grundlegendsten Arbeitsschritte von QGIS (Daten importieren, Werkzeuge finden, Karte zu pdf exportieren) verstanden haben. Erstellen Sie dann ein neues Projekt (Projekt -> New) und speichern Sie dieses direkt ab (Projekt -> Save As..). Beachten Sie dazu die Empfehlungen zur Struktur (siehe {ref}`chap-netzwerk-einleitung`).

## Übung 4: Daten importieren

Während Shapefiles im GIS-Unterricht bisher oft verwendet wurden zur Speicherung von Vectordaten, werden in QGIS vor allem Geopackage Dateien verwendet (.gpkg). QGIS kann Shapefiles durchaus lesen und schreiben, wir werden in den Übungen aber gleichwohl v.a. mit Geopackage Daten arbeiten. Geopackages sind eine alternative Methode, Vektordaten abzuspeichern. Sie beheben einige Defizite, die Shapefiles mit sich bringen. Siehe dazu auch die Website ["Shapefiles must die"](http://switchfromshapefile.org/). 

PS: Twitternutzer können auch einen spannenden Schlagabtausch der Benutzer [@shapefile](https://twitter.com/shapefiIe) versus [@geopackage1](https://twitter.com/geopackage1) und [@sfkeller](https://twitter.com/sfkeller) mitverfolgen.

1. _Neues QGIS Projekt starten und Projektdatei speichern (Beachten Sie dazu die Empfehlungen am Anfang)_
2. _CRS auf EPSG 2056 setzen_
3. _Datensatz "Gemeinde_Waedenswil.gpkg" (siehe {numref}`table-datensaetze-netzwerkanalyse`) in QGIS Importieren_
4. _Symbologie folgendermassen ändern: Fläche transparent, Stadtgrenze schwarz_


(ex-network-plugins)=
## Übung 5: Plugin installieren

QGIS wird von zahlreichen Einzelpersonen und Gruppen entwickelt. Aus diesem Grund ist die Software Modular aufgebaut, und nur ein Teil wird der Standard-Installation mitgeliefert. Für einige Funktionen müssen Erweiterungen (sogenannte "Plugins"), zusätzlich installiert werden. Installieren Sie das Plugin "QuickOSM" um OpenStreetMap (OSM) Vektordaten rasch und einfach lokal abspeichern zu können.

1. Reiter Plugins -> Manage and Install Plugins
2. Im Suchfenster "QuickOSM" suchen
3. Plugin anwählen und auf "install" klicken

Die wichtigsten Metadaten zu allen Plugins werden auf plugins.qgis.org festgehalten. Dort findet man auch Links zur Projektseite, weiteren Dokumentation und ggf. Tutorials: Zu QuickOSM sind die Metadaten hier aufrufbar: [https://plugins.qgis.org/plugins/QuickOSM/](https://plugins.qgis.org/plugins/QuickOSM/)

(ex-network-osmdownload)=
## Übung 6: OpenStreetMap Vektordaten herunterladen

Mit dem neuen Plugin "QuickOSM" laden Sie nun den Strassendatensatz der Gemeinde Wädenswil herunter. Dies geschieht folgendermassen:

1. _Rechtsklick auf den Layer "Gemeinde_Waedenswil"_ -> _Zoom to layer_
2. _Reiter Vektor_ -> _Quick OSM_ -> _Quick OSM_
3. _Wählen Sie bei der Option key "highway" und lassen value leer_
4. _Wählen Sie Option "Extent of map canvas"_
5. _Klicken Sie anschliessend auf "Run query"_

Das Query lädt nebst den Liniendaten auch noch Punkt- und Polygon-Daten herunter. Diese interessieren uns nicht und können entfernt werden (Rechtsklick -> remove).


## Übung 7: Temporäre Datei abspeichern

Outputs werden in QGIS standardmässig in einem Temp-Folder abgelegt. Diese Dateien werden nach Beendigung von QGIS gelöscht. Um die Daten auch zu einem späteren Zeitpunkt verwenden zu können, müssen sie an einem geeigneten Ort abgespeichert werden. Führen Sie diesen Schritt mit den eben beschafften OSM Strassendaten (nur Linien) aus. Im gleichen Schritt können Sie alle unnötigen Spalten von der sehr grossen Attributtabelle loswerden.

1. _Rechtsklick auf den temporären Linien-Layer_ -> _Export_ -> _Save Features As..._
2. _Unter "Select fields to export and their export options" "Deselect All" ausführen._
3. _Format: Geopackage_
4. _Filename: Geeigneter Speicherort[^speicherort] aufsuchen und Datei abspeichern als "osm_highway.gpkg"_
    _(Erweiterung muss nochmals angegeben werden)_

[^speicherort]: Merken Sie sich den Speicherort, Sie werden das File in der kommenden Übung brauchen.


```{admonition} Merken Sie sich:
:class: note
- Es lohnt sich, vor jedem Projekt eine sinnvolle Ordnerstruktur aufzubauen
- Neben shapefile gibt es weitere (bessere?) Wege, wie Vektordaten abgespeichert werden
können. Eine gute Variante ist Geopackage.
- QGIS ist mittlerweile ein mächtiges Werkzeug, welches für die Bearbeitung vieler klassischer
GIS Fragestellungen geeignet ist
- QGIS ist modular aufgebaut, wichtige Funktionen sind über Plugins verfügbar. Dadurch kommt
QGIS nicht aus "einem Guss" daher
- Outputs werden in temporären Dateien abgespeichert, die bei der Schliessung von QGIS
gelöscht werden. Sollen Geodaten permanent verfügbar sein, müssen sie entsprechend explizit
abgespeichert werden.
```