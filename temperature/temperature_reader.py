import commands
# pin7, gpio4, 4k7 resistor
# in order to work:
# add dtoverlay=w1-gpio to the bottom of  /boot/config.txt
# sudo modprobe w1-gpio
#sudo modprobe w1-therm
#reboot
def getTemperature():
	base = "/sys/bus/w1/devices/"
	gotit = commands.getoutput("cat %s/28*/w1_slave"%base).split()[-1][2:]
	return int(gotit)/1000.

if __name__=="__main__":
	import time
	while True:
		try:
			st = time.time()
			temp = getTemperature()
			ed = time.time()
			print "Temperature: ", temp, "Time between reads: ", ed - st
		except KeyboardInterrupt:
			break
