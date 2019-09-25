import asyncio
import os

from aiokafka import AIOKafkaConsumer


TOPIC_NAME = 'PythonTest'
SERVER = os.environ['IP']
PORT = 9092


async def consume(consumer, consumer_id):
    await consumer.start()
    try:
        async for msg in consumer:
            print(f'message received, consumer: {consumer_id}, message: {msg.value}')
    finally:
        await consumer.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    first_consumer = AIOKafkaConsumer(
        TOPIC_NAME,
        loop=loop,
        bootstrap_servers=f'{SERVER}:{PORT}',
        value_deserializer=lambda v: v.decode('utf-8')
    )

    second_consumer = AIOKafkaConsumer(
        TOPIC_NAME,
        loop=loop,
        bootstrap_servers=f'{SERVER}:{PORT}',
        value_deserializer=lambda v: v.decode('utf-8')
    )

    loop.run_until_complete(
        asyncio.wait([consume(first_consumer, 'first_consumer'), consume(second_consumer, 'second_consumer')])
    )
