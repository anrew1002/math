import logging
from modules.matrix import *
from modules.vectors import *

logging.basicConfig(level=logging.CRITICAL,
                    filename="py_log.log", filemode="w")


def matrix_slice(matrix: list, step=1):
    """Возвращает срез матрицы без первой строки и последней"""
    matrix = matrix_copy(matrix)
    matrix = matrix[step:]
    matrix = matrix_transpose(matrix)
    matrix = matrix[step:]
    return matrix_transpose(matrix)


def matrix_reverse(matrix: list):
    "Возвращает реверс версию"
    matrix = matrix_copy(matrix)
    matrix_x = matrix_transpose(matrix).pop()
    for row in range(len(matrix)):
        matrix[row].pop()
        matrix[row] = matrix[row][::-1]
    for row in range(len(matrix)):
        matrix[row].append(matrix_x[row])
    return matrix[::-1]


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


if __name__ == "__main__":
    def main():
        test_slay = [
            [2.0, 3.0, 2.0],
            [4.0, 3.0, 7.0]
        ]
        test_slay_2 = [[-1, 2, 6, 15],
                       [3, -6, 0, -9],
                       [1, 0, 6, 5]
                       ]
        test_slay_3 = [
            [1, 1, 1, 0],
            [4, 2, 1, 1],
            [9, 3, 1, 3]
        ]
        # logging.info(f"rev: \n{matrix_to_str(matrix_reverse(test_slay_3))}")
        otv = slay_calculation(test_slay_2)
        logging.info(f"otv: \n{matrix_to_str(otv)}")
        # logging.debug(f"gl-it:{glob_iter}")
    main()
