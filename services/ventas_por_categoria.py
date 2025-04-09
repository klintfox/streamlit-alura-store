# ventas_por_categoria.py
import pandas as pd

def calcular_categorias_vendidas(df, tienda_name):
    """Calcular la cantidad de productos vendidos por categoría."""
    categorias_vendidas = df.groupby('Categoría del Producto')['Precio'].count().sort_values(ascending=False)
    categorias_vendidas_df = categorias_vendidas.reset_index()
    categorias_vendidas_df.columns = ['Categoría', 'Cantidad de Productos Vendidos']
    return categorias_vendidas_df
