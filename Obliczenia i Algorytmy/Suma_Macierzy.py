import random
import numpy
from datetime import datetime

def losuj(ile, zakres):
    random_num = []
    random.seed(datetime.now())
    for i in range(ile):
        num = random.randint(0, zakres)
        random_num.append(num)
    return random_num

def gen_macierz(rows, columns):
    values = losuj(rows * columns, 9)
    matrix = numpy.array(values).reshape(rows, columns) 
    return matrix

def suma_macierzy(A, B, rows, columns):
    values = []
    for i in range (rows * columns):
        values.append(0)
    matrix = numpy.array(values).reshape(rows, columns) 

    for i in range (rows):
        for j in range (columns):
            matrix[i][j] = A[i][j] + B[i][j]

    return matrix

A = (gen_macierz(2,3))
print (A)
B = (gen_macierz(2,3))
print (B)
print (suma_macierzy(A,B,2,3))

