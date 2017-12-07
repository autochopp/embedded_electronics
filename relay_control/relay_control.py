import  RPi.GPIO as gpio
import time
def relay_control(relay_pin, enable):
    gpio.setwarnings(False)    
    if enable: #active low
        state = 0
    else:
        state = 1

    gpio.setmode(gpio.BCM)
    gpio.setup(relay_pin, gpio.OUT)
    gpio.output(relay_pin, state)

    #gpio.cleanup()

if __name__=="__main__":
    pins = 27
    t = 0.16
    #while True:
        #try:
    relay_control(pins, True)
    print "relay on!"    
    time.sleep(t)
    relay_control(pins, False)
    print "relay off!"
    time.sleep(t)
       # except KeyboardInterrupt:
        #    break
