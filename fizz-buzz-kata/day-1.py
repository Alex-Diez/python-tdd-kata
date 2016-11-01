# -*- codeing: utf-8 -*-

class FizzBuzzParser(object):

    def parse(self, toParse):
        result = []
        for num in toParse:
            if self._is_fizz(num) and self._is_buzz(num):
                result.append("fizzbuzz")
            elif self._is_buzz(num):
                result.append("buzz")
            elif self._is_fizz(num):
                result.append("fizz")
            else:
                result.append(str(num))
        return result

    def _is_fizz(self, num):
        return num % 3 == 0 or '3' in str(num)

    def _is_buzz(self, num):
        return num % 5 == 0 or '5' in str(num)

import unittest


class FizzBuzzTest(unittest.TestCase):

    def setUp(self):
        self.fizzBuzzParser = FizzBuzzParser()

    def test_parses_in_an_empty_vec_when_give_an_empty_vec_of_numbers(self):
        self.assertEqual([], self.fizzBuzzParser.parse([]))

    def test_parses_vec_one(self):
        self.assertEqual(["1"], self.fizzBuzzParser.parse([1]))

    def test_parses_three_to_fizz(self):
        self.assertEqual(["fizz"], self.fizzBuzzParser.parse([3]))

    def test_parses_five_to_buzz(self):
        self.assertEqual(["buzz"], self.fizzBuzzParser.parse([5]))

    def test_parses_nine_to_fizz(self):
        self.assertEqual(["fizz"], self.fizzBuzzParser.parse([9]))

    def test_parses_ten_to_buzz(self):
        self.assertEqual(["buzz"], self.fizzBuzzParser.parse([10]))

    def test_parses_fifteen_to_fizzbuzz(self):
        self.assertEqual(["fizzbuzz"], self.fizzBuzzParser.parse([15]))

    def test_parses_thirteen_to_fizz(self):
        self.assertEqual(["fizz"], self.fizzBuzzParser.parse([13]))

    def test_parse_fifty_two_to_buzz(self):
        self.assertEqual(["buzz"], self.fizzBuzzParser.parse([52]))

    def test_parse_fifty_three_to_fizzbuzz(self):
        self.assertEqual(["fizzbuzz"], self.fizzBuzzParser.parse([53]))

    def test_parse_odd_numbers(self):
        self.assertEqual(["1", "fizz", "buzz", "7", "fizz", "11", "fizz", "fizzbuzz"], self.fizzBuzzParser.parse([1, 3, 5, 7, 9, 11, 13, 15]))
