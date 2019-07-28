#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------
# Опции:

# Год начала отсчёта, принимаются любые целые числа:
YEAR_START = 1300
# До какого возраста исследовать популяцию:
AGE_END = 1000

# Переменные геометрической прогрессии роста населения:
# Численность населения в год начала отсчёта:
#POPULATION = 20000000
POPULATION = 3800000
# Уровень рождаемости (например: 0.03 значит 3%
# или 30 новорожденных на 1000 населения в год):
FERTILITY_RATE = 0.015
# Уровень смертности, аналогично:
MORTALITY_RATE = 0.012

# Переменные для расчёта военной экономики:
# ВВП на душу населения:
# https://ru.wikipedia.org/wiki/Список_стран_по_ВВП_(ППС)_на_душу_населения
GDP_RATE = 50000
# Годовой рост ВВП (без инфляции):
# Для примера, данные по росту ВВП США 1970-2013 годы:
# http://www.be5.biz/makroekonomika/gdp/gdp_usa.html
# За период в 43 года средний рост ВВП был равен:
# 1075.9*x^(43-1)=3580 x=1.029 (2.9%)
GDP_GROWTH = 0.03
# Доля военного бюджета в ВВП страны. В США, например 3.5%,
# Во время Второй мировой войны бюджеты армий доходили до 50-100% ВВП:
# http://aillarionov.livejournal.com/811219.html
GDP_ARMY = 0.2

# Далее идут переменные для распределения Гомпертца-Мейкхама:
# http://dic.academic.ru/dic.nsf/ruwiki/923652
# Можно ориентироваться на исследование популяции людей 20-го века:
# "Parametric models for life insurance mortality data: gompertz's law over time"
# Компонент Мейкхама, независимый от возраста риск (0.003 = 0.3% каждый год):
COMPONENT_A = 0.0005
# Коэффициент b:
COEFFICIENT_B = 0.000113
# Коэффициент c:
COEFFICIENT_C = 1.08

# Распределение полов.
#MALE_NAME = 'Жеребцы'
#MALE_PERCENT = 0.4
#FEMALE_NAME = 'Кобылки'
#FEMALE_PERCENT = 0.6
MALE_NAME = 'Жеребцы-единороги'
MALE_PERCENT = 0.4
FEMALE_NAME = 'Кобылки-единороги'
FEMALE_PERCENT = 0.6

# Армия (или профессия):
# Процент рекрутов: 0.25 — отборные; 0.25-0.5 — середнячки;
# 0.5-0.75 — кривые, косые; 0.75+ — глухие, слепые, убогие умом.
prof_percent = 0.5
# Профессиональный риск, изменение компонента Мейкхама:
# (0.01 = 1% риск смерти каждый год)
prof_hazard = 0.01
# Призывники обоих полов? 0 - нет; 1 - да
prof_male_switch = 1
prof_female_switch = 1
# Возраст призыва:
prof_age_apprentice = 10
# Возраст перехода в резервисты:
prof_age_expert = 20
# Возраст отставки:
prof_age_retiree = 80
prof_name_apprentice = 'Учащиеся чародеи'
prof_name_expert = 'Обученные чародеи'
prof_name_retiree = 'Пожилые чародеи'

## Армия (или профессия):
## Процент рекрутов: 0.25 — отборные; 0.25-0.5 — середнячки;
## 0.5-0.75 — кривые, косые; 0.75+ — глухие, слепые, убогие умом.
#prof_percent = 0.02
## Профессиональный риск, изменение компонента Мейкхама:
## (0.01 = 1% риск смерти каждый год)
#prof_hazard = 0.02
## Призывники обоих полов? 0 - нет; 1 - да
#prof_male_switch = 1
#prof_female_switch = 1
## Возраст призыва:
#prof_age_apprentice = 20
## Возраст перехода в резервисты:
#prof_age_expert = 40
## Возраст отставки:
#prof_age_retiree = 60
#prof_name_apprentice = 'Солдаты'
#prof_name_expert = 'Резервисты'
#prof_name_retiree = 'Отставники'


#-------------------------------------------------------------------------
# Список видов войск. Используется базой данных военной техники,
# Смотри параметр 'wpn_troops_type'.

# Для замены хорошо подойдут регулярные выражения, например в Vim'е:
# %s/'РВ'/'РВСН'/g — подправит всю базу данных. Кавычки важны.
dict_troops_types = {
        # Формат:
        # 'Вид_войск':процент,
        # https://www.myth-weavers.com/generate_town.php?do=town
        # https://dndtools.net/classes/sorcerer/
        'Чародеи':1,
        'Чародеи 1 cr 1 lvl':0.60,
        'Чародеи 1 cr 2 lvl':1 * 0.2,
        'Чародеи 1 cr 3 lvl':1 * (0.2 / 2),
        'Чародеи 2 cr 4 lvl':1 * (0.2 / 2 ** 2),
        'Чародеи 2 cr 5 lvl':1 * (0.2 / 2 ** 3),
        'Чародеи 3 cr 6 lvl':1 * (0.2 / 2 ** 4),
        'Чародеи 3 cr 7 lvl':1 * (0.2 / 2 ** 5),
        'Чародеи 4 cr 8 lvl':1 * (0.2 / 2 ** 6),
        'Чародеи 4 cr 9 lvl':1 * (0.2 / 2 ** 7),
        'Чародеи 5 cr 10 lvl':1 * (0.2 / 2 ** 8),
        'Чародеи 5 cr 11 lvl':1 * (0.2 / 2 ** 9),
        'Чародеи 6 cr 12 lvl':1 * (0.2 / 2 ** 10),
        'Чародеи 6 cr 13 lvl':1 * (0.2 / 2 ** 11),
        'Чародеи 7 cr 14 lvl':1 * (0.2 / 2 ** 12),
        'Чародеи 7 cr 15 lvl':1 * (0.2 / 2 ** 13),
        'Чародеи 8 cr 16 lvl':1 * (0.2 / 2 ** 14),
        'Чародеи 8 cr 17 lvl':1 * (0.2 / 2 ** 15),
        'Чародеи 9 cr 18 lvl':1 * (0.2 / 2 ** 16),
        'Чародеи 9 cr 19 lvl':1 * (0.2 / 2 ** 17),
        'Чародеи 9 cr 20 lvl':1 * (0.2 / 2 ** 18),
        #'Волшебники':0.01,
        #'Гвардия':0.1,
        #'Стража':0.9,
        # Военно-промышленный комплекс (боеприпасы):
        #'ВПК':1,
        ## Сухопутные войска:
        #'СВ':0.5,
        ## Ракетные войска и дальняя ПВО:
        #'РВ':0.1,
        ## Военно-воздушные войска:
        #'ВВС':0.15,
        ## Военно-морской флот:
        #'ВМФ':0.1,
        ## Инженерные войска:
        #'ИВ':0.15,
        }


#-------------------------------------------------------------------------
# База данных оружия. Двумерный массив.

# Дополняется блоками, без ограничений и очень легко. Пользуйтесь этим.
# Пожалуйста, пишите в строке 'wpn_name_comment' краткое описание оружия,
# а в строке 'wpn_cost_currency' точно указывайте валюту и год.
# История скажет вам спасибо.

# Для поиска данных можно использовать списки оружия из википедии, например:
    # https://ru.wikipedia.org/wiki/Список_оружия_и_военной_техники_сухопутных_войск_Российской_Федерации
    # https://en.wikipedia.org/wiki/Equipment_of_the_United_States_Armed_Forces
# Как ориентир, производство оружия во время Второй мировой войны:
    # https://ru.wikipedia.org/wiki/Военное_производство_во_время_Второй_мировой_войны
    # https://ru.wikipedia.org/wiki/Производство_бронетехники_в_СССР_во_время_Второй_мировой_войны
# Структура армий различный стран и периодов (кратко, pdf, en, wargame):
    # http://www.fireandfury.com/extra/ordersofbattle.shtml#CW
# Характеристики техники (кратко, неточно, en, wargame):
    # http://wargame-series.wikia.com/wiki/USSR
    # http://wargame-series.wikia.com/wiki/United_States
# Штаты частей и подразделений армии СССР (1970-1990 годы, подробно):
    # http://yv-gontar.io.ua/s204359/shtaty_tankovyh_motostrelkovyh_polkov_otdelnyh_batalonov_i_parashyutno-desantnyh_polkov
    # http://yv-gontar.io.ua/s204353/shtaty_artillerii_suhoputnyh_voysk_i_vdv
    # http://yv-gontar.io.ua/s204347/shtaty_pvo_msp_i_tp_sovetskoy_armii
# Вооружённые силы России, организация, штаты, вооружение (2015 год, подробно, но с ошибками):
    # http://www.milkavkaz.net/2015/12/vooruzhjonnye-sily-rossii.html
# Взгляды командования сухопутных войск США на реорганизацию боевых бригад (2016 год):
    # http://pentagonus.ru/publ/vzgljady_komandovanija_sukhoputnykh_vojsk_ssha_na_reorganizaciju_boevykh_brigad_2016/3-1-0-2675
# Военный бюджет США, закупки техники (2016 год):
    # http://pentagonus.ru/publ/proekt_voennogo_bjudzheta_ssha_na_2016_finansovyj_god_2015/8-1-0-2631
# Стоимость оружия (неточно, упрощённо, начало 2000-х):
    # http://monster-igstab.livejournal.com/42346.html
# И сравнение армий современных государств (en):
    # http://www.globalfirepower.com/countries-listing.asp

# Эквестрийские биты = доллары США 2015 года.

# Создаётся объединённый словарь — строки массива.
metadict_wpn = {}

## Выбирается первый из ключей — номер столбца.
#dict_wpn_key = 0
#dict_wpn = {
#        'wpn_name':'Бронетранспортёры',
#        # https://ru.wikipedia.org/wiki/БТР-70
#        'wpn_name_comment':'10-тонные колёсные и гусеничные БТР, вооружены пулемётом и АГС. Десант: 10 солдат; экипаж — двое.',
#        # Принадлежность к виду войск:
#        'wpn_troops_type':'СВ',
#        # Цена на мировом рынке оружия или стоимость производства:
#        # Для примера, «Бредли» стоит около 3.166 млн долларов:
#        # http://www.globalsecurity.org/military/systems/ground/m2-specs.htm
#        'wpn_cost':1000000,
#        'wpn_cost_currency':'Эквестрийские биты',
#        # Стоимость технического обслуживания в год, доля от стоимости машины:
#        'wpn_maintenance':0.01,
#        # Доля затрат на данный вид оружия в военном бюджете:
#        # Департамент обороны США тратит 19% бюджета на все закупки:
#        # https://upload.wikimedia.org/wikipedia/commons/6/67/US_DOD_budget_2014_RUS.png
#        'wpn_budget':0.006,
#        'wpn_name_new':'Бронетранспортёры новые',
#        'wpn_name_mid':'Бронетранспортёры устаревшие',
#        'wpn_name_old':'Бронетранспортёры под списание',
#        # Возраст потрёпанности:
#        'wpn_age_mid':10,
#        # Возраст старости:
#        'wpn_age_old':20,
#        # Переменные распределения Гомпертца-Мейкхама для оружия:
#        # Строка 'wpn_a':0.03 значит 3% вероятность потери в год.
#        # wpn_b и wpn_c корректируют вероятность по возрасту оружия,
#        # Чем выше эти параметры, тем быстрее растут потери.
#        'wpn_a':0.03,
#        'wpn_b':0.0002,
#        'wpn_c':1.4,
#        # Вооружение техники №1 (крупнокалиберный пулемёт):
#        'wpn_ammo_1_name':'Патроны 15x120',
#        # Один боекомплект:
#        'wpn_ammo_1_capacity':500,
#        # Максимум расхода боеприпасов в год:
#        'wpn_ammo_1_expense':10000,
#        # Вооружение техники №2 (малокалиберный пулемёт):
#        'wpn_ammo_2_name':'Патроны 6x48',
#        'wpn_ammo_2_capacity':2000,
#        'wpn_ammo_2_expense':10000,
#        # Вооружение техники №3 (автоматический гранатомёт):
#        'wpn_ammo_3_name':'Выстрелы АГС',
#        'wpn_ammo_3_capacity':400,
#        'wpn_ammo_3_expense':1200,
#        # Топливо/источник энергии (супермаховик 10 МДж/кг):
#        'wpn_fuel_name':'Маховики (МДж)',
#        # Разовый запас топлива/энергии, 1-тонный маховик:
#        'wpn_fuel_capacity':10000,
#        # Расход топлива на километр (максимум):
#        # 200 квт мощность, скорость 30 км/час по бездорожью.
#        'wpn_fuel_consumption':25,
#        # Годовой расход топлива (на 10 000 км, ресурс ходовой):
#        'wpn_fuel_expense':250000,
#        }
## Данные записываются в общий словарь, как столбец двумерного массива.
#metadict_wpn[dict_wpn_key] = dict_wpn
#
## Переход на новый столбец:
#dict_wpn_key = dict_wpn_key + 1
#dict_wpn = {
#        'wpn_name':'Боевые машины десанта',
#        # https://ru.wikipedia.org/wiki/БМД-2
#        'wpn_name_comment':'10-тонные гусеничные машины. Вооружены 30-мм автопушкой и ПТУРС. Десант — 9 солдат; экипаж — трое.',
#        'wpn_troops_type':'СВ',
#        'wpn_cost':3000000,
#        'wpn_maintenance':0.02,
#        'wpn_cost_currency':'Эквестрийские биты',
#        'wpn_budget':0.001,
#        'wpn_name_new':'Боевые машины десанта новые',
#        'wpn_name_mid':'Боевые машины десанта устаревшие',
#        'wpn_name_old':'Лёгкие плавающие танки под списание',
#        'wpn_age_mid':10,
#        'wpn_age_old':20,
#        'wpn_a':0.05,
#        'wpn_b':0.0004,
#        'wpn_c':1.4,
#        'wpn_ammo_1_name':'Снаряды 30x165',
#        'wpn_ammo_1_capacity':500,
#        'wpn_ammo_1_expense':2500,
#        'wpn_ammo_2_name':'Патроны 6x48',
#        'wpn_ammo_2_capacity':2000,
#        'wpn_ammo_2_expense':10000,
#        'wpn_ammo_3_name':'Управляемые ракеты',
#        'wpn_ammo_3_capacity':4,
#        'wpn_ammo_3_expense':12,
#        'wpn_fuel_name':'Маховики (МДж)',
#        'wpn_fuel_capacity':10000,
#        'wpn_fuel_consumption':25,
#        'wpn_fuel_expense':250000,
#        }
#metadict_wpn[dict_wpn_key] = dict_wpn
#
#-------------------------------------------------------------------------
# Внутренние переменные.

# Создаём рабочие переменные на основе данных из опций (для удобства):
year_real = YEAR_START
age_real = AGE_END
pop = POPULATION
fert = FERTILITY_RATE
mort = MORTALITY_RATE
a = COMPONENT_A
b = COEFFICIENT_B
c = COEFFICIENT_C


#-------------------------------------------------------------------------
# Функции, подпрограммы. Последующие вызывают предыдущие.

def population_size(year):
    """Вычисляем численность популяции.

    Рост популяции, это геометрическая прогрессия, например:
    100000*1.002^(100-1)=121872
    Начальная численность, годовой прирост, период в сто лет.
    Функция вычисляет исходную численность, зная конечную:
    121872*1.002^(1-100)=100000
    """
    population = POPULATION * ((FERTILITY_RATE - MORTALITY_RATE + 1) ** (-year))
    # Округляем число
    population = round (population)
    return population
 
def generation_size(year, percent):
    """Определяем численность поколения.

    Поколение, это процент от популяции, например, если рождаемость 0.02:
    121872*1.002^(1-100)*0.02=2000 (2% новорожденных в популяции)
    Точно так же можно определить число умерших, прирост населения, состав:
    121872*1.002^(1-100)*0.02*0.5=1000 (50% новорожденных мужского пола)
    """
    generation = round(population_size(year) * percent)
    return generation

def GDP_size(year):
    """ВВП страны в определённый год.

    Рост благосостояния, это та же геометрическая прогрессия:
    10000*1.03^(1-100)=536
    В данном случае от 536$ за столетие ВВП вырос до 10 000$
    """
    GDP_in_year = GDP_RATE * ((GDP_GROWTH + 1) ** (-year)) * population_size(year)
    GDP_in_year = round (GDP_in_year)
    return GDP_in_year

def gompertz_distribution(a, b, c, age):
    """Распределение Гомпертца. Риск смерти в зависимости от возраста.

    Распределение Гомпертца-Мейкхама неплохо работает в
    демографических расчётах для самых разных популяций.
    Единственный недостаток — оно склонно занижать
    смертность в начале и завышать в конце (экспонента, что поделать).
    Для популяции людей даёт хорошие результаты в диапазоне — 30-70 лет.
    Формула: p=a+b*(c^x)
    Где:
    p — вероятность смерти в процентах
    a — независимый от возраста риск (0.002%)
    b — коэффициент 2 (0.000350)
    c — коэффициент 3 (1.08)
    x — возраст в годах
    Коэффициенты подобраны с учётом исследования:
    "Parametric models for life insurance mortality data: gompertz's law over time".
    """
    chance_of_dying = a + b * (c ** age)
    # Проверка. Если получилось больше 1, значит 100% смерть.
    if (chance_of_dying > 1):
        chance_of_dying = 1
    return chance_of_dying


def generation_alive(generation, a, b, c, age_real):
    """Число живых в поколении.

    Каждый год умирает некий процент из поколения.
    Этот цикл вычисляет точное число живых в определённый год.
    """
    # Задаём рабочую переменную для цикла:
    age = 0
    # Из численности поколения вычитаем число погибших в первый год:
    generation_survivors = generation - \
            generation * \
            gompertz_distribution(a, b , c, age)
    # Далее это вычитание продолжается циклично.
    while (age <= age_real):
        age = age + 1
        generation_survivors = generation_survivors - \
                generation_survivors * \
                gompertz_distribution(a, b, c, age)
        # Проверка. Если число выживших уходит в минус, значит все мертвы.
        if (generation_survivors <= 0):
            generation_survivors = 0
            break
    # Округляем число
    generation_survivors = round(generation_survivors)
    return generation_survivors


def generation_profession(prof_percent, prof_hazard):
    """Число представителей определённой профессии, с учётом риска."""
    prof_number = 0
    if (prof_male_switch != 0):
        # Берём из словаря численность живых в нужном поколении
        # и пропускаем через ещё один цикл, чтобы учесть риск профессии.
        prof_number = prof_number + \
                generation_alive(dict_population['generation_alive'] * MALE_PERCENT * prof_percent,
                        # Отчёт начинается с возраста профессии.
                        prof_hazard, b, c, age_real - prof_age_apprentice)
    if (prof_female_switch != 0):
        prof_number = prof_number + \
                generation_alive(dict_population['generation_alive'] * FEMALE_PERCENT * prof_percent,
                        prof_hazard, b, c, age_real - prof_age_apprentice)
    return prof_number



#-------------------------------------------------------------------------
# Главный цикл скрипта.

# Эта база данных станет индексом для словарей.
metadict = {}

# Рабочие переменные:
progression_year = 0
year = 0

# Цикл перебирает годы, уходя в прошлое,
# пока возраст популяции не сравняется с возрастом конца исследования.
while (progression_year <= AGE_END):
    # Определяем текущий год (для прогрессии роста населения).
    year = AGE_END - progression_year
    year_real = YEAR_START - year

    # Создаём основной словарь (базу данных) для этого возраста:
    dict_population = {
            'age_real':age_real,
            'year_real':year_real,
            'population_size':population_size(year),
            'generation_size':generation_size(year, fert),
            'generation_alive':generation_alive(generation_size(year, fert), a, b, c, age_real),
            'GDP_size':GDP_size(year)
            }

    # Определяем численность призывников:
    prof_number_apprentice = 0
    if (prof_age_apprentice <= age_real < prof_age_expert):
        prof_number_apprentice = prof_number_apprentice + \
                generation_profession(prof_percent, prof_hazard)
    # Определяем численность резервистов:
    prof_number_expert = 0
    if (prof_age_expert <= age_real < prof_age_retiree):
        prof_number_expert = prof_number_expert + \
                generation_profession(prof_percent, prof_hazard)
    # И, наконец, пенсионеры:
    prof_number_retiree = 0
    if (prof_age_retiree <= age_real):
        prof_number_retiree = prof_number_retiree + \
                generation_profession(prof_percent, prof_hazard)

    # Создаём временный словарь гендеров и профессий:
    dict_demography = {
            MALE_NAME:generation_alive(generation_size(year, fert * MALE_PERCENT), a, b, c, age_real),
            FEMALE_NAME:generation_alive(generation_size(year, fert * FEMALE_PERCENT), a, b, c, age_real),
            prof_name_apprentice:prof_number_apprentice,
            prof_name_expert:prof_number_expert,
            prof_name_retiree:prof_number_retiree,
            }
 
    # Дополняем первый словарь вторым
    dict_population.update(dict_demography)
    # Создаём объединённый словарь,
    # он будет пополняться при каждом проходе цикла:
    metadict[age_real] = dict_population

    # Завершение главного цикла:
    progression_year = progression_year + 1
    age_real = age_real - 1


#-------------------------------------------------------------------------
# Модуль. Вычисляет производство и количество оружия в войсках.

# Произведённое оружие:
metadict_equipment_create = {}
# Уцелевшее оружие:
metadict_equipment_alive = {}

# Исследование объединённого словаря. Создание баз данных оружия.
# Перебираем вложенные словари начиная с последнего:
for meta_key in sorted(metadict.keys(), reverse=True):
    # Временный словарь вооружений (за один год):
    dict_equipment_create = {}
    dict_equipment_alive = {}
    # Перебираем опции из базы данных вооружений:
    for wpn_key in sorted(metadict_wpn.keys()):
        # Количество созданных машин, это бюджет на них, делённый на стоимость.
        wpn_create = round(metadict[meta_key]['GDP_size'] * GDP_ARMY * \
                metadict_wpn[wpn_key]['wpn_budget'] / metadict_wpn[wpn_key]['wpn_cost'])
        wpn_alive = generation_alive(wpn_create,
                metadict_wpn[wpn_key]['wpn_a'],
                metadict_wpn[wpn_key]['wpn_b'],
                metadict_wpn[wpn_key]['wpn_c'],
                metadict[meta_key]['age_real'])
        # Создаём временный словарь:
        dict_equipment_create[metadict_wpn[wpn_key]['wpn_name']] = wpn_create
        dict_equipment_alive[metadict_wpn[wpn_key]['wpn_name']] = wpn_alive
    # Объединяем временные словари в базу данных:
    metadict_equipment_create[meta_key] = dict_equipment_create
    metadict_equipment_alive[meta_key] = dict_equipment_alive

# Далее, вычисляем общее число вооружений на складах:
dict_equipment_all = {}
for wpn_key in sorted(metadict_wpn.keys()):
    equipment_all = 0
    for meta_key in sorted(metadict_equipment_alive.keys()):
        equipment_all = equipment_all + metadict_equipment_alive[meta_key][metadict_wpn[wpn_key]['wpn_name']]
    dict_equipment_all[metadict_wpn[wpn_key]['wpn_name']] = equipment_all


#-------------------------------------------------------------------------
# Вывод результатов.

# Вывод по годам:
for meta_key in sorted(metadict.keys(), reverse=True):
    # Вывод данных о населении:
    print('Год:', metadict[meta_key]['year_real'],
            'Возраст:', metadict[meta_key]['age_real'],
            'Родившиеся:', metadict[meta_key]['generation_size'],
            'Живые:', metadict[meta_key]['generation_alive'])
    print(MALE_NAME, metadict[meta_key][MALE_NAME],
            FEMALE_NAME, metadict[meta_key][FEMALE_NAME])
    # Вывод данных о солдатах:
    if (prof_age_apprentice <= metadict[meta_key]['age_real'] < prof_age_expert):
        print(prof_name_apprentice, metadict[meta_key][prof_name_apprentice])
    if (prof_age_expert <= metadict[meta_key]['age_real'] < prof_age_retiree):
        print(prof_name_expert, metadict[meta_key][prof_name_expert])
    if (prof_age_retiree <= metadict[meta_key]['age_real']):
        print(prof_name_retiree, metadict[meta_key][prof_name_retiree])
    # Вывод данных о вооружении:
    for wpn_key in sorted(metadict_wpn.keys()):
        # Отмена вывода, если число машинок по нулям.
        if (metadict_equipment_alive[meta_key][metadict_wpn[wpn_key]['wpn_name']] != 0):
            if (metadict[meta_key]['age_real'] < metadict_wpn[wpn_key]['wpn_age_mid']):
                print(metadict_wpn[wpn_key]['wpn_name_new'],
                        ' (Создано: ',
                        # Обращение аж к двум словарям, одно вложено в другое.
                        metadict_equipment_create[meta_key][metadict_wpn[wpn_key]['wpn_name']], ')',
                        ' Уцелело: ',
                        metadict_equipment_alive[meta_key][metadict_wpn[wpn_key]['wpn_name']], sep='')
            if (metadict_wpn[wpn_key]['wpn_age_mid'] <= metadict[meta_key]['age_real'] <
                    metadict_wpn[wpn_key]['wpn_age_old']):
                print(metadict_wpn[wpn_key]['wpn_name_mid'],
                        ' (Создано: ',
                        metadict_equipment_create[meta_key][metadict_wpn[wpn_key]['wpn_name']], ')',
                        ' Уцелело: ',
                        metadict_equipment_alive[meta_key][metadict_wpn[wpn_key]['wpn_name']], sep='')
            if (metadict_wpn[wpn_key]['wpn_age_old'] <= metadict[meta_key]['age_real']):
                print(metadict_wpn[wpn_key]['wpn_name_old'],
                        ' (Создано: ',
                        metadict_equipment_create[meta_key][metadict_wpn[wpn_key]['wpn_name']], ')',
                        ' Уцелело: ',
                        metadict_equipment_alive[meta_key][metadict_wpn[wpn_key]['wpn_name']], sep='')
    print('------------------------------------------------------------')

# Подведение итогов:
print('Ожидаемая численность:', POPULATION)
population_alive = 0
generations_all = 0
army_soldiers= 0
army_reservists = 0
for meta_key in sorted(metadict.keys()):
    population_alive = population_alive + metadict[meta_key]['generation_alive']
    generations_all = generations_all + metadict[meta_key]['generation_size']
    army_soldiers = army_soldiers + metadict[meta_key][prof_name_apprentice]
    army_reservists = army_reservists + metadict[meta_key][prof_name_expert]
print('Численность популяции:', population_alive)
print('Численность поколений:', generations_all)
print(prof_name_apprentice, 'и', prof_name_expert, 'по кругам магии и уровням:')
for troop_key in sorted(dict_troops_types.keys()):
    print('    ', troop_key, ' (', round(dict_troops_types[troop_key] * 100), '%) ',
            round(army_soldiers * dict_troops_types[troop_key]),
            ' — ', round((army_reservists) * dict_troops_types[troop_key]), sep='')
print('Смерти от болезней (в год):', round(population_alive * MORTALITY_RATE),
        ' (', round(POPULATION * MORTALITY_RATE / (population_alive) * 100),
        '% от численности населения)', sep='')
print('Несчастные случаи (в год): ', round(population_alive * COMPONENT_A),
        ' (', round(POPULATION * COMPONENT_A / (population_alive * MORTALITY_RATE) * 100),
        '% от числа смертей)', sep='')
print('Военные потери: ', round(army_soldiers * prof_hazard),
        ' (', round(army_soldiers * prof_hazard / (population_alive * COMPONENT_A) * 100),
        '% от несчастных случаев)', sep='')
print('------------------------------------------------------------')


#-------------------------------------------------------------------------
# И наконец, суммируем всё вооружение, вычисляем отношение единиц оружия к числу солдат,
# потребность армии в боеприпасаха, а также суммарный бюджет на вооружения и бюджеты по видам войск:

budget_percent = 0
budget_troops_percent = 0
# База данных потребностей в боеприпасах:
ammunition_needs = {}
# Названия боеприпасов превращаем в ключи базы данных:
for wpn_key in sorted(metadict_wpn.keys()):
    if metadict_wpn[wpn_key].get('wpn_ammo_1_name'):
        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_1_name']] = 0
    if metadict_wpn[wpn_key].get('wpn_ammo_2_name'):
        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_2_name']] = 0
    if metadict_wpn[wpn_key].get('wpn_ammo_3_name'):
        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_3_name']] = 0
    if metadict_wpn[wpn_key].get('wpn_ammo_4_name'):
        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_4_name']] = 0
    if metadict_wpn[wpn_key].get('wpn_ammo_5_name'):
        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_5_name']] = 0
    if metadict_wpn[wpn_key].get('wpn_ammo_6_name'):
        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_6_name']] = 0
    if metadict_wpn[wpn_key].get('wpn_ammo_7_name'):
        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_7_name']] = 0
    if metadict_wpn[wpn_key].get('wpn_ammo_8_name'):
        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_8_name']] = 0
    if metadict_wpn[wpn_key].get('wpn_ammo_9_name'):
        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_9_name']] = 0
    if metadict_wpn[wpn_key].get('wpn_fuel_name'):
        ammunition_needs[metadict_wpn[wpn_key]['wpn_fuel_name']] = 0
# База данных бюджета по видам войск:
# Создаётся рабочий словарь, обнуляются значения:
budget_troops_types = {}
budget_troops_types.update(dict_troops_types)
for troop_key in budget_troops_types:
    budget_troops_types[troop_key] = 0
# База данных стоимости обслуживания по видам войск:
# Создаётся рабочий словарь, обнуляются значения:
maintenance_troops_types = {}
maintenance_troops_types.update(dict_troops_types)
for troop_key in budget_troops_types:
    maintenance_troops_types[troop_key] = 0

## Перебор столбцов в базе данных оружия:
#for wpn_key in sorted(metadict_wpn.keys()):
#    equipment_all = 0
#    # Затем перебор по годам:
#    for meta_key in sorted(metadict_equipment_alive.keys()):
#        equipment_all = equipment_all + metadict_equipment_alive[meta_key][metadict_wpn[wpn_key]['wpn_name']]
#    # Если есть проект, значит есть оружие, хотя бы один экземпляр:
#    if (equipment_all < 1):
#        equipment_all = 1
#        print('Не хватает бюджета на',metadict_wpn[wpn_key]['wpn_name'])
#    # Вывод суммы оружия, сохранившегося за все годы:
#    print(metadict_wpn[wpn_key]['wpn_troops_type'], metadict_wpn[wpn_key]['wpn_name'], '—' , equipment_all, end=' ')
#    # Вывод отношения числа вооружений к числу солдат определённых видов войск:
#    army_type_percent = dict_troops_types[metadict_wpn[wpn_key]['wpn_troops_type']]
#    print('на', round(army_soldiers * army_type_percent / equipment_all),
#            prof_name_apprentice, metadict_wpn[wpn_key]['wpn_troops_type'],
#            'или на', round((army_reservists + army_soldiers) * army_type_percent / equipment_all),
#            prof_name_apprentice, '+',
#            prof_name_expert, metadict_wpn[wpn_key]['wpn_troops_type'])
#    # Вывод описания вооружения:
#    print('    ', metadict_wpn[wpn_key]['wpn_name_comment'])
#    # Подсчитываем, сколько оружия создано за год:
#    wpn_create = round(GDP_size(0) * GDP_ARMY * \
#                metadict_wpn[wpn_key]['wpn_budget'] / metadict_wpn[wpn_key]['wpn_cost'])
#    # Расходы на проект:
#    print('        Расходы: ',
#            round(metadict_wpn[wpn_key]['wpn_budget'] * 100, 3),'% бюджета ',
#            '(', metadict_wpn[wpn_key]['wpn_cost'] * wpn_create / (10 ** 9),
#            ' млрд ', metadict_wpn[wpn_key]['wpn_cost_currency'], ') ', sep='')
#    # Подсчитываем потери (без учёта старения оружия):
#    print('        Создано:', wpn_create)
#    print('        Потери:', round(wpn_create * metadict_wpn[wpn_key]['wpn_a'] + \
#            equipment_all * metadict_wpn[wpn_key]['wpn_a']))
#    print('        ---')
#    # Считаем потребность в боеприпасах (максимум 9 видов оружия) и топливо:
#    if metadict_wpn[wpn_key].get('wpn_ammo_1_name'):
#        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_1_name']] = \
#                ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_1_name']] + \
#                metadict_wpn[wpn_key]['wpn_ammo_1_expense'] * equipment_all
#    if metadict_wpn[wpn_key].get('wpn_ammo_2_name'):
#        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_2_name']] = \
#                ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_2_name']] + \
#                metadict_wpn[wpn_key]['wpn_ammo_2_expense'] * equipment_all
#    if metadict_wpn[wpn_key].get('wpn_ammo_3_name'):
#        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_3_name']] = \
#                ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_3_name']] + \
#                metadict_wpn[wpn_key]['wpn_ammo_3_expense'] * equipment_all
#    if metadict_wpn[wpn_key].get('wpn_ammo_4_name'):
#        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_4_name']] = \
#                ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_4_name']] + \
#                metadict_wpn[wpn_key]['wpn_ammo_4_expense'] * equipment_all
#    if metadict_wpn[wpn_key].get('wpn_ammo_5_name'):
#        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_5_name']] = \
#                ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_5_name']] + \
#                metadict_wpn[wpn_key]['wpn_ammo_5_expense'] * equipment_all
#    if metadict_wpn[wpn_key].get('wpn_ammo_6_name'):
#        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_6_name']] = \
#                ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_6_name']] + \
#                metadict_wpn[wpn_key]['wpn_ammo_6_expense'] * equipment_all
#    if metadict_wpn[wpn_key].get('wpn_ammo_7_name'):
#        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_7_name']] = \
#                ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_7_name']] + \
#                metadict_wpn[wpn_key]['wpn_ammo_7_expense'] * equipment_all
#    if metadict_wpn[wpn_key].get('wpn_ammo_8_name'):
#        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_8_name']] = \
#                ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_8_name']] + \
#                metadict_wpn[wpn_key]['wpn_ammo_8_expense'] * equipment_all
#    if metadict_wpn[wpn_key].get('wpn_ammo_9_name'):
#        ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_9_name']] = \
#                ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_9_name']] + \
#                metadict_wpn[wpn_key]['wpn_ammo_9_expense'] * equipment_all
#    if metadict_wpn[wpn_key].get('wpn_fuel_name'):
#        ammunition_needs[metadict_wpn[wpn_key]['wpn_fuel_name']] = \
#                ammunition_needs[metadict_wpn[wpn_key]['wpn_fuel_name']] + \
#                metadict_wpn[wpn_key]['wpn_fuel_expense'] * equipment_all
#    # Считаем общий бюджет и бюджет по родам войск:
#    budget_percent = budget_percent + metadict_wpn[wpn_key]['wpn_budget']
#    for troop_key in budget_troops_types:
#        if troop_key == metadict_wpn[wpn_key]['wpn_troops_type']:
#            budget_troops_types[troop_key] = budget_troops_types[troop_key] + \
#                    metadict_wpn[wpn_key]['wpn_budget'] * 100
#    # Считаем расходы на обслуживание данного вида оружия:
#    # Стоимость оружия * процент обслуживания * штук на складах
#    # Если строка 'wpn_maintenance' не указана, тогда обслуживание бесплатно
#    wpn_maintenance_all = metadict_wpn[wpn_key]['wpn_cost'] * \
#            metadict_wpn.get(wpn_key, 0).get('wpn_maintenance', 0)  * \
#            dict_equipment_all.get(metadict_wpn[wpn_key]['wpn_name'])
#    # Теперь распределяем расходы на обслуживание по родам войск:
#    for troop_key in maintenance_troops_types:
#        if troop_key == metadict_wpn[wpn_key]['wpn_troops_type']:
#            maintenance_troops_types[troop_key] = maintenance_troops_types[troop_key] + \
#                    wpn_maintenance_all
#
## Сумма бюджета всех проектов из базы данных оружия:
#print('Расходы военного бюджета на закупки и производство:')
#for troop_key in sorted(budget_troops_types.keys()):
#    print('    ', troop_key, ' (', round(dict_troops_types[troop_key] * 100), '%)',
#            ' — ', round(budget_troops_types[troop_key], 2), '%', sep='')
#print('Использовано ', round(budget_percent * 100, 2), '% бюджета армии',
#        ' (или ', round(GDP_ARMY * budget_percent * 100, 2), '% ВВП страны)',
#        sep='')
#print('        ---')
#
## Расходы на обслуживание оружия по видам войск:
#maintenance_percent_sum = 0
#print('Расходы военного бюджета на техническое обслуживание:')
#for troop_key in sorted(maintenance_troops_types.keys()):
#    maintenance_percent = maintenance_troops_types[troop_key] / (GDP_size(0) * GDP_ARMY)
#    maintenance_percent_sum = maintenance_percent_sum + maintenance_percent
#    print('    ', troop_key, ' (', round(dict_troops_types[troop_key] * 100), '%)',
#            ' — ', round(maintenance_percent * 100, 2), '%', sep='')
#print('Использовано ', round(maintenance_percent_sum * 100, 2), '% бюджета армии',
#        ' (или ', round(maintenance_percent_sum * GDP_ARMY * 100, 2), '% ВВП страны)',
#        sep='')
#print('        ---')
#
## Соотношение производства боеприпасов и потребности в них:
#print('Боеприпасы на складах (на год войны):')
#for ammo_key in sorted(ammunition_needs.keys()):
#    # (ammo_key, 0) — значит, если нет ключа, брать ноль.
#    print('   ', ammo_key, ' — ', dict_equipment_all.get(ammo_key, 0), ' (',
#            round(dict_equipment_all.get(ammo_key, ammunition_needs[ammo_key]) / \
#                    ammunition_needs[ammo_key] * 100), '%)', sep='')

#----
# Распределение по возрастам:

dict_population_ages = {}
dict_population_ages['0'] = 0
dict_population_ages['1-10'] = 0
dict_population_ages['11-20'] = 0
dict_population_ages['21-30'] = 0
dict_population_ages['31-40'] = 0
dict_population_ages['41-50'] = 0
dict_population_ages['51-60'] = 0
dict_population_ages['61-70'] = 0
dict_population_ages['71-80'] = 0
dict_population_ages['81-90'] = 0
dict_population_ages['91-100'] = 0
dict_population_ages['101-110'] = 0
dict_population_ages['111-120'] = 0
for meta_key in sorted(metadict.keys()):
    if (metadict[meta_key]['age_real'] == 0):
        dict_population_ages['0'] = metadict[meta_key]['generation_alive']
    elif (0 < metadict[meta_key]['age_real'] <= 10):
        dict_population_ages['1-10'] = dict_population_ages['1-10'] + metadict[meta_key]['generation_alive']
    elif (10 < metadict[meta_key]['age_real'] <= 20):
        dict_population_ages['11-20'] = dict_population_ages['11-20'] + \
                metadict[meta_key]['generation_alive']
    elif (20 < metadict[meta_key]['age_real'] <= 30):
        dict_population_ages['21-30'] = dict_population_ages['21-30'] + \
                metadict[meta_key]['generation_alive']
    elif (30 < metadict[meta_key]['age_real'] <= 40):
        dict_population_ages['31-40'] = dict_population_ages['31-40'] + \
                metadict[meta_key]['generation_alive']
    elif (40 < metadict[meta_key]['age_real'] <= 50):
        dict_population_ages['41-50'] = dict_population_ages['41-50'] + \
                metadict[meta_key]['generation_alive']
    elif (50 < metadict[meta_key]['age_real'] <= 60):
        dict_population_ages['51-60'] = dict_population_ages['51-60'] + \
                metadict[meta_key]['generation_alive']
    elif (60 < metadict[meta_key]['age_real'] <= 70):
        dict_population_ages['61-70'] = dict_population_ages['61-70'] + \
                metadict[meta_key]['generation_alive']
    elif (70 < metadict[meta_key]['age_real'] <= 80):
        dict_population_ages['71-80'] = dict_population_ages['71-80'] + \
                metadict[meta_key]['generation_alive']
    elif (80 < metadict[meta_key]['age_real'] <= 90):
        dict_population_ages['81-90'] = dict_population_ages['81-90'] + \
                metadict[meta_key]['generation_alive']
    elif (90 < metadict[meta_key]['age_real'] <= 100):
        dict_population_ages['91-100'] = dict_population_ages['91-100'] + \
                metadict[meta_key]['generation_alive']
    elif (100 < metadict[meta_key]['age_real'] <= 110):
        dict_population_ages['101-110'] = dict_population_ages['101-110'] + \
                metadict[meta_key]['generation_alive']
    elif (110 < metadict[meta_key]['age_real'] <= 120):
        dict_population_ages['111-120'] = dict_population_ages['111-120'] + \
                metadict[meta_key]['generation_alive']

population_test = 0
print('Распределение населения по возрастам:')
for key, population in dict_population_ages.items():
    population_part = population / population_alive
    #population_test = population_test + population_part
    print(key, round(population_part, 5))
