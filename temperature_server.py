from nameko.rpc import rpc

class TemperatureServer():
    name = 'temperature_server'

    @rpc
    def receive_temperature(self, temperature):
        print(temperature)

        return True
