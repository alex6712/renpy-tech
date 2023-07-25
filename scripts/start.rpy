#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Старт мода.

В данном файле в ``PYTHONPATH`` добавляются все найденные и скомпилированные
модули и пакеты с помощью ``compile_all_files`` из файла ``compile.rpy``,
в котором был создан ``named store`` с именем ``renpy_tech``.
"""

init python hide:

    from renpy import store
    from store import renpy_tech

    rt_compile_path = store.config.basedir.replace("\\", "/") + "/../../workshop/content/331470/"  # type: str

    for additional_path in persistent.rt_compile + ["4000000000",]:
        # Выполняется компиляция.
        #
        # Список путей, в которых необходимо скомпилировать файлы,
        # сохранён в ``persistent.rt_compile``.
        #
        # Для каждого из путей формируется абсолютный путь и запускается
        # ``compile_all_files``, результат выполнения которой
        # добавляется в ``PYTHONPATH``.
        rt_path_to_compile = os.path.join(rt_compile_path, additional_path)  # type: str

        sys.path.extend(renpy_tech.compile_all_files(rt_path_to_compile))

    del rt_compile_path, rt_path_to_compile


init python in renpy_tech:

    import core as core
