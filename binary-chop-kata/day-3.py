# -*- codeing: utf-8 -*-

def chop(elem, array):
    if not array:
        return -1
    low = -1
    high = len(array)
    i = _next_index(low, high)
    while high > low:
        if array[i] > elem:
            high = i - 1
            i = _next_index(low, high)
        elif array[i] < elem:
            low = i + 1
            i = _next_index(low, high)
        else:
            return i
    return -1

def _next_index(low, high):
    return int((high + low) / 2)

import unittest

class BinaryChopTest(unittest.TestCase):

    def test_chop_empty_list(self):
        self.assertEqual(-1, chop(3, []))

    def test_chop_singleton_list(self):
        self.assertEqual(0, chop(3, [3]))

    def test_chop_singleton_list_without_match(self):
        self.assertEqual(-1, chop(3, [1]))

    def test_three_elements_list(self):
        self.assertEqual(0, chop(1, [1, 3, 5]))
        self.assertEqual(1, chop(3, [1, 3, 5]))
        self.assertEqual(2, chop(5, [1, 3, 5]))
