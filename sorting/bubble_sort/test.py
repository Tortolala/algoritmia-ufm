'''
Unit testing for bubble sort.
'''


import unittest
from bubble_sort import bubble_sort
from bubble_sort_opt import bubble_sort_opt


class TestBubbleSort(unittest.TestCase):
    
    def test_base_empty_array(self):
        self.assertEqual(bubble_sort([]), [])

    def test_base_single_element_array(self):
        self.assertEqual(bubble_sort([1]), [1])

    def test_base_sorted_array(self):
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])

    def test_base_unsorted_array(self):
        self.assertEqual(bubble_sort([4, 3, 7, 1, 2, 9, 6]), [1, 2, 3, 4, 6, 7, 9])

    def test_base_array_with_duplicates(self):
        self.assertEqual(bubble_sort([4, 3, 7, 1, 3, 7, 9]), [1, 3, 3, 4, 7, 7, 9])
    
    def test_base_array_with_negatives(self):
        self.assertEqual(bubble_sort([4, 3, -7, -1, 2, 9, 6]), [-7, -1, 2, 3, 4, 6, 9])

    def test_opt_empty_array(self):
        self.assertEqual(bubble_sort_opt([]), [])

    def test_opt_single_element_array(self):
        self.assertEqual(bubble_sort_opt([1]), [1])

    def test_opt_sorted_array(self):
        self.assertEqual(bubble_sort_opt([1, 2, 3]), [1, 2, 3])

    def test_opt_unsorted_array(self):
        self.assertEqual(bubble_sort_opt([4, 3, 7, 1, 2, 9, 6]), [1, 2, 3, 4, 6, 7, 9])

    def test_opt_array_with_duplicates(self):
        self.assertEqual(bubble_sort_opt([4, 3, 7, 1, 3, 7, 9]), [1, 3, 3, 4, 7, 7, 9])
    
    def test_opt_array_with_negatives(self):
        self.assertEqual(bubble_sort_opt([4, 3, -7, -1, 2, 9, 6]), [-7, -1, 2, 3, 4, 6, 9])


if __name__ == '__main__':
    unittest.main()
