import pandas as pd
import numpy as np
from src.read_data import load_data

fileRoute = 'sources/Dataset_Talento.csv'

df = load_data(fileRoute)

if df is not None:
    # Mostrar información general
    print('\nResumen general:')
    print(df.info())
    ## ver primeras filas
    print('\n:Primeras filas:')
    print(df.head())

    # Resumen de valores nulos por columna
    print('\nValores nulos por columna:')
    print(df.isnull().sum())

    # Eliminar filas duplicadas
    filas_antes = df.shape[0]
    df = df.drop_duplicates()
    filas_despues = df.shape[0]
    print(f'\nFilas duplicadas eliminadas: {filas_antes - filas_despues}')

    # Mostrar DataFrame limpio
    print('\nDataFrame limpio (primeras filas):')
    print(df.head())
else:
    print('No se pudo cargar el archivo, revisa la ruta o el formato.')