
#Sort an array that contains only 0,1,2s

def arrSort(a,n):
  for i in range(n-1):
      for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
  return a

a = [1,0,2,0,2,1,1,2,0]
n = len(a)
print(arrSort(a,n))
