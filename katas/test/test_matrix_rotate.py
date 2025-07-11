import unittest
from katas.matrix_rotate import rotate_matrix


class TestIsUnique(unittest.TestCase):
    def test_empty_str(self):
        matrix = []
        rotated_matrix = []
        self.assertEqual(rotate_matrix(matrix), rotated_matrix)
    
    def test_empty_str(self):
        matrix = [[1]]
        rotated_matrix = [[1]]
        self.assertEqual(rotate_matrix(matrix), rotated_matrix)

    def test_unique(self):
        matrix = [[1, 2],
                  [3, 4],]
        rotated_matrix = [[3, 1],
                          [4, 2]]
        self.assertEqual(rotate_matrix(matrix), rotated_matrix)

    def test_not_unique(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        rotated_matrix = [[7, 4, 1],
                          [8, 5, 2],
                          [9, 6, 3]]
        self.assertEqual(rotate_matrix(matrix), rotated_matrix)