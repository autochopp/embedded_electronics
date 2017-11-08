import  RPi.GPIO as gpio
import time
relay_pin = 21

gpio.setmode(gpio.BCM)

gpio.setup(relay_pin, gpio.OUT)

gpio.output(relay_pin, 1) # active in low

time.sleep(1)

while True:
	try:
		gpio.output(relay_pin, 0)
		print "relay on!"	
		time.sleep(1)
		gpio.output(relay_pin, 1)
		print "relay off!"
		time.sleep(1)
	except KeyboardInterrupt:
		break
gpio.cleanup()
