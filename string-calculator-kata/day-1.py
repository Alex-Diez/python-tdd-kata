# -*- codeing: utf-8 -*-

class Calculator(object):

    def calculate(self, src):
        if len (src) == 0:
            return 0
        else:
            return self._parse_expression(src)

    def _parse_expression(self, src):
        num_left = self._parse_term(src)
        result = num_left[0]
        src = num_left[1]
        while len(src) > 0:
            sign = src[0]
            if sign == '+':
                num_left = self._parse_term(src[1:len(src)])
                result += num_left[0]
                src = num_left[1]
            elif sign == '-':
                num_left = self._parse_term(src[1:len(src)])
                result -= num_left[0]
                src = num_left[1]
            else:
                break
        return result

    def _parse_term(self, src):
        num_left = self._parse_arg(src)
        result = num_left[0]
        src = num_left[1]
        while len(src) > 0:
            sign = src[0]
            if sign == '*':
                num_left = self._parse_arg(src[1:len(src)])
                result *= num_left[0]
                src = num_left[1]
            elif sign == '/':
                num_left = self._parse_arg(src[1:len(src)])
                result /= num_left[0]
                src = num_left[1]
            else:
                break
        return (result, src)

    def _parse_arg(self, src):
        length = len (src)
        index = 0
        while index < length and src[index] != '+' and src[index] != '-' and src[index] != '*' and src[index] != '/':
            index += 1
        return (int(src[0:index]), src[index:length])


import unittest


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_calculates_0_when_given_an_empty_string(self):
        self.assertEqual(0, self.calculator.calculate(""))

    def test_calculates_a_number(self):
        self.assertEqual(123, self.calculator.calculate("123"))

    def test_calculates_addtion(self):
        self.assertEqual(23, self.calculator.calculate("20+3"))

    def test_calculates_subtraction(self):
        self.assertEqual(17, self.calculator.calculate("20-3"))

    def test_calculates_multiplication(self):
        self.assertEqual(33, self.calculator.calculate("11*3"))

    def test_calculates_division(self):
        self.assertEqual(5, self.calculator.calculate("10/2"))

    def test_calculates_multiple_operations(self):
        self.assertEqual(23, self.calculator.calculate("36+2-5*4+40/8"))
