from math import sqrt

#https://stackoverflow.com/questions/10927234/setting-the-position-on-a-button-in-python
from tkinter import *
from tkinter import Button

my_window = Tk()
my_window.title  ("Test")
my_window.configure (bg='black')
my_window.geometry("400x400")

#Label().grid(row=0)

#e1 = Entry()

#e1.grid(row=0, column=1)

button_plus = Button(my_window,text="+",width = 10,height  = 4).grid(row = 4, column = 1)

button_minus = Button(my_window,text="-",width = 10,height  = 4).grid(row = 4, column = 3)

button_multiply = Button(my_window,text="*",width = 10,height  = 4).grid(row = 1, column = 4)

button_divide = Button(my_window,text="/",width = 10,height  = 4).grid(row = 2, column = 4)

button_powerof = Button(my_window,text="x^y",width = 10,height  = 4).grid(row = 3, column = 4)

button_rootof = Button(my_window,text="√",width = 10,height  = 4).grid(row = 4, column = 4)

button_1 = Button(my_window,text="1",width = 10,height  = 4).grid(row = 1, column = 1)

button_2 = Button(my_window,text="2",width = 10,height  = 4).grid(row = 1, column = 2)

button_3 = Button(my_window,text="3",width = 10,height  = 4).grid(row = 1, column = 3)

button_4 = Button(my_window,text="4",width = 10,height  = 4).grid(row = 2, column = 1)

button_5 = Button(my_window,text="5",width = 10,height  = 4).grid(row = 2, column = 2)

button_6 = Button(my_window,text="6",width = 10,height  = 4).grid(row = 2, column = 3)

button_7 = Button(my_window,text="7",width = 10,height  = 4).grid(row = 3, column = 1)

button_8 = Button(my_window,text="8",width = 10,height  = 4).grid(row = 3, column = 2)

button_9 = Button(my_window,text="9",width = 10,height  = 4).grid(row = 3, column = 3)

button_0 = Button(my_window,text="0",width = 10,height  = 4).grid(row = 4, column = 2)





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