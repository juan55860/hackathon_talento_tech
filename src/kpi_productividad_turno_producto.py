import pandas as pd
from src.s3_upload import upload_kpi_results

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

    # Guardar en archivo CSV
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