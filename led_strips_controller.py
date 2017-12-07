import RPi. GPIO as gpio
import time

def control_strips():
    # active low
    active = 0
    flicker = 1 #forever turning var
    #pins
    pin_cup = 24
    pin_beer_pour = 10
    path_to_state = "/home/pi/autochopp-machine/embedded_electronics/tmp/leds.status"
    
    #setting pins on raspberry py
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(pin_beer_pour, gpio.OUT)
    gpio.setup(pin_cup, gpio.OUT)

    #time delay
    t = 0.5 #seconds    

    #makes sure it is all off before starting
    gpio.output(pin_cup, active)
    gpio.output(pin_beer_pour, active)

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
            
            if stats in ["taking_cup", "taking_cup\n"]:
                print "taking cup", [stats]
                gpio.output(pin_cup, flicker)
                gpio.output(pin_beer_pour, active)

            elif stats in ["pouring_chopp", "pouring_chopp\n"]:
                gpio.output(pin_beer_pour,flicker)
                gpio.output(pin_cup, active)
                print "pouring choppp", [stats]
            
            else:
                print "off", [stats]
                gpio.output(pin_cup, active)
                gpio.output(pin_beer_pour, active)
            
            time.sleep(t)
        
        except KeyboardInterrupt:
            gpio.cleanup()
            break
                
if __name__=="__main__":
    control_strips()
