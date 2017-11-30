import  RPi.GPIO as GPIO
import time

def edge_detector():
	
	sensor_pin = 18#pin 12
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(sensor_pin, GPIO.IN, GPIO.PUD_UP)
	
    if (not GPIO.input(sensor_pin)):
	    GPIO.cleanup()
        return True #end
    else:
	    GPIO.cleanup()
        return False

######################### TEST#################
if __name__=="__main__":
	print "test for the edge detector"

	edge_detector()

	GPIO.cleanup()
