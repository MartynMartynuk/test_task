import ast
from typing import Literal, Any
import numpy


class FunctionMapper:
    def __init__(self, value_1: float, value_2: float) -> None:
        self.sum = value_1 + value_2
        self.prod = value_1 * value_2
        self.pow = value_1 ** value_2


color_mapper: dict[Literal['red', 'green', 'blue'], int] \
    = {'red': 0, 'green': 1, 'blue': 2}


def function_mapper(function: str, value_1: float, value_2: float) -> float | None:
    function_lst = ['pow', 'sum', 'prod']
    with_numpy_str = f'numpy.{function}([{value_1},{value_2}])'
    without_numpy_str = f'{function}({value_1},{value_2})'

    if function in function_lst:  # TODO How to implement function call without eval?
        try:
            return float(eval(with_numpy_str))
        except AttributeError:
            return eval(without_numpy_str)
    return None


def function_mapper_2(function: str, value_1: float, value_2: float) -> float or None:
    """
    Реализация вызова функции без использования eval
    """
    result = None
    if function == 'pow':
        result = value_1 ** value_2
    elif function == 'sum':
        result = value_1 + value_2
    elif function == 'prod':
        result = value_1 * value_2
    return result


def function_mapper_3(function: str, value_1: float, value_2: float) -> float or None:
    """
    Реализация вызова функции  использованием
    """
    obj = FunctionMapper(value_1, value_2)
    try:
        return getattr(obj, function)
    except AttributeError:
        return None
