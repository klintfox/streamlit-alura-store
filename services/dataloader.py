# data_loader.py
import pandas as pd 
import requests
from io import StringIO
 
def cargar_csv(url):
    " Función para verificar si la URL devuelve datos correctos "

    response = requests.get(url)  # Hacer una solicitud GET para obtener el archivo
    if response.status_code == 200:  # Verificar si la respuesta fue exitosa
        print(f"Éxito: Datos obtenidos desde {url}")
        return pd.read_csv(StringIO(response.text))  # Cargar el CSV desde el texto de la respuesta
    else:
        print(f"Error: No se pudo obtener los datos desde {url}, código de estado: {response.status_code}")
        return None
