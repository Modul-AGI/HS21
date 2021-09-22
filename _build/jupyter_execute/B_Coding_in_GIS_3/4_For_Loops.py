#!/usr/bin/env python
# coding: utf-8

# (forloops-3)=
# # Aufgabe 11: *for loops* Advanced
# 
# ## Theorie
# 
# In diesem Kapitel kommen noch zwei Aspekte von *for loops*, die als "*Advanced*" eingestuft werden können aber in der Praxis sehr nützlich sind. Dabei geht es einerseits um verschachtelte *for loops* und zum andere um eine verkürzte Schreibweise von *for loops*. 
# 
# ### Verschachtelte *for loops*
# 
# Wir können verschiedene *for loops* auch ineinander verschachteln (englisch: *nested loops*). Das ist vor allem dann nützlich, wenn alle Kombinationen aus zwei Datensätzen miteinander verrechnet werden müssen. Angenommen du willst die drei Mitglieder deiner Band (bestehend aus *Il Buono*, *Il Brutto*, *Il Cattivo*) deinen Eltern vorstellen und auch umgekehrt deine Eltern deiner Band vorstellen. Für so was eignen sich zwei verschachtelte *for Loops* hervorragend:
# 
# ```{tip}
# :class: dropdown
# Als Platzhaltervariabel nutze ich wenn immer möglich das Singulär und für den Iterator das Plural von dem Objekt, über das ich iteriere. `for bandmitglied in band`, `for vogel in vögel` usw, dies hilft mir den Überblick im *loop* zu bewahren.
# ```

# In[1]:


eltern = ["Papa", "Mama"]
band = ["Il Buono", "Il Brutto", "Il Cattivo"]

for bandmitglied in band:
    for elternteil in eltern:
        print(elternteil, "das ist",bandmitglied)
        print(bandmitglied, "das ist",elternteil)
        print("---")


# DIESER TEIL IST ENTFERNT, TOO MUCH INFORMATION 
# 
# Ein anderes Beispiel:  Der Abschluss vom Lied "Bitch" (Meredith Brooks) geht folgendermassen:
# 
# ```
# Uuhh, uuhh, uuhh
# Uuhh, uuhh, uuhh
# Uuhh, uuhh, uuhh
# Uuhh, uuhh, uuhh
# ```
# 
# Das sind also 3 *Uuhh*'s pro Zeile, und dies 4 mal wiederholt. Um dies in einem verschachtelten *for loop* abzubilden müssen wir etwas kreativ sein.
# 
# ```python
# # der äussere Loop ist verantwortlich für die vier Zeilen
# for i in range(4):
#     
#     zeile = []
#     for j in range(3):
#         zeile.append("Uuhh")
#     print(zeile)
# ```

# ### Verkürzte Schreibweise
# 
# Es ist äusserst häufig der Fall, dass wir den Output aus einem Loop in einer Liste abspeichern wollen. Wie das geht haben wir ja bereits in {ref}`forloops-2` gelernt:

# In[2]:


rollen = ["bitch","lover","child","mother","sinner","saint"]

refrain = []
for rolle in rollen:
    liedzeile = "I'm a "+ rolle 
    refrain.append(liedzeile)


# Nur ist das ein *bisschen* umständlich, weil wir dafür viele Zeilen Code brauchen, um etwas eigentlich ganz simples zu bewerkstelligen. Es gibt deshalb dafür auch eine verkürzte Schreibweise, welche ich in der letzten Woche bereits einmal verwendet habe (siehe {ref}`offset-vis`). Der obige Loop hat in der verkürzten Schreibweise die folgende Form:

# In[3]:


refrain = ["I'm a "+ rolle for rolle in rollen]


# Diese verkürzte Schreibweise heisst in Python *list comprehension* und sie ist äusserst praktisch, wenn man sie beherrscht. Das Beherrschen ist aber nicht zentral, es reicht schon wenn ihr eine solche Schreibweise wieder erkennt und richtig interpretieren könnt (im Sinne von "*Aha, hier wird also in einem Loop eine Liste erstellt*"). In der folgenden Darstellung seht ihr farblich, welche Elemente sich in der verkürzten Schreibweise wo wiederfinden und welche Elemente gar nicht wiederverwendet werden.

# ![list](figures/list_comprehension.jpg)

# ## Übungen

# % : Nested Loop: Bellen und Fauchen
# ### Übung 11.1
# 
# Erstelle zwei Listen bestehend aus 3 Hundenamen (`hunde`) und 3 Katzennamen (`katzen`). Erstelle einen verschachtelten *For Loop*, wo jeder Hund jede Katze anbellt und jede Katze jeden Hund anfaucht.
# 
# ```python
# Bruno bellt Greta an
# Greta faucht Bruno an
# Berta bellt Greta an
# ....
# ```

# In[4]:


# Musterlösung

hunde = ["Bruno", "Berta","Helmi"]
katzen = ["Greta", "Xavier", "Zachy"]

for katze in katzen:
    for hund in hunde:
        print(hund, "bellt", katze, "an")
        print(katze, "faucht", hund,"an")


# % !!ENTFERNT!
# 
# % Nested Loop: Multiplikation
# ### Übung 11.2 (Optional)
# 
# Erstelle einen verschachtelten Loop, wo alle Kombinationen von 0 bis 9 miteinander addiert werden:
# 
# ```python
# # Musterlösung
# 
# addition = []
# werte = range(10)
# for i in werte:
#     for j in werte:
#         resultat = i+j
#         addition.append(resultat)
# ```
