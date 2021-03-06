from PIL import Image
from myConvert import *
from manip import *

def decrypt(im, jm):
    #pixels difference between original and encrypted image
    pixDiff = 0

    width, height = im.size
    im = im.convert('RGB')
    jm = jm.convert('RGB')


    #verify the new image is encrypted by comparing to the original image
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = im.getpixel((x,y))
            r2,g2,b2 = jm.getpixel((x,y))
            if(r != r2 or g != g2 or b != b2):
                pixDiff = pixDiff + 1
                
    ##########################################################################
    """
    This block of code reverses the encryption process by changing the pixels
    in the encrypted image and use
    """
    pixX = 0
    pixY = 0
    message = ""
    letterInBinary = ""
    letterInAscii = None
    actualLetter = None
    letterInBinNine=""

    for ix in range(0, pixDiff / 3):
	    #This for loop will run 3 times for 3 pixels needed to store a single letter
        for jx in range(0, 3):
            r, g, b = jm.getpixel((pixX,pixY))
            rBin = decimalToBinary(r)
            rBin = checkEight(rBin)
            gBin = decimalToBinary(g)
            gBin = checkEight(gBin)
            bBin = decimalToBinary(b)
            bBin = checkEight(bBin)

            letterInBinNine = letterInBinNine + rBin[7] + gBin[7] + bBin[7]
            if(pixX == width):
                pixX = 0
                pixY = pixY + 1
            else:
                pixX = pixX + 1
        #saves the needed least sig values
        for i in range(0,8):
            letterInBinary= letterInBinary+letterInBinNine[i]

        letterInAscii = binaryToDecimal(letterInBinary)
        actualLetter = asciiToCharacter(letterInAscii)
        message = message + actualLetter
        #Resest variables for next run thru
        letterInBinNine = ""
        letterInBinary = ""
        #End of inner loop

    #Resest variables for next run thru
    letterInBinNine = ""
    letterInBinary = ""    
        
    return message
