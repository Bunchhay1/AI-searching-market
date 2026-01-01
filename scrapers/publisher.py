import json
import logging
import os
import pika

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", "5672"))
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")

EXCHANGE_NAME = os.getenv("RABBITMQ_EXCHANGE", "market.exchange")
ROUTING_KEY = os.getenv("RABBITMQ_ROUTING_KEY", "market.raw.listings.key")
QUEUE_NAME = os.getenv("RABBITMQ_QUEUE", "market.raw.listings.queue")


class RabbitMQPublisher:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.connect()

    def connect(self):
        try:
            credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
            parameters = pika.ConnectionParameters(
                host=RABBITMQ_HOST,
                port=RABBITMQ_PORT,
                credentials=credentials,
                heartbeat=600,
                blocked_connection_timeout=300
            )
            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()

            # Declare exchange and durable queue
            self.channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type="direct", durable=True)
            self.channel.queue_declare(queue=QUEUE_NAME, durable=True)
            self.channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_NAME, routing_key=ROUTING_KEY)

            logging.info(f"Connected to RabbitMQ at {RABBITMQ_HOST}:{RABBITMQ_PORT}")
        except Exception as e:
            logging.warning(f"RabbitMQ connection warning: {e}. (Will retry upon publish)")

    def publish_listing(self, item_dict: dict) -> bool:
        """
        Publishes a scraped raw listing payload into RabbitMQ exchange
        """
        try:
            if not self.connection or self.connection.is_closed:
                self.connect()

            payload = json.dumps(item_dict, ensure_ascii=False)
            self.channel.basic_publish(
                exchange=EXCHANGE_NAME,
                routing_key=ROUTING_KEY,
                body=payload.encode("utf-8"),
                properties=pika.BasicProperties(
                    delivery_mode=2,  # make message persistent
                    content_type="application/json"
                )
            )
            logging.info(f"🚀 [RabbitMQ Publisher] Sent item to queue: '{item_dict.get('title')}' - {item_dict.get('rawPrice')}")
            return True
        except Exception as e:
            logging.error(f"❌ Failed to publish item to RabbitMQ: {e}")
            return False

    def close(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()


_publisher_instance = None

def get_publisher() -> RabbitMQPublisher:
    global _publisher_instance
    if _publisher_instance is None:
        _publisher_instance = RabbitMQPublisher()
    return _publisher_instance
