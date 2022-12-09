from slay.slay import *
import logging as log


def invert_matrix(matrix: list) -> list:
    """Поворот матрицы по диагонали"""
    matrix_len = len(matrix[0])
    matrix = identity_matrix_add(matrix)
    direct_part_matrix = slay_calculation_direct_part(matrix)
    invertable_matrix = matrix_reverse(slay_calculation_direct_part(
        matrix_reverse(direct_part_matrix, 2)), 2)
    output = [row[matrix_len:] for row in invertable_matrix]
    return output


def identity_matrix_add(matrix: list) -> list:
    """Добавление единичной матрицы"""
    original_matrix = matrix
    matrix = matrix_copy(matrix)
    for i in range(len(original_matrix)):
        matrix[i].extend([0 for x in range(i)])
        matrix[i].append(1)
        matrix[i].extend([0 for i in range(len(original_matrix)-i-1)])
    return matrix


def invert_matrix_slay_calc(matrix_a: list, matrix_b: list) -> list:
    """Расчет слау при помощи обратной матрицы"""
    matrix_a = invert_matrix(matrix_a)
    matrix_b = matrix_copy(matrix_b)
    return matrix_multiply(matrix_a, matrix_b)
