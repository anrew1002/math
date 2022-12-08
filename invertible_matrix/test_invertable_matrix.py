import unittest
from invertible_matrix.invertible_matrix import *


class testInvertMatrix(unittest.TestCase):
    def setUp(self):
        self.a = [[1, 2],
                  [3, 4]
                  ]
        self.a_1 = [[-2, 1],
                    [1.5, -0.5]]
        self.x = [[-4],
                  [5]]

    def test_invert_matrix_slay_calc(self):
        self.assertEqual(invert_matrix_slay_calc(self.a, [[6], [8]]), self.x)
        self.assertIsNot(invert_matrix_slay_calc(self.a, [[6], [8]]), self.x)

    def test_invert_matrix(self):
        self.assertEqual(invert_matrix(self.a), self.a_1)
        self.assertIsNot(invert_matrix(self.a), self.a_1)

    def test_identity_matrix_add(self):
        self.assertEqual(identity_matrix_add(self.a), [
                         [1, 2, 1, 0], [3, 4, 0, 1]])
        self.assertEqual(identity_matrix_add(
            [
                [1, 2, 1],
                [3, 0, 4],
                [2, 2, 1]
            ]),
            [
                [1, 2, 1, 1, 0, 0],
                [3, 0, 4, 0, 1, 0],
                [2, 2, 1, 0, 0, 1]
        ])
        self.assertIsNot(identity_matrix_add(self.a),
                         [[1, 2, 1, 0], [3, 4, 0, 1]])
