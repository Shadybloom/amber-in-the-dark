#----
# Строительные материалы (объём --> штучные):
    # 1 квадратный метр пропила = 1 нормо-час (пилами)
    # Лесопильные станки с круглыми пилами (7-11 кВт) -- 500-2500 квадратных метров пропила/день
    # Кубометр бруса 50x150x6000 мм = 33 нормо-часа (пилами)
    # Кубометр бруса 150x150x6000 мм = 20 нормо-часов (пилами)
    # Кубометр доски 25x150x6000 мм = 54 нормо-часов (пилами)
    # Кубометр бруса 50x50x600 мм = 90 нормо-часов (пилами)

metadict_model['Бруски обрезные хвойные 180x180x6000 мм (кубометр)'] = {
        'Брус обрезной 180x180x6000 мм (штук)':1 / (0.18 * 0.18 * 6),
        }

metadict_model['Бруски обрезные хвойные 100x150x6000 мм (кубометр)'] = {   
        'Брус обрезной 100x150x6000 мм (штук)':1 / (0.10 * 0.15 * 6),
        }

metadict_model['Бруски обрезные хвойные 100x100x6000 мм (кубометр)'] = {
        'Брус обрезной 100x100x6000 мм (штук)':1 / (0.10 * 0.10 * 6),
        }

metadict_model['Бруски обрезные хвойные 50x100x6000 мм (кубометр)'] = {
        'Брус обрезной 50x100x6000 мм (штук)':1 / (0.05 * 0.10 * 6),
        }

metadict_detail['Горбыль деловой хвойный 30x100x6000 мм (кубометр)'] = {
        'Горбыль деловой хвойный 30x100x6000 мм (штук)':1 / (0.03 * 0.10 * 6),
        }

metadict_model['Доски необрезные хвойные 50x100x6000 мм (кубометр)'] = {
        # Доска 40x100 может нести нагрузку в 300 кг.
        'Доска необрезная 50x100x6000 мм (штук)':1 / (0.05 * 0.10 * 6),
        }

metadict_model['Доски обрезные хвойные 10x100x6000 мм (кубометр)'] = {
        'Доска обрезная 10x100x6000 мм (штук)':1 / (0.01 * 0.10 * 6),
        }

metadict_model['Доски обрезные хвойные 15x100x6000 мм (кубометр)'] = {
        'Доска обрезная 15x100x6000 мм (штук)':1 / (0.015 * 0.10 * 6),
        }

metadict_model['Доски обрезные хвойные 20x100x6000 мм (кубометр)'] = {
        'Доска обрезная 20x100x6000 мм (штук)':1 / (0.02 * 0.10 * 6),
        }

metadict_model['Доски обрезные хвойные 25x100x6000 мм (кубометр)'] = {
        'Доска обрезная 25x100x6000 мм (штук)':1 / (0.025 * 0.10 * 6),
        }

metadict_model['Доски обрезные хвойные 35x100x6000 мм (кубометр)'] = {
        'Доска обрезная 35x100x6000 мм (штук)':1 / (0.035 * 0.10 * 6),
        }

metadict_model['Доски обрезные хвойные 50x100x6000 мм (кубометр)'] = {
        'Доска обрезная 50x100x6000 мм (штук)':1 / (0.05 * 0.10 * 6),
        }

metadict_detail['Жерди диаметром 40 мм (кубометр)'] = {
        # 794 метра жердей на кубометр их объёма.
        # Жерди сечением 40 мм (площадь сечения 0.00126 кв.метра)
        'Жерди диаметром 40 мм (метр)':1 / (0.00126 * 1),
        }

#----
# Строительные материалы (площадь --> штучные):

metadict_model['Черепица фальцевая 360x180x15 мм (квадратный метр)'] = {
        # Производство керамической черепицы:
            # http://works.doklad.ru/view/xG7K2Qs8qQg/all.html
            # https://ru.wikisource.org/wiki/ЭСБЕ/Черепица
        # Длина 0.36 метра, ширина 0.18 (площадь 0.065 кв. метра, 16 на квадратный метр)
        # Толщина 0.015 (объём 0.001 кубометра, масса 1.6 килограмма)
        'Черепица фальцевая 360x180x15 мм (штук)':15,
        }

#----
# Строительные материалы (длина --> штучные):

metadict_model['Брус обрезной 180x180 мм (метр)'] = {
        'Брус обрезной 180x180x6000 мм (штук)':1 / 6,
        }

metadict_model['Брус обрезной 150x150 мм (метр)'] = {
        'Брус обрезной 150x150x6000 мм (штук)':1 / 6,
        }

metadict_model['Брус обрезной 100x150 мм (метр)'] = {
        'Брус обрезной 100x150x6000 мм (штук)':1 / 6,
        }

metadict_model['Брус обрезной 100x100 мм (метр)'] = {
        'Брус обрезной 100x100x6000 мм (штук)':1 / 6,
        }

metadict_model['Брус обрезной 50x150 мм (метр)'] = {
        # TODO: Брус обрезной 50x150 мм. Это доска.
        'Брус обрезной 50x150x6000 мм (штук)':1 / 6,
        }

metadict_model['Брус обрезной 50x100 мм (метр)'] = {
        'Брус обрезной 50x100x6000 мм (штук)':1 / 6,
        }

metadict_model['Брус обрезной 50x50 мм (метр)'] = {
        'Брус обрезной 50x50x6000 мм (штук)':1 / 6,
        }

metadict_detail['Штапик деревянный 19x19 мм (метров)'] = {
        'Штапик деревянный 19x19x6000 мм (штук)':1 / 6,
        }

metadict_model['Брёвна диаметром 300 мм (метр)'] = {
        # Типичные размеры. Диаметр по тонкому концу:
        # https://web.archive.org/web/https://saper.isnet.ru/fort/les.html
        'Брёвна диаметром 300 мм (6 метров)':1 / 6,
        }

metadict_model['Брёвна диаметром 250 мм (метр)'] = {
        'Брёвна диаметром 250 мм (6 метров)':1 / 6,
        }

metadict_model['Брёвна диаметром 200 мм (метр)'] = {
        'Брёвна диаметром 200 мм (6 метров)':1 / 6,
        }

metadict_model['Накатник диаметром 80 мм (метр)'] = {
        'Накатник диаметром 80 мм (6 метров)':1 / 6,
        }

metadict_detail['Жерди диаметром 50 мм, для бочек (метр)'] = {
        'Жерди диаметром 50 мм, для бочек (5 метров)':1 / 5,
        }

metadict_detail['Жерди диаметром 40 мм, для бочек (метр)'] = {
        'Жерди диаметром 40 мм, для бочек (4 метра)':1 / 4,
        }

metadict_model['Жерди диаметром 40 мм (метр)'] = {
        'Жерди диаметром 40 мм (4 метра)':1 / 4,
        }

metadict_detail['Жерди диаметром 30 мм, для бочек (метр)'] = {
        'Жерди диаметром 30 мм, для бочек (3 метра)':1 / 3,
        }

metadict_model['Хворост диаметром 20 мм (метр)'] = {
        'Хворост диаметром 20 мм (2 метра)':1 / 2,
        }

metadict_detail['Прутья ивовые диаметром 10 мм, грубые (метр)'] = {
        'Прутья ивовые диаметром 10 мм, грубые (1.2 метра)':1 / 1.2,
        }

metadict_detail['Прутья ивовые диаметром 10 мм, очищенные (метр)'] = {
        'Прутья ивовые диаметром 10 мм, очищенные (1.2 метра)':1 / 1.2,
        }

#----
# Строительные материалы (штучные --> объём):

metadict_model['Черепица фальцевая 360x180x15 мм (штук)'] = {
        'Черепица фальцевая 360x180x15 мм (кубометр)':0.36 * 0.18 * 0.015,
        }

metadict_model['Блок теплоизоляционного арболита (штука)'] = {
        # https://kblok.ru/blog/razmery-arbolita
        # https://upload.wikimedia.org/wikipedia/commons/5/50/Производство_арболитовых_блоков.jpg
        # Размер: 600x300x250 мм (22 блок на кубометр)
        'Арболит теплоизоляционный (кубометр)':0.6 * 0.3 * 0.25,
        }

metadict_model['Кирпич керамический (штука)'] = {
        # http://chzsm54.ru/brick
            # Размер: 120x250x65 мм (512 на кубометр)
            # Объём: 0.002 м³
            # Масса: 3.1 кг
        'Кирпич керамический (кубометр)':0.12 * 0.25 * 0.065,
        }

metadict_model['Брус обрезной 180x180x6000 мм (штук)'] = {
        # Брусья пилят вдоль и подравнивают поперёк (так мы вычислим работу лесопилок):
        'Брус обрезной (кубометр)':0.18 * 0.18 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.18 * 0.18) * 2 + (0.18 * 6) * 2 + (0.18 * 6) * 2,
        }

metadict_model['Брус обрезной 150x150x6000 мм (штук)'] = {
        'Брус обрезной (кубометр)':0.15 * 0.15 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.15 * 0.15) * 2 + (0.15 * 6) * 2 + (0.15 * 6) * 2,
        }

metadict_model['Брус обрезной 100x150x6000 мм (штук)'] = {
        'Брус обрезной (кубометр)':0.10 * 0.15 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.10 * 0.15) * 2 + (0.15 * 6) * 2 + (0.10 * 6) * 2,
        }

metadict_model['Брус обрезной 100x100x6000 мм (штук)'] = {
        # В бревне 4+ брусьев. Следовательно, две стороны обрабатываются за раз:
        'Брус обрезной (кубометр)':0.1 * 0.1 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.10 * 0.10) * 2 + (0.10 * 6) + (0.10 * 6),
        }

metadict_model['Брус обрезной 50x150x6000 мм (штук)'] = {
        'Брус обрезной (кубометр)':0.05 * 0.15 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.05 * 0.15) * 2 + (0.15 * 6) + (0.05 * 6),
        }

metadict_model['Брус обрезной 50x100x6000 мм (штук)'] = {
        'Брус обрезной (кубометр)':0.05 * 0.10 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.05 * 0.10) * 2 + (0.10 * 6) + (0.05 * 6),
        }

metadict_model['Брус обрезной 50x50x6000 мм (штук)'] = {
        'Брус обрезной (кубометр)':0.05 * 0.05 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.05 * 0.05) * 2 + (0.05 * 6) + (0.05 * 6),
        }

metadict_detail['Штапик деревянный 19x19 мм (метров)'] = {
        'Брус обрезной (кубометр)':0.019 * 0.019 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.019 * 0.019) * 2 + (0.019 * 6) + (0.019 * 6),
        }

metadict_detail['Горбыль деловой хвойный 30x100x6000 мм (штук)'] = {
        'Горбыль хвойный (кубометр)':0.03 * 0.1 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.03 * 0.10) * 2 + (0.03 * 6),
        }

metadict_model['Доска необрезная 50x100x6000 мм (штук)'] = {
        'Доска необрезная (кубометр)':0.05 * 0.1 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.05 * 0.10) * 2 + (0.05 * 6) * 2,
        }

metadict_model['Доска обрезная 50x100x6000 мм (штук)'] = {
        'Доска обрезная (кубометр)':0.05 * 0.10 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.05 * 0.10) * 2 + (0.10 * 6) + (0.05 * 6) * 2,
        }

metadict_model['Доска обрезная 35x100x6000 мм (штук)'] = {
        'Доска обрезная (кубометр)':0.035 * 0.10 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.035 * 0.10) * 2 + (0.10 * 6) + (0.035 * 6) * 2,
        }

metadict_model['Доска обрезная 25x100x6000 мм (штук)'] = {
        'Доска обрезная (кубометр)':0.025 * 0.10 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.025 * 0.10) * 2 + (0.10 * 6) + (0.025 * 6) * 2,
        }

metadict_model['Доска обрезная 20x100x6000 мм (штук)'] = {
        'Доска обрезная (кубометр)':0.020 * 0.10 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.020 * 0.10) * 2 + (0.10 * 6) + (0.020 * 6) * 2,
        }

metadict_model['Доска обрезная 15x100x6000 мм (штук)'] = {
        'Доска обрезная (кубометр)':0.015 * 0.10 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.015 * 0.10) * 2 + (0.10 * 6) + (0.015 * 6) * 2,
        }

metadict_model['Доска обрезная 10x100x6000 мм (штук)'] = {
        'Доска обрезная (кубометр)':0.010 * 0.10 * 6,
        '-Распил пиломатериалов (квадратный метр)':(0.010 * 0.10) * 2 + (0.10 * 6) + (0.010 * 6) * 2,
        }

metadict_model['Брёвна диаметром 300 мм (6 метров)'] = {
        # Брёвна хвойных пород сужаются примерно на 10 мм каждый метр длины.
            # Диаметр тонкого конца -- 30 см, диаметр толстого конца -- 36 см
        # Объём усечённого конуса: V = 1/3 * Pi * h * (r1 ** 2 + r1*r2 + r2 ** 2)
        'Лес круглый (кубометр)':1/3 * 3.14159265 * 6 * ((0.30/2) ** 2 +
            (0.30/2)*(0.36/2) + (0.36/2) ** 2),
        }

metadict_model['Брёвна диаметром 250 мм (6 метров)'] = {
        # Диаметр тонкого конца -- 25 см, диаметр толстого конца -- 31 см
        'Лес круглый (кубометр)':1/3 * 3.14159265 * 6 * ((0.25/2) ** 2 +
            (0.25/2)*(0.31/2) + (0.31/2) ** 2),
        }

metadict_model['Брёвна диаметром 200 мм (6 метров)'] = {
        # Диаметр тонкого конца -- 20 см, диаметр толстого конца -- 26 см
        'Лес круглый (кубометр)':1/3 * 3.14159265 * 6 * ((0.20/2) ** 2 +
            (0.20/2)*(0.26/2) + (0.26/2) ** 2),
        }

metadict_model['Накатник диаметром 80 мм (6 метров)'] = {
        # Диаметр тонкого конца -- 8 см, диаметр толстого конца -- 14 см
        'Лес круглый (кубометр)':1/3 * 3.14159265 * 6 * ((0.08/2) ** 2 +
            (0.08/2)*(0.14/2) + (0.14/2) ** 2),
        }

metadict_detail['Жерди диаметром 50 мм, для бочек (5 метров)'] = {
        # Диаметр тонкого конца -- 5 см, диаметр толстого конца -- 10 см
        'Лес круглый для бочек (кубометр)':1/3 * 3.14159265 * 5 * ((0.05/2) ** 2 +
            (0.05/2)*(0.10/2) + (0.10/2) ** 2),
        }

metadict_model['Жерди диаметром 40 мм (4 метра)'] = {
        # Диаметр тонкого конца -- 4 см, диаметр толстого конца -- 8 см
        'Лес круглый (кубометр)':1/3 * 3.14159265 * 4 * ((0.04/2) ** 2 +
            (0.04/2)*(0.08/2) + (0.08/2) ** 2),
        }

metadict_model['Жерди диаметром 40 мм, для бочек (4 метра)'] = {
        # Диаметр тонкого конца -- 4 см, диаметр толстого конца -- 8 см
        'Лес круглый для бочек (кубометр)':1/3 * 3.14159265 * 4 * ((0.04/2) ** 2 +
            (0.04/2)*(0.08/2) + (0.08/2) ** 2),
        }

metadict_detail['Жерди диаметром 30 мм, для бочек (3 метра)'] = {
        # Диаметр тонкого конца -- 3 см, диаметр толстого конца -- 6 см
        'Лес круглый для бочек (кубометр)':1/3 * 3.14159265 * 3 * ((0.03/2) ** 2 +
            (0.03/2)*(0.06/2) + (0.06/2) ** 2),
        }

metadict_model['Хворост диаметром 20 мм (2 метра)'] = {
        # Диаметр тонкого конца -- 2 см, диаметр толстого конца -- 4 см
        'Лес круглый (кубометр)':1/3 * 3.14159265 * 2 * ((0.02/2) ** 2 +
            (0.02/2)*(0.04/2) + (0.04/2) ** 2),
        }

metadict_detail['Прутья ивовые диаметром 10 мм, грубые (1.2 метра)'] = {
        # диаметр прутка у основания -- 1.2 см, в окончании -- 0.8 см
        'Прутья ивовые, грубые (кубометр)':1/3 * 3.14159265 * 1.2 * ((0.008/2) ** 2 +
            (0.008/2)*(0.012/2) + (0.012/2) ** 2),
        }

metadict_detail['Прутья ивовые диаметром 10 мм, очищенные (1.2 метра)'] = {
        # Получаются из прутьев диаметром 12-15 мм после очистки коры (теряется 56% объёма)
        'Прутья ивовые, очищенные (кубометр)':1/3 * 3.14159265 * 1.2 * ((0.008/2) ** 2 +
            (0.008/2)*(0.010/2) + (0.010/2) ** 2),
        }

#----
# Строительные материалы (длина --> масса):

metadict_model['Чугунная труба напорная 50-мм (метр)'] = {
        # http://vse-o-trubah.ru/massa-chugunnoj-truby.html
        'Литьё чугунное, трубы (килограмм)':11,
        }

metadict_model['Чугунная труба напорная 100-мм (метр)'] = {
        'Литьё чугунное, трубы (килограмм)':25,
        }

metadict_model['Чугунная труба напорная 150-мм (метр)'] = {
        'Литьё чугунное, трубы (килограмм)':40,
        }

metadict_model['Чугунная труба напорная раструбная 100-мм (метр)'] = {
        # Трубы класса Б:
        # http://docs.cntd.ru/document/1200003069
        'Литьё чугунное, трубы (килограмм)':22.3,
        }

metadict_model['Чугунная труба напорная раструбная 200-мм (метр)'] = {
        # Трубы класса Б:
        # http://docs.cntd.ru/document/1200003069
        'Литьё чугунное, трубы (килограмм)':52.9,
        }

metadict_model['Чугунная труба напорная раструбная 400-мм (метр)'] = {
        'Литьё чугунное, трубы (килограмм)':141.4,
        }

metadict_model['Чугунная труба безнапорная 50-мм (метр)'] = {
        'Литьё чугунное, трубы (килограмм)':6,
        }

metadict_model['Чугунная труба безнапорная 100-мм (метр)'] = {
        'Литьё чугунное, трубы (килограмм)':14,
        }

metadict_model['Чугунная труба безнапорная 150-мм (метр)'] = {
        'Литьё чугунное, трубы (килограмм)':21,
        }

metadict_model['Жестяная труба безнапорная 150-мм (метр)'] = {
        # Периметр круга: P=2*Pi*r
        'Сталь листовая оцинкованная 0.7 мм (квадратный метр)':2 * 3.14159256 * (0.15 / 2)
        }

#----
# Строительные материалы (штучные --> масса):

metadict_model['Муфты надвижные для чугунных труб диаметром 50-мм (штук)'] = {
        # https://znaytovar.ru/gost/2/GOST_69422280_Truby_chugunnye.html
        'Литьё чугунное, трубы (килограмм)':1.4,
        }

metadict_model['Муфты надвижные для чугунных труб диаметром 100-мм (штук)'] = {
        'Литьё чугунное, трубы (килограмм)':3.2,
        }

metadict_model['Муфты надвижные для чугунных труб диаметром 150-мм (штук)'] = {
        'Литьё чугунное, трубы (килограмм)':5.6,
        }

metadict_model['Арматура запорная для труб диаметром 50-мм (штук)'] = {
        # http://v-teplo.ru/zapornaya-armatura.html
        'Литьё чугунное, арматура (килограмм)':10,
        }

metadict_model['Арматура запорная для труб диаметром 100-мм (штук)'] = {
        'Литьё чугунное, арматура (килограмм)':20,
        }

metadict_model['Арматура запорная для труб диаметром 150-мм (штук)'] = {
        'Литьё чугунное, арматура (килограмм)':40,
        }

metadict_model['Крепления для труб диаметром 50-мм (штук)'] = {
        # http://kzemi.ru/shop/componentry/brackets-for-mounting-of-pipes-and-cables/
        'Литьё чугунное, арматура (килограмм)':0.1,
        }

metadict_model['Шайбы оцинкованные (штук)'] = {
        'Литьё стальное, детали (килограмм)':0.01,
        }

metadict_model['Коронки типа К-105КА (штук)'] = {
        # TODO: Коронки пневмоударные буровые. Уточнить массу.
        'Литьё стальное, детали (килограмм)':10,
        }

metadict_model['Штанга буровая типа БТС-150 (штук)'] = {
        # TODO: Штанга буровая. Уточнить массу.
        'Прокат стальной, детали (килограмм)':30,
        }

metadict_model['Пневмоударники погружные типа II-105-2.6 (штук)'] = {
        # TODO: Пневмоударники погружные. Уточнить массу.
        'Литьё стальное, детали (килограмм)':30,
        }

metadict_model['Трубы буровые диаметром 100-мм (метр)'] = {
        # TODO: Трубы буровые диаметром 100-мм. Уточнить массу.
        'Прокат стальной, детали (килограмм)':30,
        }

#----
# Строительные материалы (площадь --> объём):

#metadict_model['Доска обрезная 50 мм (квадратный метр)'] = {
#        'Доска обрезная (кубометр)':0.050,
#        }
#
#metadict_model['Доска обрезная 25 мм (квадратный метр)'] = {
#        'Доска обрезная (кубометр)':0.025,
#        }
#
#metadict_model['Доска обрезная 20 мм (квадратный метр)'] = {
#        'Доска обрезная (кубометр)':0.020,
#        }
#
#metadict_model['Доска обрезная 15 мм (квадратный метр)'] = {
#        'Доска обрезная (кубометр)':0.015,
#        }
#
#metadict_model['Доска обрезная 10 мм (квадратный метр)'] = {
#        'Доска обрезная (кубометр)':0.010,
#        }

metadict_model['Кровельная солома 300 мм (квадратный метр)'] = {
        # Длина соломы 0.6-1 метра.
        'Солома сухая (кубометр)':0.3,
        }

metadict_model['Кровельная глиносолома 100 мм (квадратный метр)'] = {
        # Длина соломы 0.6-1 метра.
        'Солома сухая (кубометр)':0.3,
        }

#----
# Строительные материалы (масса --> площадь):

metadict_model['Толь гидроизоляционный ТГ-350 (килограмм)'] = {
        # http://stroyres.net/vyazhushhie-materialy/organicheskie/tol
        # Рулон 15 кв. метров -- 24 кг (1.6 кг/кв.метр)
        'Толь гидроизоляционный ТГ-350 (квадратный метр)':1 / 1.6,
        }

metadict_model['Пергамин кровельный П-350 (килограмм)'] = {
        # http://docs.cntd.ru/document/9056512
        'Пергамин кровельный П-350 (квадратный метр)':1 / 0.75,
        }

metadict_model['Рубероид РКЦ-400 (килограмм)'] = {
        # http://www.vashdom.ru/gost/10923-93/
        'Рубероид РКЦ-400 (квадратный метр)':1 / 3,
        }

metadict_detail['Бумага ролевая (килограмм)'] = {
        # Плотность 50 грамм/кв.метр
        'Бумага ролевая (квадратный метр)':1 / 0.05,
        }

#----
# Строительные материалы (площадь --> масса):

metadict_model['Прокат железный 1.8 мм для бочек (квадратный метр)'] = {
        'Прокат железный для бочек (килограмм)':0.0018 * 7600,
        }

metadict_model['Прокат железный 1.2 мм для бочек (квадратный метр)'] = {
        'Прокат железный для бочек (килограмм)':0.0012 * 7600,
        }

metadict_model['Сталь листовая оцинкованная 0.7 мм (квадратный метр)'] = {
        'Прокат стальной, листы (килограмм)':0.0007 * 7600,
        }

#----
# Строительные материалы (объём --> площадь):

metadict_model['Черепица фальцевая 360x180x15 мм (кубометр)'] = {
        'Черепица (квадратный метр)':1 / 0.0145,
        }

#----
# Строительные материалы (площадь --> упрощение):

metadict_model['Рубероид РКЦ-400 (квадратный метр)'] = {
        'Толь (квадратный метр)':1,
        }

metadict_model['Толь гидроизоляционный ТГ-350 (квадратный метр)'] = {
        'Толь (квадратный метр)':1,
        }

metadict_detail['Бумага ролевая (квадратный метр)'] = {
        'Бумага газетная (квадратный метр)':1,
        }

metadict_model['Пергамин кровельный П-350 (квадратный метр)'] = {
        # Толь вместо пергамина. Суть та же.
        'Толь (квадратный метр)':1,
        }

metadict_model['Сетка тканевая с квадратными ячейками №05 без покрытия (квадратный метр)'] = {
        # TODO: Сетка тканевая. Это рогожная сетка.
        'Ткань льняная, мешковина (квадратный метр)':1,
        }

metadict_model['Рогожа (квадратный метр)'] = {
        'Ткань льняная, мешковина (квадратный метр)':1,
        }

metadict_model['Стекло оконное (квадратный метр)'] = {
        'Стекло листовое (квадратный метр)':1,
        }

#----
# Строительные материалы (объём --> упрощение):

metadict_model['Арболит теплоизоляционный (кубометр)'] = {
        'Кирпич опилкобетонный лёгкий (кубометр)':1,
        }

metadict_model['Гравий крупный (кубометр)'] = {
        'Гравий (кубометр)':1,
        }

metadict_model['Гравий мелкий (кубометр)'] = {
        'Гравий (кубометр)':1,
        }

metadict_model['Песок крупный (кубометр)'] = {
        'Песок (кубометр)':1,
        }

metadict_model['Песок кварцевый (кубометр)'] = {
        'Песок (кубометр)':1,
        }

metadict_model['Песок строительный (кубометр)'] = {
        'Песок (кубометр)':1,
        }

metadict_model['Пемза шлаковая (кубометр)'] = {
        'Щебень (кубометр)':1,
        }

metadict_model['Щебень балластный (кубометр)'] = {
        'Щебень (кубометр)':1,
        }

metadict_model['Щебень дорожный (кубометр)'] = {
        'Щебень (кубометр)':1,
        }

metadict_model['Щебень фракции 5-10 миллиметров (кубометр)'] = {
        'Щебень (кубометр)':1,
        }

metadict_model['Щебень фракции 10-20 миллиметров (кубометр)'] = {
        'Щебень (кубометр)':1,
        }

metadict_model['Щебень фракции 40-70 миллиметров (кубометр)'] = {
        'Щебень (кубометр)':1,
        }

metadict_model['Брусья для шпал (кубометр)'] = {
        # Срок службы деревянных шпал (Николаевская железная дорога) -- 4-8 лет
            # Дубовые шпалы без пропитки служат -- 7-15 лет.
            # Пропитка дубовых шпал увеличивает срок службы всего лишь на 25%, то есть до 20 лет.
            # Обработан медным купоросом или хлористым цинком
            # https://ru.wikisource.org/wiki/ЭСБЕ/Дерево,_материал
            # https://ru.wikisource.org/wiki/ЭСБЕ/Брусовой_лес
            # https://ru.wikisource.org/wiki/ЭСБЕ/Железные_дороги,_в_техническом_отношении
        # Размеры шпал на заграничных Ж. дорогах: длина 2,5—2,7 метра, высота 16 см и ширина 25 см.
        'Брус высушенный пропитанный (кубометр)':1,
        }

metadict_model['Брусья для стрелочных переводов (кубометр)'] = {
        'Брус высушенный пропитанный (кубометр)':1,
        }

metadict_model['Брус обрезной (кубометр)'] = {
        'Брус высушенный (кубометр)':1,
        }

metadict_model['Лесоматериалы круглые 140-270 мм (кубометр)'] = {
        'Лес круглый (кубометр)':1,
        }

metadict_model['Лёгкий саман для утепления (кубометр)'] = {
        'Кирпич саманный лёгкий (кубометр)':1,
        }

metadict_model['Кирпич-половняк керамический (кубометр)'] = {
        # Это обломки кирпича, брак производства.
        '-Кирпич-половняк (требуется/кубометр)':1,
        }

metadict_model['Брус высушенный (кубометр)'] = {
        'Пиломатериалы (кубометр)':1,
        }

metadict_model['Брус высушенный пропитанный (кубометр)'] = {
        # TODO: Брус высушенный пропитанный. Обработан медным купоросом или хлористым цинком.
        'Пиломатериалы (кубометр)':1,
        }

metadict_model['Горбыль хвойный (кубометр)'] = {
        'Пиломатериалы (кубометр)':1,
        }

metadict_model['Доска необрезная (кубометр)'] = {
        'Пиломатериалы (кубометр)':1,
        }

metadict_model['Доска обрезная (кубометр)'] = {
        'Пиломатериалы (кубометр)':1,
        }

metadict_model['Кирпич керамический (кубометр)'] = {
        'Кирпич (кубометр)':1,
        }

#----
# Строительные материалы (масса --> упрощение):

metadict_model['Фасонные соединительные части для 400-мм водопровода (килограмм)'] = {
        'Литьё чугунное, трубы (килограмм)':1,
        }

metadict_model['Фасонные соединительные части для 200-мм водопровода (килограмм)'] = {
        'Литьё чугунное, трубы (килограмм)':1,
        }

metadict_model['Фасонные соединительные части для 100-мм водопровода (килограмм)'] = {
        'Литьё чугунное, трубы (килограмм)':1,
        }

metadict_model['Фасонные соединительные части для 50-мм водопровода (килограмм)'] = {
        'Литьё чугунное, трубы (килограмм)':1,
        }

metadict_model['Арматура (килограмм)'] = {
        'Литьё чугунное, арматура (килограмм)':1,
        }

metadict_model['Сталь листовая оцинкованная 0.7 мм (килограмм)'] = {
        'Прокат стальной, листы (килограмм)':1,
        }

metadict_model['Башмаки круглые и бугели (килограмм)'] = {
        'Литьё чугунное, детали (килограмм)':1,
        }

metadict_detail['Битум строительный БН-90/10 (килограмм)'] = {
        # http://polimerkor.ru/bitum-bn-90-10-goryachego-primeneniya
        'Дёготь (килограмм)':1,
        }

metadict_model['Мастика битумная кровельная горячая (килограмм)'] = {
        # Массовые доли:
            # 46-63% -- битума (каменноугольной смолы)
            # 12-15% -- волокнистого наполнителя (асбест, древесная мука)
            # 25-39% -- пылевого наполнителя (тонкомолотый тальк, известь, мел)
            # https://fundaizol.ru/mastika_bitumnaya_krovelnaya_goryachaya.html
        'Мастика битумная (килограмм)':1,
        }

metadict_model['Мастика битумно-полимерная (килограмм)'] = {
        'Мастика битумная (килограмм)':1,
        }

metadict_model['Болты с гайками и шайбами строительные (килограмм)'] = {
        'Литьё стальное, детали (килограмм)':1,
        }

metadict_model['Болты стыковые (килограмм)'] = {
        'Литьё стальное, детали (килограмм)':1,
        }

metadict_model['Войлок строительный (килограмм)'] = {
        'Пакля (килограмм)':1,
        }

metadict_model['Гвозди кровельные и толевые (килограмм)'] = {
        'Прокат железный, гвозди (килограмм)':1,
        }

metadict_model['Гвозди толевые круглые 3x40 мм (килограмм)'] = {
        'Прокат железный, гвозди (килограмм)':1,
        }

metadict_model['Гвозди строительные (килограмм)'] = {
        'Прокат железный, гвозди (килограмм)':1,
        }

metadict_model['Ерши металлические (килограмм)'] = {
        # Нет, это не щётки, это штыри.
        'Прокат железный, гвозди (килограмм)':1,
        }

metadict_model['Пакля пропитаная (килограмм)'] = {
        'Пакля смоляная (килограмм)':1,
        }

metadict_model['Каболка (килограмм)'] = {
        'Пакля смоляная (килограмм)':1,
        }

metadict_model['Костыли путевые (килограмм)'] = {
        'Литьё стальное, детали (килограмм)':1,
        }

metadict_model['Масла каменноугольные для пропитки древесины (килограмм)'] = {
        'Дегтярное масло, скипидар (килограмм)':1,
        }

metadict_model['Масла креозотовые (килограмм)'] = {
        'Дегтярное масло, скипидар (килограмм)':1,
        }

metadict_detail['Керосин для технических целей КТ-1 (килограмм)'] = {
        # Используется как растворитель, для разжижения битума, пёка.
        'Дегтярное масло, скипидар (килограмм)':1,
        }

metadict_model['Накладки стыковые (килограмм)'] = {
        'Литьё стальное, детали (килограмм)':1,
        }

metadict_detail['Клей КМЦ (для наклейки обоев) (килограмм)'] = {
        'Клей обойный (килограмм)':1,
        }

metadict_model['Олифа комбинированная марки К-2 (килограмм)'] = {
        'Олифа (килограмм)':1,
        }

metadict_model['Олифа для улучшенной окраски (килограмм)'] = {
        'Олифа (килограмм)':1,
        }

metadict_model['Смазка солидол жировой марки «Ж» (килограмм)'] = {
        'Смазка машинная (килограмм)':1,
        }

metadict_model['Паста антисептическая строительная (килограмм)'] = {
        'Дёготь (килограмм)':1,
        }

metadict_model['Перевод стрелочный (килограмм)'] = {
        'Литьё стальное, детали (килограмм)':1,
        }

metadict_model['Подкладки шпальные (килограмм)'] = {
        'Прокат стальной, детали (килограмм)':1,
        }

metadict_model['Поковки из квадратных заготовок (килограмм)'] = {
        'Литьё чугунное, детали (килограмм)':1,
        }

metadict_model['Поковки из квадратных заготовок 1.8 кг (килограмм)'] = {
        'Литьё чугунное, детали (килограмм)':1,
        }

metadict_model['Проволока вязальная (килограмм)'] = {
        'Прокат стальной, проволока (килограмм)':1,
        }

metadict_model['Проволока горячекатаная в мотках 6.5 мм (килограмм)'] = {
        'Прокат стальной, проволока (килограмм)':1,
        }

metadict_model['Прокат полосковый (килограмм)'] = {
        'Прокат стальной, листы (килограмм)':1,
        }

metadict_model['Рельсы железнодорожные (килограмм)'] = {
        'Прокат стальной, рельсы (килограмм)':1,
        }

metadict_model['Скобы шпальные (килограмм)'] = {
        'Прокат стальной, детали (килограмм)':1,
        }

metadict_model['Стекло жидкое калийное (килограмм)'] = {
        'Стекло жидкое (килограмм)':1,
        }

metadict_model['Цемент гипсоглинозёмный расширяющийся (килограмм)'] = {
        'Цемент (килограмм)':1,
        }

metadict_model['Портландцемент тампонажный бездобавочный (килограмм)'] = {
        'Цемент (килограмм)':1,
        }

metadict_model['Шпатлёвка масляно-клеевая (килограмм)'] = {
        'Шпатлёвка (килограмм)':1,
        }

metadict_model['Шпатлёвка клеевая (килограмм)'] = {
        'Шпатлёвка (килограмм)':1,
        }

metadict_model['Штыри строительные (килограмм)'] = {
        'Литьё стальное, детали (килограмм)':1,
        }

metadict_model['Шурупы путевые (килограмм)'] = {
        'Литьё стальное, детали (килограмм)':1,
        }

metadict_model['Шурупы строительные (килограмм)'] = {
        'Литьё стальное, детали (килограмм)':1,
        }
