from PIL import Image
from myConvert import *
from manip import *


#The following 2 variables are used to navigate thru the picture's pixels
# x and y coordinates
pixX = 0
pixY = 0

im = Image.open('../Pictures/1.png')

width, height = im.size

#Folling line of code makes a copy of image
#This copy will be used as the changed image
jm = im.copy()

msg = "hi"

msgLength = len(msg)

#The following variable will be used in inner for loop
#It will go thru the indexes of the binary string of the current letter
nextIndex = 0

#below is a for loop that will iterate  thru the individual letters
#in a message (takes one letter at a time)
for ix in range(0, msgLength):
	#asciOfLetter = convertToAsci(msg[ix])
	asciiOfLetter = characterToAscii(msg[ix])
	#letterBin = convertToBinary(asciOfLetter)
	letterInBin = decimalToBinary(asciiOfLetter)
	#letterBin = checkEight(letterBin)
	letterInBin = checkEight(le
	print letterBin
	
	#This for loop will run 3 times for 3 pixels needed to store a single letter
	#Essentially, this will encrypt the current letter in our picture
	for jx in range(0, 3):
		r, g, b = jm.getpixel((pixX,pixY))
		
		rBin = convertToBinary(r)
		gBin = convertToBinary(g)
		bBin = convertToBinary(b)
		print(rBin, gBin, bBin)
		
		
		if nextIndex < 8:
			r =  changeLeastSig(r, letterBin[nextIndex])
			nextIndex = nextIndex + 1
		if nextIndex < 8:
			g = changeLeastSig(g, letterBin[nextIndex])
			nextIndex = nextIndex + 1
		if nextIndex < 8:
			b = changeLeastSig(b, letterBin[nextIndex])
			nextIndex = nextIndex + 1
		"""
		r = convertToDecimal(rBin)
		g = converToDecimal(gBin)
		b = converToDecimal(bBin)
		"""
		rBin = convertToBinary(r)
		gBin = convertToBinary(g)
		bBin = convertToBinary(b)
		print(rBin, gBin, bBin)

		jm.putpixel((jx + pixX, 0 + pixY), (r, g, b))
	
		if(pixX == width):
			pixX = 0
			pixY = pixY + 1
		else
			pixX = pixX + 1
	
	
	#reassign nextIndex to 0 to be ready for next binary string of next letter
	nextIndex = 0
	
	
print("Finished")
		


jm.save('../Pictures/newPic.png', 'PNG')


print(im.getpixel((0,0)))
print(im.getpixel((1,0)))
print(im.getpixel((2,0)))
print(jm.getpixel((0,0)))
print(jm.getpixel((1,0)))
print(jm.getpixel((2,0)))
