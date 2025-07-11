import unittest
from katas.reduce_list import reduce_array


class TestIsUnique(unittest.TestCase):
    def test_empty_str(self):
        sample_list = []
        Reduced_list = []
        self.assertEqual(reduce_array(sample_list), Reduced_list)

    def test_unique(self):
        sample_list = [10, 15, 7, 20, 25]
        Reduced_list = [10, 5, -8, 13, 5]
        self.assertEqual(reduce_array(sample_list), Reduced_list)

    def test_not_unique(self):
        sample_list = [1, 2, 3, 4, 5]
        Reduced_list = [1, 1, 1, 1, 1]
        self.assertEqual(reduce_array(sample_list), Reduced_list)
    
    def test_not_unique(self):
        sample_list = [-1, -2, -3, -4, -5]
        Reduced_list = [-1, -1, -1, -1, -1]
        self.assertEqual(reduce_array(sample_list), Reduced_list)