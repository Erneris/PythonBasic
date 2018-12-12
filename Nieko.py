

print('Ivesk primą skiačiu')
p = input()
print('Ivesk antra skiačiu')
a = input()
print('Iveskite simboli')
s = input()

if(s == '+'):
      sum = int(p) + int(a)
      print(sum)
elif(s == '-'):
     sum = int(p)- int(a)
     print(sum)
elif(s == '/'):
     sum = int(p) / int(a)
     print(sum)
elif(s == '*'):
     sum = int(p) * int(a)
     print(sum)
else:
    print("Neteisingas simbolis")
