import os
import pandas as pd
import zipfile
from io import TextIOWrapper
import re

def find_zip_files_by_pattern(directory, pattern=None):
    """
    Busca recursivamente arquivos .zip que contenham um padrão específico no nome.
    Caso nenhum padrão seja fornecido, retorna todos os arquivos .zip.

    :param directory: Diretório onde procurar os arquivos.
    :param pattern: Padrão a ser buscado no nome do arquivo. Se None, retorna todos os arquivos .zip.
    :return: Lista de caminhos completos dos arquivos que correspondem ao critério.
    """
    zip_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".zip"):
                if pattern is None or pattern.lower() in file.lower():
                    full_path = os.path.join(root, file)
                    zip_files.append(full_path)
    return zip_files

def extract_origem_from_filename(filename):
    """
    Retorna a origem do dado com base no nome do arquivo.
    Ex: 'arquivo_lai_FGTS_AC_202006.csv' -> 'FGTS'
    """
    if 'FGTS' in filename.upper():
        return 'FGTS'
    elif 'SIDA' in filename.upper():
        return 'SIDA'
    elif 'PREV' in filename.upper():
        return 'PREV'
    else:
        return 'OUTROS'
    
def extract_anomes_from_filename(filename):
    """
    Retorna o ano e mês do nome do arquivo.
    Ex: 'arquivo_lai_FGTS_AC_202006.csv' -> '202006'
    """
    match = re.search(r'_(\d{6})\.csv$', filename)
    if match:
        return match.group(1)
    else:
        raise ValueError(f"Formato de nome de arquivo inesperado: {filename}")


def read_zip_csvs_as_df(zip_path, encoding="utf-8", sep=";", verbose=True):
    """
    Reads a .zip file, extracts all CSVs, and concatenates them into a single DataFrame.

    :param zip_path: Path to the .zip file.
    :param encoding: Encoding used in the CSV files.
    :param sep: Field separator used in the CSV files.
    :param verbose: If True, prints file processing status.
    :return: A pandas DataFrame containing the concatenated CSV data.
    """
    dataframes = []

    with zipfile.ZipFile(zip_path, 'r') as z:
        for file_name in z.namelist():
            if file_name.lower().endswith("csv"):
                if verbose:
                    print(f"📂 Reading: {file_name}")
                with z.open(file_name) as f:
                    df = pd.read_csv(TextIOWrapper(f, encoding=encoding), sep=sep)
                    df["__source_file__"] = file_name
                    dataframes.append(df)

    if not dataframes:
        raise ValueError("No CSV files found in the ZIP archive.")

    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df
def save_parquet(df, path, columns=None, unique=False, order_by=None):
    """
    Saves a DataFrame as a Parquet file, keeping only the specified columns,
    optionally sorting and considering only unique records.

    :param df: DataFrame to be saved.
    :param path: File path for the .parquet file (with or without extension).
    :param columns: List of columns to be retained in the file (default: all columns).
    :param unique: Boolean flag to consider only unique records (default: False).
    :param order_by: List of columns to sort by before saving (default: None).
    :return: Filtered and saved DataFrame.
    """
    # Filter the DataFrame by the specified columns, if provided
    if columns is not None:
        df_filtered = df[columns]
    else:
        df_filtered = df

    # Drop duplicates if unique is True
    if unique:
        df_filtered = df_filtered.drop_duplicates()

    # Sort by specified columns if provided
    if order_by is not None:
        df_filtered = df_filtered.sort_values(by=order_by)

    # Ensure the file path ends with .parquet
    if not path.endswith(".parquet"):
        path += ".parquet"

    # Save to Parquet
    df_filtered.to_parquet(path, index=False)
    print(f"File saved at: {path}")

    return df_filtered
