"""Функции для работы с персонажами.

В данном файле описаны функции для работы с персонжами:
их создания, удаления, изменения.

Является частью *\"платформы\"* **Ren'Py Tech**.
"""

init 1 python in renpy_tech.characters:

    from store import (
        _show_two_window,
        adv,
        colors,
        names,
        names_list,
        nvl,
        style,
        time_of_day,
    )

    _characters_data = dict()  # type: Dict[str, Dict[str, Any]]
    """Словарь с данными обо всех персонажах"""


    def _init_characters_data():
        # type: () -> None
        """Функция инициализации словаря данных персонажей.

        Инициализирует словарь данных персонажей игры. Устанавливает
        имя, словарь цветов и placeholder дополнительных настроек персонажа.
        Данные для инициализации берутся из оригинальных словарей ``names``
        и ``colors``.
        """
        for character_id, name in names.items():
            character_data = {  # type: Dict[str, Any]
                "name": name,
                "color_data": dict(),
                "properties": dict(),
            }

            _characters_data.setdefault(character_id, character_data)

            color_data = colors.get(character_id)  # type: Optional[Dict[str, Union[Tuple[int], str]]]

            if color_data is None:
                color_data = {  # type: Dict[str, Union[Tuple[int], str]]
                    "day": style.default.color,
                    "sunset": style.default.color,
                    "night": style.default.color,
                    "prolog": style.default.color,
                }

            character_data.get("color_data").update(color_data)


    def _get_character_data(character_id):
        # type: (str) -> Optional[Dict[str, Any]]
        """Возвращает данные по запрашиваемому персонажу.

        Принимает на вход идентификатор персонажа в виде строки,
        возвращает словарь сохранённых данных о персонаже.

        Если персонаж не зарегистрирован, возвращается ``None``.

        Arguments
        ---------
        character_id : str
            Глобальный идентификатор персонажа, например, ``mi``.

        Returns
        -------
        Optional[Dict[str, Any]]
            Словарь с данными запрашиваемого персонажа.
        """
        return _characters_data.get(character_id)

    
    def register_dynamic_character(
        character_id,       # type: str
        name,               # type: str
        color,              # type: Union[Tuple[int], str]
        color_data=dict(),  # type: Dict[str, Union[Tuple[int], str]]
        **properties
    ):
        # type: (...) -> None
        """Добавляет данные о персонаже в словарь.

        Используется как внешний публичный интерфейс добавления
        данных о персонаже в "приватный" словарь ``characters_data``.

        Arguments
        ---------
        character_id : str
            Глобальный идентификатор персонажа, например, ``mi``.
        name : str
            Имя персонажа.
        color : Union[Tuple[int], str]
            Цвет имени персонажа. Может передаваться либо как кортеж
            из трёх или четырёх целочисленных значений (RGB и RGBA) или
            как строка (HEX).
        color_data : Dict[str, Union[Tuple[int], str]]
            Словарь с даными о цвете имени персонажа в зависимости от
            состояния времени игры.
        """
        for state in ("day", "sunset", "night", "prolog"):
            color_data.setdefault(state, color)

        character_data = _get_character_data(character_id)  # type: Dict[str, Any]
        character_data.update({"name": name})
        character_data.update({"color_data": color_data})

        character_properties = character_data.get("properties")  # type: Dict[str, Any]
        character_properties.update(properties)


    def define_dynamic_character(character_id, name=None, is_nvl=False, **properties):
        # type: (str, Optional[str], bool, **Any) -> DynamicCharacter
        """TODO: docstring"""
        kind, ctc_animation = (nvl, "ctc_animation_nvl") if is_nvl else (adv, "ctc_animation")

        default_properties = {
            "kind": kind,
            "who_color": style.default.color,
            "who_suffix": ":" if is_nvl else kind.who_suffix,
            "what_style": "normal_{}".format(time_of_day),
            "image": character_id,
            "ctc": ctc_animation,
            "ctc_position": "fixed",
            "show_two_window": _show_two_window,
        }

        def _safe_update(to, from_):
            # type: (Dict[str, Any], Dict[str, Any]) -> None
            """Функция безопасного обновления характеристик.

            Существует приоритет характеристик персонажа:
            * характеристики персонажа из аргументов функции ``define_dynamic_character``;
            * характеристики персонажа из аргументов функции ``register_dynamic_character``;
            * характеристики персонажа по умолчанию ``default_properties``.

            Для того, чтобы не нарушить иерархию, была создана эта функция. Она позволяет
            добавлять новые значения при спуске по иерархии, но не обновлять сущестующие.
            Таким образом то, что было установлено в более верхней по иерархии структуре
            не будет заменено, а то, что не было установлено в ней, будет взято из структуры
            ниже по иерархии.

            Arguments
            ---------
            to : Dict[str, Any]
                Словарь, который будет обновляться.
            from_ : Dict[str, Any]
                Словарь, из которого будут взяты значения.
            """
            for key, value in from_.items():
                to.setdefault(key, value)

        character_data = _get_character_data(character_id)  # type: Dict[str, Any]

        if character_data is not None:
            character_properties = character_data.get("properties")  # type: Dict[str, Any]
            character_properties.setdefault("who_color", character_data.get("color_data").get(time_of_day))

            _safe_update(properties, character_properties)  # добавляем сохранённые характеристики

            if name is None:
                name = character_data.get("name")  # type: Optional[str]

        _safe_update(properties, default_properties)  # добавляем стандартные характеристики

        name_variable = "{}_name".format(character_id)  # type: str

        set_dynamic_character_name(character_id, name)
        globals()[character_id] = DynamicCharacter(name_variable, **properties)

        return globals()[character_id]


    def set_dynamic_character_name(character_id, name):
        # type: (str, str) -> None
        """Изменяет имя персонажа.

        Использует возможности класса ``DynamicCharacter``, позволяющие
        отслеживать имя персонажа из переменной в глобальной области
        видимости.

        В оригинальном БЛ отслеживаемая переменная с именем имеет вид
        <идентификатор персонажа>_name.

        Arguments
        ---------
        character_id : str
            Идентификатор персонажа в виде строки, например, ``"mi"``.
        name : str
            Строка, которая будет установлена как имя персонажа.

        Notes
        -----
        Если персонаж был создан классами ``Character``, ``ADVCharacter`` и др.
        не предоставляющими возможности отслеживать привязанную переменную
        с именем, то изменить их имя с помощью этой функции невозмножно.
        """
        globals()["{}_name".format(character_id)] = name


init 998 python hide in renpy_tech.characters:

    _init_characters_data()
