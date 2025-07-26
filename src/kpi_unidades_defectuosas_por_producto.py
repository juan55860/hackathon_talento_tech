import pandas as pd
from src.s3_upload import upload_kpi_results

def kpi_unidades_defectuosas_por_producto(df):
    kpi_defectuosas_producto = df.groupby('producto_id').agg({
        'unidades_defectuosas': 'sum',
        'cantidad_producida': 'sum',
        'producto_id': 'count'
    }).round(2)

    # Calcular tasa de defectos
    kpi_defectuosas_producto['tasa_defectos'] = (
        kpi_defectuosas_producto['unidades_defectuosas'] / 
        kpi_defectuosas_producto['cantidad_producida'] * 100
    ).round(2)

    # Renombrar columnas
    kpi_defectuosas_producto = kpi_defectuosas_producto.rename(columns={
        'unidades_defectuosas': 'total_defectuosas',
        'cantidad_producida': 'total_producido',
        'producto_id': 'total_registros'
    })

    # Ordenar por total de defectuosas (descendente)
    kpi_defectuosas_producto = kpi_defectuosas_producto.sort_values('total_defectuosas', ascending=False)

    print("Unidades Defectuosas por Producto")
    print("=" * 40)
    print(kpi_defectuosas_producto)

    # Guardar en archivo CSV
    filename = './kpis_results/kpi_unidades_defectuosas_por_producto.csv'
    kpi_defectuosas_producto.to_csv(filename)
    print(f"Resultados guardados en: {filename}")
    
    # Subir a S3
    print("Subiendo archivo a S3...")
    upload_success = upload_kpi_results(filename)
    if upload_success:
        print("✅ Archivo subido exitosamente a S3")
    else:
        print("❌ Error al subir archivo a S3")

    return kpi_defectuosas_producto