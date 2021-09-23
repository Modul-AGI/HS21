#!/usr/bin/env python
# coding: utf-8

# (chap-intro-cig1)=
# # Einleitung

# In diesem Block bekommt ihr euren ersten Kontakt mit Python und lernt dabei auch gerade Jupyter Notebooks kennen, um mit Python zu interagieren. Er soll einen Einstieg in die Programmierwelt von Python bieten und spezifisch zeigen wie man räumliche Fragestellungen mit frei verfügbarer Software lösen kann. 
# Die Voraussetzung für dieser Kurs ist eine Offenheit, neue Tools und Ansätze kennen zu lernen, die Bereitschaft für lösungorientiertes Arbeiten sowie etwas Hartnäckigkeit. 
# 
# Im Kurs werdet ihr nachstehende Datensätze benötigen, die ihr mittels *Rechtsklick > Speichern unter* bei euch lokal speichern könnt. 
# 
# ```{list-table} Datensätze für den Teil "Coding in GIS I - III"
# :header-rows: 1
# :name: table-datensaetze
# 
# * - Datensatz (inkl. Link)
#   - Beschreibung
# * - [zeckenstiche.csv](https://raw.githubusercontent.com/Modul-AGI/HS21/main/B_Coding_in_GIS_1/data/zeckenstiche.csv)
#   - Eine CSV mit 10 Zeckenstich-Meldungen im Kanton Zürich
# * - [zeckenstiche_full.csv](https://raw.githubusercontent.com/Modul-AGI/HS21/main/B_Coding_in_GIS_1/data/zeckenstiche_full.csv)
#   - Eine CSV mit 1'076 Zeckenstich-Meldungen im Kanton Zürich
# * - [wald.gpkg](https://github.com/Modul-AGI/HS21/raw/main/B_Coding_in_GIS_1/data/wald.gpkg)
#   - Ein Geodatensatz mit einem flächendeckenden (lückenlosen) Polygon, welche den Kanton Zürich in "Wald" und "nicht Wald" unterscheidet
# 
# ```
# 
# ```{admonition} Übungsziele
# :class: attention
# - JupyterLabs aufstarten, kennenlernen und bei Bedarf personalisieren
# - Python kennen lernen, erste Interaktionen
# - Die wichtigsten Datentypen in Python kennen lernen (`bool`, `str`, `int`, `float`, `list`, `dict`)
# - Pandas DataFrames kennen lernen und einfache Manipulationen durchführen
# ```

# <!--
# Noch ein paar Hinweise:
# 
# - Die Musterlösungen zu allen Aufgaben stehen bereit. Wir werden diese bald einblenden
# - Wenn sich im Fliesstext Programmiercode befindet, wird er in `dieser Festschriftart` dargestellt
# - Englische Begriffe, deren Übersetzung eher verwirrend als nützlich wären, werden *in dieser Weise* hervorgehoben
# - Da viele von euch bereits Erfahrung in R haben, stelle ich immer wieder den Bezug zu dieser Programmiersprache her.
# - Alleinstehende Codezeilen werden folgendermassen dargestellt:
# - ```python
#   print("Coding in GIS!")
#   ```
# 
# -->
# 

# Die Slides zur heutigen Vorlesung findet ihr hier: 
# 
# <iframe src="https://modul-agi.github.io/slides/Coding_in_GIS_I" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="400px" width="100%" allowfullscreen></iframe>
# 
# In einem neuen Fenster öffnen: [modul-agi.github.io/slides](https://modul-agi.github.io/slides)
