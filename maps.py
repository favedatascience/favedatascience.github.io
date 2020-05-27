import pandas as pd
import folium
from folium.plugins import FastMarkerCluster, MeasureControl, DualMap, MarkerCluster

m_zero = pd.read_csv('QueryResultsold.csv')
#m_zero.fillna(0, inplace =True)
m_zero.dropna(inplace =True)
o = folium.Map(location=[3, 102], zoom_start=2)
mc = MarkerCluster()

# print(type(m_zero['address_latitude']))
# print(type(m_zero['address_longitude']))

for row in m_zero.itertuples():
    #folium.Marker([m_zero.iloc[i]['longitude'], m_zero.iloc[i]['latitude']], popup = m_zero.iloc[i]['company_name']).add_to(o)
    #o.add_child(FastMarkerCluster(m_zero[['latitude', 'longitude']].values.tolist(),overlay=False))
    try:

        mc.add_child(folium.Marker(location=[row.address_latitude,  row.address_longitude], popup=row.company_name))
        # mc.add_child(folium.Marker(location=[row.latitude,  row.longitude], popup=row.company_name))

    except Exception as e:
        print(row.address_latitude,  row.address_longitude)
        print(e,'\n')
o.add_child(mc)
o.save('index.html')