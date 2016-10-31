# -*- codeing: utf-8 -*-

class Calculator(object):

    def calculate(self, src):
        return self._parse_expression(src)

    def _parse_expression(self, src):
        result, src = self._parse_term(src)
        while src:
            sign = src[0]
            num, src = self._parse_term(src[1:])
            if sign == '+':
                result += num
            elif sign == '-':
                result -= num
            else:
                break
        return result

    def _parse_term(self, src):
        result, src = self._parse_arg(src)
        while src:
            sign = src[0]
            num, src = self._parse_arg(src[1:])
            if sign == '*':
                result *= num
            elif sign == '/':
                result /= num
            else:
                src = sign + str(num) + src
                break
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
        self.assertEqual(14, self.calculator.calculate("8+6"))

    def test_calculates_a_subtraction(self):
        self.assertEqual(4, self.calculator.calculate("14-10"))

    def test_calculates_a_multiplication(self):
        self.assertEqual(24, self.calculator.calculate("4*6"))

    def test_calculates_a_division(self):
        self.assertEqual(3, self.calculator.calculate("12/4"))

    def test_calculates_multiple_different_operations(self):
        self.assertEqual(10, self.calculator.calculate("5+4/2-10+5*3-2"))
