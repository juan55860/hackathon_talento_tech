import pandas as pd
import numpy as np
from src.read_data import load_data
from src.clean_data import normalize_data
from src.linear_regression import linear_regression
from src.s3_upload import upload_kpi_results


def kpi_productividad_por_operador(df):
    # KPI: Productividad por operador
    kpi_productividad_operador = df.groupby('operador_id').agg({
        'cantidad_producida': 'sum',
        'unidades_defectuosas': 'sum',
        'eficiencia_porcentual': 'mean',
        'operador_id': 'count'
    }).round(2)
    # Calcular tasa de defectos
    kpi_productividad_operador['tasa_defectos'] = (
        kpi_productividad_operador['unidades_defectuosas'] / 
        kpi_productividad_operador['cantidad_producida'] * 100
    ).round(2)
    # Renombrar columnas
    kpi_productividad_operador = kpi_productividad_operador.rename(columns={
        'cantidad_producida': 'total_producido',
        'unidades_defectuosas': 'total_defectuosas',
        'eficiencia_porcentual': 'eficiencia_promedio',
        'operador_id': 'total_registros'
    })

    # Ordenar por productividad total (descendente)
    kpi_productividad_operador = kpi_productividad_operador.sort_values('total_producido', ascending=False)
    filename = './kpis_results/kpi_productividad_por_operador.csv'
    kpi_productividad_operador.to_csv(filename)
    print(f"Resultados guardados en: {filename}")
    
    # Subir a S3
    print("Subiendo archivo a S3...")
    upload_success = upload_kpi_results(filename)
    if upload_success:
        print("✅ Archivo subido exitosamente a S3")
    else:
        print("❌ Error al subir archivo a S3")

    return kpi_productividad_operador


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
    
    # Subir a S3
    print("Subiendo archivo a S3...")
    upload_success = upload_kpi_results(filename)
    if upload_success:
        print("✅ Archivo subido exitosamente a S3")
    else:
        print("❌ Error al subir archivo a S3")

    return kpi_productividad

def main():
    fileRoute = 'sources/Dataset_Talento.csv'
    df = load_data(fileRoute)
    
    if df is not None:
        # Calculo KPIs de productividad por turno y producto
        resulset_kpi_productividad_turno_y_producto = kpi_productividad_turno_y_producto(df)
        print("Productividad por Turno y Producto")
        print("=" * 40)
        print(resulset_kpi_productividad_turno_y_producto)

        # Calculo KPIs de productividad por operador
        resulset_kpi_productividad_por_operador = kpi_productividad_por_operador(df)
        print("Productividad por Operador")
        print("=" * 40)
        print(resulset_kpi_productividad_por_operador)
    else:
        print("No se pudo cargar el archivo para calcular KPIs.")

if __name__ == "__main__":
    main()