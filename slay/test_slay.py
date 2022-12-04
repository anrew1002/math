import unittest
from slay.slay import *


class TestSLE(unittest.TestCase):
    def setUp(self):
        self.a = [[2, 3, 2], [4, 3, 7]]

    def test_calculation(self):
        self.assertEqual(slay_calculation(
            [[3, 2, -5, -1],
             [2, -1, 3, 13],
             [1, 2, -1, 9]]
        ),
            [[1, 0, 0, 3],
             [0, 1, 0, 5],
             [0, 0, 1, 4]])
        self.assertEqual(slay_calculation(
            [[1, 1, 1, 0],
             [4, 2, 1, 1],
             [9, 3, 1, 3]]), [[1, 0, 0, 0.5], [0, 1, 0, -0.5], [0, 0, 1, 0]])
        self.assertEqual(slay_calculation(
            [[4, -7, 8, -23],
             [2, -4, 5, -13],
             [-3, 11, 1, 16]]
        ),
            [[1, 0, 0, -2],
             [0, 1, 0, 1],
             [0, 0, 1, -1]]
        )
        self.assertEqual(slay_calculation([[2, 3, 2], [4, 3, 7]]), [
                         [1, 0, 2.5], [0, 1, -1]])

    def test_clean_func(self):
        self.assertIsNot(slay_calculation(self.a), self.a)
        self.assertIsNot(slay_row_swap(self.a), self.a)
        self.assertIsNot(slay_calculation_direct_part(self.a), self.a)
