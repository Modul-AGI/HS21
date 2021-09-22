#!/usr/bin/env python
# coding: utf-8

# # Einleitung

# 
# Heute widmen wir uns zwei grossen Themen bevor wir uns an die Umsetzung der Monte Carlo Simulation ({ref}`chap-waldanteil`) wenden. 
# 
# Im ersten Thema geht es um *for Loops*, mit denen wir eine Aufgabe mehrfach ("Iterativ") durchzuführen können. Ein *for Loop* ist ein sehr wichtiges und hilfreiches Werkzeug das man unbedingt kennen sollte. Wir werden *for loops* brauchen um Zeckenstiche zu simulieren, indem wir die bestehenden Meldungen x-fach zufällig verschieben. Das Thema *for loops* behandeln wir in {ref}`forloops-1`, {ref}`forloops-2` und {ref}`forloops-3`. 
# 
# Beim zweiten Thema geht es um GIS. Wir haben bisher mit Daten gearbeitet die eine Rauminformation beinhalten, die Zeckenstiche haben x/y-Koordinaten. Diese Rauminformation haben wir aber nicht als solche behandelt, wir haben die Koordinaten als Zahlen eingelesen und uns nicht gross darum geschert, dass es sich dabei um spezifische Punkte in der Schweiz handelt. Heute werden wir dies ändern müssen da uns eine räumliche Abfrage bevorsteht: Wir wollen nämlich wissen, welche Zeckenstiche sich im Wald befinden. Dadurch lernen wir eine neue Erweiterung kennen und sehen, was für räumliche Operationen in Python möglich sind. Das Thema behandeln wir in {ref}`chap-pythongis`, {ref}`chap-raeumliche-operationen` und {ref}`chap-spatialjoin`. 
# 
# 
# ```{admonition} Übungsziele
# :class: attention
# - Ihr kennt *for-Loops* und könnt sie anwenden
# - Ihr seht, was mit räumlichen Operationen in Python möglich ist und kennt ein Tool, welches dazu notwendig ist
# - Ihr könnt räumliche Operationen (*spatial join*, *overlay*) in Python umsetzen
# - Ihr könnt summary Statistiken (mit `groupby`/`count`) aus DataFrames extrahieren
# ```
