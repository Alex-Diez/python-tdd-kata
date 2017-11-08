# -*- codeing: utf-8 -*-

class PrimeFactor(object):

    def generate(self, n):
        primes = []
        candidate = 2
        while n > 1:
            while n % candidate == 0:
                primes.append(candidate)
                n /= candidate
            candidate += 1
        return primes

import unittest

class PrimeFactorTest(unittest.TestCase):

    def setUp(self):
        self.primeFactor = PrimeFactor()

    def test_one(self):
        self.assertEqual([], self.primeFactor.generate(1))

    def test_two(self):
        self.assertEqual([2], self.primeFactor.generate(2))

    def test_three(self):
        self.assertEqual([3], self.primeFactor.generate(3))

    def test_four(self):
        self.assertEqual([2, 2], self.primeFactor.generate(4))

    def test_six(self):
        self.assertEqual([2, 3], self.primeFactor.generate(6))

    def test_eighth(self):
        self.assertEqual([2, 2, 2], self.primeFactor.generate(8))

    def test_nine(self):
        self.assertEqual([3, 3], self.primeFactor.generate(9))
