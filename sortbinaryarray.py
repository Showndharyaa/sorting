#program to sort a binary array

def sortBinaryArray(a,n):
    j = -1
    for i in range(n):
        if a[i] < 1:
            j = j+1
            a[i],a[j] = a[j],a[i]

a = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0]
n = len(a)

sortBinaryArray(a, n)

for i in range(n):
    print (a[i],end=' ')
