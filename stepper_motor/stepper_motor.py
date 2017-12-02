import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_1 = 12
pin_2 = 16
pin_3 = 20
pin_4 = 21

tempo = 2.0/800

GPIO.setup(pin_1, GPIO.OUT)
GPIO.setup(pin_2, GPIO.OUT)
GPIO.setup(pin_3, GPIO.OUT)
GPIO.setup(pin_4, GPIO.OUT)

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


while(True):
	try:
		step_1()
		time.sleep(tempo)
		step_2()
		time.sleep(tempo)
		step_3()
		time.sleep(tempo)
		step_4()
		time.sleep(tempo)
	except KeyboardInterrupt:
		break
GPIO.cleanup()
