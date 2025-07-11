import unittest
from katas.list_flatten import flatten_list


class TestIsUnique(unittest.TestCase):
    def test_empty_str(self):
        self.assertEqual(flatten_list([]), [])

    def test_unique(self):
        self.assertEqual(flatten_list([1, 2]), [1, 2])

    def test_not_unique(self):
        self.assertEqual(flatten_list([1, [2, 3], [4, [5, 6]], 7]), [1, 2, 3, 4, 5, 6, 7])
    
    def test_not_unique(self):
        self.assertEqual(flatten_list([1, [2, [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]]]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])