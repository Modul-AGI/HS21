(chap-netzwerk-iii)=
# Netzwerkanalyse III


Angenommen Sie sind auf Wohnungssuche in Wädenswil. Dabei gilt es nebst dem Budget viele wichtige raumgebundene Variablen zu berücksichtigen, dazu verwenden Sie natürlich QGIS. Sie wollen drei Kriterien untersuchen:

1. Laufdistanz zur nächsten Entsorgungsstelle
2. Erschliessung an die öffentlichen Verkehrsmittel (unter Berücksichtigung des Fahrplans)
3. Distanz zur Durchfahrtsstrasse

Wir werden für jeden dieser drei Kriterien einen Rasterdatensatz kreieren, den wir zum Schluss miteinander verrechnen können. So finden wir den Optimalen Standort unter der Berücksichtigung aller drei Kriterien. Starten Sie dazu QGIS und laden Sie folgende Daten in das Projekt:

1. Strassennetz Wädenswil ("osm_highway_prepared.gpkg", siehe {numref}`table-datensaetze-netzwerkanalyse`)
2. Entsorgungsstellen Wädenswil ("abfallentsorgung_waedenswil.gpkg", siehe {numref}`table-datensaetze-netzwerkanalyse`)
3. Gemeindegrenze Wädenswil ("Gemeinde_Waedenswil.gpkg", siehe {numref}`table-datensaetze-netzwerkanalyse`)
4. Optional: OSM Hintergrundkarte grau eingefärbt (siehe {ref}`ex-osm-background`)

**Achtung!:** Achten Sie darauf, dass Sie "QGIS Desktop 3.10.0 **with GRASS 7.8.0**" starten, ansonsten stehen ihnen die GRASS Erweiterungen nicht zur Verfügung  (siehe {ref}`chap-vorbereitung-aufstarten`).


```{admonition} Übungsziele
:class: attention
- Sie sind in der Lage, einfache Reisezeitberechnungen in QGIS selber durchzuführen.
- Sie erweitern Ihr Skillset zur Umwandlung von verschiedenen Geodatentypen (Vektor zu Raster, Raster zu Vektor, Linien zu Punkte, usw.)
- Sie können eine einfache Multi-Kriterien-Analyse (MCA) mit Raster-Daten in QGIS selbständig durchführen.
- Sie können einfache Map Overlay-Operationen in QGIS selber ausführen.
```
