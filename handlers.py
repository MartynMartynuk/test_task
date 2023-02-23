import json
from classes import *
from maps import *

# a = '''[
#     {"value": 1, "color": "red"},
#     {"value": 2, "color": "green"},
#     {"value": -2, "color": "blue"}
# ]'''
# b = '''[
#     {"function": "prod", "value": 2},
#     {"function": "sum", "value": 1},
#     {"function": "pow", "value": -2}
# ]'''

# c = [
#     {"value": [2, 0, 0]},
#     {"value": [0, 3, 0]},
#     {"value": [0, 0, -0.25]}
# ]

a = '''{"value": 1, "color": "red"}'''
b = '''{"function": "prod", "value": 2}'''
c = '''{"value": [2, 0, 0]}'''


def function_2(a_json, b_json):
    a = json.loads(a_json)
    b = json.loads(b_json)
    if type(a) is list and type(b) is list:
        pass
    elif type(a) is dict and type(b) is dict:
        return handler(a, b)


def handler(a, b):
    a_obj = A(a['value'], a['color'])
    b_obj = B(b['function'], b['value'])
    res = function_mapper(b_obj.function, a_obj.value, b_obj.value)
    lst = [0] * 3
    lst[color_mapper[a_obj.color]: int] = res
    c_obj = C(lst)
    return c_obj.toJSON()


print(function_2(a, b))
