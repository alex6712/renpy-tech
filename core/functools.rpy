"""Реализация базовых функций модификации.

В данном файле реализованы многие базовые функции, которые
используются в разных участках модификации.
Субмодуль ``functools`` модуля ``renpy_tech.core``.

Список функций и их саммари:
* ``get_salt`` -- функция генерации криптографической соли.
"""

init -1 python in renpy_tech.core.functools:
    

    def _replace_screen():
        _screens = renpy.display.screen.screens  # type: list

        _screens[(old_screen_name, None)] = _screens[(new_screen_name, None)]
