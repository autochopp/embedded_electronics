# all the set of functions that will be used 
import socket
import RPi.GPIO as gpio
import time

# receiving data
def receiver():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 9600
    BUFFER_SIZE = 1    # Normally 1024, but we want fast response
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((TCP_IP, TCP_PORT))
    soc.listen(1)
    #print "Up and running!!"
    conn, addr = soc.accept()
    #print 'Connection address:', addr
    data = conn.recv(BUFFER_SIZE)
    #print "received data:", data
    conn.close()
    #print "Server close"
    #COD:[COL, TM, CHP]
    my_dictionary = {"0":[500,"tradicional", 1 ], "1":[500,"tradicional", 2 ], "2":[700,"tradicional", 1 ], "3":[700,"tradicional", 2 ]}

    try:
    	return my_dictionary[data]
    except:
    	raise KeyError("Wrong code!") 

def check_cup():
    sensor_pin = 18
    gpio.setmode(gpio.BCM)
    gpio.setup(sensor_pin, gpio.IN, gpio.PUD_UP)
    start = time.time()
    while True:
        if gpio.input(sensor_pin) == 0:
                #print "Cup placed!!"
                data = True
                break

            else: 
                #print "No cup!!"
                if (time.time() - start) > 60:
                    data = False
                    break
            time.sleep(0.1)
    gpio.cleanup()
    return data


######################### test ##############
def test():
	print "Init"
	print "Value from socket:", receiver()    

if __name__=="__main__":
		test()