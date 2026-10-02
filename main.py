import unittest

def reverse_string(s):
    return s[::-1]

class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character_string(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_long_string(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_with_spaces(self):
        self.assertEqual(reverse_string("hello  world"), "dlrow  olleh")

    def test_with_punctuation(self):
        self.assertEqual(reverse_string("Hello, world!"), "!dlrow ,olleH")

if __name__ == "__main__":
    unittest.main()
