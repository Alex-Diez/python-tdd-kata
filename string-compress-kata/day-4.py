# -*- codeing: utf-8 -*-

class StringCompressor(object):

    def compress(self, toCompress):
        if toCompress is None:
            return ""
        else:
            result = []
            index = 0
            length = len(toCompress)
            while index < length:
                counter = 1
                index += 1
                while index < length and toCompress[index - 1] == toCompress[index]:
                    counter += 1
                    index += 1
                result.append(str(counter))
                result.append(toCompress[index - 1])
            return ''.join(result)

import unittest

class StringComperssorTest(unittest.TestCase):

    def setUp(self):
        self.compressor = StringCompressor()

    def test_none_compressed_to_an_empty_line(self):
        self.assertEqual("", self.compressor.compress(None))

    def test_one_char_string(self):
        self.assertEqual("1a", self.compressor.compress("a"))

    def test_string_of_unique_chars(self):
        self.assertEqual("1a1b1c", self.compressor.compress("abc"))

    def test_compress_a_string_of_doubled_characters(self):
        self.assertEqual("2a2b2c", self.compressor.compress("aabbcc"))

    def test_an_empty_string_is_compressed_to_another_empty_string(self):
        self.assertEqual("", self.compressor.compress(""))
