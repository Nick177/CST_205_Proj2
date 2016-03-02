#This file contains all conversion functions we will need for this project

#Summary: This function converts a decimal value to binary format
#Precondition: Pass in a decimal value
#Postcondition: Returns binary string of decimal value passed in
def convertToBinary(dVal):
	binNum = "{0:b}".format(dVal)
	return binNum


#Summary: This function converts a character to its correlated asci value
#Preconditiion: Pass in a character
#Postcondtion: Returns decimal number representing Asci value of that character
def convertToAsci(ch):
	asciVal = ord(ch)
	return asciVal

#Summary: This function converts a binary value to decimal format
#Precondiition: Pass in binary value
#Postcondtion: Returns decimal value representing the binary value passed in
def convertToDecimal(bVal):
	decVal = int(bVal, 2)
	return decVal
#Summary: returns the binary number needed with all 0
lengthx=len(convertToBinary(10))
def checkEight (lengthx):
	neededZeros=8-lengthx
	for i in range (0, neededZeros):
		result=result+'0'
        binNumber=result+binNum
        return binNumber
