# -*- codeing: utf-8 -*-

class Converter(object):
    def __init__(self):
        self.factors = {5: "V", 4: "IV", 1: "I"}

    def convert(self, n):
        if n < 1:
            return ""
        key = list(filter(lambda e: e <= n, self.factors.keys()))[-1]
        roman = self.factors.get(key)
        return roman + self.convert(n - key)

import unittest

class RomanNumberTest(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def test_converts_0(self):
        self.assertEqual("", self.converter.convert(0))

    def test_converts_1(self):
        self.assertEqual("I", self.converter.convert(1))

    def test_converts_5(self):
        self.assertEqual("V", self.converter.convert(5))

    def test_converts_2(self):
        self.assertEqual("II", self.converter.convert(2))

    def test_converts_4(self):
        self.assertEqual("IV", self.converter.convert(4))
