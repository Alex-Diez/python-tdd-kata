# -*- codeing: utf-8 -*-

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

import unittest

class LeapYearTest(unittest.TestCase):

    def test_leap_year_is_divisible_by_4(self):
        self.assertTrue(is_leap_year(1996))

    def test_simple_year_is_not_divisible_by_4(self):
        self.assertFalse(is_leap_year(1995))

    def test_simple_year_is_divisible_by_100(self):
        self.assertFalse(is_leap_year(1900))

    def test_leap_year_is_divisible_by_400(self):
        self.assertTrue(is_leap_year(2000))
