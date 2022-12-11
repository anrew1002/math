import slay.slay as slay


def isclose(a: float, b: float, rel_tol=1e-09, abs_tol=0.0) -> bool:
    """Сравнение float"""
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def calc_linear_function(points: list) -> list:
    """Возвращает a b коэффиценты из слау"""
    initial_equation = [[x, 1, y] for x, y in points]
    output_ab = slay.slay_calculation(initial_equation)
    output_ab = slay.matrix_transpose(output_ab)[-1]
    return output_ab


def linear_equation(a: float, b: float, x: float) -> float:
    """Возвращает y линейной функции"""
    return a*x + b


def calc_piecewise_linear_function(points: list) -> list:
    """Возращает a b коэффиценты для каждого куска функции"""
    output_ab = []
    for i in range(len(points)-1):
        output_ab.append(calc_linear_function([points[i]]+[points[i+1]]))
    return output_ab


def elem_of_piecewise_linear_function(points: list, x: float) -> float:
    """Возвращает интерпалированное или экстраполированное значение"""
    piece_func = calc_piecewise_linear_function(points)
    for i in range(len(points)-1):
        if x < points[i+1][0]:
            return linear_equation(*piece_func[i], x)
    return linear_equation(*piece_func[-1], x)


def is_interpolated_elem(points: list, x: float) -> bool:
    """Возарщает интерпалированное ли значение"""
    if x >= points[0][0] and x <= points[-1][0]:
        return True
    return False


def polinom_L(points: list, x: float) -> float:
    """Возрвращает L(x) многочлен """
    output = 0
    for i, point in enumerate(points):
        output += point[1] * basis_polinom(i, points, x)
    return output


def basis_polinom(i: int, points: list, x: float) -> float:
    """Возвращает l(y), базисный полином Лангранжа"""
    output = 1
    for j, point in enumerate(points):
        if j != i:
            output *= (x - point[0]) / (points[i][0] - point[0])
    return output
