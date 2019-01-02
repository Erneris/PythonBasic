print('Iveskite simbolį')
s = input()
if (s == '^'):
    print('Ivesk skaičių')
    p = float(input())
    print('Ivesk laipsnį')
    l = float(input())

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

else:
    print("Neteisingas simbolis")
