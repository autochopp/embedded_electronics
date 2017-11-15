import requests
from temperature  import getTemperature

# This classes should send sensors data via socket
class Collector:

    def __init__(self, server_url='127.0.0.1', port=3000):
        self.temperature = 0.0
        self.volume = 0.0
        self.machine_status = False

        # Rails API is running in localhost:3000
        self.server_url = 'http://' + server_url + ':' + str(port) + '/setsensors'

    # Collect all sensors data
    def collect(self):
        self.temperature = getTemperature()

    # Send the HTTP POST request
    def send_to_server(self):
        data = {
            'temperature': self.temperature,
            'volume': self.volume,
            'machine_status': self.machine_status
        }

        requests.post(self.server_url, data)


####################### TEST ###################
if __name__=="__main__":
	test = Collector()
	while(1):
		try:
			test.collect()
			print "Temperature: ",  test.temperature
		except:
			break
