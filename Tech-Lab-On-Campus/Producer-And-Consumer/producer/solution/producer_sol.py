from producer_interface import mqProducerInterface
import pika
import os

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str):
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.channel = None
        self.exchange_name = None
        self.setupRMQConnection() 
    
    def setupRMQConnection(self):
        # connection 
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        connection = pika.BlockingConnection(parameters=con_params)

        # channel
        self.channel = connection.channel()

        exchange = self.channel.exchange_declare(exchange="New Exchange")
        self.exchange_name = "New Exchange"

    def publishOrder(self, message: str) -> None:
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=message,
)
    
  
