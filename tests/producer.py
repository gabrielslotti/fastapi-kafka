from pykafka import KafkaClient
import time

client = KafkaClient("127.0.0.1:9092")
test = client.topics["test"]

with test.get_sync_producer() as producer:
    i = 0
    for _ in range(10):
        producer.produce(f"Kafka is not just an author {str(i)}".encode('ascii'))  # noqa
        i += 1
        time.sleep(1)
