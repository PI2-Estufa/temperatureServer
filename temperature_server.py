from nameko.rpc import rpc
from nameko.messaging import Publisher
from kombu import Exchange, Queue
import db
from db import Temperature

exchange = Exchange("temperature", "direct", durable=True)
queue = Queue("temperature_queue", exchange=exchange)


class TemperatureServer():
    name = "temperature_server"
    publish = Publisher(exchange=exchange, queue=queue)

    @rpc
    def receive_temperature(self, temperature):
        t = Temperature()
        t.value = temperature
        t.unit = ('C')
        db.session.add(t)
        db.session.commit()
        self.publish(temperature)
        return temperature
