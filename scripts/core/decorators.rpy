"""Декораторы.

В данном файле описаны некоторые декораторы [1]_, которые
позволяют модифицировать Ваши классы и функции.

Список декораторов и их саммари:
* ``singleton`` -- модифицирует класс, реализуя в нём паттерн ``Singleton``[2]_.

.. [1] Специальный механизм языка Python, см. https://peps.python.org/pep-0318/
.. [2] Паттерн, позволяющий использовать единственный экземпляр класса, см. 
    https://en.wikipedia.org/wiki/Singleton_pattern
"""

init 1 python in renpy_tech.core.decorators:

    def singleton(cls):
        # type: (type) -> type
        instances = {}
    
        def get_instance(*args, **kwargs):
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)

            return instances[cls]
    
        return get_instance
