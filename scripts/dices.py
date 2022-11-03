#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Скрипт бросает игральные кости и выдаёт результат.
# Один бросок шестигранной кости:
# dices 1d6
# Четыре броска восьмигранной кости:
# dices 4d8
# Тысяча бросков тридцатигранной кости:
# dices 1000d30

import random
import argparse

#-------------------------------------------------------------------------
# Опции:

# Стандартная кость:
DICE = 20
# Число бросков стандартной кости:
DICE_THROWS = 1

#-------------------------------------------------------------------------
# Аргументы командной строки:

def create_parser():
    """Список доступных параметров скрипта."""
    parser = argparse.ArgumentParser()
    parser.add_argument('dice_string',
                        action='store', type=str, nargs='*', default='',
                        help='Кость D&D, например 2d6 (по умолчанию 1d20)'
                        )
    return parser

#-------------------------------------------------------------------------
# Функции:

def dice_range (n1, n2, throws=1):
    """Возвращает рандомное число в диапазоне."""
    d_sum = 0
    while throws > 0:
        # randint: n1 <= d <= n2
        d = random.randint(n1, n2)
        throws -= 1
        d_sum += d
    return d_sum

def throw_d2(throws=1):
    # Функции ниже для внешних вызовов.
    # Сам скрипт использут только dice_range
    """Бросаем двухгранную кость (монетку)."""
    d = dice_range(1, 2, throws)
    return d

def throw_d3(throws=1):
    d = dice_range(1, 3, throws)
    return d

def throw_d4(throws=1):
    """Бросаем четырёхгранную кость."""
    d = dice_range(1, 4, throws)
    return d

def throw_d6(throws=1):
    """Бросаем шестигранную кость."""
    d = dice_range(1, 6, throws)
    return d

def throw_d8(throws=1):
    """Бросаем восьмигранную кость."""
    d = dice_range(1, 8, throws)
    return d

def throw_d10(throws=1):
    """Бросаем десятигранную кость."""
    d = dice_range(1, 10, throws)
    return d

def throw_d12(throws=1):
    """Бросаем двенацтигранную кость."""
    d = dice_range(1, 12, throws)
    return d

def throw_d20(throws=1):
    """Бросаем двадцатигранную кость."""
    d = dice_range(1, 20, throws)
    return d

def throw_d100(throws=1):
    """Бросаем стогранную кость (проценты)."""
    d = dice_range(1, 100, throws)
    return d

#-------------------------------------------------------------------------
# Тело программы:

if __name__ == '__main__':
    # Создаётся список аргументов скрипта:
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.dice_string:
        # Бросок записывается как 2d6 (2 броска кости 6-гранной)
        # Вводим строку и дробим её по разделителю 'd' на два элемента.
        # Сначала число бросков, затем число граней кости.
        throws_dice_list = (namespace.dice_string[0].split('d'))
        throws = int(throws_dice_list[0])
        dice = int(throws_dice_list[1])
    else:
        throws = DICE_THROWS
        dice = DICE
    output = dice_range(1, dice, throws)
    print(output)
