import unittest
from vectors.vectors import *
import math


class TestVectors(unittest.TestCase):
    def test_Area(self):
        self.assertEqual(is_collinear([1, 1], [2, 2]), True)
        self.assertEqual(is_collinear([2, 2, 10], [1, 1, 5]), True)
        self.assertEqual(is_vectors_equal([0, 1], [0, 1]), True)
        self.assertEqual(vector_lenght([1, 1]), math.sqrt(2))
        self.assertEqual(cos_of_vectors([0, 1], [1, 0]), 0)
        # self.assertEqual(vector_normalize([3, 7, 2]),
        #                  [3/math.sqrt(62), 7/math.sqrt(62), math.sqrt(2/31)])
        self.assertAlmostEqual(angle_of_vectors([0, 1], [1, 0]), 90, 4)
        self.assertAlmostEqual(vector_projection([1, 2], [3, 4]), 2.2)
        self.assertEqual(vector_projection([4, 5], [6, 0]), 4)


if __name__ == '__main__':
    unittest.main()
