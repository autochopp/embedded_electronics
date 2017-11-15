import requests
from temperature  import getTemperature

# This classes should send sensors data via socket
class Collector:

    def __init__(self, server_url='http://127.0.0.1', port="3000"):
		self.temperature = 0.0
		self.volume = 0 # in ml, int
		self.machine_status = False
		self.sent_status = False
		# Rails API is running in localhost:3000
		self.server_url = server_url + ':' + str(port) + '/setsensors'

    # Collect all sensors data
    def collect(self):
		self.temperature = getTemperature()
		f = open("volume.vol", "r")
		self.volume = int(f.read())
		f.close()
		

    # Send the HTTP POST request
    def send_to_server(self):
		data = {
			'temperature': self.temperature,
			'volume': self.volume,
			'machine_status': self.machine_status
			}
		r = requests.post(self.server_url, data)
		if r.status_code == 204:
			self.sent_status = True
		else:
			self.sent_status = False	


####################### TEST ###################
if __name__=="__main__":
	test = Collector("https://fast-retreat-18030.herokuapp.com", '')
	import time
	
	while(1):
		try:
			test.collect()
			print "\nTemperature: ",  test.temperature
			print "Volume: ", test.volume
			test.send_to_server()
			print "Sent status: ", test.sent_status
			time.sleep(5)
		except KeyboardInterrupt:
			break		

