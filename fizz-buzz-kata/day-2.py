# -*- codeing: utf-8 -*-

class Parser(object):

    def parse(self, toParse):
        result = []
        for num in toParse:
            str_num = str(num)
            if self._is_fizz(num, str_num) and self._is_buzz(num, str_num):
                result.append("fizzbuzz")
            elif self._is_fizz(num, str_num):
                result.append("fizz")
            elif self._is_buzz(num, str_num):
                result.append("buzz")
            else:
                result.append(str_num)
        return result

    def _is_divisible_by(self, num, div):
        return num % div == 0

    def _is_element_of(self, n, seq):
        return n in seq

    def _is_fizz(self, num, char_seq):
        return self._is_divisible_by(num, 3) or self._is_element_of('3', char_seq)

    def _is_buzz(self, num, char_seq):
        return self._is_divisible_by(num, 5) or self._is_element_of('5', char_seq)


import unittest


class FizzBuzzParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_parses_empty_list(self):
        self.assertEqual([], self.parser.parse([]))

    def test_parses_one(self):
        self.assertEqual(["1"], self.parser.parse([1]))

    def test_parses_three(self):
        self.assertEqual(["fizz"], self.parser.parse([3]))

    def test_parses_nine(self):
        self.assertEqual(["fizz"], self.parser.parse([9]))

    def test_parses_thirteen(self):
        self.assertEqual(["fizz"], self.parser.parse([13]))

    def test_parses_five(self):
        self.assertEqual(["buzz"], self.parser.parse([5]))

    def test_parses_ten(self):
        self.assertEqual(["buzz"], self.parser.parse([10]))

    def test_parses_fifty_two(self):
        self.assertEqual(["buzz"], self.parser.parse([52]))

    def test_parses_fifteen(self):
        self.assertEqual(["fizzbuzz"], self.parser.parse([15]))

    def test_parses_fifty_three(self):
        self.assertEqual(["fizzbuzz"], self.parser.parse([53]))
