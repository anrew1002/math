import slay.slay as slay
from matrix.matrix import matrix_transpose, matrix_copy
import interpolation.interpolation as interpol


def least_squares(matrix: list):
    """
    Метод наименьших квадратов возвращает матрицу с одной строкой
    содержащей коэфиценты функции
    """
    matrix = matrix_copy(matrix)
    matrix_tr = matrix_transpose(matrix)
    b_part = matrix_transpose(matrix_tr[-1:])
    A_part = matrix_transpose(matrix_tr[:-1])
    A_tilda = slay.matrix_multiply(matrix_transpose(A_part), A_part)
    b_tilda = slay.matrix_multiply(matrix_transpose(A_part), b_part)
    # print(A_tilda)
    # print(b_tilda)
    out = []
    for i in range(len(A_tilda)):
        A_tilda[i].extend(b_tilda[i])
    # print(slay.matrix_to_str(A_tilda))
    out_put = slay.slay_calculation(A_tilda)
    # print(out_put)
    return matrix_transpose(out_put)[-1:][0]


def linear_aproximation(xy_data: list):
    """Получение коэффицентов апроксимированной линейной функции из точек"""
    matrix = [[x, 1, y] for x, y in xy_data]
    return least_squares(matrix)


def calc_linear_function_for_list(x_data: list, a, b):
    """Возвращает y по x из апроксимированной функции"""
    return [interpol.linear_equation(a, b, x) for x in x_data]


def aproximation_2nd_power(xy_data):
    """Получение коэффицентов апроксимированого полинома второй степени из точек"""
    matrix = [[x**2, x, 1, y] for x, y in xy_data]
    return least_squares(matrix)


def calc_aproximation_2nd_power_for_list(x_data, a, b, c):
    """Возвращает y по x из апроксимированной функции"""
    return [second_power_polunom(a, b, c, x) for x in x_data]


def second_power_polunom(a, b, c, x):
    return a*x**2 + b*x+c


def aproximation_3nd_power(xy_data):
    """Получение коэффицентов апроксимированого полинома третьей степени из точек"""
    matrix = [[x**3, x**2, x, 1, y] for x, y in xy_data]
    return least_squares(matrix)


def calc_aproximation_3nd_power_for_list(x_data, a, b, c, d):
    """Возвращает y по x из апроксимированной функции"""
    return [third_power_polunom(a, b, c, d, x) for x in x_data]


def third_power_polunom(a, b, c, d, x):
    """Функция третьей степени"""
    return a*x**3 + b*x**2 + c*x+d
