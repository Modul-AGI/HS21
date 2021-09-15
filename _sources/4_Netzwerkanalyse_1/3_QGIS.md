# Aufgabe 1: Operationen mit QGIS

Starten Sie "QGIS 3. 10 .0 with GRASS GIS 7. 8 .1", beginnen Sie ein neues QGIS Projekt und speichern dies an einem geeigneten Ort (siehe Vorbereitungsübungen) ab. Weisen Sie dem Projekt das Koordinatensystem EPSG 2056 zu und importieren die Gemeindegrenze sowie die OSM Strassendaten aus der Vorbereitungsübung (siehe {numref}`table-datensaetze-netzwerkanalyse`).

````{admonition} Achtung!
:class: tip

Achten Sie darauf, dass Sie "QGIS Desktop 3.10.0 **with GRASS 7.8.0**" starten, ansonsten stehen ihnen die GRASS Erweiterungen nicht zur Verfügung (siehe {ref}`chap-vorbereitung-aufstarten`).

````

(ex-network-transfrom)=
## Übung 1.1: Daten Transformieren

Die OSM Daten sind aktuell noch im Koordinatensystem WGS84 (EPSG 4326). Die Gemeindegrenze hingegen ist mit den neuen Schweizer Landeskoordinaten CH1903+ LV95 (EPSG 2056) abgespeichert. Wir wollen in unserer Analyse mit CH1903+ LV95 (EPSG 2056) arbeiten. Transformieren Sie dazu den Strassendatensatz in das Koordinatensystem CH1903+ LV95 (EPSG 2056). Nutzen Sie dazu das Tool "Reproject Layer". **Wichtig**: Speichern Sie den Transformierten Strassendatensatz *in einer neuen Datei* (siehe {numref}`saveToFile`)

```{figure} figures/ueb1_fig1.jpg
:name: qgistools

Viele wichtige Tools lassen sich über den Menü Bar aufrufen (v.a. "Vector" und "Raster"). Die Tools lassen sich auch relativ rasch mit der Suchfunktion der "Processing Toolbox" finden.
```




```{figure} figures/saveTo.jpg
:name: saveToFile

Speichern Sie den neuen Strassendatensatz in einer *neuen* Datei, nicht als temporärer Layer. Normalerweise spielt dies keine Rolle, doch im Falle von "reproject" entsteht beim Speichern als temporärer Layer ein Fehler.
```
(ex-clip)=
## Übung 1.2: Daten Clippen

Zoomen sie auf die Gemeindegrenze (Layers Panel -> Rechtsklick auf Datensatz -> Zoom to layer"). Es ist ersichtlich, dass die Strassendaten über die Gemeindegrenze hinaus verlaufen. Wir möchten für die kommenden Übungen nur die Strassen, die _innerhalb_ der Gemeinde Wädenswil liegen. Dazu müssen wir das Strassennetz mit der Gemeindegrenze verschneiden ("clip"). Führen Sie das gleichnamige Werkzeug mit dem Input Layer "OSM_highway" und dem Clip Layer "Stadt_ Waedenswil.gpkg" aus. Speichern Sie die Ausgabe in einer neuen Datei. 

Es gibt eine ganze Reihe Werkzeuge zum Begriff "clip". Entscheiden Sie selbst, welches für diese Fragestellung geeignet ist.