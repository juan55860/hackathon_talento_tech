import pandas as pd
from src.s3_upload import upload_kpi_results

def kpi_falla_de_maquina_por_turno(df):
    kpi_fallas_turno = df[df['fallo_detectado'] == 'Sí'].groupby('turno').agg({
        'maquina_id': 'count',
        'tipo_fallo': 'value_counts'
    }).round(2)

    # Renombrar columnas
    kpi_fallas_turno = kpi_fallas_turno.rename(columns={
        'maquina_id': 'total_fallas'
    })

    print("Fallas de Máquina por Turno")
    print("=" * 40)
    print(kpi_fallas_turno)

    # Guardar en archivo CSV
    filename = './kpis_results/kpi_falla_de_maquina_por_turno.csv'
    kpi_fallas_turno.to_csv(filename)
    print(f"Resultados guardados en: {filename}")
    
    # Subir a S3
    print("Subiendo archivo a S3...")
    upload_success = upload_kpi_results(filename)
    if upload_success:
        print("✅ Archivo subido exitosamente a S3")
    else:
        print("❌ Error al subir archivo a S3")

    return kpi_fallas_turno 