# -*- codeing: utf-8 -*-

class Compressor(object):

    def compress(self, toCompress):
        if toCompress is None:
            return ""
        else:
            compressed = []
            index = 0
            length = len(toCompress)
            while index < length:
                counter = 1
                index += 1
                while index < length and toCompress[index] == toCompress[index - 1]:
                    counter += 1
                    index += 1
                compressed.append(str(counter))
                compressed.append(toCompress[index - 1])
            return ''.join(compressed)


import unittest


class StringComperssorTest(unittest.TestCase):

    def setUp(self):
        self.compressor = Compressor()

    def test_none_compresses_to_empty_string(self):
        self.assertEqual("", self.compressor.compress(None))

    def test_one_char_string(self):
        self.assertEqual("1a", self.compressor.compress("a"))

    def test_string_of_unique_chars(self):
        self.assertEqual("1a1b1c", self.compressor.compress("abc"))

    def test_string_of_duobled_chars(self):
        self.assertEqual("2a2b2c", self.compressor.compress("aabbcc"))

    def test_empty_string_compressed_into_empty_string(self):
        self.assertEqual("", self.compressor.compress(""))
