#!/usr/bin/env python
# coding: utf-8

# (chap-dataframes)=
# # Aufgabe 4: Tabellarische Daten
# 
# ## Theorie
# 
# Schauen wir uns nochmals die *Dictionary* `people` aus der letzten Übung an. Diese ist ein Spezialfall einer Dictionary: Jeder Eintrag besteht aus einer Liste von gleich vielen Werten. Wie bereits erwähnt, kann es in einem solchen Fall sinnvoll sein, die Dictionary als Tabelle darzustellen.

# In[1]:


people = {"vornamen": ["Christopher", "Henning", "Severin"], "nachnamen": ["Annen","May", "Kantereit"], "groessen": [174, 182, 162]}


# In[2]:


import pandas as pd # Was diese Zeile beudeutet lernen wir später

people_df = pd.DataFrame(people)

people_df


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# ## Übungen
# 
# % : von einer *Dictionary* zu einer *DataFrame*
# ### Übung 4.1
# 
# Importiere `pandas` und nutze die Funktion `DataFrame` um `people` in eine DataFrame umzuwandeln (siehe dazu das beispiel oben). Weise den Output der Variable `people_df` zu und schaue es dir im *Variable Explorer* an. 
# 

# In[4]:


# Musterlösung

import pandas as pd 

people_df = pd.DataFrame(people)


# % : *DataFrame* in csv umwandeln
# (ex-to-csv)=
# ### Übung 4.2

# In der Praxis kommen Tabellarische Daten meist als "csv" Dateien daher. Wir können aus unserer eben erstellten DataFrame sehr einfach eine csv Datei erstellen. Führe das mit folgendem Code aus und suche anschliessend die erstellte csv-Datei.

# In[5]:


people_df.to_csv("people.csv")


# % : CSV als *DataFrame* importieren
# (ex-import-zeckenstiche)=
# ### Übung 4.3
# 
# Genau so einfach ist es eine csv zu importieren. Lade die Datei "zeckenstiche.csv" (siehe {numref}`table-datensaetze`) herunter und speichere es im aktuellen Arbeitsverzeichnis ab. Importiere mit folgendem Code die Datei "zeckenstiche.csv". Schau dir `zeckenstiche` nach dem importieren im "Variable Inspector" an.

# In[6]:


# ich habe die Daten in einem Unterordner "data" abgespeichert
zeckenstiche = pd.read_csv("data/zeckenstiche.csv")


# ````{admonition} Achtung!
# :class: tip
# - Wenn du auf dem JupyterHub Server arbeitest dann ist dein Arbeitsverzeichnis ebenfalls *auf dem Server*. Das heisst, du musst "zeckenstiche.csv" auf den Server hochladen. Dies kannst du mit dem Button "Upload Files" im Tab "File Browser" bewerkstelligen (s.u.).
# 
# ```{image} figures/upload.jpg
# :name: label
# ```
# 
# - Der Code (`pd.read_csv("data/zeckenstiche.csv")`) funktioniert nur, wenn "zeckenstiche.csv" in einem Ordner "data" im aktuellen Arbeitsverzeichnis (*Current Working Directory*) abgespeichert ist. Wenn du nicht sicher bist, wo dein aktuelles Arbeitsverzeichnis liegt, kannst du dies mit der Funktion `os.getcwd()` (**get** **c**urrent **w**orking **d**irectory) herausfinden (s.u.).
# ``` python
# import os
# os.getcwd()
# ```
# ````
# 
# 

# % : Koordinaten räumlich darstellen
# (ex-scatterplot)=
# ### Übung 4.4
# 
# Die *DataFrame* `zeckenstiche` beinhaltet x und y Koordinaten für jeden Unfall in den gleichnamigen Spalten. Wir können die Stiche mit einem Scatterplot räumlich visualisieren. Führe dazu folgenden Code aus. Überlege dir, was die zweite Zeile bewirkt und warum dies sinnvoll ist.
# 

# In[7]:


fig = zeckenstiche.plot.scatter("x","y")

fig.axis("equal")


# In[8]:


# Musterlösung

# fig.axis("equal") sorgt dafür, dass die Skala der beiden Achsen
# (x und y) gleich sind. Dies ist desshalb sinnvoll, da es sich um 
# räumliche Koordinaten handelt und die Distanzen in Richtung "Nord-Süd"
# (y-Achse) sowie in "West-Ost" (x-Achse) die gleiche Skala haben (Meter)
# https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.pyplot.axis.html


# % : Einzelne Spalte selektieren
# (ex-sel-col)=
# ### Übung 4.5
# 
# Um eine einzelne Spalte zu selektieren (z.B. die Spalte "ID"), kann man gleich vorgehen wie bei der Selektion eines Eintrags in einer *Dictionary*. Probiere es aus.

# In[9]:


# Musterlösung

zeckenstiche["ID"]


# % : Neue Spalte erstellen
# (ex-new-col)=
# ### Übung 4.6
# 
# Auch das Erstellen einer neuen Spalte ist identisch mit der Erstellung eines neuen *Dictionary* Eintrags. Erstelle eine neue Spalte "Stichtyp" mit dem Wert "Zecke" auf jeder Zeile (s.u.).

# In[10]:


# Musterlösung
zeckenstiche["Stichtyp"] = "Zecke"


# In[11]:


zeckenstiche

