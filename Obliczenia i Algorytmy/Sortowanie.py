import cmath
import random
import numpy

random_num = []

for number in range(50):
    random_num.append(random.randint(1,100))

def sortowanie_babelkowe(random_list):
    for i in range(len(random_list)):
        n = len(random_list) - 1
        while n > i:
            if random_list[n] < random_list[n-1]:
                tmp = random_list[n]
                random_list[n] = random_list[n-1]
                random_list[n-1] = tmp    

            n -= 1
            
    random_list.reverse()

    return random_list


def test_sort(random_list, wynik_sortowania):
    random_list.sort(reverse=True)
    if wynik_sortowania == random_list:
        print ("sortowanie sie powiodlo")
    else:
        print ("sortowanie sie nie powiodlo")


test_sort(random_num, sortowanie_babelkowe(random_num))