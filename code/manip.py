def checkEight(x):
	lengthx = len(x)
	neededZeros=8-lengthx
	result = ""
	for i in range (0, neededZeros):
		result=result+'0'

	result=result+x
	return result

def changeLeastSig(DecimalColor, binaryLetter):
	if binaryLetter=='1':
		DecimalColor=DecimalColor|1	
	if binaryLetter=='0':
		DecimalColor=DecimalColor&254
	return DecimalColor
		
	
		
	