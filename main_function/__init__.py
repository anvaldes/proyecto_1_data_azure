import azure.functions as func
import traceback

try:
    from data_pipeline import run_data_pipeline
    from uniendo_data import uniendo_data
    from utils_blob import download_blob_to_df, upload_df_to_blob
    import pandas as pd
    from io import StringIO
except Exception as e:
    print("❌ Error en imports:")
    print(traceback.format_exc())
    raise e

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        year = req.params.get('year', '2025')
        month = req.params.get('month', '06')

        print(f"📦 Iniciando pipeline para {year}-{month}")

        dfs = []
        for i in range(1, 4):
            path = f"source_data/{year}_{month}/credit_risk_{i}.csv"
            df = download_blob_to_df(path)
            dfs.append(df)

        df_combined = uniendo_data(dfs)
        outputs = run_data_pipeline(df_combined)

        for name, df in outputs.items():
            output_path = f"datasets/{year}_{month}/{name}.csv"
            upload_df_to_blob(df, output_path)
            print(f"☁️ Subido: {output_path}")

        return func.HttpResponse(f"✅ Pipeline completado para {year}-{month}. Beto V!", status_code=200)

    except Exception as e:
        print("❌ Error en ejecución:")
        print(traceback.format_exc())
        return func.HttpResponse("❌ Falló la función:\n" + str(e), status_code=500)
