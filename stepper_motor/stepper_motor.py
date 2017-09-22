import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_1 = 31
pin_2 = 33
pin_3 = 35
pin_4 = 37

GPIO.setmode(pin_1, GPIO.OUT)
GPIO.setmode(pin_2, GPIO.OUT)
GPIO.setmode(pin_3, GPIO.OUT)
GPIO.setmode(pin_4, GPIO.OUT)

GPIO.output(pin_1, 0)
GPIO.output(pin_2, 0)
GPIO.output(pin_3, 0)
GPIO.output(pin_4, 0)





def step_1():
	GPIO.output(pin_1, 1)
	GPIO.output(pin_2, 1)
	GPIO.output(pin_3, 0)
	GPIO.output(pin_4, 0)

def step_2():
	GPIO.output(pin_1, 0)
	GPIO.output(pin_2, 1)
	GPIO.output(pin_3, 1)
	GPIO.output(pin_4, 0)

def step_3():
	GPIO.output(pin_1, 0)
	GPIO.output(pin_2, 0)
	GPIO.output(pin_3, 1)
	GPIO.output(pin_4, 1)

def step_4():
	GPIO.output(pin_1, 1)
	GPIO.output(pin_2, 0)
	GPIO.output(pin_3, 0)
	GPIO.output(pin_4, 1)


while(true):
	step_1()
	time.sleep(1)
	step_2()
	time.sleep(1)
	step_3()
	time.sleep(1)
	step_4()
	time.sleep(1)
