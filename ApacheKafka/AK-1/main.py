import json
from kafka import KafkaProducer

folderName = "./"
HOST = ""
SSL_PORT = 13664
producer = KafkaProducer(
    bootstrap_servers=f"{HOST}:{SSL_PORT}",
    security_protocol="SSL",
    ssl_cafile=folderName+"ca.pem",
    ssl_certfile=folderName+"service.cert",
    ssl_keyfile=folderName+"service.key",
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii')
)

# callback to check for errors
def on_send_success(record_metadata):
    print(f"Message sent to {record_metadata.topic} partition {record_metadata.partition} offset {record_metadata.offset}")

def on_send_error(excp):
    print('Error:', excp)

future = producer.send("ak-topic",
                       key={"key": 1},
                       value={"message": "Hello, I'm learning Apache Kafka"})

future.add_callback(on_send_success)
future.add_errback(on_send_error)


producer.flush()
# producer.close