import numpy


def wyznacznik_macierzy(A):
    values = []
    for i in range (9):
        values.append(0)
    matrix = numpy.array(values).reshape(3,3)

    wyznacznik = A[0][0] * A [1][1] * A [2][2] + A[0][1] * A [1][2] * A [2][0] + A[0][2] * A [1][0] * A [2][1]
    return wyznacznik


A = (gen_macierz(3,3))
print (A)
print (wyznacznik_macierzy(A))

