import time 
import math 

####################################################
# Calculates the sensor servos position  
####################################################


def angle():


	ServoSpeed = 1
	sin = math.sin(time.time()*ServoSpeed)
	sin = int((sin+1)*90)
	return sin




