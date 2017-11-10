# from https://pimylifeup.com/raspberry-pi-temperature-sensor/
#use 3v3, a 4k7ohms between vcc and data and use pin7
from temperature_reader import getTemperature
import time
import  RPi.GPIO as gpio

def temp_control(max_temp=2., active_low=False, interval=2.):
	relay_pin = 21
	gpio.setmode(gpio.BCM)
	gpio.setup(relay_pin, gpio.OUT)

        if active_low:
		active = 0
		inactive = 1
	else:
		active = 1
		inactive = 0

        temp = getTemperature()

	if (temp>max_temp):
		gpio.output(relay_pin, active)
		print "relay on! temperature:", temp

	else:
		gpio.output(relay_pin, inactive)
		print "relay off! temperature:", temp

        time.sleep(interval)

if __name__ =="__main__":
	while True:
		try:
			temp_control(active_low=False)
		except KeyboardInterrupt:
			break
	gpio.cleanup()
