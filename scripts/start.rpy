#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Старт мода.

В данном файле в ``PYTHONPATH`` добавляются все найденные и скомпилированные
модули и пакеты.

В ``named stores`` добавляется ``renpy_tech``,который является объектом 
:ref:`renpy.python.StoreModule` и позволяет изолироватьидентификаторы от 
глобального ``store``, что позволить свести к минимуму конфликты имён.
"""

python early in renpy_tech:

    import os
    import sys
    import py_compile

    from renpy import store

    def _compile_all_files(path):
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
        modules = set()  # set[str]
    
        for name in os.listdir(path):
            new_path = os.path.join(path, name)  # str
    
            if os.path.isfile(new_path):
                if new_path.endswith(".py") and not os.path.isfile(new_path + "o"):
                    py_compile.compile(new_path)

                if name == "__init__.py":
                    modules.add(path.rsplit("\\", 1)[0])
            else:
                modules.update(_compile_all_files(new_path))
    
        return modules

    # Выбираем область компиляции.
    # Если флаг persistent.rt_compile_all верен,
    # то компилируется вся мастерская. В ином случае
    # только Ren'Py Tech
    rt_compile_path = store.config.basedir.replace("\\", "/") + "/../../workshop/content/331470/"

    # Добавляем родительские пути модулей в PYTHONPATH,
    # чтобы можно было их импортить
    sys.path.extend(_compile_all_files(rt_compile_path))
