"""Система изоляции модификаций (Modification Isolation System)

Позволяет изолировать модификации друг от друга, создавая
виртуальные окружения для каждой по отдельности.

В совокупности с возможностью включать это окружение
в сценарии это создаёт мощную систему противодействия
конфликтам модов.

Examples
--------
init:

    open modification modification_name  # создаём окружение модификации

    mod_char = Character(...)

    def mod_func(...):
        ...

    close modification modification_name

    def global_func(...):
        ...

label mod_label:

    use modification modification_name  # используем окружение модификации

    window show
    mod_char \"Я персонаж из модификации!\"  # Отлично!
    window hide

    $ mod_func(\"Я функция из модификации!\")  # Отлично!

    $ global_func(\"Я глобальная функция!\")  # Отлично!

    quit modification modification_name

    jump mot_mod_label

label mot_mod_label:

    # не используем окружение модификации

    window show
    mod_char \"Я персонаж из модификации!\"  # NameError: name 'mod_char' is not defined
    window hide

    $ mod_func(\"Я функция из модификации!\")  # NameError: name 'mod_func' is not defined

    $ global_func(\"Я глобальная функция!\")  # Отлично!

    return
"""

init -1 python in renpy_tech.mis:

    class Modification:
        """docstring for Modification"""
        def __init__(self, arg):
            super(Modification, self).__init__()
            self.arg = arg

            
