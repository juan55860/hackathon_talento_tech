import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        print('Archivo cargado correctamente.')
        return df
    except FileNotFoundError:
        print(f'Error: El archivo {path} no existe.')
        return None
    except pd.errors.ParserError:
        print('Error: Problema al parsear el archivo CSV.')
        return None
    except Exception as e:
        print(f'Error inesperado: {e}')
        return None 