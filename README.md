# test_task
Веб-сервис написан с использованием ``Django Rest Framework``. В качестве базы данных использовалась ``sqlite3``.
Приложение обёрнуто в Docker: готово к запуску на ``dev`` сервере.

Архитектура программы повторяет классическую архитектуру Django приложения:
* Api реализация функций 2 и 3 представлена в ``test_endpoint/function_handler/views.py``
* Реализация функции 2 представлена в ``test_endpoint/function_handler/services/handlers``
* Файлы ``Dockerfile`` и ``docker-compose.yml`` в корневом каталоге.

Для запуска function-2 подать ``POST`` запрос на адрес ``.../function_2/``, содержащий json представление объектов А и В:
```
[
  {"value": 2, "color": "red"}, 
  {"function": "sum", "value": 3}
]
```
Для запуска function-2 в режиме множественных расчётов подать ``POST`` запрос на адрес ``.../function_2/many``, содержащий json представление списков объектов А и В (длины списков должны быть равны!):
```
[
    [
        {
            "value": 1,
            "color": "red"
        },
        {
            "value": 2,
            "color": "green"
        },
        {
            "value": -2,
            "color": "blue"
        }
    ],
    [
        {
            "function": "prod",
            "value": 2
        },
        {
            "function": "sum",
            "value": 1
        },
        {
            "function": "pow",
            "value": -2
        }
    ]
]
```

Для запуска function-3 подать пустой ``POST`` запрос на адрес ``.../function_3/id_a/id_b/``, где ``id_a`` и ``id_b`` - id объектов А и В соответственно.

Для удобного добавления объектов А и В в базу данных подать ``POST`` запрос, содержащий JSON-представление объекта А иил В на адрес ``.../function_3/id_a/id_b/``. Например:
```
{"value": 2, "color": "red"}
```
Если переданный JSON будет соответствовать объекту А или В, то объект будет добавлен.