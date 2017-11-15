# -*- coding: utf-8 -*-
#! /usr/bin/python

import RPi.GPIO as gpio
import time

""" Global """
PIN1 = 16
PIN2 = 20


""" Configurando GPIO """
# Configurando o modo dos pinos como BCM
gpio.setmode(gpio.BCM) 

# Configurando PIN como INPUT e modo pull-donw interno
gpio.setup(PIN1, gpio.IN)
gpio.setup(PIN2, gpio.IN)

# Adicionando um evento ao GPIO 20 na mudança RISING 0V[LOW] - > 3.3V[HIGH]
gpio.add_event_detect(PIN1, gpio.BOTH)
gpio.add_event_detect(PIN2, gpio.BOTH)
while True:
	if gpio.event_detected(PIN1):
		print "pulse_init_detect"
		init = time.time()
		print init
		break
	
	
while True:
	if gpio.event_detected(PIN2):
		print "pulse_end_detect"
		end = time.time()
		print end
		break

tempo = end - init
print (tempo)

velocidade = 0.132/tempo
vasao = velocidade * 0.000078539
vasao = vasao*1000000 #vasao em ml/s

print vasao




gpio.cleanup()
exit()
