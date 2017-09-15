import  RPi.GPIO as gpio
import time
sensor_pin = 18

gpio.setmode(gpio.BCM)

gpio.setup(sensor_pin, gpio.IN, gpio.PUD_UP)

while True:
	try:
		if gpio.input(sensor_pin)==0:
			print "Cup placed!!"
		else: print "No cup!!"
		time.sleep(0.1)
	except KeyboardInterrupt:
		break
gpio.cleanup()
