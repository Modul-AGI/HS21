#!/usr/bin/env python
# coding: utf-8

# # Input: Komplexe Datentypen
# 
# Im letzten Kapitel haben wir primitive Datentypen angeschaut. Diese stellen eine gute Basis dar, in der Praxis haben wir aber meistens nicht *einen* Temperaturwert, sondern eine Liste von Temperaturwerten. Wir haben nicht *einen* Vornamen sondern eine Tabelle mit Vor- und Nachnamen. Dafür gibt es in Python komplexere Datenstrukturen die als Gefässe für primitive Datentypen betrachtet werden können.  Auch hier finden wir viele Ähnlichkeiten mit R:
# 

# ````{list-table}
# :header-rows: 1
# 
# * - Python
#   - R
#   - Beschreibung
#   - Beispiel
# * - List
#   - (Vector)
#   - werden über die Position abgerufen
#   - ```python
#     hexerei = [3,2,1]
#     ```
# * - Dict
#   - List
#   - werden über ein Schlüsselwort abgerufen
#   - ```python
#     langenscheidt = {"trump":"erdichten"}
#     ```
# * - DataFrame
#   - Dataframe
#   - Tabellarische Daten
#   - ```python
#     pd.DataFrame(langenscheidt)
#     ```
# ````

# In Python gibt es noch weitere komplexe Datentypen wie *Tuples* und *Sets*. Diese spielen in unserem Kurs aber eine untergeordnete Rolle. Ich erwähne an dieser Stelle zwei häufig genannte Typen, damit ihr sie schon mal gehört habt:
# 
# - *Tuples*: 
#   - sind ähnlich wie *Lists*, nur können sie nachträglich nicht verändert werden. Das heisst, es ist nach der Erstellung keine Ergänzung von neuen Werten oder Löschung von bestehenden Werten möglich. 
#   - sie werden mit runden Klammern erstellt: `mytuple = (2,2,1)`
# - *Sets*
#   - sind ähnlich wie *Dicts*, verfügen aber nicht über `keys` und `values`
#   - jeder Wert wird nur 1x gespeichert (Duplikate werden automatisch entfernt)
#   - sie werden mit geschweiften Klammern erstellt: `myset = {3,2,2}`
