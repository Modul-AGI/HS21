#!/usr/bin/env python
# coding: utf-8

# (forloops-2)=
# # Aufgabe 10: *for loop* Basics

# ## Theorie
# 
# Bis jetzt haben wir lediglich Sachen in die Konsole herausgeben lassen, doch wie schon bei Functions ist der Zweck einer *for loop* meist, dass nach Durchführung etwas davon zurückbleibt. Aber `return()` gibt es wie bereits erwähnt bei *for loops* nicht. Nehmen wir folgendes Beispiel:

# In[1]:


for rolle in ["bitch","lover","child","mother","sinner","saint"]:
    liedzeile = "I'm a "+ rolle 
    print(liedzeile)


# Der Output von dieser For-Loop sind zwar sechs Liederzeilen, wenn wir die Variabel `liedzeile` aber jetzt anschauen ist dort nur das Resultat aus der letzten Durchführung gespeichert. Das gleiche gilt auch für die Variabel `rolle`.

# In[2]:


liedzeile


# In[3]:


rolle


# Das verrät uns etwas über die Funktionsweise des *for loops*: Bei jedem Durchgang werden die Variablen immer wieder überschrieben. Wenn wir also den Output des ganzen For-Loops abspeichern wollen, müssen wir dies etwas vorbereiten.
# 
# Dafür erstellen wir unmittelbar for dem *for loops* einen leeren Behälter, zum Beispiel eine leere Liste:

# In[4]:


refrain = []


# Nun können wir innerhalb des *Loops* `append()` nutzen, um den Output von einem Durchgang dieser Liste hinzuzufügen.

# In[5]:


for rolle in ["bitch","lover","child","mother","sinner","saint"]:
    liedzeile = "I'm a "+ rolle 
    refrain.append(liedzeile)


# In unserer Liste `refrain` ist nun der Wert *jeder* Iteration gespeichert.

# In[6]:


refrain


# ## Übungen
# 
# % : Grüsse speichern
# ### Übung 10.1
# 
# Nehmen wir nochmals das Beispiel aus {ref}`for-gruss`. Erstelle nochmal ein Loop, wo drei Personen aus einer Liste gegrüsst werden. Diesmal sollen aber die drei Grüsse in einer Liste (z.B. `mylist`) gespeichert werden.

# In[7]:


# Musterlösung

mylist = []

for name in ["Il Buono", "Il Brutto", "Il Cattivo"]:
    mylist.append("Ciao "+name)


# In[8]:


# Das Resultat sieht dann so aus:
mylist


# % : Ganze Strophe speichern
# (ex-loopoutput)=
# ### Übung 10.2
#     
# Der im Beispiel verwendete Refrain aus [dem Lied "Bitch" von Meredith Brooks](https://www.metrolyrics.com/bitch-lyrics-meredith-brooks.html) besteht bis auf zwei Zeilen aus Wiederholungen. Versuche mit zwei verschiedenen *for loops* den ganzen Refrain in einer Liste zu speichern. Die beiden Teile die vom Muster Abweichen ("*I do not feel ashamed*" und "*You know you wouldn't want it any other way*") kannst du auch ausserhalb der Loops in die Listen einfügen (`append`).

# In[9]:


# Musterlösung

refrain = []

for rolle in ["bitch","lover","child","mother","sinner","saint"]:
    liedzeile = "I'm a "+ rolle 
    refrain.append(liedzeile)
refrain.append("I do not feel ashamed")
for rolle in ["your hell","your dream","nothing in between"]:
    liedzeile = "I'm "+ rolle 
    refrain.append(liedzeile)
refrain.append("You know you wouldn't want it any other way") 


# In[10]:


# Das Resultat sieht dann so aus:
refrain

