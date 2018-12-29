print('Iveskite simboli')
s = input()
if(s == '*2'):
    print('Ivesk skaičiu')
    p = input()
elif (s == '*3'):
    print('Ivesk skaičiu')
    p = input()
else:
    print('Ivesk pirmą skiačiu')
    p = input()
    print('Ivesk antra skiačiu')
    a = input()

if(s == '+'):
      sum = int(p) + int(a)
      print(sum)
elif(s == '-'):
     sum = int(p) - int(a)
     print(sum)
elif(s == '/'):
     sum = int(p) / int(a)
     print(sum)
elif(s == '*'):
     sum = int(p) * int(a)
     print(sum)
elif(s == '*2'):
     sum = int(p) * int(p)
     print(sum)
elif (s == '*3'):
     sum = int(p) * int(p) * int(p)
     print(sum)
else:
    print("Neteisingas simbolis")
