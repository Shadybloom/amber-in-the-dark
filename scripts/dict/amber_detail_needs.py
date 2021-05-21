#----
# Заметки:
# Государство будущего. Производство и потребление в социальном государстве. 1900 год
# https://istmat.info/node/27169

#----
# Потребности (возрастные):

metadict_detail['-Младенцы'] = {
        'Потребности основные (пони)':1,
        'Потребность в здравоохранении, младенцы (пони)':1,
        'Потребность в одежде, жеребята (пони)':1,
        }

metadict_detail['-Дети (1-6 лет)'] = {
        'Потребности основные (пони)':1,
        'Потребность в здравоохранении, дети (пони)':1,
        'Потребность в одежде, жеребята (пони)':1,
        }

metadict_detail['-Школьники (7-10 лет)'] = {
        # Начальная школа, до получения метки.
        # Только 85% жеребят обучаются грамоте. Земные ещё не все втянулись.
        'Потребности основные (пони)':1,
        'Потребность в образовании, начальная школа (пони)':0.85,
        'Потребность в здравоохранении, дети (пони)':1,
        'Потребность в одежде, жеребята (пони)':1,
        }

metadict_detail['-Школьники (11-13 лет)'] = {
        # Средняя школа, в ожидании метки.
        # Только 50% грамотных получают среднее образование. Проблема расстояний.
        'Потребности основные (пони)':1,
        'Потребность в образовании, средняя школа (пони)':0.85 * 0.5,
        'Потребность в здравоохранении, подростки (пони)':1,
        'Потребность в одежде, подростки (пони)':1,
        }

metadict_detail['-Подмастерья (14-20 лет)'] = {
        # Ученичество, реальные училища.
        # 50% закончивших школу -- специальное образование.
        'Потребности основные (пони)':1,
        'Потребность в образовании, старшая школа (пони)':0.85 * 0.5 * 0.5,
        'Потребность в образовании, университеты (пони)':0.85 * 0.5 * 0.005,
        'Потребность в здравоохранении, подростки (пони)':1,
        'Потребность в одежде, подростки (пони)':1,
        }

metadict_detail['-Рабочие'] = {
        # Понячье высшее образование начинается с 20 лет и длится до 26 лет.
        # Хотя некоторые твайки и начинают подростками, а заканчивают в двадцать.
        'Потребности основные (пони)':1,
        'Потребность в образовании, университеты (пони)':0.5 * 0.5 * 0.005,
        'Потребность в здравоохранении, взрослые (пони)':1,
        'Потребность в одежде, взрослые (пони)':1,
        }

metadict_detail['-Старики'] = {
        'Потребности основные (пони)':1,
        'Потребность в здравоохранении, старики (пони)':1,
        'Потребность в одежде, взрослые (пони)':1,
        }

#----
# Потребности (национальные):

metadict_detail['Североморские горожане бедняки'] = {
        'Североморский рацион (пони/год)':0.25,
        'Городской рацион (пони/год)':0.75,
        'Расход воды и мыла горожанами (пони/день)':360,
        'Североморское городское жильё (квадратный метр)':15,
        'Потребность в развлечениях, горожане (пони/день)':360 / 6,
        'Потребность в путешествиях, горожане (пони/день)':30,
        'Потребность в одежде, северяне (пони)':1,
        }

metadict_detail['Североморские горожане середняки'] = {
        'Североморский рацион (пони/год)':0.25,
        'Городской рацион (пони/год)':0.50,
        'Изысканный рацион (пони/год)':0.25,
        'Расход воды и мыла горожанами (пони/день)':360,
        'Частное городское жильё (квадратный метр)':30,
        'Потребность в развлечениях, горожане (пони/день)':360 / 6,
        'Потребность в путешествиях, горожане (пони/день)':60,
        'Потребность в одежде, северяне (пони)':1,
        }

metadict_detail['Североморские горожане богатеи'] = {
        # Смотри, чтобы было не больше 160 нерабочих дней в году.
        # 120 дней уже занято культурой и путешествиями.
        'Североморский рацион (пони/год)':0.50,
        'Изысканный рацион (пони/год)':0.50,
        'Расход воды и мыла городскими богатеями (пони/день)':360,
        'Богатое городское жильё (квадратный метр)':60,
        'Потребность в развлечениях, богатеи (пони/день)':360 / 6,
        'Потребность в путешествиях, богатеи (пони/день)':100,
        'Потребность в одежде, богатеи (пони)':1,
        }

metadict_detail['Североморские селяне бедняки'] = {
        'Североморские запасы (пони/год)':1,
        'Североморский рацион (пони/год)':1,
        'Расход воды и мыла селянами (пони/день)':360,
        'Североморское сельское жильё (квадратный метр)':15,
        'Потребность в развлечениях, селяне (пони/день)':360 / 6,
        'Потребность в путешествиях, селяне (пони/день)':15,
        'Потребность в одежде, северяне (пони)':1,
        }

metadict_detail['Североморские селяне середняки'] = {
        'Североморские запасы (пони/год)':1,
        'Североморский рацион (пони/год)':0.75,
        'Изысканный рацион (пони/год)':0.25,
        'Расход воды и мыла селянами (пони/день)':360,
        'Частное сельское жильё (квадратный метр)':30,
        'Потребность в развлечениях, селяне (пони/день)':360 / 6,
        'Потребность в путешествиях, селяне (пони/день)':30,
        'Потребность в одежде, северяне (пони)':1,
        }

metadict_detail['Североморские селяне богатеи'] = {
        'Североморские запасы (пони/год)':1,
        'Североморский рацион (пони/год)':0.50,
        'Изысканный рацион (пони/год)':0.50,
        'Расход воды и мыла сельскими богатеями (пони/день)':360,
        'Богатое сельское жильё (квадратный метр)':60,
        'Потребность в развлечениях, богатеи (пони/день)':360 / 6,
        'Потребность в путешествиях, богатеи (пони/день)':100,
        'Потребность в одежде, богатеи (пони)':1,
        }

metadict_detail['Среднеземные горожане бедняки'] = {
        'Среднеземный рацион (пони/год)':0.25,
        'Городской рацион (пони/год)':0.75,
        'Расход воды и мыла горожанами (пони/день)':360,
        'Среднеземное городское жильё (квадратный метр)':15,
        'Потребность в развлечениях, горожане (пони/день)':360 / 6,
        'Потребность в путешествиях, горожане (пони/день)':30,
        'Потребность в одежде, среднеземцы (пони)':1,
        }

metadict_detail['Среднеземные горожане середняки'] = {
        'Среднеземный рацион (пони/год)':0.25,
        'Городской рацион (пони/год)':0.50,
        'Изысканный рацион (пони/год)':0.25,
        'Расход воды и мыла горожанами (пони/день)':360,
        'Частное городское жильё (квадратный метр)':30,
        'Потребность в развлечениях, горожане (пони/день)':360 / 6,
        'Потребность в путешествиях, горожане (пони/день)':60,
        'Потребность в одежде, среднеземцы (пони)':1,
        }

metadict_detail['Среднеземные горожане богатеи'] = {
        'Среднеземный рацион (пони/год)':0.50,
        'Изысканный рацион (пони/год)':0.50,
        'Расход воды и мыла городскими богатеями (пони/день)':360,
        'Богатое городское жильё (квадратный метр)':60,
        'Потребность в развлечениях, богатеи (пони/день)':360 / 6,
        'Потребность в путешествиях, богатеи (пони/день)':100,
        'Потребность в одежде, богатеи (пони)':1,
        }

metadict_detail['Среднеземные селяне бедняки'] = {
        'Среднеземные запасы (пони/год)':1,
        'Среднеземный рацион (пони/год)':1,
        'Расход воды и мыла селянами (пони/день)':360,
        'Среднеземное сельское жильё (квадратный метр)':15,
        'Потребность в развлечениях, селяне (пони/день)':360 / 6,
        'Потребность в путешествиях, селяне (пони/день)':15,
        'Потребность в одежде, среднеземцы (пони)':1,
        }

metadict_detail['Среднеземные селяне середняки'] = {
        'Среднеземные запасы (пони/год)':1,
        'Среднеземный рацион (пони/год)':0.75,
        'Изысканный рацион (пони/год)':0.25,
        'Расход воды и мыла селянами (пони/день)':360,
        'Частное сельское жильё (квадратный метр)':30,
        'Потребность в развлечениях, селяне (пони/день)':360 / 6,
        'Потребность в путешествиях, селяне (пони/день)':30,
        'Потребность в одежде, среднеземцы (пони)':1,
        }

metadict_detail['Среднеземные селяне богатеи'] = {
        'Среднеземные запасы (пони/год)':1,
        'Среднеземный рацион (пони/год)':0.50,
        'Изысканный рацион (пони/год)':0.50,
        'Расход воды и мыла сельскими богатеями (пони/день)':360,
        'Богатое сельское жильё (квадратный метр)':60,
        'Потребность в развлечениях, богатеи (пони/день)':360 / 6,
        'Потребность в путешествиях, богатеи (пони/день)':100,
        'Потребность в одежде, богатеи (пони)':1,
        }

metadict_detail['Южноморские горожане бедняки'] = {
        'Южноморский рацион (пони/год)':0.25,
        'Городской рацион (пони/год)':0.75,
        'Расход воды и мыла горожанами (пони/день)':360,
        'Южноморское городское жильё (квадратный метр)':15,
        'Потребность в развлечениях, горожане (пони/день)':360 / 6,
        'Потребность в путешествиях, горожане (пони/день)':30,
        'Потребность в одежде, южане (пони)':1,
        }

metadict_detail['Южноморские горожане середняки'] = {
        'Южноморский рацион (пони/год)':0.25,
        'Городской рацион (пони/год)':0.50,
        'Изысканный рацион (пони/год)':0.25,
        'Расход воды и мыла горожанами (пони/день)':360,
        'Частное городское жильё (квадратный метр)':30,
        'Потребность в развлечениях, горожане (пони/день)':360 / 6,
        'Потребность в путешествиях, горожане (пони/день)':60,
        'Потребность в одежде, южане (пони)':1,
        }

metadict_detail['Южноморские горожане богатеи'] = {
        'Южноморский рацион (пони/год)':0.50,
        'Изысканный рацион (пони/год)':0.50,
        'Расход воды и мыла городскими богатеями (пони/день)':360,
        'Богатое городское жильё (квадратный метр)':60,
        'Потребность в развлечениях, богатеи (пони/день)':360 / 6,
        'Потребность в путешествиях, богатеи (пони/день)':100,
        'Потребность в одежде, богатеи (пони)':1,
        }

metadict_detail['Южноморские селяне бедняки'] = {
        'Южноморские запасы (пони/год)':1,
        'Южноморский рацион (пони/год)':1,
        'Расход воды и мыла селянами (пони/день)':360,
        'Южноморское сельское жильё (квадратный метр)':15,
        'Потребность в развлечениях, селяне (пони/день)':360 / 6,
        'Потребность в путешествиях, селяне (пони/день)':15,
        'Потребность в одежде, южане (пони)':1,
        }

metadict_detail['Южноморские селяне середняки'] = {
        'Южноморские запасы (пони/год)':1,
        'Южноморский рацион (пони/год)':0.75,
        'Изысканный рацион (пони/год)':0.25,
        'Расход воды и мыла селянами (пони/день)':360,
        'Частное сельское жильё (квадратный метр)':30,
        'Потребность в развлечениях, селяне (пони/день)':360 / 6,
        'Потребность в путешествиях, селяне (пони/день)':30,
        'Потребность в одежде, южане (пони)':1,
        }

metadict_detail['Южноморские селяне богатеи'] = {
        'Южноморские запасы (пони/год)':1,
        'Южноморский рацион (пони/год)':0.50,
        'Изысканный рацион (пони/год)':0.50,
        'Расход воды и мыла сельскими богатеями (пони/день)':360,
        'Богатое сельское жильё (квадратный метр)':60,
        'Потребность в развлечениях, богатеи (пони/день)':360 / 6,
        'Потребность в путешествиях, богатеи (пони/день)':100,
        'Потребность в одежде, богатеи (пони)':1,
        }

#----
# Потребности (хозяйственная вода):

metadict_detail['Расход воды и мыла городскими богатеями (пони/день)'] = {
        # TODO:
            # У тебя завышено использование мыла.
            # Уборку привяжи к площади и типу жилья. Пользуйся нормативами.
            # Уборку в эксплуатацию жилья.
        # 6 килограмм моющих средств/год -- современный показатель.
        'Использование душа, город (раз)':1,
        'Использование ванной, город (раз)':1 / 2,
        'Использование умывальника, город (раз)':6,
        'Использование уборной, город (раз)':3,
        '-Городское водоснабжение (литр)':180,
        }

metadict_detail['Расход воды и мыла горожанами (пони/день)'] = {
        # 2 килограмма моющих средств/год.
        'Использование душа, город (раз)':1,
        'Использование бани, город (раз)':1 / 6,
        'Использование ванной, город (раз)':1 / 6,
        'Использование умывальника, город (раз)':6,
        'Использование уборной, город (раз)':3,
        '-Городское водоснабжение (литр)':130,
        }

metadict_detail['Расход воды и мыла сельскими богатеями (пони/день)'] = {
        # 6 килограмма моющих средств/год.
        'Использование душа, село (раз)':1,
        'Использование бани, село (раз)':1 / 3,
        'Использование умывальника, город (раз)':6,
        'Использование уборной, город (раз)':3,
        '-Сельское водоснабжение (литр)':130,
        }

metadict_detail['Расход воды и мыла селянами (пони/день)'] = {
        # 2 килограмма моющих средств/год.
        'Использование душа, село (раз)':1 / 3,
        'Использование бани, село (раз)':1 / 6,
        'Использование умывальника, село (раз)':6,
        'Использование уборной, село (раз)':3,
        '-Сельское водоснабжение (литр)':50,
        }

#----
# Потребности (жильё):

metadict_detail['Богатое городское жильё (квадратный метр)'] = {
        # Ничего выдающегося, богатеи всего в 16 раз богаче бедняков.
        'Городское жильё, особняк (квадратный метр)':1,
        }

metadict_detail['Богатое сельское жильё (квадратный метр)'] = {
        'Сельское жильё, усадьба (квадратный метр)':1,
        }

metadict_detail['Частное городское жильё (квадратный метр)'] = {
        # Квартиры в кирпичных домах. Обычно двух-трёхкомнатные.
        'Городское жильё, квартира (квадратный метр)':1,
        }

metadict_detail['Частное сельское жильё (квадратный метр)'] = {
        'Сельское жильё, фахверк (квадратный метр)':1,
        }

metadict_detail['Североморское городское жильё (квадратный метр)'] = {
        # Деревянные дома на окраинах города. Брусья каркаса и саманные стены.
        'Городское жильё, фахверк (квадратный метр)':1,
        }

metadict_detail['Североморское сельское жильё (квадратный метр)'] = {
        'Сельское жильё, изба (квадратный метр)':1,
        }

metadict_detail['Среднеземное городское жильё (квадратный метр)'] = {
        'Городское жильё, фахверк (квадратный метр)':1,
        }

metadict_detail['Среднеземное сельское жильё (квадратный метр)'] = {
        # Деревянные домишки среднего запада. Каркас, фанера и опилкобетон.
        'Сельское жильё, каркасный дом (квадратный метр)':1,
        }

metadict_detail['Южноморское городское жильё (квадратный метр)'] = {
        # Старомодные многоквартирные дома. Инсулы.
        'Городское жильё, фахверк (квадратный метр)':1,
        }

metadict_detail['Южноморское сельское жильё (квадратный метр)'] = {
        'Сельское жильё, хата (квадратный метр)':1,
        }

#----
# Потребности (одежда):

metadict_army['Потребность в одежде, богатеи (пони)'] = {
        # Пони носят плащ в дождь, пальто в снег, платок на кухне, шляпу в жаркий день.
        # Из обуви резиновые галоши и плетёные шлёпанцы, чтобы копыта не марать.
        # Наконец, украшения. Ленты, чепчики, броши, заколки, кружева.
            # Износ -- 3 комплекта белья/год, 1 костюм, 1 пальто.
            # https://istmat.info/node/27433
        # Пони вовсе не носят рубахи и панталоны. А верхнюю одежду не каждый день.
        '|Одежда богатая летняя (комплект)':2,
        '|Одежда богатая зимняя (комплект)':2,
        '|Одежда простая летняя (комплект)':1,
        '|Одежда простая зимняя (комплект)':1,
        '|Постельное бельё богатое (комплект)':4,
        'Использование богатой зимней одежды (дней/год)':60,
        'Использование богатой летней одежды (дней/год)':300 / 2,
        'Использование богатого постельного белья (дней/год)':360,
        }

metadict_army['Потребность в одежде, северяне (пони)'] = {
        '|Одежда простая летняя (комплект)':1,
        '|Одежда простая зимняя (комплект)':1,
        '|Постельное бельё простое (комплект)':2,
        'Использование простой зимней одежды (дней/год)':120,
        'Использование простой летней одежды (дней/год)':240 / 2,
        'Использование простого постельного белья (дней/год)':360,
        }

metadict_army['Потребность в одежде, среднеземцы (пони)'] = {
        '|Одежда простая летняя (комплект)':1,
        '|Одежда простая зимняя (комплект)':1 / 2,
        '|Постельное бельё простое (комплект)':2,
        'Использование простой зимней одежды (дней/год)':60,
        'Использование простой летней одежды (дней/год)':300 / 2,
        'Использование простого постельного белья (дней/год)':360,
        }

metadict_army['Потребность в одежде, южане (пони)'] = {
        # Почти не носят одежду. Разве что плащи в дождливые дни.
        # А дожди у понях по расписанию. Пегасы же.
        '|Одежда простая летняя (комплект)':1,
        '|Одежда простая зимняя (комплект)':1 / 5,
        '|Постельное бельё простое (комплект)':2,
        'Использование простой летней одежды (дней/год)':360 / 2,
        'Использование простого постельного белья (дней/год)':360,
        }

metadict_army['Потребность в одежде, жеребята (пони)'] = {
        # Не используется. Обобщение в одеждах для климатических зон.
        }

metadict_army['Потребность в одежде, подростки (пони)'] = {
        }

metadict_army['Потребность в одежде, взрослые (пони)'] = {
        }

#----
# Потребности (здравоохранение):
    # Статистика 10-тысячного кантона Эквестрии:
    # Вывод war-economy-analyser.py:
        # Ожидаемая численность: 10575
        # Численность популяции: 10556
        # Численность поколений: 31510
        # Суммарный коэффициент рождаемости: 1.9 (1.8 детей в семье)
        # ------------------------------------------------------------
        # Смерти от болезней (в год):127 (1% от численности населения)
        # Несчастные случаи (в год): 5 (4% от числа смертей)
        # ------------------------------------------------------------
        # Средний возраст популяции: 35 лет
        # Ожидаемая продолжительность жизни: 78 лет
        # ------------------------------------------------------------
        # Распределение населения по возрастам:
        # 0 -- 159 (2%)
        # 1-10 -- 1553 (15%)
        # 11-20 -- 1495 (14%)
        # 21-30 -- 1435 (14%)
        # 31-40 -- 1367 (13%)
        # 41-50 -- 1280 (12%)
        # 51-60 -- 1158 (11%)
        # 61-70 -- 972 (9%)
        # 71-80 -- 696 (7%)
        # 81-90 -- 352 (3%)
        # 91-100 -- 85 (1%)
        # 101-110 -- 4 (0%)
    # Статистика Советского союза и Российской федерации:
        # https://rusind.ru/statistika-zdravooxraneniya-v-rossii.html
    # Статистика больниц 1940 - 1990 годы:
        # Врачей -- 7.4-45 на 10 000 населения
        # Медперсонала -- 26-124 на 10 000 населения
        # Больничных коек -- 500-2000 на 10 000 населения
        # Работа больничной койки -- 330 дней/год, 12 дней/больного, 27 больных/койка-год
        # Статистика больничных коек по отделениям 2017 год:
            # Терапевтический профиль -- 24%
            # Психиатрия -- 13.3%
            # Хирургия -- 21%
            # Неврология -- 7.1%
            # Туберкулёз -- 7%
            # Роддомы -- 5.7%
            # Гинекология -- 4.5%
            # Инфекционный профиль -- 5.6%
            # Наркология -- 2%
            # Дермато-венерологический профиль -- 1.1%
            # Офтальмология -- 1.9%
            # Отоларингология -- ???
            # Онкология -- ???
    # Профилактическая статистика 2015 год:
        # * Осмотрено взрослых (15+ лет) -- 2700 (34%), 13.5 посетителей/день
        # * Осмотрено детей (0-14 лет) -- 1500 (73%), 7.5 посетителей/день
    # Статистика болезней 2015 год:
        # * Всего заболевших/год -- 7 800 на 10 000 населения (21.7 посетителей/день)
        # * Скорая помощь (вызовов/год) -- 2200-3500 на 10 000 населения (6-10 посетителей/день)
        # Болезнь                             | Процент | на 7800 заболевших
        # ----------------------------------- | ------- | ------------------
        # Органы дыхания                      | 46.1    | 3596
        # Травмы, отравления                  | 11.7    | 913
        # Мочеполовая система                 | 5.8     | 452
        # Кожа                                | 5.3     | 413
        # Система кровообращения              | 4.5     | 351
        # Желудочно-кишечный тракт            | 4.1     | 320
        # Кости, мышцы, соединительные ткани  | 3.9     | 304
        # Глаза                               | 3.9     | 304
        # Осложнения родов                    | 1.9     | 148
        # Опухоли, рак                        | 1.5     | 117
        # Прочее                              | 11.3    | 881
    # Статистика инвалидности (2017 год):
        # Инвалиды, всего -- 835 на 10 000 населения.
            # 1 группа, живут в больницах (тяжело больные и глубокие старики) -- 89
            # 2 группа, нуждаются в заботе (слух, зрение, потеря конечности) -- 403
            # 3 группа, нуждаются в частом отдыхе (трудоспособны) -- 299
        # Дети-инвалиды 1-3 групп -- 43 (каждый сотый подросток маленькая Сноудроп)

metadict_army['Потребность в здравоохранении, младенцы (пони)'] = {
        '_-Обращение в поликлинику, рождение (посещений/год)':1,
        '_-Обращение в поликлинику, болезни (посещений/год)':0.55,
        '_-Обращение в поликлинику, профилактика (посещений/год)':1,
        '_-Обращение в скорую помощь, болезни (посещений/год)':0.15,
        }

metadict_army['Потребность в здравоохранении, дети (пони)'] = {
        '_-Обращение в поликлинику, болезни (посещений/год)':0.35,
        '_-Обращение в поликлинику, профилактика (посещений/год)':0.85,
        '_-Обращение в скорую помощь, болезни (посещений/год)':0.15,
        }

metadict_army['Потребность в здравоохранении, подростки (пони)'] = {
        '_-Обращение в поликлинику, болезни (посещений/год)':0.45,
        '_-Обращение в поликлинику, профилактика (посещений/год)':0.55,
        '_-Обращение в скорую помощь, болезни (посещений/год)':0.20,
        }

metadict_army['Потребность в здравоохранении, взрослые (пони)'] = {
        '_-Обращение в поликлинику, болезни (посещений/год)':0.75,
        '_-Обращение в поликлинику, профилактика (посещений/год)':0.35,
        '_-Обращение в скорую помощь, болезни (посещений/год)':0.30,
        }

metadict_army['Потребность в здравоохранении, старики (пони)'] = {
        '_-Обращение в поликлинику, болезни (посещений/год)':0.90,
        '_-Обращение в поликлинику, профилактика (посещений/год)':0.65,
        '_-Обращение в скорую помощь, болезни (посещений/год)':0.55,
        }

#----
# Потребности (образование):
    # Понячья цивилизация на уровне Германии 1895 года.
    # Германия, 1875 год -- 0.00039 (39 студента на 100k населения)
    # Германия, 1895 год -- 0.00053 (53 студента на 100k населения)
    # Германия, 1914 год -- 0.00092 (92 студента на 100k населения)
# Четыре университета (московский, петербургский, киевский, харьковский) -- 75% всех студентов.
    # Московский университет 1895 года:
        # - 4147 студентов, 233 преподавателя
        # - Средства -- 4 106 589 рублей, 1183 рублей/год, или 99 рублей/месяц на студента**
        # - Полное содержание в общежитии (расходы) -- 190 рублей/год, 16 рублей/месяц.
        # - Бесплатные обеды (расходы) -- 0.4 рубля/студента
    # Казанский университет 1893 года:
        # - 803 студента, 109 преподавателей
        # - Средства -- 570 рублей/год, или 47 рублей/месяц на студента
        # - Стипендия (20% студентов) -- 226 рублей/год, 18.8 рублей/месяц
        # - Библиотека -- 56 643 названия, 142 159 томов (177 томов/студента)**
    # Новороссийский университет 1896 года:
        # - 581 студент,  61 преподавателей
        # - Средства -- 475 рублей/год, или 40 рублей/месяц на студента
        # - Библиотека -- ??? названия, 168 500 томов (290 томов/студента)

metadict_army['Потребность в образовании, начальная школа (пони)'] = {
        # Жеребята не очень-то мотивированы ходить в школу. Часто убегают, иногда болеют.
        '_-Обращение к образованию, начальная школа (посещений/год)':200 * 0.75,
        }

metadict_army['Потребность в образовании, средняя школа (пони)'] = {
        '_-Обращение к образованию, средняя школа (посещений/год)':200 * 0.85,
        }

metadict_army['Потребность в образовании, старшая школа (пони)'] = {
        '_-Обращение к образованию, старшая школа (посещений/год)':200 * 0.90,
        '-+Образование, специалисты (пони)':1 / 0.25,
        }

metadict_army['Потребность в образовании, университеты (пони)'] = {
        # Если в Эквестрии 18 000 студентов, тогда 70 000 отучившихся в университетах.
        # Поступающих в университеты -- 1 / 100 от достигших 20 лет.
        # Это вывод war-economy-analyser.py
        '_-Обращение к образованию, университет (посещений/год)':200 * 0.95,
        '-+Образование, высшее (пони)':1 / 0.25,
        '-+Образование, врачи (пони)':1 / 0.25 * 0.25,
        }

#----
# Потребности (основные):

metadict_detail['Потребности основные (пони)'] = {
        'Потребность в дорогах (метр)':20,
        }

#----
# Потребности (путешествия):
    # Командировки и отпуска.
    # С пегасами и их планёрами путешествия всегда были доступны для всех.
    # TODO: 25% времени в пути, 75% на месте. Гостиницы и общежития.


metadict_detail['Потребность в путешествиях, богатеи (пони/день)'] = {
        'Региональное путешествие (пони/день)':0.4,
        'Межрегиональное путешествие (пони/день)':0.3,
        'Заграничное путешествие (пони/день)':0.3,
        }

metadict_detail['Потребность в путешествиях, горожане (пони/день)'] = {
        'Региональное путешествие (пони/день)':0.5,
        'Межрегиональное путешествие (пони/день)':0.4,
        'Заграничное путешествие (пони/день)':0.1,
        }

metadict_detail['Потребность в путешествиях, селяне (пони/день)'] = {
        'Региональное путешествие (пони/день)':0.7,
        'Межрегиональное путешествие (пони/день)':0.25,
        'Заграничное путешествие (пони/день)':0.05,
        }

#----
# Потребности (прочие):
    # Печатное дело в Германии на 1890 год (50 млн. человек, 7650 чел/типографию, 5-6 рабочих/типографию)
    # Печатное дело в России на 1897 год (129 млн. человек, 66 000 чел/типографию)
        # - 1885 год, общий тираж книг: ??? названий, 18.77 млн.
        # - 1893 год, общий тираж книг: 7783 названий, 27.2 млн. экземпляров (средний тираж -- 3500)
        # - 1901 год, общий тираж книг: ??? названий, 56.3 млн. экземпляров
        # - 1913 год, общий тираж книг: 30 100 названий, 98.2 млн. экземпляров (средний тираж -- 3300)**
    # Книги, печать и периодика в Российской империи
        # http://www.protown.ru/information/hide/6631.html
        # https://ru.wikisource.org/wiki/ЭСБЕ/Печать
        # https://ru.wikisource.org/wiki/ЭСБЕ/Газеты
        # https://ru.wikisource.org/wiki/ЭСБЕ/Типографское_дело

metadict_detail['Потребность в развлечениях, горожане (пони/день)'] = {
        # TODO:
            # Допилить
            # Помни о распределении. Это число дней в году, которые тратятся на развлечения.
            # А ниже, например, 0.1 -- театр, 0.2 -- книги, это процент времени дней отдыха.
        # TODO:
            # Книги, газеты, театр, путешествия.
            # Сделай распределение книг по содержанию.
        # TODO: только в 50+ тысячных мегаполисах развита культурная жизнь.
            # А у нас остальные 50% горожан во всяких Понивилях. Им приходится ездить в свои кантерлоты.
        }

metadict_detail['Потребность в развлечениях, селяне (пони/день)'] = {
        }

metadict_detail['Потребность в развлечениях, богатеи (пони/день)'] = {
        }

#----
# Запасы еды, перепроизводство и внешняя торговля:

metadict_detail['Североморские запасы (пони/год)'] = {
        'Североморские запасы еды (пони/день)':360,
        }

metadict_detail['Среднеземные запасы (пони/год)'] = {
        'Среднеземные запасы еды (пони/день)':360,
        }

metadict_detail['Южноморские запасы (пони/год)'] = {
        'Южноморские запасы еды (пони/день)':360,
        }

metadict_detail['Североморские запасы еды (пони/день)'] = {
        # TODO:
            # Меню изменилось. Перепилить
        'Чечевица сухая (грамм)':50,
        'Зерно овса (грамм)':100,
        'Зерно ячменя (грамм)':100,
        'Зерно пшеницы (грамм)':100,
        'Зерно ржи (грамм)':200,
        'Семена подсолнечника (грамм)':50,
        'Семена льна (грамм)':25,
        }

metadict_detail['Среднеземные запасы еды (пони/день)'] = {
        'Бобы арахиса в шелухе (грамм)':100,
        'Сухофрукты среднеземные (грамм)':50,
        'Чечевица сухая (грамм)':50,
        'Фасоль сухая (грамм)':50,
        'Зерно овса (грамм)':100,
        'Зерно пшеницы (грамм)':200,
        'Зерно кукурузы (грамм)':400,
        'Зерно риса посевного (грамм)':50,
        'Семена подсолнечника (грамм)':50,
        'Масло оливковое (грамм)':50,
        }

metadict_detail['Южноморские запасы еды (пони/день)'] = {
        # TODO:
            # Меню изменилось. Перепилить
        'Морская капуста сушёная (грамм)':10,
        'Бобы арахиса в шелухе (грамм)':25,
        'Соя сухая шлифованная (грамм)':50,
        'Сухофрукты среднеземные (грамм)':25,
        'Чечевица сухая (грамм)':50,
        'Фасоль сухая (грамм)':25,
        'Зерно пшеницы (грамм)':150,
        'Зерно кукурузы (грамм)':100,
        'Зерно риса посевного (грамм)':200,
        'Семена подсолнечника (грамм)':50,
        'Семена кунжута (грамм)':50,
        'Масло оливковое (грамм)':25,
        }

#----

metadict_detail['Снабжение для Белой гавани (зебры/год)'] = {
        # TODO:
            # Расчёты готовы, можно убрать
        # Для полумиллиона полосатых.
        'Посевы для Белой гавани (зебры/год)':500000,
        }

metadict_detail['Посевы для Белой гавани (зебры/год)'] = {
        'Урожай с полей восточной колонии (зебры/день)':360,
        }

metadict_detail['Урожай с полей восточной колонии (зебры/день)'] = {
        'Бобы арахиса в шелухе (грамм)':150,
        'Зерно пшеницы (грамм)':100,
        'Зерно кукурузы (грамм)':250,
        }
