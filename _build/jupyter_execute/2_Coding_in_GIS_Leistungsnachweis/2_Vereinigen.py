#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# (chap-waldanteil)=
# # Aufgabe 15: Grand Finale
# 
# ## Theorie
# 
# Um an diesen Punkt zu kommen habt ihr euch diverse Werkzeuge aneignen müssen (*Functions*, *For Loops*, *GIS*) und habt dazu Übungen gelöst. Die nachstehenden Code Blöcke nutzen Elemente aus diesen Übungen um auf den gleichen Stand zu kommen, mit der ihr im Themenblock "Datenqualität und Unsicherheiten" in die Übung gestartet seid. Ihr hattet damals (a) Simulierte Zeckenstich-Daten und (b) einen Layer Waldinformation im Projektgebiet. 
# 
# Kopiere die Code Blöcke in ein frisches Notebook und versuche den Code zu verstehen - sie sollten dir sehr bekannt vorkommen. Schau, ob du gewisse Teile an deine Umgebung anpassen musst.
# 
# ---

# Lade die benötigten Module (siehe {ref}`chap-modules-import`): 

# In[32]:


# Benötigten Module laden #####################
import pandas as pd
import geopandas as gpd
from matplotlib import pyplot as plt
###############################################


# Definiere die benötigte *Function* (siehe {ref}`ex-offset-function`):

# In[33]:


# Notwendige Functions definieren #############
def offset_coordinate(old, distance = 100):
    import random
    new = old + random.normalvariate(0,distance)
    return(new)
###############################################


# Importiere die notwendigen Datensätze (siehe {ref}`ex-import-zeckenstiche` und {ref}`ex-import-wald` sowie {numref}`table-datensaetze`):

# In[34]:


# Daten Importieren ###########################
zeckenstiche = pd.read_csv("data/zeckenstiche.csv")
wald = gpd.read_file("data/wald.gpkg")
###############################################


# Simuliere die Zeckenstiche (siehe {ref}`ex-monte-carlo-loop`):

# In[35]:


# Daten Simulieren ############################
monte_carlo = []
for i in range(5):
    zeckenstiche["x_sim"] = zeckenstiche["x"].apply(offset_coordinate)
    zeckenstiche["y_sim"] = zeckenstiche["y"].apply(offset_coordinate)
    zeckenstiche["Run"] = i
    monte_carlo.append(zeckenstiche.copy())
    
monte_carlo_df = pd.concat(monte_carlo)
###############################################


# ## Übungen
# 
# Wir wollen nun den Anteil der Zeckenstiche pro "Simulationsrunde", sprich pro *Loop* Iteration, ermitteln. Diese ist in `monte_carlo_df` mit `Run` gekennzeichnet. Dafür müssen wir noch folgendes machen:
# 
# 1. Die *DataFrame* `monte_carlo_df` in eine *GeoDataFrame* konvertieren
# 2. Für jeden simulierten Punkt ob er sich im Wald befindet oder nicht
# 3. Der Anteil der Zeckenstiche im Wald *pro Run* ermitteln
# 4. Verteilung dieser berechneten Anteile visualisieren

# (ex-14-1)=
# ### Übung 15.1 
# 
# Konvertiere `monte_carlo_df` in eine *GeoDataFrame* und speichere den Output als `monte_carlo_gpd`. Setze dabei auch das Korrekte Koordinatensystem. Schaue dir nochmal {ref}`chap-pythongis` an wenn du dir unsicher bist, wie das geht.

# In[36]:


# Musterlösung

monte_carlo_gpd = gpd.GeoDataFrame(monte_carlo_df,
                                    geometry=gpd.points_from_xy(monte_carlo_df['x_sim'], monte_carlo_df['y_sim']),
                                    crs = 2056) 


# (ex-14-3)=
# ### Übung 15.2
# 
# Ermittle für jeden simulierten Punkt, ob er im Wald ist oder nicht und speichere den Output als `monte_carlo_join`. Schaue dir nochmal {ref}`chap-spatialjoin` an wenn du dir unsicher bist, wie das geht. Schau dir anschliessend `monte_carlo_join` an. Sortiere die *GeoDataFrame* nach "Run" (`monte_carlo_join.sort_values("Run")`) um anschliessend nach "ID" und versuche so, einen Überblick über die Daten zu gewinnen.

# In[37]:


# Musterlösung

monte_carlo_join = gpd.sjoin(monte_carlo_gpd, wald)


# ```python
# # Musterlösung
# 
# monte_carlo_join.sort_values("Run")
# monte_carlo_join.sort_values("ID")
# ```

# (ex-groupby)=
# ### Übung 15.3
# 
# Nun wollen wir von jeder Iteration (bzw. jedem "Run") wissen, wie viele der der Simulierten Punkte sich im Wald und wie viel sich ausserhalb des Waldes befinden. Mit `size` werden Elemente in einer *DataFrame* gezählt, vorher muss man mit `groupby` aber bestimmen was gezählt weren soll. Nachstehender Code zählt zum Beispiel die Anzahl Zeckenstiche pro Run:

# In[38]:


# Hier manipuliere ich die Daten um es so aussehen zu lassen, als seien im 
# Run nummer 4 alle Zeckenstiche im Wald gelandet. Der Code ist für die 
# Studis nicht ersichtlich.
monte_carlo_join.loc[monte_carlo_join.Run == 4,"Wald_text"] = "ja"


# In[39]:


monte_carlo_join.groupby(["Run"]).size()


# Wenn wir nach `Run` *und* `Wald_text` gruppieren, erhalten wir die Anzahl Werte jeder Kombination, was die Information ist nach der wir suchen.

# In[40]:


monte_carlo_join.groupby(["Run","Wald_text"]).size() 


# ### Übung 15.4
# 
# Das ist schon mal nahe dran an was wir wollen, wir haben nun aber für jede Iteration zwei Zeilen: Eine für "Ja" (im Wald) und eine für "Nein" (nicht im Wald). Für die kommenden Schritte wäre es aber praktischer, wenn wir pro Iteration eine Zeile hätten die Anzahl ("Ja" und "Nein") in zwei Spalten. Dies erreichen wir durch den Zusatz `.unstack()`. Führe diesen Befehl bei dir aus und schau dir den Output an.
# 

# In[41]:


monte_carlo_join.groupby(["Run","Wald_text"]).size().unstack()


# ### Übung 15.5
# 
# In meiner Simulation sind im Run Nummer 4 alle Zeckenstiche im Wald gelandet, deshalb steht dort in der Spalte "Nein" der Wert `NaN` ("*not a number*"). Mit `fill_value` kann `NaN` durch einen anderen Wert ersetzt werden. In unserem Fall ist ein `fill_value` von `0` sinnvoll. Ergänze dies in deinem Code und speichere den Output als `mont_carlo_results`.

# In[42]:


mont_carlo_results = monte_carlo_join.groupby(["Run","Wald_text"]).size().unstack(fill_value = 0)

mont_carlo_results


# ### Übung 15.6
# 
# Wir haben nun die *Anzahl* der Werte pro Kategorie und Interation, aussagekräftiger wäre aber deren *Anteil* (`ja_anteil = ja / (ja+nein)`). Erstelle eine neue Spalte "ja_anteil" wo der Anteil der Punkte im Wald enthalten ist.
# 
# ```{tip}
# :class: dropdown
# 
# Schau dir {ref}`ex-sel-col` und {ref}`ex-new-col` an wenn du nicht mehr weisst, wie man Spalten selektiert / erstellt. 
# 
# Für Profis: in die gleiche Familie wie `apply` (siehe {ref}`ex-apply`) gehört die Funktion [`assign`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.assign.html). Diese eignet sich wunderbar für die Erstellung von `ja_anteil`, vor allem in Kombination mit einer `lamba`-*function* (siehe {ref}`chap-functions-lambda`). 
# 
# ```

# In[43]:


# Musterlösung

# Variante 1
mont_carlo_results["ja"] / (mont_carlo_results["ja"] + mont_carlo_results["nein"])

# Variante 2
mont_carlo_results = mont_carlo_results.assign(ja_anteil = lambda x: x.ja/(x.ja+x.nein))


# In[746]:


# Das Resultat sollte folgendermassen aussehen:
mont_carlo_results


# %: Mittelwerte Visualisieren
# ### Übung 15.7
# 
# Gratuliere! Wenn du an diesem Punkt angekommen bist hast du eine ganze Monte Carlo Simulation von A bis Z mit Python durchgeführt. Von hier an steht dir der Weg frei für noch komplexere Analysen. Zum Abschluss kannst du die Mittelwerte wir nun auf einfache Weise visualisieren. Versuche dabei die Methods `plot()` und `boxplot()`.

# In[799]:


# Musterlösung

mont_carlo_results.plot(y = "ja_anteil")


# In[803]:


# Musterlösung

mont_carlo_results.boxplot("ja_anteil", patch_artist=True)

