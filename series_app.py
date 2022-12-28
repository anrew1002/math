import numpy as np
from series.series import *
from series.plot import *
import math

x1 = np.linspace(-10, 10, 100)
y1 = list(map(lambda x: Exponential(x, 5), x1))
x2 = np.linspace(-10, 10, 100)
y2 = list(map(lambda x: math.e**x, x1))


draw_plot(x1, y1, x2, y2)


x1 = np.linspace(-10, 10, 100)
y1 = list(map(lambda x: sin_f(x, 5), x1))
x2 = np.linspace(-10, 10, 100)
y2 = list(map(lambda x: math.sin(x), x2))

draw_plot(x1, y1, x2, y2)

x1 = np.linspace(-10, 10, 100)
y1 = list(map(lambda x: cos_f(x, 5), x1))
x2 = np.linspace(-10, 10, 100)
y2 = list(map(lambda x: math.cos(x), x2))


draw_plot(x1, y1, x2, y2)

x1 = np.linspace(-1, 1, 100)
y1 = list(map(lambda x: arcsin_f(x, 5), x1))
x2 = np.linspace(-1, 1, 100)
y2 = list(map(lambda x: math.asin(x), x2))


draw_plot(x1, y1, x2, y2)

x1 = np.linspace(-1, 1, 100)
y1 = list(map(lambda x: arccos_f(x, 5), x1))
x2 = np.linspace(-1, 1, 100)
y2 = list(map(lambda x: math.acos(x), x2))


draw_plot(x1, y1, x2, y2)
