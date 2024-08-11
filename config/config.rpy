"""Файл конфигурации мода.

В данном файле описан класс ``Config``, содержащий
главные константы модификации, а также создаётся субмодуль
``config`` модуля ``renpy_tech``.

Используется практически во всех других модулях модификации.
"""

init 2 python in renpy_tech.config:

    from store.renpy_tech.core.singleton import Singleton


    class Config(Singleton):
        """Класс с базовыми значениями модификации.

        Используется для хранения базовых значений модификации.

        **Настоятельно НЕ рекомендуется вручную менять содержимое
        атрибута ``_instance`` и атрибутов экземпляра.**

        Использует паттерн ``Singleton``.

        See Also
        --------
        store.renpy_tech.core.Singleton :
            Родительский класс для реализации паттерна ``Singleton``.
        """

        STEAM_ID = "4000000000"  # type: str
        """Идентификатор мода в стиме"""

        MODIFICATION_NAME = "Ren'Py Tech | Техно Ren'Py"  # type: str
        """Наименование мода"""
