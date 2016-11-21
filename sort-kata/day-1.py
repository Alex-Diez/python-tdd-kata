# -*- codeing: utf-8 -*-

def bubble_sort(to_sort):
    index = 0
    while index < len(to_sort):
        offset = index
        while offset > 0 and to_sort[offset - 1] > to_sort[offset]:
            temp = to_sort[offset]
            to_sort[offset] = to_sort[offset - 1]
            to_sort[offset - 1] = temp
            offset -= 1
        index += 1
    return to_sort

def quick_sort(to_sort):
    result = []
    if to_sort:
        eq = to_sort[0]
        lt, gt = _split_by(to_sort, eq)
        for e in quick_sort(lt):
            result.append(e)
        result.append(eq)
        for e in quick_sort(gt):
            result.append(e)
    return result

def _split_by(to_sort, eq):
    lt = []
    gt = []
    for e in to_sort[1:]:
        if e < eq:
            lt.append(e)
        if e > eq:
            gt.append(e)
    return (lt, gt)

import unittest

class BubbleSortTest(unittest.TestCase):

    def test_sorts_empty_list(self):
        self.assertEqual([], bubble_sort([]))

    def test_sorts_single_element_list(self):
        self.assertEqual([1], bubble_sort([1]))

    def test_sorts_two_elements_sorted_list(self):
        self.assertEqual([1, 2], bubble_sort([1, 2]))

    def test_sorts_two_elements_unsorted_list(self):
        self.assertEqual([1, 2], bubble_sort([2, 1]))

    def test_sorts_three_elements_sorted_list(self):
        self.assertEqual([1, 2, 3], bubble_sort([1, 2, 3]))

    def test_sorts_2_1_3_list(self):
        self.assertEqual([1, 2, 3], bubble_sort([2, 1, 3]))

    def test_sorts_1_3_2_list(self):
        self.assertEqual([1, 2, 3], bubble_sort([1, 3, 2]))

    def test_sorts_3_2_1_list(self):
        self.assertEqual([1, 2, 3], bubble_sort([3, 2, 1]))

class QuickSortTest(unittest.TestCase):

    def test_sorts_an_empty_list(self):
        self.assertEqual([], quick_sort([]))

    def test_sorts_single_element_list(self):
        self.assertEqual([1], quick_sort([1]))

    def test_sorts_two_elements_sorted_list(self):
        self.assertEqual([1, 2], quick_sort([1, 2]))

    def test_sorts_two_elements_unsorted_list(self):
        self.assertEqual([1, 2], quick_sort([2, 1]))

    def test_sorts_three_elements_sorted_list(self):
        self.assertEqual([1, 2, 3], quick_sort([1, 2, 3]))

    def test_sorts_2_1_3_list(self):
        self.assertEqual([1, 2, 3], quick_sort([2, 1, 3]))

    def test_sorts_1_3_2_list(self):
        self.assertEqual([1, 2, 3], quick_sort([1, 3, 2]))

    def test_sorts_3_2_1_list(self):
        self.assertEqual([1, 2, 3], quick_sort([3, 2, 1]))
