'''
Unit testing for merge sort.
'''


import unittest
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    
    def test_empty_array(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_sorted_array(self):
        self.assertEqual(merge_sort([1, 2, 3]), [1, 2, 3])

    def test_unsorted_array(self):
        self.assertEqual(merge_sort([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8])

    def test_array_with_duplicates(self):
        self.assertEqual(merge_sort([5, 5, 5, 1, 1, 1]), [1, 1, 1, 5, 5, 5])
    
    def test_array_with_negatives(self):
        self.assertEqual(merge_sort([5, -10, 5, -1, 1, 1]), [-10, -1, 1, 1, 5, 5])
    
    def test_array_with_floats(self):
        self.assertEqual(merge_sort([3.8, 1.0, -5.5]), [-5.5, 1.0, 3.8])


if __name__ == '__main__':
    unittest.main()
