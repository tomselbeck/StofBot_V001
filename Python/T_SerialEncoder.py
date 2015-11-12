

# Serial Encoder: Takes a variable, encodes it into a serial communication format, to be decoded by the Arduino. 

def Encoder(VarID,VarValue):

	## Create output array
	print ("Running Serial Encoder")
	StrVarValue = map(int, str(VarValue))
	#print StrVarValue
	## Add a zero the the front of the list to make shure the value string stays 4 strings long 
	if (len(StrVarValue) == 3):	
		StrVarValue.insert(0,"0")
		pass
	if (len(StrVarValue) == 2):	
		StrVarValue.insert(0,"0")
		StrVarValue.insert(1,"0")
		pass
	if (len(StrVarValue) == 1):	
		StrVarValue.insert(0,"0")
		StrVarValue.insert(1,"0")
		StrVarValue.insert(2,"0")

		pass
	if (len(StrVarValue) == 0):	
		StrVarValue.insert(0,"0")
		StrVarValue.insert(1,"0")
		StrVarValue.insert(2,"0")
		StrVarValue.insert(3,"0")
		pass

	## Create output list  ##
	Output = ['O',VarID[0],VarID[1],StrVarValue[0],StrVarValue[1],StrVarValue[2],StrVarValue[3],'C']
	print Output
	print ("Done")
	return Output
	pass


## Scipt End












