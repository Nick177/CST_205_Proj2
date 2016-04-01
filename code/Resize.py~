#Resize an image: 
##################################
import PIL
from PIL import Image

def resizeImage(img):
    #basewidth = 300
    baseHeight = 350
    #img = Image.open('somepic.jpg')
    #wpercent = (basewidth/float(img.size[0]))
    hpercent = (baseHeight/float(img.size[1]))
    #hsize = int((float(img.size[1])*float(wpercent)))
    wsize = int((float(img.size[0])*float(hpercent)))
    img = img.resize((wsize,baseHeight), PIL.Image.ANTIALIAS)
    #img.save('sompic.jpg')
    return img
###################################

