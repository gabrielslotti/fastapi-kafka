from aiokafka import AIOKafkaConsumer
from config import KAFKA_INSTANCE
from config import PROJECT_NAME
import asyncio


# TODO:
# 1. Partition and offset.


async def consume():
    topicnames = ['test']
    consumer = AIOKafkaConsumer(*topicnames,
                                client_id=PROJECT_NAME,
                                group_id='my-group',
                                bootstrap_servers=KAFKA_INSTANCE,
                                enable_auto_commit=False)
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()

asyncio.run(consume())
