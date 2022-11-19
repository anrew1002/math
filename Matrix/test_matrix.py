import unittest
from main import *
from modules.vectors import *
import math


class TestVectors(unittest.TestCase):
    def setUp(self):
        self.a = [[1, 2],
                  [6, 4]
                  ]
        self.b = [[2, 1],
                  [1, 1]]

    def test_matrix_valid_raise(self):
        self.assertTrue(is_matrix_valid([[1, 2, 3], [1, 2, 1]]))
        self.assertFalse(is_matrix_valid([[1, 2, 4], [1, 2]]))
        with self.assertRaises(TypeError):
            matrix_exception((1, 2, 3))
            matrix_exception(1)
        with self.assertRaises(ValueError):
            matrix_exception([[1, 2, 3], [1, 2]])

    def test_matrix_copy(self):
        def deep_not_is(matrix1, matrix2, k=0):
            count = 0
            for i in range(len(matrix1)):
                if matrix1[i] is matrix2[i]:
                    count += 1
                    if count > k:
                        return False
            return True
        self.assertFalse(matrix_copy(self.a) is self.a)
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
        with self.assertRaises(ValueError):
            matrix_multiply(self.a, self.b[0])


if __name__ == '__main__':
    unittest.main()
