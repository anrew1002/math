import unittest
from interpolation.interpolation import *


class TestSLE(unittest.TestCase):
    def setUp(self):
        self.a = [[1, 2], [3, 4], [3.5, 3], [6, 7]]

    def test_calc_linear_function(self):
        self.assertEqual(calc_linear_function([[2, 5], [6, 9]]), [1, 3])
        self.assertEqual(calc_linear_function([[1, 2], [3, 4]]), [1, 1])
        self.assertEqual(
            list(map(lambda x: round(x, 10), calc_linear_function([[3.5, 3], [6, 7]]))), [1.6, -2.6])
        self.assertEqual(
            list(map(round, calc_linear_function([[3, 4], [3.5, 3]]))), [-2, 10])

    def test_linear_equation(self):
        self.assertEqual(linear_equation(1, 3, 4), 7)

    def test_calc_piecewise_linear_function(self):
        b = [list(map(lambda x: round(x, 10), x))
             for x in calc_piecewise_linear_function(self.a)]
        self.assertEqual(b, [[1, 1], [-2, 10], [1.6, -2.6]])

    def test_elem_of_piecewise_linear_function(self):
        self.assertEqual(elem_of_piecewise_linear_function(self.a, -1.5), -0.5)
        self.assertEqual(elem_of_piecewise_linear_function(self.a, 3), 4)
        self.assertEqual(elem_of_piecewise_linear_function(self.a, 2), 3)
        self.assertEqual(
            round(elem_of_piecewise_linear_function(self.a, 5), 10), 5.4)

    def test_is_interpolated_elem(self):
        self.assertFalse(is_interpolated_elem(self.a, -5))
        self.assertFalse(is_interpolated_elem(self.a, 9))
        self.assertTrue(is_interpolated_elem(self.a, 3))

    def test_polinom_L(self):
        self.assertAlmostEqual(polinom_L(self.a, 4), 2.12)
        self.assertAlmostEqual(polinom_L(self.a, 2), 4.92)
