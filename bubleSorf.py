a = [3,6,7,4,5,0,1,2,8]
for j in range(len(a)):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i] , a[i+1] = a[i+1], a[i]
print(a)
