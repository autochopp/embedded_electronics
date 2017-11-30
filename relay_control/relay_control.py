import  RPi.GPIO as gpio
import time
def relay_control(relay_pins, enable):
    gpio.setwarnings(False)    
    if enable:
        state = 1
    else:
        state = 0

    gpio.setmode(gpio.BCM)
    gpio.setup(i, gpio.OUT)
    gpio.output(i, state)

    gpio.cleanup()

if __name__=="__main__":
    pins = 21

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
