"""Реализация паттерна ``Singleton``.

В данном файле находится реализация паттерна ``Singleton``
с помощью родительского класса.

Другие варианты в виде метакласса и декоратора показались
менее наглядными и сложными (как в случае с метаклассом) или
урезающими функционал (как в случае с декоратором).
"""

init 1 python in renpy_tech.core:

    class Singleton:
        """Родительский класс для реализации паттерна Singleton.

        Реализует паттерн ``Singleton``. Таким образом, в памяти единовременно
        хранится лишь один экземпляр этого класса, а сам класс предоставляет
        точку доступа к этому инстансу.

        Чтобы использовать паттерн наследуйте свой класс от этого.

        Notes
        -----
        Для более подробной информации о ``Singleton``:
        1. https://en.wikipedia.org/wiki/Singleton_pattern
        2. https://habr.com/ru/companies/otus/articles/779914

        Examples
        --------
        >>> from store.renpy_tech.core import Singleton
        >>> class SingletonClass(Singleton):
        ...     pass
        ...
        >>> singleton_one = SingletonClass()
        >>> singleton_two = SingletonClass()
        >>> singleton_one is singleton_two
        True
        """

        _instance = None  # type: Optional[Singleton]
        """Единственнй экземпляр класса"""

        def __new__(cls, *args, **kwargs):
            # type: (*Any, **Any) -> Singleton
            """Дандер-метод (магический метод) создания экземпляра, конструктор.

            Реализует паттерн ``Singleton``, позволяющий использовать
            один экземпляр класса, независимо от того, сколько раз
            и где был вызван конструктор.

            Если экземпляр ещё не был ни разу создан, то получаем его,
            вызвав конструктор родительского класса (object).

            Returns
            -------
            _instance : Singleton
                Экземпляр-одиночка класса ``Singleton``.
            """
            if cls._instance is None:
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

            return cls._instance