import unittest
from approximation.approximation import *


class TestSLE(unittest.TestCase):
    def setUp(self):
        self.test_m = [[2, 3, 7],
                       [3, 3, 7],
                       [4, 7, 3]]
        self.test_m2 = [[2, 4],
                        [3, 9]]
        self.test_data3 = [[1, 2],
                           [3, 4],
                           [3.5, 3],
                           [6, 7]]

    def test_least_squares(self):
        self.assertEqual(round(least_squares(self.test_m2)[0], 2), 2.69)
        self.assertEqual(
            list(map(lambda x: round(x, 2), least_squares(self.test_m))), [4.68, -2.06])

    def test_linear_aproximation(self):
        self.assertEqual(
            list(map(lambda x: round(x, 2), linear_aproximation(self.test_data3))), [0.99, 0.67])

    def test_calc_linear_function_for_list(self):
        self.assertEqual(
            list(map(lambda x: round(x, 2), calc_linear_function_for_list([1, 3, 5], *linear_aproximation(self.test_data3)))), [1.66, 3.63, 5.60])

    def test_aproximation_2nd_power_for_list(self):
        self.assertEqual(
            list(map(lambda x: round(x, 2), calc_aproximation_2nd_power_for_list([1, 3, 5], *second_power_polunom(self.test_data3)))), [0.12, 0.07, 1.89])
