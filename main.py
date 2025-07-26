import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from src.read_data import load_data
from src.clean_data import normalize_data
from src.linear_regression import linear_regression
from kpis import run_kpis

# Cargar variables de entorno
load_dotenv()

# Obtener ruta del archivo desde variables de entorno
fileRoute = os.getenv('DATA_FILE_PATH', 'sources/Dataset_Talento.csv')

df = load_data(fileRoute)

if df is not None:

    # EDA: analisis exploratorio de datos
    # Mostrar información general
    print('\n📊EDA análisis exploratorio de datos:')
    print(df.info())

    # Identificando tipos de datos por columna y cuantos valores únicos hay
    print('\n📊Tipo de datos por columna y valores únicos:')
    n_rows = len(df)
    for col in df.columns:
        dtype = df[col].dtype
        n_unique = df[col].nunique(dropna=False)
        if dtype in ['int64', 'int32']:
            tipo = 'int'
        elif dtype in ['float64', 'float32']:
            tipo = 'float/double'
        elif dtype in ['object', 'category'] or n_unique < 0.1 * n_rows:
            tipo = 'enum/categorica'
        else:
            tipo = str(dtype)
        print(f'- {col}: {tipo} (dtype: {dtype}, unicos: {n_unique})')

    # Resumen de valores nulos por columna
    print('\n 📊Valores nulos por columna:')
    print(df.isnull().sum())

    # Eliminar filas duplicadas
    filas_antes = df.shape[0]
    df = df.drop_duplicates()
    filas_despues = df.shape[0]
    print(f'\n📊Filas duplicadas eliminadas: {filas_antes - filas_despues}')

    # Regresión lineal
    # print('\n📈 Regresión lineal:')
    # Usar temperatura como variable independiente y eficiencia_porcentual como dependiente
    #df_clean = df[['temperatura', 'eficiencia_porcentual']].dropna()
    #if len(df_clean) > 0:
    #    modelo = linear_regression(df_clean, 'temperatura', 'eficiencia_porcentual')
    #else:
    #    print("No hay suficientes datos para realizar la regresión lineal.")

    # Ejecutar KPIs
    print('\n📊 Ejecutando KPIs...')
    run_kpis(df)

else:
    print('No se pudo cargar el archivo, revisa la ruta o el formato.')