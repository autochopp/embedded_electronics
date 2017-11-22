import  RPi.GPIO as GPIO
import time

def cup_in_place():
	
	sensor_pin = 18#pin 12
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(sensor_pin, GPIO.IN, GPIO.PUD_UP)
	
	if (not GPIO.input(sensor_pin)):
		print "cup in place"
	else:
		print "cup not placed"


######################### TEST#################
if __name__=="__main__":
	print "test for the cup detector"
	while(1):
		try:
			cup_in_place()
			time.sleep(0.1)
		except KeyboardInterrupt:
			break
	GPIO.cleanup()

