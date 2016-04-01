from PIL import Image
from myConvert import *
from manip import *
import os

def encrypt(im, msg):
    #The following 2 variables are used to navigate thru the picture's pixels
    # x coordinate
    pixX = 0
    # y coordinate
    pixY = 0

    im = im.convert('RGB')
    width, height = im.size

    #Copies original image
    #This copy will be used as the changed image
    jm = im.copy()
    jm = jm.convert('RGB')


    msgLength = len(msg)

    #The following variable will be used in the inner for loop
    #It will go thru the indexes of the binary string of the current letter
    nextIndex = 0

    #below is a for loop that will iterate  thru the individual letters
    #in our secret message (takes one letter at a time)
    for ix in range(0, msgLength):
        asciiOfLetter = characterToAscii(msg[ix])
        letterInBin = decimalToBinary(asciiOfLetter)
        letterInBin = checkEight(letterInBin)

        #This for loop will run 3 times for 3 pixels needed to store a single letter
        #Essentially, this will encrypt the current letter in our picture
        for jx in range(0, 3):
            r, g, b = jm.getpixel((pixX,pixY))

            rBin = decimalToBinary(r)
            gBin = decimalToBinary(g)
            bBin = decimalToBinary(b)

	
            if nextIndex < 8:
                r =  changeLeastSig(r, letterInBin[nextIndex])
                nextIndex = nextIndex + 1
            if nextIndex < 8:
                g = changeLeastSig(g, letterInBin[nextIndex])
                nextIndex = nextIndex + 1
            if nextIndex < 8:
                b = changeLeastSig(b, letterInBin[nextIndex])
                nextIndex = nextIndex + 1

            rBin = decimalToBinary(r)
            gBin = decimalToBinary(g)
            bBin = decimalToBinary(b)

            jm.putpixel((pixX, pixY), (r,g,b))

            if(pixX == width):
                pixX = 0
                pixY = pixY + 1
            else:
                pixX = pixX + 1


        #reassign nextIndex to 0 to be ready for next binary string of next letter
        nextIndex = 0
    """
    The following block of code saves the original picture
    in the 'Original_Pics' directory for easy access.
    Likewise, it does the same for the encrypted picture
    """
    currentDirectory = os.getcwd()
    newPath = currentDirectory + '/Original_Pics/'
    
    if not os.path.exists(newPath):
        os.makedirs(newPath)
        im.save(newPath + '/original.png', 'PNG')
    else:
        im.save(newPath + 'original.png', 'PNG')

    newPath = currentDirectory + '/Encrypted_Pics/'
    
    if not os.path.exists(newPath):
        os.makedirs(newPath)
        jm.save(newPath + '/picWithMSG.png', 'PNG')
    else:
        jm.save(newPath + 'picWithMSG.png', 'PNG')


    return jm
