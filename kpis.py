import pandas as pd
import numpy as np
from src.read_data import load_data
from src.clean_data import normalize_data
from src.linear_regression import linear_regression
from src.kpi_productividad_operador import kpi_productividad_por_operador
from src.kpi_productividad_turno_producto import kpi_productividad_turno_y_producto
from src.kpi_falla_de_maquina_por_turno import kpi_falla_de_maquina_por_turno
from src.kpi_falla_de_maquina_por_producto import kpi_falla_de_maquina_por_producto


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
        print("No se pudo cargar el archivo para calcular los KPIs.")

if __name__ == "__main__":
    main()