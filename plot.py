import pandas as pd
import plotly.express as px

lat, lon = 45.7965772, -74.1137449

df = pd.read_csv('age.csv', sep=';')
df['z'] = 1
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='z',
        radius=10, center=dict(lat=lat,lon=lon), zoom=10,
        mapbox_style='stamen-terrain')
fig.show()
