# productos.py

import pandas as pd

def productos_mas_menos_vendidos(tienda, tienda_nombre):
    """
    Calcular y mostrar los productos más y menos vendidos de una tienda.

    tienda: DataFrame
        El DataFrame de la tienda que contiene las columnas 'Producto' y 'Cantidad de cuotas'.

    tienda_nombre: str
        El nombre de la tienda para imprimir en los resultados.
    """
    # Contar el número de ventas por producto
    productos_ventas = tienda.groupby('Producto')['Cantidad de cuotas'].sum().reset_index()

    # Ordenar los productos de mayor a menor cantidad de ventas
    productos_ventas = productos_ventas.sort_values(by='Cantidad de cuotas', ascending=False)

    # Productos más vendidos (Top 5)
    productos_mas_vendidos = productos_ventas.head(5)

    # Productos menos vendidos (con al menos una venta, Top 5)
    productos_menos_vendidos = productos_ventas.tail(5)

    # Concatenar los productos más y menos vendidos
    productos_completos = pd.concat([productos_mas_vendidos, productos_menos_vendidos])
    productos_completos['Tienda'] = tienda_nombre  # Agregar la tienda para identificar la tienda

    return productos_completos