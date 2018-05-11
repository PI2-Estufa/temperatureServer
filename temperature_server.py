from nameko.rpc import rpc
from nameko.messaging import Publisher
from kombu import Exchange, Queue
import db

exchange = Exchange("main", "direct", durable=True)
queue = Queue("temperature_queue", exchange=exchange)


class TemperatureServer():
    name = "temperature_server"
    publish = Publisher(exchange=exchange, queue=queue)

    @rpc
    def receive_temperature(self, temperature):
        print(temperature)
        self.publish(temperature)
        return temperature
