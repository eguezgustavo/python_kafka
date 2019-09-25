#!/usr/bin/env python3

from kafka import KafkaConsumer
import os

TOPIC_NAME = 'PythonTest'
SERVER = os.environ['IP']
PORT = 9092

consumer = KafkaConsumer(
    bootstrap_servers=f'{SERVER}:{PORT}',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: m.decode('utf-8')
)
consumer.subscribe([TOPIC_NAME])

if __name__ == '__main__':
    print(f'Consumer on server: {SERVER} running')
    print()
    while True:
        try:
            for message in consumer:
                print('new message: ', message.value)
        except KeyboardInterrupt:
            exit(0)

# docker run --rm --interactive ches/kafka kafka-console-producer.sh --topic PythonTest --broker-list 10.4.1.29:9092
# docker run --rm ches/kafka kafka-console-consumer.sh --topic PythonTest  --zookeeper $IP:2181

# docker run --rm ches/kafka kafka-topics.sh --list --zookeeper $IP:2181