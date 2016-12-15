# -*- codeing: utf-8 -*-

class Converter(object):

    def __init__(self):
        self.factors = {10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

    def convert(self, n):
        if n < 1:
            return ""
        arabic = sorted(list(filter(lambda e: e <= n, self.factors)))[-1]
        roman = self.factors.get(arabic)
        return roman + self.convert(n - arabic)

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

    def test_converts_10(self):
        self.assertEqual("X", self.converter.convert(10))

    def test_converts_9(self):
        self.assertEqual("IX", self.converter.convert(9))

    def test_converts_29(self):
        self.assertEqual("XXIX", self.converter.convert(29))
