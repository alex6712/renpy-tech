"""Настройки мода.

В данном файле в устанавливаются ``default`` значения атрибутов
``persistent``:
* ``rt_override_config`` -- флаг перезаписи установленных ``config``.

Если флаг ``persistent.rt_override_config`` верен, то атрибуты
``config`` будут перезаписаны на установленные в этом файле.
"""

default persistent.rt_override_config = False  # type: bool

init 1 python:

    if persistent.rt_override_config:
        config.screen_width = 1920
        config.screen_height = 1080
        """Размеры экрана"""
    
        config.say_attribute_transition = Dissolve(0.2)  # dspr
        """Переход, использующийся в операторе ``@``"""
