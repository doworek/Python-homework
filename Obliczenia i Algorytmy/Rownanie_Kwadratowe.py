import cmath
import random
from datetime import datetime
import numpy

def pierwiastki(a,b,c):

    delta = b**2 - 4*a*c

    pierwiastek1 = (-b + cmath.sqrt(delta))/ 2*a
    pierwiastek2 = (-b - cmath.sqrt(delta))/ 2*a

    return pierwiastek1, pierwiastek2

wynik1 = pierwiastki(1,4,3)
wynik2 = pierwiastki(1,2,5)

print (wynik1)
print (wynik2)