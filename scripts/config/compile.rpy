"""Файл с объявлением функции компиляции и ``named store``.

Создаётся функция ``compile_all_files`` для компиляции ``.py`` файлов
в ``.pyo``.

В ``named stores`` добавляется ``renpy_tech``, который является объектом 
``renpy.python.StoreModule`` и позволяет изолировать идентификаторы от 
глобального ``store``, что позволяет свести к минимуму конфликты имён.
"""

python early in renpy_tech:

    import os
    import py_compile


    def compile_all_files(path):
        # type: (str) -> set[str]
        """Компилирует все файлы в папке по пути *path* и всех её подпапках.

        Находит все файлы Python и компилирует их в ``.pyo``
        для подхвата движком Ren'Py. Находит файлы ``__init__.py``
        и возвращает множество родительских путей до найденный пакетов.

        Parameters
        ----------
        path : `str`
            Путь до директории, от которой начинается спуск
            по дереву вниз и компилирирование всех ``.py`` файлов

        Returns
        -------
        packages : `set[str]`
            Множество абсолютных родительских путей до всех найденных пакетов
        """
        packages = set()  # type: set[str]
    
        for name in os.listdir(path):  # type: str
            new_path = os.path.join(path, name)  # type: str
    
            if os.path.isfile(new_path):
                file = new_path  # type: str

                # пропускаем ren'py-in-python файлы
                if file.endswith("_ren.py"):
                    continue

                if file.endswith(".py") and not os.path.isfile(file + "o"):
                    py_compile.compile(file)

                if name == "__init__.py":
                    packages.add(path.rsplit("\\", 1)[0])
            else:
                packages.update(compile_all_files(new_path))
    
        return packages
