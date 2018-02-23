

#Importing packages

import pandas as pd
import folium

# Importing Octopus vulgaris data. 
specie = pd.read_csv('oc_vulgaris_record.csv')
specie1 = pd.read_csv('sp_officinalis_record.csv')
specie2 = pd.read_csv('S_pilchaldrus_record.csv')

# Lectura de latitud y longitud de las observaciones
lon, lat = specie['decimalLongitude'], specie['decimalLatitude']
lon1, lat1 = specie1['decimalLongitude'], specie1['decimalLatitude']
lon2, lat2 = specie2['decimalLongitude'], specie2['decimalLatitude']


#AÑADIENDO LA FECHA
# Extraemos las fechas del conjunto de datos, los cuales utilizaremos para la creación de marcadores.
dates = specie['eventDate'].astype('str')
dates1 = specie1['eventDate'].astype('str')
dates2 = specie2['eventDate'].astype('str')

# CREACIÓN DEL MAPA PARA VISUALIZACION
m = folium.Map(location=[50, 10], zoom_start=3, tiles='Stamen Watercolor')

# Creacion del conjunto de puntos
feature_group = folium.FeatureGroup('Ocurrences')


# 
for lon, lat, dates in zip(lon, lat, dates):
    feature_group.add_child(folium.RegularPolygonMarker(location=[lat, lon], popup = dates, color='#af1818', fill_color='#af1818', number_of_sides=4, radius=3))

for lon1, lat1, dates1 in zip(lon1, lat1, dates1):    
    feature_group.add_child(folium.RegularPolygonMarker(location = [lat1, lon1], popup = dates1, color= '#57cc31', fill_color='#57cc31', number_of_sides=4, radius=3))

for lon2, lat2, dates2 in zip(lon2, lat2, dates2):
    feature_group.add_child(folium.RegularPolygonMarker(location =[lat2, lon2], popup = dates2, color='#99208c', fill_color='#99208c', number_of_sides=4, radius=3))                                                      

# Se incorporan los puntos al mapa
m.add_child(feature_group)  


# Se guarda el mapa como una pagina web
m.save('map_three_species.html')

