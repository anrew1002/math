import unittest
from matrix.matrix import *
from vectors.vectors import *
import math


class TestVectors(unittest.TestCase):
    def setUp(self):
        self.a = [[1, 2],
                  [6, 4]
                  ]
        self.b = [[2, 1],
                  [1, 1]]

    def test_matrix_valid_raise(self):
        with self.assertRaises(TypeError):
            matrix_exception((1, 2, 3))
            matrix_exception(1)
            matrix_exception([[1, "2", "str"], [1, 2, 3]])
        with self.assertRaises(ValueError):
            matrix_exception([[1, 2, 3], [1, 2]])

    def test_matrix_copy(self):
        def deep_not_is(matrix1, matrix2, k=0):
            """Глубокое применение  is """
            count = 0
            for i in range(len(matrix1)):
                if matrix1[i] is matrix2[i]:
                    count += 1
                    if count > k:
                        return False
            return True
        self.assertIsNot(matrix_copy(self.a), self.a)
        self.assertTrue(deep_not_is(
            matrix_row_multiply(self.a, 1, 1), self.a, 1))
        self.assertTrue(deep_not_is(matrix_scalar_product(self.a, 0), self.a))

    def test_matrix_add_and_sub(self):
        self.assertEqual(matrix_add(self.a, self.b), [
                         [3, 3], [7, 5]], "add is not correct")
        self.assertEqual(matrix_sub(self.a, self.b), [
                         [-1, 1], [5, 3]], "sub not correct")

    def test_matrix_transpose(self):
        self.assertEqual(matrix_transpose(self.a), [
                         [1, 6], [2, 4]], "Transpose doesnt work")

    def test_matrix_column(self):
        self.assertEqual(get_matrix_column(self.a, 0), [1, 6])

    def test_matrix_row(self):
        self.assertEqual(get_matrix_row(self.a, 0), [1, 2])
        self.assertFalse(get_matrix_row(self.a, 0) is self.a[0])

    def test_matrix_multiply(self):
        self.assertEqual(matrix_multiply(self.a, self.b), [[4, 3], [16, 10]])
        mt1 = [[1, 2, 2],
               [6, 4, 2]
               ]
        mt2 = [[2, 2],
               [2, 2],
               [3, 3]
               ]
        self.assertEqual(matrix_multiply(mt1, mt2), [[12, 12], [26, 26]])

        with self.assertRaises(ValueError):
            matrix_multiply(self.a, [self.b[0]])

    def test_matrix_scalar(self):
        self.assertEqual(matrix_scalar_product(self.a, 2), [[2, 4], [12, 8]])
        self.assertIsNot(matrix_scalar_product(self.a, 2), self.a)

    def test_add_sub_multiplied_row(self):
        self.assertEqual(add_multiplied_matrix_row(
            self.a, 0, 1, 3), [[19, 14], [6, 4]])
        self.assertEqual(sub_multiplied_matrix_row(
            self.a, 1, 0, 2), [[1, 2], [4, 0]])

    def test_matrix_row_multiply(self):
        self.assertEqual(matrix_row_multiply(self.a, 0, 2), [[2, 4], [6, 4]])
        self.assertIsNot(matrix_row_multiply(self.a, 0, 2), self.a)

    def test_swap_row(self):
        self.assertEqual(swap_matrix_row(self.a, 0, 1), [[6, 4], [1, 2]])
        self.assertIsNot(swap_matrix_row(self.a, 0, 1), self.a)

    def get_row_column(self):
        self.assertEqual(get_matrix_column(self.a, 0), [1, 6])
        self.assertEqual(get_matrix_row(self.a, 0), [1, 2])


if __name__ == '__main__':
    unittest.main()
