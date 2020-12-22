import cmath

a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

def iloczyn_skalarny(a,b):
    wynik = 0
    for i in range (len(a)):
        wynik += a[i] * b[i]
    return wynik

print (iloczyn_skalarny(a,b))
