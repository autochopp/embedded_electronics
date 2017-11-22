from cup_detector import cup_in_place
from stepper_motor import *
from relay_control import relay_control
class MachineController:

	def __init__(self):
		self.t_out = 20.
	
	#returns true when the cup drawer is open
	def is_drawer_open(self):
		pass
	#returns true if the cup is placed and in the right position to get beer
	def cup_activate(self):
		
		#detect cup in place
		if cup_in_place(self.t_out):
			#when placed, move to 45 degrees
			cup_to_position(True)
			
			# close cup drawer
			return True
		else:
			return False 

	
	# returns true when the beer was already taken
	def already_got_beer(self, what_beer):
		pass


##################### TEST ########################
if __name__=="__main__":
	machine = MachineController()
	print"cup activate test"
	if machine.cup_activate():
		print "placed"
	else:
		print "not placed"
