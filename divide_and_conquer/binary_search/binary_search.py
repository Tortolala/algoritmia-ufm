'''
Binary search implementation.
'''


def binary_search(arr, key, left=0, right=None):

    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, left, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, right)


test_arr = [1, 2, 4, 7, 8, 10, 12, 14, 18, 21, 24, 26, 29, 30]
print(binary_search(test_arr, 7))
print(binary_search(test_arr, 42))
print(binary_search(test_arr, 14))
print(binary_search(test_arr, -8))
print(binary_search(test_arr, 15))
print(binary_search(test_arr, 21))
