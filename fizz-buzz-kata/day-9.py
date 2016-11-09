# -*- codeing: utf-8 -*-

class Parser(object):

    def parse(self, toParse):
        return list(map(self._to_fizz_buzz, toParse))

    def _to_fizz_buzz(self, num):
        is_buzz = self._is_buzz(num)
        is_fizz = self._is_fizz(num)
        if is_fizz and is_buzz:
            return "fizzbuzz"
        if is_fizz:
            return "fizz"
        elif is_buzz:
            return "buzz"
        else:
            return str(num)

    def _is_fizz(self, num):
        return num % 3 == 0 or '3' in str(num)

    def _is_buzz(self, num):
        return num % 5 == 0 or '5' in str(num)

import unittest

class FizzBuzzParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_parses_one(self):
        self.assertEqual(["1"], self.parser.parse([1]))

    def test_parses_two(self):
        self.assertEqual(["2"], self.parser.parse([2]))

    def test_parses_three(self):
        self.assertEqual(["fizz"], self.parser.parse([3]))

    def test_parses_six(self):
        self.assertEqual(["fizz"], self.parser.parse([6]))

    def test_parses_thirteen(self):
        self.assertEqual(["fizz"], self.parser.parse([13]))

    def test_parses_five(self):
        self.assertEqual(["buzz"], self.parser.parse([5]))

    def test_parses_ten(self):
        self.assertEqual(["buzz"], self.parser.parse([10]))

    def test_parses_fifty_two(self):
        self.assertEqual(["buzz"], self.parser.parse([52]))

    def test_parses_fifty_three(self):
        self.assertEqual(["fizzbuzz"], self.parser.parse([53]))

    def test_parses_odd_numbers_till_fifteen(self):
        self.assertEqual(
            ["1", "fizz", "buzz", "7", "fizz", "11", "fizz", "fizzbuzz"],
            self.parser.parse([1, 3, 5, 7, 9, 11, 13, 15])
        )
