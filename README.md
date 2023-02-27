# test_task
Веб-сервис написан с использованием ``Django Rest Framework``. В качестве базы данных использовалась ``sqlite3``.
Приложение обёрнуто в Docker: готово к запуску на ``dev`` сервере.

Архитектура программы повторяет классическую архитектуру Django приложения:
* Api реализация функций 2 и 3 представлена в ``test_endpoint/function_handler/views.py``
* Реализация функции 2 представлена в ``test_endpoint/function_handler/services/handlers``
* Файлы ``Dockerfile`` и ``docker-compose.yml`` в корневом каталоге.
