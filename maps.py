import collections
import numpy

ColorMappper = collections.namedtuple('col_map', 'red green blue')
color_mapper = ColorMappper(red=0, green=1, blue=2)


def function_mapper(function: str, value_1: float, value_2: float) -> None:
    function_lst = ['pow', 'sum', 'prod']
    with_numpy_str = f'numpy.{function}([{value_1},{value_2}])'
    without_numpy_str = f'{function}({value_1},{value_2})'

    if function in function_lst:
        try:
            return eval(with_numpy_str)
        except AttributeError:
            return eval(without_numpy_str)


print(function_mapper('pow', 2, 0))
print(function_mapper('sum', 2, 3))
print(function_mapper('prod', 2, 18))


