# Aufgabe 3: Kürzeste Pfade (shortest path)

````{admonition} Achtung!
:class: tip

- Achten Sie darauf, dass Sie "QGIS Desktop 3.16.12" starten.
- Standartmässig werden Dateien als Temporäre Files abgespeichert, die nach dem Schliessen von QGIS gelöscht werden. Um einen Output an einem festgelegten Ort abzuspeichern muss der Output definieret werden. Dazu klickt man neben [Save to temporary file] auf die drei Punkte und wählt "Save to File" aus.

````

```{figure} figures/saveToTemp.jpg
:name: saveToTempFile
```
(ex-osm-background)=
## Übung 3.1: Projekt vorbereiten

Starten Sie "QGIS Desktop 3.16.12" und beginnen Sie ein neues Projekt mit dem CRS CH1903+ LV95 (EPSG 2056). Laden Sie den Datensatz "osm_highway_prepared.gpkg" von letzter Woche. Wer den Datensatz von letzter Woche nicht auffinden kann, findet die Datei in {numref}`table-datensaetze-netzwerkanalyse`. Prüfen Sie, ob das CRS richtig erkannt wurde (Rechtsklick -> Properties -> Reiter Source -> Set source coordinate reference system -> Hier sollte EPSG 2056 stehen).

Wir brauchen zudem eine Hintergrundkarte zur Orientierung. Blenden Sie diese mit dem Plugin "QuickMapServices" die Openstreetmap Hintergrundkarte ein (Web -> QuickMapServices -> OSM -> OSM Standard) ein. Falls Sie diese Option nicht finden, müssen Sie das enstprechede Plugin "QuickMapServices" installieren (siehe dazu {ref}`ex-network-plugins`).

Die Hintergrundkarte dient lediglich zur Orientierung, die Farbe lenkt uns jedoch vom Netzwerk ab. Wechseln Sie deshalb den Darstellungsmodus auf Graustufen mittels Rechtklick auf den Layer "OSM Standard" -> Properties -> Symbology -> Grayscale Auswahl: "By lightness".

(ex-shortestpath)=
## Übung 3.2: Kürzester Pfad berechnen

Nun können wir mittels "*Shortest path (point to point)*" (aus dem Toolset "Network analyses" den kürzesten Pfad zwischen zwei Knotenpunkten auf dem Netzwerk berechnen. Starten sie das Tool und wählen sie als Input Datensatz ("Vector Layer representing network") _osm_highway_prepared_ aus.

Die Start- und Endpunkte können Sie interaktiv in der Karte setzen. Klicken Sie dazu auf das Symbol neben den entsprechenden Feldern ("Start point" bzw. "End point") und klicken Sie in der Karte an den gewünschten Stellen. Führen Sie das Tool mit "Run" aus.

Visualisieren Sie nun den neuen Layer "Shortest Path" so, dass er gut ersichtlich ist.

**Hinweis:** Auch GRASS GIS bietet einen Shortest Path Algorithmus an (v.net.path). Dieser ist darauf ausgelegt, viele Kürzeste Pfade für viele Punkte zu berechnen, und nimmt als Input deshalb ein Textfile.

## Übung 3.3: Mit ORS Routing vergleichen

Nun wollen wir diese Route mit derjenigen eines professionellen Routing Services vergleichen. https://maps.openrouteservice.org/ bietet ihre Dienste bis zu einem bestimmten Kontingent kostenlos an. Installieren Sie das Plug-In "ORS Tools" um diesen Service zu nutzen.

Führen Sie das Tool nach der Installation via Web -> ORS Tools -> ORS Tools aus. Fügen Sie bei Settings ( ) ->  "API Key" folgenden Schlüssel ein: 5b3ce3597851110001cf6248435b5e715b1444afad6510cc04475d96

Über diesen Schlüssel wird sichergestellt, dass die Anzahl Abfragen pro Minute und Tag ein gewisses Maximum nicht überschreiten.

Geben Sie Start und Endpunkt mit der Maus ein (klick auf das +) und orientieren sich dabei an dem Layer "Shortest_Path" (aus der vorherigen Übung). Allenfalls verschwindet das "ORS Tools" Fenster, sie können es aber über die Toolbar (siehe {numref}`ORSrouting`) wieder aufrufen.

```{figure} figures/osm.jpg
:name: ORSrouting

Mit klick auf dieses Symbol erscheint ORS Routing wieder
```

Führen Sie die Berechnung mit "Apply" aus und vergleichen den resultierenden Pfad mit "Shortest Path" aus {ref}`ex-shortestpath`. Führen Sie die gleiche Berechnung mit verschiedenen Einstellungen durch (kürzeste Route, schnellste Route, Fahrrad, zu Fuss). Vergleichen Sie die unterschiedlichen Routen mit unserer eigenen Berechnung und visualisieren Sie diese in einer Karte.

Berechnen Sie nun mit OSM Routing den kürzesten Pfad zwischen Campus Grüental und Campus Reidbach, auch wieder je einmal mit der Verkehrsmodalität Auto, Fahrrad und Fussweg. Vergleichen Sie die drei Resultate.

:::{note}
Das `ORS Tools Plugin` bietet keine Möglichkeit, die blauen Linien zu entfernen, die die ausgewählten Punkte auf der Karte verbinden (https://github.com/GIScience/orstools-qgis-plugin/issues/120). Diese Linien sind temporär, d.h. sie werden beim nächsten Öffnen des QGIS-Projekts wieder verschwinden. Wenn Sie also Ihr Projekt neu starten, werden sie verschwinden.
:::