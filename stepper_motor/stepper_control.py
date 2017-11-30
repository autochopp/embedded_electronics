import RPi.GPIO as GPIO
import time
#TODO put the real pins 
def steps(total_steps, pins, forward=True):
	
	interval = 2./100.
		
	# default pins
	
	pin_1 = pins[0]
	pin_2 = pins[1]
	pin_3 = pins[2]
	pin_4 = pins[3]
	
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(pin_1, GPIO.OUT)
	GPIO.setup(pin_2, GPIO.OUT)
	GPIO.setup(pin_3, GPIO.OUT)
	GPIO.setup(pin_4, GPIO.OUT)
	

	GPIO.output(pin_1, 0)
	GPIO.output(pin_2, 0)
	GPIO.output(pin_3, 0)
	GPIO.output(pin_4, 0)


	for i in xrange(0, total_steps/4):
		
		if forward:		
			GPIO.output(pin_1, 1)
			GPIO.output(pin_2, 1)
			GPIO.output(pin_3, 0)
			GPIO.output(pin_4, 0)

			time.sleep(interval)	

			GPIO.output(pin_1, 0)
			GPIO.output(pin_2, 1)
			GPIO.output(pin_3, 1)
			GPIO.output(pin_4, 0)

			time.sleep(interval)	

			GPIO.output(pin_1, 0)
			GPIO.output(pin_2, 0)
			GPIO.output(pin_3, 1)
			GPIO.output(pin_4, 1)

			time.sleep(interval)	

			GPIO.output(pin_1, 1)
			GPIO.output(pin_2, 0)
			GPIO.output(pin_3, 0)
			GPIO.output(pin_4, 1)

			time.sleep(interval)	
		
		else:
			GPIO.output(pin_1, 1)
			GPIO.output(pin_2, 0)
			GPIO.output(pin_3, 0)
			GPIO.output(pin_4, 1)

			time.sleep(interval)	

			GPIO.output(pin_1, 0)
			GPIO.output(pin_2, 0)
			GPIO.output(pin_3, 1)
			GPIO.output(pin_4, 1)

			time.sleep(interval)	

			GPIO.output(pin_1, 0)
			GPIO.output(pin_2, 1)
			GPIO.output(pin_3, 1)
			GPIO.output(pin_4, 0)

			time.sleep(interval)	

			GPIO.output(pin_1, 1)
			GPIO.output(pin_2, 1)
			GPIO.output(pin_3, 0)
			GPIO.output(pin_4, 0)

			time.sleep(interval)

	GPIO.cleanup()

#set to 45 degrees and back
def cup_to_position(set_to_angle, size):
	if size=="big":
        st = 50
    elif size=="small":
        st = 100
       
	pins = [6, 13, 19, 26]
	
	if set_to_angle:
	# 200steps per revolution, 1.8 degrees, but the motor needs to turn 90degrees, 50 steps
		steps(st, pins, True)
	else:
		steps(st, pins, False)

#control valve
def valve_control(set_open):
	
	pins = [6, 13, 19, 26]
	
	if set_open:
	# 200steps per revolution, 1.8 degrees, but the motor needs to turn 90degrees, 50 steps
		steps(50, pins, True)
	else:
		steps(50, pins, False)



def foam_activation(active):
	pins =[6, 13, 19, 26]
	
	if active:
		steps(200, pins, True)
	else:
		steps(200, pins, False)

#########################    TEST  ####################
if __name__=="__main__":
	time.sleep(1)
	print "setting to 45"
	cup_to_position(True)
	time.sleep(2)
	print "setting it back"
	cup_to_position(False)
	time.sleep(2)
