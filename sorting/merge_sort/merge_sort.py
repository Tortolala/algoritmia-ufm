'''
Merge sort implementation.
'''

import math


def merge(left_arr, right_arr):
    
    merged = []
    i, j = 0, 0

    # Sentinels
    left_arr.append(math.inf)
    right_arr.append(math.inf)

    # Merges lists into one
    while (left_arr[i] != math.inf) or (right_arr[j] != math.inf):
        if left_arr[i] < right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1

    left_arr.pop()
    right_arr.pop()

    return merged


def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
