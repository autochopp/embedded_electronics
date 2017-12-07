# from https://pimylifeup.com/raspberry-pi-temperature-sensor/
#use 3v3, a 4k7ohms between vcc and data and use pin7
from temperature_reader import getTemperature
import time
import  RPi.GPIO as gpio

def temp_control(min_temp=4., max_temp=6., active_low=False, interval=10.):
    relay_pin = 2
    gpio.setmode(gpio.BCM)
    gpio.setup(relay_pin, gpio.OUT)
      
    if active_low:
        active = 0
        inactive = 1
    else:
        active = 1
        inactive = 0

    try:
        temp = getTemperature()
    except:
        temp = 25.
    if (temp>max_temp):
        gpio.output(relay_pin, active)
        print "relay on! "
    
    if(temp<min_temp):
        gpio.output(relay_pin, inactive)
        print "relay off!"
    print "temperature", temp
    
    time.sleep(interval)

if __name__ =="__main__":
    print "starting temperature control"
    while True:
        try:
            temp_control(active_low=True)
        except KeyboardInterrupt:
            break
    gpio.cleanup()
