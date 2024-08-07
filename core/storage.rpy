"""Хранилища.

В данном файле описаны классы для работы с хранилищами:
* ``Storage`` -- для создания именованных хранилищ;
* ``StorageManager`` -- для менеджмента хранилищ.

Также создан субмодуль ``storage`` модуля ``renpy_tech.core``.
"""

init -1 python in renpy_tech.core.storage:

    class Storage:
        """Хранилище.

        Предоставляет инструмент для создания именованных хранилищ
        с дополнительными настройками.

        Является обёрткой для класса list.

        Attributes
        ----------
        _counter : int
            Атрибут класса, счётчик созданных экземпляров-хранилищ.
        _storage : list
            Внутреннее хранилище. Список, содержащий элементы
            хранилища.
        name : str
            Наименование хранилища.
        _limit : Optional[int]
            Предел количества хранимых элементов.
        _frozen : bool
            Флаг невозможности модификации. Если установлен на True,
            то не допускается изменение содержимого хранилища.
        _typing : Type
            Указание, какого типа значения хранилище способно
            сохранять.
        """

        _counter = 0  # type: int
        """Счётчик созданных хранилищ"""

        def __init__(
            self,            # type: Storage
            _iterable=None,  # type: Optional[Iterable[Any]]
            name=None,       # type: Optional[str]
            limit=None,      # type: Optional[int]
            frozen=False,    # type: bool
            typing=object,   # type: Type
        ):
            # type: (...) -> None
            """Дандер-метод инициализации экземпляра, инициализатор.

            Принимает перечисленные ниже аргументы и инициализирует
            новый объект-хранилище.

            Arguments
            ---------
            _iterable : Optional[Iterable[Any]]
                Объект, поддерживающий итерирование, на основе
                элементов которого будет создано хранилище.
            name : Optional[str]
                Наименование хранилища. Если не указано, генерируется
                автоматически по шаблону:
                    storage_<порядковый номер>
            limit : Optional[int]
                Предел количества хранимых элементов. Если не указан,
                предел не установлен.
            frozen : bool
                Если установлен на True, то не допускается изменение
                содержимого хранилища после его создания.
            typing : Type
                Если указан, то хранилище принимает элементы только
                переданного типа.
            """
            Storage._counter += 1

            self._storage = list()  # type: List[Any]

            if _iterable is not None:
                self._storage.extend(_iterable)

            if name is not None:
                self.name = name  # type: str
            else:
                self.name = "storage_{number}".format(number=Storage._counter)

            self._limit = limit  # type: Optional[int]
            self._frozen = frozen  # type: bool
            self._typing = typing  # type: Type

        def _set_frozen(self, state):
            # type: (bool) -> None
            """Устанавливает значение атрибута ``_frozen``.

            Устанавливает в атрибут ``_frozen`` значение state.
            "Приватный" сеттер атрибута, реализующий проверку на
            правильность типа сохраняемых данных.

            Arguments
            ---------
            state : bool
                Значение, которое необходимо установить в атрибут ``_frozen``.

            Raises
            ------
            TypeError
                Несоответствие типа переданного значения и необходимого, bool.
            """
            if not isinstance(state, bool):
                raise TypeError(
                    "невозможно установить значение '{value}' в атрибут хранилища `_frozen`, "
                    "несоответствие типов '{given_type}' (передан) и 'bool' (разрешён)".format(
                        value=state, given_type=type(state)
                    )
                )

            self._frozen = state

        def freeze(self):
            # type: () -> None
            """Заомраживает хранилище.

            Устанавливает в атрибут ``_frozen`` значение True, что замораживает
            хранилище, не позволяя изменять его содержимое (добавлять, удалять
            элементы).

            See Also
            --------
            store.renpy_tech.core.storage.Storage._set_frozen :
                Сеттер атрибута ``_frozen``.
            """
            self._set_frozen(True)

        def defrost(self):
            # type: () -> None
            """Размораживает хранилище.

            Устанавливает в атрибут ``_frozen`` значение False, что размораживает
            хранилище, позволяя изменять его содержимое (добавлять, удалять
            элементы).

            See Also
            --------
            store.renpy_tech.core.storage.Storage._set_frozen :
                Сеттер атрибута ``_frozen``.
            """
            self._set_frozen(False)

        def is_frozen(self):
            # type: () -> bool
            """Возвращает значение приватного поля ``_frozen``.

            Является, по сути, геттером атрибута ``_frozen``, предоставляя
            внешний публичный интерфейс для получения значения внутреннего,
            "приватного" атрибута ``_frozen``.

            Returns
            -------
            bool
                Значение атрибута ``_frozen``.
            """
            return self._frozen

        def append(self, entity):
            # type: (Any) -> None
            """Добавляет новый элемент в хранилище.

            Проверяет, заморожено ли хранилище, зполнено ли оно до предела
            и совпадает ли тип переданной сущности с типом хранимых значений.

            При выявлении критического случая вызывает исключение.

            Arguments
            ---------
            entity : Any
                Сущность, которую необходимо добавить в хранилище.

            Raises
            ------
            TypeError
                Если это хранилище заморожено.
            IndexError
                Если это хранилище переполнено.
            """
            if self._frozen:
                raise TypeError("данный объект 'Storage' был заморожен, невозможно изменить его содержимое")

            if self._limit is not None and self.count_elements() == self._limit:
                raise IndexError("невозможно добавить ещё один элемент, достигнут лимит")

            if not isinstance(entity, self._typing):
                raise TypeError("данное хранилище принимает лишь элементы типа '{type_}' или его производных".format(type_=self._typing))

            self._storage.append(entity)

        def count_elements(self):
            # type: () -> int
            """Подсчитывает количество элементов в хранилище.

            Возвращает результат работы функции len на внутреннем
            хранилище ``_storage``.

            Returns
            -------
            int
                Количество элементов в хранилище.
            """
            return len(self._storage)
