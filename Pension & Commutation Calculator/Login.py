#importing tkinter module
import mysql.connector as sql
from tkinter import messagebox
from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image

import os

#giving basic characteristics and geomertry to the window
win = Tk()
Myfont=font.Font(family="Helvetica", size=16)

win.geometry("1000x700")
image = Image.open('LoginImage.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(win, image = photo_image)
label.pack()
win.title("Pension And Commutation Calculator -- Login")

#function for login
def login():
    db = sql.connect(host="localhost", user="root", passwd="Password@123")

    cur = db.cursor()

    try:

        cur.execute("create database loginbase")

        db = sql.connect(host="localhost", user="root", passwd="Password@123", database="loginbase")

        cur = db.cursor()


    except sql.errors.DatabaseError:

        db = sql.connect(host="localhost", user="root", passwd="Password@123", database="loginbase")

        cur = db.cursor()

        try:

            cur.execute("create table main(username varchar(50), NOT NULL, password int NOT NULL)")


        except sql.errors.ProgrammingError:

            pass


    finally:

        try:

            cur.execute("create table main(username varchar(50) NOT NULL, "  "password int NOT NULL)")


        except sql.errors.ProgrammingError:

            pass

    while True:

        user = user1.get()

        passwd = passwd1.get()

        cur.execute("select * from main where username = '%s' and password = %s" % (user, passwd))

        rud = cur.fetchall()

        if rud:

            messagebox.showinfo("Status", "Welcome back")
            os.system('python choosing_window.py')

            break


        else:

            messagebox.showinfo("Status", "No account found, Please create an account")

            break

    cur.close()

    db.close()


def ok():
    os.system( 'python SignUp.py')


#defining geometry and basic characteristics for the entry fields and buttons.
userlvl = Label(win, text="Username :")
passwdlvl = Label(win, text="PIN  :")
user1 = Entry(win, textvariable=StringVar(),width=25)
passwd1 = Entry(win, textvariable=IntVar().set(""),width= 25)
enter = Button(win, text="Login",width= 9,command=lambda: login(), bd=0)
enter.configure(bg="black",fg= "white")

#using place funtion to place the items in correct place.
user1.place(x=320, y=450)
passwd1.place(x=320, y=490)
userlvl.place(x=230, y=450)
passwdlvl.place(x=230, y=490)
enter.place(x=450, y=540)
button = Button(win, text="Sign UP",width=7, bg="green", fg="white", command=ok).place(x=350, y=570)

win.mainloop()
