from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Calculator")
win.configure(bg='#313866')

style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', background='#83B8FF', foreground='white', font=('Georgia', 12, 'bold'))
style.map('TButton', background=[('active', '#248BD6')], foreground=[('active', '#313866')])
style.configure('TEntry', fieldbackground='#OF6BAE', foreground='black', font=('Georgia', 12))
style.configure('TLabel', background='#313866', foreground='#C6CDFF', font=('Georgia', 12))

def add():
    result.config(text=(float(firstNum.get()) + float(secondNum.get())))
def subtract():
    result.config(text=(float(firstNum.get()) - float(secondNum.get())))
def multiply():
    result.config(text=(float(firstNum.get()) * float(secondNum.get())))
def divide():
    result.config(text=(float(firstNum.get()) / float(secondNum.get())))
def floor():
    result.config(text=(float(firstNum.get()) // float(secondNum.get())))
def exponent():
    result.config(text=(float(firstNum.get()) ** float(secondNum.get())))
def modulos():
    result.config(text=(float(firstNum.get()) % float(secondNum.get())))

title = Label(win, text="Python GUI: Basic Calculator v1", font=("Georgia", 16), bg='#313866', fg='#C6CDFF').place(x=200, y=30)
firstTxt = ttk.Label(win, text="First Number:")
firstTxt.place(x=120, y=75)
firstNum = ttk.Entry(win, width=25)
firstNum.place(x=300, y=80)
secondTxt = ttk.Label(win, text="Second Number:")
secondTxt.place(x=120, y=115)
secondNum = ttk.Entry(win, width=25)
secondNum.place(x=300, y=120)
resultTxt = ttk.Label(win, text="Result:")
resultTxt.place(x=560, y=70)
result = ttk.Label(win, text="00", background='#248BD6', foreground='white', font=('Georgia', 12, 'bold'))
result.place(x=560, y=100)

addBtn = ttk.Button(win, width=3, text="+", command=add).place(x=160, y=170)
subBtn = ttk.Button(win, width=3, text="-", command=subtract).place(x=225, y=170)
multiplyBtn = ttk.Button(win, width=3, text="x", command=multiply).place(x=290, y=170)
divideBtn = ttk.Button(win, width=3, text="÷", command=divide).place(x=355, y=170)
floorBtn = ttk.Button(win, width=3, text="//", command=floor).place(x=420, y=170)
expoBtn = ttk.Button(win, width=3, text="^", command=exponent).place(x=485, y=170)
modulosBtn = ttk.Button(win, width=3, text="%", command=modulos).place(x=550, y=170)
win.geometry("800x300+600+300")
win.mainloop()
