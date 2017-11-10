import  RPi.GPIO as gpio
sensor_pin = 18

gpio.setmode(gpio.BCM)

gpio.setup(sensor_pin, gpio.IN, gpio.PUD_UP)

def exist_cup():
	exist_cup = False

	if gpio.input(sensor_pin) == 0:
		# so return true
		print "Cup placed!!"
		exist_cup = True
	else:
		print "No cup!"

	gpio.cleanup()

	return exist_cup