# facturacion.py
import pandas as pd

def calcular_ingreso_total(tienda):
    """Calcular el ingreso total de una tienda."""
    if tienda is not None:
        return tienda['Precio'].sum()
    return 0
