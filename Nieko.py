from math import sqrt

from tkinter import *


def add_label():
    label_1=Label(my_window, text = "Hello World")
    label_1.pack()
my_window = Tk()
my_window.title  ("Test")
my_window.configure (bg='black')
my_window.geometry("1400x900")

button_1 = Button(my_window,
                  text="Click me",
                  command=add_label)

button_1.pack()

my_window.mainloop()


print('Iveskite simbolį')
s = input()
if (s == '^'):
    print('Ivesk skaičių')
    p = float(input())
    print('Ivesk laipsnį')
    l = float(input())

elif (s == 's'):
    print('Ivesk skaičių')
    p = float(input())

else:
    print('Ivesk pirmą skiačių')
    p = float(input())
    print('Ivesk antra skiačių')
    a = float(input())

if (s == '+'):
    print (p + a)
elif (s == '-'):
    print (p - a)
elif (s == '/'):
    print(p / a)
elif (s == '*'):
    print(p*a)
elif (s == '^'):
    print(pow(p, l))
elif (s == 's'):
    print(sqrt(p))
else:
    print("Neteisingas simbolis")
#Made_by_Erneris