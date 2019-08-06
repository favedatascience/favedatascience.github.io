import pandas as pd
import folium
from folium.plugins import FastMarkerCluster, MeasureControl, DualMap

m_zero = pd.read_csv('/Users/aiyas/Downloads/QueryResults.csv')

o = folium.Map(location=[3, 102], zoom_start=2)

o.add_child(FastMarkerCluster(m_zero[['latitude', 'longitude']].values.tolist(),overlay=False))

o.save('index.html')