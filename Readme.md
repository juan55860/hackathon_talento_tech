# Análisis de Datos

Group:   Juankers
Authors: Juan David Arias - Juan Camilo Varela

# Exploración de Datos (Exploratory Data Analysis)

``` sh
{
    "timestamp": "YYYY-MM-DD hh:mm:ss" required*,
    "turno": ENUM: "Mañana", "Tarde","Noche" required*,
    "operador_id": "OP_" required*,
    "maquina_id" : "M_1" to "M_10", required*,
    "producto_id": "P_", required*,
    "temperatura": decimal 
    "vibración": decimal 
    "humedad": decimal 
    "tiempo_ciclo": decimal
    "fallo_detectado": "Sí" "No" required*,
    "tipo_fallo": "Eléctrico", "Mecánico", "nan",
    "cantidad_producida" : integer required*
    "unidades_defectuosas": integer required*,
    "eficiencia_porcentual": decimal,
    "consumo_energia": decimal,
    "paradas_programadas" : integer required*,
    "paradas_imprevistas" : integer required*,
    "observaciones": text
}

```

## Create .env file with this content

```sh
AWS_ACCESS_KEY=
AWS_SECRET_KEY=
AWS_REGION=
S3_BUCKET_NAME=
DATA_FILE_PATH=sources/Dataset_Talento.csv
```

## Install dependencies

## Run project 

```sh
python3 main.py
```
