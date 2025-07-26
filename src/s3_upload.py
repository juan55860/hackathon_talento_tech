import boto3
import os
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de credenciales AWS desde variables de entorno
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME', 'hackathon-juankers')

def upload_to_s3(file_path, bucket_name=None, s3_key=None, make_public=True):
    """
    Sube un archivo a AWS S3.
    
    Args:
        file_path (str): Ruta local del archivo a subir
        bucket_name (str): Nombre del bucket de S3 (opcional, usa el valor por defecto)
        s3_key (str): Clave/nombre del archivo en S3 (opcional, usa el nombre del archivo si no se especifica)
        make_public (bool): Si True, intenta hacer el archivo público (depende de la configuración del bucket)
    
    Returns:
        bool: True si se subió exitosamente, False en caso contrario
    """
    try:
        # Usar bucket por defecto si no se especifica
        if bucket_name is None:
            bucket_name = S3_BUCKET_NAME
            
        # Verificar que las credenciales estén configuradas
        if not AWS_ACCESS_KEY or not AWS_SECRET_KEY:
            print("❌ Error: Credenciales de AWS no configuradas en el archivo .env")
            print("Verifica que AWS_ACCESS_KEY y AWS_SECRET_KEY estén definidos")
            return False
        
        # Crear sesión con credenciales específicas
        session = boto3.Session(
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=AWS_REGION
        )
        
        # Crear cliente S3 con la sesión
        s3_client = session.client('s3')
        
        # Si no se especifica s3_key, usar el nombre del archivo
        if s3_key is None:
            s3_key = os.path.basename(file_path)
        
        # Leer el archivo
        with open(file_path, 'rb') as file_data:
            # Configurar parámetros de subida (sin ACL)
            upload_params = {
                'Bucket': bucket_name,
                'Key': s3_key,
                'Body': file_data
            }
            
            # Subir archivo
            s3_client.put_object(**upload_params)
        
        # Generar URL (el bucket debe estar configurado como público)
        url = f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"
        print(f"✅ Archivo subido exitosamente a s3://{bucket_name}/{s3_key}")
        print(f"🌐 URL: {url}")
        print("ℹ️  Nota: Si el bucket no es público, la URL puede no ser accesible")
        
        return True
        
    except NoCredentialsError:
        print("❌ Error: No se encontraron credenciales de AWS")
        print("Verifica que AWS_ACCESS_KEY y AWS_SECRET_KEY estén configurados correctamente en .env")
        return False
        
    except ClientError as e:
        print(f"❌ Error de AWS: {e}")
        return False
        
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {file_path}")
        return False
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def upload_kpi_results(file_path, bucket_name=None):
    """
    Función específica para subir resultados de KPIs a S3.
    
    Args:
        file_path (str): Ruta del archivo CSV de KPIs
        bucket_name (str): Nombre del bucket (opcional, usa el valor por defecto)
    
    Returns:
        bool: True si se subió exitosamente
    """
    # Usar el nombre del archivo sin timestamp
    filename = os.path.basename(file_path)
    name_without_ext = os.path.splitext(filename)[0]
    s3_key = f"kpis/{name_without_ext}.csv"
    
    return upload_to_s3(file_path, bucket_name, s3_key, make_public=True) 