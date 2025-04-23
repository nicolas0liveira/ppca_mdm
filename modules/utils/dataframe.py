import re

def ping():
    print("pong")

def dataframe_info(df, ignore=None):
    """
    Exibe informações básicas sobre um DataFrame, incluindo shape, colunas, tipos, categorias e estatísticas,
    com a opção de ignorar colunas específicas.
    
    :param df: O DataFrame a ser analisado.
    :param ignore: Lista de colunas a serem ignoradas na análise (default: []).
    """
    if ignore is None:
        ignore = []

    # Remove as colunas ignoradas
    df_filtrado = df.drop(columns=ignore, errors='ignore')

    variaveis_numericas = df_filtrado.select_dtypes(include=['number'])
    variaveis_categoricas = df_filtrado.select_dtypes(include=['category', 'object'])

    print("Variáveis categóricas:")
    print(variaveis_categoricas.columns.tolist())
    print("\nNúmero de categorias únicas:")
    print(variaveis_categoricas.nunique())

    for v in variaveis_categoricas.columns:
        print(f"\n>>>>> {v} <<<<<")
        print(f"Total de categorias: {variaveis_categoricas[v].nunique()}")
        print((variaveis_categoricas[v].value_counts(normalize=True) * 100).round(2).astype(str) + '%')

    print("\nVariáveis numéricas:")
    print(variaveis_numericas.columns.tolist())
    print("\nResumo estatístico:")
    print(variaveis_numericas.describe())

    print("\n\nInformações gerais do DataFrame:")
    print(f"Uso de memória: {df_filtrado.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print(f"Shape: {df.shape}")
    print(f"Colunas: {df.columns.tolist()}")
    print(f"\nValores ausentes por coluna:\n{df.isnull().sum()}")
    print(f"\nTamanho total (elementos): {df.size}")

 
