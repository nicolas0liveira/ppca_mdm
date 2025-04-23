import re

def ping():
    print("pong")

# from pyspark.sql.types import NumericType, StringType
# from pyspark.sql.functions import col, countDistinct, count, sum

# def dataframe_info_spark(df):
#     """
#     Exibe informações básicas sobre um DataFrame do PySpark, separando variáveis categóricas e numéricas.
    
#     :param df: O DataFrame do PySpark a ser analisado.
#     """
#     print("Esquema do DataFrame:")
#     df.printSchema()

#     # Separar variáveis numéricas e categóricas (string)
#     schema = df.schema
#     variaveis_numericas = [f.name for f in schema if isinstance(f.dataType, NumericType)]
#     variaveis_categoricas = [f.name for f in schema if isinstance(f.dataType, StringType)]

#     print("\nVariáveis categóricas:")
#     print(variaveis_categoricas)

#     print("\nNúmero de categorias únicas por variável categórica:")
#     for col_name in variaveis_categoricas:
#         n_categorias = df.select(col_name).distinct().count()
#         print(f"{col_name}: {n_categorias} categorias únicas")

#         print("Distribuição:")
#         df.groupBy(col_name).count().orderBy('count', ascending=False).show(10, truncate=False)

#     print("\nVariáveis numéricas:")
#     print(variaveis_numericas)

#     print("\nResumo estatístico das variáveis numéricas:")
#     df.select(variaveis_numericas).describe().show()

#     print("\nValores nulos por coluna:")
#     df.select([
#         sum(col(c).isNull().cast("int")).alias(c) for c in df.columns
#     ]).show()

#     print(f"\nNúmero total de linhas: {df.count()}")
#     print(f"Número total de colunas: {len(df.columns)}")
#     print(f"Colunas: {df.columns}")
