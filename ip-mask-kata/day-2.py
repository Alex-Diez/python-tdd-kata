# -*- codeing: utf-8 -*-

import math

class Resolver(object):

    def resolve(self, ip_mask):
        reversed_ip_mask = 0
        octet_index = 3
        for octet in ip_mask.split('.'):
            reversed_ip_mask |= (int(octet) ^ 0xFF) << octet_index * 8
            octet_index -= 1
        mask = 0;
        while reversed_ip_mask != 0:
            reversed_ip_mask = reversed_ip_mask >> 1
            mask += 1
        return 32 - mask


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
