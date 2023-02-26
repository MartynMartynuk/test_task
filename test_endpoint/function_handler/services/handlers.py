import json

from function_handler.models import A, B
# from function_handler.services.classes import *
from function_handler.services.maps import *

a = '''[
    {"value": 1, "color": "red"},
    {"value": 2, "color": "green"},
    {"value": -2, "color": "blue"}
]'''
b = '''[
    {"function": "prod", "value": 2},
    {"function": "sum", "value": 1},
    {"function": "pow", "value": -2}
]'''

c = [
    {"value": [2, 0, 0]},
    {"value": [0, 3, 0]},
    {"value": [0, 0, -0.25]}
]


# a = '''{"value": 1, "color": "red"}'''
# b = '''{"function": "prod", "value": 2}'''
# c = '''{"value": [2, 0, 0]}'''


def function_2(a_json, b_json):
    if type(a_json and b_json) is str:
        a = json.loads(a_json)
        b = json.loads(b_json)
    else:
        a = a_json
        b = b_json
    if type(a) is list and type(b) is list:
        if len(a) == len(b):
            c_lst = []
            i = 0
            iter_a = iter(a)
            iter_b = iter(b)

            while i < len(a):
                c_lst.append(single_mean_handler(next(iter_a), next(iter_b)))
                i += 1
            return c_lst
    elif type(a) is dict and type(b) is dict:
        return single_mean_handler(a, b)


def single_mean_handler(a, b):
    # a_obj = A(a['value'], a['color'])
    # b_obj = B(b['function'], b['value'])
    # a_obj = A.objects.create(value=a['value'], color=a['color'])
    # b_obj = B.objects.create(function=b['function'], value=b['value'])
    # print(a_obj)
    # res = function_mapper(b_obj.function, a_obj.value, b_obj.value)
    lst = [0] * 3
    # color_index = color_mapper[a_obj.color]

    # lst[color_index] = res
    # c_obj = C(lst)
    return lst


print(function_2(a, b))
