# Anhang

## Datensätze

Hier befinden sich alle Datensätze, die im Laufe des Blocks "Netzwerkanalyse" benötigt werden:

```{list-table} Datensätze für den Block "Netzwerkanalyse"
:header-rows: 1
:name: table-datensaetze-netzwerkanalyse

* - Datensatz (inkl. Link und CRS / EPSG)
  - Beschreibung
* - [Gemeinde_Waedenswil.gpkg](https://raw.githubusercontent.com/modul-agi/hs20/master/04_Netzwerkanalyse/data/Gemeinde_Waedenswil.gpkg) (EPSG 2056)
  - Die Gemeindegrenze von Wädenswil. Dieser Datensatz basiert auf swissBOUNDARIES3D von Swisstopo.
* - [osm_highway.gpkg](https://raw.githubusercontent.com/modul-agi/hs20/master/04_Netzwerkanalyse/data/osm_highway.gpkg) (EPSG 4326)
  - Alle "Highway" Linien aus dem OpenStreetmaps (Stand *nach* {ref}`ex-network-osmdownload`)
* - [osm_highway_prepared.gpkg](https://github.com/Modul-AGI/HS20/raw/master/04_Netzwerkanalyse/data/osm_highway_prepared.gpkg) (EPSG 2056)
  - Alle "Highway" Linien transformiert und neu projiziert (Output aus {ref}`ex-clip`)
* - [shops_waedenswil.gpkg](https://github.com/Modul-AGI/HS20/raw/master/04_Netzwerkanalyse/data/shops_waedenswil.gpkg) (EPSG 2056)
  - Alle Läden in Wädenswil, für {ref}`ex-network-traveling-shops`
* - [buildings_waedenswil_polygons.gpkg](https://github.com/Modul-AGI/HS20/raw/master/04_Netzwerkanalyse/data/buildings_waedenswil_polygons.gpkg) (EPSG 2056)
  - Alle Gebäudestandorte (Polygon Daten) in Wädenswil, für {ref}`ex-network-traveling-buildings`
* - [abfallentsorgung_waedenswil.gpkg](https://github.com/Modul-AGI/HS20/raw/master/04_Netzwerkanalyse/data/abfallentsorgung_waedenswil.gpkg) (EPSG 2056)
  - Entsorgungsstellen Wädenswil
* - [waedenswil_centrality.gpkg](https://github.com/Modul-AGI/HS20/raw/master/04_Netzwerkanalyse/data/waedenswil_centrality.gpkg) (EPSG 2056)
  - Zentralitätsmasse für Wädenswil (aus {ref}`ex-centrality-calculate`)
```

