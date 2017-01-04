# -*- codeing: utf-8 -*-

def chop(elem, array):
    if not array:
        return -1
    high = len(array)
    low = -1
    index = _next_probe_index(low, high)
    while high > low:
        if array[index] > elem:
            high = index - 1
        elif array[index] < elem:
            low = index + 1
        else:
            return index
        index = _next_probe_index(low, high)
    return -1

def _next_probe_index(low, high):
    return int((high + low) / 2)

import unittest

class BinaryChopTest(unittest.TestCase):

    def test_chop_empty_list(self):
        self.assertEqual(-1, chop(3, []))

    def test_chop_singleton_list(self):
        self.assertEqual(0, chop(3, [3]))

    def test_chop_singleton_list_without_match(self):
        self.assertEqual(-1, chop(3, [1]))

    def test_chop_three_elements_list(self):
        self.assertEqual(0, chop(1, [1, 3, 5]))
        self.assertEqual(1, chop(3, [1, 3, 5]))
        self.assertEqual(2, chop(5, [1, 3, 5]))

        self.assertEqual(-1, chop(2, [1, 3, 5]))
