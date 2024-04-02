from consumer_interface import mqConsumerInterface
import pika
import os

class mqConsumer(mqConsumerInterface):
    def __init__(
        self, binding_key: str, exchange_name: str, queue_name: str
    ) -> None:
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        channel = connection.channel()
        channel.queue_declare(queue=self.queue_name)
        exchange = channel.exchange_declare(exchange=self.exchange_name)

        channel.queue_bind(
        queue= self.queue_name,
        routing_key= self.routing_key,
        exchange=self.exchange_name,
    )
        channel.basic_consume(
        self.queue_name, self.on_message_callback, auto_ack=False
    )

    def on_message_callback(
        self, channel, method_frame, header_frame, body
    ) -> None:
        channel.basic_ack(method_frame.delivery_tag, False)
        print("Hihihi")

    def startConsuming(self) -> None:
        print("[*] Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()
    
    def __del__(self) -> None:
        print("Closing RMQ connection on destruction")
        channel.close()
        connection.close()      
