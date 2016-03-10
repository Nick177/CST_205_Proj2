
from PIL import Image
from myConvert import *
from manip import *

pixDiff = 0

im = Image.open('../Pictures/1.png')
jm = Image.open('newPic')

width, height = im.size

#verify the new image is encrypted by comparing to the original image
for x in range(0, width):
    for y in range(0, height):
        if(im.getpixel((x,y)) != jm.getpixel((x,y))):
            pixDiff = pixDiff + 1
            
            
##########################################################################

message = ""
#holds the 9 RGB vals of the 3 pixels
letterInBinNine=""
#holds the 8 RGB vals needed for the asci
letterInBinary = ""
pixX=0

	
	#This for loop will run 3 times for 3 pixels needed to store a single letter
for jx in range(0, 3):
	r, g, b = jm.getpixel((pixX,pixY))
	rBin = convertToBinary(r)
	gBin = convertToBinary(g)
	bBin = convertToBinary(b)
	letterInBinNine=letterInBinNine + rBin[7] + gBin[7] + bBin[7]
		

#saves the need least sig values
for i in range(0,8)
	letterInBinary= letterInBinary+letterInBinNine[i]
	
			