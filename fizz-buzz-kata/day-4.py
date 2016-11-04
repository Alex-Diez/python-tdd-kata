# -*- codeing: utf-8 -*-

class Parser(object):

    def parse(self, toParse):
        return list(map(self._to_fizz_buzz, toParse))

    def _to_fizz_buzz(self, num):
        if self._is_fizz(num) and self._is_buzz(num):
            return "fizzbuzz"
        if self._is_fizz(num):
            return "fizz"
        elif self._is_buzz(num):
            return "buzz"
        else:
            return str(num)

    def _is_fizz(self, num):
        return num % 3 == 0 or '3' in str(num)

    def _is_buzz(self, num):
        return num % 5 == 0 or '5' in str(num)

import unittest

class FizzBuzzParaserTest(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_parses_one(self):
        self.assertEqual(["1"], self.parser.parse([1]))

    def test_parses_two(self):
        self.assertEqual(["2"], self.parser.parse([2]))

    def test_parses_three(self):
        self.assertEqual(["fizz"], self.parser.parse([3]))

    def test_parses_nine(self):
        self.assertEqual(["fizz"], self.parser.parse([9]))

    def test_parses_thirteen(self):
        self.assertEqual(["fizz"], self.parser.parse([13]))

    def test_parses_fife(self):
        self.assertEqual(["buzz"], self.parser.parse([5]))

    def test_parses_twenty(self):
        self.assertEqual(["buzz"], self.parser.parse([20]))

    def test_parses_fifty_two(self):
        self.assertEqual(["buzz"], self.parser.parse([52]))

    def test_parses_fifteen(self):
        self.assertEqual(["fizzbuzz"], self.parser.parse([15]))

    def test_parses_odd_numbers_from_one_till_fifteen(self):
        self.assertEqual(
            ["1", "fizz", "buzz", "7", "fizz", "11", "fizz", "fizzbuzz"],
            self.parser.parse(self._odd_numbers_from_one_till_fifteen())
        )

    def _odd_numbers_from_one_till_fifteen(self):
        return list(filter(lambda x: x % 2 == 1, range(16)))
