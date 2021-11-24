import os
import tkinter
from tkinter import *
from tkinter import font
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import ttk
from ttkthemes import themed_tk as tk
from PIL import ImageTk,Image

t=tk.ThemedTk(theme='equilux')
t.geometry("750x400")
t.title("Employee Registration")
if "nt" == os.name:
    t.wm_iconbitmap(bitmap = "tie.ico")
else:
    t.wm_iconbitmap(bitmap = "@tie.xbm")

p=Image.open("bg.jpg")
p=p.resize((750,400))
p=ImageTk.PhotoImage(p)
pic=tkinter.Label(image=p)
pic.place(x=0,y=0)


name=Label(text='Name ',font=('bold',10),relief=RIDGE)
name.place(x=20,y=30)
e_nm=Entry()
e_nm.place(x=150,y=30)

age=Label(text='Age ',font=('bold',10),relief=RIDGE)
age.place(x=400,y=30)
e_age=Entry()
e_age.place(x=500,y=30)

doj=Label(text='D.O.J ',font=('bold',10),relief=RIDGE)
doj.place(x=20,y=70)
e_doj=Entry()
e_doj.place(x=150,y=70)

email=Label(text='Email ',font=('bold',10),relief=RIDGE)
email.place(x=400,y=70)
e_em=Entry()
e_em.place(x=500,y=70)

phone=Label(text='Phone ',font=('bold',10),relief=RIDGE)
phone.place(x=20,y=110)
e_ph=Entry()
e_ph.place(x=150,y=110)

genderlist=[
    "",
    "Male",
    "Female",
    "Others",
]
gender=Label(text="Gender",font=('bold',10),relief=RIDGE)
gender.place(x=400,y=110)
e_gr=ttk.Combobox(value=genderlist,width=19,height=7,state='readonly')
e_gr.place(x=500,y=105)

address=Label(text='Address ',font=('bold',10),relief=RIDGE)
address.place(x=20,y=150)
e_ad=Text()
e_ad.place(x=150,y=150,width=510,height=140)


def insert():
    name=e_nm.get()
    age=e_age.get()
    doj=e_doj.get()
    email=e_em.get()
    phone=e_ph.get()
    gender=e_gr.get()
    address=e_ad.get("1.0",'end-1c')

    if (id=="" or name=="" or phone=="" or gender==""):
        MessageBox.showinfo('Insert Status','All fields are required')
    else:
        x=mysql.connect(host='localhost',user='root',password='',db='employees')
        cur=x.cursor()
        cur.execute("insert into employees values('"+ name +"','"+ age +"','"+ doj +"','"+ email +"','"+ phone +"','"+ gender +"','"+ address +"')")
        cur.execute("commit")

        e_nm.delete(0,'end')
        e_age.delete(0,'end')
        e_doj.delete(0,'end')
        e_em.delete(0,'end')
        e_ph.delete(0,'end')
        e_gr.delete(0,'end')
        e_ad.delete("1.0",'end')
        MessageBox.showinfo('Insert Status','Inserted Successfully')
        x.close()

Button(text='Submit',command=insert,fg="white",bg="#097969", bd=0).place(x=320,y=320)

t.mainloop()