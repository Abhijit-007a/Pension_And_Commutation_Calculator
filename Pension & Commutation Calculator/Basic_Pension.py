# importing tkinter module.
import tkinter 
from tkinter import ttk 
from PIL import ImageTk,Image
from tkinter import messagebox #for pop-up window
import mysql.connector as sql #to connect to MySQL server


import os
top = tkinter.Tk()

#Give basic characteristics and geometry to the window.
top.geometry("1000x600")
image = Image.open('Basic_PensionImage.png')
photo_image = ImageTk.PhotoImage(image)
label = tkinter.Label(top, image = photo_image)
label.pack()
top.title(" - Pension and Commutation Calculator - ")

db = sql.connect(host="localhost", user="root", passwd="Password@123")

cur = db.cursor()




#declaring the variables required for storing and calculating the values.
name_var=tkinter.StringVar() 
year_var=tkinter.IntVar()
year_var=tkinter.IntVar()
one_var=tkinter.IntVar()
ten_var=tkinter.IntVar()
commutation_var=tkinter.IntVar()
basic_pension= tkinter.IntVar()
reduced_pension= tkinter.IntVar()
totalcommutation_var= tkinter.IntVar()

# creating a label for title using widget Label
personal_label = tkinter.Label(top, text = 'Personal Information :                                          ',font=('calibre', 10, 'bold','underline')) 

# creating a label and entry for name using widget Label and Entry rspt.
name_label = tkinter.Label(top, text = 'Name :',font=('calibre', 10, 'bold'))    
name_entry = tkinter.Entry(top, textvariable = name_var,width= 30, font=('calibre',10,'normal')) 

# creating a label for name using widget Label
TypeofRetirement_label = tkinter.Label(top, text = 'Type of Retirement :',font=('calibre', 10, 'bold'))    
n = tkinter.StringVar() 
TypeofRetirement = ttk.Combobox(top, width = 32, textvariable = n)   
# Adding combobox drop down list 
TypeofRetirement['value'] = (' Superannuation', ' Volutary') 
TypeofRetirement.current(1)  

# creating a label for name using widget Label .
DateofBirth_label = tkinter.Label(top, text = 'Date of Birth :',font=('calibre', 10, 'bold'))    
d = tkinter.StringVar() 
m = tkinter.StringVar() 
y = tkinter.StringVar() 
Date = ttk.Combobox(top, width = 5, textvariable = d)   
# Adding combobox drop down list 
Date['value'] = ('Date','1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
               '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
          '21','22', '23', '24', '25', '26', '27', '28', '29', '30', '31') 
Date.current(0)
Month = ttk.Combobox(top, width = 10, textvariable = m,)   
# Adding combobox drop down list 
Month['value'] = ('Month','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December') 
Month.current(0)
Year = ttk.Combobox(top, width = 7, textvariable = y)   
# Adding combobox drop down list 
Year['value'] = ('Year','2020','2019','2018','2017','2016','2015','2014','2013','2012','2011','2010',
                        '2009','2008','2007','2006','2005','2004','2003','2002','2001','2000','1999',
                        '1998','1997','1996','1995','1994','1993','1992','1991','1990','1989','1988',
                        '1987','1986','1985','1984','1983','1982','1981','1980','1979','1978','1977',
                        '1976','1975','1974','1973','1972','1971','1970','1969','1968','1967','1966',
                        '1965','1964','1963','1962','1961','1960','1959','1958','1957','1956','1955',
                        '1954','1953','1952','1951','1950','1949','1948','1947','1946','1945','1944',
                        '1943','1942','1941','1940') 
Year.current(0)

# creating a label for name using widget Label 
DateofRetirement_label = tkinter.Label(top, text = 'Date of Retirement :',font=('calibre', 10, 'bold'))    
rd = tkinter.StringVar() 
rm = tkinter.StringVar() 
ry = tkinter.StringVar() 
rDate = ttk.Combobox(top, width = 5, textvariable = rd)   
# Adding combobox drop down list 
rDate['value'] = ('Date','1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
               '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
          '21','22', '23', '24', '25', '26', '27', '28', '29', '30', '31') 
rDate.current(0)
rMonth = ttk.Combobox(top, width = 10, textvariable = rm,)   
# Adding combobox drop down list 
rMonth['value'] = ('Month','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December') 
rMonth.current(0)
rYear = ttk.Combobox(top, width = 7, textvariable = ry)   
# Adding combobox drop down list 
rYear['value'] = ('Year','2020','2019','2018','2017','2016','2015','2014','2013','2012','2011','2010',
                         '2009','2008','2007','2006','2005','2004','2003','2002','2001','2000','1999',
                         '1998','1997','1996','1995','1994','1993','1992','1991','1990','1989','1988',
                         '1987','1986','1985','1984','1983','1982','1981','1980','1979','1978','1977',
                         '1976','1975','1974','1973','1972','1971','1970','1969','1968','1967','1966',
                         '1965','1964','1963','1962','1961','1960','1959','1958','1957','1956','1955',
                         '1954','1953','1952','1951','1950','1949','1948','1947','1946','1945','1944',
                         '1943','1942','1941','1940')  
rYear.current(0)

# creating a label and entry for name using widget Label and Entry rspt.
input_label = tkinter.Label(top, text = ' Input to calculate pension :                                 ',font=('calibre', 10, 'bold','underline')) 
TotalQualifyingService_label = tkinter.Label(top, text = 'Total Qualifying Service(in year) :',font=('calibre', 10, 'bold'))    
TotalQualifyingServicemonth_entry = tkinter.Entry(top,textvariable = year_var,width= 30, font=('calibre',10,'normal'))

# creating a label and entry for name using widget Label and Entry rspt.
explanation_one ='''Sum of Last 10 
months Emoluments
(Basic Pay (including Grade Pay)+ NPA)
(in Rs.) :''' 
tenmonthsEmoluments_label = tkinter.Label(top, text = explanation_one ,font=('calibre', 10, 'bold'))  
tenmonthsEmoluments_entry = tkinter.Entry(top,textvariable = ten_var,width=30, font=('calibre',10,'normal'))

# creating a label and entry for name using widget Label and Entry rspt.
explanation_two ='''Sum of Last 
month Emoluments
(Basic Pay (including Grade Pay)+ NPA)
(in Rs.) :''' 
onemonthEmoluments_label = tkinter.Label(top, text = explanation_two ,font=('calibre', 10, 'bold'))    
onemonthEmoluments_entry = tkinter.Entry(top,textvariable = one_var,width=30, font=('calibre',10,'normal'))

# Create a Button
def store(result):
    db = sql.connect(host="localhost", user="root", passwd="Password@123")

    cur = db.cursor()

    try:

        cur.execute("create database storingres")

        db = sql.connect(host="localhost", user="root", passwd="Password@123", database="storingres")

        cur = db.cursor()


    except sql.errors.DatabaseError:

        db = sql.connect(host="localhost", user="root", passwd="Password@123", database="storingres")

        cur = db.cursor()

        try:

            cur.execute("create table main(basicpen  int )")


        except sql.errors.ProgrammingError:

            pass


    finally:

        try:

            cur.execute("create table main(basicpen int )")


        except sql.errors.ProgrammingError:

            pass

    while True:
        result

        cur.execute("insert into main values({})".format(int(result)))

        db.commit()
        messagebox.showinfo("Status", "your data is stored in database successfully")
        break

    cur.close()

    db.close()
def CalcBasicPension():

    temp1 =one_var.get()
    temp2 = year_var.get()
    basic_pension=(temp1*temp2)/7

    messagebox.showinfo("Your Basic Pension is ",basic_pension)
    store(basic_pension)
checkbtn = tkinter.Button(top, text = 'Check my Basic pension',width= 30, bd = '4', command = CalcBasicPension)


def commutation_Calc_redirect():
    os.system('python Commutation.py')
nextbtn = tkinter.Button(top, text = 'Check Your Commutation Now!',width= 30, bd = '4', command = commutation_Calc_redirect) 


Quitbtn = tkinter.Button(top, text = 'Quit',width= 15, bd = '4', command = quit) 


# placing the label and entry in the required position using place method 

personal_label.place(x=60 ,y=85 )
name_label.place(x=100, y=125) 
name_entry.place(x=250, y=125)
DateofBirth_label.place(x=100, y=170)  
Date.place(x=250, y=170)
Month.place(x=310, y=170)
Year.place(x=400, y=170)
TypeofRetirement_label.place(x=500, y=125) 
TypeofRetirement.place(x=680, y=125)  
DateofRetirement_label.place(x=500, y=170)
rDate.place(x=680, y=170)
rMonth.place(x=740, y=170)
rYear.place(x=830, y=170)
input_label.place(x=60,y=220)
TotalQualifyingService_label.place(x=100, y=295)
TotalQualifyingServicemonth_entry.place(x=390, y=295)
tenmonthsEmoluments_label.place(x=100, y=350)
tenmonthsEmoluments_entry.place(x=390, y=365)
onemonthEmoluments_label.place(x=100, y=435)
onemonthEmoluments_entry.place(x=392, y=450)
Quitbtn.place(x=800, y=50)
checkbtn.place(x=250, y=530)
nextbtn.place(x=500,y=530)

top.mainloop()