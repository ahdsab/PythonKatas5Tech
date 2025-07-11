import unittest
from katas.sum_of_digits import sum_of_digits


class TestIsUnique(unittest.TestCase):
    def test_empty_str(self):
        input = ""
        self.assertEqual(sum_of_digits([]), 0)

    def test_unique(self):
        input = "abc123"
        self.assertEqual(sum_of_digits([1, 2]), 6)

    def test_not_unique(self):
        input = "5 cats and 2 dogs"
        self.assertEqual(sum_of_digits([-1, 100, -39, 1092]), 7)
    
    def test_not_unique(self):
        input = "No digits here!"
        self.assertEqual(sum_of_digits([1092]), 0)

