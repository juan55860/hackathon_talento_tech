import pandas as pd
from src.s3_upload import upload_kpi_results

def kpi_productividad_por_operador(df):
    """
    Calcula KPIs de productividad por operador.
    df: DataFrame con los datos de producción
    Returns: DataFrame con los KPIs calculados
    """
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
    
    # Guardar en archivo CSV
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