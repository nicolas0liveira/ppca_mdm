import os
import json
import glob
import time
import zipfile
import traceback
from datetime import datetime
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

INPUT_DIR = "/home/nicolas/Documents/dados/pgfn/dados_para_juntar"
OUTPUT_DIR = f"{INPUT_DIR}/concatenated/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Colunas comuns a serem utilizadas
# columns = ["CPF_CNPJ"]

columns = [
    "CPF_CNPJ",
    "DATA_INSCRICAO",
    "INDICADOR_AJUIZADO",
    "NOME_DEVEDOR",
    "NUMERO_INSCRICAO",
    "SITUACAO_INSCRICAO",
    "TIPO_DEVEDOR",
    "TIPO_PESSOA",
    "TIPO_SITUACAO_INSCRICAO",
    "UNIDADE_RESPONSAVEL",
    "VALOR_CONSOLIDADO",
]

JSONL_FILE = os.path.join(OUTPUT_DIR, f"{timestamp}_resultado.jsonl")
CSV_FILE = os.path.join(OUTPUT_DIR, f"{timestamp}_resultado.csv")
PARQUET_FILE = os.path.join(OUTPUT_DIR, f"{timestamp}_resultado.parquet")
ERROR_LOG = os.path.join(OUTPUT_DIR, f"{timestamp}_erros.jsonl")

parquet_writer = None
total_rows = 0
start_time = time.time()


for zip_path in glob.glob(os.path.join(INPUT_DIR, "*.zip")):
    print(f"\n📄 Processando arquivo ZIP: {zip_path}")

    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            csv_files = [f for f in zf.namelist() if f.endswith(".csv")]

            for csv_name in csv_files:
                print(f"  📊 Processando arquivo CSV: {csv_name}")

                try:
                    with zf.open(csv_name) as file:
                        chunk_count = 0

                        for encoding in ["utf-8", "latin1"]:
                            try:
                                for chunk in pd.read_csv(
                                    file,
                                    chunksize=100_000,
                                    encoding=encoding,
                                    sep=";",
                                    usecols=columns,
                                ):
                                    chunk_count += 1
                                    row_count = len(chunk)
                                    total_rows += row_count
                                    print(
                                        f"    🧩 Chunk {chunk_count}: {row_count} linhas"
                                    )

                                    # JSONL
                                    chunk.to_json(
                                        JSONL_FILE,
                                        orient="records",
                                        lines=True,
                                        mode="a",
                                    )

                                    # CSV
                                    header = not os.path.exists(CSV_FILE)
                                    chunk.to_csv(
                                        CSV_FILE, index=False, mode="a", header=header
                                    )

                                    # Parquet
                                    table = pa.Table.from_pandas(chunk)
                                    if parquet_writer is None:
                                        parquet_writer = pq.ParquetWriter(
                                            PARQUET_FILE, table.schema
                                        )
                                    parquet_writer.write_table(table)
                                break  # Se tudo funcionou, não tenta outros encodings
                            except (UnicodeDecodeError, ValueError):
                                file.seek(0)
                        else:
                            raise ValueError("Nenhum encoding funcionou.")

                except Exception as e:
                    error_data = {
                        "zip_path": zip_path,
                        "csv_name": csv_name,
                        "error": str(e),
                        "traceback": traceback.format_exc(),
                    }
                    with open(ERROR_LOG, "a", encoding="utf-8") as err_file:
                        err_file.write(
                            json.dumps(error_data, ensure_ascii=False) + "\n"
                        )
                    print(f"    ⚠️ Erro ao processar {csv_name}, erro registrado.")

    except Exception as e:
        error_data = {
            "zip_path": zip_path,
            "csv_name": None,
            "error": str(e),
            "traceback": traceback.format_exc(),
        }
        with open(ERROR_LOG, "a", encoding="utf-8") as err_file:
            err_file.write(json.dumps(error_data, ensure_ascii=False) + "\n")
        print(f"  ⚠️ Erro ao abrir ZIP {zip_path}, erro registrado.")

if parquet_writer:
    parquet_writer.close()

elapsed = time.time() - start_time
print("\n✅ Processamento finalizado!")
print(f"📊 Total de linhas processadas: {total_rows:,}")
print(f"📁 Arquivos salvos em: {OUTPUT_DIR}")
print(f"⏱️ Tempo total: {elapsed:.2f} segundos")
