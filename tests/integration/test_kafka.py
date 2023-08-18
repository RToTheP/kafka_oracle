from kafka import KafkaConsumer, KafkaProducer, TopicPartition

from ko.config import CONFIG

def test_kafka_hello_world():
    encoding = 'UTF-8'
    message = 'hello world'
    topic = 'hello'
    bootstrap_servers=CONFIG.KAFKA_BOOTSTRAP_SERVER
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    producer.send(topic=topic, value=bytes(message, encoding))

    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, consumer_timeout_ms=1000)
    topic_partition = TopicPartition(topic=topic, partition=0)
    consumer.assign([topic_partition])
    consumer.seek_to_beginning()
    print('position = ',consumer.position(topic_partition))
    messages = []
    for cm in consumer:
        m = str(cm.value, encoding=encoding)
        print(cm.offset, m)
        messages.append(m)
    print(messages)
    assert message in messages

