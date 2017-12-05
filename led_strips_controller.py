import RPi. GPIO as gpio
import time

def control_strips():
    # active low
    inactive = 1
    flicker = 1 #forever turning var
    #pins
    pin_cup = 24
    pin_beer_pour = 10
    path_to_state = "/home/pi/autochopp-machine/embedded_electronics/tmp/leds.status"
    
    #setting pins on raspberry py
    gpio.setmode(gpio.BCM)
    gpio.setup(pin_beer_pour, gpio.OUT)
    gpio.setup(pin_cup, gpio.OUT)

    #time delay
    t = 0.5 #seconds    

    #run
    while(True):
        try:
            stats = ""
            try:
                f = open(path_to_state, "r")
                stats = f.read()
                f.close()
            except IOError:
                pass
            flicker ^= 1 #keeps turning
            
            if stats=="taking_cup":
                gpio.output(pin_cup, flicker)
                gpio.output(pin_beer_pour, inactive)

            elif stats=="pouring_beer":
                gpio.output(pin_beer_pour,flicker)
                gpio.output(pin_cup, inactive)
            
            else:
                gpio.output(pin_cup, inactive)
                gpio.output(pin_beer_pour, inactive)
            
            time.sleep(t)
        
        except KeyboardInterrupt:
            gpio.cleanup()
            break
                
if __name__=="__main__":
    control_strips()
