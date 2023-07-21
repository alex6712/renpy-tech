#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Модуль работы с пакетами incode через pip.

Из доступных функций:
* :func:`install` устанавливает пакет;
* :func:`uninstall` удаляет пакет;
* :func:`install_requirements` устанавливает зависимости из файла;
* :func:`uninstall_requirements` удаляет зависимости, описаные в файле.

Модуль призван облегчить работу Python-разработчиков модов для игр
на Ren'Py.
"""

import sys
import subprocess


def install(package):
    """Функция установки python-пакета через pip.

    На вход принимает наименование пакета в PyPi и устанавливает его.

    :param package: наименование устанавливаемого пакета
    :type package: str
    """
    _execute_pip(["install", package])


def uninstall(package):
    """Функция удаления python-пакета через pip.

    На вход принимает наименование пакета в PyPi и удаляет его.

    :param package: наименование удаляемого пакета
    :type package: str
    """
    _execute_pip(["uninstall", package])


def install_requirements(path):
    """Функция установки зависимостей из файла.

    Принимает на вход путь до файла и устанавливает все зависимости из него.

    :param path: путь до файла с зависимостями
    :type path: str
    """
    _execute_pip(["install", "-r", path])


def uninstall_requirements(path):
    """Функция удаления зависимостей, описанных в файле.

    Принимает на вход путь до файла и удаляет все зависимости,
    описанные в нём.
    
    :param path: путь до файла с зависимостями
    :type path: str
    """
    _execute_pip(["uninstall", "-r", path])


def _execute_pip(args):
    """Функция взаимодейтсвия с pip через исполняемый код Python.

    Официциально было заявлено
    `(здесь) <https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program>`_,
    что в исполняемом коде лучше всего устанавливать пакеты, вызвав интерфейс 
    командной строки pip через подпроцесс.

    Т.к. pip вызывается для ``sys.executable``, то использован будет текущий
    интерпретатор.
    Т.е. пакет установится в окружение Python для Бесконечного лета, а не интерпретатора
    из ``PATH``.

    .. seealso::
        Модуль :mod:`subprocess`
            Документация модуля :mod:`subprocess` стандартной библиотеки

        Атрибут :attr:`executable` модуля :mod:`sys`
            Текущий интерпретатор

    :param args: аргументы вызова pip в виде отдельных строк без пробелов
    :type args: list[str]
    """
    subprocess.check_call([sys.executable, "-m", "pip"] + args)
