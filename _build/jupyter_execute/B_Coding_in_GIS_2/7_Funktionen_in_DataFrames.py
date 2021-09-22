#!/usr/bin/env python
# coding: utf-8

# (chap-offset-dataframe)=
# # Aufgabe 8: Funktionen in *DataFrames*
# 
# ## Theorie
# 
# In dieser Aufgabe haben wir das Ziel, die in der letzten Aufgabe ({ref}`chap-random-numbers`) erstellte Funktion `offset_coordinate()` auf alle Zeckenstich-Koordinaten anwenden. Bildlich gesprochen: Wir nehmen unsere Zeckenstichdatensatz und schütteln ihn **einmal** durch. So erhalten wir einen Datensatz ähnlich wie in {numref}`arcgiszecken` mit dem Unterschied, dass jede Zeckenstichmeldung nicht eine *Wolke* von simulierten Punkten enthält, sondern nur einen einzelnen Punkt.
# 
# Nutze hier die Datei "zeckenstiche.csv" von letzter Woche (siehe {numref}`table-datensaetze`). Erstelle ein neues Notebook und nutze nachstehenden Code um die nötigen Module und Functions zu haben:

# In[1]:


# to add figures to images.. havent found out how to do this yet
from myst_nb import glue


# In[2]:


import pandas as pd

def offset_coordinate(old, distance = 100):
    import random
    new = old + random.normalvariate(0,distance)

    return(new)

zeckenstiche = pd.read_csv("data/zeckenstiche.csv")

zeckenstiche


# In[3]:


from matplotlib import pyplot as plt

off = [offset_coordinate(0) for x in range(10000)]

plt.hist(off)


# 
# ## Übungen

# % : Spalten selektieren
# ### Übung 8.1
# 
# Mache dich nochmals damit vertraut, einzelne Spalten zu selektieren. Schau dir {ref}`chap-dataframes` nochmals an wenn du nicht mehr weisst wie das geht.

# In[4]:


# Musterlösung

zeckenstiche["x"]
zeckenstiche["y"]


# % Neue Spalten erstellen
# ### Übung 8.2
# 
# Mache dich nochmals damit vertraut, wie man neue Spalten erstellt. Schau dir {ref}`chap-dataframes` nochmals an wenn du nicht mehr weisst wie das geht. Erstelle ein paar neue Spalten nach dem Beispiel unten um die Hangriffe zu üben. Lösche die Spalten im Anschluss wieder mit `del zeckenstiche['test1']` etc.

# In[5]:


# Musterlösung

zeckenstiche["test1"] = "test1"

zeckenstiche["test2"] = 10

zeckenstiche["test3"] = [1,2,3,4,5,6,7,8,9,10]


# In[6]:


zeckenstiche


# In[7]:


# Musterlösung

del zeckenstiche['test1']
del zeckenstiche['test2']
del zeckenstiche['test3']


# % : `apply`
# (ex-apply)=
# ### Übung 8.3
# 
# `pandas` kennt eine ganze Familie von Methoden, um Spalten zu Manipulieren und Daten zu Aggregiren (`apply`, `map`, `mapapply`, `assign`). Es würde den Rahmen von diesem Kurs sprengen, die alle im Detail durch zu gehen, es lohnt sich aber sehr sich mit diesen zu befassen wenn man in sich näher mit Python befassen möchte.
# 
# Im unseren Fall brauchen wir lediglich die Methode `apply` um die Funktion `offset_coordinate()` auf die Zeckenstichkoordinaten anzuwenden. Dabei gehen wir wie folgt for:
# 

# In[8]:


zeckenstiche["x"].apply(offset_coordinate)
#\______1_______/ \_2_/\_______3_________/

# 1. Spalte selektieren (["x"])
# 2. Methode "apply" aufrufen
# 3. Function übergeben


# Verwende dieses Schema um auch `offset_coordinate` auf die `y` Spalte anzuwenden und speichere den Output dieser beiden Operationen als neue Spalten `x_sim` sowie `y_sim`. Die *DataFrame* `zeckenstiche` sollte danach wie folgt aussehen:

# In[9]:


# Musterlösung

zeckenstiche["x_sim"] = zeckenstiche["x"].apply(offset_coordinate)
zeckenstiche["y_sim"] = zeckenstiche["y"].apply(offset_coordinate)


# In[10]:


zeckenstiche


# % : Zusätzliche Parameter
# (ex-param)=
# ### Übung 8.4
# 
# In {ref}`ex-apply` haben wir unsere Funktion `offset_coordinate` aufgerufen, ohne den Parameter `distance` zu spezifizieren. Dies war möglich, weil wir für `distance` einen Defaultwert festgelegt hat (100 Meter). Wir können aber auch zusätzliche Parameter kommagetrennt nach der Funktion angeben. Dies sieht folgendermassen aus:

# In[11]:


zeckenstiche["x"].apply(offset_coordinate,distance = 200)


# Nuzte diese Möglichkeit, um die den Offset (`distance`) auf lediglich etwa 10 Meter zu reduzieren.

# In[12]:


# Musterlösung

zeckenstiche["x_sim"] = zeckenstiche["x"].apply(offset_coordinate, distance = 10)
zeckenstiche["y_sim"] = zeckenstiche["y"].apply(offset_coordinate, distance = 10)


# % : Simulation visualisieren
# ### Übung 8.5
# 
# Um die Original `x`/`y`-Werte sowie die Simulierten Daten im gleichen Plot darzustellen, wird folgendermassen vorgegangen: Der erste Datensatz wird mit `.plot()` visualisiert, wobei der Output einer Variabel  (z.B. `basemap`)  zugewiesen wird. Danach wird der zweite Datensatz ebenfalls mit `.plot()` visualisiert, wobei auf den ersten Plot via dem Argument `ax` verwiesen wird.
# 
# Bei den roten Punkten handelt es sich um die Original-Zeckenstichen, bei den blauen um die simulierten (leicht verschoben) Zeckenstiche. Visualisiere deine eigenen Zeckenstiche auf diese Weise.

# In[13]:


from matplotlib import pyplot as plt


# In[14]:


basemap = zeckenstiche.plot.scatter("x", "y", color = "red")
zeckenstiche.plot.scatter("x_sim", "y_sim", ax = basemap, color = "blue")

plt.axis("scaled")

plt.show()


# % Genauigkeitsangaben der Punkte mitberücksichtigen.
# ### Übung 8.6
# 
# In {ref}`ex-param` haben wir alle Punkte um etwa die gleiche Distaz (+/- 10m) verschoben. Wenn wir unsere *DataFrame* "zeckensiche" genau anschauen, steht uns eine Genauigkeitsangabe pro Punkt zur Verfügung: Die Spalte `accuracy`. Diese Spalte ist eine Genauigkeitsangabe über den gemeldeten Zeckenstich. Sie sagt etwas darüber aus, wie sicher der/die Nutzer\*in bei der Standortsangabe war (z.B. "*Diese Meldung ist etwa auf 300 Meter genau*"). Wir können diese Genauigkeitsangabe auch nutzen um den offset *pro Punkt* zu bestimmen.
# 
# Nutze die Spalte `accuracy` als Argument des Parameters `distance` in der Funktion `offset_coordinate` um genau dies zu erreichen. Visualisiere nun die Daten. Was ist hier passiert?

# In[15]:


zeckenstiche


# In[16]:


# Musterlösung

zeckenstiche["x_sim"] = zeckenstiche["x"].apply(offset_coordinate, distance = zeckenstiche["accuracy"])
zeckenstiche["y_sim"] = zeckenstiche["y"].apply(offset_coordinate, distance = zeckenstiche["accuracy"])

zeckenstiche


# In[17]:


# Musterlösung
basemap = zeckenstiche.plot.scatter("x", "y", color = "red")
zeckenstiche.plot.scatter("x_sim", "y_sim", ax = basemap, color = "blue")

plt.axis("scaled")

plt.show()

# Was ist hier passier? 
# Offensichtlich sind die Zeckenstiche nur wenige Meter voneinander entfernt.
# Der offset von mehreren hunder Meter ist viel weiter, als diese Distanz.

