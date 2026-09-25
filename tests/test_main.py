import unittest
from main import reverse_string

class TestReverseString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character_string(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_two_character_string(self):
        self.assertEqual(reverse_string("ab"), "ba")

    def test_longer_string(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

if __name__ == "__main__":
    unittest.main()
