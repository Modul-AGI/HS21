#!/usr/bin/env python
# coding: utf-8

# (forloops-1)=
# # Aufgabe 9: *for loop* Einführung

# ## Theorie
# 
# ### Die Grundform
# Nirgends ist der Aspekt der Automatisierung so sichtbar wie in *for loops*. Loops sind "Schleifen" wo eine Aufgabe beliebig lange wiederholt wird. Auch *for loops* sind im Grunde genommen simple. Auf den ersten Blick sieht eine *for loop* aus wie eine *Function* definition (siehe {ref}`function-basics` und {ref}`function-advanced`). Im folgenden Beispiel seht ihr ein minimales Beispiel einer *for loop*.

# In[1]:


for platzhalter in [0,1,2]:
    print("Iteration",platzhalter)


# - `for` legt fest, dass eine For-Loop beginnt
# - Nach `for` kommt eine Platzhalter-Variabel, die ihr beliebig benennen könnt. Im obigen Beispiel lautet diese `platzhalter`
# - Nach dem Platzhalter kommt der Begriff `in`. Dieser Begriff kommt zwingend nach dem Platzhalter.
# - Nach `in` wird der "Iterator" festgelegt, also worüber der For-Loop iterieren soll (hier: über eine `List` mit den Werten `[0,1,2]`). 
# - Danach kommt ein Doppelpunkt `:` der zeigt: "Nun legen wir gleich fest was im For-Loop passieren soll" (ähnlich wie in einer *Function*)
# - Auf einer neuen Zeile wird eingerückt festgelegt, was in der *For-Loop* passieren soll. Dieser Teil kann beliebig lange sein, ein *for loop* ist dann fertig, wenn man nicht mehr eingerückt wird. In unserem Fall wird mit `print`[^print] etwas in die Konsole ausgegeben.
# - Achtung: `return()` gibt’s in For-Loops nicht!
# 
# [^print]: Mit `print` können wir Variabeln in die Konsole "ausdrucken" lassen. Innerhalb von `print` können dazu verschiedene Variablen kommagetrennt aufgeführt werden, ohne sie mit `+` verbinden zu müssen wie damals in {ref}`function-basics`.

# ### Der Iterator
# 
# Im obigen Beispiel haben wir über eine *List* iteriert, wir haben also eine Liste als Iterator verwendet. Es gibt aber noch andere "Dinge", über die wir iterieren können. Angenommen wir wollen den gleichen *for loop* mit den Zahlen von 0 bis 100 oder 100 bis 1'000 durchführen. Es wäre ganz schön mühsam, alle Zahlen von 0 bis 100 manuell in einer Liste zu erfassen. Zu diesem Zweck können wir die Funktion `range` verwenden. Mit `range(3)` erstellen wir einen Iterator mit den Werten 0, 1 und 2. Mit `range(100,1001)` erhalten wir die Werte von 100 bis 1'000. 
# 
# Der gleiche *loop* wie oben lautet mit `range` folgendermassen:

# In[2]:


for platzhalter in range(3):
    print("Iteration",platzhalter)


# ### Der Platzhalter
# 
# Die Platzhaltervariabel liegt immer zwischen `for` und `in`, den Namen dieser Variabel könnt ihr frei wählen. Ich habe sie im obigen Beispiel `platzhalter` genannt. Speziell an dieser Variabel ist, dass sie während der Dauer des *Loops* ihren Wert verändert. Mehr dazu in {ref}`forloops-2`.

# ## Übungen

# ### Übung 9.1
# 
# Kopiere den ersten der beiden *Loops* und lasse ihn bei dir laufen. Spiele mit den Werten rum, um ein Gefühl für *For Loops* zu bekommen: Ergänze die Liste mit weiteren Zahlen, verändere den Namen der Platzhaltervariabel und verändere den Text, der in `print` ausgegeben wird.

# In[3]:


# Musterlösung

for platzhalter in [0,1,2,5,10]:
    print("Iteration",platzhalter)
    
for nonsense in [0,1,2,5,10]:
    print("Iteration",nonsense)

for nonsense in [0,1,2,5,10]:
    print("wow",nonsense, "cool")


# % : Erste For-Loop erstellen
# (for-gruss)=
# ### Übung 9.2
# 
# Konstruiere eine Liste bestehend aus 3 Namen und nenne diese Liste `namen`. Erstelle danach einen *for loop*, mit welcher jede Person in der Liste gegrüsst wird. Nutze dafür `print`.
# 

# In[4]:


# Musterlösung

namen = ["Il Buono", "Il Brutto", "Il Cattivo"]

for name in namen:
    print("Ciao ",name)


# ```python
# # Der Output könnte etwa so aussehen
# 
# Ciao  Il Buono
# Ciao  Il Brutto
# Ciao  Il Cattivo
# ```

# % : For-Loop mit `range()`
# ### Übung 9.3
# 
# Kopiere den zweiten *For Loop* (der mit `range`) und spiele hier mit den Werten herum. Verändere den *For Loop* so, dass er über die Werte von -5 bis +5 iteriert.

# In[5]:


# Musterlösung

# Iteriert von -5 bis +5
for platzhalter in range(-5,6):
    print("Iteration",platzhalter)


# % : *for loop* mit Quadieren
# ### Übung 9.4
# 
# Bis jetzt haben unsere *Loops* nicht viel Arbeiten müssen. Erstelle nun einen *For Loop*, welcher für die Werte -5 bis +5 folgendes ausgibt:
# 
# ```python
# Das Quadrat von -5 ist 25
# Das Quadrat von -4 ist 16
# ...
# ```

# In[6]:


# Musterlösung

for platzhalter in range(-5,6):
    print("Das Quadrat von",platzhalter, "ist",platzhalter*platzhalter)


# % : *for loop* ohne Platzhaltervariabel
# ### Übung 9.5
# 
# Bisher haben wir die Platzhaltervariabel immer in unserem *Loop* wiederverwendet. Das müssen wir aber gar nicht, wir können den *for loop* einfach nutzen um etwas x mal zu wiederholen. Erstellen einen *for loop* der folgende beiden Sätze 5x wiederholt:
# 
# ```
# Who likes to party?
# We like to party!
# Who likes to party?
# ....
# ```
# 
# ```{tip}
# :class: dropdown
# Nutze dafür zwei verschiedene `print` Befehle auf zwei Zeilen.
# ```
# 
# 

# In[7]:


# Musterlösung

for i in range(5):
    print("Who likes to party?")
    print("We like to party!")

