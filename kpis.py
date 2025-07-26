from src.kpi_productividad_operador import kpi_productividad_por_operador
from src.kpi_productividad_turno_producto import kpi_productividad_turno_y_producto
from src.kpi_falla_de_maquina_por_turno import kpi_falla_de_maquina_por_turno
from src.kpi_falla_de_maquina_por_producto import kpi_falla_de_maquina_por_producto

def run_kpis(df):
    """
    Ejecuta todos los KPIs con el DataFrame proporcionado.
    df: DataFrame con los datos de producción
    """
    if df is not None and len(df) > 0:
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

        # Calculo KPIs de falla de máquina por turno
        resulset_kpi_falla_de_maquina_por_turno = kpi_falla_de_maquina_por_turno(df)
        print("Fallas de Máquina por Turno")
        print("=" * 40)
        print(resulset_kpi_falla_de_maquina_por_turno)

        # calculo KPIs de falla de máquina por producto
        resulset_kpi_falla_de_maquina_por_producto = kpi_falla_de_maquina_por_producto(df)
        print("Fallas de Máquina por Producto")
        print("=" * 40)
        print(resulset_kpi_falla_de_maquina_por_producto)
    else:
        print("No se pudo calcular los KPIs: DataFrame vacío o nulo.")