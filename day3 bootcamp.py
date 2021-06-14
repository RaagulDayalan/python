import tkinter
from tkinter import *

window = Tk()

window.title("bootcamp day3")
window.geometry('720x720')
window.configure(background= "Purple")


Firstname = Label(window ,text = "  First Name",bd=1,anchor=W).grid(row = 0,column=0,columnspan=1)
LastName = Label(window ,text = " Last Name",anchor=W).grid(row = 1,column = 0,columnspan=1)
Email = Label(window ,text = " Email Id",anchor=W).grid(row = 2,column = 0,columnspan=1)
Mobile = Label(window ,text = "Contact Number",anchor=E).grid(row = 3,column = 0,columnspan=1)

salary = Label(window ,text = " salary",bd=1,anchor=W).grid(row = 4,column=0,columnspan=1)
fatherName = Label(window ,text = "father's Name",anchor=W).grid(row = 5,column = 0,columnspan=1)
motherName = Label(window ,text = "mother name",anchor=W).grid(row = 6,column = 0,columnspan=1)
altMobile = Label(window ,text = "alternate Number",anchor=E).grid(row = 7,column = 0,columnspan=1)

degree = Label(window ,text = "Degree",anchor=E).grid(row = 8,column = 0,columnspan=1)
rating = Label(window ,text = "rating",anchor=E).grid(row = 9,column = 0,columnspan=1)

firstname1 = Entry(window)
firstname1.grid(row = 0,column = 1)
Lastname1 = Entry(window)
Lastname1.grid(row = 1,column = 1)
Email1 = Entry(window)
Email1.grid(row = 2,column = 1)
Mobile1 = Entry(window)
Mobile1.grid(row = 3,column = 1)

salary1= Entry(window)
salary1.grid(row = 4,column = 1)
fatherName1 = Entry(window)
fatherName1.grid(row = 5,column = 1)
motherName1 = Entry(window)
motherName1.grid(row = 6,column = 1)
altMobile1 = Entry(window)
altMobile1.grid(row = 7,column = 1)
degree1 = Entry(window)
degree1.grid(row = 8,column = 1)
rating1 = Entry(window)
rating1.grid(row = 9,column = 1)



def clicked1():
    # a = e.get
    res = "Welcome "+ firstname1.get()
    qwe = Label(window,text= res,fg='blue',bg='black',borderwidth=8).grid(row= 39,column = 1)
def displayer():
    f1="\n"+firstname1.get()
    f2="\n"+salary1.get()
    f3="\n"+fatherName1.get()
    f4="\n"+motherName1.get()
    f5="\n"+altMobile1.get()
    f6="\n"+Email1.get()
    f7="\n"+Mobile1.get()
    f8="\n"+degree1.get()
    f9="\n"+rating1.get()
    f10="\n"+Lastname1.get()
    frame2 = Tk()
    savedinfo = Label(frame2,text= "saved info \n"+f1+f2+f3+f4+f5+f6+f7+f8+f9+f10)
    savedinfo.grid(row = 13,column = 2,rowspan = 3)
    window.destroy()
    frame2.mainloop()






button2 = Button(window,text="save",command=clicked1).grid(row=13,column=0)

button = Button(window,text="exit",command = window.quit).grid(row = 13,column = 2,rowspan = 3)

btn = Button(window ,text="Submit",command=displayer).grid(row=13,column=1)



window.mainloop()

