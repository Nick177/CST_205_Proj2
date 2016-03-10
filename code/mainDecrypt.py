from PIL import Image
from myConvert import *
from manip import *

pixDiff = 0

im = Image.open('../Pictures/1.png')
jm = Image.open('../Pictures/newPic.png')

width, height = im.size

#verify the new image is encrypted by comparing to the original image
for x in range(0, width):
    for y in range(0, height):
    	r, g, b = im.getpixel((x,y))
    	r2,g2,b2 = jm.getpixel((x,y))
        if(r != r2 or g != g2 or b != b2):
            pixDiff = pixDiff + 1
            
print(pixDiff)
##########################################################################
pixX = 0
pixY = 0
message = ""
letterInBinary = ""
letterInAscii = None
actualLetter = None
#holds the 9 RGB vals of the 3 pixels
letterInBinNine=""

	
	#1) Convert each RGB value to binary [one at a time]
	#2) Save the least significat 0 or 1 to a separate string
	#3) At the end of the third pixel, convert separate binary string to decimal value (ascii value of actual letter)
	#4) Convert ascii value to character and save character to result string
	#5) Repeat steps 1 - 4 until end of loop
	
	#"""
for ix in range(0, pixDiff / 3):
	#This for loop will run 3 times for 3 pixels needed to store a single letter
	for jx in range(0, 3):
		r, g, b = jm.getpixel((pixX,pixY))
		rBin = decimalToBinary(r)
		gBin = decimalToBinary(g)
		bBin = decimalToBinary(b)
		print(rBin, gBin, bBin)
		letterInBinNine = letterInBinNine + rBin[7] + gBin[7] + bBin[7]
		if(pixX == width):
			pixX = 0
			pixY = pixY + 1
		else:
			pixX = pixX + 1
	#saves the need least sig values
	for i in range(0,8):
		letterInBinary= letterInBinary+letterInBinNine[i]
	#letterInBinary = letterInBinNine[0:8]
	print(letterInBinary)
	letterInAscii = binaryToDecimal(letterInBinary)
	actualLetter = asciiToCharacter(letterInAscii)
	message = message + actualLetter
	#Resest variables for next run thru
	letterInBinNine = ""
	letterInBinary = ""
	#End of inner loop
"""
letterInBinary = letterInBinNine[:7]
letterInAscii = convertToDecimal(letterInBinary)
actualLetter = convertToCharacter(letterInAscii)
message = message + actualLetter
"""

#Resest variables for next run thru
letterInBinNine = ""
letterInBinary = ""    
    
print(message)
   