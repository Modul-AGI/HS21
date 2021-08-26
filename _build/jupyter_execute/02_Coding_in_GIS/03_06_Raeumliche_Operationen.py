#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
zeckenstiche = pd.read_csv("data/zeckenstiche.csv")
import geopandas as gpd


zeckenstiche_gpd = gpd.GeoDataFrame(zeckenstiche, 
                                    geometry=gpd.points_from_xy(zeckenstiche['x'], zeckenstiche['y']),
                                    crs = 2056) 


# (chap-raeumliche-operationen)=
# # Aufgabe 13: Räumliche Operationen
# 
# ## Theorie
# 
# Was bringt uns diese *Geo* Erweiterung? Mit *GeoDataFrames* sind nun alle räumliche Operationen möglich, die wir bereits aus ArcGIS kennen aber mit einfachen *DataFrames* noch nicht möglich waren. Ich möchte dies an ein paar Beispielen Demonstrieren.
# 
# 
# ```{admonition} Wichtig
# :class: attention
# 
# - Die verschiedenen räumlichen Operationen in Geopandas erwarten unterschiedlichen Input, deshalb müssen wir manchmal zwischen *Geometrien*, *Geoseries* und *GeoDataFrames* hin- und her konvertieren (siehe {ref}`chap-pythongis-datenstruktur`). 
# - Welche Operation welcher Datentyp braucht seht ihr in [der Dokumentation](https://geopandas.org/). Was für ein Datentyp eure Variabel ist seht ihr mit `type()`.
# - Um `x` zu konvertieren (`crs` ggf. anpassen):
#   - von *Geometry* zu *Geoseries*: `gpd.GeoSeries(x, crs = 2056)`
#   - von *GeoSeries* zu *GeoDataFrame*: `gpd.GeoDataFrame(geometry = x, crs = 2056)` 
# ```
# 
# ### Buffer
# 
# Eine typische GIS Operation ist das "Buffern" von Objekten. Der ArcGIS Befehl ["Buffer"](https://pro.arcgis.com/en/pro-app/tool-reference/analysis/buffer.htm) erreichen wir in Geopandas mit `.buffer()`. Folgender Code macht einen Buffer mit einer Distanz von 10m. 

# In[2]:


buffered = zeckenstiche_gpd.buffer(10) 


# Um Geopandas-Objekte zu plotten kann man einfach `.plot()` verwenden. Zudem kann man mit `boundary` die Umrisse eines Polygons extrahieren:

# In[3]:


base = buffered.boundary.plot() # plottet die boundries    

zeckenstiche_gpd.plot(ax = base, color = "black") # plottet die Punkte


# ### Union
# 
# Mit `unary_union` können wir aus unserer *Point*-Geometrie ein *MultiPoint* erstellen (siehe {ref}`chap-pythongis-datenstruktur`). Dieser Befehl lautet in ArcGIS [Union](https://desktop.arcgis.com/de/arcmap/10.3/tools/analysis-toolbox/union.htm).

# In[4]:


zeckenstiche_union = zeckenstiche_gpd["geometry"].unary_union

type(zeckenstiche_union) # Es handelt sich nun um den Typ "geometry"


# Wenn wir uns `zeckenstiche_union` nun mit `print` anschauen sehen wir, dass sämtliche Koordinaten in einem Objekt zusammengepackt sind: 

# In[5]:


print(zeckenstiche_union)


# (chap-raeumliche-operationen-mbg)=
# ### Minimum Bounding Geometry
# 
# Über ein *MultiPoint* lassen sich jetzt wunderbar sogenannte (in ESRI Terminologie) [Minimum Bounding Geometries](https://pro.arcgis.com/de/pro-app/tool-reference/data-management/minimum-bounding-geometry.htm) rechnen. Mit den gleichnamigen Funktionen können wir nun eine `convex_hull` [^convex-hull] sowie eine `envelope` [^envelope] über alle Punkte rechnen.
# 
# [^convex-hull]:  Convex Hull stellt ein "Rahmen" um alle Punkte dar, wo alle Innenwinkel kleiner sind als 180° (*konvex*)
# [^envelope]: Envelope stellt ebenfalls ein "Rahmen um alle Punkte dar, die aber quadratisch geformt und am Koordiatensystem ausgerichtet ist.
# 
# 

# In[6]:


my_convex_hull = zeckenstiche_union.convex_hull
my_envelope = zeckenstiche_union.envelope


# Nun konvertiere ich beide Polygon-Geometrien in *GeoSeries*, damit sie einfacher zu visualisieren sind:

# In[7]:


my_convex_hull = gpd.GeoSeries(my_convex_hull)
my_envelope = gpd.GeoSeries(my_envelope)


# Um die beiden Objekte nebeneinander zu visualisieren importiere ich zuerst `pyplot` aus `matplotlib` (mit dem alias `plt`) und erstelle `subplots`

# In[8]:


from matplotlib import pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2,sharex=True, sharey = True,figsize = (10,10))

# Erstellt den linken Plot
my_convex_hull.plot(ax = ax1)
ax1.set_title("Convex Hull")
zeckenstiche_gpd.plot(ax = ax1, color = "black")

# Erstellt den rechten Plot
my_envelope.plot(ax = ax2)
ax2.set_title("Envelope")
zeckenstiche_gpd.plot(ax = ax2, color = "black")


# ### Overlay
# 
# Viele der Funktionen aus dem ESRI Toolset ["Overlay"](https://pro.arcgis.com/de/pro-app/tool-reference/analysis/an-overview-of-the-overlay-toolset.htm) sind in der *Geopandas* Funktion `overlay` verpackt. Um sie zu demonstrieren nutze ich die Geometrien, die wir in weiter oben erstellt haben (`buffered` und `my_convex_hull`). Zuerst muss ich sie aber noch von *GeoSeries* in *GeoDataFrames* konverieren.

# In[9]:


buffered_gdf = gpd.GeoDataFrame(geometry = buffered, crs = 2056)               
my_convex_hull_gdf = gpd.GeoDataFrame(geometry = my_convex_hull, crs = 2056) 


# Nun kann ich zum beispielsweise die Overlay-Funktion `difference` ausführen:

# In[10]:


my_difference = gpd.overlay(my_convex_hull_gdf,buffered_gdf, how='difference')


# In[11]:


# Bereitet die drei Subplots vor ################
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharex=True, sharey = True, figsize = (10,10))
#################################################

# Plot links ####################################
my_convex_hull_gdf.plot(ax = ax1)               #
ax1.set_title("1. Das Minimum Convex Polygon")  # 
ax1.set_axis_off()                              #
# Plot mitte ####################################
buffered_gdf.plot(ax = ax2)                     #
ax2.set_title("2. Die gebufferten Punkte")      # 
ax2.set_axis_off()                              #
# Plot rechts ###################################
my_difference.plot(ax = ax3)                    #
ax3.set_title("'difference' aus 1. & 2.")       # 
ax3.set_axis_off()                              #
#################################################


# ## Übungen
# 
# Nun ist es Zeit, dass ihr selbst mit *GeoDataFrames* Hand anlegt. Achtet dabei immer auf die Datentypen eurer Daten (mit `type`) und konsultiert dazu {ref}`chap-pythongis-datenstruktur`. Zudem ist Geopandas gut dokumentiert, es lohnt ich diese immer wieder zu konsultieren: [geopandas.org](https://geopandas.org)
# 
# % *DataFrame* zu *GeoDataFrame*
# ### Übung 13.1

# Importiere *Geopandas* und wandle `zeckenstiche` in eine *GeoDataFrame* um (`zeckenstiche_gpd`). Vergiss nicht, das Koordinatenbezugssystem festzulegen!

# In[12]:


# Musterlösung

import geopandas as gpd

zeckenstiche_gpd = gpd.GeoDataFrame(zeckenstiche, geometry=gpd.points_from_xy(zeckenstiche['x'], zeckenstiche['y'], crs = 2056))


# % Punkte Buffern
# ### Übung 13.2
# 
# Buffere die Zeckenstiche um eine Distanz von 12 Meter und speichere den Output in der Variabel `zeckenstiche_buffer`. Visualisiere die gebufferten Punkte in einem Plot.

# In[13]:


# Musterlösung

zeckenstiche_buffer = zeckenstiche_gpd.buffer(12)
zeckenstiche_buffer.plot()


# % : Umrisse visualisieren
# ### Übung 13.3
# 
# Extrahiere die Umrisse von `zeckenstiche_buffer` und speichere diese in `zeckenstiche_buffer_outline`. Visualisiere anschliessend diese Umrisse.

# In[14]:


# Musterlösung

zeckenstiche_buffer_outline = zeckenstiche_buffer.boundary


# In[15]:


zeckenstiche_buffer_outline.plot()


# % : Layers überlagern
# ### Übung 13.4
# 
# Nutze nachstehenden Code um zwei Datensätze im gleichen Plot darzustellen. 

# In[16]:


from matplotlib import pyplot as plt
fig, ax = plt.subplots()

zeckenstiche_buffer_outline.plot(ax = ax, color = "green")
zeckenstiche_gpd.plot(ax = ax, color = "pink")


# % Envelope
# ### Übung 13.5
# 
# Berechne das "Envelope" von `zeckenstiche_gpd` anhand der obigen Beispielen. Speichere den Output als `zeckenstiche_envelope`.
# 
# ```{tip}
# :class: dropdown
# Denk daran, dass du zuerst noch einen Union machen musst (siehe {ref}`chap-raeumliche-operationen`)
# ```
# 

# In[17]:


# Musterlösung

zeckenstiche_envelope = zeckenstiche_gpd.unary_union.envelope


# % Overlay Operation
# ### Übung 13.6
# 
# Führe die Overlay Operationen *Union* und *Symetrical Difference* zwischen `zeckenstiche_envelope` und `zeckenstiche_buffer` durch. Schaue dir dazu die entsprechende [Geopandas Hilfeseite](https://geopandas.org/set_operations.html#set-operations-with-overlay) an. 
# 
# ```{tip}
# :class: dropdown
# - `zeckenstiche_envelope` musst zu zuerst noch in eine GeoSeries umwandeln. Den Ouput davon kannst du in eine GeoDataFrame konvertieren
# - `zeckenstiche_buffer` sollte schon eine GeoSeries sein, diese kannst du direkt in eine GeoDataFrame konvertieren
# - beim Konvertieren in eine GeoDataFrame kannst du jeweils direkt das Koordinatensystem (`crs = `) korrekt setzen. 
# ```

# In[18]:


# Musterlösung

zeckenstiche_buffer_gdf = gpd.GeoDataFrame(geometry = zeckenstiche_buffer, crs = 2056)

zeckenstiche_envelope_gdf = gpd.GeoDataFrame(geometry = gpd.GeoSeries(zeckenstiche_envelope), crs = 2056)

my_union = gpd.overlay(zeckenstiche_envelope_gdf, zeckenstiche_buffer_gdf, how = "union")

my_symmdiff = gpd.overlay(zeckenstiche_envelope_gdf, zeckenstiche_buffer_gdf, how = "symmetric_difference")


# In[19]:


# Das Resultat sollte folgendermassen aussehen

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (10,8))

my_union.plot(ax = ax1)
ax1.set_title("Union")
my_symmdiff.plot(ax = ax2)
ax2.set_title("Symetrical Difference")


# ### Übung 13.7 
# 
# Exportiere `zeckenstiche_gpd` als "Geopackage" mit dem Namen "zeckenstiche.gpkg". Lese nochmal {ref}`chap-pythongis-formate` wenn du nicht mehr weisst, wie das geht. Versuche anschliessend, "zeckenstiche.gpgk" wieder einzulesen.

# ```python
# # Musterlösung
# 
# zeckenstiche_gpd.to_file("data/zeckenstiche.gpkg")
# ```
