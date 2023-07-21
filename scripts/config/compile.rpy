#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Файл с объявлением функции компиляции и ``named store``.

Создаётся функция :func:`compile_all_files` для компиляции ``.py`` файлов
в ``.pyo``.

В ``named stores`` добавляется ``renpy_tech``, который является объектом 
:ref:`renpy.python.StoreModule` и позволяет изолировать идентификаторы от 
глобального ``store``, что позволяет свести к минимуму конфликты имён.
"""

python early in renpy_tech:

    import os
    import sys
    import py_compile

    from renpy import store

    def compile_all_files(path):
        """Компилирует все файлы в папке по пути *path* и всех её подпапках.

        Находит все файлы Python и компилирует их в ``.pyo``
        для подхвата движком Ren'Py. Находит файлы ``__init__.py``
        и возвращает множество родительских путей до найденный модулей.

        :param path: путь до директории, от которой начинается спуск
            по дереву вниз и компилирирование всех ``.py`` файлов
        :type path: str
        :return: множество абсолютных родительских путей до всех найденных модулей
        :rtype: set[str]
        """
        modules = set()  # type: set[str]
    
        for name in os.listdir(path):  # type: str
            new_path = os.path.join(path, name)  # type: str
    
            if os.path.isfile(new_path):
                if new_path.endswith(".py") and not os.path.isfile(new_path + "o"):
                    py_compile.compile(new_path)

                if name == "__init__.py":
                    modules.add(path.rsplit("\\", 1)[0])
            else:
                modules.update(compile_all_files(new_path))
    
        return modules
