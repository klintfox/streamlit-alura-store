# costo_envio_por_tienda.py

def calcular_promedio_costo_envio(tienda):
    """
    Calcular el promedio de costo de envío por tienda.

    tienda: DataFrame
        El DataFrame de la tienda que contiene la columna 'Costo de envío'.
    
    Retorna el promedio redondeado a 2 decimales.
    """
    # Calculamos el promedio de la columna 'Costo de envío' y lo redondeamos a 2 decimales
    costo_envio_promedio = round(tienda['Costo de envío'].mean(), 2)
    return costo_envio_promedio
