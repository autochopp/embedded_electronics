import RPi.GPIO as gpio
import time

def steps(total_steps, pins, forward=True, interval = 0.04):
   
     
    pin_1 = pins[0]
    pin_2 = pins[1]
    pin_3 = pins[2]
    pin_4 = pins[3]
    # default pins
  

    gpio.setmode(gpio.BCM)    
    gpio.setup(pin_1, gpio.OUT)
    gpio.setup(pin_2, gpio.OUT)
    gpio.setup(pin_3, gpio.OUT)
    gpio.setup(pin_4, gpio.OUT)

    for i in xrange(0, total_steps/4):
        
        if forward:        
            gpio.output(pin_1, 1)
            gpio.output(pin_2, 1)
            gpio.output(pin_3, 0)
            gpio.output(pin_4, 0)

            time.sleep(interval)    

            gpio.output(pin_1, 0)
            gpio.output(pin_2, 1)
            gpio.output(pin_3, 1)
            gpio.output(pin_4, 0)

            time.sleep(interval)    

            gpio.output(pin_1, 0)
            gpio.output(pin_2, 0)
            gpio.output(pin_3, 1)
            gpio.output(pin_4, 1)

            time.sleep(interval)    

            gpio.output(pin_1, 1)
            gpio.output(pin_2, 0)
            gpio.output(pin_3, 0)
            gpio.output(pin_4, 1)

            time.sleep(interval)   

                       
        
        else:
            gpio.output(pin_1, 1)
            gpio.output(pin_2, 0)
            gpio.output(pin_3, 0)
            gpio.output(pin_4, 1)

            time.sleep(interval)    

            gpio.output(pin_1, 0)
            gpio.output(pin_2, 0)
            gpio.output(pin_3, 1)
            gpio.output(pin_4, 1)

            time.sleep(interval)    

            gpio.output(pin_1, 0)
            gpio.output(pin_2, 1)
            gpio.output(pin_3, 1)
            gpio.output(pin_4, 0)

            time.sleep(interval)    

            gpio.output(pin_1, 1)
            gpio.output(pin_2, 1)
            gpio.output(pin_3, 0)
            gpio.output(pin_4, 0)

            time.sleep(interval)


#set to 45 degrees and back
def cup_to_position(set_to_angle):
    st = 52
    
    pins = [12, 16, 20, 21]
    
   
    if set_to_angle:
    # 200steps per revolution, 1.8 degrees, but the motor needs to turn 90degrees, 50 steps
        steps(st, pins, forward=True, interval=0.02)
        #gpio.output(12, 1)
        #gpio.output(16, 0)
        #gpio.output(20, 0)
        #gpio.output(21, 1)


    else:
        steps(st, pins, forward=False, interval=0.02)

    gpio.cleanup()

#control valve
def valve_control(set_open):
    
      
    pins = [6, 13, 19, 26]
    if set_open:
    # 200steps per revolution, 1.8 degrees, but the motor needs to turn 90degrees, 50 steps
        steps(40, pins, forward=False, interval=0.004)

    else:
        steps(40, pins, forward=True, interval=0.004)
    
    gpio.cleanup()

def foam(minus):
   
      
    pins = [6, 13, 19, 26]
    if minus:
        steps(10, pins,  forward=False, interval=0.004)

    else:
        steps(10, pins,  forward=False, interval=0.004)

#########################    TEST  ####################
if __name__=="__main__":
    for i in xrange(1):



        #time.sleep(1)
        #print "setting to cup"
        #cup_to_position(True)
        #time.sleep(2)
        valve_control(True)
        time.sleep(3)
        valve_control(False)
        #time.sleep(2)
        #print "setting it back"
        #cup_to_position(False)
       
   # gpio.cleanup()
