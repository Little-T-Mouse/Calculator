from tkinter import *
from selenium import webdriver
import time

def press(num):
    global shown
    shown = shown + str(num)
    equation.set(shown) # Update the equation
    
def equalpress():
    try:
        global shown
        total = str(eval(shown))
        equation.set(total)
        shown = ""
    except:
        if "/0" in shown:
            equation.set("Cannot Divide By Zero")
        else:
            equation.set("Syntax Error")
        shown = ""
        
def back():
    global shown
    if len(shown)>0:
        shown = shown[:-1]
    equation.set(shown)

def hamster():
    global shown
    shown = "•̀ ω •́ ✧"
    equation.set(shown)
    shown = ""
def clear():
    global shown
    shown = ""
    equation.set("")

def off():
    window.destroy()
    
shown = ""
window = Tk()
window.configure(background="white")
window.title("Little Mouse Calculator")
window.geometry("330x330")
equation = StringVar()
expression = Entry(window, textvariable=equation)
expression.grid(columnspan=5, ipadx=70)
button1 = Button(window, text='1', fg='black', bg='gray',
                  height=3, command=lambda: press(1), width=7)
button1.grid(row=3, column=0)
button2 = Button(window, text='2', fg='black', bg='gray',
                  height=3, command=lambda: press(2), width=7)
button2.grid(row=3, column=1)
button3 = Button(window, text='3', fg='black', bg='gray',
                  height=3, command=lambda: press(3), width=7)
button3.grid(row=3, column=2)
button4 = Button(window, text='4', fg='black', bg='gray',
                  height=3, command=lambda: press(4), width=7)
button4.grid(row=4, column=0)
button5 = Button(window, text='5', fg='black', bg='gray',
                  height=3, command=lambda: press(5), width=7)
button5.grid(row=4, column=1)
button6 = Button(window, text='6', fg='black', bg='gray',
                  height=3, command=lambda: press(6), width=7)
button6.grid(row=4, column=2)
button7 = Button(window, text='7', fg='black', bg='gray',
                  height=3, command=lambda: press(7), width=7)
button7.grid(row=5, column=0)
button8 = Button(window, text='8', fg='black', bg='gray',
                  height=3, command=lambda: press(8), width=7)
button8.grid(row=5, column=1)
button9 = Button(window, text='9', fg='black', bg='gray',
                  height=3, command=lambda: press(9), width=7)
button9.grid(row=5, column=2)
button0 = Button(window, text='0', fg='black', bg='gray',
                  height=3, command=lambda: press(0), width=7)
button0.grid(row=6, column=0)
dots = Button(window, text='.', fg='black', bg='gray',
                    command=lambda: press('.'), height=3, width=7)
dots.grid(row=6, column=1)
equal = Button(window, text='=', fg='black', bg='gray',
                    command=equalpress, height=3, width=7)
equal.grid(row=6, column=2)
clear = Button(window, text='clear', fg='black', bg='gray',
                command=clear, height=3, width=7)
clear.grid(row=7, column=0)
off = Button(window, text='OFF', fg='black', bg='gray',
                command=off, height=3, width=7)
off.grid(row=7, column=1)
plus = Button(window, text='+', fg='black', bg='gray',
                command=lambda: press("+"), height=3, width=7)
plus.grid(row=3, column=3)
minus = Button(window, text='-', fg='black', bg='gray',
            command=lambda: press("-"), height=3, width=7)
minus.grid(row=4, column=3)
multiply = Button(window, text='×', fg='black', bg='gray',
                command=lambda: press("*"), height=3, width=7)
multiply.grid(row=5, column=3)
divide = Button(window, text='÷', fg='black', bg='gray',
                command=lambda: press("/"), height=3, width=7)
divide.grid(row=6, column=3)
back = Button(window, text='DEL', fg='black', bg='gray',
                command=back, height=3, width=7)
back.grid(row=7, column=3)
hamster = Button(window, text='\^o^/', fg='black', bg='gray',
                command=hamster, height=3, width=7)
hamster.grid(row=7, column=2)
window.mainloop()
