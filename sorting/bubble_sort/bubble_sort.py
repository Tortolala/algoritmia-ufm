'''
Simplest bubble sort implementation.
'''


def bubble_sort(arr):

    n = len(arr)

    for _ in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
