import json
from function_handler.services.maps import *


def function_2(a_json, b_json):  # TODO Why declaration is without typing?
    """
    Реализация function-2 - может работать как с полями dict, так и с list
    (при множественном задании расчетов)
    :param a_json:
    :param b_json:
    :return:
    """
    if type(a_json and b_json) is str:
        a = json.loads(a_json)
        b = json.loads(b_json)
    else:
        a = a_json
        b = b_json
    if type(a) is list and type(b) is list:
        if len(a) == len(b):  # TODO What is returned if len(a) != len(b)?
            c_lst = []
            i = 0
            iter_a = iter(a)
            iter_b = iter(b)

            while i < len(a):
                c_lst.append(single_mean_handler(next(iter_a), next(iter_b)))
                i += 1
            return c_lst
    elif type(a) is dict and type(b) is dict:  # TODO What is returned if previous conditions are not met?
        return single_mean_handler(a, b)


def single_mean_handler(a: dict, b: dict) -> dict:
    res = function_mapper(b['function'], a['value'], b['value'])
    lst = [0] * 3
    color_index = color_mapper[a['color']]
    if res % 1 == 0:  # TODO What is the purpose of converting float to int?
        res = int(res)
    lst[color_index] = res
    return {'value': lst}
