from myConvert import *

def checkEight(x):
	lengthx = len(x)
	neededZeros=8-lengthx
	result = ""
	for i in range (0, neededZeros):
		result=result+'0'

	result=result+x
	return result

def changeLeastSig(DecimalColor, binaryLetter):
	#convert decimal color to binary string to compare last character to binaryLetter
	#1 convert decimal color to binary string
	#2 Check if last character equals binaryLetter
	#3 if so then change 2nd least sig and convert back to decimal
	#4 if not then just use following if statements
	binColor = decimalToBinary(DecimalColor)
	binColor = checkEight(binColor)
	
	if(binColor[7] != binaryLetter):
		if binaryLetter=='1':
			DecimalColor=DecimalColor|1	
		if binaryLetter=='0':
			DecimalColor=DecimalColor&254
	else:
		if(binColor[6] == '1'):
			l = list(binColor)
			l[6] = '0'
			binColor = ''.join(l)
		elif(binColor[6] == '0'):
			l = list(binColor)
			l[6] = '1'
			binColor = ''.join(l)
		DecimalColor = binaryToDecimal(binColor)
	return DecimalColor
		
	
		
	
