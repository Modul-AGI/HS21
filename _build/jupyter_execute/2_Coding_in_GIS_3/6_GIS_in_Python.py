#!/usr/bin/env python
# coding: utf-8

# (chap-pythongis)=
# # Input: GIS in Python

# Manche mag das jetzt überraschen, andere haben es vielleicht schon gemerkt: Mit **GIS** hatte unseres bisheriges Wirken in Python eigentlich wenig zu tun. Unsere Zeckenstiche haben zwar x/y-Koordinaten, aber diese haben wir bisher gleich behandlet wie alle anderen Spalten.
# 
# Anders gesagt: *Wir* wissen ja, dass mit den Spalten `x` und `y` Koordinaten in der Schweiz gemeint sind, Python hingegen wusste das bisher (noch) nicht. Der konkrete Raumbezug fehlt also noch, und das wird irgendwann problematisch: Denn bald wollen wir für jeden simulierten Zeckenstich ermitteln, ob er sich im Wald befindet oder nicht. Das ist eine explizit räumliche Abfrage, welche nur mit explizit räumlichen Geodaten beantwortet werden kann. 
# 
# Was wir später mit den simulierten Zeckenstiche machen wollen, spielen wir an dieser Stelle mit den original Zeckenstichmeldungen (`zeckenstiche.csv`, siehe {numref}`table-datensaetze`) durch.

# In[1]:


# Unsere Zeckenstiche hatten wir auf folgende Weise importiert:
    
import pandas as pd
zeckenstiche = pd.read_csv("data/zeckenstiche.csv")
zeckenstiche


# ## *DataFrames* > ***Geo**DataFrames*

# Glücklicherweise können wir unsere Zeckenstich-*Dataframe* mit nur einem Zusatzmodul und wenigen Zeilen code in eine **räumliche** *DataFrame* konvertieren. Mit dem Modul ***geo**pandas* erstellen wir aus unserer *pandas DataFrame* eine ***geo**pandas **Geo**DataFrame*. Mit dieser Erweiterung erhält die *DataFrame* 
# 
# 1. **geometry**: eine Zusatzspalte `geometry` mit der Geometrie als räumliches Objekt und
# 2. **crs**: ein Attribut `crs` welches das Koordinatenbezugssystem der Geometriespalte enthält. 
# 
# Beide Bestandteile müssen wir bei der Erstellung der *GeoDataFrame* festlegen. Nachstehend seht ihr, wie ihr dies bei den Zeckenstichen machen könnt, was diese Bestandteile genau bedeuten seht ihr in {ref}`chap-pythongis-datenstruktur` (**geometry**) und {ref}`chap-pythongis-crs` (**crs**). 

# In[14]:


import geopandas as gpd

zeckenstiche_gpd = gpd.GeoDataFrame(zeckenstiche, # die Basis-DataFrame / die "Attributtabelle"
                                    # die Geometrie Spalte:
                                    geometry=gpd.points_from_xy(zeckenstiche['x'], zeckenstiche['y']),
                                    crs = 2056) # EPSG Code des Koordinatenbezugssystem


# Nun sehen wir, dass die neue `geometry` Spalte die Punkt-Geometrie enthält.

# In[15]:


zeckenstiche_gpd


# Zudem hat die *GeoDataFrame* nun ein Attribut `crs`, wo das Koordinatenbezugssystem gespeichert ist.

# In[16]:


zeckenstiche_gpd.crs.name


# (chap-pythongis-datenstruktur)=
# ## Aufbau von GeoDataFrames

# Mit `geometry = ` haben wir die Geometriespalte der *GeoDataFrame* festgelegt. Bei unseren Zeckenstichdaten ist die Geometrie sehr simpel: Sie besteht aus Punkt-Objekte die sich wiederum aus den x- und y-Koordinaten zusammensetzen. Um x/y-Koordinaten in Punktgeometrien zu konvertieren gibt es in Geopandas die Funktion `points_from_xy`. Diese verwende ich im obigen Code um die Punkt-Objekte zu erstellen.
# 
# An dieser Stelle ist es wichtig, die drei Hierarchiestufen von GeoDataFrames zu kären. Von "unten" nach "oben" erläutert gibt es folgende Stufen:
# 
# - **Geometry**: Einzelne Objekte [^shapely] der folgenden Typen
#   - Points / Multipoint [^multi]
#   - Linestring / Multilinestring [^multi]
#   - Polygon / Multipolygon [^multi]
# - **GeoSeries**: Eine vielzahl an *Geometries*, typischerweise eine Spalte einer *GeoDataFrame* namens (*geometry*)
# - **GeoDataFrame**: Eine Tabelle, welche über eine Geometrie-Spalte (*GeoSeries*) verfügt

# ```{figure} figures/Geopandas_types.jpg
# ---
# name: geopandas-types
# ---
# Die drei Hierarchien in Geopandas: Eine *GeoDataFrame* verfügt immer über eine Geometrie-Spalte, welche sich eine *GeoSeries* nennt. Diese wiederum besteht aus Einzelgeometrien, sogenannten *Geometries*.
# ```

# [^shapely]: Die Geometrien in Geopandas sind eigentlich Objekte vom Modul [*Shapely*](https://pypi.org/project/Shapely/). Shapely wiederum ist ein Python Modul, welches mit *Geopandas* mit-installiert und mit-importiert wird.
# 
# (chap-pythongis-crs)=
# ## Koordinatenbezugssystem
# 
# Mit `crs = ` wird das Koordinatenbezugssystem (engl. **C**oordinate **R**eference **S**ystem) unseres Datensatzes festgelegt. Das Koordinatenbezugssystem gibt unseren x/y-Zahlenwerten einen konkreten Raumbezug auf dem Planeten und macht aus ihnen Koordiaten *in der Schweiz*. Wie lautet aber das "Koordinatenbezugssystem" unserer Daten? 
# 
# Im Prinzip weiss diese Information nur derjenige, der die Daten erstellt hat. Man man das Koordinatensytem aber auch anhand der Koordinaten erahnen: Es handelt sich in unserem Fall um Werte im Bereich von 2.6 Mio auf der einen und 1.2 Mio auf der anderen Achse. Da wir wissen das die Daten aus der Schweiz stammen kann man mit etwas Erfahrung sagen, dass es sich um Daten im neuen Schweizer Koordinatenbezugssystem [CH1903+ / LV95](https://epsg.io/2056) handeln muss. Der EPSG Code dieses Koordinatenbezugssystems lautet 2056 und diesen Code können wir in der Funktion `gpd.GeoDataFrame` nutzuen, um das Korrekte Koordinatenbezugssystem zu zuweisen.

# In[17]:


# Das Attribut `crs` wurde aufgrund vom EPSG Code richtig erkannt:
zeckenstiche_gpd.crs.name


# (chap-pythongis-formate)=
# ## Geodatenformate
# 
# Das Einlesen von CSV und die Konvertierung von *DataFrame* zu *GeoDataFrame* hat bei den Zeckenstichen zwar gut funktioniert, es ist aber auch etwas umständlich jedes Mal die `geometry` Spalte und das `crs` zu setzen. CSVs eignen sich nicht besonders gut für das speichern von Geodaten, insbesonders wenn die Daten komplexer sind, wie (*Multi-*) *Linestring*/*Polygon*. Deshalb gibt es auch spezifische Datenformate, in den Geodaten gespeichert werden können. Bei diesen Datenformaten werden `geometry` und `crs` automatisch abgespeichert. 
# 
# Ihr seid im Studium mit solchen Datenformate bereits in Kontakt gekommen, sicher kennt ihr ESRI's *File Geodatabases*/*Feature Classes*  sowie *Shapefiles*. Dies sind häufig genutzte Formate, aber leider nicht offen, und gerade Shapefiles haben viele Tücken (siehe [switchfromshapefile.org](http://switchfromshapefile.org/)). Es gibt dafür ganz tolle Alternativen, beispielsweise *Geopackages* (nicht zu verwechseln mit ArcGIS Pro Packages!). Mit nachstehendem Befehl können wir `zeckenstiche_gpd` als Geopackage abspeichern.
# 
# ```python
# zeckenstiche_gpd.to_file("data/zeckenstiche.gpkg", driver = "GPKG")
# ```
# Das File "zeckenstiche.gpkg" befindet sich nun in meiner *Working Directory* und ich kann sie mit `gpd.read_file("zeckenstiche.gpkg")` wieder einlesen. Im Unterschied zu vorher musst ich nun `geometry` und `crs` nicht mehr zuweisen, diese sind beim Schreiben des Geopackage abgespeichert worden. Das Geopackage kann ich nun auch mit ArcGIS / QGIS öffnen, wenn ich die Punkte interaktiv explorieren möchte.
# 
# Im Block "Datenqualität und Unsicherheit" habt ihr mit dem Wald Datensatz gearbeitet. Ich habe diesen als *Geopackage* exportiert (siehe {numref}`table-datensaetze`) und kann ihn wie im nachstehend Codeblock ersichtlich einlesen und visualisieren.
# 
# 

# In[18]:


import geopandas as gpd

wald = gpd.read_file("data/wald.gpkg") # <- importiert das File "wald.gpkg"

wald


# Es handelt sich also um einen Datensatz mit nur zwei Zeilen, aber mehreren Polygonen pro Zeile (das macht es zu einem ***Multi**polygon*[^multi]). Mit `plot` können wir diesen Datensatz einfach visualisieren und mit den Zeckenstichdaten überlagern.
# 
# 
# [^multi]: Der Unterschied zwischen Point und *Multi*point, Linesstring und *Multi*linestring und Polygon *Multi*polyon ist folgendermassen: Typischerweise hat jedes Attribut *eine* Geometrie. Zum Beispiel hat jede Zeckenstichmeldung eine ID, eine Ungenauigkeitsangabe und eben *eine* Punkgeometrie. Somit handelt es sich bei diesem Datensatz um einen einfach *Point* Datensatz. Wenn pro Attribut mehrere Geometrien zugewiesen sind handelt es sich um ein *Multi*point Objekt.

# In[19]:


base = wald.plot(color = ["Lightgrey","Green"])
zeckenstiche_gpd.plot(ax = base, color = "red")


# Nun wird auch klar, dass es sich bei unseren 10 Zeckenstichen um sehr dicht beieinanderliegenden Punkte handelt.

# KOMMENTAR:
# 
# Aktuell wird die bei der Funktion "GeoDataFrame()" die ursprüngliche DataFrame modifiziert. siehe https://github.com/geopandas/geopandas/issues/1179
# 
# Das führt zu sehr unangenehmen Nebeneffekten. Zum Beispiel kann die letzte Aufgabe nicht in einem For Loop gelöst werden, wie im Commit 1bedada versucht wurde (https://github.com/ratnanil/codingingis/commit/1bedada0c73fcb25716f8442c2d6ed86fc372713)
