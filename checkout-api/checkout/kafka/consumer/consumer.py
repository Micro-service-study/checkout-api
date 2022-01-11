from kafka import KafkaConsumer
import json

consumer = KafkaConsumer("checkout-check-request", 
                         bootstrap_servers='localhost:9092',
                         api_version=(0,11,15))
print('Start consumer...')
for message in consumer:
  print (json.loads(message))