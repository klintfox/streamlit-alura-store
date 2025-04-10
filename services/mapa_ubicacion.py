import streamlit as st
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster  # Importa MarkerCluster

# Función para crear un mapa de puntos
def crear_mapa_distribucion(tienda, tienda_nombre, color_icono):
    # Promedio de latitudes y longitudes de la tienda
    prom_lat = tienda['lat'].mean()
    prom_lon = tienda['lon'].mean()

    # Crear el mapa centrado en la tienda
    m = folium.Map(location=[prom_lat, prom_lon], zoom_start=6)

    # Crear un objeto MarkerCluster para agrupar los marcadores
    marker_cluster = MarkerCluster().add_to(m)

   # Agregar los puntos de venta al grupo de marcadores
    for index, row in tienda.iterrows():
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=f"{tienda_nombre}: {row['Producto']}, {row['Cantidad de cuotas']} cuotas",
            icon=folium.Icon(color=color_icono, icon='info-sign')
        ).add_to(marker_cluster)

    # Guardar el mapa como un archivo HTML
    mapa_html = m._repr_html_()  # Obtiene el código HTML del mapa para insertarlo en Streamlit
    return mapa_html

# Función para crear un mapa de calor
def crear_mapa_calor(tienda, tienda_nombre,color_icono):
    # Promedio de latitudes y longitudes de la tienda
    prom_lat = tienda['lat'].mean()
    prom_lon = tienda['lon'].mean()

    # Crear el mapa centrado en la tienda
    m = folium.Map(location=[prom_lat, prom_lon], zoom_start=7)

    # Agregar el mapa de calor
    heat_data = [[row['lat'], row['lon']] for index, row in tienda.iterrows()]    
    HeatMap(heat_data).add_to(m)    

    # Titulo del mapa de calor
    folium.Marker(
        location=[prom_lat, prom_lon], 
        popup=f"Mapa de Calor de {tienda_nombre}",
        icon=folium.Icon(color=color_icono, icon='info-sign')).add_to(m)

    # Obtener el código HTML del mapa
    return m._repr_html_()