#!/usr/bin/env python
# coding: utf-8

# # Verwendung von ArcPy in Jupyter
# 
# Um die ganzen Befehle von ArcGIS direkt in Python ansteuern zu können, muss das package `arcpy` installiert werden. Bisher haben wir alle unsere Packages mit conda installiert, z.B. 
# 
# ```
# conda install -c conda-forge geopandas
# ```
# 
# Mit `arcpy` geht dies leider nicht, weil `arcpy` ein kostenpflichtiges Modul ist welches eine ArcGIS Lizenz benötigt. Glücklicherweise nutzt ArcGIS aber auch Conda Environments. Wir müssen also nur bewerkstelligen, das Spyder die gleiche Conda environment verwendet wie ArcGIS. Dazu gehen wir wie folgt vor:
# 
# 1. {ref}`chap-arcpy-clone`
# 2. {ref}`chap-arcpy-activate`
# 3. {ref}`chap-arcpy-install-additional`
# 
# Wenn wir diese Schritte hinter uns bringen, haben wir Zugriff auf ein extrem mächtiges und einfach zugängliches Toolset. Ich habe euch die Anleitung Schritt für Schritt dokumentiert, so sollte es bei allen klappen.
# 
# 
# (chap-arcpy-clone)=
# ## Schritt 1: ArcGIS Python Umgebung Klonen
# 
# Zuerst prüfen wir die Python Umgebung in ArcGIS. Diese findet man in ArcGIS unter Project > Python
# 
# 
# ```{figure} figures/arcgis_pythonenv2.jpg
# :name: arcgis-pythonenv2
# 
# Hier ist einerseits die Project Environement ersichtlich (1), andererseits steht aber auch, dass diese Environment "read only" ist (2). Das bedeutet, dass wir keine neuen module installieren können, wenn wir diese Environment benutzen. Wir folgen deshalb den Vorschlag "Clone and activate a new environment". Dazu klicken wir auf "Manage Environment" (3). Übrigens: Das ArcGIS Conda benutzt sehen wir an (4).
# ```
# 
# ```{figure} figures/arcgis_pythonenv3.jpg
# :name: arcgis-pythonenv3
# 
# Klicke hier auf "Clone Default" um die Umgebung zu kopieren. Das dauert eine Weile, danach kann man die neue Environment auswählen (Klick auf den Button "Active"). Notiert dir den Namen der neuen Environment, speichere das ArcGIS Projekt ab und starte das ArcGIS neu
# ```
# 
# (chap-arcpy-activate)=
# ## Schritt 2: Die neue Environment aktivieren
# 
# Nun haben wir uns eine wunderschöne Python Umgebung parat gemacht und können diese jetzt in CMD aktivieren. Starte dazu Command Prompt / CMD und schaue dir die verfügbaren environments an:
# 
# ```
# conda env list
# ```
#  
# Bei mir sieht der output folgendermassen aus:
# ```
# # conda environments:
# #
# arcgisonline             C:\Users\rata\AppData\Local\ESRI\conda\envs\arcgisonline
# arcgisonline2            C:\Users\rata\AppData\Local\ESRI\conda\envs\arcgisonline2
# arcgispro-py3-clone      C:\Users\rata\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone
# arcgispro-py3-clone1     C:\Users\rata\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone1
# cameratraps-detector     C:\Users\rata\AppData\Local\ESRI\conda\envs\cameratraps-detector
# codingingis              C:\Users\rata\AppData\Local\ESRI\conda\envs\codingingis
# test                     C:\Users\rata\AppData\Local\ESRI\conda\envs\test
# arcgispro-py3         *  C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3
# root                     C:\Program Files\ArcGIS\Pro\bin\Python 
# ```
# 
# Aktiviere nun die eben erstelle environment mit folgendem code (ersetzte `name-der-environmnet` mit dem tatsächlichen Namen deiner neuen environment aus {ref}`chap-arcpy-clone`:
# 
# ```
# activate name-der-environment
# ```
# (chap-arcpy-install-additional)=
# ## Schritt 3: weitere Module installieren
# 
# Glücklicherweise ist `jupyterlab` bereits in der `arcgis environment` installiert, dies können wir mit folgendem code überprüfen:
# 
# ```
# conda list
# ```

# ```
# # packages in environment at C:\Users\rata\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone1:
# #
# affine                    2.3.0                      py_0    anaconda
# arcgis                    1.8.2                 py36_1275    esri
# arcgispro                 2.6                           0    esri
# .
# .
# .
# jupyterlab                2.2.9                      py_0    conda-forge
# jupyterlab_pygments       0.1.2              pyh9f0ad1d_0    conda-forge
# jupyterlab_server         1.2.0                      py_0    conda-forge
# .
# .
# .
# ```

# Wenn jetzt aber noch module fehlen (wie z.B. `geopandas`), dann können wir diese wie gewohnt (siehe {ref}`chap-install-module`) installieren.
# 
# 
# (chap-use-arcpy)=
# ## Schritt 4: `arcpy` verwenden
# 
# Wenn alles gewünschten Module installiert sind können wir nun Jupyter Lab starten (siehe {ref}`conda-cheet-sheet`). 
# 
# Sobald Jupyter Lab gestartet ist, können wir innerhalb einer cell das Modul `arcpy` mit `import arcpy`  importieren und nun auch verwenden. Zum Beispiel folgendermassen:
# 
# 
# ```
# import arcpy
# from arcpy import env
# 
# # Set environment settings
# env.workspace = "C:/data/Habitat_Analysis.gdb"
# 
# # Select suitable vegetation patches from all vegetation
# veg = "vegtype"
# suitableVeg = "C:/output/Output.gdb/suitable_vegetation"
# whereClause = "HABITAT = 1" 
# arcpy.Select_analysis(veg, suitableVeg, whereClause)
# ```
# 
# Der Syntax ist auf jeder jeweiligen Tool Beschreibung gut dokumentiert (Abschnitt "Code Sample", z.B. [hier](https://pro.arcgis.com/en/pro-app/tool-reference/analysis/buffer.htm))
# 
# 
