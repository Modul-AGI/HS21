#!/usr/bin/env python
# coding: utf-8

# # Leistungsnachweis
# 
# Im Leistungsnachweis von *Coding in GIS* werden wir die Übungen 2 und 3 aus "*Datenqualität und Unsicherheit*" nochmals durchführen. Dieses mal werdet ihr die Daten aber selbst simulieren, und das ganze natürlich in Python umsetzen. 
# 
# In der Übung geht es um folgendes: Wir wissen das die Lagegenauigkeit der Zeckenstichmeldungen mit einer gewissen Unsicherheit behaftet ist. Um diese Unsicherheit bei  der Frage "*Welcher Anteil der der Zeckenstiche befindet sich im Wald?*" zu berücksichtigen, führen wir eine *Monte Carlo Simulation* durch. In diesem Ansatz simulieren wir Zeckenstichmeldungen durch zufälliges Verschieben ihrer Koordinaten. Für jede Iteration der Verschiebung ("*Run*") berechnen wir den Anteil der Meldungen *im Wald*. Die Verteilung dieser Werte beantwortet die Frage ("*Welcher Anteil der der Zeckenstiche befinden sich im Wald?*") unter Berücksichtigung der Unsicherheit.
# 
# 
# ```{figure} figures/sim-workflow.jpg
# ---
# name: fig-sim-workflow
# ---
# Der generelle Workflow userer Monte Carlo Simulation
# ```
# 
# 

# Um diese Komplexe Aufgabe lösen zu können müssen wir sie in Teilaufgaben zerlegen. Wir haben in den drei Blöcken (*Coding in GIS I - III*) darauf hingearbeitet, alle Voraussetzungen zur Lösung dieser Teilaufgaben zu erfüllen. Siehe dazu die nachstehende Tabelle:
# 
# ```{list-table} Teilaufgaben für das Lösen der Monte Carlo Simulation
# :header-rows: 1
# :name: monte-carlo-workflow
# 
# * - Teilaufgabe
#   - Status
#   - Voraussetzung
# * - Einen Einzelpunkt zufällig verschieben
#   - ✓ haben wir in {ref}`ex-offset-function` gelöst 
#   - {ref}`function-basics` und {ref}`function-advanced`
# * - Alle Punkte einer DataFrame zufällig verschieben
#   - ✓ haben wir in {ref}`ex-apply` gelöst
#   - {ref}`chap-random-numbers` und {ref}`chap-offset-dataframe`
# * - Wiederholung von Schritt 2 (zum Beispiel 50-mal)
#   - ✓ haben wir in {ref}`chap-simulation` gelöst
#   - {ref}`forloops-1` und {ref}`forloops-2`
# * - Für jeden simulierten Punkt ermitteln, ob er sich im Wald / ausserhalb des Waldes befindet
#   - ✓ haben wir in {ref}`ex-spatialjoin` gelöst
#   - {ref}`chap-pythongis`
# * - Anteil der Punkte im Wald pro Run ermitteln
#   - werden wir in {ref}`ex-groupby` lösen
#   - Coding in GIS I - III
# ```
