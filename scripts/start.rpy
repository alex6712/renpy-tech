"""Старт мода.

В данном файле в ``PYTHONPATH`` добавляются все найденные и скомпилированные
модули и пакеты с помощью ``compile_all_files`` из файла ``compile.rpy``,
в котором был создан ``named store`` с именем ``renpy_tech``.
"""

init python hide:

    from store import (
        mods,
        os,
        renpy_tech,
        sys,
    )
    from store import modsImages as mods_images
    from store.renpy_tech import constants

    rt_compile_path = store.config.basedir.replace("\\", "/") + "/../../workshop/content/331470/"  # type: str

    for additional_path in persistent.rt_compile + [constants.STEAM_ID,]:
        # Выполняется компиляция.
        #
        # Список путей, в которых необходимо скомпилировать файлы,
        # сохранён в ``persistent.rt_compile``.
        #
        # Для каждого из путей формируется абсолютный путь и запускается
        # функция ``compile_all_files``, результат выполнения которой
        # добавляется в ``PYTHONPATH``.
        rt_path_to_compile = os.path.join(rt_compile_path, additional_path)  # type: str

        sys.path.extend(renpy_tech.compile_all_files(rt_path_to_compile))

    mods["renpy_tech_start"] = "%s" % constants.MODIFICATION_NAME
    """Добаление мода в список модов"""

    try:
        mods_images["renpy_tech_start"] = (None, False, constants.MODIFICATION_NAME)
    except NameError as _:
        pass
    """Добавляем мод в табличное меню модов"""

label renpy_tech_start:

    window hide dissolve2

    $ renpy.scene()
    $ renpy.show("bg black")
    $ renpy.with_statement(dissolve2)

    $ renpy.block_rollback()

    window show
    me "Привет, разработчик!"
    window hide
