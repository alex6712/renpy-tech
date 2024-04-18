"""Реализация базовых функций модификации.

В данном файле реализованы многие базовые функции, которые
используются в разных участках модификации.
Субмодуль ``functools`` модуля ``renpy_tech``.

Список функций и их саммари:
* ``get_salt`` -- функция генерации криптографической соли.
"""

init 2 python in renpy_tech.functools:

    from random import choice as random_choice
    from string import ascii_letters, digits

    alphabet_with_digits = digits + ascii_letters  # type: str


    def get_salt(_callable=random_choice, length=16):
        # type: (Callable[Iterable[Any], Any], int) -> str
        """Функция генерации криптографической соли.

        Используя переданный рандомайзер и алфавит, состоящий из цифр
        и букв латинского алфавита генерирует криптографическую соль
        заданной длины.

        Arguments
        ---------
        _callable : Callable[Iterable[Any], Any]
            Вызываемый объект, который позволяет выбрать
            случаный элемент итерируемой сущности.
        length : int
            Длина соли. Используется модуль переданного числа.

        Returns
        -------
        str
            Сгенерированная криптографическая соль.

        Examples
        --------
        >>> from store.renpy_tech.functools import get_salt
        >>> get_salt()
        '3sKBzm8Hqlp12uoL'

        >>> get_salt(length=32)
        'XgoK7X7r9p5V1JtMGemToEnJPokGN5nK'
        """
        return "".join(_callable(alphabet_with_digits) for _ in range(abs(length)))


    def _replace_screen():
        _screens = renpy.display.screen.screens  # type: list

        _screens[(old_screen_name, None)] = _screens[(new_screen_name, None)]
