from vectors.vectors import *


def matrix_to_str(matrix: list) -> str:
    return '\n'.join(map(str, (matrix)))+"\n"


def matrix_copy(matrix: list) -> list:
    return [elem[:] for elem in matrix]


# def is_matrix_valid(matrix: list):
#     if len(matrix) == 1:
#         return True
#     for i in range(1, len(matrix)):
#         if len(matrix[i]) != len(matrix[i-1]):
#             return False
#     return True


def matrix_exception(matrix: list) -> None:
    def is_matrix_valid(matrix):
        if len(matrix) != 1:
            for i in range(1, len(matrix)):
                if len(matrix[i]) != len(matrix[i-1]):
                    raise ValueError(
                        f"Матрица {matrix} имеет разное кол-во элементов в строках")
    if not (isinstance(matrix, list)):
        raise TypeError("Матрица должна быть задана типом list")
    for i in range(len(matrix)):
        if isinstance(matrix[i], list):
            is_matrix_valid(matrix)
            for j in range(len(matrix[i])):
                if not (isinstance(matrix[i][j], int | float)):
                    raise TypeError(
                        f"Матрица или ее элемент ,{matrix[i][j]},некорректного типа")
        elif not (isinstance(matrix[i], int | float)):
            raise TypeError(
                f"Матрица или ее элемент ,{matrix[i]} coords: {i,j},некорректного типа")

    return None


def matrix_scalar_product(matrix: list, scalar: float) -> list:
    """Умножение матрицы на скаляр"""
    matrix_exception(matrix)
    return list(map(lambda mt, sc=scalar: scalar_product(mt, sc), matrix))


def matrix_add(matrix1: list, matrix2: list) -> list:
    """Сложение матриц"""
    matrix_exception(matrix1)
    matrix_exception(matrix2)
    return list(map(vectors_add, matrix1, matrix2))


def matrix_sub(matrix1: list, matrix2: list) -> list:
    """Вычитание матриц"""
    matrix_exception(matrix1)
    matrix_exception(matrix2)
    return list(map(vectors_sub, matrix1, matrix2))


def matrix_transpose(matrix: list) -> list:
    """Транспонирование матрицы"""
    matrix_exception(matrix)
    output = []
    for i in zip(*matrix):
        output.append(list(i))
    return output


def matrix_multiply(matrix1: list, matrix2: list) -> list:
    """Умножение матриц"""
    matrix_exception(matrix1)
    matrix_exception(matrix2)
    if len(matrix2) != len(matrix1[0]):
        raise ValueError(
            "Невозможно умножить матрицы с разным количеством строк у первой и столбцов у второй.")
    tr_matrix2 = matrix_transpose(matrix2)
    return [[dot_product(matrix1[i], tr_matrix2[j])
             for j in range(len(matrix2[0]))] for i in range(len(matrix1))]


def get_matrix_row(matrix: list, index: int) -> list:
    """Получение строки матрицы по индексу от 0"""
    matrix_exception(matrix)
    return matrix[index].copy()


def get_matrix_column(matrix: list, index: int) -> list:
    """Получение столбца матрицы по индексу от 0"""
    matrix_exception(matrix)
    return matrix_transpose(matrix)[index]


def swap_matrix_row(matrix: list, i1: int, i2: int) -> list:
    """Поменять местами строчки в мастрице"""
    matrix_exception(matrix)
    matrix = matrix_copy(matrix)
    matrix[i1], matrix[i2] = matrix[i2], matrix[i1]
    return matrix


def matrix_row_multiply(matrix: list, row: int, scalar: float) -> list:
    """Умножение строки на скаляр"""
    matrix = matrix_copy(matrix)
    matrix[row] = scalar_product(matrix[row], scalar)
    return matrix


def add_multiplied_matrix_row(matrix: list, row_1, row_2, scalar) -> list:
    """Сложение строки row1 с умноженой на scalar строки row_2"""
    if row_1 == row_2:
        raise ValueError("Введены одинаковые строки")
    matrix = matrix_copy(matrix)
    matrix[row_1] = vectors_add(
        matrix[row_1], matrix_row_multiply(matrix, row_2, scalar)[row_2])
    return matrix


def sub_multiplied_matrix_row(matrix: list, row_1, row_2, scalar) -> list:
    """Вычитание строки row1 с умноженой на scalar строки row_2"""
    if row_1 == row_2:
        raise ValueError("Введены одинаковые строки")
    matrix = matrix_copy(matrix)
    matrix[row_1] = vectors_sub(
        matrix[row_1], matrix_row_multiply(matrix, row_2, scalar)[row_2])
    return matrix


if __name__ == "__main__":
    def main():
        test_matrix = [[1, 2],
                       [3, 4],
                       [5, 6]
                       ]
        test_matrix2 = [[7, 8],
                        [9, 10]
                        ]
        print(matrix_to_str(add_multiplied_matrix_row(
            test_matrix, 1, 2, 3)))
        print(matrix_to_str(test_matrix))
        # print(test_matrix)
        # a = get_matrix_row(test_matrix, 1)
        # a[0] = 999
        # print(test_matrix)
    main()
