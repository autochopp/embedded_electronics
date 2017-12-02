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
    pins = 22

    while True:
        try:
            relay_control(pins, True)
            print "relay on!"    
            time.sleep(1)
            relay_control(pins, False)
            print "relay off!"
            time.sleep(1)
        except KeyboardInterrupt:
            break
