# importing tkinter module.
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox  # for pop-up window
import mysql.connector as sql  # to connect to MySQL server

import os

top = tkinter.Tk()

# Give basic characteristics and geometry to the window.
top.geometry("1000x600")
image = Image.open('Commutation_Image.png')
photo_image = ImageTk.PhotoImage(image)
label = tkinter.Label(top, image = photo_image)
label.pack()
top.title(" - Pension and Commutation Calculator - ")
db = sql.connect(host="localhost", user="root", passwd="Password@123")

cur = db.cursor()

name_var = tkinter.StringVar()
year_var = tkinter.IntVar()
month_var = tkinter.IntVar()
one_var = tkinter.IntVar()
ten_var = tkinter.IntVar()
commutation_var = tkinter.IntVar()
basic_pension = tkinter.IntVar()
reduced_pension = tkinter.IntVar()
totalcommutation_var = tkinter.IntVar()


def store(result, redd):
    db = sql.connect(host="localhost", user="root", passwd="Password@123")

    cur = db.cursor()

    try:

        cur.execute("create database comm")

        db = sql.connect(host="localhost", user="root", passwd="Password@123", database="comm")

        cur = db.cursor()


    except sql.errors.DatabaseError:

        db = sql.connect(host="localhost", user="root", passwd="Password@123", database="comm")

        cur = db.cursor()

        try:

            cur.execute("create table main(commut  int,redpen int )")


        except sql.errors.ProgrammingError:

            pass


    finally:

        try:

            cur.execute("create table main(commut int,redpen int  )")


        except sql.errors.ProgrammingError:

            pass

    while True:
        result
        redd

        cur.execute("insert into main values({},{})".format(int(result), int(redd)))

        db.commit()
        messagebox.showinfo("Status", "your data is stored in database successfully")
        break

    cur.close()

    db.close()


def calcom():
    temp2 = commutation_var.get()
    temp3 = basic_pension.get()
    if (temp2 <= 33):
        temp = ((temp2 / 100) * temp3) * 10
        totalcommutation_var = temp
        temp1 = (temp3 - (temp2 / 100) * temp3)
        reduced_pension = temp1
        messagebox.showinfo("Total commutation is ", totalcommutation_var)
        messagebox.showinfo("Final pension is ", reduced_pension)
        store(totalcommutation_var, reduced_pension)
    else:
        messagebox.showinfo("Warning!! ", "invalid commutation value. Please enter a valid value less than 33")


def Redirect_Basic_Pension():
    os.system('python BAsic_Pension.py')


# creating a label and entry for name using widget Label and Entry rspt
basicpension_label = tkinter.Label(top, text='Your Basic Pension :', font=('calibre', 10, 'bold'))
basicpension_entry = tkinter.Entry(top, textvariable=basic_pension, width=30, font=('calibre', 10, 'normal'))
Calc_Basic_Pension_label = tkinter.Label(top, text='If you have not Calculated your Basic Pension --->',
                                         font=('calibre', 10, 'bold', 'underline'))
Calc_Basic_Pension_btn = tkinter.Button(top, text='Calculate your Basic Pension Here', width=30, bd='4',
                                        command=Redirect_Basic_Pension)
commutation_label = tkinter.Label(top, text='Commutation(Maximum 33%) :', font=('calibre', 10, 'bold'))
commutation_entry = tkinter.Entry(top, textvariable=commutation_var, width=30, font=('calibre', 10, 'normal'))

calCommutation_btn = tkinter.Button(top, text='Calculate my Commutation and Final Pension', width=40, bd='4',
                                    command=calcom)

# placing the label and entry in the required position using place method 
basicpension_label.place(x=120, y=300)
basicpension_entry.place(x=330, y=300)
commutation_label.place(x=120, y=400)
commutation_entry.place(x=330, y=400)
calCommutation_btn.place(x=350, y=450)
Calc_Basic_Pension_btn.place(x=600, y=345)
Calc_Basic_Pension_label.place(x=250, y=350)
top.mainloop()