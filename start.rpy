"""Старт мода.

В данном файле мод добавляется в оригинальный список всех
модификаций ``mods`` и в его модифицированную табличную
версию ``modsImages``.

Также здесь описана метка старта модификации ``renpy_tech_start``.
"""

init 999 python hide:

    from store import mods    
    from store.renpy_tech.config import Config

    _config = Config()  # type: Config

    mods["renpy_tech_start"] = "{}".format(_config.MODIFICATION_NAME)  # добаление мода в список модов

    try:
        from store import modsImages as mods_images
    except ImportError as _:
        pass
    else:
        mods_images["renpy_tech_start"] = (None, False, _config.MODIFICATION_NAME)  # добаление мода в табличный список модов

label renpy_tech_start:

    window hide dissolve2

    $ renpy.scene()
    $ renpy.show("bg black")
    $ renpy.with_statement(dissolve2)

    $ renpy.block_rollback()

    window show
    me "Привет, разработчик!"
    window hide
