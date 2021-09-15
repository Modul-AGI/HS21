#!/usr/bin/env python
# coding: utf-8

# (function-basics)=
# # Aufgabe 5: *Function* Basics
# 
# ## Theorie
# 
# Ein Grundprinzip von Programmieren ist "DRY" (*Don't repeat yourself*). Wenn unser Script sehr viele gleiche oder sehr ähnliche Codezeilen enthält ist das ein Zeichen dafür, dass man besser eine *Function* schreiben sollte. Das hat viele Vorteile: Unter anderem wird der Code wird lesbarer, einfacher zu warten und kürzer. 
# 
# Um mit Python gut zurecht zu kommen ist das schreiben von eigenen *Functions* unerlässlich. Sie sind auch nicht weiter schwierig: Eine *Function* wird mit `def` eingeleitet, braucht einen Namen, einen Input und einen Output.
# 
# Wenn wir zum Beispiel eine Function erstellen wollen die uns grüsst, so geht dies folgendermassen:

# In[1]:


def sag_hallo():
    return "Hallo!"


# - Mit `def` sagen wir: "Jetzt definiere ich eine Function". 
# - Danach kommt der Name der *Function*, in unserem Fall `sag_hallo` (mit diesem Namen können wir die *Function* später wieder abrufen). 
# - Als drittes kommen die runden Klammern, wo wir bei Bedarf Inputvariablen (sogenannte Parameter) festlegen können. In diesem ersten Beispiel habe ich keine Parameter festgelegt
# - Nach der Klammer kommt ein Doppelpunkt was bedeutet: "jetzt wird gleich definiert, was die Funktion tun soll"
# - Auf einer neuen Zeile wird eingerückt festgelegt, was die Function eben tun soll. Meist sind hier ein paar Zeilen Code vorhanden
# - Die letzte eingerückte Zeile (in unserem Fall ist das die einzige Zeile) gibt mit `return` an, was die *Function* zurück geben soll (der Output). In unserem Fall soll sie "Hallo!"  zurück geben.
# 
# Das war’s schon! Jetzt können wir diese *Function* schon nutzen:
# 

# In[2]:


sag_hallo()


# Diese *Function* ohne Input ist wenig nützlich. Meist wollen wir der *Function* etwas - einen Input - übergeben können. Beispielsweise könnten wir der *Function* unseren Vornamen übergeben, damit wir persönlich gegrüsst werden:

# In[3]:


def sag_hallo(vorname):
    return "Hallo " + vorname + "!" 


# Nun können wir der Function ein Argument übergeben. In folgendem Beispiel ist `vorname` ein Parameter, "Guido" ist sein Argument.

# In[4]:


sag_hallo(vorname = "Guido")


# Wir können auch eine *Function* gestalten, die mehrere Parameter annimmt. Beispielweise könnte `sag_hallo()` zusätzlich noch einen Parameter `nachname` erwarten:

# In[5]:


def sag_hallo(vorname, nachname):
    return "Hallo " + vorname + " " + nachname + "!" 


# In[6]:


sag_hallo(vorname = "Guido", nachname = "van Rossum")


# ## Übungen
# 
# % : Erste *Function* erstellen
# ### Übung 5.1
# 
# Erstelle eine Function, die `gruezi` heisst, einen Nachnamen als Input annimmt und per Sie grüsst. 

# In[7]:


# Musterlösung

def gruezi(nachname):
    return "Guten Tag, " + nachname


# In[8]:


# Das Resultat soll in etwa folgendermassen aussehen:
gruezi(nachname = "van Rossum")


# % : *Function* erweitern
# (gruezi2)=
# ### Übung 5.2
# 
# Erstelle eine neue Funktion `gruezi2` welche im Vergleich zu `gruezi` einen weiteren Parameter namens `anrede` annimmt. 
# 
# Das Resultat soll in etwa folgendermassen aussehen:

# In[9]:


# Musterlösung

def gruezi2(nachname, anrede):
    return "Guten Tag, " + anrede + " "+nachname


# In[10]:


gruezi2(nachname = "van Rossum", anrede = "Herr")


# % : Zahlen summieren
# ### Übung 5.3
# 
# Erstelle eine Funktion `add` die zwei Zahlen summiert.

# In[11]:


# Musterlösung

def add(zahl1, zahl2):
    return zahl1 + zahl2


# In[12]:


# Das Resultat sollte folgendermassen aussehen:
add(zahl1 = 2, zahl2 = 10)


# % : Quadratzahl
# ### Übung 5.4
# 
# Erstelle eine Funktion `square`, welche den Input quadriert.
# 
# ```{tip}
# :class: dropdown
# "Quadireren" heisst ja "mit sich selbst multiplizieren". In Python können zwei Zahlen mit `*` multipliziert werden.
# ```

# In[13]:


# Musterlösung

def square(zahl):
    return zahl*zahl


# In[14]:


# Das Resultat sollte folgendermassen aussehen:
square(zahl = 5)


# % : Meter in Fuss konvertieren
# ### Übung 5.5
# 
# Erstelle eine Funktion `meter_zu_fuss`, die eine beliebige Zahl von Meter in Fuss konvertiert. Zur Errinnerung: 30.48 cm ergeben 1 Fuss. 

# In[15]:


# Musterlösung

def meter_zu_fuss(meter):
    return meter/0.3048


# In[16]:


# Das Resultat sollte folgendermassen aussehen:

meter_zu_fuss(meter = 1.80)

