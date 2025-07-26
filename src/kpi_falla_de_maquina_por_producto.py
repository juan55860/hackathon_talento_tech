import pandas as pd
from src.s3_upload import upload_kpi_results

def kpi_falla_de_maquina_por_producto(df):
    """
    Calcula KPIs de fallas de máquina por producto.
    df: DataFrame con los datos de producción
    Returns: DataFrame con los KPIs calculados
    """
    # Filtrar solo registros con fallos detectados
    df_fallas = df[df['fallo_detectado'] == 'Sí'].copy()
    
    if len(df_fallas) == 0:
        print("No se encontraron fallos detectados en los datos.")
        return pd.DataFrame()
    
    # KPI: Fallas por producto
    kpi_fallas_producto = df_fallas.groupby('producto_id').agg({
        'maquina_id': 'count',  # Total de fallos
        'tipo_fallo': lambda x: x.value_counts().to_dict(),  # Tipos de fallo
        'eficiencia_porcentual': 'mean',
        'tiempo_ciclo': 'mean',
        'cantidad_producida': 'sum',
        'unidades_defectuosas': 'sum'
    }).round(2)
    
    # Calcular tasa de fallos por producto
    total_produccion_por_producto = df.groupby('producto_id')['cantidad_producida'].sum()
    kpi_fallas_producto['tasa_fallos'] = (
        kpi_fallas_producto['maquina_id'] / total_produccion_por_producto * 100
    ).round(2)
    
    # Renombrar columnas
    kpi_fallas_producto = kpi_fallas_producto.rename(columns={
        'maquina_id': 'total_fallas',
        'eficiencia_porcentual': 'eficiencia_promedio_con_fallas',
        'tiempo_ciclo': 'tiempo_ciclo_promedio_con_fallas',
        'cantidad_producida': 'produccion_con_fallas',
        'unidades_defectuosas': 'defectuosas_con_fallas'
    })
    
    # Ordenar por total de fallos (descendente)
    kpi_fallas_producto = kpi_fallas_producto.sort_values('total_fallas', ascending=False)
    
    # Guardar en archivo CSV
    filename = './kpis_results/kpi_falla_de_maquina_por_producto.csv'
    kpi_fallas_producto.to_csv(filename)
    print(f"Resultados guardados en: {filename}")
    
    # Subir a S3
    print("Subiendo archivo a S3...")
    upload_success = upload_kpi_results(filename)
    if upload_success:
        print("✅ Archivo subido exitosamente a S3")
    else:
        print("❌ Error al subir archivo a S3")

    return kpi_fallas_producto 