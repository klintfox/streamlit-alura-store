# app.py
import os
import pandas as pd
from PIL import Image

from services.dataloader import cargar_csv
from services.facturacion import calcular_ingreso_total
from services.ventas_por_categoria import calcular_categorias_vendidas
from services.calificacion_promedio import calcular_calificacion_promedio
from services.productos_vendidos import productos_mas_menos_vendidos
from services.costo_envio_por_tienda import calcular_promedio_costo_envio
from services.utils import graficar_pie, graficar_barras, graficar_linea, graficar_productos_mas_menos_vendidos, graficar_costo_envio_por_tienda  
from services.mapa_ubicacion import crear_mapa, crear_mapa_calor

import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html


# Título
APP_TITLE = "Alura Store"
# Menú para la aplicación
MENU_ALURA_STORE = "Alura Store"
MENU_MAPA_DIS_GEOGRAFICA = "Distribucion Geográfica"
MENU_MAPA_CALOR = "Mapa Calor"

def configure_page():
    # Construir la ruta relativa al archivo logo.ico dentro de la carpeta assets
    logo_path = os.path.join(os.path.dirname(__file__), 'assets', 'logo.ico')

    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        # Proceder con el uso de la imagen (por ejemplo, mostrarla)
    else:
        print(f"El archivo {logo_path} no se encuentra en la ruta especificada.")
        # Puedes usar una imagen predeterminada o manejar el error de otra forma

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
        opcion = st.selectbox("Selecciona una tienda", ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"], key="select_tienda_ingresos")

        # Dependiendo de la tienda seleccionada, mostramos el reporte correspondiente
        if opcion == "Tienda 1":
            st.subheader("Datos de Tienda 1")
            mostrar_datos_con_paginacion(tienda1)

        elif opcion == "Tienda 2":
            st.subheader("Datos de Tienda 2")
            mostrar_datos_con_paginacion(tienda2)

        elif opcion == "Tienda 3":
            st.subheader("Datos de Tienda 3")
            mostrar_datos_con_paginacion(tienda3)

        elif opcion == "Tienda 4":
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
                'Nro Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
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
        categorias_tienda1 = calcular_categorias_vendidas(tienda1, "Tienda 1")
        categorias_tienda2 = calcular_categorias_vendidas(tienda2, "Tienda 2")
        categorias_tienda3 = calcular_categorias_vendidas(tienda3, "Tienda 3")
        categorias_tienda4 = calcular_categorias_vendidas(tienda4, "Tienda 4")

        # Combo box para seleccionar la tienda
        opcionCategoria = st.selectbox("Selecciona una tienda", ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"], key="select_tienda_categoria")

        if opcionCategoria == 'Tienda 1':
            categorias_tienda1 = calcular_categorias_vendidas(tienda1, "Tienda 1")
            st.subheader("Productos por categoría de Tienda 1")
            st.dataframe(categorias_tienda1)

        elif opcionCategoria == 'Tienda 2':
            categorias_tienda2 = calcular_categorias_vendidas(tienda2, "Tienda 2")
            st.subheader("Productos por categoría de Tienda 2")
            st.dataframe(categorias_tienda2)

        elif opcionCategoria == 'Tienda 3':
            categorias_tienda3 = calcular_categorias_vendidas(tienda3, "Tienda 3")
            st.subheader("Productos por categoría de Tienda 3")
            st.dataframe(categorias_tienda3)

        elif opcionCategoria == 'Tienda 4':
            categorias_tienda4 = calcular_categorias_vendidas(tienda4, "Tienda 4")
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
                'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
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
                'Tienda 1': calificacion_promedio1,
                'Tienda 2': calificacion_promedio2,
                'Tienda 3': calificacion_promedio3,
                'Tienda 4': calificacion_promedio4
            }

            # Ordenar las calificaciones de mejor a peor
            calificaciones_ordenadas = dict(sorted(calificaciones.items(), key=lambda item: item[1], reverse=True))    

            # Graficar calificación promedio
            graficar_linea(calificaciones)

        # 4 Productos Más y Menos Vendidos
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("4 Productos más y menos Vendidos")

        # 4 Productos más y menos vendidos    
        opcionCategoria = st.selectbox("Selecciona una tienda", ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"])

        # Mostrar el DataFrame de acuerdo a la tienda seleccionada
        if opcionCategoria == "Tienda 1":
            productos_df = productos_mas_menos_vendidos(tienda1, "Tienda 1")
        elif opcionCategoria == "Tienda 2":
            productos_df = productos_mas_menos_vendidos(tienda2, "Tienda 2")
        elif opcionCategoria == "Tienda 3":
            productos_df = productos_mas_menos_vendidos(tienda3, "Tienda 3")
        elif opcionCategoria == "Tienda 4":
            productos_df = productos_mas_menos_vendidos(tienda4, "Tienda 4")

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
                'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
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
            tiendas = ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4']
            costos_envio = [tienda_1_promedio_costo_envio, tienda_2_promedio_costo_envio, tienda_3_promedio_costo_envio, tienda_4_promedio_costo_envio]
            graficar_costo_envio_por_tienda(tiendas, costos_envio)

    # Definir el color de los íconos para cada tienda
    color_tienda1 = 'blue'
    color_tienda2 = 'green'
    color_tienda3 = 'red'
    color_tienda4 = 'purple'

    # Extra    
    if opcion == MENU_MAPA_DIS_GEOGRAFICA:  
        st.subheader("Visualización de la Distribución Geográfica")

        # Usar un selectbox para elegir la tienda
        opcionCategoria = st.selectbox("Selecciona una tienda", ["Tienda 1", "Tienda 2",
             "Tienda 3", "Tienda 4"], key="tienda_mapa")        
        
        if opcionCategoria == "Tienda 1":
            st.write("Mostrando mapa para Tienda 1")
            mapa_tienda1 = crear_mapa(tienda1, "Tienda 1", color_tienda1)            
            html(mapa_tienda1, height=500) 
        elif opcionCategoria == "Tienda 2":
            st.write("Mostrando mapa para Tienda 2")
            mapa_tienda2 = crear_mapa(tienda2, "Tienda 2", color_tienda2)
            html(mapa_tienda2, height=500)
        elif opcionCategoria == "Tienda 3":
            st.write("Mostrando mapa para Tienda 3")
            mapa_tienda3 = crear_mapa(tienda3, "Tienda 3", color_tienda3)
            html(mapa_tienda3, height=500)
        elif opcionCategoria == "Tienda 4":
            st.write("Mostrando mapa para Tienda 4")
            mapa_tienda4 = crear_mapa(tienda4, "Tienda 4", color_tienda4)
            html(mapa_tienda4, height=500)


    if opcion == MENU_MAPA_CALOR:  
        st.subheader("Informe de Recomendación")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("Mapa de Calor")
        # Interfaz de selección de tienda
        opcionCategoria = st.selectbox("Selecciona una tienda para ver el mapa de calor", 
                                    ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"], 
                                    key="tienda_mapa_calor")

        # Mostrar el mapa de calor de la tienda seleccionada
        if opcionCategoria == "Tienda 1":
            st.write("Mostrando mapa de calor para Tienda 1")
            mapa_calor_tienda1 = crear_mapa_calor(tienda1, "Tienda 1",color_tienda1)
            html(mapa_calor_tienda1, height=500)
        elif opcionCategoria == "Tienda 2":
            st.write("Mostrando mapa de calor para Tienda 2")
            mapa_calor_tienda2 = crear_mapa_calor(tienda2, "Tienda 2",color_tienda2)
            html(mapa_calor_tienda2, height=500)
        elif opcionCategoria == "Tienda 3":
            st.write("Mostrando mapa de calor para Tienda 3")
            mapa_calor_tienda3 = crear_mapa_calor(tienda3, "Tienda 3",color_tienda3)
            html(mapa_calor_tienda3, height=500)
        elif opcionCategoria == "Tienda 4":
            st.write("Mostrando mapa de calor para Tienda 4")
            mapa_calor_tienda4 = crear_mapa_calor(tienda4, "Tienda 4",color_tienda4)
            html(mapa_calor_tienda4, height=500)

        st.markdown("<hr>", unsafe_allow_html=True)
        # st.subheader("Análisis Geográfico de Ingresos y Calificaciones")

if __name__ == '__main__':
    main()