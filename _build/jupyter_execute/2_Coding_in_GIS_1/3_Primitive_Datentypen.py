#!/usr/bin/env python
# coding: utf-8

# # Aufgabe 1: Primitive Datentypen
# 
# Bei primitiven Datentypen handelt es sich um die kleinste Einheit der Programmiersprache, sie werden deshalb auch "atomare Datentypen" genannt. Alle komplexeren Datentypen (Tabellarische Daten, Bilder, Geodaten) basieren auf diesen einfachen Strukturen. Die für uns wichtigsten Datentypen lauten: *Boolean*, *String*, *Integer* und *Float*. Das sind ähnliche Datentypen wie ihr bereits aus R kennt:
# 
# ````{list-table}
# :header-rows: 1
# 
# * - Python
#   - R
#   - Beschreibung
#   - Beispiel
#   - in Python
# * - Boolean
#   - Logical
#   - Logische Werte ja / nein
#   - Wahr / Falsch
#   - ```python
#     regen = True
#     ```
# * - String
#   - Character
#   - Textinformation
#   - Bern, Luzern
#   - ```python
#     stadt = "Bern"
#     ```
# * - Integer
#   - Integer
#   - Zahl ohne Nachkommastelle
#   - Anzahl Einwohner
#   - ```python
#     bern = 133115
#     ```
# * - Float
#   - Double
#   - Zahl mit Nachkommastelle
#   - Temperatur
#   - ```python
#     temp = 22.5
#     ```
# ````

# ### Boolean
# 
# Hierbei handelt es sich um den einfachsten Datentyp. Er beinhaltet nur zwei Zustände: Wahr oder Falsch. In Python werden diese mit `True` oder `False` definiert (diese Schreibweise muss genau beachtet werden). Beispielsweise sind das Antworten auf geschlossene Fragen.
# 

# In[1]:


regen = True # "es regnet"

sonne = False # "die Sonne scheint nicht"

type(sonne)


# Um zu prüfen, ob ein bestimmter Wert `True` oder `False` ist verwendet man `is True`. Will man also fragen ob es regnet, wir dies folgendermassen formuliert:

# In[2]:


# regnet es?
regen is True


# Ob die Sonne scheint, lautet folgendermassen (natürlich müssen dazu die Variabel `sonne` bereits existieren):

# In[3]:


# scheint die Sonne?
sonne is True


# ### String
# 
# In sogenannten *Strings* werden Textinformationen gespeichert. Beispielsweise können das die Namen von Ortschaften sein.

# In[4]:


stadt = "Bern"
land = "Schweiz"

type(stadt)


# Strings können mit `+` miteinander verbunden werden

# In[5]:


stadt + " ist die Hauptstadt der " + land


# ### Integer
# 
# In *Integer* werden ganzzahlige Werte gespeichert, beispielsweise die Anzahl Einwohner einer Stadt. 

# In[6]:


bern_einwohner = 133115

type(bern_einwohner)


# ### Float
# 
# Als `Float` werden Zahlen mit Nachkommastellen gespeichert, wie zum Beispiel die Temperatur in Grad Celsius.

# In[7]:


bern_flaeche = 51.62

type(bern_flaeche)


# ## Übungen
# 
# % Variablen erstellen
# ### Übung 1.1
# 
# Erstelle eine Variabel `vorname` mit deinem Vornamen und eine zweite Variabel `nachname` mit deinem Nachnamen.  Was sind `vorname` und `nachname` für Datentypen?
# 
# 

# In[8]:


# Musterlösung

vorname = "Guido"
nachname = "van Rossum"

type(vorname) # es handelt sich um den Datentyp "str", also String (Text)


# % : String verbinden
# ### Übung 1.2
# 
# "Klebe" Vor- und Nachname mit einem Leerschlag dazwischen zusammen.

# In[9]:


# Musterlösung

vorname+" "+nachname


# % : Zahl ohne Nachkommastelle
# ### Übung 1.3
# 
# Erstelle eine Variabel `groesse_cm` mit deiner Körpergrösse in Zentimeter. Was ist das für ein Datentyp?

# In[10]:


# Musterlösung

groesse_cm = 184
type(groesse_cm) # es handelt sich hierbei um den Datentyp "integer"


# % : Zahl mit Nachkommastelle
# ### Übung 1.4
# 
# Ermittle deine Grösse in Fuss auf der Basis von `groesse_cm` (1 Fuss entspricht 30.48 cm). Was ist das für ein Datentyp?
# 

# In[11]:


# Musterlösung

groesse_fuss = groesse_cm/30.48
type(groesse_fuss) # es handelt sich um den Datentyp "float"


# % : Boolsche Variabeln
# ### Übung 1.5
# 
# Erstelle eine boolsche Variable blond und setzte sie auf `True` wenn diese Eigenschaft auf dich zutrifft und `False` falls nicht. 

# In[12]:


# Musterlösung

blond = False


# % : Einwohnerdichte
# ### Übung 1.6
# 
# Erstelle eine Variabel `einwohner` mit der Einwohnerzahl der Schweiz (8'603'900, per31. Dezember 2019). Erstelle eine zweite Variabel `flaeche` (ohne Umlaute!) mit der Flächengrösse der Schweiz (41'285 km$^2$). Berechne nun die Einwohnerdichte.

# In[13]:


# Musterlösung

einwohner = 8603900
flaeche = 41285

dichte = einwohner/flaeche

dichte


# % :  BMI
# ### Übung 1.7
# 
# Erstelle eine Variabel `gewicht_kg` (kg) und `groesse_cm` (m) und berechne aufgrund von `gewicht_kg` und `groesse_m` ein BodyMassIndex ($BMI=\frac{m}{l^2}$, $m$: Körpermasse in Kilogramm, $l$: Körpergrösse in Meter).

# In[14]:


# Musterlösung

gewicht_kg = 85
groesse_m = groesse_cm/100

gewicht_kg/(groesse_m*groesse_m)

