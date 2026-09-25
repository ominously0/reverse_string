def reverse_string(s: str) -> str:
    return s[::-1]

import unittest

class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character_string(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_multiple_characters_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

if __name__ == "__main__":
    unittest.main()
