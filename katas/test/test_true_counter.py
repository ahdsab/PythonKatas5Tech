import unittest
from katas.true_counter import count_true_values


class TestIsUnique(unittest.TestCase):
    def test_empty_str(self):
        self.assertEqual(count_true_values([]), 0)

    def test_unique(self):
        self.assertEqual(count_true_values([True] * 5), 5)

    def test_not_unique(self):
        self.assertEqual(count_true_values([True, False] + [True] * 5), 6)
        
    def test_unique_case_insensitivity(self):
        self.assertNotEqual(count_true_values([True, False] + [True] * 5), 7)

