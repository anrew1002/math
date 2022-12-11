from interpolation.interpolation import *
import interpolation.mat_plot as plot
import numpy as np
# print(ab := calc_linear_function([[2, 5], [6, 9]]))
# print(linear_equation(*ab, 4))
# print(linear_equation(*ab, 1))
# print(calc_piecewise_linear_function([[1, 2], [3, 4], [3.5, 3], [6, 7]]))
# print(elem_of_piecewise_linear_function(
#     [[1, 2], [3, 4], [3.5, 3], [6, 7]], 9))
# print(is_interpolated_elem([[1, 2], [3, 4], [3.5, 3], [6, 7]], 1))
# print(polinom_L([[1, 2], [3, 4], [3.5, 3], [6, 7]], 2))

x1 = np.linspace(-5, 10, 100)
polinom = polinom_L([[1, 2], [3, 4], [3.5, 3], [6, 7]], x1)
y1 = polinom


x2 = np.linspace(-5, 10, 100)
y2 = list(map(lambda x: elem_of_piecewise_linear_function(
    [[1, 2], [3, 4], [3.5, 3], [6, 7]], x), x2))

plot.draw_plot(x1, y1, x2, y2)
