#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------
# Модули:

# Парсер аргументов командной строки:
import argparse
# Переменные операционной системы:
import os
# Регулярные выражения:
import re
# Сортировка вывода:
from collections import OrderedDict

# Автоматизацией не пренебрегай:
# _-Смешивание лапши в миске (килограмм)..... | 19
# _-Смешивание риса в миске (килограмм)...... | 45
# _-Смешивание салата в миске (килограмм).... | 51
# Преобразуем вывод в новые элементы словаря:
# xclip -o | sed "s@# @@" | sed "s@\.* | .*@@gi" | sed "s@^@metadict_detail['@" | sed "s@\$@'] = {@" | sed "s@\$@\n        }\n@"
# Или так, сразу дополняя:
# xclip -o | sed "s@# @@" | sed "s@\.* | .*@@gi" | sed "s@\(.*\)@metadict_army['\1'] = {\n        '\1':1,\n        }\n@"
# Строки из вывод в строки словаря:
# xclip -o | xclip -o | sed "s@# @@" | sed "s@\.* | .*@@gi" | sed "s@\(.*\)@        '\1':1,@gi"
# С подстановкой значений:
# xclip -o | sed "s@# @@" | sed "s@\.* | \(.*\)@:\1,@gi" | sed "s@\(.*\):@        '\1':@gi"

#-------------------------------------------------------------------------
# Опции:

# Каталог словарей:
METADICT_DIR = 'dict'
# Объект для исследования по умолчанию:
SQUAD = ''
# Число однотипных объектов для исследования:
NUMBER = 1
# Глубина исследования:
DEPTH = 99
# Словарь исполняемых в выводе выражений:
dict_math = {}

#-------------------------------------------------------------------------
# Аргументы командной строки:

def create_parser():
    """Список доступных параметров скрипта."""
    parser = argparse.ArgumentParser()
    parser.add_argument('squad',
                        nargs='*',
                        help='Название отряда (в "кавычках")'
                        )
    parser.add_argument('-D', '--directory',
                        action='store', dest='dir', type=str,
                        help='Каталог словарей (путь)'
                        )
    parser.add_argument('-d', '--depth',
                        action='store', dest='depth', type=int,
                        help='Глубина исследования (0-999)'
                        )
    parser.add_argument('-n', '--number',
                        action='store', dest='number', type=float,
                        help='Доля отряда, либо число отрядов (0.001-999)'
                        )
    parser.add_argument('-e', '--except',
                        action='store', dest='exc', type=str, nargs='*',
                        help='Искать в составе отряда (строка в "кавычках")'
                        )
    parser.add_argument('-E', '--except-cut',
                        action='store', dest='cut', type=str, nargs='*',
                        help='Отсечь поисковую выборку (строка в "кавычках")'
                        )
    parser.add_argument('-s', '--short',
                        action='store_true', default='False',
                        help='Краткий вывод, обобщение, расчёты'
                        )
    parser.add_argument('-m', '--model',
                        action='store_true', default='False',
                        help='Моделирование, затраты времени'
                        )
    parser.add_argument('-S', '--sort',
                        action='store_true', default='False',
                        help='Сортировка вывода по величине'
                        )
    return parser

#-------------------------------------------------------------------------
# Функции:

def metadict_path (metadict_dir):
    """Возвращает абсолютный путь к каталогу словарей."""
    # Получаем абсолютный путь к каталогу скрипта:
    script_path = os.path.dirname(os.path.abspath(__file__))
    # Добавляем к пути каталог словарей:
    metadict_path = script_path + '/' + metadict_dir
    return metadict_path

def find_files (directory):
    """Возвращает список путей ко всем файлам каталога, включая подкаталоги."""
    path_f = []
    for d, dirs, files in os.walk(directory):
        for f in files:
                # Формирование адреса:
                path = os.path.join(d,f)
                # Добавление адреса в список:
                path_f.append(path)
    return path_f

def key_search (search_string, dict):
    """Поиск нужного объекта в словаре, выбор по списку совпадений."""
    # Создаётся регистронезависимая поисковая строка:
    p = re.compile(search_string, re.I)
    # Создаём словарь совпадений:
    dict_found = {}
    counter = 0
    # Поиск в словаре:
    for line in sorted(dict.keys()):
        if p.findall(line):
            dict_found[counter] = line
            search_string = line
            counter = counter + 1
    # Если искомое не найдено, тогда выход:
    if not dict_found:
        print('---Совпадений не найдено')
        exit(0)
    # Если найден один варинт, тогда его и выбираем:
    elif len(dict_found) == 1:
        squad = dict_found[0]
    # Если несколько совпадений, тогда выбор по номеру:
    else:
        for key in dict_found:
            print(key,dict_found[key])
        string_number = input('---Найдено несколько совпадений (введите номер): ')
        search_string = dict_found[int(string_number)]
        squad = search_string
        print('-----------------------------------------------------')
    return squad

def key_search_list (search_string, dict):
    """Возвращает срез ключей словаря по регулярному выражению."""
    # Создаётся регистронезависимая поисковая строка:
    p = re.compile(search_string, re.I)
    # Создаём словарь совпадений:
    list_found = []
    # Поиск в словаре:
    for line in sorted(dict.keys()):
        if p.findall(line):
            list_found.append(line)
    if not list_found:
        print('---Совпадений не найдено, нет ключей для --cut', search_string)
        exit(0)
    else:
        return list_found

def bfd(vertex, number, dict_crew, metadict_army):
    """Обработка иерархической базы данных, функция обхода в ширину."""
    #print ('    vertex:', vertex, number)
    # Проверка, является ли объект составным:
    if vertex in metadict_army:
        # Определяется состав объекта:
        for key,value in sorted(metadict_army[vertex].items()):
            #print ('        key:', key, value)
            if type(value) == str and 'x' in value:
                dict_math[key] = value
                value = 1
            elif type(value) == list:
                dict_math[key] = value
                value = 1
            elif type(value) == str and 'x' not in value:
                print('Ошибка. type(value) == str', key)
                continue
            if vertex in dict_crew:
                #print(value, dict_crew[vertex])
                value = value * dict_crew[vertex]
            else:
                value = value * number
            # Если объект уже есть в рабочем словаре, прибавить:
            if key in dict_crew:
                dict_crew[key] = dict_crew[key] + value
            # Иначе создать новый объект:
            else:
                dict_crew[key] = value
    # Если объект цельный:
    else:
        # Проверка, есть ли такие объекты в рабочем словаре:
        if vertex in dict_crew:
            # Если да, суммировать:
            dict_crew[vertex] = dict_crew[vertex] + number
        else:
            dict_crew[vertex] = number

def value_replace(value, math_value, dict_crew_all):
    """Вычисления с переменными в выводе данных."""
    if type(math_value) == str:
        # Можно записать так:
        #'|----Обжитые земли (квадратный километр)':1 / 100,
        #'|----Обжитые земли (радиус, километр)':'(x / 100 / 3.14159265) ** (1/2)',
        # Тогда будет подмена x из значения
        math_value = math_value.replace('x', str(value))
        result = eval(math_value)
    elif len(math_value) == 2:
        # Или используя list;
        #'Обжитые земли (радиус, километр)':[
        #    '(x / 3.14159265) ** (1/2)',
        #    'Обжитые земли (квадратный километр)'],
        x = dict_crew_all.get(math_value[1], 1)
        math_value = math_value[0]
        math_value = math_value.replace('x', str(x))
        # Можно использовать ключевое слово "value":
        # metadict_detail['--Бедняки'] = {
        #         # Процент бедняков от численности населения:
        #         '+++- Бедняки (%)':[
        #             '(value / x) * 100',
        #             '++++ Население',
        #             ],
        #         }
        if 'value' in math_value:
            math_value = math_value.replace('value', str(value))
        result = eval(math_value)
    elif len(math_value) == 3:
        # Две переменные в списке:
        x = dict_crew_all.get(math_value[1], 1)
        y = dict_crew_all.get(math_value[2], 1)
        math_value = math_value[0]
        if 'x' in math_value:
            math_value = math_value.replace('x', str(x))
        if 'y' in math_value:
            math_value = math_value.replace('y', str(y))
        result = eval(math_value)
    elif len(math_value) >= 4:
        # Три переменные в списке:
        x = dict_crew_all.get(math_value[1], 1)
        y = dict_crew_all.get(math_value[2], 1)
        z = dict_crew_all.get(math_value[3], 1)
        math_value = math_value[0]
        if 'x' in math_value:
            math_value = math_value.replace('x', str(x))
        if 'y' in math_value:
            math_value = math_value.replace('y', str(y))
        if 'z' in math_value:
            math_value = math_value.replace('z', str(z))
        result = eval(math_value)
    else:
        print('Ошибка в value_replace: ', value, math_value)
        result = 0
    return result

#-------------------------------------------------------------------------
# Обработка аргументов командной строки:

# Создаётся список аргументов скрипта:
parser = create_parser()
namespace = parser.parse_args()

# Проверка, указана ли ссылка на каталог словарей (ключ -D --directory):
if namespace.dir:
    dir_path = os.path.expanduser(namespace.dir)
    dicts_list = find_files(dir_path)
else:
    dicts_list = find_files(metadict_path(METADICT_DIR))

# Загрузка словарей в базу данных:
metadict_army = {}
metadict_detail = {}
metadict_model = {}
for file_path in dicts_list:
    with open(file_path) as f:
        code = compile(f.read(), file_path, 'exec')
        exec(code, globals(), locals())

# Проверка, выбран ли словарь деталей (ключ -s --short):
if namespace.short is True:
    # Объединяем словари
    metadict_army.update(metadict_detail)

# Проверка, выбран ли словарь модели (ключ -m --model):
if namespace.model is True:
    # Объединяем словари
    metadict_army.update(metadict_model)

# Проверка, введено ли название отряда:
if namespace.squad:
    squad = ' '.join(namespace.squad)
else:
    # Если нет, берём стандартный:
    squad = SQUAD

# Проверка, указано ли число расчётных объектов:
if namespace.number is not None:
    obj_number = namespace.number
else:
    # Если нет, берём из опций:
    obj_number = NUMBER

# Если название неточное, срабатывает встроенный поисковик:
if squad not in metadict_army.keys():
    squad = key_search(squad, metadict_army)
    print('Выбрано:', squad, round(obj_number))

# Исключаем (выделяем) указанный объект из словаря:
if namespace.exc:
    squad_except = ' '.join(namespace.exc)
    # Если название неточное, срабатывает встроенный поисковик:
    if squad_except not in metadict_army.keys():
        print('-----------------------------------------------------')
        print('---Число каких объектов вычисляем?')
        squad_except = key_search(squad_except, metadict_army)
else:
    squad_except = None

# Исключаем (выделяем) указанный объект из словаря:
if namespace.cut and not namespace.exc:
    squad_cut = ' '.join(namespace.cut)
    # Если название неточное, срабатывает встроенный поисковик:
    if squad_cut not in metadict_army.keys():
        squad_cut_list = key_search_list(squad_cut, metadict_army)
        for key in squad_cut_list:
            if key in metadict_army:
                metadict_army.pop(key)
else:
    squad_cut_list = None

# Проверка, указана ли глубина исследования:
if namespace.depth != None:
    depth = namespace.depth
else:
    # Если нет, мспользовать стандартную:
    depth = DEPTH

#-------------------------------------------------------------------------
# Исполняемый код:

# Рабочий словарь:
dict_crew = {}

# Рабочий словарь с бэкапом наибольших значений:
dict_crew_all = {}

# Многоуровневый обход в ширину:
if depth == 0:
    for key,value in sorted(metadict_army[squad].items()):
        key = key * obj_number
        dict_crew[key] = value
else:
    cycles = depth - 1
    # Формируется временный словарь
    for key,value in sorted(metadict_army[squad].items()):
        value = value * obj_number
        # Первый уровень исследования
        #print ('-----------------')
        #print ('cycle:',cycles)
        bfd(key, value, dict_crew, metadict_army)
        #print ('    dict:', dict_crew)
    # Цикл исследования временного словаря
    while cycles > 0:
        #print ('-----------------')
        #print ('cycle:',depth)
        for key,value in sorted(dict_crew.items()):
            if key in metadict_army and squad_except != key:
                # Функция извлекает состав объекта:
                bfd(key, value, dict_crew, metadict_army)
                # Удаляется обработанный объект из словаря:
                value_backup = dict_crew.pop(key)
                # Сохраняем наибольшие значения в бэкапе:
                if key not in dict_crew_all:
                    dict_crew_all[key] = value_backup
                elif key in dict_crew_all\
                        and type(dict_crew_all[key]) == float:
                    dict_crew_all[key] += value_backup
                #print ('    dict:', dict_crew)
        cycles -= 1
        depth -= 1


# Ищем самый длинный ключ в словаре:
if len(dict_crew) > 0:
    longest_key=max(map(len, dict_crew))

# Пополнение словаря бэкапа данными из вывода:
for key,value in sorted(dict_crew.items()):
    dict_crew_all[key] = value

# Вывод данных:
if namespace.exc:
    value = dict_crew.pop(squad_except, 0)
    if squad_except in metadict_army[squad]:
        value = metadict_army[squad][squad_except]
    if squad_except in dict_math.keys():
        value = value_replace(value, dict_math[squad_except], dict_crew_all)
    #print(squad_except, round(value))
    print ('{0:.<{width}} | {1:0,}'.format(squad_except, round(value), width=longest_key))
else:
    if namespace.sort == True:
        dict_crew = OrderedDict(sorted(dict_crew.items(), key = lambda t: t[1], reverse = True))
    else:
        dict_crew = OrderedDict(sorted(dict_crew.items()))
    for key,value in dict_crew.items():
        if len(dict_math) > 0:
            for math_key,math_value in dict_math.items():
                if math_key == key:
                    value = value_replace(value, math_value, dict_crew_all)
        # Пропускаем строки, не относящиеся к срезу через ключ -E
        # Переводим заглавные буквы в строчные через lower:
        if namespace.cut and squad_cut.lower() not in key.lower():
            continue
        print ('{0:.<{width}} | {1:0,}'.format(key, round(value), width=longest_key))
