# -*- codeing: utf-8 -*-

class Calculator(object):

    def calculate(self, src):
        if len(src) == 0:
            return 0
        else:
            return self._parse_expression(src)

    def _parse_expression(self, src):
        num_and_left = self._parse_term(src)
        result = num_and_left[0]
        src = num_and_left[1]
        while len(src) > 0:
            sign = src[0]
            num_and_left = self._parse_term(src[1:len(src)])
            src = num_and_left[1]
            if sign == '+':
                result += num_and_left[0]
            elif sign == '-':
                result -= num_and_left[0]
            else:
                break
        return result

    def _parse_term(self, src):
        num_and_left = self._parse_arg(src)
        result = num_and_left[0]
        src = num_and_left[1]
        while len(src) > 0:
            sign = src[0]
            num_and_left = self._parse_arg(src[1:len(src)])
            if sign == '*':
                result *= num_and_left[0]
                src = num_and_left[1]
            elif sign == '/':
                result /= num_and_left[0]
                src = num_and_left[1]
            else:
                break
        return (result, src)

    def _parse_arg(self, src):
        index = 0
        end = len(src)
        while index < end and src[index] not in ['+', '-', '*', '/']:
            index += 1
        return (int(src[0:index]), src[index:end])


import unittest


class StringCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_calculates_an_empty_string_into_0(self):
        self.assertEqual(0, self.calculator.calculate(""))

    def test_calculates_a_single_number(self):
        self.assertEqual(123, self.calculator.calculate("123"))

    def test_calculates_an_addition(self):
        self.assertEqual(15, self.calculator.calculate("10+5"))

    def test_calcualtes_a_subtraction(self):
        self.assertEqual(5, self.calculator.calculate("10-5"))

    def test_calculates_a_multiplication(self):
        self.assertEqual(20, self.calculator.calculate("4*5"))

    def test_calculates_a_division(self):
        self.assertEqual(3, self.calculator.calculate("12/4"))

    def test_calculates_number_of_different_operations(self):
        self.assertEqual(4, self.calculator.calculate("2+5*3-40/4+3-6"))
