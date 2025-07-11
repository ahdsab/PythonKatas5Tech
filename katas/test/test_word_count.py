import unittest
from katas.word_count import count_words


class TestIsUnique(unittest.TestCase):
    def test_empty_str(self):
        sentence = ""
        self.assertEqual(count_words(sentence), 0)

    def test_unique(self):
        sentence = "This "
        self.assertEqual(count_words(sentence), 1)

    def test_not_unique(self):
        sentence = "Thisis asample sentence for counting words."
        self.assertEqual(count_words(sentence), 6)
    