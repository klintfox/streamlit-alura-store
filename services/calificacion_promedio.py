# calificacion_promedio.py
import pandas as pd

def calcular_calificacion_promedio(tienda):
    """Calcular la calificación promedio de una tienda."""
    if tienda is not None:
        return tienda['Calificación'].mean()
    return 0
