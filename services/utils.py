# utils.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def graficar_pie(ingresos):
    # Datos para el gráfico de pie
    labels = ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4']
    sizes = [ingresos[0], ingresos[1], ingresos[2], ingresos[3]]
    
    # Crear el gráfico de pie
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Distribución de Ingresos por Tienda")
    st.pyplot(plt)

def graficar_barras(categorias_tienda1, categorias_tienda2, categorias_tienda3, categorias_tienda4):
    plt.figure(figsize=(12, 8))

    # Graficar barras para Tienda 1
    plt.bar(categorias_tienda1['Categoría'], categorias_tienda1['Cantidad de Productos Vendidos'], label='Tienda 1', alpha=0.7)
    
    # Graficar barras para Tienda 2
    plt.bar(categorias_tienda2['Categoría'], categorias_tienda2['Cantidad de Productos Vendidos'], label='Tienda 2', alpha=0.7)
    
    # Graficar barras para Tienda 3
    plt.bar(categorias_tienda3['Categoría'], categorias_tienda3['Cantidad de Productos Vendidos'], label='Tienda 3', alpha=0.7)
    
    # Graficar barras para Tienda 4
    plt.bar(categorias_tienda4['Categoría'], categorias_tienda4['Cantidad de Productos Vendidos'], label='Tienda 4', alpha=0.7)

    # Configurar el título y las etiquetas
    plt.title('Cantidad de Productos Vendidos por Categoría en Cada Tienda')
    plt.xlabel('Categoría del Producto')
    plt.ylabel('Cantidad de Productos Vendidos')

    # Rotar las etiquetas del eje X si es necesario
    plt.xticks(rotation=45, ha='right')

    # Añadir la leyenda
    plt.legend()

    # Mejorar el espaciado
    plt.tight_layout()

    # Mostrar el gráfico
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
    tiend1_mas_vendidos, tiend1_menos_vendidos = obtener_productos_por_tienda(tienda1, "Tienda 1")
    tiend2_mas_vendidos, tiend2_menos_vendidos = obtener_productos_por_tienda(tienda2, "Tienda 2")
    tiend3_mas_vendidos, tiend3_menos_vendidos = obtener_productos_por_tienda(tienda3, "Tienda 3")
    tiend4_mas_vendidos, tiend4_menos_vendidos = obtener_productos_por_tienda(tienda4, "Tienda 4")

    # Concatenar los datos de las 4 tiendas para los productos más vendidos
    productos_mas_vendidos = pd.concat([tiend1_mas_vendidos, tiend2_mas_vendidos, tiend3_mas_vendidos, tiend4_mas_vendidos])
    
    # Concatenar los datos de las 4 tiendas para los productos menos vendidos
    productos_menos_vendidos = pd.concat([tiend1_menos_vendidos, tiend2_menos_vendidos, tiend3_menos_vendidos, tiend4_menos_vendidos])
    
    # Crear los gráficos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
    
    # Gráfico para los productos más vendidos
    sns.barplot(x='Producto', y='Cantidad de cuotas', hue='Tienda', data=productos_mas_vendidos, ax=ax1)
    ax1.set_title('Productos Más Vendidos por Tienda')
    ax1.set_xlabel('Producto')
    ax1.set_ylabel('Cantidad de Ventas')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')  # Gira las etiquetas del eje X
    
    # Gráfico para los productos menos vendidos
    sns.barplot(x='Producto', y='Cantidad de cuotas', hue='Tienda', data=productos_menos_vendidos, ax=ax2)
    ax2.set_title('Productos Menos Vendidos por Tienda')
    ax2.set_xlabel('Producto')
    ax2.set_ylabel('Cantidad de Ventas')
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')  # Gira las etiquetas del eje X
    
    plt.tight_layout()
    #plt.show()
    st.pyplot(plt)


def graficar_costo_envio_por_tienda(tiendas, costos_envio):
    """
    Crear y mostrar un gráfico de barras horizontal de los promedios de costo de envío por tienda.
    
    tiendas: List[str]
        Lista con los nombres de las tiendas.
    
    costos_envio: List[float]
        Lista con los promedios de costo de envío correspondientes a cada tienda.
    """
    # Crear el gráfico de barras horizontal
    plt.figure(figsize=(8, 6))
    plt.barh(tiendas, costos_envio, color='skyblue')

    # Agregar títulos y etiquetas
    plt.title('Promedio de Costo de Envío por Tienda', fontsize=14)
    plt.xlabel('Promedio Costo de Envío (en moneda)', fontsize=12)
    plt.ylabel('Tienda', fontsize=12)

    # Mostrar los valores sobre las barras
    for i, valor in enumerate(costos_envio):
        plt.text(valor + 300, i, f'{valor:.2f}', va='center', fontsize=10)

    # Mostrar el gráfico
    #plt.show()
    st.pyplot(plt)