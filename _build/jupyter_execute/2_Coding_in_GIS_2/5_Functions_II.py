#!/usr/bin/env python
# coding: utf-8

# (function-advanced)=
# # Aufgabe 6: *Function* Advanced
# 
# ## Theorie
# 
# ### Standart-Werte
# 
# Man kann für einzelne (oder alle) Parameter auch Standardwerte festlegen. Das sind Werte die dann zum Zug kommen, wenn der Nutzer der Funktion das entsprechende Parameter leer lässt. Schauen wir dazu nochmals `sag_hallo()` an.

# In[1]:


def sag_hallo(vorname):
    return "Hallo " + vorname + "!" 


# Um diese Funktion zu nutzen müssen dem Parameter `vorname` ein Argument übergeben, sonst erhalten wir eine Fehlermeldung. 

# In[2]:


sag_hallo()


# Wenn wir möchten, dass gewisse Parameter auch ohne Argument auskommen, dann könnnen wir einen Standartwert festlegen. So wird der Parameter optional. Bespielsweise könnte `sag_hallo()` einfach *Hallo Du!* zurück geben, wenn kein Vorname angegeben wird. Um dies zu erreichen, definieren wird den Standartwert bereits innerhalb der Klammer, und zwar folgendermassen:

# In[3]:


def sag_hallo(vorname = "Du"):
    return "Hallo " + vorname + "!" 

# Wenn "vorname" nicht angegeben wird:
sag_hallo()


# ```{admonition} Wichtig
# :class: attention
# Wenn mehrere Parameter in einer Funktion definiert werden, dann kommen die optionalen Parameter **immer zum Schluss**.
# ```

# ### Reihenfolge der Argumente
# 
# Wenn die Argumente in der gleichen Reihenfolge eingegeben werden, wie sie in der *Function*-Definiert sind, müssen die Parameter **nicht** spezifiziert werden (z.B: `anrede=`, `nachname=`).

# In[4]:


def gruezi2(nachname, anrede):
    return "Guten Tag, " + anrede + " "+nachname

gruezi2("van Rossum", "Herr")


# Wenn wir die Reihenfolge missachten, ist der Output unserer Funktion fehlerhaft:

# In[5]:


gruezi2("Herr","van Rossum")


# Aber wenn die Parameter der Argumente spezifiziert werden, können wir sie in jeder beliebigen Reihenfolge auflisten:

# In[6]:


gruezi2(anrede = "Herr", nachname = "van Rossum")


# ### Funktionen auf mehreren Zeilen
# 
# Bisher waren unsere Funktionen sehr kurz und einfach und wir benötigten dafür immer nur zwei Zeilen: Die erste Zeile begann die *Function*-Definition (`def..`) und die zweite Zeile retournierte bereits die Lösung `return(...)`. Zwischen diesen beiden Komponenten haben wir aber viel Platz, den wir uns zu Nutze machen können. Wir können hier Kommentare hinzufügen wie auch unsere Funktion in Einzelschritte aufteilen um den Code lesbarer zu machen.

# In[7]:


def gruezi2(nachname, anrede):
    # Wozu ist diese Funktion da?
    # Diese Funktion soll Menschen freundlich grüssen
    
    gruss = "Guten Tag, " + anrede + " "+nachname
    return gruss


# ### Globale und Lokale Variabeln
# 
# Innerhalb einer *Function* können nur die Variabeln verwendet werden, die der *Function* als Argumente übergeben (oder innerhalb der Funktion erstellt) werden. Diese nennt man "lokale" Variabeln, sie sind lokal in der *Function* vorhanden. Im Gegensatz dazu stehen "globale" Variabeln, diese sind Teil der aktuellen Session. 
# 
# Versuchen wir das mit einem Beispiel zu verdeutlichen. Angenommen wir definieren gobal die Variabeln `nachname` und `anrede`:

# In[8]:


# Wir definieren globale Variabeln
vorname = "Guido"

# Nun erstellen wir eine Function, welche diese Variabel ("vorname") nutzen soll:
def sag_hallo(vorname):
    return "Hallo " + vorname

# Wenn wir jetzt aber die Function ausführen wollen, entsteht die Fehlermeldung,
# dass "vorname" fehlt (obwohl wir vorname ja schon definiert haben)
sag_hallo()


# (chap-functions-lambda)=
# ### Lambda-Function
# 
# Mit dem Begriff `lambda` kann eine *Function* verkürzt geschrieben werden. Wir werden dies im Unterricht kaum verwenden, es ist aber doch gut davon gehört zu haben. Nachstehend wird die Funktion `sag_hallo()` in der bekannten, wie auch in der verkürzten Form definiert. 
# 
# ````{panels}
# Herkömmliche Weise:
# ```python
# def sag_hallo(vorname):
#     return "Hallo "+vorname
# ```
# ---
# Verkürzt mit `lambda`:
# ```python
# sag_hallo = lambda vorname: "Hallo "+vorname
# ```
# ````
# 

# ## Übungen

# %: Multiplizieren
# ### Übung 6.1
# 
# Erstelle eine Funktion namens `times`, die zwei Zahlen miteinander multipliziert. 

# In[9]:


# Musterlösung

def times(x,y):
    return x*y


# In[10]:


times(2,2)


# % : Optionale Parameter
# ### Übung 6.2
# 
# Die eben erstellte Funktion `times` benötigt 2 Argumente (die miteinander multipliziert werden). Wandle den einen in Parameter einen optionalen Parameter um (mit dem Defaultwert `1`). 
# 
# **Zusatzaufgabe**: Was passiert, wenn du den ersten Parameter in einen optionalen Parameter umwandelst?

# In[11]:


# Musterlösung

def times(x,y = 1):
    return x*y


# In[12]:


times(3)


# ``` python
# # Musterlösung
# # (Zusatzaufgabe)
# 
# def times(x  = 1 ,y):
#     return x*y
# 
#   File "<ipython-input-10-e0d2091c9b0f>", line 1
#     def times(x  = 1 ,y):
#               ^
# SyntaxError: non-default argument follows default argument
# ```

# % : BMI
# ### Übung 6.3
# 
# Erstelle eine Funktion namens `bmi`, die aus Grösse und Gewicht einen BodyMassIndex berechnet ($BMI=\frac{m}{l^2}$, $m$: Körpermasse in Kilogramm, $l$: Körpergrösse in Meter). Das Resultat soll etwa folgendermassen aussehen:

# In[13]:


# Musterlösung

def bmi(groesse_m, gewicht_kg):
    return gewicht_kg / (groesse_m*groesse_m)


# In[14]:


bmi(groesse_m=1.8, gewicht_kg=88)


# %  Mittelwert
# ### Übung 6.4
# 
# Erstelle eine Funktion `mean()`, welche den Mittelwert aus einer Liste (`List`) von Zahlen berechnet. Das Resultat sollte folgendermassen aussehen:
# 
# 
# ```{tip}
# :class: dropdown
# Nutze dazu `sum()` und `len()` analog {ref}`mittelwert`.
# ```

# In[15]:


# Musterlösung

def mean(zahlen):
    return sum(zahlen)/len(zahlen)


# In[16]:


meine_zahlen = [50, 100,550,1000]
mean(meine_zahlen)


# %  Grad Celsius in Farenheit
# ### Übung 6.5
# 
# Erstelle eine Funktion `celsius_zu_farenheit`, welche eine beliebige Zahl von Grad Celsius in Grad Kelvin konvertiert. Zur Erinnerung: *Temperatur in °F = Temperatur in °C x 1,8 + 32*. 

# In[17]:


# Musterlösung

def celsius_in_farenheit(celsius):
    return celsius*1.8+32


# Das Resultat sollte folgendermassen aussehen:

# In[18]:


celsius_in_farenheit(celsius = 25)


# % Lambda Function
# ### Übung 6.6
# 
# Schreibe die letzte Funktion `celsius_zu_farenheit` in der *lambda* Notation.

# In[19]:


# Musterlösung

celsius_in_farenheit2 = lambda celsius: celsius*1.8+32

