

#Importing packages

import pandas as pd
import folium

# Importing Octopus vulgaris data. 
specie = pd.read_csv('oc_vulgaris_record.csv')
specie1 = pd.read_csv('sp_officinalis_record.csv')

# Lectura de latitud y longitud de las observaciones
lon, lat = specie['decimalLongitude'], specie['decimalLatitude']
lon1, lat1 = specie1['decimalLongitude'], specie1['decimalLatitude']

# MODIFICABLE
# Lectura de datos adicionales (se deben convertir a cadena para visualizarlos)
dates = specie['eventDate'].astype('str')
dates1 = specie['eventDate'].astype('str')

# MODIFICABLE
# Opciones de visualizacion de la especie
# Debeis ajustar las coordenadas y el zoom del mapa a la localizacion de la especie
# Muchas mas en: http://python-visualization.github.io/folium/docs-v0.5.0/modules.html
m = folium.Map(location=[50, 10], zoom_start=1, tiles='Stamen Watercolor')

# Creacion del conjunto de puntos
feature_group = folium.FeatureGroup('Ocurrences')


# MODIFICABLE
for lon, lat, dates in zip(lon, lat, dates):
    feature_group.add_child(folium.Marker(location=[lat, lon], popup = dates))

for lon1, lat1, dates1 in zip(lon1, lat1, dates1):    
    feature_group.add_child(folium.CircleMarker(location = [lat1, lon1], radius = '50', popup = dates1, color= '#3186cc'))
                                                       
                                                                                               

# Se incorporan los puntos al mapa
m.add_child(feature_group)  


# Se guarda el mapa como una pagina web
m.save('map_two_species.html')

