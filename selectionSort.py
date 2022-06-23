#Program to sort an array using selectionSort algorithm

A = [40,19,82,39,50]

def selectionSort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range (i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i],A[min_idx] = A[min_idx],A[i]
    return (A)

print (selectionSort(A))
