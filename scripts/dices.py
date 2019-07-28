#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

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
    d = dice_range(1, 2, throws)
    return d

def throw_d3(throws=1):
    d = dice_range(1, 3, throws)
    return d

def throw_d4(throws=1):
    d = dice_range(1, 4, throws)
    return d

def throw_d6(throws=1):
    d = dice_range(1, 6, throws)
    return d

def throw_d8(throws=1):
    d = dice_range(1, 8, throws)
    return d

def throw_d10(throws=1):
    d = dice_range(1, 10, throws)
    return d

def throw_d12(throws=1):
    d = dice_range(1, 12, throws)
    return d

def throw_d20(throws=1):
    d = dice_range(1, 20, throws)
    return d

def throw_d100(throws=1):
    d = dice_range(1, 100, throws)
    return d

def ability_gen():
    """Создаём параметры персонажа по правилам D&D 3.5
    
    1) Под каждый параметр бросаем 4 кости на d6
    2) Получается список чисел (например 1,4,6,3)
    3) Меньшее число из списка отбрсываем (получается 4,6,3)
    3) Суммируем показатели, получаем число в диапазоне 3-18
    4) Повторяем шесть раз.
    """
    ability_list = []
    while len(ability_list) < 6:
        # Четыре раза бросаем кость d6, сохраняем все значения:
        trows_list = [throw_d6() for x in range(4)]
        # Удаляем меньшее значение
        trows_list.remove(min(trows_list))
        ability = sum(trows_list)
        ability_list.append(ability)
    return ability_list

def ability_gen_max(ability_sum=60, ability_min=8, ability_max=13):
    """Создаём крутого персонажа, слабаков отбраковываем."""
    ability_list = ability_gen()
    # Исправить
        # Почему and не срабатывает?
    print(ability_list)
    while max(ability_list) <= ability_max \
    and sum(ability_list) <= ability_sum \
    and min(ability_list) >= ability_min:
        ability_list = ability_gen()
        print(ability_list)
    return ability_list

def hit_trow(level=1):
    """Бросаем кубики хит-поинтов."""
    # Исправить
        # Допилить
    hits = throw_d4(level)
    return ability_list


#-------------------------------------------------------------------------
# Тело программы:

if __name__ == '__main__':
    ability_gen_max()
    print(throw_d4(20))
    #print(throw_d4(1))
    #print(throw_d4(1))
    #print(throw_d4(1))
    #print(throw_d4(1))
    #print(throw_d8(1))
    #print(throw_d8(1))
    #print(throw_d8(1))
    #print(throw_d8(1))
    #print(throw_d8(1))
    #print(throw_d6(1))
    #print(throw_d6(1))
    #print(throw_d6(1))
    #print(throw_d6(1))
    #print(throw_d6(1))
