# app.py
import os
import pandas as pd
from PIL import Image

import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html

from services.dataloader import cargar_csv
from services.facturacion import calcular_ingreso_total
from services.ventas_por_categoria import calcular_categorias_vendidas
from services.calificacion_promedio import calcular_calificacion_promedio
from services.productos_vendidos import productos_mas_menos_vendidos
from services.costo_envio_por_tienda import calcular_promedio_costo_envio
from services.utils import graficar_pie, graficar_barras, graficar_linea, graficar_productos_mas_menos_vendidos, graficar_costo_envio_por_tienda  
from services.mapa_ubicacion import crear_mapa, crear_mapa_calor

from config import APP_TITLE, MENU_ALURA_STORE, MENU_MAPA_DIS_GEOGRAFICA, MENU_MAPA_CALOR, COLOR_TIENDA_1, COLOR_TIENDA_2, COLOR_TIENDA_3, COLOR_TIENDA_4
from config import TIENDA1, TIENDA2, TIENDA3, TIENDA4, TIENDAS

def configure_page():
    logo = Image.open(os.path.join("assets","logo.ico"))
    st.set_page_config(page_title=APP_TITLE, page_icon=logo, layout="wide")

# Función para mostrar los datos con paginación
def mostrar_datos_con_paginacion(df):

    # Paginador
    page_size = 5
    total_pages = len(df) // page_size + (1 if len(df) % page_size != 0 else 0)

    # Crear un selector para elegir la página
    page = st.slider("Selecciona la página", min_value=1, max_value=total_pages, value=1)

    # Mostrar los registros de la página seleccionada
    start_row = (page - 1) * page_size
    end_row = page * page_size
    st.dataframe(df[start_row:end_row])

# Cargar los datos
url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda1 = cargar_csv(url)
tienda2 = cargar_csv(url2)
tienda3 = cargar_csv(url3)
tienda4 = cargar_csv(url4)

def main():
    configure_page()
    menu = [
        MENU_ALURA_STORE, MENU_MAPA_DIS_GEOGRAFICA, MENU_MAPA_CALOR
    ]

    opcion = st.sidebar.selectbox("Selecciona una opción", menu)

    if opcion == MENU_ALURA_STORE:

        # Título de la sección
        st.subheader("Datos")

        # Combo box para seleccionar la tienda
        opcion = st.selectbox("Selecciona una tienda", TIENDAS, key="select_tienda_ingresos")

        # Dependiendo de la tienda seleccionada, mostramos el reporte correspondiente
        if opcion == TIENDA1:
            st.subheader("Datos de Tienda 1")
            mostrar_datos_con_paginacion(tienda1)

        elif opcion == TIENDA2:
            st.subheader("Datos de Tienda 2")
            mostrar_datos_con_paginacion(tienda2)

        elif opcion == TIENDA3:
            st.subheader("Datos de Tienda 3")
            mostrar_datos_con_paginacion(tienda3)

        elif opcion == TIENDA4:
            st.subheader("Datos de Tienda 4")
            mostrar_datos_con_paginacion(tienda4)

        # 1 Análisis de facturación
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("1 Análisis de Facturación")

        # Crear columnas para mostrar los datos y el gráfico en una misma línea
        col1_ingresos, col2_ingresos = st.columns(2)
        with col1_ingresos:   
            # Ingreso Total por tienda
            ingreso_tienda1 = calcular_ingreso_total(tienda1)
            ingreso_tienda2 = calcular_ingreso_total(tienda2)
            ingreso_tienda3 = calcular_ingreso_total(tienda3)
            ingreso_tienda4 = calcular_ingreso_total(tienda4)

            ingresos_df = pd.DataFrame({
                'Nro Tienda': [TIENDA1, TIENDA2, TIENDA3, TIENDA4],
                'Ingreso Total': [ingreso_tienda1, ingreso_tienda2, ingreso_tienda3, ingreso_tienda4]
            })

            # Mostrar los ingresos totales por tienda con la tabla centrada
            st.markdown("<h4 style='text-align: center;'>Ingresos Totales por Tienda</h4>", unsafe_allow_html=True)
            
            # Estilo de la tabla centrado
            st.dataframe(
            ingresos_df.style.set_table_styles([
                    {'selector': 'th', 'props': [('text-align', 'center')]},  # Alineación de los encabezados
                    {'selector': 'td', 'props': [('text-align', 'center')]}     # Alineación de las celdas
                ])
            )

        with col2_ingresos:
            # 1 Graficar ingresos totales
            ingresos = [ingreso_tienda1, ingreso_tienda2, ingreso_tienda3, ingreso_tienda4]
            graficar_pie(ingresos)


        # 2 Ventas por categoría
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("2 Ventas de Productos por Categoria")    
        
        # Texto antes de la segunda línea horizontal
        categorias_tienda1 = calcular_categorias_vendidas(tienda1, TIENDA1)
        categorias_tienda2 = calcular_categorias_vendidas(tienda2, TIENDA2)
        categorias_tienda3 = calcular_categorias_vendidas(tienda3, TIENDA3)
        categorias_tienda4 = calcular_categorias_vendidas(tienda4, TIENDA4)

        # Combo box para seleccionar la tienda
        opcionCategoria = st.selectbox("Selecciona una tienda", TIENDAS, key="select_tienda_categoria")

        if opcionCategoria == TIENDA1:
            categorias_tienda1 = calcular_categorias_vendidas(tienda1, TIENDA1)
            st.subheader("Productos por categoría de Tienda 1")
            st.dataframe(categorias_tienda1)

        elif opcionCategoria == TIENDA2:
            categorias_tienda2 = calcular_categorias_vendidas(tienda2, TIENDA2)
            st.subheader("Productos por categoría de Tienda 2")
            st.dataframe(categorias_tienda2)

        elif opcionCategoria == TIENDA3:
            categorias_tienda3 = calcular_categorias_vendidas(tienda3, TIENDA3)
            st.subheader("Productos por categoría de Tienda 3")
            st.dataframe(categorias_tienda3)

        elif opcionCategoria == TIENDA4:
            categorias_tienda4 = calcular_categorias_vendidas(tienda4, TIENDA4)
            st.subheader("Productos por categoría de Tienda 4")
            st.dataframe(categorias_tienda4)
        
        # Graficar ventas por categoría
        graficar_barras(categorias_tienda1, categorias_tienda2, categorias_tienda3, categorias_tienda4)        

        # 3 Calificación promedio de la tienda por lo clientes
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("3 Calificación Promedio de Tienda por Clientes")

        calificacion_promedio1 = calcular_calificacion_promedio(tienda1)
        calificacion_promedio2 = calcular_calificacion_promedio(tienda2)
        calificacion_promedio3 = calcular_calificacion_promedio(tienda3)
        calificacion_promedio4 = calcular_calificacion_promedio(tienda4)
        
        col1_calificacion, col2_calificacion = st.columns(2)
        with col1_calificacion:
            calificacion_df = pd.DataFrame({
                'Tienda': [TIENDA1, TIENDA2, TIENDA3, TIENDA4],
                'Calificación': [calificacion_promedio1, calificacion_promedio2, calificacion_promedio3, calificacion_promedio4]
            })

            # Mostrar los ingresos totales por tienda con la tabla centrada
            st.markdown("<h4 style='text-align: center;'>Resultados</h4>", unsafe_allow_html=True)                
            
            # Estilo de la tabla centrado
            st.dataframe(
                calificacion_df.style.set_table_styles([
                    {'selector': 'th', 'props': [('text-align', 'center'), ('font-size', '16px'), ('border', '1px solid black')]},  # Alineación de los encabezados
                    {'selector': 'td', 'props': [('text-align', 'center'), ('font-size', '14px'), ('border', '1px solid black')]},  # Alineación de las celdas
                    {'selector': 'table', 'props': [('border-collapse', 'collapse')]},  # Unificar bordes de la tabla
                ])
            )
            
        with col2_calificacion:
            # Creando diccionario para poner el promedio de calificaciones por tienda
            calificaciones = {
                TIENDA1: calificacion_promedio1,
                TIENDA2: calificacion_promedio2,
                TIENDA3: calificacion_promedio3,
                TIENDA4: calificacion_promedio4
            }

            # Ordenar las calificaciones de mejor a peor
            calificaciones_ordenadas = dict(sorted(calificaciones.items(), key=lambda item: item[1], reverse=True))    

            # Graficar calificación promedio
            graficar_linea(calificaciones)

        # 4 Productos Más y Menos Vendidos
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("4 Productos más y menos Vendidos")

        # 4 Productos más y menos vendidos    
        opcionCategoria = st.selectbox("Selecciona una tienda", TIENDAS)

        # Mostrar el DataFrame de acuerdo a la tienda seleccionada
        if opcionCategoria == TIENDA1:
            productos_df = productos_mas_menos_vendidos(tienda1, TIENDA1)
        elif opcionCategoria == TIENDA2:
            productos_df = productos_mas_menos_vendidos(tienda2, TIENDA2)
        elif opcionCategoria == TIENDA3:
            productos_df = productos_mas_menos_vendidos(tienda3, TIENDA3)
        elif opcionCategoria == TIENDA4:
            productos_df = productos_mas_menos_vendidos(tienda4, TIENDA4)

        # Mostrar el DataFrame
        st.dataframe(productos_df)
        
        # # Graficar los productos más y menos vendidos por tienda    
        graficar_productos_mas_menos_vendidos(tienda1, tienda2, tienda3, tienda4)

        # 5 Costo de envío promedio por tienda
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("5 Costo de Envío Promedio por Tienda")        
        tienda_1_promedio_costo_envio = calcular_promedio_costo_envio(tienda1)
        tienda_2_promedio_costo_envio = calcular_promedio_costo_envio(tienda2)
        tienda_3_promedio_costo_envio = calcular_promedio_costo_envio(tienda3)
        tienda_4_promedio_costo_envio = calcular_promedio_costo_envio(tienda4)

        col1_costo_envio, col2_costo_envio = st.columns(2)
        with col1_costo_envio:
            costo_envio_df = pd.DataFrame({
                'Tienda': [TIENDA1, TIENDA2, TIENDA3, TIENDA4],
                'Costo Envío': [tienda_1_promedio_costo_envio, tienda_2_promedio_costo_envio, tienda_3_promedio_costo_envio, tienda_4_promedio_costo_envio]
            })

            # Mostrar los ingresos totales por tienda con la tabla centrada
            st.markdown("<h4 style='text-align: center;'>Resultados</h4>", unsafe_allow_html=True)                
            
            # Estilo de la tabla centrado
            st.dataframe(
                costo_envio_df.style.set_table_styles([
                    {'selector': 'th', 'props': [('text-align', 'center'), ('font-size', '16px'), ('border', '1px solid black')]},  # Alineación de los encabezados
                    {'selector': 'td', 'props': [('text-align', 'center'), ('font-size', '14px'), ('border', '1px solid black')]},  # Alineación de las celdas
                    {'selector': 'table', 'props': [('border-collapse', 'collapse')]},  # Unificar bordes de la tabla
                ])
            )

        with col2_costo_envio:
            # Gráfico Envío promedio por tienda    
            tiendas = [TIENDA1, TIENDA2, TIENDA3, TIENDA4]
            costos_envio = [tienda_1_promedio_costo_envio, tienda_2_promedio_costo_envio, tienda_3_promedio_costo_envio, tienda_4_promedio_costo_envio]
            graficar_costo_envio_por_tienda(tiendas, costos_envio)

    # Extra    
    if opcion == MENU_MAPA_DIS_GEOGRAFICA:  
        st.subheader("Visualización de la Distribución Geográfica")

        # Usar un selectbox para elegir la tienda
        opcionCategoria = st.selectbox("Selecciona una tienda", [TIENDA1, TIENDA2,
             TIENDA3, TIENDA4], key="tienda_mapa")        
        
        if opcionCategoria == TIENDA1:
            st.write("Mostrando mapa para Tienda 1")
            mapa_tienda1 = crear_mapa(tienda1, TIENDA1, COLOR_TIENDA_1)            
            html(mapa_tienda1, height=500) 
        elif opcionCategoria == TIENDA2:
            st.write("Mostrando mapa para Tienda 2")
            mapa_tienda2 = crear_mapa(tienda2, TIENDA2, COLOR_TIENDA_2)
            html(mapa_tienda2, height=500)
        elif opcionCategoria == TIENDA3:
            st.write("Mostrando mapa para Tienda 3")
            mapa_tienda3 = crear_mapa(tienda3, TIENDA3, COLOR_TIENDA_3)
            html(mapa_tienda3, height=500)
        elif opcionCategoria == TIENDA4:
            st.write("Mostrando mapa para Tienda 4")
            mapa_tienda4 = crear_mapa(tienda4, TIENDA4, COLOR_TIENDA_4)
            html(mapa_tienda4, height=500)


    if opcion == MENU_MAPA_CALOR:  
        st.subheader("Informe de Recomendación")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("Mapa de Calor")
        # Interfaz de selección de tienda
        opcionCategoria = st.selectbox("Selecciona una tienda para ver el mapa de calor", 
                                    TIENDAS, 
                                    key="tienda_mapa_calor")

        # Mostrar el mapa de calor de la tienda seleccionada
        if opcionCategoria == TIENDA1:
            st.write("Mostrando mapa de calor para Tienda 1")
            mapa_calor_tienda1 = crear_mapa_calor(tienda1, TIENDA1,COLOR_TIENDA_1)
            html(mapa_calor_tienda1, height=500)
        elif opcionCategoria == TIENDA2:
            st.write("Mostrando mapa de calor para Tienda 2")
            mapa_calor_tienda2 = crear_mapa_calor(tienda2, TIENDA2,COLOR_TIENDA_2)
            html(mapa_calor_tienda2, height=500)
        elif opcionCategoria == TIENDA3:
            st.write("Mostrando mapa de calor para Tienda 3")
            mapa_calor_tienda3 = crear_mapa_calor(tienda3, TIENDA3,COLOR_TIENDA_3)
            html(mapa_calor_tienda3, height=500)
        elif opcionCategoria == TIENDA4:
            st.write("Mostrando mapa de calor para Tienda 4")
            mapa_calor_tienda4 = crear_mapa_calor(tienda4, TIENDA4,COLOR_TIENDA_4)
            html(mapa_calor_tienda4, height=500)

        st.markdown("<hr>", unsafe_allow_html=True)
        # st.subheader("Análisis Geográfico de Ingresos y Calificaciones")

if __name__ == '__main__':
    main()