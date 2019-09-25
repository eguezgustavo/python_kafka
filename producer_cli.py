#!/usr/bin/env python3

from kafka import KafkaProducer
import os

TOPIC_NAME = 'PythonTest'
SERVER = os.environ['IP']
PORT = 9092

producer = KafkaProducer(bootstrap_servers=f'{SERVER}:{PORT}', value_serializer=lambda v: v.encode('utf-8'))


if __name__ == '__main__':
    while True:
        try:
            message = input('Input the message to be posted: ')
            producer.send(TOPIC_NAME, message)
            print(f'Message: "{message}" has been posted')
            print('')
        except KeyboardInterrupt:
            exit(0)
