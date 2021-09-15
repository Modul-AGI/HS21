#!/usr/bin/env python
# coding: utf-8

# # Aufgabe 3: Dictionaries
# 
# ## Theorie

# In den letzten Übungen haben wir einen Fokus auf Listen gelegt. Nun wollen wir ein besonderen Fokus auf den Datentyp *Dictionary* legen.
# 
# Ähnlich wie eine List, ist eine Dictionary ein Behälter wo mehrere Elemente abgespeichert werden können. Wie bei einem Wörterbuch bekommt jedes Element ein "Schlüsselwort", mit dem man den Eintrag finden kann. 
# Unter dem Eintrag "trump" findet man im Langenscheidt Wörterbuch (1977) die Erklärung "erdichten, schwindeln, sich aus den Fingern saugen".  

# ![](figures/trump.jpg)

# In Python würde man diese *Dictionary* folgendermassen erstellen:

# In[1]:


langenscheidt = {"trump":"erdichten- schwindeln- sich aus den Fingern saugen"}


# Schlüssel (von nun an mit *Key* bezeichnet) des Eintrages lautet "trump" und der dazugehörige Wert (*Value*) "erdichten- schwindeln- aus den Fingern saugen". Beachte die geschweiften Klammern (`{` und `}`) bei der Erstellung einer Dictionary.
# 
# Eine *Dictionary* besteht aber meistens nicht aus einem, sondern aus mehreren Einträgen: Diese werden Kommagetrennt aufgeführt. 

# In[2]:


langenscheidt = {"trump":"erdichten- schwindeln- sich aus den Fingern saugen", "trumpery":"Plunder- Ramsch- Schund"}


# Der Clou der *Dictionary* ist, dass man nun einen Eintrag mittels dem *Key* aufrufen kann. Wenn wir also nun wissen wollen was "trump" heisst, ermitteln wir dies mit der nachstehenden Codezeile:  

# In[3]:


langenscheidt["trump"]


# Um eine *Dictionary* mit einem weiteren Eintrag zu ergänzen, geht man sehr ähnlich vor wie beim Abrufen von Einträgen. 

# In[4]:


langenscheidt["trumpet"] = "trompete" 


# Ein *Key* kann auch mehrere Einträge enthalten. An unserem Langenscheidts Beispiel: Das Wort "trump" ist zwar eindeutig, doch "trumpery" hat vier verschiedene Bedeutungen. In so einem Fall können wir einem Eintrag auch eine *List* von Werten zuweisen. Beachte die Eckigen Klammern und die Kommas, welche die Listeneinträge voneinander trennt.

# In[5]:


langenscheidt["trumpery"] = ["Plunder- Ramsch- Schund", 
                             "Gewäsch- Quatsch", 
                             "Schund- Kitsch", 
                             "billig- nichtssagend"]    
langenscheidt["trumpery"]


# In[6]:


len(langenscheidt["trumpery"])


# ## Übungen
# 
# % : Dictionary erstellen
# ### Übung 3.1
# 
# Erstelle eine *Dictionary* mit folgenden Einträgen: Vorname und Nachname von (d)einer Person. Weise diese Dictionary der Variable `me` zu.

# In[7]:


# Musterlösung

me = {"vorname": "Guido", "nachname": "van Rossum"}


# % : Elemente aus Dictionary ansprechen
# ### Übung 3.2
# 
# 
# Rufe verschiedene Elemente aus der Dictionary via dem *Key* ab.

# In[8]:


# Musterlösung

me["nachname"]


# % : *Dictionary* nutzen
# ### Übung 3.3
# 
# Nutze `me` um nachstehenden Satz (mit **deinen** *Values*) zu erstellen:

# In[9]:


# Musterlösung

"Mein name ist "+me["nachname"] +", "+ me["vorname"]+" "+me["nachname"]


# ``` python
# 'Mein name ist van Rossum, Guido van Rossum'
# ```

# % : Key ergänzen
# ### Übung 3.4
# 
# Ergänze die Dictionary `me` durch einen Eintrag "groesse" mit (d)einer Grösse.

# In[10]:


# Musterlösung

me["groesse"] = 181


# % : Dictionary mit List
# ### Übung 3.5
# 
# Erstelle eine neue Dictionary `people` mit den *Keys* "vornamen", "nachnamen" und "groesse" und jeweils 3 Einträgen pro *Key*.

# In[11]:


# Musterlösung

people = {"vornamen": ["Christopher", "Henning", "Severin"], "nachnamen": ["Annen","May", "Kantereit"], "groessen": [174, 182, 162]}


# % : Einträge abrufen
# ### Übung 3.6
# 
# Rufe den **ersten** Vornamen deiner *Dict* auf. Dazu musst du dein Wissen über Listen und Dictionaries kombinieren.

# In[12]:


# Musterlösung

people["vornamen"][0]


# % : Einträge abrufen
# ### Übung 3.7
# 
# Rufe den **dritten** Nachname deiner *Dict* auf.

# In[13]:


# Musterlösung

people["nachnamen"][2]


# % : Mittelwert berechnen
# ### Übung 3.8
# 
# Berechne den Mittelwert aller grössen in deiner Dict

# In[14]:


# Musterlösung

sum(people["groessen"])/len(people["groessen"])

