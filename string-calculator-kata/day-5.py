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
        while index < len(src) and src[index] not in ['+', '-', '*', '/']:
            index += 1
        return (int(src[0:index]), src[index:])


import unittest


class StringCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_calculates_a_number(self):
        self.assertEqual(56, self.calculator.calculate("56"))

    def test_calculates_an_addition(self):
        self.assertEqual(16, self.calculator.calculate("9+7"))

    def test_calculates_a_subtraction(self):
        self.assertEqual(5, self.calculator.calculate("8-3"))

    def test_calculates_a_multiplication(self):
        self.assertEqual(10, self.calculator.calculate("5*2"))

    def test_calculates_a_division(self):
        self.assertEqual(3, self.calculator.calculate("15/5"))

    def test_calculates_multiple_different_operations(self):
        self.assertEqual(27, self.calculator.calculate("4+3/1-2+10*3-56/7"))
