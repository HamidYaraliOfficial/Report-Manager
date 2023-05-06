from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from db import DBConnect
from listComp import ListComp

# تنظیمات
conn = DBConnect()
root = Tk()
root.geometry('530x285')
root.title('مدیریت شکایات')
root.configure(background='#E0FFFF')

# استایل
style = Style()
style.theme_use('classic')
for elem in ['TLabel', 'TButton', 'TRadioutton']:
    style.configure(elem, background='#AEB6BF')

# شبکه گرید
labels = [':نام و نام خانوادگی', ':جنسیت', ':نظر']
for i in range(3):
    Label(root, text=labels[i]).grid(row=i, column=14, padx=10, pady=10, sticky=E)

BuList = Button(root, text='لیست شکایات')
BuList.grid(row=4, column=2)
BuSubmit = Button(root, text='ارسال شکایت')
BuSubmit.grid(row=4, column=3)

# ورودی ها
fullname = Entry(root, width=30, font=('Arial', 14))
fullname.grid(row=0, column=2, columnspan=2)
SpanGender = StringVar()
Radiobutton(root, text='مرد', value='male', variable=SpanGender).grid(row=1, column=2)
Radiobutton(root, text='زن', value='female', variable=SpanGender).grid(row=1, column=3)
comment = Text(root, width=35, height=5, font=('Arial', 14))
comment.grid(row=2, column=2, columnspan=2, padx=10, pady=10)


def SaveData():
    msg = conn.Add(fullname.get(), SpanGender.get(), comment.get(1.0, 'end'))
    fullname.delete(0, 'end')
    comment.delete(1.0, 'end')
    showinfo(title='اضافه کردن اطلاعات', message=msg)


def ShowList():
    listrequest = ListComp()


BuSubmit.config(command=SaveData)
BuList.config(command=ShowList)

root.mainloop()