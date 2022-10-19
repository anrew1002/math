from vectors import *


def input_equal_vectors() -> tuple:
    v1, v2 = (1, 1, 1), (0, 0)
    while len(v1) != len(v2):
        print("Введите одноразмерные вектора")
        v1, v2 = input_vectors()
    return v1, v2


def input_vectors() -> tuple:
    fst = input("Введите первый массив ").split(" ")
    scd = input("Введите второй массив ").split(" ")
    fst = [float(x) for x in fst]
    scd = [float(x) for x in scd]
    return fst, scd


def input_one_vector():
    v1 = [float(x) for x in input("Введите вектор: ")]
    return v1


def add_module():
    v1, v2 = input_equal_vectors()
    output = add(v1, v2)
    printing_res(output, "Сложение векторов: ")


def sub_module():
    v1, v2 = input_equal_vectors()
    output = sub(v1, v2)
    printing_res(output, "Вычитание векторов: ")


def scalar_product_module():
    v1 = input_one_vector()
    num = int(input("Введите скаляр: "))
    output = scalar_product(v1, num)
    printing_res(output, "Умножение на скаляр: ")


def collinearity_module():
    v1, v2 = input_equal_vectors()
    if is_collinear(v1, v2):
        print("Вектора коллинеарны!")
        k = koef_collinearity(v1, v2)
        if k > 0:
            print("..и сонаправленны")
        elif k < 0:
            print("..и противоположно направленны")
    else:
        print("Неколинеарны!")


def vector_lenght_module():
    a = input_one_vector()
    print("Длинна вектора: ", vector_lenght(a))


def vector_equal_module():
    if is_vectors_equal():
        print("Вектора коллинеарны")
    else:
        print("Вектора неколлинеарны")
