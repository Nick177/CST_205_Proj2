#This file contains all conversion functions we will need for this project

#Summary: This function converts a decimal value to binary format
#Precondition: Pass in a decimal value
#Postcondition: Returns binary string of decimal value passed in
def decimalToBinary(dVal):
	binNum = "{0:b}".format(dVal)
	return binNum

#Summary: This function converts a character to its correlated asci value
#Preconditiion: Pass in a character
#Postcondtion: Returns decimal number representing Asci value of that character
def characterToAscii(ch):
	asciVal = ord(ch)
	return asciVal
	
def asciiToCharacter(asciiVal):
	letter = chr(asciiVal)
	return letter
	

#Summary: This function converts a binary value to decimal format
#Precondiition: Pass in binary value
#Postcondtion: Returns decimal value representing the binary value passed in
def binaryToDecimal(bVal):
	decVal = int(bVal, 2)
	return decVal
