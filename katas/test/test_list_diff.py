import unittest
from katas.list_diff import find_difference


class TestIsUnique(unittest.TestCase):
    def test_empty_str(self):
        self.assertEqual(find_difference([]), 0)

    def test_unique(self):
        self.assertEqual(find_difference([1, 2]), 1)

    def test_not_unique(self):
        self.assertEqual(find_difference([-1, 100, -39, 1092]), 1131)
    
    def test_not_unique(self):
        self.assertEqual(find_difference([1092]), 0)