import unittest
from main import Calculate, MAX_WORDS_LIMIT


class TestCalculate(unittest.TestCase):
    """Test cases for the Calculate class."""
    def test_calculate_empty_list(self):
        """Test calculate method with an empty list."""
        calc = Calculate()
        calc.words_or_path = ""
        self.assertEqual(calc.calculate(), None, "Empty list should return None")

    def test_calculate_ascending_ignore_case(self):
        """Test calculate method with ascending order and ignoring case."""
        calc = Calculate(ascending=True, ignore_case=True, words_or_path="Banana, apple, cherry")
        self.assertEqual(calc.calculate(), "apple, Banana, cherry")

    def test_calculate_ascending(self):
        """Test calculate method with ascending order."""
        calc = Calculate(ascending=True, words_or_path="Banana, apple, cherry")
        self.assertEqual(calc.calculate(), "Banana, apple, cherry")

    def test_calculate_descending_ignore_case(self):
        """Test calculate method with descending order and ignoring case."""
        calc = Calculate(ignore_case=True, words_or_path="Banana, apple, cherry")
        self.assertEqual(calc.calculate(), "cherry, Banana, apple")

    def test_calculate_descending(self):
        """Test calculate method with descending order."""
        calc = Calculate(words_or_path="Banana, apple, cherry")
        self.assertEqual(calc.calculate(), "cherry, apple, Banana")

    def test_calculate_word_limit_exceeded(self):
        """Test calculate method with word limit exceeded."""
        calc = Calculate(words_or_path=", ".join(["word"] * (MAX_WORDS_LIMIT + 1)))
        self.assertIsNone(calc.calculate(), "Exceeding word limit should return None")


if __name__ == '__main__':
    unittest.main()
