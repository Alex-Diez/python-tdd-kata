# -*- codeing: utf-8 -*-

def chop(elem, array):
    if array:
        low = -1
        high = len(array)
        return _chop(low, high, elem, array)
    return -1

def _chop(low, high, elem, array):
    if high > low:
        index = int((high + low) / 2)
        if elem < array[index]:
            return _chop(low, index - 1, elem, array)
        elif elem > array[index]:
            return _chop(index + 1, high, elem, array)
        else:
            return index
    else:
        return -1

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
