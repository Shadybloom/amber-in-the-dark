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
#POPULATION = 22000000
#POPULATION = 2000000
#POPULATION = 3700000
POPULATION = 10575
#POPULATION = 10000
#POPULATION = 1639
# Уровень рождаемости (например: 0.03 значит 3%
# или 30 новорожденных на 1000 населения в год):
FERTILITY_RATE = 0.015
# Уровень смертности, аналогично:
MORTALITY_RATE = 0.012

# Переменные для расчёта военной экономики:
# ВВП на душу населения:
# https://ru.wikipedia.org/wiki/Список_стран_по_ВВП_(ППС)_на_душу_населения
# Российская Империя 1910 года -- 125 рублей/человека,
# При этом средние доходы крестьян -- 40 рублей/год на домохозяйство
GDP_RATE = 125
# Годовой рост ВВП (без инфляции):
# Для примера, данные по росту ВВП США 1970-2013 годы:
# http://www.be5.biz/makroekonomika/gdp/gdp_usa.html
# За период в 43 года средний рост ВВП был равен:
# 1075.9*x^(43-1)=3580 x=1.029 (2.9%)
GDP_GROWTH = 0.01
# Доля военного бюджета в ВВП страны. В США, например 3.5%,
# Во время Второй мировой войны бюджеты армий доходили до 50-100% ВВП:
# http://aillarionov.livejournal.com/811219.html
GDP_ARMY = 0.1

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

# Младенческая смертность (записывается как 0.2 -- обозначает 20%). Прибавляется к риску за первый год жизни:
# https://ru.wikipedia.org/wiki/Список_стран_по_уровню_младенческой_смертности
# http://vln.by/node/213
# https://skaramanga-1972.livejournal.com/26904.html
A_INFANT_MORTALITY_CORRECTION=0.005

# Возрастное распределение, используется для расчётов социальных слоёв:
# Возраст перехода дети>подростки.
AGE_TEENAGER=6
# Возраст перехода подростки>взрослые.
AGE_ADULT=15
# Возраст стариков. С этого возраста начинает работать C_OLD_AGE_MORTALITY_CORRECTION.
AGE_OLDER=50
# Минимальный возраст деторождения (используется в вычислении суммарного коэффициента рождаемости):
AGE_FERTILE_MIN=15
# Максимальный возраст деторождения (менопауза):
AGE_FERTILE_MAX=40

# Распределение полов.
MALE_NAME = 'Жеребцы'
MALE_PERCENT = 0.4
FEMALE_NAME = 'Кобылки'
FEMALE_PERCENT = 0.6
#MALE_NAME = 'Жеребцы-единороги'
#MALE_PERCENT = 0.42
#FEMALE_NAME = 'Кобылки-единороги'
#FEMALE_PERCENT = 0.58

# Школьники
# Армия (или профессия):
# Процент рекрутов: 0.25 — отборные; 0.25-0.5 — середнячки;
# 0.5-0.75 — кривые, косые; 0.75+ — глухие, слепые, убогие умом.
prof_percent = 0.85
# Профессиональный риск, изменение компонента Мейкхама:
# (0.01 = 1% риск смерти каждый год)
prof_hazard = 0.000
# Призывники обоих полов? 0 - нет; 1 - да
prof_male_switch = 1
prof_female_switch = 1
# Возраст призыва:
prof_age_apprentice = 7
# Возраст перехода в резервисты:
prof_age_expert = 10
# Возраст отставки:
prof_age_retiree = 100
prof_name_apprentice = 'Учащиеся'
prof_name_expert = 'Грамотные'
prof_name_retiree = 'Грамотные-старики'

## Учёные
## Армия (или профессия):
## Процент рекрутов: 0.25 — отборные; 0.25-0.5 — середнячки;
## 0.5-0.75 — кривые, косые; 0.75+ — глухие, слепые, убогие умом.
#prof_percent = 0.01
## Профессиональный риск, изменение компонента Мейкхама:
## (0.01 = 1% риск смерти каждый год)
#prof_hazard = 0.001
## Призывники обоих полов? 0 - нет; 1 - да
#prof_male_switch = 1
#prof_female_switch = 1
## Возраст призыва:
#prof_age_apprentice = 20
## Возраст перехода в резервисты:
#prof_age_expert = 26
## Возраст отставки:
#prof_age_retiree = 60
#prof_name_apprentice = 'Студенты'
#prof_name_expert = 'Учёные'
#prof_name_retiree = 'Отставники'

## Чародеи
## Армия (или профессия):
## Процент рекрутов: 0.25 — отборные; 0.25-0.5 — середнячки;
## 0.5-0.75 — кривые, косые; 0.75+ — глухие, слепые, убогие умом.
#prof_percent = 0.1
## Профессиональный риск, изменение компонента Мейкхама:
## (0.01 = 1% риск смерти каждый год)
#prof_hazard = 0.01
## Призывники обоих полов? 0 - нет; 1 - да
#prof_male_switch = 1
#prof_female_switch = 1
## Возраст призыва:
#prof_age_apprentice = 10
## Возраст перехода в резервисты:
#prof_age_expert = 20
## Возраст отставки:
#prof_age_retiree = 80
#prof_name_apprentice = 'Учащиеся чародеи'
#prof_name_expert = 'Обученные чародеи'
#prof_name_retiree = 'Пожилые чародеи'

## Гвардия
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
        'Грамотные':1,
        #'Учёные':1,
        #'Учёные-врачи':0.2,
        #'Чародеи 1 cr 1 lvl':0.60,
        #'Чародеи 1 cr 2 lvl':1 * 0.2,
        #'Чародеи 1 cr 3 lvl':1 * (0.2 / 2),
        #'Чародеи 2 cr 4 lvl':1 * (0.2 / 2 ** 2),
        #'Чародеи 2 cr 5 lvl':1 * (0.2 / 2 ** 3),
        #'Чародеи 3 cr 6 lvl':1 * (0.2 / 2 ** 4),
        #'Чародеи 3 cr 7 lvl':1 * (0.2 / 2 ** 5),
        #'Чародеи 4 cr 8 lvl':1 * (0.2 / 2 ** 6),
        #'Чародеи 4 cr 9 lvl':1 * (0.2 / 2 ** 7),
        #'Чародеи 5 cr 10 lvl':1 * (0.2 / 2 ** 8),
        #'Чародеи 5 cr 11 lvl':1 * (0.2 / 2 ** 9),
        #'Чародеи 6 cr 12 lvl':1 * (0.2 / 2 ** 10),
        #'Чародеи 6 cr 13 lvl':1 * (0.2 / 2 ** 11),
        #'Чародеи 7 cr 14 lvl':1 * (0.2 / 2 ** 12),
        #'Чародеи 7 cr 15 lvl':1 * (0.2 / 2 ** 13),
        #'Чародеи 8 cr 16 lvl':1 * (0.2 / 2 ** 14),
        #'Чародеи 8 cr 17 lvl':1 * (0.2 / 2 ** 15),
        #'Чародеи 9 cr 18 lvl':1 * (0.2 / 2 ** 16),
        #'Чародеи 9 cr 19 lvl':1 * (0.2 / 2 ** 17),
        #'Чародеи 9 cr 20 lvl':1 * (0.2 / 2 ** 18),
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

# Выбирается первый из ключей — номер столбца.
dict_wpn_key = 0
dict_wpn = {
        'wpn_name':'Публикации (всего)',
        'wpn_troops_type':'Учёные',
        # Распределение книг, вышедших в 1913 г., по видам изданий и содержанию
        # Источник: Статистика произведений печати, вышедших в России в 1913 г. Пг., 1915. С. 5-7.
        # http://www.protown.ru/information/hide/6631.html
        # Всего 33 000 названий (3546 книг/тираж)
        # Всего 37 430 191 рублей (1134 рубля/тираж)
        # Всего 117 006 227 книг (0.32 рубля/книга)
        'wpn_cost':1134,
        'wpn_cost_currency':'Рубль 1913 года',
        # Стоимость технического обслуживания в год, доля от стоимости проекта:
        'wpn_maintenance':0.01,
        # Доля затрат на проект от "военного" бюджета:
        # В Эквестрии 22 млн. пони, 500 публикаций на миллион -- 11 000 публикаций/год
        # Новые публикации в год на 1 млн. жителей.
            # Россия 1913 год -- 181
            # Россия 1893 год -- 65
            # Германия 1900 -- 500
            # Германия 1850 -- 480
            # Англия 1800 -- 250
            # Numbers of new book-titles published per 1 million inhabitants
            # https://ourworldindata.org/books
            # https://en.wikipedia.org/wiki/Global_spread_of_the_printing_press
            # https://en.wikipedia.org/wiki/Incunable
        'wpn_budget':0.05,
        'wpn_name_new':'Публикации текущего века',
        'wpn_name_mid':'Публикации коллекционные',
        'wpn_name_old':'Публикации исторические',
        # Возраст потрёпанности:
        'wpn_age_mid':100,
        # Возраст старости:
        'wpn_age_old':200,
        # Переменные распределения Гомпертца-Мейкхама для оружия:
        # Строка 'wpn_a':0.03 значит 3% вероятность потери в год.
        # wpn_b и wpn_c корректируют вероятность по возрасту оружия,
        # Чем выше эти параметры, тем быстрее растут потери.
        #'wpn_a':0.03,
        #'wpn_b':0.0002,
        #'wpn_c':1.4,
        'wpn_a':0.001,
        'wpn_b':0.000113,
        'wpn_c':1.00,
        }
# Данные записываются в общий словарь, как столбец двумерного массива.
metadict_wpn[dict_wpn_key] = dict_wpn

# Переход на новый столбец:
dict_wpn_key = dict_wpn_key + 1
dict_wpn = {
        # Издано и продано:
        # Россия 2013 года -- 2.72 книг/человека
        # Соединённые штаты 2013 года -- 2.68 книг/человека
        'wpn_name':'Книги (всего)',
        'wpn_troops_type':'Грамотные',
        'wpn_cost':0.32,
        'wpn_cost_currency':'Рубль 1913 года',
        'wpn_maintenance':0.001,
        'wpn_budget':0.05,
        'wpn_name_new':'Книги текущего века',
        'wpn_name_mid':'Книги коллекционные',
        'wpn_name_old':'Книги музейные',
        'wpn_age_mid':100,
        'wpn_age_old':200,
        # 10% риск потери книги каждый год, снижение риска на 0.1% каждый год.
        'wpn_a_correction':0.001,
        'wpn_a':0.1,
        'wpn_b':0.000113,
        'wpn_c':1.02,
        }
metadict_wpn[dict_wpn_key] = dict_wpn

dict_wpn_key = dict_wpn_key + 1
dict_wpn = {
        # Всего 37 430 191 рублей (1134 рубля/тираж)
        # | №   | содержание             | названий   | тираж      | цена тиража | цена книги | доля назван.
        # | --- | ---------------------- | ---------- | ---------- | ----------- | ---------  | ------------
        # |  1. | Учебные пособия        | 2761       | 22 556 928 | 9 768 063   | 0.433      | 0.084
        'wpn_name':'Учебные пособия',
        'wpn_troops_type':'Грамотные',
        'wpn_cost':0.433,
        'wpn_cost_currency':'Рубль 1913 года',
        'wpn_maintenance':0.001,
        'wpn_budget':0.05 * 0.26,
        'wpn_name_new':'1. Учебные пособия текущего века',
        'wpn_name_mid':'1. Учебные пособия коллекционные',
        'wpn_name_old':'1. Учебные пособия музейные',
        'wpn_age_mid':100,
        'wpn_age_old':200,
        'wpn_a_correction':0.001,
        'wpn_a':0.1,
        'wpn_b':0.000113,
        'wpn_c':1.02,
        }
metadict_wpn[dict_wpn_key] = dict_wpn

dict_wpn_key = dict_wpn_key + 1
dict_wpn = {
        # Всего 37 430 191 рублей (1134 рубля/тираж)
        # | №   | содержание             | названий   | тираж      | цена тиража | цена книги | доля назван.
        # | --- | ---------------------- | ---------- | ---------- | ----------- | ---------  | ------------
        # |  2. | Народные издания       | 2506       | 21 625 709 |   936 573   | 0.043      | 0.076
        'wpn_name':'Народные издания',
        'wpn_troops_type':'Грамотные',
        'wpn_cost':0.043,
        'wpn_cost_currency':'Рубль 1913 года',
        'wpn_maintenance':0.001,
        'wpn_budget':0.05 * 0.025,
        'wpn_name_new':'2. Народные издания текущего века',
        'wpn_name_mid':'2. Народные издания коллекционные',
        'wpn_name_old':'2. Народные издания музейные',
        'wpn_age_mid':100,
        'wpn_age_old':200,
        'wpn_a_correction':0.001,
        'wpn_a':0.1,
        'wpn_b':0.000113,
        'wpn_c':1.02,
        }
metadict_wpn[dict_wpn_key] = dict_wpn

dict_wpn_key = dict_wpn_key + 1
dict_wpn = {
        # Всего 37 430 191 рублей (1134 рубля/тираж)
        # | №   | содержание             | названий   | тираж      | цена тиража | цена книги | доля назван.
        # | --- | ---------------------- | ---------- | ---------- | ----------- | ---------  | ------------
        # | 16. | Календари              |  676       | 13 703 665 | 2 287 886   | 0.167      | 0.021 
        'wpn_name':'Календари',
        'wpn_troops_type':'Грамотные',
        'wpn_cost':0.311,
        'wpn_cost_currency':'Рубль 1913 года',
        'wpn_maintenance':0.001,
        'wpn_budget':0.05 * 0.054,
        'wpn_name_new':'16. Календари текущего века',
        'wpn_name_mid':'16. Календари коллекционные',
        'wpn_name_old':'16. Календари музейные',
        'wpn_age_mid':100,
        'wpn_age_old':200,
        'wpn_a_correction':0.1,
        'wpn_a':0.7,
        'wpn_b':0.000113,
        'wpn_c':1.02,
        }
metadict_wpn[dict_wpn_key] = dict_wpn

dict_wpn_key = dict_wpn_key + 1
dict_wpn = {
        # Всего 37 430 191 рублей (1134 рубля/тираж)
        # | №   | содержание             | названий   | тираж      | цена тиража | цена книги | доля назван.
        # | --- | ---------------------- | ---------- | ---------- | ----------- | ---------  | ------------
        # |  5. | Беллетристика          | 1878       |  7 659 723 | 2 707 662   | 0.353      | 0.056
        'wpn_name':'Беллетристика',
        'wpn_troops_type':'Грамотные',
        'wpn_cost':0.353,
        'wpn_cost_currency':'Рубль 1913 года',
        'wpn_maintenance':0.001,
        'wpn_budget':0.05 * 0.073,
        'wpn_name_new':'5. Беллетристика текущего века',
        'wpn_name_mid':'5. Беллетристика коллекционные',
        'wpn_name_old':'5. Беллетристика музейные',
        'wpn_age_mid':100,
        'wpn_age_old':200,
        'wpn_a_correction':0.001,
        'wpn_a':0.1,
        'wpn_b':0.000113,
        'wpn_c':1.02,
        }
metadict_wpn[dict_wpn_key] = dict_wpn

dict_wpn_key = dict_wpn_key + 1
dict_wpn = {
        # Всего 37 430 191 рублей (1134 рубля/тираж)
        # | №   | содержание             | названий   | тираж      | цена тиража | цена книги | доля назван.
        # | --- | ---------------------- | ---------- | ---------- | ----------- | ---------  | ------------
        # |  8. | Детские издания        | 1396       |  6 549 530 | 2 034 071   | 0.311      | 0.042
        'wpn_name':'Детские издания',
        'wpn_troops_type':'Грамотные',
        'wpn_cost':0.311,
        'wpn_cost_currency':'Рубль 1913 года',
        'wpn_maintenance':0.001,
        'wpn_budget':0.05 * 0.054,
        'wpn_name_new':'8. Детские издания текущего века',
        'wpn_name_mid':'8. Детские издания коллекционные',
        'wpn_name_old':'8. Детские издания музейные',
        'wpn_age_mid':100,
        'wpn_age_old':200,
        'wpn_a_correction':0.002,
        'wpn_a':0.2,
        'wpn_b':0.000113,
        'wpn_c':1.02,
        }
metadict_wpn[dict_wpn_key] = dict_wpn

dict_wpn_key = dict_wpn_key + 1
dict_wpn = {
        # Всего 37 430 191 рублей (1134 рубля/тираж)
        # | №   | содержание             | названий   | тираж      | цена тиража | цена книги | доля назван.
        # | --- | ---------------------- | ---------- | ---------- | ----------- | ---------  | ------------
        # | 24. | История                |  516       |    950 875 | 1 154 284   | 1.214      | 0.016 
        'wpn_name':'История',
        'wpn_troops_type':'Грамотные',
        'wpn_cost':1.214,
        'wpn_cost_currency':'Рубль 1913 года',
        'wpn_maintenance':0.001,
        'wpn_budget':0.05 * 0.031,
        'wpn_name_new':'24. История текущего века',
        'wpn_name_mid':'24. История коллекционные',
        'wpn_name_old':'24. История музейные',
        'wpn_age_mid':100,
        'wpn_age_old':200,
        'wpn_a_correction':0.0005,
        'wpn_a':0.05,
        'wpn_b':0.000113,
        'wpn_c':1.02,
        }
metadict_wpn[dict_wpn_key] = dict_wpn

dict_wpn_key = dict_wpn_key + 1
dict_wpn = {
        # Почта (Российская империя, 1897 год, 129 млн. человек)
            # Газет и журналов -- 1.4 штук/человека
        # Почта (Германия, 1870-1895 годы, 41-52.5 млн. чел)
            # Газет -- 4.7-17 на человека
        # Услуги (1913 год, Киев)
            # Газеты — 3-5 коп. 
        # Численность населения РСФСР по переписи 1989 года — 147.4 млн человек.
            # Газет и журналов — 31 800 миллионов (по 216 на каждого человека).
        'wpn_name':'Газеты',
        'wpn_troops_type':'Грамотные',
        'wpn_cost':0.04,
        'wpn_cost_currency':'Рубль 1913 года',
        'wpn_maintenance':0.001,
        'wpn_budget':0.06,
        'wpn_name_new':'Газеты текущего века',
        'wpn_name_mid':'Газеты коллекционные',
        'wpn_name_old':'Газеты музейные',
        'wpn_age_mid':100,
        'wpn_age_old':200,
        'wpn_a_correction':0.1,
        'wpn_a':0.7,
        'wpn_b':0.000113,
        'wpn_c':1.02,
        }
metadict_wpn[dict_wpn_key] = dict_wpn

dict_wpn_key = dict_wpn_key + 1
dict_wpn = {
        # Почта (Российская империя, 1897 год, 129 млн. человек)
            # Газет и журналов -- 1.4 штук/человека
        # Почта (Германия, 1870-1895 годы, 41-52.5 млн. чел)
            # Газет -- 4.7-17 на человека
        # Литература (1894 год):
            # Журналики в 40 страниц на плохой бумаге -- 3-10 копеек
        'wpn_name':'Журналы',
        'wpn_troops_type':'Грамотные',
        'wpn_cost':0.1,
        'wpn_cost_currency':'Рубль 1913 года',
        'wpn_maintenance':0.001,
        'wpn_budget':0.05,
        'wpn_name_new':'Журналы текущего века',
        'wpn_name_mid':'Журналы коллекционные',
        'wpn_name_old':'Журналы музейные',
        'wpn_age_mid':100,
        'wpn_age_old':200,
        'wpn_a_correction':0.002,
        'wpn_a':0.2,
        'wpn_b':0.000113,
        'wpn_c':1.02,
        }
metadict_wpn[dict_wpn_key] = dict_wpn

dict_wpn_key = dict_wpn_key + 1
dict_wpn = {
        # Почта (Российская империя, 1897 год, 129 млн. человек)
            # Писем и бандеролей -- 3.5 штук/человека
        # Почта (Германия, 1870-1895 годы, 41-52.5 млн. чел)
            # Писем -- 21-45 на человека
            # Международных отправлений -- 1.7-2.5 на человека
        # Услуги связи:
            # - простое письмо, земская почта (1892 год) -- 1-5 копеек
            # - послать письмо (1910 год) - 4 коп.
        'wpn_name':'Письма',
        'wpn_troops_type':'Грамотные',
        'wpn_cost':0.03,
        'wpn_cost_currency':'Рубль 1913 года',
        'wpn_maintenance':0.001,
        'wpn_budget':0.08,
        'wpn_name_new':'Письма текущего века',
        'wpn_name_mid':'Письма коллекционные',
        'wpn_name_old':'Письма музейные',
        'wpn_age_mid':100,
        'wpn_age_old':200,
        'wpn_a_correction':0.002,
        'wpn_a':0.2,
        'wpn_b':0.000113,
        'wpn_c':1.02,
        }
metadict_wpn[dict_wpn_key] = dict_wpn

dict_wpn_key = dict_wpn_key + 1
dict_wpn = {
        # Почта (Российская империя, 1897 год, 129 млн. человек)
            # Посылок и денежных пакетов -- 0.18 штук/человека
            # Посылок и денежных пакетов (на сумму) -- 49 рублей/человека (40% ВВП!)
        # Почта (Германия, 1870-1895 годы, 41-52.5 млн. чел)
            # Посылок -- 0.2-8.4 на человека
        # Услуги связи:
            # - посылка, земская почта (1892 год) -- 10-12 копеек/килограмм
            # - отправить посылку весом менее 5 кг (1910 год) - 65 коп.
        # В основном это доставка из магазинов и книги по почте.
        'wpn_name':'Посылки',
        'wpn_troops_type':'Грамотные',
        'wpn_cost':0.15,
        'wpn_cost_currency':'Рубль 1913 года',
        'wpn_maintenance':0.001,
        'wpn_budget':0.10,
        'wpn_name_new':'Посылки текущего века',
        'wpn_name_mid':'Посылки коллекционные',
        'wpn_name_old':'Посылки музейные',
        'wpn_age_mid':100,
        'wpn_age_old':200,
        'wpn_a_correction':0.002,
        'wpn_a':0.7,
        'wpn_b':0.000113,
        'wpn_c':1.02,
        }
metadict_wpn[dict_wpn_key] = dict_wpn

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


def generation_alive(generation, a, b, c, age_real, a_correction = False):
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
        if a_correction:
            a = a - a_correction
            if a < 0:
                a = 0
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
                metadict[meta_key]['age_real'],
                metadict_wpn[wpn_key].get('wpn_a_correction', False),
                )
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

#----
# Суммарный коэффициент рождаемости:

age_parturition = AGE_FERTILE_MAX - AGE_FERTILE_MIN
population_parturition = 0
population_fertile_female = 0
for meta_key in sorted(metadict.keys()):
    if metadict[meta_key]['age_real'] >= 0 and metadict[meta_key]['age_real'] <= age_parturition:
        population_parturition = population_parturition + metadict[meta_key]['generation_size']
    if (metadict[meta_key]['age_real'] >= AGE_FERTILE_MIN) and (metadict[meta_key]['age_real'] <= AGE_FERTILE_MAX):
        population_fertile_female = population_fertile_female + (metadict[meta_key]['generation_alive'] * FEMALE_PERCENT)
# Суммарный коэффициент рождаемости, это число рождений, делённое на число фертильных женщих:
total_fertility_rate = population_parturition / population_fertile_female
# Коррекция под человеческий социум (если кобылок больше, чем жеребцов)
human_form_total_fertility_rate = (total_fertility_rate * 2) * FEMALE_PERCENT

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
print('Суммарный коэффициент рождаемости: {} ({} детей в семье)'.format(
    round(total_fertility_rate, 1),
    round((total_fertility_rate * (1 - A_INFANT_MORTALITY_CORRECTION)), 1)
    #round(human_form_total_fertility_rate, 1),
    #round((human_form_total_fertility_rate * (1 - A_INFANT_MORTALITY_CORRECTION)), 1)
    ))
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

# Перебор столбцов в базе данных оружия:
for wpn_key in sorted(metadict_wpn.keys()):
    equipment_all = 0
    equipment_create = 0
    # Затем перебор по годам:
    for meta_key in sorted(metadict_equipment_alive.keys()):
        equipment_create = equipment_create\
                + metadict_equipment_create[meta_key][metadict_wpn[wpn_key]['wpn_name']]
        equipment_all = equipment_all\
                + metadict_equipment_alive[meta_key][metadict_wpn[wpn_key]['wpn_name']]
    # Если есть проект, значит есть оружие, хотя бы один экземпляр:
    if (equipment_all < 1):
        equipment_all = 1
        print('Не хватает бюджета на',metadict_wpn[wpn_key]['wpn_name'])
    # Вывод суммы оружия, сохранившегося за все годы:
    print(metadict_wpn[wpn_key]['wpn_name'],
            equipment_all,
            '(сохранилось',
            round(equipment_all / equipment_create * 100), '% изданных,',
            round(equipment_all / population_alive, 2), 'на жителя)')
    # Вывод отношения числа вооружений к числу солдат определённых видов войск:
    #army_type_percent = dict_troops_types[metadict_wpn[wpn_key]['wpn_troops_type']]
    #print('на', round(army_soldiers * army_type_percent),
    #        prof_name_apprentice, metadict_wpn[wpn_key]['wpn_troops_type'],
    #        'или на', round((army_reservists + army_soldiers) * army_type_percent),
    #        prof_name_apprentice, '+',
    #        prof_name_expert, metadict_wpn[wpn_key]['wpn_troops_type'])
    # Вывод описания вооружения:
    #print('    ', metadict_wpn[wpn_key]['wpn_name_comment'])
    # Подсчитываем, сколько оружия создано за год:
    wpn_create = round(GDP_size(0) * GDP_ARMY * \
                metadict_wpn[wpn_key]['wpn_budget'] / metadict_wpn[wpn_key]['wpn_cost'])
    # Расходы на проект:
    print('        Расходы: ',
            round(metadict_wpn[wpn_key]['wpn_budget'] * 100, 3),'% бюджета ',
            '(', round(metadict_wpn[wpn_key]['wpn_cost'] * wpn_create / (10 ** 6), 2),
            ' млн. ', metadict_wpn[wpn_key]['wpn_cost_currency'], ') ', sep='')
    # Подсчитываем потери (без учёта старения оружия):
    print('        Издано:', wpn_create, '(', round(wpn_create / population_alive, 2), 'на жителя)')
    #print('        Потери:', round(wpn_create * metadict_wpn[wpn_key]['wpn_a'] + \
    #        equipment_all * metadict_wpn[wpn_key]['wpn_a']))
    print('        ---')
    # Считаем потребность в боеприпасах (максимум 9 видов оружия) и топливо:
    #if metadict_wpn[wpn_key].get('wpn_ammo_1_name'):
    #    ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_1_name']] = \
    #            ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_1_name']] + \
    #            metadict_wpn[wpn_key]['wpn_ammo_1_expense'] * equipment_all
    #if metadict_wpn[wpn_key].get('wpn_ammo_2_name'):
    #    ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_2_name']] = \
    #            ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_2_name']] + \
    #            metadict_wpn[wpn_key]['wpn_ammo_2_expense'] * equipment_all
    #if metadict_wpn[wpn_key].get('wpn_ammo_3_name'):
    #    ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_3_name']] = \
    #            ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_3_name']] + \
    #            metadict_wpn[wpn_key]['wpn_ammo_3_expense'] * equipment_all
    #if metadict_wpn[wpn_key].get('wpn_ammo_4_name'):
    #    ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_4_name']] = \
    #            ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_4_name']] + \
    #            metadict_wpn[wpn_key]['wpn_ammo_4_expense'] * equipment_all
    #if metadict_wpn[wpn_key].get('wpn_ammo_5_name'):
    #    ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_5_name']] = \
    #            ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_5_name']] + \
    #            metadict_wpn[wpn_key]['wpn_ammo_5_expense'] * equipment_all
    #if metadict_wpn[wpn_key].get('wpn_ammo_6_name'):
    #    ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_6_name']] = \
    #            ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_6_name']] + \
    #            metadict_wpn[wpn_key]['wpn_ammo_6_expense'] * equipment_all
    #if metadict_wpn[wpn_key].get('wpn_ammo_7_name'):
    #    ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_7_name']] = \
    #            ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_7_name']] + \
    #            metadict_wpn[wpn_key]['wpn_ammo_7_expense'] * equipment_all
    #if metadict_wpn[wpn_key].get('wpn_ammo_8_name'):
    #    ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_8_name']] = \
    #            ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_8_name']] + \
    #            metadict_wpn[wpn_key]['wpn_ammo_8_expense'] * equipment_all
    #if metadict_wpn[wpn_key].get('wpn_ammo_9_name'):
    #    ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_9_name']] = \
    #            ammunition_needs[metadict_wpn[wpn_key]['wpn_ammo_9_name']] + \
    #            metadict_wpn[wpn_key]['wpn_ammo_9_expense'] * equipment_all
    #if metadict_wpn[wpn_key].get('wpn_fuel_name'):
    #    ammunition_needs[metadict_wpn[wpn_key]['wpn_fuel_name']] = \
    #            ammunition_needs[metadict_wpn[wpn_key]['wpn_fuel_name']] + \
    #            metadict_wpn[wpn_key]['wpn_fuel_expense'] * equipment_all
    # Считаем общий бюджет и бюджет по родам войск:
    budget_percent = budget_percent + metadict_wpn[wpn_key]['wpn_budget']
    for troop_key in budget_troops_types:
        if troop_key == metadict_wpn[wpn_key]['wpn_troops_type']:
            budget_troops_types[troop_key] = budget_troops_types[troop_key] + \
                    metadict_wpn[wpn_key]['wpn_budget'] * 100
    # Считаем расходы на обслуживание данного вида оружия:
    # Стоимость оружия * процент обслуживания * штук на складах
    # Если строка 'wpn_maintenance' не указана, тогда обслуживание бесплатно
    wpn_maintenance_all = metadict_wpn[wpn_key]['wpn_cost'] * \
            metadict_wpn.get(wpn_key, 0).get('wpn_maintenance', 0)  * \
            dict_equipment_all.get(metadict_wpn[wpn_key]['wpn_name'])
    # Теперь распределяем расходы на обслуживание по родам войск:
    for troop_key in maintenance_troops_types:
        if troop_key == metadict_wpn[wpn_key]['wpn_troops_type']:
            maintenance_troops_types[troop_key] = maintenance_troops_types[troop_key] + \
                    wpn_maintenance_all

# Сумма бюджета всех проектов из базы данных оружия:
print('Расходы военного бюджета на закупки и производство:')
for troop_key in sorted(budget_troops_types.keys()):
    print('    ', troop_key, ' (', round(dict_troops_types[troop_key] * 100), '%)',
            ' — ', round(budget_troops_types[troop_key], 2), '%', sep='')
print('Использовано ', round(budget_percent * 100, 2), '% бюджета армии',
        ' (или ', round(GDP_ARMY * budget_percent * 100, 2), '% ВВП страны)',
        sep='')
print('        ---')

# Расходы на обслуживание оружия по видам войск:
#maintenance_percent_sum = 0
#print('Расходы военного бюджета на хранение и обслуживание:')
#for troop_key in sorted(maintenance_troops_types.keys()):
#    maintenance_percent = maintenance_troops_types[troop_key] / (GDP_size(0) * GDP_ARMY)
#    maintenance_percent_sum = maintenance_percent_sum + maintenance_percent
#    print('    ', troop_key, ' (', round(dict_troops_types[troop_key] * 100), '%)',
#            ' — ', round(maintenance_percent * 100, 2), '%', sep='')
#print('Использовано ', round(maintenance_percent_sum * 100, 2), '% бюджета армии',
#        ' (или ', round(maintenance_percent_sum * GDP_ARMY * 100, 2), '% ВВП страны)',
#        sep='')
#print('        ---')

# Соотношение производства боеприпасов и потребности в них:
#print('Боеприпасы на складах (на год войны):')
#for ammo_key in sorted(ammunition_needs.keys()):
#    # (ammo_key, 0) — значит, если нет ключа, брать ноль.
#    print('   ', ammo_key, ' — ', dict_equipment_all.get(ammo_key, 0), ' (',
#            round(dict_equipment_all.get(ammo_key, ammunition_needs[ammo_key]) / \
#                    ammunition_needs[ammo_key] * 100), '%)', sep='')

#----
# Распределение по возрастам:

dict_population_ages = {}
dict_population_ages['0-4'] = 0
dict_population_ages['5-9'] = 0
dict_population_ages['10-14'] = 0
dict_population_ages['15-19'] = 0
dict_population_ages['20-24'] = 0
dict_population_ages['25-29'] = 0
dict_population_ages['30-34'] = 0
dict_population_ages['35-39'] = 0
dict_population_ages['40-44'] = 0
dict_population_ages['45-49'] = 0
dict_population_ages['50-54'] = 0
dict_population_ages['55-59'] = 0
dict_population_ages['60-64'] = 0
dict_population_ages['65-69'] = 0
dict_population_ages['70-74'] = 0
dict_population_ages['75-79'] = 0
dict_population_ages['80-84'] = 0
dict_population_ages['85-89'] = 0
dict_population_ages['90-94'] = 0
dict_population_ages['95-99'] = 0
dict_population_ages['100+'] = 0
for meta_key in sorted(metadict.keys()):
    if (0 <= metadict[meta_key]['age_real'] <= 4):
        dict_population_ages['0-4'] = dict_population_ages['0-4'] + metadict[meta_key]['generation_alive']
    elif (5 <= metadict[meta_key]['age_real'] <= 9):
        dict_population_ages['5-9'] = dict_population_ages['5-9'] + metadict[meta_key]['generation_alive']
    elif (10 <= metadict[meta_key]['age_real'] <= 14):
        dict_population_ages['10-14'] = dict_population_ages['10-14']\
                + metadict[meta_key]['generation_alive']
    elif (15 <= metadict[meta_key]['age_real'] <= 19):
        dict_population_ages['15-19'] = dict_population_ages['15-19']\
                + metadict[meta_key]['generation_alive']
    elif (20 <= metadict[meta_key]['age_real'] <= 24):
        dict_population_ages['20-24'] = dict_population_ages['20-24']\
                + metadict[meta_key]['generation_alive']
    elif (25 <= metadict[meta_key]['age_real'] <= 29):
        dict_population_ages['25-29'] = dict_population_ages['25-29']\
                + metadict[meta_key]['generation_alive']
    elif (30 <= metadict[meta_key]['age_real'] <= 34):
        dict_population_ages['30-34'] = dict_population_ages['30-34']\
                + metadict[meta_key]['generation_alive']
    elif (35 <= metadict[meta_key]['age_real'] <= 39):
        dict_population_ages['35-39'] = dict_population_ages['35-39']\
                + metadict[meta_key]['generation_alive']
    elif (40 <= metadict[meta_key]['age_real'] <= 44):
        dict_population_ages['40-44'] = dict_population_ages['40-44']\
                + metadict[meta_key]['generation_alive']
    elif (45 <= metadict[meta_key]['age_real'] <= 49):
        dict_population_ages['45-49'] = dict_population_ages['45-49']\
                + metadict[meta_key]['generation_alive']
    elif (50 <= metadict[meta_key]['age_real'] <= 54):
        dict_population_ages['50-54'] = dict_population_ages['50-54']\
                + metadict[meta_key]['generation_alive']
    elif (55 <= metadict[meta_key]['age_real'] <= 59):
        dict_population_ages['55-59'] = dict_population_ages['55-59']\
                + metadict[meta_key]['generation_alive']
    elif (60 <= metadict[meta_key]['age_real'] <= 64):
        dict_population_ages['60-64'] = dict_population_ages['60-64']\
                + metadict[meta_key]['generation_alive']
    elif (65 <= metadict[meta_key]['age_real'] <= 69):
        dict_population_ages['65-69'] = dict_population_ages['65-69']\
                + metadict[meta_key]['generation_alive']
    elif (70 <= metadict[meta_key]['age_real'] <= 74):
        dict_population_ages['70-74'] = dict_population_ages['70-74']\
                + metadict[meta_key]['generation_alive']
    elif (75 <= metadict[meta_key]['age_real'] <= 79):
        dict_population_ages['75-79'] = dict_population_ages['75-79']\
                + metadict[meta_key]['generation_alive']
    elif (80 <= metadict[meta_key]['age_real'] <= 84):
        dict_population_ages['80-84'] = dict_population_ages['80-84']\
                + metadict[meta_key]['generation_alive']
    elif (85 <= metadict[meta_key]['age_real'] <= 89):
        dict_population_ages['85-89'] = dict_population_ages['85-89']\
                + metadict[meta_key]['generation_alive']
    elif (90 <= metadict[meta_key]['age_real'] <= 94):
        dict_population_ages['90-94'] = dict_population_ages['90-94']\
                + metadict[meta_key]['generation_alive']
    elif (95 <= metadict[meta_key]['age_real'] <= 99):
        dict_population_ages['95-99'] = dict_population_ages['95-99']\
                + metadict[meta_key]['generation_alive']
    elif (metadict[meta_key]['age_real'] >= 100):
        dict_population_ages['100+'] = dict_population_ages['100+']\
                + metadict[meta_key]['generation_alive']

# Средний возраст популяции
population_half = 0
for meta_key in sorted(metadict.keys()):
    population_half = population_half + metadict[meta_key]['generation_alive']
    if population_half >= (POPULATION / 2):
        population_middle_age = metadict[meta_key]['age_real']
        break
print('------------------------------------------------------------')
print('Средний возраст популяции: {}'.format(population_middle_age))

population_test = 0
print('Распределение населения по возрастам:')
for key, population in dict_population_ages.items():
    population_part = population / population_alive
    population_test = population_test + population_part
    #print(key, round(population_part, 5))
    print(key, ' -- ', round(population), ' (' , round(population_part * 100), '%)', sep='')
