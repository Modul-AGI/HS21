#!/usr/bin/env python
# coding: utf-8

# (chap-random-numbers)=
# # Aufgabe 7: Zufallszahlen generieren
# 
# ## Theorie
# 
# Im Block "*Datenqualität und Unsicherheit*" hattet ihr auch mit Zufallszahlen und Simulationen auseinandergesetzt. Programmiersprachen sind für eine solche Anwendung sehr gut geeignet, und deshalb werden wir in diesem Abschnitt eine Erweiterung zur Erstellung von Zufallszahlen kennenlernen. Diese Erweiterung lautet `random` und ist teil der ["Python Standard Library"](https://en.wikibooks.org/wiki/Python_Programming/Standard_Library), was bedeutet das wir dieses Erweiterung bereits installiert ist, und wir sie nicht installieren müssen um sie zu nutzen. 

# In[1]:


import random


# In[2]:


random.seed(2)


# Innerhalb vom `random` gibt es zahlreiche Funktionen um Zufallszahlen zu generieren, je nach dem was unsere Anforderungen an die Zufallszahl ist. Zum Beispiel könnte eine Anforderung sein, dass die Zahl innerhalb von einem bestimmten Bereich liegt (z.B. "*generiere eine Zufallszahl zwischen 1 und 10*"). Oder aber, dass sie eine ganze Zahl sein muss. Weiter könnte die Anforderung sein, dass sie aus einer bestimmten Verteilung kommen sollte, zum Beispiel einer Normalverteilung. In diesem letzten Fall müssen wir den Mittlwert sowie die Standartabweichung unserer Verteilung angeben.
# 
# Um eine ganzzahlige Zufallszahl zwischen 0 und 10 zu generieren, können wir die Funktion `randrange()` nutzen:

# In[3]:


random.randrange(start = 0, stop = 10)


# In[4]:


random.randrange(start = 0, stop = 10)


# In[5]:


random.randrange(start = 0, stop = 10)


# Wenn wir auf diese Weise mit `randrange()` immer wieder neue Zufallszahlen generieren fällt irgendwann auf, dass die Verteilung der Zahlen ziemlich gleichmässig ist. Es ist also gleich wahrscheinlich eine 10 zu bekommen eine eine 0 oder eine 5. Die Zahlen kommen also aus einer "uniformen" Verteilung. Dies lässt sich auch sehr schön visualisieren. Ich generiere in den folgenden Codezeilen 1'000 zufallszahlen zwischen 0 und 10 mit der Funktion `randrange`.

# In[6]:


from matplotlib import pyplot as plt


# In[7]:


fig, ax = plt.subplots() 
a = [random.randrange(0,10) for x in range(0,1000)]

ax.hist(a) 

plt.show()


# Die Funktion `randrange(0,10)` generiert nur ganzzahlige Zufallszahlen. Wenn wir aber eine Zufallszahl mit Nachkommastellen haben möchten, müssen wir die Funktion `uniform()` verwenden. 
# 
# Um Zufallszahlen aus einer "Normalverteilung" zu bekommen müssen wir die Funktion `normalvariate` nutzen. Hier müssen wir, wie Eingangs erwähnt, den Mittelwert und die Standartabweichung dieser Verteilung angeben. Tatsächlich können wir bei dieser Variante keine Minimum- und Maximumwerte festlegen. Theoretisch könnte der Generator jeden erdenklichen Zahlenwert rausspucken, am wahrscheinlichsten ist jedoch eine Zahl nahe am angegebenen Mittelwert.

# In[8]:


# mu = Mittelwert, sigma = Standartabweichung
random.normalvariate(mu = 5, sigma = 2)


# In[9]:


# mu = Mittelwert, sigma = Standartabweichung
random.normalvariate(mu = 5, sigma = 2)


# In[10]:


# mu = Mittelwert, sigma = Standartabweichung
random.normalvariate(mu = 5, sigma = 2)


# Wenn wir die obige Funktion 1000x laufen lassen und uns das Histogramm der generierten Zahlen anschauen, dann zeichnet sich folgendes Bild ab. 

# In[11]:


fig, ax = plt.subplots() 
a = [random.normalvariate(5,2) for x in range(0,1000)]

ax.hist(a) 

plt.show()


# ## Übungen
# 
# Nun wollen wir diesen Zufallszahlengenerator `random` nutzen um eine Funktion zu entwickeln, welche einen beliebigen Punkt (mit einer x-/y-Koordinate) zufällig in einem definierten Umkreis verschiebt. Unser Fernziel ist es, den simulierten Datensatz aus  "Datenqualität und Unsicherheit" zu rekonstruieren (siehe unten). Der erste Schritt dorthin ist es, einen gemeldeten Punkt (rot in {numref}`arcgiszecken`) in einem definierten Umkreis zu verschieben.
# 
# (arcgiszecken)=
# ```{figure} figures/arcgiszecken.jpg
# Ausschnitt der simulierten Zeckenstiche. Der rote Punkt stellt jeweils der gemeldete Zeckenstich dar, die blaue Punktwolke drum herum sind simulierte Punkte welche die Ungenauigkeit der Daten wiederspiegelt.
# ```
# 

# 
# Das Ziel dieser Übung ist es also, dass wir eine Funktion entwickeln, die uns einen zufälligen Punkt in der Nähe eines Ursprungspunktes vorschlägt. Unser Vorgehen: Wir addieren jedem Koordinatenwert (`x`/`y`) des Ursprungspunktes einen Zufallswert, zum Beispiel zwischen -100 bis +100.
# 

# % Zufallszahlen aus Uniformverteilung
# ### Übung 7.1
# 
# Bevor wir mit Koordinaten arbeiten wollt ihr euch zuerst mit dem Modul `random` vertraut machen. Importiere das Modul `random` und generiere eine Zufallszahl zwischen -100 und +100 aus einer uniformen Verteilung sowie aus einer Normalverteilung mit Mittelwert 100 und Standartabweichung 20.

# In[12]:


# Musterlösung

import random

random.uniform(-100,100)

random.normalvariate(100,20)


# % Dummykoordinaten erstellen
# ### Übung 7.2
# 
# Nun wollen wir uns den Koordinaten zuwenden. Erstelle als erstes zwei Dummykoordinaten `x_start` und `y_start` mit jeweils dem Wert `0`. Diese sollen als "Ursprungskoordinaten" dienen.
# 

# In[13]:


# Musterlösung

x_start = 0
y_start = 0


# % : Zufallswerte generieren
# ### Übung 7.3
# 
# Generiere nun eine Zufallszahl, die aus einer Normalverteilung stammt und die *in etwa* zwischen -100 und +100 liegt. Weise diese Zahl der Variabel `x_offset` zu.
# Generiere danach eine zweite Zufallszahl (auf die gleiche Art) und weise diese `y_offset` zu.
# 
# 
# ````{tip}
# :class: dropdown
# Überlege dir, welcher *Mittelwert* Sinn macht um Werte zwischen -100 und +100 zu bekommen. Welche Zahl liegt zwischen -100 und +100?
# 
# Überlege dir als nächstes, welche Standartabweichung sinnvoll wäre. Zur Erinnerung: Etwa 68% der Werte liegen inerhalb von +/- 1 Standartabweichung (SD), 95% innerhalb von +/- 2 SD, 99% innerhalb von 3 SD (siehe unten):
# 
# 
# ```{figure} figures/normalverteilung.jpg
# Normalverteilung und die Anteile innerhalb von 1 Standartabweichung (Mittelwert $\mu$ minus Standartabweichung $\sigma$), 2 Standartabweichungen ($\mu - 2\times\sigma)$ und 2 Standartabweichungen ($\mu - 3\times\sigma)$. Quelle: [cobocards](https://www.cobocards.com/)
# ```
# ````

# In[14]:


# Musterlösung

# Normalverteilte Werte mit Mittelwert 0 und Standartabweichung 100  
# Achtung: bei dieser Standartabweichung sind ca 30% der Werte > 100!
x_offset = random.normalvariate(0,100)
y_offset = random.normalvariate(0,100)

x_offset
y_offset


# % : Zufallswerte addieren
# ### Übung 7.4
# 
# Addiere nun die Zufallszahlen `x_offset` und `y_offset` **jeweils** zu den Dummykoordinaten `x_start` und `y_start` und weise diese neuen Koordinaten `x_neu` und `y_neu` zu. Die neuen Werte stellen die leicht verschobenen Ursprungskoordinaten dar. In meinem Fall sind diese um 10.2 Meter nach Osten (positiver Wert) bzw. 4.4 Meter nach Süden (negativer Wert) verschoben worden.

# In[15]:


x_offset = 10.246170309600945
y_offset = -4.443904000288846


# In[16]:


# Musterlösung

x_neu = x_start+x_offset
y_neu = y_start+y_offset


# In[17]:


x_neu


# In[18]:


y_neu


# Visuell betrachtet sieht das folgendermassen aus:

# In[19]:


from matplotlib import pyplot as plt 
import pandas as pd


plt.scatter(x_start,y_start, color = "red") # ursprung
plt.scatter(x_neu,y_neu, color = "blue")    # neu

plt.axis("scaled")
plt.gca().set_xlim([-100,100])
plt.gca().set_ylim([-100,100])


# % : Arbeitsschritte in eine *Function* verwandeln
# (ex-offset-function)=
# ### Übung 7.5
# 
# Nun haben wir das zufällige Verschieben eines Einzelpunktes am Beispiel einer Dummykoordinaten (`0`/`0`) durchgespielt. In der nächsten Aufgabe ({ref}`chap-offset-dataframe`) werden wir *alle* unsere Zeckenstichkoordinaten auf diese Weise zufällig verschieben um einen Simulierten Zeckenstichdatensatz ähnlich wie {numref}`arcgiszecken` zu erhalten. 
# 
# Dafür brauchen wir die eben erarbeiteten Einzelschritte als Funktion, um diese auf alle Zeckenstiche anwenden zu können. **Erstelle jetzt eine Funktion namens `offset_coordinate` welche als Input eine `x` oder `y`-Achsenwert annimmt und eine leicht verschobene Wert zurück gibt.** Integriere die Standartabweichung der Verteilung als optionalen Parameter mit einem Standartwert von 100.

# In[20]:


# Musterlösung

def offset_coordinate(old, distance = 100):
    new = old + random.normalvariate(0,distance)

    return(new)


offset_coordinate(x_start, 100)


# % : Output visualisieren
# (offset-vis)=
# ### Übung 7.6
# 
# Nun ist es wichtig, dass wir unser Resultat visuell überprüfen. Im Beispiel unten wende ich die in der letzten Übung erstellte Funktion `offset_coordinate()` 1'000x auf die Dummykoordinate an. Nutze *deine* Funktion `offset_coordinate` um eine Visualisierung gemäss unten stehendem beispiel zu machen.

# In[21]:


from matplotlib import pyplot as plt 
import pandas as pd

x_neu_list = [offset_coordinate(x_start, 100) for i in range(1,1000)]
y_neu_list = [offset_coordinate(y_start, 100) for i in range(1,1000)]

fig = plt.scatter(x_neu_list,y_neu_list)

plt.axis("scaled")

