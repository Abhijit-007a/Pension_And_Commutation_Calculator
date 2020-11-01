#import tkinter modules
import tkinter
from tkinter import *
from PIL import ImageTk,Image
import os

#defining geometry and basic characteristics of window
win = Tk()
win.geometry("1550x900")
image = Image.open('WelcomeImage.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(win, image = photo_image)
label.pack()
#giving title to the window
win.title("Pension And Commutation Calculator -- Welcome")
#assigning what happens on click
def click():
    os.system('python Login.py')

#button to go to next page
button = Button(win, text="Calculate Your Pension Now!",width= 30, bg="blue", fg="white", command=click).place(x=230, y=545)
win.mainloop()
