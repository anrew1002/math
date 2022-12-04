import logging
from matrix.matrix import *
from vectors.vectors import *

logging.basicConfig(level=logging.CRITICAL,
                    filename="py_log.log", filemode="w")


def slay_row_swap(slay):
    slay = matrix_copy(slay)
    "Меняет местами строки при условии что первый элемент левого столбца нулевой"
    if get_matrix_row(slay, 0)[0] == 0:
        logging.debug("swap was!")
        for row in range(len(slay)):
            if slay[row][0] != 0:
                slay = swap_matrix_row(slay, 0, row)
        return slay
    return slay


def slay_calculation_direct_part(slay: list) -> list:
    """
    Прямой ход в Жордана Гаусса
    для реализации обратного в аргументы перейдать matrix_reverse версию
    """
    if slay != []:
        logging.debug(f"slay before row_swap func: \n{matrix_to_str(slay)}")
        slay = matrix_copy(slay)
        slay = slay_row_swap(slay)
        logging.debug(f"slay: \n{matrix_to_str(slay)}")
        row_0 = get_matrix_row(slay, 0)
        row_0 = scalar_product(row_0, 1/(row_0[0]))
        slay[0] = row_0
        for row_i in range(1, len(slay)):
            slay = sub_multiplied_matrix_row(
                slay, row_i, 0, slay[row_i][0])
        slay_2 = slay_calculation_direct_part(matrix_slice(slay))
        slay = merge_recursion_matrix(slay, slay_2)
        return slay
    return slay


def merge_recursion_matrix(slay, slay_2):
    """
    Возвращает матрицу смерженную с другой
    Нужна для соединения рекурсий
    """
    slay = matrix_copy(slay)
    slay_2 = matrix_copy(slay_2)
    for row in range(len(slay_2)):
        for column in range(len(slay_2[0])):
            slay[row+1][column+1] = slay_2[row][column]
    return slay


def slay_calculation(slay: list) -> list:
    """Основная функция вычеления СЛАУ"""
    output = slay_calculation_direct_part(slay)
    logging.info("direct part was succsesfull")
    return matrix_reverse(slay_calculation_direct_part(matrix_reverse(output)))
