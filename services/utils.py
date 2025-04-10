# utils.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
from config import COLOR_TIENDA_1, COLOR_TIENDA_2, COLOR_TIENDA_3, COLOR_TIENDA_4
from config import TIENDA1, TIENDA2, TIENDA3, TIENDA4, TIENDAS

def graficar_pie(ingresos):
    # Datos para el gráfico de pie
    labels = TIENDAS
    sizes = [ingresos[0], ingresos[1], ingresos[2], ingresos[3]]

    # Colores personalizados
    colores = [COLOR_TIENDA_1, COLOR_TIENDA_2, COLOR_TIENDA_3, COLOR_TIENDA_4]
    
    # Crear el gráfico de pie
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, colors=colores, autopct='%1.1f%%', startangle=140)
    plt.title("Distribución de Ingresos por Tienda")
    st.pyplot(plt)

def graficar_barras(cat1, cat2, cat3, cat4):
    # Asegurar que todas tengan las mismas categorías y orden
    categorias = cat1['Categoría'].tolist()

    # Extraer los valores de cada tienda
    valores1 = cat1['Cantidad de Productos Vendidos'].tolist()
    valores2 = cat2['Cantidad de Productos Vendidos'].tolist()
    valores3 = cat3['Cantidad de Productos Vendidos'].tolist()
    valores4 = cat4['Cantidad de Productos Vendidos'].tolist()

    x = np.arange(len(categorias))  # Posiciones para cada grupo
    width = 0.2  # Ancho de cada barra

    plt.figure(figsize=(12, 6))
    plt.bar(x - 1.5*width, valores1, width, label=TIENDA1, color=COLOR_TIENDA_1)
    plt.bar(x - 0.5*width, valores2, width, label=TIENDA2, color=COLOR_TIENDA_2)
    plt.bar(x + 0.5*width, valores3, width, label=TIENDA3, color=COLOR_TIENDA_3)
    plt.bar(x + 1.5*width, valores4, width, label=TIENDA4, color=COLOR_TIENDA_4)

    plt.xlabel('Categoría del Producto')
    plt.ylabel('Cantidad de Productos Vendidos')
    plt.title('Cantidad de Productos Vendidos por Categoría en Cada Tienda')
    plt.xticks(x, categorias, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)


def graficar_linea(calificaciones_ordenadas):
    """Generar un gráfico de línea de las calificaciones promedio por tienda."""
    plt.figure(figsize=(10,6))
    plt.plot(calificaciones_ordenadas.keys(), calificaciones_ordenadas.values(), marker='o', linestyle='-', color='b', alpha=0.7, linewidth=2)
    plt.title('Calificación Promedio por Tienda (Gráfico de Línea)', fontsize=16)
    plt.xlabel('Tienda', fontsize=14)
    plt.ylabel('Calificación Promedio', fontsize=14)
    #plt.show()
    st.pyplot(plt)

def obtener_productos_por_tienda(tienda, tienda_nombre):
    """
    Obtener los productos más y menos vendidos por tienda.
    
    tienda: DataFrame
        El DataFrame de la tienda que contiene las columnas 'Producto' y 'Cantidad de cuotas'.
    
    tienda_nombre: str
        El nombre de la tienda para identificarla en los resultados.
    
    Retorna dos DataFrames: productos más vendidos y productos menos vendidos.
    """
    # Agrupar los datos por 'Producto' y sumar la cantidad de ventas
    productos_ventas = tienda.groupby('Producto')['Cantidad de cuotas'].sum().reset_index()
    
    # Ordenar por la cantidad de ventas en orden descendente
    productos_ventas = productos_ventas.sort_values(by='Cantidad de cuotas', ascending=False)
    
    # Obtener los 5 productos más vendidos
    productos_mas_vendidos = productos_ventas.head(5)
    productos_mas_vendidos['Tienda'] = tienda_nombre
    
    # Obtener los 5 productos menos vendidos
    productos_menos_vendidos = productos_ventas.tail(5)
    productos_menos_vendidos['Tienda'] = tienda_nombre
    
    return productos_mas_vendidos, productos_menos_vendidos

def graficar_productos_mas_menos_vendidos(tienda1, tienda2, tienda3, tienda4):
    """
    Crear y mostrar los gráficos de los productos más y menos vendidos por tienda.
    """
    # Obtener los productos más y menos vendidos para cada tienda
    tiend1_mas_vendidos, tiend1_menos_vendidos = obtener_productos_por_tienda(tienda1, TIENDA1)
    tiend2_mas_vendidos, tiend2_menos_vendidos = obtener_productos_por_tienda(tienda2, TIENDA2)
    tiend3_mas_vendidos, tiend3_menos_vendidos = obtener_productos_por_tienda(tienda3, TIENDA3)
    tiend4_mas_vendidos, tiend4_menos_vendidos = obtener_productos_por_tienda(tienda4, TIENDA4)

    # Concatenar los datos de las 4 tiendas para los productos más vendidos
    productos_mas_vendidos = pd.concat([tiend1_mas_vendidos, tiend2_mas_vendidos, tiend3_mas_vendidos, tiend4_mas_vendidos])
    
    # Concatenar los datos de las 4 tiendas para los productos menos vendidos
    productos_menos_vendidos = pd.concat([tiend1_menos_vendidos, tiend2_menos_vendidos, tiend3_menos_vendidos, tiend4_menos_vendidos])
    
    # Crear los gráficos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    colores_tienda = {
    'Tienda 1': COLOR_TIENDA_1,
    'Tienda 2': COLOR_TIENDA_2,
    'Tienda 3': COLOR_TIENDA_3,
    'Tienda 4': COLOR_TIENDA_4
}
    
    # Gráfico para los productos más vendidos
    sns.barplot(x='Producto', y='Cantidad de cuotas', hue='Tienda', data=productos_mas_vendidos, ax=ax1,
                palette=colores_tienda)  # Usar la paleta de colores personalizada
    ax1.set_title('Productos Más Vendidos por Tienda')
    ax1.set_xlabel('Producto')
    ax1.set_ylabel('Cantidad de Ventas')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')  # Gira las etiquetas del eje X
    
    # Gráfico para los productos menos vendidos
    sns.barplot(x='Producto', y='Cantidad de cuotas', hue='Tienda', data=productos_menos_vendidos, ax=ax2,
                palette=colores_tienda)  # Usar la paleta de colores personalizada
    ax2.set_title('Productos Menos Vendidos por Tienda')
    ax2.set_xlabel('Producto')
    ax2.set_ylabel('Cantidad de Ventas')
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')  # Gira las etiquetas del eje X
    
    plt.tight_layout()
    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)


def graficar_costo_envio_por_tienda(tiendas, costos_envio):
    """
    Crear y mostrar un gráfico de barras horizontal de los promedios de costo de envío por tienda.
    
    tiendas: List[str]
        Lista con los nombres de las tiendas.
    
    costos_envio: List[float]
        Lista con los promedios de costo de envío correspondientes a cada tienda.
    """
    # Diccionario de colores por tienda
    COLORES_TIENDA = {
        'Tienda 1': COLOR_TIENDA_1,
        'Tienda 2': COLOR_TIENDA_2,
        'Tienda 3': COLOR_TIENDA_3,
        'Tienda 4': COLOR_TIENDA_4
    }

    # Crear una lista de colores para las barras según el nombre de cada tienda
    colores = [COLORES_TIENDA[tienda] for tienda in tiendas]

    # Crear el gráfico de barras horizontal
    plt.figure(figsize=(8, 6))
    plt.barh(tiendas, costos_envio, color=colores)

    # Agregar títulos y etiquetas
    plt.title('Promedio de Costo de Envío por Tienda', fontsize=14)
    plt.xlabel('Promedio Costo de Envío (en moneda)', fontsize=12)
    plt.ylabel('Tienda', fontsize=12)

    # Mostrar los valores sobre las barras
    for i, valor in enumerate(costos_envio):
        plt.text(valor + 300, i, f'{valor:.2f}', va='center', fontsize=10)

    # Mostrar el gráfico
    st.pyplot(plt)