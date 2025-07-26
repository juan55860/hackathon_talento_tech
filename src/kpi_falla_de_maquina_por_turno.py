import pandas as pd
from src.s3_upload import upload_kpi_results

def kpi_falla_de_maquina_por_turno(df):
    """
    Calcula KPIs de fallas de máquina por turno.
    df: DataFrame con los datos de producción
    Returns: DataFrame con los KPIs calculados
    """
    # Filtrar solo registros con fallos detectados
    df_fallas = df[df['fallo_detectado'] == 'Sí'].copy()
    
    if len(df_fallas) == 0:
        print("No se encontraron fallos detectados en los datos.")
        return pd.DataFrame()
    
    # KPI: Fallas por turno
    kpi_fallas_turno = df_fallas.groupby('turno').agg({
        'maquina_id': 'count',  # Total de fallos
        'tipo_fallo': 'value_counts'  # Tipos de fallo
    }).round(2)
    
    # Calcular estadísticas adicionales
    kpi_fallas_turno_detailed = df_fallas.groupby('turno').agg({
        'maquina_id': 'count',
        'tipo_fallo': lambda x: x.value_counts().to_dict(),
        'eficiencia_porcentual': 'mean',
        'tiempo_ciclo': 'mean'
    }).round(2)
    
    # Renombrar columnas
    kpi_fallas_turno_detailed = kpi_fallas_turno_detailed.rename(columns={
        'maquina_id': 'total_fallas',
        'eficiencia_porcentual': 'eficiencia_promedio_con_fallas',
        'tiempo_ciclo': 'tiempo_ciclo_promedio_con_fallas'
    })
    
    # Guardar en archivo CSV
    filename = './kpis_results/kpi_falla_de_maquina_por_turno.csv'
    kpi_fallas_turno_detailed.to_csv(filename)
    print(f"Resultados guardados en: {filename}")
    
    # Subir a S3
    print("Subiendo archivo a S3...")
    upload_success = upload_kpi_results(filename)
    if upload_success:
        print("✅ Archivo subido exitosamente a S3")
    else:
        print("❌ Error al subir archivo a S3")

    return kpi_fallas_turno_detailed 