from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='kafka:29092',
                         api_version=(0,11,15))

def brokerProducer(topic, message):
  try:
    producer.send(topic, str.encode(json.dumps(message)))
    producer.flush()
  except Exception as error:
    print(error)
  return

