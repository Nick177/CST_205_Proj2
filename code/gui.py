from Tkinter import *
import ttk
from PIL import Image, ImageTk
from tkFileDialog import askopenfilename
from Resize import resizeImage
from mainEncr import *
from mainDecr import *

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Steganography")
        winWidth = 750
        winHeight = 550
        self.backgroundColor = '#353B3D'
        self.fontStyle = ("Times", 13)
        self.fontColor = 'white'
        
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Main Page", command=self.openMainPage)

        menubar.add_cascade(label="Menu", menu=fileMenu)
         ###################
        # Main Page Setup #
        ###################
        self.mainScreen = Frame(self.master, width = winWidth, height = winHeight, background = self.backgroundColor)
        self.mainScreen.grid(column=4, row=0, padx=20, pady=5, sticky=(W, N, E))
        
        pageTitle= Label(self.mainScreen, text="Main Page", font=("Times", 24), fg=self.fontColor, background = self.backgroundColor)

        pageTitle.grid(row = 0, column = 6,columnspan=3, padx= 0, pady = 25, sticky= W+N+S+E)

        openButton = Button(self.mainScreen, text="Decrypt", command=self.openDecr)
        openButton.grid(row=1, column=9, padx= 50)
        
        openButton = Button(self.mainScreen, text="Encrypt", command=self.openEncr)
        openButton.grid(row=1, column=0, padx=200, columnspan=7)

        ########################
        # Encrypt Screen Setup #
        ########################
        self.encryptScreen = Frame(self.master, width = winWidth, height = winHeight, background = self.backgroundColor)

        self.encryptScreen.grid(column=0, row=0, padx=20, pady=5, sticky=(W, N, E))

        origPicLabel = Label(self.encryptScreen, text="Original Picture:", background=self.backgroundColor, font=self.fontStyle, fg = self.fontColor)
        origPicLabel.grid(row=0, column=0, padx = 25, pady = 15)

        self.origIm = Image.open('samplePic.png')
        self.origIm = resizeImage(self.origIm)
        photo = ImageTk.PhotoImage(self.origIm)


        self.origImLabel = Label(self.encryptScreen, relief=SUNKEN, image=photo)
        self.origImLabel.image = photo
        self.origImLabel.grid(row=1, column = 0, rowspan=2, columnspan=2, ipadx = 10, padx = 25, ipady = 10, pady = 15)


        
        openButton = Button(self.encryptScreen, text="Open", command=self.openNewPicture)
        openButton.grid(row=3, column=0)
        
        labelForEntry = Label(self.encryptScreen, text="Secret Message:", background=self.backgroundColor, font=self.fontStyle, fg=self.fontColor)
        labelForEntry.grid(row=4, column = 0, pady = 15)
        
        self.entryText = StringVar()
        entry = Entry(self.encryptScreen, textvariable=self.entryText)
        entry.grid(row=4, column = 1)
        
        encryptButton = Button(self.encryptScreen, text="Encrypt", command=self.onClickEncrypt)
        encryptButton.grid(row=4, column = 2, padx=15)

        

        ########################
        # Decrypt Screen Setup #
        ########################
        self.decryptScreen = Frame(self.master, width = winWidth, height = winHeight, background = self.backgroundColor)
        self.decryptScreen.grid(column=0, row=0, padx=20, pady=5, sticky=(W, N, E))

        
        decryPicLabel = Label(self.decryptScreen, text="Picture to decrypt:", background=self.backgroundColor, font=self.fontStyle, fg=self.fontColor)
        decryPicLabel.grid(row=0, column=0, padx = 25, pady = 15)



        openDecrButton = Button(self.decryptScreen, text="Open", anchor=S, command=self.openDecrIM)
        openDecrButton.grid(row=6, column=0)

        self.decrImLabel = Label(self.decryptScreen, relief=SUNKEN) #self.imToDecrLabel

        self.encryPicLabel = Label(self.encryptScreen, relief=SUNKEN)

        self.msg = StringVar()
        self.msg.set('')
        

        self.encryptScreen.grid_forget()
        self.decryptScreen.grid_forget()


    def openDecrIM(self):
        self.picEncr = askopenfilename()
        self.decryptIm = Image.open(self.picEncr)
        resized = resizeImage(self.decryptIm)
        photo = ImageTk.PhotoImage(resized)
        self.decrImLabel.configure(image = photo)
        self.decrImLabel.image = photo
        self.decrImLabel.grid(row=1, column=0, rowspan=4, columnspan=4)

        self.text = StringVar()
        self.text.set('Open original picture:')
        self.picTextLabel = Label(self.decryptScreen, textvariable=self.text,  background=self.backgroundColor, font=self.fontStyle, fg = self.fontColor)
        self.picTextLabel.grid(row=0, column=4, padx = 25, pady = 15)

        self.openButton = Button(self.decryptScreen, text="Open", anchor=S, command=self.openEncrPic)
        self.openButton.grid(row=2, column=4, pady=15)

    def openNewPicture(self):
        
        pic = askopenfilename() 
        self.origIm = Image.open(pic)
        resized = resizeImage(self.origIm)
        photo = ImageTk.PhotoImage(resized)
        self.origImLabel.configure(image = photo)
        self.origImLabel.image = photo


    def onClickEncrypt(self):
        self.encrPicLabel = Label(self.encryptScreen, text="Picture with Secret Message", padx=25, pady=15, background = self.backgroundColor, font=self.fontStyle, fg=self.fontColor, justify= RIGHT)
        self.encrPicLabel.grid(row=0, column=3)
        
        secretMessage = self.entryText.get()        

        
        self.encryptIm = encrypt(self.origIm, secretMessage)
        resized = resizeImage(self.encryptIm)
        photo = ImageTk.PhotoImage(resized)
        self.encryPicLabel.configure(image=photo)
        self.encryPicLabel.image = photo
        self.encryPicLabel.grid(row=1, column = 3, rowspan=2, columnspan=2, ipadx = 10, padx = 25, ipady = 10, pady = 15)


    def openEncrPic(self):
        self.picOrig = askopenfilename()
        fileName = StringVar()
        fileName.set(self.picOrig)
        self.encrImLabel = Label(self.decryptScreen, textvariable=fileName)
        self.encrImLabel.grid(row=1, column = 4, ipadx = 25, padx = 25, ipady = 15, pady = 15)

        self.text.set('Original Picture:')

        self.decryptButton = Button(self.decryptScreen, text="Decrypt", anchor=S, command=self.decryptIM)#, pady=25)
        self.decryptButton.grid(row=6, column=4)

    def decryptIM(self):
        self.secretMsg = Label(self.decryptScreen, textvariable=self.msg, background='white', font=self.fontStyle)
        self.secretMsg.grid(row=3, column=4, padx=25, pady=15)
        
        orig = Image.open(self.picOrig)
        encr = Image.open(self.picEncr)
        print(orig.size, encr.size)
        m = decrypt(orig, encr)
        
        self.msg.set(m)


    
    #Main page, Encrypt button   
    def openEncr(self):
        self.mainScreen.grid_forget()
        self.decryptScreen.grid_forget()
        self.encryptScreen.grid(column=0, row=0, padx=20, pady=5, sticky=(W, N, E))
    
    #Main page, Decrypt button    
    def openDecr(self):
        self.mainScreen.grid_forget()
        self.encryptScreen.grid_forget()
        self.decryptScreen.grid(column=0, row=0, padx=20, pady=5, sticky=(W, N, E))


    #Back to main page
    def openMainPage(self):
        self.decryptScreen.grid_forget()
        self.encryptScreen.grid_forget()
        self.mainScreen.grid(column=0, row=0, padx=20, pady=5, sticky=(W, N, E))


root = Tk()
root.geometry('850x750')
root.configure(background='#353B3D')
my_gui = GUI(root)
root.mainloop()
