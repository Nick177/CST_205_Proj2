from myConvert import *

#makes the string a length of 8
def checkEight(x):
	lengthx = len(x)
	neededZeros=8-lengthx
	result = ""
	for i in range (0, neededZeros):
		result=result+'0'

	result=result+x
	return result

#Changes the least significant value in the binary string
def changeLeastSig(DecimalColor, binaryLetter):
	binColor = decimalToBinary(DecimalColor)
	binColor = checkEight(binColor)
	
	#changes least sig value if different from orginal value
	if(binColor[7] != binaryLetter):
		if binaryLetter=='1':
			DecimalColor=DecimalColor|1	
		if binaryLetter=='0':
			DecimalColor=DecimalColor&254
	#changes second least sig value if the least sig was the same
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
