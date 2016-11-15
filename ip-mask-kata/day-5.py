# -*- codeing: utf-8 -*-

import math


class Resolver(object):

    def resolve(self, ip_mask):
        return sum(self._octet_value(octet) for octet in ip_mask.split("."))

    def _octet_value(self, octet):
        return 8 - math.log2(256 - int(octet))


import unittest


class MaskResolverTest(unittest.TestCase):

    def setUp(self):
        self.resolver = Resolver()

    def test_resolves_four_octets(self):
        self.assertEqual(32, self.resolver.resolve("255.255.255.255"))

    def test_resolves_three_octets(self):
        self.assertEqual(24, self.resolver.resolve("255.255.255.0"))

    def test_resolves_two_octets(self):
        self.assertEqual(16, self.resolver.resolve("255.255.0.0"))

    def test_resolves_255_255_254_0(self):
        self.assertEqual(23, self.resolver.resolve("255.255.254.0"))
