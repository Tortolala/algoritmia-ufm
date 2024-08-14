'''
Counting sort implementation.
'''


def counting_sort(arr):

    if not arr: 
        return []

    n = len(arr)
    k = max(arr) + 1 
    C = [0] * k # Creates new aux array C
   
    for i in range(n): # Counts values in A
        C[arr[i]] += 1

    for i in range(1, k): # Transforms C
        C[i] = C[i] + C[i - 1] 

    B = [None] * len(arr)

    for i in range(n-1, -1, -1): # Sorts values into new array B
        C[arr[i]] -= 1
        B[C[arr[i]]] = arr[i]
    
    return B
