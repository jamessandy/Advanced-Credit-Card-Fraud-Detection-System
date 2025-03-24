import json
from kafka import KafkaConsumer

KAFKA_TOPIC = "transactions"
KAFKA_BROKER = "localhost:9092"

def consume_transactions():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for message in consumer:
        print("Received:", message.value)

consume_transactions()
