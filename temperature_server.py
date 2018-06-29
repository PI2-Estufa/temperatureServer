from nameko.rpc import rpc
import db
from db import Temperature
from psycopg2 import OperationalError


class TemperatureServer():
    name = "temperature_server"

    @rpc
    def receive_temperature(self, temperature):
        temperature = round(temperature, 1)
        t = Temperature()
        t.value = temperature
        t.unit = ('C')
        try:
            db.session.add(t)
            db.session.commit()
        except OperationalError:
            db.session.rollback()
        return temperature
