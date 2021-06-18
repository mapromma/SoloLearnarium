import random

# a = [3,6,7,4,5,0,1,2,8]
try:
    array_size = int(input('Укажите размерность массива '))
except:
    array_size = False

if array_size:
    a = []
    for i in range(array_size):
        a.append(random.randint(0, 10_000))
    for j in range(len(a)):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                t = a[i]
                a[i] = a[i+1]
                a[i+1] = t
    print(a)
