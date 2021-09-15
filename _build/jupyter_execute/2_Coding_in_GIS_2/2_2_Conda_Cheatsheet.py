#!/usr/bin/env python
# coding: utf-8

# (conda-cheet-sheet)=
# # Conda cheat sheet
# 
# In der folgenden Tabelle werden die Einzelschritte in der Verwendung von Conda näher beschrieben. Wichtig ist vor allem, wann dieser Schritt nötig ist und wie er ausgeführt wird. Um die Tabelle kompakt zu halten werden gewisse Details als Fussnote verlinkt.
# 
# 
# ```{list-table}
# :header-rows: 1
# 
# * - Schritt
#   - Wann ist dies nötig?
#   - Details zum Vorgehen / Befehl für die Konsole[^konsole]
# * - **1\. Conda installieren** (installiert das Program *conda*)
#   - einmalig (ist nicht nötig, wenn ArcGIS Pro installiert ist)
#   - [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (empfohlen) oder [anaconda](https://www.anaconda.com/products/individual) herunterladen und installieren
# * - **2\. Systemvariable setzen** (vermittelt der Konsole, wo das Programm *conda* installiert ist)
#   - einmalig und nur, wenn folgender Befehl in der Konsole eine Fehlermeldung verursacht:
#     `conda --version`
#   - Pfad zur *conda*-installation [^condapath] in die Umgebungsvariable "Path" einfügen [^umgebungsvariable]
# * - **3\. *Virtual environment* erstellen** (erstellt eine neue Arbeitsumgebung)
#   - einmal pro Projekt nötig (wobei eine environment auch wiederverwendet werden kann)
#   - in der Konsole:
#     ```bash
#     conda create --name codingingis
#     ```
# * - **4\. *Virutal environment* aktivieren** (schaltet den "Bearbeitungsmodus" ein)
#   - jedes mal nöig wenn ein **Erweiterung installiert** oder **jupyter lab gestartet** werden soll
#   - in der Konsole [^linux]:
#     ```bash
#     activate codingingis
#     ```
# * - **5\. Jupyter lab installieren** (fügt der virtuellen Umgebung diese IDE hinzu)
#   - 1x pro *environment*
#   - in der Konsole [^activate]:
#     ```bash
#     conda install -c conda-forge jupyterlab
#     ```
# * - **6\. Jupyter lab starten** (startet die IDE "Jupyter Lab")
#   - jedes mal, wenn am Projekt gearbeitet wird
#   - in der Konsole [^activate]:
#     ```bash
#     jupyter lab
#     ```
# * - **7\. Jupyter lab (JL) beenden** (beendet "JupyterLab" in der Console)
#   - wenn ihr die Konsole wieder braucht
#   - Während JL läuft, ist die Konsole blockiert. Um JL zu beenden und die Konsole freizugeben: Tastenkombination `CTRL + C`
# * - **8\. weitere Module [^weiteremodule] installieren** (fügt der *environment* zB `pandas` hinzu)
#   - jedes mal nötig, wenn ein Modul in einer Environment fehlt[^modulfehlt]
#   - in der Konsole [^activate][^jupyterlabbeenden]:
#     ```bash
#     conda install -c conda-forge pandas
#     ```
# ```
# 
# [^konsole]: Mit Konsole ist unter Windows *cmd* gemeint (Windowstaste > cmd). Unter Linux wird bash, auf Mac der Terminal verwendet. 
# [^condapath]: Wenn *conda* von ArcGIS Pro verwendet wird, befindet sich die *conda* installation vermutlich hier: *C:\Program Files\ArcGIS\Pro\bin\Python\Scripts*. Prüfen, ob dieser Folder existiert und dort `conda.exe` vorhanden ist.
# [^linux]: Unter Linux: `conda activate codingingis`
# [^umgebungsvariable]: Windowstaste > Umgebungsvariable für dieses Konto bearbeiten > Zeile "Path" auswählen (doppelklick) > Neu > Pfad zur conda installation hinzufügen > mit OK bestätigen > cmd neu starten > `conda --version` nochmals eingeben.
# [^activate]: Falls die richtige environment noch nicht aktiviert ist, muss dies zuerst noch erfolgen (z.B `activate codingingis`).
# [^modulfehlt]: Dies macht sich bemerkbar duch die Fehlermeldung `ModuleNotFoundError: No module named 'pandas'`
# [^weiteremodule]: In Coding in GIS I - III brauchen wir die Module `pandas`, `matplotlib`, `geopandas` und `descartes`
# [^jupyterlabbeenden]: Falls Jupyter Labs läuft und dadurch die Konsole blockiert ist, gibt es folgende Möglichkeiten:
#     1. Jupyter Labs beenden (CTRL + C) > Modul installieren > Jupyter Lab nochmal starten
#     2. einen neue Konsole starten > *environment* aktivieren > Modul installieren
#     3. den Terminal innerhalb von Jupyter Labs verwenden (File > New > Terminal) und dort die *environment* aktivieren und Modul installieren 
