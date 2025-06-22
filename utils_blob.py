import os
from azure.storage.blob import BlobServiceClient, ContentSettings
import pandas as pd
from io import StringIO

print("HOLAAAAAAAAAAAAAAAAAAA")

# Obtener conexión desde variable de entorno
BLOB_CONN_STR = os.getenv("BLOB_CONN_STR")
if not BLOB_CONN_STR:
    raise ValueError("La variable de entorno 'BLOB_CONN_STR' no está definida.")

# Parámetros fijos
CONTAINER_NAME = "data-pipeline-1"

print("HOLAAAAAA 2")

# Crear cliente de contenedor
blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONN_STR)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# Función para leer CSV desde Blob a DataFrame
def download_blob_to_df(blob_path):
    blob_client = container_client.get_blob_client(blob_path)
    blob_data = blob_client.download_blob().readall().decode("utf-8")
    return pd.read_csv(StringIO(blob_data))

# Función para subir DataFrame como CSV al Blob
def upload_df_to_blob(df, blob_path):
    blob_client = container_client.get_blob_client(blob_path)
    csv_data = df.to_csv(index=False)
    blob_client.upload_blob(
        csv_data,
        overwrite=True,
        content_settings=ContentSettings(content_type="text/csv")
    )
