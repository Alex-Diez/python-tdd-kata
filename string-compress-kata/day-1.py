# -*- codeing: utf-8 -*-

class Compresser(object):

    def compress(self, string):
        if string is None:
            return ""
        else:
            result = []
            i = 0
            length = len(string)
            while i < length:
                count = 1
                i += 1
                while i < length and string[i-1] == string[i]:
                    count += 1
                    i += 1
                result.append(str(count))
                result.append(string[i - 1])
            return ''.join(result)


import unittest


class StringCompresser(unittest.TestCase):

    def setUp(self):
        self.compresser = Compresser()

    def test_null_compressed_into_empty_string(self):
        self.assertEqual("", self.compresser.compress(None))

    def test_empty_string_compressed_into_empty_string(self):
        self.assertEqual("", self.compresser.compress(""))

    def test_one_char_string(self):
        self.assertEqual("1a", self.compresser.compress("a"))

    def test_string_of_unique_chars(self):
        self.assertEqual("1a1b1c", self.compresser.compress("abc"))

    def test_string_of_duobled_chars(self):
        self.assertEqual("2a2b2c", self.compresser.compress("aabbcc"))

    def test_long_string_of_the_same_character(self):
        self.assertEqual("8a", self.compresser.compress("aaaaaaaa"))
