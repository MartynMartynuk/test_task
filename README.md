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

Для запуска function-3 подать ``POST`` запрос на адрес ``.../function_3/id_a/id_b/``, где ``id_a`` и ``id_b`` - id объектов А и В соответственно.
