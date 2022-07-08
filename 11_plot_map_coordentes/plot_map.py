from matplotlib.pyplot import margins
import plotly.express as px
import pandas as pd
#tutorial---https://www.youtube.com/watch?v=1-6ndLqsy6M 

df = pd.read_csv("11_plot_map_coordentes/coordinates.csv")

fig = px.scatter_mapbox(df,
                        lon = df["longitude"],
                        lat = df["latitude"],
                        zoom = 13,
                        size = df["size"],
                        width = 1200,
                        height = 900,
                        title = "Plot coordinates in OSM"
                        )

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0, "t":50, "l":0, "b":10})
fig.show()