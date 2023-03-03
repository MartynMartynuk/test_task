import json
from function_handler.serializers import ASerializer, BSerializer
from function_handler.services.maps import *


def function_2(a_json: str | list | dict, b_json: str | list | dict) -> None | list | dict:
    # TODO Why declaration is without typing?
    # Хотел обработать ошибки, но впоследствии забыл :(
    """
    Реализация function-2 - может работать как с полями dict, так и с list
    (при множественном задании расчетов)
    :param a_json:
    :param b_json:
    :return:
    """
    result = None
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
            result = c_lst
    elif type(a) is dict and type(b) is dict:  # TODO What is returned if previous conditions are not met?
        result = single_mean_handler(a, b)
    return result


def serializer_checker(obj_lst: list, obj_class: str) -> bool:
    """
    Вспомогательная функция определения соответствия величин в списке сериализатору объекта
    :param obj_lst: список
    :param obj_class: тип объекта
    :return:
    """
    result = True
    if obj_class == 'A':
        for obj_dict in obj_lst:
            obj_serializer = ASerializer(data=obj_dict)
            if obj_serializer.is_valid():
                pass
            else:
                return False
    elif obj_class == 'B':
        for obj_dict in obj_lst:
            obj_serializer = BSerializer(data=obj_dict)
            if obj_serializer.is_valid():
                pass
            else:
                return False
    else:
        result = False
    return result


def single_mean_handler(a: dict[Literal['value', 'color'], [float, str] ],
                        b: dict[Literal['function', 'value'], [str, float]]) -> \
        dict[Literal['value'], list] | None:
    res = function_mapper_3(b['function'], a['value'], b['value'])
    if res is not None:
        lst = [0] * 3
        color_index = color_mapper[a['color']]
        if res % 1 == 0:  # TODO What is the purpose of converting float to int?
            res = int(res)  # Причина в том, что в примерах был показан вывод числа int а не float в случае int ввода
        lst[color_index] = res
        return {'value': lst}
    return res
