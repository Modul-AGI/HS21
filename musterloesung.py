# Musterlösung

# Benötigten Module laden #####################
import pandas as pd
import geopandas as gpd
from matplotlib import pyplot as plt
###############################################
# Notwendige Functions definieren #############
def offset_coordinate(old, distance = 100):
    import random
    new = old + random.normalvariate(0,distance)
    return new
###############################################

# Daten Importieren ###########################
zeckenstiche_full = pd.read_csv("data/zeckenstiche_full.csv")
wald = gpd.read_file("data/wald.gpkg")
###############################################

radii = [10,100,1000]
monte_carlo2 = []

for radius in radii:
    for i in range(10):
        zeckenstiche_full["x_sim"] = zeckenstiche_full["x"].apply(offset_coordinate)
        zeckenstiche_full["y_sim"] = zeckenstiche_full["y"].apply(offset_coordinate)
        zeckenstiche_full["Run"] = i
        zeckenstiche_full["Radius"] = radius
        monte_carlo2.append(zeckenstiche_full.copy())
    
monte_carlo_df2 = pd.concat(monte_carlo2)

monte_carlo_gpd2 = gpd.GeoDataFrame(monte_carlo_df2,
                                    geometry=gpd.points_from_xy(monte_carlo_df2['x_sim'], monte_carlo_df2['y_sim']),
                                    crs = 2056) 

monte_carlo_join2 = gpd.sjoin(monte_carlo_gpd2, wald)

monte_carlo_join2.to_file("data/monte_carlo_join2.gpkg", driver = "GPKG")

monte_carlo_join2 = gpd.read_file("data/monte_carlo_join2.gpkg")


results = monte_carlo_join2.groupby(["Radius","Run","Wald_text"]).size().unstack(fill_value = 0).assign(ja_anteil = lambda x: x.ja/(x.ja+x.nein))
                                                                             
results.boxplot(column = "ja_anteil",by = "Radius", color = "blue")
