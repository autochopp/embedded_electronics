from cup_detector import *
from stepper_motor import *
from relay_control import relay_control
import time
import RPi.GPIO as gpio

class MachineController:

    def __init__(self):
        gpio.setwarnings(False)
        gpio.cleanup()
        
        self.t_out = 60.
        
        self.relay_pin_small = 27 
        self.relay_pin_big = 22 

        self.cup_size_pin = None
        self.collar = False
        self.type = "tradicional" #for compatibility only
        self.size = "small"
        self.small_time = 10. #need to be tested
        self.big_time = 5. # need to be tested
        self.collar_time = 2. # needs to tested

    def power_on_nobreak(self):
        nobk_pin = 23
        gpio.setmode(gpio.BCM)
        gpio.setup(nobk_pin, gpio.IN, gpio.PUD_UP)
        if (not gpio.input(nobk_pin)):
            gpio.cleanup()
            return True
        else:
            gpio.cleanup()
            return False
    #receives and sets the settings
    def set_chopp(self, chopp):
        if chopp==0:
            self.cup_size_pin = self.relay_pin_small 
            self.collar = False
            self.type = "tradicional"
            self.size = "small"
        
        elif chopp==1:
            self.cup_size_pin = self.relay_pin_small 
            self.collar = True
            self.type = "tradicional"
            self.size = "small"
        
        elif chopp==2:
            self.cup_size_pin = self.relay_pin_big
            self.collar = False
            self.type = "tradicional"
            self.size = "big"
        
        elif chopp==3:
            self.self.cup_size_pin = self.relay_pin_big
            self.collar = True
            self.type = "tradicional"
            self.size = "big"
        print "########################### %s %%%%%%%%%%%%%%"%chopp
    #returns true when the cup drawer is open
    def is_drawer_open(self):
        relay_control(self.cup_size_pin, True)
        time.sleep(1)
        relay_control(self.cup_size_pin, False)
        return True # it stays open till the next step closes it
    
    #returns true if the cup is placed and in the right position to get beer
    def cup_activate(self):
        #detect cup in place
        if cup_in_place(self.t_out):
            return True
        else:
            return False 

    # returns true when the beer was already taken
    def already_got_beer(self):
        #check if it generates foam TODO
        #valve_control(True)
        #time.sleep(1) #to get some foam 
        #valve_control(False)
        
        if self.size=="small":
            t = self.small_time
        elif self.size=="big":
            t = self.big_time
        
        #set cup to position
        cup_to_position(True, self.size)
        
        #start time
        t1 = time.time()
        t2 = time.time()
        sensor = False
        #pouring chopp out
        valve_control(True)
        
        print"total", t
        while(not sensor): #stops by time or beer level
            t2 = time.time()
            time.sleep(1)
            if (t2-t1)<= t:
                break
            else:
                print "time", t2-t1
            sensor = edge_detector()
        #stops pouring
        valve_control(False)

        cup_to_position(False, self.size) 
        #making collar and closing chopp
        if self.collar:
            valve_control(True)
            time.sleep(self.collar_time)
            valve_control(False)
        
        return True


##################### TEST ########################
if __name__=="__main__":
    while(True):
        try:
            machine = MachineController()
            """
            print"chopp test"
            print "Tirando chopp pequeno e pouco colarinho, status:", machine.set_chopp(1)
            print "Abrindo gaveta, status: ",  machine.is_drawer_open()
            print "Posicione o copo na base"
            print "Copo na base:", machine.cup_activate()
            print "Tirar chopp"
            print "chopp, status:", machine.already_got_beer()
            """
           
            print "power on nobreak: ", machine.power_on_nobreak()
        except KeyboardInterrupt:
            break 
            gpio.cleanup()
        
