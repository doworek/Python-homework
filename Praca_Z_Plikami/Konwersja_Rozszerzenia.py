import os

dir = "C:\\Users\\User\\Documents\\STUDIA\\IV rok\\Python"

for filename in os.listdir(dir):
    if filename.endswith(".jpg"):
        name = filename.split(".")
        os.rename(filename, name[0] + '.png')