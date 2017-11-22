import  RPi.GPIO as GPIO
import time

def edge_detector():
	
	sensor_pin = 18#pin 12
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(sensor_pin, GPIO.IN, GPIO.PUD_UP)
	
	while(1):
		if (not GPIO.input(sensor_pin)):
			print "end of cup"
			break
		end = time.time()	
######################### TEST#################
if __name__=="__main__":
	print "test for the edge detector"

	edge_detector()
	GPIO.cleanup()

