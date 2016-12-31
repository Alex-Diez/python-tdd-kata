# -*- codeing: utf-8 -*-

def chop(e, array):
    if not array:
        return -1
    low = -1
    high = len(array)
    i = int((high + low) / 2)
    while high > low:
        if e < array[i]:
            high = i - 1
        elif e > array[i]:
            low = i + 1
        else:
            return i
        i = int((high + low) / 2)
    return -1

import unittest

class BinaryChopTest(unittest.TestCase):

    def test_search_empty_list(self):
        self.assertEqual(-1, chop(3, []))

    def test_one_element_list(self):
        self.assertEqual(0, chop(3, [3]))

    def test_one_element_list_without_match(self):
        self.assertEqual(-1, chop(3, [1]))

    def test_three_elements_list(self):
        self.assertEqual(0, chop(1, [1, 3, 5]))
        self.assertEqual(1, chop(3, [1, 3, 5]))
        self.assertEqual(2, chop(5, [1, 3, 5]))
        self.assertEqual(-1, chop(2, [1, 3, 5]))
