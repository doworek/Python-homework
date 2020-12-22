import os

dir = "C:\\Users\\User\\Documents\\STUDIA\\IV rok\\Python"

for root, dirnames, filenames in os.walk(dir):
    path = root.split(os.sep)
    print(os.path.basename(root))
    for name in filenames:
        print(name)