import cmath
from Liczby_Zespolone import Complex

a1 = int(input('podaj real1  '))
b1 = int(input('podaj imag1  '))
u = Complex(a1,b1)
print(u)

a2 = int(input('podaj real2  '))
b2 = int(input('podaj imag2  '))
v = Complex(a2,b2)
print(v)

dzialanie = input('dzialanie  ')

if dzialanie == '+':
    print (u + v)
elif dzialanie == '-':
    print (u - v)
elif dzialanie == '*':
    print (u * v)
else: print ('error: nie ma takiego dzialania')