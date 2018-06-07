from nameko.rpc import rpc
import db
from db import Temperature


class TemperatureServer():
    name = "temperature_server"

    @rpc
    def receive_temperature(self, temperature):
        temperature = round(temperature, 1)
        t = Temperature()
        t.value = temperature
        t.unit = ('C')
        db.session.add(t)
        db.session.commit()
        return temperature
