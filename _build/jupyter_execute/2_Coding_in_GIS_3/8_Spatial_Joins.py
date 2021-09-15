#!/usr/bin/env python
# coding: utf-8

# (chap-spatialjoin)=
# # Aufgabe 14: Spatial Join
# 
# ## Theorie
# 
# In dieser Aufgabe wollen wir für jeden Zeckenstich ermitteln, ob er sich im Wald befindet oder nicht. Den Wald Layer kennt ihr bereits aus dem Block "Datenqualität und Unsicherheit" und wir haben ihn in {ref}`chap-pythongis-formate` kurz angeschaut. Nutzen wir hier nochmal die Gelegenheit, um den Wald und die Zeckenstiche (siehe {numref}`table-datensaetze`) als Geodaten einzulesen und in einer grossem Plot zu visualisieren.
# 
# Wie ihr schon in vorherigen Plots von mir bemerkt hat, nutze ich manchmal `pyplot` aus `matplotlib` (importiert mit alias `plt`) wenn ich etwas mehr flexibiltät haben möchte in meinen plots. Wir werden diese Visualisierungtechnik nicht weiter in diesem Kurs, kopiert einfach den entsprechenden Code in euer Notebook.

# In[9]:


from matplotlib import pyplot as plt
import geopandas as gpd
zeckenstiche_gpd = gpd.read_file("data/zeckenstiche.gpkg")
wald = gpd.read_file("data/wald.gpkg")

# Subplots mit 1 Zeile und 1 Spalte
fig, ax = plt.subplots(1, 1, figsize = (12,12))
wald.plot(color = ["Lightgray","Green"], ax = ax)
zeckenstiche_gpd.plot(color = "Red", ax = ax)


# ### Wie funktioniert ein *Spatial Join*?
# 
# In {ref}`chap-pythongis` habt ihr euch mit den GIS-Funktionalitäten von `geopandas` vertraut gemacht. Eine ganz zentrale Funktion in GIS sind die sogenannten "Spatial Joins". Dabei werden Attribute von einem Geodatensatz auf einen anderen Geodatensatz aufgrund einer räumlichen Beziehung der beiden Datensätze übertragen. Konkret auf unsere Zeckenstiche bedeutet dies: Jedem Zeckenstich sollte die Eigenschaft "Wald: ja" / "Wald: nein" aus `wald` zugewiesen werden. Am einfachsten lässt sich dies in einer Darstellung erklären:
# 
# ```{figure} figures/spatialjoin.jpg
# :name: spatialjoin
# 
# "Spatial Join" zwischen `zeckenstiche` und `wald`. In diesem Spatial Join wurde die Geometrie von `zeckenstiche` übernommen, das heisst das Resultat des Joins ist ein Punkt-Layer.
# ```

# In Python wird ein *Spatial Join* zwischen `zeckenstiche` und `wald` wie folgt durchgeführt (wichtig ist dabei auch die Reihenfolge der Argumente: `left_df` bestimmt den Geometrietyp des Outputs):

# In[7]:


gpd.sjoin(left_df = zeckenstiche_gpd, right_df = wald)


# ## Übungen
# 
# (ex-import-wald)=
# ### Übung 14.1
# 
# Lade das File "wald.gpgk" (siehe {numref}`table-datensaetze`) herunter und speichere es in deiner Workings Directory. Importiere den Datensatz und speichere ihn in der Variable `wald`. 
# 
# Schau dir `wald` an (mit `type`, `.plot()` etc.)

# In[9]:


# Musterlösung

wald = gpd.read_file("data/wald.gpkg")

wald
type(wald)
wald.plot()


# (ex-spatialjoin)=
# ### Übung 14.2
# 
# Führe einen SpatialJoin zwischen `wald` und `zeckenstiche` durch. Vertausche die Reihenfolge (`left_df`, `right_df`) und schaue dir den Output an. Was ist hier passiert?
# 
# ```{admonition} Wichtig!
# :class: attention
# Melde dich bei den Betreuern wenn der *SpatialJoin* bei dir nicht funktioniert und du eine Fehlermeldung bekommst. In diesem Fall kann es sein, dass du auf dem [Server](https://jupyterhub01.zhaw.ch) arbeiten musst (siehe {ref}(chap-intro-cig1)). 
# ```
# 

# In[11]:


# Musterlösung

gpd.sjoin(left_df = zeckenstiche_gpd, right_df = wald) 
gpd.sjoin(left_df = wald, right_df = zeckenstiche_gpd) 

# in beiden Fällen hat der Output geich viele Zeilen. In der ersten Variante ist die Geometrie
# des Outputs "Point", im zweiten Fall "Multipolygon"

