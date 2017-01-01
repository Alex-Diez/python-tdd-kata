# -*- codeing: utf-8 -*-

def chop(elem, array):
    if not array:
        return -1
    low = -1
    high = len(array)
    index = int((high + low) / 2)
    return _chop(low, high, index, elem, array)

def _chop(low, high, index, elem, array):
    if high > low:
        if elem < array[index]:
            high = index - 1
            index = int((high + low) / 2)
            return _chop(low, high, index, elem, array)
        elif elem > array[index]:
            low = index + 1
            index = int((high + low) / 2)
            return _chop(low, high, index, elem, array)
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
        self.assertEqual(-1, chop(2, [1, 3, 5]))
        self.assertEqual(-1, chop(4, [1, 3, 5]))
