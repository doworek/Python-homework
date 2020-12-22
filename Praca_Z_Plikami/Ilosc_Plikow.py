import os

dir = "C:\\Users\\User\\Documents\\STUDIA\\IV rok\\Python"

onlyfiles = next(os.walk(dir))[2]
print ("Liczba plikow: ", len(onlyfiles))