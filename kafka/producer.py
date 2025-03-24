from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder \
    .appName("FraudDetection") \
    .getOrCreate()

# Read streaming data from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions") \
    .load()

# Convert data
df = df.selectExpr("CAST(value AS STRING)")

# Apply simple fraud detection logic
def detect_fraud(transaction_df):
    return transaction_df.withColumn(
        "is_fraud", when(col("amount") > 500, 1).otherwise(0)
    )

fraud_df = detect_fraud(df)

# Output fraud transactions
query = fraud_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
