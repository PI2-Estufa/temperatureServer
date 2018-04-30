from nameko.rpc import rpc

class TemperatureServer():
    name = 'temperature_server'

    @rpc
    def receiveTemperature(self, temperature):
        print(temperature)

        return True
