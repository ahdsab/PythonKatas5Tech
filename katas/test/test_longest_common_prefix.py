import unittest
from katas.longest_common_prefix import longest_common_prefix


class TestIsUnique(unittest.TestCase):
    def test_empty_str(self):
        test1 = ["flower", "flow", "flight"]
        self.assertEqual(longest_common_prefix(test1), "fl")

    def test_unique(self):
        test2 = ["dog", "racecar", "car"]
        self.assertEqual(longest_common_prefix(test2), "")

    def test_not_unique(self):
        test3 = ["interspecies", "interstellar", "interstate"]
        self.assertEqual(longest_common_prefix(test3), "inter")
    
    def test_not_unique(self):
        test4 = ["apple", "apricot", "ape"]
        self.assertEqual(longest_common_prefix(test4), "ap")