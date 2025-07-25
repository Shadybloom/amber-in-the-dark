#----
# Водоснабжение (коррекция величин):

metadict_model['-Городское водоснабжение (литр)'] = {
        '-Городское водоснабжение (кубометр)':1 / 1000,
        }

metadict_model['-Сельское водоснабжение (литр)'] = {
        '-Сельское водоснабжение (кубометр)':1 / 1000,
        }

metadict_model['-Городское водоснабжение (кубометр)'] = {
        'Городское водоснабжение (кубометр/сутки)':1 / 360,
        'Вода водопроводная (кубометр)':1,
        }

metadict_model['-Сельское водоснабжение (кубометр)'] = {
        'Сельское водоснабжение (кубометр/сутки)':1 / 360,
        'Вода колодезная (кубометр)':1,
        }

#----
# Городской водопровод:

metadict_model['Сельское водоснабжение (кубометр/сутки)'] = {
        # TODO: Сельское водоснабжение. Кроме шахтных колодцев много скважин.
            # https://ru.wikisource.org/wiki/ЭСБЕ/Артезианский_колодезь
        # Производительность 0.5-3 кубометра/час (42 кубометра/сутки)
        # Используется на 15%
        'Шахтный колодец (эксплуатация)':1 / 42 / 0.15,
        }

metadict_model['Шахтный колодец (эксплуатация)'] = {
        'Отделка шахтного колодца':1,
        'Обслуживание шахтных колодцев':1,
        'Строительство шахтных колодцев':1 / 30,
        }

metadict_model['Обслуживание шахтных колодцев'] = {
        # TODO: Обслуживание шахтных колодцев. Ремонт и чистка фильтра.
        }

metadict_model['Строительство шахтных колодцев'] = {
        'Шахтный колодец (смета)':1,
        }

#----
# Городской водопровод:
    # Лондонский водопровод:
    # 1866 год -- 0.47 водопроводных кранов, считая колонки на улицах
    # 1870 год -- вода и канализация в каждом доме дороже >35 фунтов/год
    # 1900 год -- плата за воду 1.5-4 фунтов/год (14-38 рублей/год)
    # Часовое потребление днём -- 10% от суточного.
    # Значит нужно нам 0.05 кубометра в час на каждую пони на уровне районных и уличных трубопроводов.
    # - Труба с радиусом 0.05 метра -- 0.008 квадратных метра (28 кубометров/час, 500 пони, квартал)
    # - Труба с радиусом 0.10 метра -- 0.03 квадратных метра (113 кубов/час, 5 кварталов)
    # - Труба с радиусом 0.15 метра -- 0.07 квадратных метра (252 куба/час, 10 кварталов)
    # - Труба с радиусом 0.2 метра -- 0.125 квадратных метра (450 кубов/час, весь город)
    # - Труба с радиусом 0.3 метра -- 0.28 квадратных метра (1000 кубов/час, два города)
    # - Труба с радиусом 0.7 метра -- 1.54 квадратных метра (5500 кубов/час, мегаполис)

metadict_model['Городское водоснабжение (кубометр/сутки)'] = {
        # Водопровод используется на 75%
        'Городской водопровод (эксплуатация) (кубометров/сутки)':1 / 0.75,
        }

metadict_model['Городской водопровод (эксплуатация) (кубометров/сутки)'] = {
        # Водопровод рассчитан на очистку 3500 кубометров/сутки
        'Городской водопровод (эксплуатация)':1 / 3500,
        }

metadict_model['Городской водопровод (эксплуатация)'] = {
        'Городской водопровод (обслуживание)':1,
        'Городской водопровод (строительство)':1 / 30,
        }

metadict_model['Городской водопровод (обслуживание)'] = {
        # TODO: Городской водопровод (обслуживание).
            # Перенеси сюда оборудование водопровода.
            # Фильтры чистят и пополняют раз в несколько месяцев.
            # https://ru.wikisource.org/wiki/ЭСБЕ/Снабжение_городов_водой
            # https://ru.wikisource.org/wiki/ЭСБЕ/Фильтр
        # Питерский водопровод начала 1920-х годов -- 1000 вёдер воды требует 15 минут времени рабочих
            # Тысяча вёдер, это 12.3 тонн воды, 49.2 тонны/час работы (0.02 нормо-часа/тонну)
            # В сутки 3500 тонн воды, 360 дней в году.
            # https://istmat.org/node/27934
        # Немного статистики, обслуживание труб.
        '_-Работа водопроводчика (нормо-часов)':3500 * 0.02 * 360,
        '-Городской водопровод, магистральные трубы (эксплуатация) (метр)':1000 + 1000,
        '-Городской водопровод, районные трубы (эксплуатация) (метр)':1000 + (1000 + 1500) * 2,
        '-Городской водопровод, уличные трубы (эксплуатация) (метр)':14 * 2500,
        }

metadict_model['Городской водопровод (строительство)'] = {
        'Городской водопровод (смета)':1,
        }

#----
# Строительство, городской водопровод:
    # СП 31.13330.2012 Водоснабжение. Наружные сети и сооружения.
    # http://docs.cntd.ru/document/1200093820
    # СНиП 2.04.02-84* ВОДОСНАБЖЕНИЕ НАРУЖНЫЕ СЕТИ И СООРУЖЕНИЯ
    # http://soyuzproekt.ru/ntd/879.htm
    # Н. Н. АБРАМОВ "Водоснабжение"
    # http://www.bibliotekar.ru/spravochnik-15/index.htm
    # https://ru.wikisource.org/wiki/ЭСБЕ/Снабжение_городов_водой
    # https://ru.m.wikipedia.org/wiki/Московский_водопровод
    # https://ru.wikisource.org/wiki/ЭСБЕ/Акведук

metadict_model['Городской водопровод (смета)'] = {
        # Первый мытищинский водопровод (1779-1805, 1826-1835 годы):
            # Строительство (1779-1805 гг): 1.7 млн рублей
            # Водоснабжение (после 1835): 2 500 тонн/сутки
            # https://ru.wikisource.org/wiki/ЭСБЕ/Москва
        # Второй мытищинский водопровод
            # Водоснабжение: +22 140 тонн/сутки
        # Третий мытищинский водопровод:
            # Строительство (1897-1906 гг): 5.5 млн рублей (5.3 рубля/жителя)
            # Водоснабжение (после 1906): +18 450 тонн/сутки
            # Доход: -- сбор 500 000 рублей/год (0.5 рубля/жителя)
            # Чертёж водопроводной сети:
                # Москва (3 мили диаметром, 1.037 млн человек, 1896 год)
                # - Воробьёвский резервуар (1902 год) -- 170 000 кубометров воды.
                # - Две магистрали к городу (24 дюйма, 0.61 метра) -- 18 километров
                # - Кольцевая магистраль вокруг Москвы (14 дюймов, 0.356 метра) -- 15.5 км
                # - Пять магистралей пересекающих город (10 дюймов, 0.254 метра) -- 26 км
                # - Множество малых труб, но густота их невелика (150x400 метров) -- ~163 км
                # Общая длина сети -- 115 километров, план 213 км
                # Стоимость водопроводной сети (оценочно) -- 50-70% стоимости водопровода.
                # https://nilsky-nikolay.livejournal.com/1477990.html?nojs=1
                # https://ic.pics.livejournal.com/nilsky_nikolay/24750888/84704/84704_original.jpg
                # https://alex-avr2.livejournal.com/212771.html
                # http://tmp.avr.net.ru/m3/zimin1908.pdf
                # https://alex-avr2.livejournal.com/95935.html
                # https://alex-avr2.livejournal.com/95734.html
        'Конструкция городского водопровода (смета)':1,
        #'Оборудование городского водопровода':1,
        #'Отделка городского водопровода':1,
        }

metadict_model['Конструкция городского водопровода (смета)'] = {
        # TODO: Конструкция городского водопровода. Допилить детали.
            # Нужны выпуски в нижней части сети и воздушные вантузы в верхней.
            # В московском водопроводе 1900 года масса уличных труб была в 4 раза больше, чем городских.
        # Размеры города (10 000 жителей) 500x2500 метров (5x10 кварталов, 100x250 метров/квартал)
            # Городской водопровод ведёт от водозабора к водоочистной и водонапорной станции.
            # Районные водопроводы пересекают город поперёк в 3 местах и замыкают кольцо.
            # Уличные водопроводы пересекают город вдоль улиц.
        'Водозаборная станция (смета)':1,
        'Водоочистная станция (смета)':1,
        'Водонапорная станция (смета)':1,
        'Водоподъёмная станция (смета)':2,
        'Водопровод городской (метр)':1000 + 1000,
        'Водопровод районный (метр)':1000 + (1000 + 1500) * 2,
        'Водопровод уличный (метр)':14 * 2500,
        }

#----
# Строительство, водоочистные станции:

metadict_model['Водоочистная станция (смета)'] = {
        # https://ru.wikisource.org/wiki/ЭСБЕ/Фильтр
        # https://ru.m.wikipedia.org/wiki/Медленные_фильтры
        'Конструкция водоочистной станции':1,
        #'Оборудование водоочистной станции':1,
        #'Отделка водоочистной станции':1,
        }

metadict_model['Конструкция водоочистной станции'] = {
        # http://www.another.kiev.ua/starinnoe-podzemnoe-vodoxranilishhe-xix-veka-v-kieve/
        # https://mishanik-210.livejournal.com/1586.html
        # -------------------------------|
        # |..............................|
        # |..............................|
        # |==============================|
        # |..............................|
        # |..............................|
        # |==============================|
        # |..............................|
        # |..............................|
        # |==============================|
        # |..............................|
        # |..............................|
        # -------------------------------|
        'Внешняя стена водного резервуара (метр)':(61 * 2) + (6 * 2) * 4,
        'Камера водного резервуара (6x60x3 метра)':4,
        'Перегородка водного резервуара (метр)':60 * 3,
        }

metadict_model['Оборудование водоочистной станции'] = {
        'Медленный фильтр (6x60 метров)':4,
        }

metadict_model['Медленный фильтр (6x60 метров)'] = {
        # Отделения фильра (площадь) -- 700-2000 кв.метров
        # Скорость фильтрации (на квадратный метр) -- 0.1 кубометра/час
        # Камера 6x60x3 метра, площадь фильтра 360 кв.метров (860 кубометров/сутки)
        '-Очистка воды (кубометров/сутки)':2.4 * (6 * 60),
        'Медленный фильтр (квадратный метр)':6 * 60,
        }

#----
# Строительство, водозаборные станции:

metadict_model['Водозаборная станция (смета)'] = {
        # TODO: Водозаборная станция. Допилить. Пока заглушка.
            # У тебя есть подробнейшией данные о строительстве Московского водопровода того времени.
        #'Конструкция водозаборной станции':1,
        #'Оборудование водозаборной станции':1,
        #'Отделка водозаборной станции':1,
        }

#----
# Строительство, водоподъёмные станции:

metadict_model['Водоподъёмная станция (смета)'] = {
        # TODO: Водоподъёмная станция. Допилить. Пока заглушка.
        #'Конструкция водоподъёмной станции':1,
        #'Оборудование водоподъёмной станции':1,
        #'Отделка водоподъёмной станции':1,
        }

#----
# Строительство, водонапорные станции:

metadict_model['Водонапорная станция (смета)'] = {
        # Заглублённый бассейн, должен стоять метров на 20 выше города.
        # Сглаживает дневной пик потребления воды, облегчая работу насосам.
        'Конструкция водонапорной станции':1,
        #'Оборудование водонапорной станции':1,
        #'Отделка водонапорной станции':1,
        }

metadict_model['Конструкция водонапорной станции'] = {
        # Резервуар 18x30x3 метров.
        # ----------------|
        # |...............|
        # |...............|
        # |===============|
        # |...............|
        # |...............|
        # |===============|
        # |...............|
        # |...............|
        # ----------------|
        'Внешняя стена водного резервуара (метр)':(31 * 2) + (6 * 2) * 3,
        'Камера водного резервуара (6x30x3 метра)':3,
        'Перегородка водного резервуара (метр)':30 * 3,
        }

metadict_model['Оборудование водонапорной станции'] = {
        'Водный резервуар (6x30x3 метров)':3,
        }

metadict_model['Водный резервуар (6x30x3 метров)'] = {
        '-Хранение питьевой воды (кубометров)':6 * 30 *3,
        }

#----
# Строительство, водопроводы:

metadict_model['Водопровод магистральный (метр)'] = {
        # TODO: Водопровод магистральный. Допилить.
            # Трубопрвод должен быть железобетонным/глиняным/кирпичным.
            # Своды в два кирпича. Обязательно бутовое/щебёночное основание.
            # Простой траншеей тут не обойтись.
        # 200 000 жителей (5500 кубометров/час)
        # Диаметр трубы (внутренний) 1.4 метра (наружный 2 метра). Профиль траншеи: 2x3x5.
        # Площадь трапеции: S = 1/2 * (a + b) * h
        '_-Траншея (кубометр)':(1/2 * (2 + 3) * 5),
        '_-Насыпь (кубометр)':(1/2 * (2 + 3) * 5) - 3.14159265 * (2 / 2) ** 2,
        'Устройство 1400-мм кирпичной водопропускной трубы (метр)':1,
        '_-Устройство гравийного основания под трубопроводы (кубометр)':2,
        }

metadict_model['Водопровод городской (метр)'] = {
        # 20 000 жителей (450 кубометров/час)
        # Диаметр трубы (внутренний) 0.4 метра (наружный 0.43 метра). Профиль траншеи: 0.8x2x3.
        '_-Разборка щебёночного шоссе (квадратный метр)':2,
        '_-Траншея (кубометр)':(1/2 * (0.8 + 2) * 3),
        '_-Прокладка 400-мм водопровода (метр)':1,
        '_-Установка фасонных частей 400-мм водопровода (штук)':1 / 20,
        '_-Насыпь (кубометр)':(1/2 * (0.8 + 2) * 3) \
                - 3.14159265 * (0.43 / 2) ** 2,
        '_-Вывоз грунта (кубометр)':3.14159265 * (0.43 / 2) ** 2,
        '_-Восстановление щебёночного шоссе, двухслойного (квадратный метр)':2,
        }

metadict_model['Водопровод районный (метр)'] = {
        # 5000 жителей (113 кубометров/час)
        # Диаметр трубы (внутренний) 0.2 метра (наружный 0.23 метра). Профиль траншеи: 0.6x2x3.
        '_-Разборка булыжной мостовой (квадратный метр)':2,
        '_-Траншея (кубометр)':(1/2 * (0.6 + 2) * 3),
        '_-Прокладка 200-мм водопровода (метр)':1,
        '_-Установка фасонных частей 200-мм водопровода (штук)':1 / 20,
        '_-Насыпь (кубометр)':(1/2 * (0.6 + 2) * 3) \
                - 3.14159265 * (0.23 / 2) ** 2,
        '_-Вывоз грунта (кубометр)':3.14159265 * (0.23 / 2) ** 2,
        '_-Восстановление булыжной мостовой (квадратный метр)':2,
        }

metadict_model['Водопровод уличный (метр)'] = {
        # 1000 жителей (28 кубометров/час)
        # Диаметр трубы (внутренний) 0.1 метра (наружный 0.12 метра). Профиль траншеи: 0.5x2x3.
        '_-Разборка булыжной мостовой (квадратный метр)':2,
        '_-Траншея (кубометр)':(1/2 * (0.5 + 2) * 3),
        '_-Прокладка 100-мм водопровода (метр)':1,
        '_-Установка фасонных частей 100-мм водопровода (штук)':1 / 20,
        '_-Насыпь (кубометр)':(1/2 * (0.5 + 2) * 3) \
                - 3.14159265 * (0.12 / 2) ** 2,
        '_-Вывоз грунта (кубометр)':3.14159265 * (0.12 / 2) ** 2,
        '_-Восстановление булыжной мостовой (квадратный метр)':2,
        }

#----
# Строительство, сбор дождевой воды:

metadict_model['Водоотвод с крыши (8x8 метров)'] = {
        # TODO: водоотвод с крыши даёт 100 литров/домохозяйство селянам при 800 мм/год осадков.
        # https://upload.wikimedia.org/wikipedia/commons/1/15/Wei%C3%9Fes_Wohnhaus_in_Schwetzingen_2010.JPG
            # 1) Желоб из оцинкованной стали
            # 2) Водопроводная труба с крыши
            # 3) Цистерна для воды на подставке
            # 4) Водопроводная труба в дом
        # Можно собрать 60-80% выпадающей влаги:
            # https://ru.wikisource.org/wiki/ЭСБЕ/Снабжение_городов_водой
            # При осадках в 800 мм/год за сутки это даёт: 0.8 / 360 * (8 * 8) * 0.7 = 0.1 кубометра
        '_-Прокладка 150-мм водосточной трубы (метр)':6 + 1,
        'Кровля из оцинкованной стали (квадратный метр)':(8 + 8) * 2 * 0.2,
        }

#----
# Строительство, шахтные колодцы:

metadict_model['Шахтный колодец (смета)'] = {
        # Производительность 0.5-3 кубометра/час
            # https://ru.wikisource.org/wiki/ЭСБЕ/Снабжение_городов_водой
            # https://www.parthenon-house.ru/content/articles/index.php?article=5155
            # http://gardenweb.ru/shakhtnye-kolodtsy
        'Конструкция шахтного колодца':1,
        #'Оборудование шахтного колодца':1,
        #'Отделка шахтного колодца':1,
        }

metadict_model['Конструкция шахтного колодца'] = {
        # http://www.mukhin.ru/stroysovet/voda/2_06.html
        # 1) Котлован с диаметром 3.25 метра и глубиной 1.5 метра.
        # 2) Слой глины 1-2 метра вокруг скважины до глубины 1.5 метра.
        # 3) Копание колодца с диаметром 1.25 метра на грубину 15 метров.
        # 4) Кирпичная кладка в 1 кирпич (площадь вычисляем по периметру и глубине шахты)
        # 6) Глино-соломенная кровля (конусообразная, высотой в 1.5 метра)
        # 7) Вентиляция шахты.
        '_-Котлован (кубометр)':3.14159265 * (((1.250 + 2) / 2) ** 2) * 1.5,
        '_-Устройство глиняного замка (кубометр)':(3.14159265 * (((1.250 + 2) / 2) ** 2) * 1.5) \
                - (3.14159265 * ((1.250 / 2) ** 2)) * 1.5,
        '_-Сооружение шахтных колодцев (кубометр)':(3.14159265 * ((1.250 / 2) ** 2)) * 15,
        '_-Вывоз грунта (кубометр)':3.14159265 * (((1.250 + 2) / 2) ** 2) * 1.5 \
                + (3.14159265 * ((1.250 / 2) ** 2)) * 15,
        '_-Кирпичная кладка сводов в 1 кирпич (квадратный метр)':(2 * 3.14159265 * (1.250 / 2)) * 15,
        'Простая стропильная система (2x2 метра)':1,
        'Соломенная кровля (квадратный метр)':3.14159265 * ((1.250 + 0.75) / 2) * 1.5,
        '_-Прокладка 150-мм вытяжной трубы (метр)':2,
        }

metadict_model['Оборудование шахтного колодца'] = {
        '_-Устройство донного фильтра копателем (штука)':1,
        'Медленный фильтр (квадратный метр)':(3.14159265 * ((1.250 / 2) ** 2)),
        }

metadict_model['Отделка шахтного колодца'] = {
        '|Механизм гидравлический (насос, 35 литров/минуту)':1,
        }

#----
# Компостные ямы:

metadict_model['Люфт-клозет'] = {
        # Нехитрая система, где сточные воды кое-как очищаются и уходят в почву,
        # А смешанные с торфом твёрдые отходы остаются в ближней камере компостной ямы.
        # http://www.bibliotekar.ru/spravochnik-81/29.htm
        'Конструкция люфт-клозета':1,
        'Оборудование люфт-клозета':1,
        }

metadict_model['Конструкция люфт-клозета'] = {
        'Внешняя стена компостной ямы (метр)':(4 * 1) * 2,
        'Камера компостной ямы (4x1x2 метра)':1,
        }

metadict_model['Оборудование люфт-клозета'] = {
        # Большинство туалетов были "торфяными"
        # - Торф обеззораживает нечистоты (поглощает воду x8 веса, аммиак, сероводород)
            # Торфяные клозеты (1 кг торфа на 4-6 кг нечистот)
            # Торф + 2-5% серной кислоты = сильное дезинфицирующее средство
            # https://ru.wikisource.org/wiki/ЭСБЕ/Торф,_в_санитарном_отношении
        '_-Прокладка 150-мм трубопровода канализации (метр)':6,
        'Медленный фильтр (квадратный метр)':2,
        }

metadict_model['Внешняя стена компостной ямы (метр)'] = {
        # TODO: Камера люфт-клозета. Высота должна увеличиваться, наклон же.
        # Профиль траншеи: 0.5x1x2.
        # Площадь трапеции: S = 1/2 * (a + b) * h
        '_-Траншея (кубометр)':(1/2 * (0.5 + 1) * 1.5),
        '_-Обваловка (кубометр)':0.5 * (1/2 * (0.5 + 1) * 1.5),
        '_-Вывоз грунта (кубометр)':0.5 * (1/2 * (0.5 + 1) * 1.5),
        '_-Устройство основания под фундаменты (кубометр)':0.5 * 0.25,
        '_-Устройство каменного ленточного фундамента (кубометр)':0.25 * 1.25,
        '_-Гидроизоляция боковая оклеенная (квадратный метр)':2,
        '_-Устройство глиняного замка (кубометр)':2 * 0.2,
        }

metadict_model['Камера компостной ямы (4x1x2 метра)'] = {
        # ------
        # |==  |
        # ------
        '_-Котлован (кубометр)':4 * 2,
        '_-Вывоз грунта (кубометр)':0.75 * 4 * 2,
        '_-Устройство подстилающего слоя (кубометр)':4 * 0.25,
        '_-Гидроизоляция горизонтальная оклеенная (квадратный метр)':2,
        '_-Устройство перегородок дощатых (квадратный метр)':4,
        '_-Насыпь (кубометр)':0.25 * 4 * 2,
        }

#metadict_model['Компостная камера люфт-клозета (3 кубометра)'] = {
#        # Фактически, две камеры: фекалии стекают в дальнюю, а ближняя для золы и кухонных отходов.
#        # Дымовая кирпичная труба в системе, это вытяжка, что ставится рядом с печной.
#        # Сверху траншея прикрыта накатником и слоем глины, стенки кирпичные.
#        '_-Котлован (кубометр)':(0.5 * 2 * 0.5) + (1.25 * 2 * 1) + (1.5 * 2 * 1),
#        '_-Вывоз грунта (кубометр)':(0.5 * 2 * 0.5) + (1.25 * 2 * 1) + (1.5 * 2 * 1),
#        '_-Кирпичная кладка в 0.5 кирпича (квадратный метр)':2 * (0.5*2 + 0.5*0.5) + 2 * (1.25*2 + 1.25*1) + 2 * (1.5*2 + 1.5*1),
#        'Накатник диаметром 80 мм (метр)':2 * (6/0.5),
#        '_-Устройство глиняного замка (кубометр)':(6 + 1) * 2 * 1.25 * 0.2,
#        '_-Устройство подстилающего слоя (кубометр)':(0.1 * 6 * 1) * 2,
#        '_-Кладка дымовых кирпичных труб (кубометр)':0.2 * (2 + 4 + 0.5 - 1),
#        }

#----
# Сложные элементы зданий:

metadict_model['Камера водного резервуара (6x60x3 метра)'] = {
        # 1) Котлован 6x60x4 и столбчатый фундамент из бутового камня.
        # 2) Глиняно-печанное подстилающий слой и плита из железобетона.
        # 3) 36 кирпичных столбов и два полуцилиндрических свода.
        # 4) Насыпь из 0.25 извлечённого грунта, 0.75 на вывоз.
        # https://upload.wikimedia.org/wikipedia/commons/5/54/Brockhaus_and_Efron_Encyclopedic_Dictionary_b70_862-2.jpg
        # |====1==1==1==1==1==1==1==1==1==1==1==1==1==1==1==1==1==1====|
        # |............................................................|
        # |............................................................|
        # 0....1..1..1..1..1..1..1..1..1..1..1..1..1..1..1..1..1..1....0
        # |............................................................|
        # |............................................................|
        # --------------------------------------------------------------
        '_-Котлован (кубометр)':(6 * 60 * 4) \
                + 36 * (1.2 * 1.2 * 1),
        '_-Вывоз грунта (кубометр)':0.75 * ((6 * 60 * 4) \
                + 36 * (1.2 * 1.2 * 1)),
        '_-Устройство основания под фундаменты (кубометр)':36 * (1.2 * 1.2 * 0.5),
        '_-Устройство каменного столбового фундамента (кубометр)':36 * (1.2 * 1.2 * 0.5),
        '_-Устройство подстилающего слоя (кубометр)':(6 * 60 * 0.5) \
                - 36 * (1.2 * 1.2 * 0.5),
        'Железобетон тяжёлый (кубометр)':(6 * 60 * 0.5) \
                - 36 * (0.8 * 0.8 * 0.5),
        '_-Гидроизоляция горизонтальная оклеенная (квадратный метр)':(6 * 60) \
                - 36 * (0.8 * 0.8),
        '_-Кирпичная кладка столбов в 3 кирпича (метр)':36 * 0.5,
        '_-Кирпичная кладка столбов в 2 кирпича (метр)':36 * 3,
        '_-Кирпичная кладка сводов в 0.5 кирпича (квадратный метр)':2 * (3.14159265 * 1.5) * 60,
        '_-Насыпь (кубометр)':0.25 * ((6 * 60 * 4) \
                + 36 * (1.2 * 1.2 * 1)),
        }

metadict_model['Камера водного резервуара (6x30x3 метра)'] = {
        # |====1==1==1==1==1==1==1==1==1=|
        # |..............................|
        # |..............................|
        # 0....1..1..1..1..1..1..1..1..1.0
        # |..............................|
        # |..............................|
        # --------------------------------
        '_-Котлован (кубометр)':(6 * 30 * 4) \
                + 18 * (1.2 * 1.2 * 1),
        '_-Вывоз грунта (кубометр)':0.75 * ((6 * 30 * 4) \
                + 18 * (1.2 * 1.2 * 1)),
        '_-Устройство основания под фундаменты (кубометр)':18 * (1.2 * 1.2 * 0.5),
        '_-Устройство каменного столбового фундамента (кубометр)':18 * (1.2 * 1.2 * 0.5),
        '_-Устройство подстилающего слоя (кубометр)':(6 * 30 * 0.5) \
                - 18 * (1.2 * 1.2 * 0.5),
        'Железобетон тяжёлый (кубометр)':(6 * 30 * 0.5) \
                - 18 * (0.8 * 0.8 * 0.5),
        '_-Гидроизоляция горизонтальная оклеенная (квадратный метр)':(6 * 30) \
                - 18 * (0.8 * 0.8),
        '_-Кирпичная кладка столбов в 3 кирпича (метр)':18 * 0.5,
        '_-Кирпичная кладка столбов в 2 кирпича (метр)':18 * 3,
        '_-Кирпичная кладка сводов в 0.5 кирпича (квадратный метр)':2 * (3.14159265 * 1.5) * 30,
        '_-Насыпь (кубометр)':0.25 * ((6 * 30 * 4) \
                + 18 * (1.2 * 1.2 * 1)),
        }

metadict_model['Внешняя стена водного резервуара (метр)'] = {
        # 1) Траншея и ленточный фундамент из бутового камня.
        # 2) Стена высотой: 0.5 метра в основании; 3 метра до уровня воды; 1.5 метра в сводах.
        # 3) Внешняя и внутренняя гидроизоляция.
        # 4) Обваловка стены.
        # Профиль траншеи: 1.2x3x4.5.
        # Площадь трапеции: S = 1/2 * (a + b) * h
        '_-Траншея (кубометр)':(1/2 * (1.2 + 3) * 4.5),
        '_-Вывоз грунта (кубометр)':0.75 * (1/2 * (1.2 + 3) * 4.5),
        '_-Устройство основания под фундаменты (кубометр)':1.2 * 0.5,
        '_-Устройство каменного ленточного фундамента (кубометр)':1.2 * 0.5,
        '_-Кирпичная кладка в 3 кирпича (квадратный метр)':0.5,
        '_-Кирпичная кладка в 2.5 кирпича (квадратный метр)':3,
        '_-Кирпичная кладка в 1.5 кирпича (квадратный метр)':1.5,
        '_-Гидроизоляция боковая оклеенная (квадратный метр)':3 * 2,
        '_-Устройство глиняного замка (кубометр)':4 * 0.5,
        '_-Обваловка (кубометр)':0.25 * (1/2 * (1.2 + 3) * 4.5),
        }

metadict_model['Перегородка водного резервуара (метр)'] = {
        # Высота камеры -- 3 метра.
        '_-Кирпичная кладка в 1.5 кирпича (квадратный метр)':3,
        '_-Гидроизоляция боковая оклеенная (квадратный метр)':3 * 2,
        }

metadict_model['Медленный фильтр (квадратный метр)'] = {
        # Кварцевый песок (24 дюйма) -- 0.610 метра
        # Крупный песок (3 дюйма) -- 0.076 метра
        # Гравий (3 дюйма) -- 0.076 метра
        # Крупный гравий (4 дюйма) -- 0.102 метра
        # Крупный булыжник (8 дюймов) -- 0.203 метра
        'Песок кварцевый (кубометр)':0.610,
        'Песок крупный (кубометр)':0.076,
        'Гравий мелкий (кубометр)':0.076,
        'Гравий крупный (кубометр)':0.102,
        'Камень бутовый (кубометр)':0.203,
        }

#----
# Канализация:
    # План московской канализации (1896 год):
        # Планируется на 1.533 млн человек, 203 млн. литров нечистот (132 литра/жителя-день)
        # Строительство: 17.45 млн рублей (11.4 рубля/жителя) (из них 6.246 на покупку полей)
        # Поля покупаются, чтобы орошать их стоками после очистки известью и фильтрами.
        # Поля (1 гектар/250 человек, 12 500—25 000 кубометров/год) -- 6100 гектаров
    # Канализация, керамические трубы (Москва, 1901 год) -- 261 км (205.4 км 15.24 см диаметр)
        # - Диаметром 6" 15.24 см -- 96.280 (205.4 км)
        # - диаметром 10" 25.4 см -- 5.500 (11.7 км)
        # - диаметром 12" 30.48 см -- 3.540 (7.6 км)
        # - диаметром 14" 35.56 см -- 1.720 (3.7 км)
        # - диаметром 15" 38.1 см -- 520 (1.1 км)
        # - диаметром 18" 45.72 см -- 1.680 (3.6 км)
        # - диаметром 21" 53.34 см -- 2.800 (6 км)
        # Всего разных труб около 122.110 погонных сажен (261 км)
        # https://ljsear.ch/savedcopy?post=691317646
        # https://leonovvaleri.livejournal.com/126067.html
    # Стоимость каналиазации по списку из 10 европейских городов (усреднённо):
        # Длина водостоков -- 0.64 метра/жителя; 140 метров/гектар города
        # Стоимость устройства -- 22.7 рубля/жителя, 37 рублей/метр водостоков
        # Стоимость содержания (водостоков) -- 0.21 рубля/жителя
        # Стоимость содержания (машин) -- 0.14 рубля/жителя
        # https://ru.wikisource.org/wiki/ЭСБЕ/Канализация
