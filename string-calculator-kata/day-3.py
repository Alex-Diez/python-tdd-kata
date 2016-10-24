# -*- codeing: utf-8 -*-

class Calculator(object):

    def calculate(self, src):
        return self._parse_expression(src)

    def _parse_expression(self, src):
        num_and_left = self._parse_term(src)
        result = num_and_left[0]
        src = num_and_left[1]
        while src:
            sign = src[0]
            num_and_left = self._parse_term(src[1:])
            if sign == '+':
                result += int(num_and_left[0])
            elif sign == '-':
                result -= int(num_and_left[0])
            else:
                break
            src = num_and_left[1]
        return result

    def _parse_term(self, src):
        num_and_left = self._parse_arg(src)
        result = num_and_left[0]
        src = num_and_left[1]
        while src:
            sign = src[0]
            num_and_left = self._parse_arg(src[1:])
            if sign == '*':
                result *= int(num_and_left[0])
            elif sign == '/':
                result /= int(num_and_left[0])
            else:
                break
            src = num_and_left[1]
        return (result, src)

    def _parse_arg(self, src):
        index = 0
        length = len (src)
        while index < length and src[index] not in ['+', '-', '*', '/']:
            index += 1
        return (int(src[0:index]), src[index:])


import unittest


class StringCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_calculates_a_single_number(self):
        self.assertEqual(43, self.calculator.calculate("43"))

    def test_calculates_an_addition(self):
        self.assertEqual(13, self.calculator.calculate("6+7"))

    def test_calculates_a_subtraction(self):
        self.assertEqual(6, self.calculator.calculate("8-2"))

    def test_calculates_a_multiplication(self):
        self.assertEqual(35, self.calculator.calculate("5*7"))

    def test_calculates_a_division(self):
        self.assertEqual(8, self.calculator.calculate("40/5"))

    def test_calculates_multiple_different_operations(self):
        self.assertEqual(8, self.calculator.calculate("4+6/2-5+10*1-4"))
