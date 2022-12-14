from approximation.approximation import *
import numpy as np
from approximation.mat_plot import *

test_m = [[2, 3, 7],
          [3, 3, 7],
          [4, 7, 3]]
test_m2 = [[2, 4],
           [3, 9]]
test_data3 = [[1, 2],
              [3, 4],
              [3.5, 3],
              [6, 7]]
print(least_squares(test_m2))
print(linear_aproximation(test_data3))

print(calc_linear_function_for_list(
    [1, 3, 5], *linear_aproximation(test_data3)))
print()
print(aproximation_2nd_power(test_data3))
print(calc_aproximation_2nd_power_for_list(
    [1, 3, 5], *aproximation_2nd_power(test_data3)))
print()
print(aproximation_3nd_power(test_data3))
print(calc_aproximation_3nd_power_for_list(
    [1, 3, 5], *aproximation_3nd_power(test_data3)))

# x1 = np.linspace(-5, 10, 100)
# y1 = calc_linear_function_for_list(x1, *linear_aproximation(test_data3))

# x2 = np.linspace(-5, 10, 100)
# y2 = calc_aproximation_2nd_power_for_list(
#     x1, *aproximation_2nd_power(test_data3))

# x3 = np.linspace(-5, 10, 100)
# y3 = calc_aproximation_3nd_power_for_list(
#     x3, *aproximation_3nd_power(test_data3))

# draw_plot([[x1, y1], [x2, y2], [x3, y3]], ["red", "blue", "orange"])
