import pandas as pd
import numpy as np
from src.read_data import load_data
from src.clean_data import normalize_data
from src.linear_regression import linear_regression

def kpi_productividad_turno_y_producto(df):
    """
    Calcula KPIs de productividad por turno y producto.
    df: DataFrame con los datos de producción
    Returns: DataFrame con los KPIs calculados
    """
    # KPI: Productividad por turno y producto
    kpi_productividad = df.groupby(['turno', 'producto_id']).agg({
        'cantidad_producida': 'sum',
        'unidades_defectuosas': 'sum'
    }).round(2)

    # Calcular tasa de defectos
    kpi_productividad['tasa_defectos'] = (
        kpi_productividad['unidades_defectuosas'] / 
        kpi_productividad['cantidad_producida'] * 100
    ).round(2)

    # Renombrar columnas
    kpi_productividad = kpi_productividad.rename(columns={
        'cantidad_producida': 'total_producido',
        'unidades_defectuosas': 'total_defectuosas'
    })

    # Guardar en archivo CSV con el nombre de la función
    filename = './kpis_results/kpi_productividad_turno_y_producto.csv'
    kpi_productividad.to_csv(filename)
    print(f"Resultados guardados en: {filename}")

    return kpi_productividad

def main():
    fileRoute = 'sources/Dataset_Talento.csv'
    df = load_data(fileRoute)
    
    if df is not None:
        kpis = kpi_productividad_turno_y_producto(df)
        print("Productividad por Turno y Producto")
        print("=" * 40)
        print(kpis)
    else:
        print("No se pudo cargar el archivo para calcular KPIs.")

if __name__ == "__main__":
    main()