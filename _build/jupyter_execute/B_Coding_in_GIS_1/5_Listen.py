#!/usr/bin/env python
# coding: utf-8

# # Aufgabe 2: Listen
# 
# ## Theorie
# 
# Wohl das einfachste Gefäss, um mehrere Werte zu speichern sind Python-Listen, sogenannte *Lists*. Diese *Lists* werden mit eckigen Klammern erstellt. Die Reihenfolge, in denen die Werte angegeben werden, wird gespeichert. Das erlaubt es uns, bestimmte Werte aufgrund ihrer Position abzurufen. 
# 
# Eine *List* wird folgendermassen erstellt:

# In[1]:


hexerei = [3,1,2]


# Der erste Wert wird in Python mit `0` (!!!) aufgerufen:

# In[2]:


hexerei[0]


# In[3]:


type(hexerei)


# Im Prinzip sind *Lists* ähnlich wie *Vectors* in R, mit dem Unterschied das in Python-Lists unterschiedliche Datentypen abgespeichert werden können. Zum Beispiel auch weitere, verschachtelte Lists:

# In[4]:


chaos = [23, "ja", [1,2,3]]


# In[5]:


# Der Inhalt vom ersten Wert ist vom Typ "Int"
type(chaos[0])


# In[6]:


# Der Inhalt vom dritten Wert ist vom Typ "List"

type(chaos[2])


# ## Übungen
# 
# % : Lists
# ### Übung 2.1
# 
# 1. Erstelle eine Variable `vornamen` bestehend aus einer *List* mit 3 Vornamen
# 2. Erstelle eine zweite Variable `nachnamen` bestehend aus einer *List* mit 3 Nachnamen
# 3. Erstelle eine Variable `groessen` bestehend aus einer *List* mit 3 Grössenangaben in Zentimeter.

# In[7]:


# Musterlösung

vornamen = ["Christopher", "Henning", "Severin"]
nachnamen = ["Annen","May", "Kantereit"]

groessen = [174, 182, 162]


# % : Elemente aus Liste ansprechen
# ### Übung 2.2
# 
# Wie erhältst du den ersten Eintrag in der Variable `vornamen`? 

# In[8]:


# Musterlösung

vornamen[0]


# % : Liste ergänzen
# ### Übung 2.3
# 
# Listen können durch die Methode `append` ergänzt werden (s.u.). Ergänze die Listen `vornamen`, `nachnamen` und `groessen` durch je einen Eintrag.

# In[9]:


vornamen.append("Malte")


# In[10]:


# Musterlösung

nachnamen.append("Huck")

groessen.append(177)


# % : Summen berechnen
# ### Übung 2.4
# 
# Ermittle die Summe aller Werte in `groesse`. Tip: Nutze dazu `sum()`

# In[11]:


# Musterlösung

sum(groessen)


# % : Anzahl Werte ermitteln
# ### Übung 2.5
# 
# Ermittle die Anzahl Werte in `groesse` . Tip: Nutze dazu `len()`

# In[12]:


# Musterlösung

len(groessen)


# % : Mittelwert berechnen
# (mittelwert)=
# ### Übung 2.6
# 
# Berechne die durchschnittliche Grösse aller Personen in `groesse`. Tip: Nutze dazu `len()` und `sum()`.

# In[13]:


# Musterlösung

sum(groessen)/len(groessen)


# % : Minimum-/Maximumwerte
# ### Übung 2.7
# 
# Ermittle nun noch die Minimum- und Maximumwerte aus `grossen` (finde die dazugehörige Funktion selber heraus).

# In[14]:


# Musterlösung

min(groessen)
max(groessen)

