import os
import glob
import zipfile
import pandas as pd
import json

# Diretório de entrada com os arquivos .zip
INPUT_DIR = "/home/nicolas/Documents/dados/pgfn/dados_para_juntar"  # <-- ajuste esse caminho
OUTPUT_JSONL = "headers_extraidos.jsonl"

# Remove o JSONL antigo se existir
if os.path.exists(OUTPUT_JSONL):
    os.remove(OUTPUT_JSONL)

# Processa todos os arquivos ZIP no diretório
for zip_path in glob.glob(os.path.join(INPUT_DIR, "*.zip")):
    print(f"🔍 Lendo ZIP: {zip_path}")

    with zipfile.ZipFile(zip_path, "r") as zf:
        for csv_name in zf.namelist():
            if csv_name.lower().endswith(".csv"):
                print(f"  📄 Lendo header de: {csv_name}")
                try:
                    with zf.open(csv_name) as file:
                        df = pd.read_csv(
                            file, nrows=0, encoding="ISO-8859-1"
                        )  # Apenas header
                        header_info = {
                            "zip_path": zip_path,
                            "csv_name": csv_name,
                            "columns": df.columns.tolist(),
                        }
                        with open(OUTPUT_JSONL, "a", encoding="utf-8") as out_f:
                            out_f.write(
                                json.dumps(header_info, ensure_ascii=False) + "\n"
                            )
                except Exception as e:
                    print(f"    ⚠️ Erro ao processar {csv_name}: {e}")
