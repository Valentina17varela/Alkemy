"""
CHALLENGE DATA ANALYTICS CON PYTHON
Author: Valentina Varela Alzate
"""

import userInterface
import dataCollector


def run():
    
    userInterface.menu_principal()
    
    museos = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'
    
    cines = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
    
    bibliotecas = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'
 
    # Reading and storing data
    museos_csv = dataCollector.obtener_datos(museos,'museos')
    cines_csv = dataCollector.obtener_datos(cines,'cines')
    bibliotecas_csv = dataCollector.obtener_datos(bibliotecas,'bibliotecas')
    
    # Data processing and table normalization
    unica, conjuntos, info_cines = dataCollector.procesar_datos(museos_csv,cines_csv,bibliotecas_csv)


if __name__ == '__main__':
    run()