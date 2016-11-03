# -*- codeing: utf-8 -*-

class FizzBuzzParser(object):

    def parse(self, toParse):
        return list(map(self._to_fizz_buzz, toParse))

    def _to_fizz_buzz(self, num):
        if self._is_buzz(num) and self._is_fizz(num):
            return "fizzbuzz"
        elif self._is_fizz(num):
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


class FizzBuzzParserTest(unittest.TestCase):

    def setUp(self):
        self.fizzBuzzParser = FizzBuzzParser()

    def _assert_that_parsed_into(self, expected, actual):
        self.assertEqual(expected, str(self.fizzBuzzParser.parse(actual)))

    def test_parses_one(self):
        self._assert_that_parsed_into("['1']", [1])

    def test_parses_three(self):
        self._assert_that_parsed_into("['fizz']", [3])

    def test_parses_nine(self):
        self._assert_that_parsed_into("['fizz']", [9])

    def test_parses_thirteen(self):
        self._assert_that_parsed_into("['fizz']", [13])

    def test_parses_five(self):
        self._assert_that_parsed_into("['buzz']", [5])

    def test_parses_ten(self):
        self._assert_that_parsed_into("['buzz']", [10])

    def test_parses_fifty_two(self):
        self._assert_that_parsed_into("['buzz']", [52])

    def test_parses_fifteen(self):
        self._assert_that_parsed_into("['fizzbuzz']", [15])

    def test_parses_odd_numbers(self):
        self._assert_that_parsed_into(
            "['1', 'fizz', 'buzz', '7', 'fizz', '11', 'fizz', 'fizzbuzz']",
            [1, 3, 5, 7, 9, 11, 13, 15]
        )
