import  RPi.GPIO as GPIO
import time

def cup_in_place(t_out=20):
	
	sensor_pin = 18
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(sensor_pin, GPIO.IN, GPIO.PUD_UP)

	cup_placed = False
	start = time.time() 
	t2 = time.time()

	while((t2-start) <= t_out):
		
		cup = []
		cup.append (GPIO.input(sensor_pin)) # 0==placed
		time.sleep(1)	
		cup.append (GPIO.input(sensor_pin)) # 0==placed
		time.sleep(1)	
		cup.append (GPIO.input(sensor_pin)) # 1==placed
		
		if ((cup[0]==0) and (cup[1]==0) and (cup[2]==0)):
			cup_placed = True
			break
		t2  = time.time()
	
	GPIO.cleanup()
	return cup_placed

######################### TEST#################
if __name__=="__main__":
	print "test for the cup detector"
	while(1):
		try:
			print "Cup in place? ", cup_in_place(6)
		except KeyboardInterrupt:
			break
	GPIO.cleanup()

