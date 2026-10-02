def reverse_string(s: str) -> str:
    return s[::-1]

class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")
    
    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")
    
    def test_normal_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_special_characters(self):
        self.assertEqual(reverse_string("#$%&amp;"), "&amp;%$#")
    
    def test_whitespace(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
