# 🏭 Analizados de KPIS 
## Análisis de Datos Industriales - Proyecto Talento Tech

## 📋 Información del Proyecto

**Grupo:** Juankers  
**Autores:** Juan David Arias - Juan Camilo Varela  
**Descripción:** Sistema de análisis de datos industriales con KPIs, regresión lineal y almacenamiento en la nube.

---

## 🚀 Características Principales

- 📊 **Análisis Exploratorio de Datos (EDA)** completo
- 🎯 **KPIs Industriales** automatizados
- ☁️ **Almacenamiento en AWS S3** con URLs públicas
- 🔧 **Modular y Escalable** - fácil agregar nuevos análisis
- 🔒 **Configuración Segura** con variables de entorno

---

## 📁 Estructura del Proyecto

```
hackaton/
├── main.py                          # Script principal
├── kpis.py                          # Gestor de KPIs
├── requirements.txt                 # Dependencias
├── .env                            # Variables de entorno
├── .gitignore                      # Archivos ignorados
├── src/                            # Módulos del proyecto
│   ├── read_data.py               # Carga de datos
│   ├── clean_data.py              # Limpieza y normalización
│   ├── linear_regression.py       # Regresión lineal
│   ├── s3_upload.py               # Subida a AWS S3
│   ├── kpi_productividad_operador.py
│   ├── kpi_productividad_turno_producto.py
│   ├── kpi_falla_de_maquina_por_turno.py
│   └── kpi_falla_de_maquina_por_producto.py
├── sources/                        # Datos de entrada
│   └── Dataset_Talento.csv
├── kpis_results/                   # Resultados locales
└── metabase_data/                  # Datos para Metabase
```

---

## 📊 Esquema de Datos

El dataset contiene información de producción industrial con las siguientes columnas:

| Campo | Tipo | Descripción | Requerido |
|-------|------|-------------|-----------|
| `timestamp` | datetime | Fecha y hora del registro | ✅ |
| `turno` | enum | "Mañana", "Tarde", "Noche" | ✅ |
| `operador_id` | string | ID del operador (OP_XX) | ✅ |
| `maquina_id` | string | ID de la máquina (M_1 a M_10) | ✅ |
| `producto_id` | string | ID del producto (P_XX) | ✅ |
| `temperatura` | decimal | Temperatura de operación | ❌ |
| `vibración` | decimal | Nivel de vibración | ❌ |
| `humedad` | decimal | Humedad ambiental | ❌ |
| `tiempo_ciclo` | decimal | Tiempo del ciclo de producción | ❌ |
| `fallo_detectado` | enum | "Sí" o "No" | ✅ |
| `tipo_fallo` | enum | "Eléctrico", "Mecánico", "nan" | ❌ |
| `cantidad_producida` | integer | Unidades producidas | ✅ |
| `unidades_defectuosas` | integer | Unidades defectuosas | ✅ |
| `eficiencia_porcentual` | decimal | Porcentaje de eficiencia | ❌ |
| `consumo_energia` | decimal | Consumo energético | ❌ |
| `paradas_programadas` | integer | Número de paradas programadas | ✅ |
| `paradas_imprevistas` | integer | Número de paradas imprevistas | ✅ |
| `observaciones` | text | Observaciones adicionales | ❌ |

---

## ⚙️ Configuración

### 1. Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

```bash
# AWS S3 Credentials
AWS_ACCESS_KEY=""
AWS_SECRET_KEY=""
AWS_REGION=""
# S3 Bucket Configuration
S3_BUCKET_NAME=hackathon-juankers
# Data Source
DATA_FILE_PATH=sources/Dataset_Talento.csv
```

### 2. Instalación de Dependencias

```bash
pip3 install -r requirements.txt
```
---

## ⚙️ Uso

```bash
python3 main.py
```

Esto ejecutará:
1. **EDA** - Análisis exploratorio de datos
2. **Normalizacion de datos** - Normalización de datos
2. **KPIs** - Cálculo de indicadores clave
4. **Subida a S3** - Almacenamiento en la nube

---

## 📈 KPIs Disponibles

### 1. **Productividad por Turno y Producto**
- Total producido por turno y producto
- Tasa de defectos
- Análisis de eficiencia

### 2. **Productividad por Operador**
- Rendimiento individual de operadores
- Eficiencia promedio
- Ranking de productividad

### 3. **Fallas de Máquina por Turno**
- Análisis de fallos por turno
- Tipos de fallo más comunes
- Impacto en eficiencia

### 4. **Fallas de Máquina por Producto**
- Fallos específicos por producto
- Tasa de fallos
- Análisis de costos por defecto

---

## ☁️ Almacenamiento en AWS S3

Los resultados se almacenan automáticamente en S3 con URLs públicas:

- **Archivos CSV** con resultados de KPIs
- **URLs accesibles** para compartir con el equipo
- **Sin timestamp** - siempre el archivo más reciente
- **Estructura organizada** en carpetas por tipo de KPI


## Visuzalizacion de datos en Quicksight

Los gráficos podran verse en QuickSight de AWS, nota se adjunta un pdf de como se verian los datos en caso de que no se cuente temporalmente con el acceso

---

## 🔧 Funcionalidades Técnicas

### Análisis de Datos
- ✅ Detección automática de tipos de datos
- ✅ Identificación de valores nulos
- ✅ Eliminación de duplicados
- ✅ Normalización de variables numéricas

### Infraestructura
- ✅ Configuración segura con variables de entorno
- ✅ Subida automática a AWS S3
- ✅ Código modular y reutilizable
- ✅ Información en el dashboard de Quicksight

---

## 📞 Contáctanos

**Juan David Arias** - [@juanarias14](https://github.com/juanarias14)  ari_juan14@hotmail.com
**Juan Camilo Varela** - [@juan55860](https://github.com/juan55860) juan55860@gmail.com

Proyecto Link: [https://github.com/juankers/hackaton-talento-tech](https://github.com/juankers/hackaton-talento-tech)