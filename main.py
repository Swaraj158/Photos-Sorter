import os
import shutil
from tkinter import *
from PIL import ImageTk, Image

sourceDirectory = "Images/"
selectedDirectory = "Selected/"
discardedDirectory = "Discarded/"

imgsArray = os.listdir(sourceDirectory)

global index
index = 0

global currentImg
currentImg = imgsArray[0]
total = len(imgsArray)

global lblImage
lblImage = None

def rotateFunction():
    global lblImage
    lblImage=lblImage.transpose(Image.ROTATE_270)
    new_height = 680
    new_width  = int(new_height * lblImage.width / lblImage.height)
    lblImage = lblImage.resize((new_width, new_height), Image.ANTIALIAS)
    img2= ImageTk.PhotoImage(lblImage)
    label.configure(image=img2)
    label.image=img2

def selectFunction() :
    print('Select button is clicked.')
    global currentImg
    shutil.copy(sourceDirectory+currentImg,selectedDirectory+currentImg)
    print(currentImg)
    print("Image Copied!")

def previousFunction() :
    print('Previous button is clicked.')
    global index
    print(index)
    print(total)
    if(index!=0):
        currentImg = imgsArray[index-1]
        global lblImage
        lblImage=Image.open(sourceDirectory+ currentImg)
        new_height = 680
        new_width  = int(new_height * lblImage.width / lblImage.height)
        lblImage = lblImage.resize((new_width, new_height), Image.ANTIALIAS)
        img2= ImageTk.PhotoImage(lblImage)
        label.configure(image=img2)
        label.image=img2
        label1.config(text=currentImg)
        index = index - 1
    else:
        print("First Image!")

def nextFunction() :
    print('Next button is clicked.')
    global index
    print(index)
    print(total)
    if(index!=total-1):
        global currentImg
        currentImg = imgsArray[index+1]
        global lblImage
        lblImage=Image.open(sourceDirectory+ currentImg)
        new_height = 680
        new_width  = int(new_height * lblImage.width / lblImage.height)
        lblImage = lblImage.resize((new_width, new_height), Image.ANTIALIAS)
        img2= ImageTk.PhotoImage(lblImage)
        label.configure(image=img2)
        label.image=img2
        label1.config(text=currentImg)
        index = index + 1
    else:
        print("All Images Done")

def discardFunction() :
    print('Discard button is clicked.')
    global currentImg
    shutil.copy(sourceDirectory+currentImg,discardedDirectory+currentImg)
    print("Image Copied!")

window_main = Tk(className='Tkinter - PhotoManager', )
window_main.geometry("1000x800")
window_main.configure(bg='black')
window_main.state('zoomed')


frame1 = Frame(window_main, width=40, height=200,bg='black')
frame1.pack(side=TOP,padx=20, pady=30)

lblText = currentImg
label1 = Label(frame1,width=50,height=4,text=currentImg)
label1.grid(row=1,column=1,padx=20)

button_rotate = Button(frame1, text ="Rotate", command=rotateFunction)
button_rotate.config(width=25, height=4)
button_rotate.grid(row=1,column=2,padx=20)


# Create a Label Widget to display the text or Image
lblImage=Image.open(sourceDirectory+ currentImg)
new_height = 680
new_width  = int(new_height * lblImage.width / lblImage.height)
lblImage = lblImage.resize((new_width, new_height), Image.ANTIALIAS)
img1= ImageTk.PhotoImage(lblImage)
label = Label(window_main, image = img1)
label.pack(side=TOP,padx=20, pady=30)

frame = Frame(window_main, width=60, height=200,bg='black')
frame.pack(side=BOTTOM,padx=20, pady=30)

button_select = Button(frame, text ="Select", command=selectFunction)
button_select.config(width=25, height=4)
button_select.grid(row=1,column=2,padx=20)

button_previous = Button(frame, text ="Previous", command=previousFunction)
button_previous.config(width=25, height=4)
button_previous.grid(row=1,column=3,padx=20)

button_next = Button(frame, text ="Next", command=nextFunction)
button_next.config(width=25, height=4)
button_next.grid(row=1,column=4,padx=20)

button_discard = Button(frame, text ="Discard", command=discardFunction)
button_discard.config(width=25, height=4)
button_discard.grid(row=1,column=5,padx=20)


window_main.mainloop()
