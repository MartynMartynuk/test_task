import json


class A:
    def __init__(self, value_: float, color_: str):
        self.value = value_
        self.color = color_

    def __repr__(self):
        return f'{self.value}, {self.color}'

class B:
    def __init__(self, function_: str, value_: float):
        self.function = function_
        self.value = value_

    def __repr__(self):
        return f'{self.function}, {self.value}'


class C:
    def __init__(self, value_: list):
        self.value = value_

    def __repr__(self):
        return str(self.value)

    def __dict__(self):
        return {'value': self.value}

    def toJSON(self):
        return json.dumps(self.__dict__, default=str)
