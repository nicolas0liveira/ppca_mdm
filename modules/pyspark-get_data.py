from pyspark.sql import SparkSession

# Cria a SparkSession
spark = SparkSession.builder \
    .appName("Spark SQL com Impala") \
    .config("spark.driver.extraClassPath", "/caminho/para/ImpalaJDBC42.jar") \
    .getOrCreate()

# Parâmetros da conexão
jdbc_url = "jdbc:impala://<IMPALA_HOST>:21050/nomedobanco"

# Registra a tabela temporária via JDBC
spark.read \
    .format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "sua_tabela") \
    .option("driver", "com.cloudera.impala.jdbc.Driver") \
    .load() \
    .createOrReplaceTempView("impala_temp")

# Agora você pode usar Spark SQL direto
df = spark.sql("SELECT * FROM impala_temp WHERE alguma_coluna IS NOT NULL")

# Exibe os dados
df.show()

# Salva como CSV (um único arquivo, se quiser)
df.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("data/impala_resultado")

# Encerra sessão
spark.stop()
