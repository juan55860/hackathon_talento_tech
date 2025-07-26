# Visualizacion de Datos

Authors: Juan David Arias - Juan Camilo Varela


# Datos

`` sh
{
    "timestamp": "YYYY-MM-DD hh:mm:ss" required,
    "turno": ENUM: "Mañana", "Tarde","Noche" required,
    "operador_id": "OP_" required
    "maquina_id" : "M_1" to "M_10", required
    "producto_id": "P_", required
    "temperatura": decimal ? -> 5820
    "vibración": decimal ?
    "humedad": decimal ?
    "tiempo_ciclo": decimal ?
    "fallo_detectado": "Sí" "No",
    "tipo_fallo": "Eléctrico", "Mecánico", "nan",
    "cantidad_producida" : integer
    "unidades_defectuosas": integer,
    "eficiencia_porcentual": decimal,
    "consumo_energia": decimal,
    "paradas_programadas" : integer,
    "paradas_imprevistas" : integer,
    "observaciones": text
}

``