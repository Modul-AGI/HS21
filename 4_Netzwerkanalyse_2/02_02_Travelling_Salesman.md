# Aufgabe 4: Traveling Salesman

Das Problem des Handlungsreisenden (engl. Traveling Salesman Problem) ist ein kombinatorisches Optimierungsproblem, in dem die Aufgabe darin besteht, eine Reihenfolge für den Besuch mehrerer Orte so zu wählen, dass keine Station außer der ersten mehr als einmal besucht wird, die gesamte Reisestrecke des Handlungsreisenden möglichst kurz und die erste Station gleich der letzten Station ist. 

## Übung 4.1: Traveling Salesman für Campus Standorte

Angenommen Sie sind ein Kurrierdienst und müssen ausgehend von der Halbinsel Au aus alle Campus Standorte der ZHAW Wädenswil besuchen. Sie wollen die Route so optimieren, dass Sie die kürzeste Route Sie das gleichnamige Tool (v.net.salesmen) um genau dieses Problem zu lösen.

1. Erstellen Sie dazu als erstes eine neue Geopackage Datei (Layer -> Create Layer -> New Geopackage Layer) um die Campus Standorte zu erfassen
    - Mit dem Feld "Database" ist der Pfad inkl. Dateiname der zu erstellenden Datei gemeint. Wählen Sie hier an einem geeigneten Speicherort den Dateiname "campus_waedenswil.gpkg"
    - "Table name" ist der Name des Layers innerhalb der Geopackage Datei (im Gegensatz zu einem Shapefile können innerhalb eines Geopackage mehrere Layers von unterschiedlichen Datentypen Coexistieren)  
    - Wählen Sie bei "Geometry Type" "Point" aus und bei CRS EPSG 2056
    - Fügen Sie eine Spalte in der Attributtabelle hinzu indem Sie unter "New field" -> "Name" den Wert "Standort_name" eingeben (Hier wollen wir "Grüental", "Reidbach".. erfassen) Wählen Sie einen geeigneten Datentyp sowie eine geeignete Maximallänge
    - Bestätigen Sie mittels "Add field to list"
    - Erstellen Sie das Geopackage mit "OK"  
2. Starten Sie mit einem Klick auf **den Stift** die Editiersession und fügen Sie Features hinzu mit dem "Add Feature" Werkzeug. Digitalisieren Sie so die Campus Standorte (Grüental, Reidbach, Seifenstreuli, Schloss) sowie den Ausgangspunkt (Halbinsel Au). Wählen Sie pro Standort einen für Sie geeigneten Punkt, möglichst auf dem OSM Strassennetz.
3. Speichern Sie die erfassten Punkte mit einem Klick auf "Save Edits".
4. Starten Sie nun das Tool v.net.salesman (über die Processing Toolbox) und wählen als Input Layer den OSM Strassendatensatz und als "Center Point Layer" die eben digitalisierten Standorte.
5. v.out.ogr output type: auto.
6. Betrachen Sie die Output daten.

(ex-network-traveling-shops)=
## Übung 4.2: Traveling Salesman für mehr Standorte

Der Traveling-Salesman-Pfad für fünf Punkte zu berechnen ist relativ trivial und könnte "von Hand" gerechnet werden. Anspruchsvoller wird es jedoch, wenn sich die Anzahl der Standorte erhöht. Nehmen wir an, Sie wollen eine Einkaufstour durch alle Läden in Wädenswil machen: Nutzen Sie die OSM Daten und v.net.salesman und eine sinnvolle Route zu berechnen.  

1. OSM Daten der Läden laden: Vector -> QuickOSM -> QuickOSM
2. key "shop" -> Run query sowie Gebiet wählen (siehe dazu {ref}`ex-network-osmdownload`)
3. Punkt-Daten der Shops in CRS 2056 konvertieren (reproject, siehe {ref}`ex-network-transfrom`). Clippen ist fakultativ (nicht erreichbare Knotenpunkte werden schlicht ignoriert)
4. v.net.salesman mit diesen Standorten durchführen

(ex-network-traveling-buildings)=
## Übung 4.3 (fakultativ, Guezli-Challenge): Traveling Salesman für noch mehr Standorte

Um unsere Rechenmaschine richtig herauszufordern, können wir den Traveling Salesmen Pfad für alle Gebäudestandorte in Wädenswil berechnen. Nutzen Sie hierzu QuickOSM um "building" herrunterzuladen. Reprojizieren Sie die Polygon-Daten in CRS 2056 und konvertieren Sie diese in Punkte, indem Sie das Centroid pro Polygon berechnen (Tool "Polygon Centroids"). Berechnen Sie anschliessend den Traveling Salesman. Ermitteln Sie die Gesamtdistanz dieses Pfades, indem Sie mit dem Field Calculator die Länge pro Segment rechnen (length) und anschliessend die Summe aller Längen ermitteln (View -> Panels -> Statistic). **Wer zuerst die korrekte Distanz in den Chat schreibt, wird mit Ruhm und Ehre belohnt und zur/zum "AGI Studentin/Student des Tages" erkürt!**

```{note}
- Für viele klassische Fragestellungen (z.B. shortest path, traveling salesmen) bietet QGIS / GRASS 
 einen passenden Algorithmus
 - Die Tools werden teilweise sehr unterschiedlich angesprochen (shortest path braucht Textfiles,
 Traveling salesmen braucht Punkt-Features) und liefern unterschiedliche Outputs
```

