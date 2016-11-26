# -*- codeing: utf-8 -*-

def bubble_sort(to_sort):
    for i in range(len(to_sort)):
        j = i
        while j > 0:
            if to_sort[j - 1] > to_sort[j]:
                temp = to_sort[j - 1]
                to_sort[j - 1] = to_sort[j]
                to_sort[j] = temp
            j -= 1
    return to_sort

def quick_sort(to_sort):
    result = []
    if to_sort:
        eq = to_sort[0]
        lt, gt = _split_by(to_sort, eq)

        result.extend(quick_sort(lt))
        result.append(eq)
        result.extend(quick_sort(gt))

    return result

def _split_by(array, elem):
    lt = []
    gt = []
    for e in array:
        if e > elem:
            gt.append(e)
        if e < elem:
            lt.append(e)
    return (lt, gt)

import unittest

class BubbleSortTest(unittest.TestCase):

    def test_sorts_an_empty_list(self):
        self.assertEqual([], bubble_sort([]))

    def test_sorts_a_single_element_list(self):
        self.assertEqual([1], bubble_sort([1]))

    def test_sorts_a_sorted_two_elements_list(self):
        self.assertEqual([1, 2], bubble_sort([1, 2]))

    def test_sorts_an_unsorted_two_elements_list(self):
        self.assertEqual([1, 2], bubble_sort([2, 1]))

    def test_sorts_a_sorted_three_elements_list(self):
        self.assertEqual([1, 2, 3], bubble_sort([1, 2, 3]))

    def test_sorts_2_1_3_list(self):
        self.assertEqual([1, 2, 3], bubble_sort([2, 1, 3]))

    def test_sorts_3_1_2_list(self):
        self.assertEqual([1, 2, 3], bubble_sort([3, 1, 2]))

    def test_sorts_3_2_1_list(self):
        self.assertEqual([1, 2, 3], bubble_sort([3, 2, 1]))

class QuickSortTest(unittest.TestCase):

    def test_sorts_an_empty_list(self):
        self.assertEqual([], quick_sort([]))

    def test_sorts_a_single_element_list(self):
        self.assertEqual([1], quick_sort([1]))

    def test_sorts_a_sorted_two_elements_list(self):
        self.assertEqual([1, 2], quick_sort([1, 2]))

    def test_sorts_an_unsorted_two_elements_list(self):
        self.assertEqual([1, 2], quick_sort([2, 1]))

    def test_sorts_a_sorted_three_elements_list(self):
        self.assertEqual([1, 2, 3], quick_sort([1, 2, 3]))

    def test_sorts_2_1_3_list(self):
        self.assertEqual([1, 2, 3], quick_sort([2, 1, 3]))

    def test_sorts_1_3_2_list(self):
        self.assertEqual([1, 2, 3], quick_sort([1, 3, 2]))

    def test_sorts_3_2_1_list(self):
        self.assertEqual([1, 2, 3], quick_sort([3, 2, 1]))
