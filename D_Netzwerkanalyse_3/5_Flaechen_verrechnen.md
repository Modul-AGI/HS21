(chap-netzwerk-multikriterien)=
# Aufgabe 8: Flächen verrechnen

In dieser Übung verschneiden wir die Informationen aus Entsorgungsstellen (abfall_raster.tif), ÖV-Güteklassen (oev_raster.tif), und Zentralitätsmass (centrality_raster.tif), die wir in den vorherigen Übungen berechnet und in Raster überführt haben. Durch die Verschneidung können wir den Optimalen Wohnort eruieren. Diese Methode ist auch als Multikriterienevaluation bekannt und kennt ihr bereits vom GIS "Basic" Modul.
In einem ersten Schritt müssen wir alle drei Rasterdatensätze auf eine einheitliche Skala (z.B. 0 – 100) bringen um sie anschliessend miteinander verrechnen zu können. Dafür brauchen wir die Minimum- und Maximumwerte der drei Raster Datensätzen Güteklassen oev_raster.tif, centrality_raster.tif, abfall_raster.tif. Gehen Sie dafür in die Properties -> Information von jedem Layer und notieren Sie sich die minimalen und maximalen Zellenwerte.

## Übung 8.1: Rasterdatensätze skalieren
Öffnen Sie anschliessend den Raster Calculator (Raster -> Raster Calculator) und Skalieren sie jeden der drei Rasterdatensätze jeweils so, dass Sie Werte von 0 bis 100 erhalten. Dies erreichen Sie mit folgender folgender Formel:

$X_{new}$ = $\frac{x_{i} - x_{min}}{x_{max} - x_{min}} * 100$

In Worten: Ziehen Sie vom Rasterwert $x_{i}$ den Minimumwert ($x_{min}$) ab und dividieren sie diesen durch die Spannweite der Zahlen ($x_{max}$-$x_{min}$)
- $x_{i}$ ist der jeweilige Rasterdatensatz, $x_{min}$ und $x_{max}$ sind jeweils die Zahlenwerte, die sich eingangs notiert hatten.
- Achten sie darauf, dass Sie die richtigen Klammen setzen.
- Speichern Sie diese unter folgenden Namen ab: oev_scaled.tif, abfall_scaled.tif, centrality_scaled.tif.

```{figure} figures/rastCalc.jpg
:name: 
```


## Übung 8.2: Zusammenführen mit Raster Calculator

Nutzen Sie erneut den Raster Calculator um die drei Rasterdatensätze miteinander zu verrechnen. Die einfachste Variante ist den Mittelwert der drei Rasterdatensätze zu berechnen. Dafür muss man alle drei summieren und mit drei dividieren:

$raster_{neu}$ = $\frac{oev_{scaled}+abfall_{scaled}+centrality_{scaled}}{3}$

Optional kann man auch die drei Rasterdatensätze unterschiedlich gewichten, wie beispielweise nachstehend. Beachten Sie, dass in diesem Fall nicht mehr durch 3, sondern durch die Summe der Gewichte dividiert wird. Visualisieren und interpretieren Sie anschliessend das Resultat.

$raster_{neu}$ = $\frac{oev_{scaled}\times1+abfall_{scaled}\times10+centrality_{scaled}\times5}{16}$
