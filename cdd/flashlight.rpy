"""CDD для отрисовки фонарика.

Был написан для мода `"Зелёный свет" <https://steamcommunity.com/sharedfiles/filedetails/?id=2028014801>`_.

Предоставляет возможность создавать сцены с использованием
визуального эффекта "фонарика". Код CDD был немного доработан
по сравнению с версией в моде "Зелёный свет".

В основном это коснулось возможности обработки событий
подложки и замены всех отображаемых частей прямо в процессе
работы.
"""

init 1 python in renpy_tech.cdd.flashlight:

    from renpy.display.core import Displayable
    from renpy.display.render import Render

    
    class Flashlight(object, Displayable):
        """Класс CDD для отрисовки визуального эффекта фонарика.

        Является интерактивным визуальным CDD, который позволяет
        на основе трёх изображений: занавеса, подложки и маски создать
        визуальный эффект "фонарика".

        Подложка есть основное изображение, на которое "светят". Оно скрывается
        за занавесом, изображением, которое затмевает собой подложку. Фонарик является
        маской, на прозрачных пикселях которой отображается занавес,
        а на непрозрачных - подложка.

        Attributes
        ----------
        events : bool
            Обрабатыает ли объект события.
        _child : Displayable
            Подложка сцены.
        _mask : Displayable
            Маска фонарика сцены.
        _curtain : Displayable
            Занавес сцены.
        _xpos : int
            Последнее положение мышки пользователя по оси OX.
        _ypos : int
            Последнее положение мышки пользователя по оси OY.

        Methods
        -------
        render(width, height, st, at)
            Возвращает объект Render сцены.
        event(ev, x, y, st)
            Обрабатывает событие сцены.
        visit()
            Возвращает список использованных Displayables.

        Examples
        --------
        >>> from store.renpy_tech.cdd import Flashlight
        >>> flashlight_scene = Flashlight("bg some_your_bg", "your_flashlight_mask")
        >>> show flashlight_scene as bg

        >>> from store.renpy_tech.cdd import Flashlight
        >>> show expression Flashlight("bg some_your_bg", "your_flashlight_mask") as bg
        """
        def __init__(
            self,            # type: Flashlight
            child,           # type: Union[str, Displayable]
            mask,            # type: Union[str, Displayable]
            curtain="#000",  # type: Union[str, Displayable]
            **kwargs         # type: **Any
        ):
            # type: (...) -> None
            super(Flashlight, self).__init__(**kwargs)

            self.events = True  # type: bool

            self._child = renpy.displayable(child)  # type: Displayable
            self._mask = renpy.displayable(mask)  # type: Displayable
            self._curtain = renpy.displayable(curtain)  # type: Displayable

            self._xpos, self._ypos = renpy.get_mouse_pos()  # type: int

        @property
        def child(self):
            # type: () -> Displayable
            return self._child

        @child.setter
        def child(self, child):
            # type: (Union[str, Displayable]) -> None
            self._child = renpy.displayable(child)

        @property
        def mask(self):
            # type: () -> Displayable
            return self._mask

        @mask.setter
        def mask(self, mask):
            # type: (Union[str, Displayable]) -> Displayable
            self._mask = renpy.displayable(mask)

        @property
        def curtain(self):
            # type: () -> Displayable
            return self._curtain

        @curtain.setter
        def curtain(self, curtain):
            # type: (Union[str, Displayable]) -> Displayable
            self._curtain = renpy.displayable(curtain)

        def render(self, width, height, st, at):
            # type: (int, int, float, float) -> Render
            """TODO: docstring
            """
            scene = renpy.render(self._child, width, height, st, at)  # type: Render
            curtain = renpy.render(self._curtain, width, height, st, at)  # type: Render

            mask = renpy.render(self._mask, width, height, st, at)  # type: Render
            mask_width, mask_height = mask.get_size()  # type: int

            light = Render(width, height, opaque=False)  # type: Render

            light.place(self._mask, self._xpos - (mask_width / 2.0), self._ypos - (mask_height / 2.0))

            rv = Render(width, height, opaque=False)  # type: Render

            rv.operation = renpy.display.render.IMAGEDISSOLVE
            rv.operation_alpha = True
            rv.operation_complete = 0.5
            rv.operation_parameter = 8

            if renpy.display.render.models:
                rv.mesh = True
                rv.add_shader("renpy.imagedissolve",)
                rv.add_uniform("u_renpy_dissolve_offset", 0)
                rv.add_uniform("u_renpy_dissolve_multiplier", 1.0)
                rv.add_property("mipmap", renpy.config.mipmap_dissolves if (self.style.mipmap is None) else self.style.mipmap)

            rv.blit(light, (0, 0), focus=False, main=False)
            rv.blit(curtain, (0, 0), focus=False, main=False)
            rv.blit(scene, (0, 0), focus=True, main=True)

            return rv

        def event(self, ev, x, y, st):
            # type: (pygame.Event, int, int, float) -> Union[None, Any]
            if self.events and ev.type == pygame.MOUSEMOTION:
                self._xpos, self._ypos = renpy.get_mouse_pos()
                renpy.redraw(self, 0)

            return self._child.event(ev, x, y, st)

        def visit(self):
            # type: () -> List[Displayable]
            return [self._child, self._mask, self._curtain]
