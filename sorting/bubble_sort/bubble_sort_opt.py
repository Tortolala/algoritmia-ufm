'''
Optimized bubble sort implementation
'''


def bubble_sort_opt(arr):

    n = len(arr)

    for i in range(n):

        sorted = True

        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False
        
        if sorted:
            return arr
        
    return arr
