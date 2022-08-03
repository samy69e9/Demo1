
from tkinter import *

# b1=Button(ab,text="Login",fg="red")
# b1.place(x=100,y=80)

ab=Tk()
var = StringVar()
label = Label( ab, textvariable=var)

var.set("Registration Form")
label.pack()

l1=Label(ab,text="Sr. No")
l1.place(x=30,y=30)
e1 = Entry(ab)
e1.place(x=80,y=30)
l2=Label(ab,text="Name")
l2.place(x=30,y=60)
e2 = Entry(ab)
e2.place(x=80,y=60)
l3=Label(ab,text="Roll No")
l3.place(x=30,y=90)
e3 = Entry(ab)
e3.place(x=80,y=90)
l4=Label(ab,text="Address")
l4.place(x=30,y=120)
e4 = Entry(ab)
e4.place(x=80,y=120)
l5=Label(ab,text="Branch")
l5.place(x=30,y=150)
str=StringVar()
options = [
    "Branch 1",
    "Branch 2",
    "Branch 3"
    ]
branch=OptionMenu(ab,str,options)
branch.place(x=80,y=150)
l6=Label(ab,text="Gender")
l6.place(x=30,y=180)
b1=Button(ab,text="Submit Form",fg="red")
ab.mainloop()