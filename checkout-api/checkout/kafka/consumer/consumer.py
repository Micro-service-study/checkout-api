from kafka import KafkaConsumer
import json

def consumerGet():
    consumer = KafkaConsumer("checkout-check-request",
                         bootstrap_servers='kafka:29092',
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         api_version=(0,11,15))
    print('Start consumer...')
    for message in consumer:
        print(json.loads(message.value))