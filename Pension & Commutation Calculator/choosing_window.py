#importing tkinter module
import tkinter
from tkinter import *
from tkinter import messagebox

import sys
import os

#defining the function for the buttons to do when cicked
def basicPension():
    os.system('python Basic_Pension.py')
def commutation():
    os.system('python Commutation.py')
root = tkinter.Tk()
root.geometry("1920x1080")
root.title("--- Pension And Commutation Calculator --- Choose ")

photo = PhotoImage(file="CalcBasicPension.png")
photo2 = PhotoImage(file="CalcCommutation.png")
#buttons configurations
btn = Button(
    root,
    image=photo,
    command=basicPension,
    border=0,
)
btn.pack(side = LEFT, expand = True, fill = BOTH)

btn2 = Button(
    root,
    image=photo2,
    command=commutation,
    border=0,
)
btn2.pack(side = RIGHT, expand = True, fill =BOTH)
root.mainloop()