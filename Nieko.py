from math import sqrt

#https://stackoverflow.com/questions/10927234/setting-the-position-on-a-button-in-python
from tkinter import *
from tkinter import Button

my_window = Tk()
my_window.title  ("Test")
my_window.configure (bg='black')
my_window.geometry("1400x900")

button_plus = Button(my_window,text="+",width = 10)

button_plus.pack()

button_1 = Button(my_window,text="1",width = 10)
#button_1.grid(row=0, column=0)

button_1.pack()

button_2 = Button(my_window,text="2",width = 10)
#button_2.grid(row=1, column=0)

button_2.pack()

button_3 = Button(my_window,text="3",width = 10)

button_3.pack()

button_4 = Button(my_window,text="4",width = 10)

button_4.pack()

button_5 = Button(my_window,text="5",width = 10)

button_5.pack()

button_6 = Button(my_window,text="6",width = 10)

button_6.pack()

button_7 = Button(my_window,text="7",width = 10)

button_7.pack()

button_8 = Button(my_window,text="8",width = 10)

button_8.pack()

button_9 = Button(my_window,text="9",width = 10)

button_9.pack()

button_0 = Button(my_window,text="0",width = 10)

button_0.pack()




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