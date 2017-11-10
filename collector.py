# This classes should send sensors data via socket
class Collector:

    def __init__(self):
        self.temperature = 0.0
        self.volume = 0.0
        self.machine_status = False

    # Collect all sensors data
    def collect(self):
        pass

    # Send the HTTP POST request
    def send_to_server(self):
        pass
