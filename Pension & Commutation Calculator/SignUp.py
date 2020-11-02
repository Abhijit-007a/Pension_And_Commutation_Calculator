#importing all the tkinter modules.
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as sql

win = Tk()
#defining basic geometry and characteristics of the window.
win.geometry("1000x700")
image = Image.open('SignUpImage.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(win, image = photo_image)
label.pack()
#defining the title of the window
win.title("Pension And Commutation Calculator -- SignUp")

#function login that checks the criteria, username and password with the database.
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

            cur.execute("create table main(username varchar(50) NOT NULL, "

                        "password int NOT NULL)")


        except sql.errors.ProgrammingError:

            pass

    while True:

        user = user1.get()

        passwd = passwd1.get()

        cur.execute("insert into main values('{}', {})".format(str(user), passwd))

        db.commit()
        messagebox.showinfo("Status", "Account created! Now Please Login")
        break


    cur.close()

    db.close()

#setting the lable and entry box characteristics.
userlvl = Label(win, text="Username :")
passwdlvl = Label(win, text="PIN  :")
user1 = Entry(win, textvariable=StringVar(),width=25)
passwd1 = Entry(win, textvariable=IntVar().set(""),width= 25)
enter = Button(win, text="SignUp",width= 9,command=lambda: login(), bd=0)
enter.configure(bg="black",fg= "white")

#using place function to put the lable and entry into right places.
user1.place(x=750, y=450)
passwd1.place(x=750, y=490)
userlvl.place(x=650, y=450)
passwdlvl.place(x=650, y=490)
enter.place(x=890, y=540)

win.mainloop()