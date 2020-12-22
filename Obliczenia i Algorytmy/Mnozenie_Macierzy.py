import numpy
import random
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

def iloczyn_macierzy(A,B):
    values = []

    for i in range (64):
        values.append(0)
    matrix = numpy.array(values).reshape(8,8) 

    for k in range (8):
        for g in range (8):

            for i in range (8):
                for j in range (8):
                    matrix[k][g] += A[0][k] * B[i][g]

    return matrix

A = (gen_macierz(8,8))
print (A)
B = (gen_macierz(8,8))
print (B)

print (iloczyn_macierzy(A,B))