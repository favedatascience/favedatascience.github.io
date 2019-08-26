import pandas as pd
import folium
from folium.plugins import FastMarkerCluster, MeasureControl, DualMap, MarkerCluster

fave_df = pd.read_csv('/Users/jatin/Documents/Fave/Datascience/sunflower/my_fb_outlets.csv')
place_df = pd.read_csv('/Users/jatin/Documents/Fave/Datascience/sunflower/fb_google.csv')


#m_zero.fillna(0, inplace =True)
o = folium.plugins.DualMap(location=(3, 102),layout='horizontal', zoom_start=8)
fm = MarkerCluster()
gm = MarkerCluster()

for row in fave_df.itertuples():
    fm.add_child(folium.Marker(location=[row.latitude,  row.longitude], popup=row.company_name))

for row in place_df.itertuples():
    gm.add_child(folium.Marker(location=[row.lat,  row.lng], popup=row.place_id))

fm.add_to(o.m1)
gm.add_to(o.m2)
o.save('index.html')