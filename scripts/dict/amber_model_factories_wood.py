#----
# Производства (мебель)
    # Справочная книга столяра-строителя и мебельщика 4. Нормы и расценки
        # http://mebel.townevolution.ru/books/item/f00/s00/z0000010/st099.shtml
    # ТИПОВЫЕ НОРМЫ ВРЕМЕНИ НА ИЗГОТОВЛЕНИЕ СТОЛЯРНЫХ ИЗДЕЛИЙ
        # http://www.libussr.ru/doc_ussr/usr_15369.htm
        # http://www.up-pro.ru/library/production_management/productivity/schitajte_vremja_i_snizhajte_zatraty.html
    # Производство мебели (Германия, 1895 год)
        # Обивка дивана -- 8 нормо-часов
        # Обшивка мягкого стула -- 1.7 нормо-часа
        # Отделка пружинного матраца -- 6 нормо-часа
        # Квартирный комплект мебели -- 800 нормо-часов (2000 марок, 620 рублей)

#----
# Производство ящиков (трудозатраты):
    # Общесоюзные нормы технологического проектирования предприятий
    # машиностроения, приборостроения и металлообработки. Деревообрабатывающие цехи.
        # http://www.gosthelp.ru/text/ONTP0286Obshhesoyuznyenor2.html
    # ГОСТ 10198-91 Ящики деревянные для грузов массой свыше 200 до 20000 кг.
        # http://www.gosthelp.ru/text/GOST1019891YAshhikiderevy.html
    # ГОСТ 20463-75 Ящики деревянные проволокоармированные для овощей и фруктов.
        # http://docs.cntd.ru/document/1200011163

metadict_detail['_Производство деревянной тары (ящик 50-литровый щитовой)'] = {
        # Нормы расхода материалов на изготовление деревянных ящиков
        # http://www.gosthelp.ru/text/ONTP0286Obshhesoyuznyenor2.html
            # ГОСТ 2991-76, на 100 щитовых ящиков по 50 кг груза:
        '_-Изготовление ящиков из готовых досок (нормо-часов)':17 / 100,
        'Пиломатериалы (кубометр)':2.4 / 100,
        'Гвозди для ящиков (килограмм)':36 / 100,
        'Лента стальная для ящиков (килограмм)':18 / 100,
        }

metadict_detail['_Производство деревянной тары (ящик 50-литровый решётчатый)'] = {
        # Обычно ящики для овощей делают по 5 кг на 20 кг груза.
        # Нормы расхода материалов на изготовление деревянных ящиков
        # http://www.gosthelp.ru/text/ONTP0286Obshhesoyuznyenor2.html
            # ГОСТ 2991-76, на 100 щитовых ящиков по 50 кг груза:
        '_-Изготовление ящиков из готовых досок (нормо-часов)':17 / 100,
        'Пиломатериалы (кубометр)':1.2 / 100,
        'Гвозди для ящиков (килограмм)':18 / 100,
        'Лента стальная для ящиков (килограмм)':9 / 100,
        }

#metadict_model['Ремонт ящиков (штука)'] = {
#        # http://www.libussr.ru/doc_ussr/usr_14391.htm
#            # Прибить, заменить 2 - 3 дощечки (10 часов на 100 ящиков)
#            # 70 ящиков за 7 часов, 0.1 часа/ящик.
#        '_-Работа по ремонту ящиков (нормо-часов)':0.1,
#        'Пиломатериалы (кубометр)':0.0012,
#        'Гвозди стальные (килограмм)':0.018,
#        'Лента стальная (килограмм)':0.009,
#        }

#----
# Производство бочек (трудозатраты):
# Бондарное производство (Германия, 1895 год)
    # Бондарей -- 11 на 10 000 населения.
    # Бондарное производство (капитал 31 000 рублей, 6 рабочих) -- 30 000 бочек/год
        # Пивная бочка фабрично (12-100 литров) -- 0.5 нормо-часа.
        # Бочка кустарно -- 3-4 нормо-часа.
    # Производство керосиновых бочек (40 машин, 180 кВт, 53 рабочих) -- 750 000 бочек/год
        # Керосиновая бочка фабрично (100+ литров) -- 0.16 нормо-часа.
        # https://istmat.org/node/27453
    # Дубовая бочка своими руками:
        # http://sam-stroy.info/plotnik/bondar-start.htm
        # https://dom-vinokura.ru/samogon/oborudovanie/dubovaya-bochka-svoimi-rukami.html#i-10
    # ЕДИНЫЕ НОРМЫ ВЫРАБОТКИ И ВРЕМЕНИ НА ИЗГОТОВЛЕНИЕ ДЕРЕВЯННЫХ БОЧЕК
        # http://www.libussr.ru/doc_ussr/usr_15368.htm
    # ГОСТ 8777-80 Бочки деревянные заливные и сухотарные.
        # http://docs.cntd.ru/document/1200011181
        # https://ru.wikisource.org/wiki/ЭСБЕ/Бочка
        # https://ru.wikisource.org/wiki/ЭСБЕ/Бочарные_или_бондарные_изделия
        # https://ru.wikisource.org/wiki/ЭСБЕ/Бочарный_или_бондарный_лес
        # amber Эквестрия -E "|||Ёмкость бондарная"

metadict_detail['_Производство бондарной тары (бочка наливная 500-литровая, 135x73x73-см)'] = {
        # Высота - 1000; диаметр (min) - 805; диаметр (max) - 985
            # Периметр: 2 * 3.14 * (985 / 2) = 3093 мм
            # 3100x50x2.5 железный обруч (8 штук).
            # 31 клёпка боковика шириной 100 мм.
            # 8 клёпок донника шириной 100 мм (2 донца).
            # http://wine.historic.ru/books/item/f00/s00/z0000015/st036.shtml
        # Железные обручи не использовались для стационарных бочек.
        #'Обруч железный для бочки 3100x50x2.5 мм (штука)':8,
        'Обруч деревянный для бочки 3100x50x25 мм (штука)':8,
        'Клёпки боковика для бочки 1100x100x36 мм (штука)':31,
        'Клёпки донника для бочки 800x100x36 мм (штука)':8 * 2,
        '_-Изготовление бочек из готовых клёпок, фабрично (нормо-часов)':0.5,
        '_-Конопатка бочек (квадратный метр)':(1 * 0.1 * 31) + ((0.8 * 0.1 * 8) * 2 * 0.8),
        '_Бондарное производство (годовой оборот)':1 / 20000,
        }

metadict_detail['_Производство бондарной тары (бочка наливная вощёная 500-литровая, 135x73x73-см)'] = {
        # Бочки эмалируют канифолью. Вощение парафином, воском.
        'Обруч деревянный для бочки 3100x50x25 мм (штука)':8,
        'Клёпки боковика для бочки 1100x100x36 мм (штука)':31,
        'Клёпки донника для бочки 800x100x36 мм (штука)':8 * 2,
        '_-Изготовление бочек из готовых клёпок, фабрично (нормо-часов)':0.5,
        '_-Конопатка бочек (квадратный метр)':(1 * 0.1 * 31) + ((0.8 * 0.1 * 8) * 2 * 0.8),
        '_-Вощение бочек (квадратный метр)':(1 * 0.1 * 31) + ((0.8 * 0.1 * 8) * 2 * 0.8),
        '_Бондарное производство (годовой оборот)':1 / 20000,
        }

metadict_detail['_Производство бондарной тары (бочка наливная 300-литровая, 83x83x83-см)'] = {
        # Высота - 850; диаметр (min) - 685; диаметр (max) - 840 мм
            # Периметр: 2 * 3.14 * (840 / 2) = 2638 мм
            # 2700x50x2.2 железный обруч (8 штук).
            # 27 клёпок боковика шириной 100 мм.
            # 7 клёпок донника шириной 100 мм (2 донца).
        #'Обруч железный для бочки 2700x50x2.2 мм (штука)':8,
        'Обруч деревянный для бочки 2700x50x25 мм (штука)':8,
        'Клёпки боковика для бочки 950x100x30 мм (штука)':27,
        'Клёпки донника для бочки 700x100x30 мм (штука)':7 * 2,
        '_-Изготовление бочек из готовых клёпок, фабрично (нормо-часов)':0.4,
        '_-Конопатка бочек (квадратный метр)':(0.85 * 0.1 * 27) + ((0.7 * 0.1 * 7) * 2 * 0.8),
        '_Бондарное производство (годовой оборот)':1 / 25000,
        }

metadict_detail['_Производство бондарной тары (бочка наливная 100-литровая, 56x53x53-см)'] = {
        # Высота - 670; диаметр (min) - 450; диаметр (max) - 515 мм
            # Периметр: 2 * 3.14 * (515 / 2) = 1617 мм
            # 1600x45x1.8 железный обруч (6 штук).
            # 24 клёпки боковика шириной 70 мм.
            # 7 клёпок донника шириной 70 мм (2 донца).
        # Это самые ходовые в торговле бочки, поэтому обручи железные.
        'Обруч железный для бочки 1600x45x1.8 мм (штука)':6,
        'Клёпки боковика для бочки 750x70x20 мм (штука)':24,
        'Клёпки донника для бочки 450x70x20 мм (штука)':7 * 2,
        '_-Изготовление бочек из готовых клёпок, фабрично (нормо-часов)':0.3,
        '_-Конопатка бочек (квадратный метр)':(0.75 * 0.07 * 24) + ((0.45 * 0.07 * 7) * 2 * 0.8),
        '_Бондарное производство (годовой оборот)':1 / 30000,
        }

metadict_detail['_Производство бондарной тары (бочка наливная вощёная 100-литровая, 56x53x53-см)'] = {
        'Обруч железный для бочки 1600x45x1.8 мм (штука)':6,
        'Клёпки боковика для бочки 750x70x20 мм (штука)':24,
        'Клёпки донника для бочки 450x70x20 мм (штука)':7 * 2,
        '_-Изготовление бочек из готовых клёпок, фабрично (нормо-часов)':0.3,
        '_-Конопатка бочек (квадратный метр)':(0.75 * 0.07 * 24) + ((0.45 * 0.07 * 7) * 2 * 0.8),
        '_-Вощение бочек (квадратный метр)':(0.75 * 0.07 * 24) + ((0.45 * 0.07 * 7) * 2 * 0.8),
        '_Бондарное производство (годовой оборот)':1 / 30000,
        }

metadict_detail['_Производство бондарной тары (бочка сухотарная 100-литровая, 56x53x53-см)'] = {
        'Обруч железный для бочки 1600x45x1.8 мм (штука)':6,
        'Клёпки боковика для бочки 750x70x20 мм (штука)':24,
        'Клёпки донника для бочки 450x70x20 мм (штука)':7 * 2,
        '_-Изготовление бочек из готовых клёпок, фабрично (нормо-часов)':0.2,
        '_-Конопатка бочек (квадратный метр)':(0.75 * 0.07 * 24) + ((0.45 * 0.07 * 7) * 2 * 0.8),
        '_Бондарное производство (годовой оборот)':1 / 50000,
        }

metadict_detail['_Производство бондарной тары (кадка 500-литровая, 135x73x73-см)'] = {
        #'Обруч железный для бочки 3100x50x2.5 мм (штука)':8,
        'Обруч деревянный для бочки 3100x50x25 мм (штука)':8,
        'Клёпки боковика для бочки 1100x100x36 мм (штука)':31,
        'Клёпки донника для бочки 800x100x36 мм (штука)':8,
        '_-Изготовление бочек из готовых клёпок, фабрично (нормо-часов)':0.5,
        '_-Конопатка бочек (квадратный метр)':(1 * 0.1 * 31) + ((0.8 * 0.1 * 8) * 2 * 0.8),
        '_Бондарное производство (годовой оборот)':1 / 20000,
        }

metadict_detail['_Производство бондарной тары (кадка 300-литровая, 60x83x83-см)'] = {
        #'Обруч железный для бочки 2700x50x2.2 мм (штука)':8,
        'Обруч деревянный для бочки 2700x50x25 мм (штука)':8,
        'Клёпки боковика для бочки 950x100x30 мм (штука)':27,
        'Клёпки донника для бочки 700x100x30 мм (штука)':7,
        '_-Изготовление бочек из готовых клёпок, фабрично (нормо-часов)':0.4,
        '_-Конопатка бочек (квадратный метр)':(0.85 * 0.1 * 27) + ((0.7 * 0.1 * 7) * 2 * 0.8),
        '_Бондарное производство (годовой оборот)':1 / 25000,
        }

metadict_detail['_Производство бондарной тары (кадка 100-литровая, 56x53x53-см)'] = {
        #'Обруч железный для бочки 1600x45x1.8 мм (штука)':6,
        'Обруч деревянный для бочки 1600x40x20 мм (штука)':6,
        'Клёпки боковика для бочки 750x70x20 мм (штука)':24,
        'Клёпки донника для бочки 450x70x20 мм (штука)':7,
        '_-Изготовление бочек из готовых клёпок, фабрично (нормо-часов)':0.3,
        '_-Конопатка бочек (квадратный метр)':(0.75 * 0.07 * 24) + ((0.45 * 0.07 * 7) * 2 * 0.8),
        '_Бондарное производство (годовой оборот)':1 / 30000,
        }

metadict_detail['_Производство бондарной тары (кадка 50-литровая, 48x45x45-см)'] = {
        # Высота - 540; диаметр (min) - 360; диаметр (max) - 410 мм
            # Периметр: 2 * 3.14 * (410 / 2) = 1287 мм
            # 1300x40x1.6 железный обруч (4 штуки).
            # 19 клёпки боковика шириной 70 мм.
            # 5 клёпок донника шириной 70 мм.
        #'Обруч железный для бочки 1300x40x1.6 мм (штука)':6,
        'Обруч деревянный для бочки 1300x30x15 мм (штука)':6,
        'Клёпки боковика для бочки 600x70x17 мм (штука)':19,
        'Клёпки донника для бочки 360x70x20 мм (штука)':6,
        '_-Изготовление бочек из готовых клёпок, фабрично (нормо-часов)':0.2,
        '_-Конопатка бочек (квадратный метр)':(0.6 * 0.07 * 24) + ((0.36 * 0.07 * 7) * 0.8),
        '_Бондарное производство (годовой оборот)':1 / 40000,
        }

metadict_detail['_Производство бондарной тары (ведро 10-литровое, 35x27x27-см)'] = {
        # Высота - 310; диаметр (min) - 235; диаметр (max) - 265 мм
            # Периметр: 2 * 3.14 * (265 / 2) = 832 мм
            # 830x40x1.6 железный обруч (2 штуки).
            # 19 клёпки боковика шириной 40 мм.
            # 5 клёпок донника шириной 40 мм.
        'Обруч железный для бочки 900x40x1.2 мм (штука)':4,
        'Клёпки боковика для бочки 350x40x14 мм (штука)':21,
        'Клёпки донника для бочки 240x40x16 мм (штука)':6,
        '_-Изготовление бочек из готовых клёпок, фабрично (нормо-часов)':0.2,
        '_-Конопатка бочек (квадратный метр)':(0.35 * 0.04 * 21) + ((0.24 * 0.04 * 6) * 0.8),
        '_Бондарное производство (годовой оборот)':1 / 40000,
        }

#----
# Производство бочек (детали):

metadict_model['Обруч железный для бочки 1600x45x1.8 мм (штука)'] = {
        'Прокат железный 1.8 мм для бочек (квадратный метр)':1.6 * 0.045,
        '_-Изготовление обручей бочек, железных (1000 штук)':1/1000,
        }

metadict_detail['Обруч железный для бочки 900x40x1.2 мм (штука)'] = {
        'Прокат железный 1.2 мм для бочек (квадратный метр)':0.9 * 0.04,
        '_-Изготовление обручей бочек, железных (1000 штук)':1/1000,
        }

metadict_detail['Обруч деревянный для бочки 3100x50x25 мм (штука)'] = {
        # Жерди (стволы тонких деревьев: ель, липа, ива, дуб) предварительно очищены от коры и распарены.
        # Жерди раскалываются надвое, концы связываются в замок.
        'Жерди диаметром 50 мм, для бочек (метр)':3.1 / 2,
        '_-Изготовление обручей бочек, деревянных (1000 штук)':1 / 1000,
        }

metadict_detail['Обруч деревянный для бочки 2700x50x25 мм (штука)'] = {
        'Жерди диаметром 50 мм, для бочек (метр)':2.7 / 2,
        '_-Изготовление обручей бочек, деревянных (1000 штук)':1 / 1000,
        }

metadict_detail['Обруч деревянный для бочки 1600x40x20 мм (штука)'] = {
        'Жерди диаметром 40 мм, для бочек (метр)':1.6 / 2,
        '_-Изготовление обручей бочек, деревянных (1000 штук)':1 / 1000,
        }

metadict_detail['Обруч деревянный для бочки 1300x30x15 мм (штука)'] = {
        'Жерди диаметром 30 мм, для бочек (метр)':1.3 / 2,
        '_-Изготовление обручей бочек, деревянных (1000 штук)':1 / 1000,
        }

metadict_detail['Клёпки боковика для бочки 1100x100x36 мм (штука)'] = {
        'Заготовка клёпки для бочки (кубометр)':1.1 * 0.1 * 0.036,
        '_-Обработка заготовки клёпки боковика (1000 штук)':1/1000,
        }

metadict_detail['Клёпки боковика для бочки 950x100x30 мм (штука)'] = {
        'Заготовка клёпки для бочки (кубометр)':0.95 * 0.1 * 0.03,
        '_-Обработка заготовки клёпки боковика (1000 штук)':1/1000,
        }

metadict_detail['Клёпки боковика для бочки 750x70x20 мм (штука)'] = {
        'Заготовка клёпки для бочки (кубометр)':0.75 * 0.07 * 0.02,
        '_-Обработка заготовки клёпки боковика (1000 штук)':1/1000,
        }

metadict_detail['Клёпки боковика для бочки 600x70x17 мм (штука)'] = {
        'Заготовка клёпки для бочки (кубометр)':0.6 * 0.07 * 0.017,
        '_-Обработка заготовки клёпки боковика (1000 штук)':1/1000,
        }

metadict_detail['Клёпки боковика для бочки 350x40x14 мм (штука)'] = {
        'Заготовка клёпки для бочки (кубометр)':0.35 * 0.04 * 0.014,
        '_-Обработка заготовки клёпки боковика (1000 штук)':1/1000,
        }

metadict_detail['Клёпки донника для бочки 800x100x36 мм (штука)'] = {
        'Заготовка клёпки для бочки (кубометр)':0.8 * 0.1 * 0.036,
        '_-Обработка заготовки клёпки донника (1000 штук)':1/1000,
        }

metadict_detail['Клёпки донника для бочки 700x100x30 мм (штука)'] = {
        'Заготовка клёпки для бочки (кубометр)':0.7 * 0.1 * 0.03,
        '_-Обработка заготовки клёпки донника (1000 штук)':1/1000,
        }

metadict_detail['Клёпки донника для бочки 450x70x20 мм (штука)'] = {
        'Заготовка клёпки для бочки (кубометр)':0.45 * 0.07 * 0.02,
        '_-Обработка заготовки клёпки донника (1000 штук)':1/1000,
        }

metadict_detail['Клёпки донника для бочки 360x70x20 мм (штука)'] = {
        'Заготовка клёпки для бочки (кубометр)':0.36 * 0.07 * 0.02,
        '_-Обработка заготовки клёпки донника (1000 штук)':1/1000,
        }

metadict_detail['Клёпки донника для бочки 240x40x16 мм (штука)'] = {
        'Заготовка клёпки для бочки (кубометр)':0.24 * 0.04 * 0.016,
        '_-Обработка заготовки клёпки донника (1000 штук)':1/1000,
        }

metadict_model['Заготовка клёпки для бочки (кубометр)'] = {
        # 3.2.1. Изготовление заготовок клёпок для деревянных заливных и сухотарных бочек
            # Норма расхода необрезных пиломатериалов на 1 куб. м клепки составляет:
            # хвойных пород - 1,62 куб. м, мягких пород - 1,93; твердых пород - 2,01 куб. м.
        # Заготовка клепки для деревянных заливных и сухотарных бочек. Технические условия
            # https://engenegr.ru/gost-8821-75
        'Лес круглый для бочек (кубометр)':2,
        '_-Изготовление заготовок клёпки (кубометр)':1,
        }

#----
# Утилизация (деревянная тара)

metadict_detail['_Утилизация деревянной тары (килограмм)'] = {
        # Ящики, лотки, изделия из досок.
        '+Доски старые (доступно/килограмм)':1,
        }

metadict_detail['_Утилизация бондарной тары (килограмм)'] = {
        # TODO: Утилизация бондарной тары. Трудозатраты.
        # Нет смысла сжигать в печах, это будет 1/10 от собираемого валежника.
        '+Бочки старые (доступно/килограмм)':1,
        }

#----
# Производство корзин (трудозатраты):
    # ТИПОВЫЕ НОРМЫ ВЫРАБОТКИ НА МЕХАНИЗИРОВАННЫЕ И РУЧНЫЕ РАБОТЫ В САДОВОДСТВЕ
        # http://www.libussr.ru/doc_ussr/usr_14391.htm
    # Конструирование и производство плетеной мебели
        # http://splesti.ru/books/item/f00/s00/z0000004/index.shtml
    # Дубровский В.М., Логинов В.В. 'Плетение из ивового прута'
        # http://splesti.ru/books/item/f00/s00/z0000003/index.shtml
    # "Плетеные изделия" - 1982, Никулин Ф.М., Бочаров В.С., Железнов В.П. 
        # http://splesti.ru/books/item/f00/s00/z0000008/index.shtml

metadict_detail['_Производство плетёной тары (корзина 50-литровая)'] = {
        # TODO: Производство плетёной тары. Нужен деревянный обруч. Палка 70-150 мм.
        # Корзина 50x50x35-см.
            # Прутья диаметром 10 мм (75% объёма),
            # Площадь стенок 0.95 кв.метра (95 метров прутьев),
            # Объём прутьев: 0.95*0.01*0.75=0.007 кубометра.
        # Изготовление:
            # 1) Подобрать прутья по размеру, поднести к месту работы,
            # 2) сплести корзины размером 50x50x35 см, изготовить и закрепить ручки
        # Производительность:
            # 4 корзины за 7 часов -- 1.75 часа на корзину.
            # 930 корзин по 5.25 кг на мастера (Дзержинский лесхоз) -- 1.72 часа на корзину.
            # http://splesti.ru/books/item/f00/s00/z0000008/st026.shtml
            # http://splesti.ru/books/item/f00/s00/z0000004/st027.shtml
            # http://www.junradio.com/olim2/korz.htm
        # Хозяйственные корзины из неошкуренных прутьев, влажность до 20%.
        'Прутья ивовые диаметром 10 мм, грубые (метр)':95,
        '_-Изготовление корзин из готовых ивовых прутьев (нормо-часов)':105 / 60,
        '_Корзинное производство (годовой оборот)':1 / 10000,
        }

metadict_detail['_Производство плетёной тары (корзина 10-литровая)'] = {
        # Корзина 25x25x20-см, 0.33 кв.метра (33 метра прутьев)
        # https://ru.wikisource.org/wiki/ЭСБЕ/Плетеные_изделия
        # https://ru.wikisource.org/wiki/ЭСБЕ/Корзиночное_производство
        'Прутья ивовые диаметром 10 мм, очищенные (метр)':33,
        '_-Изготовление корзин из готовых ивовых прутьев (нормо-часов)':60 / 60,
        '_Корзинное производство (годовой оборот)':1 / 10000,
        }

metadict_detail['_Производство плетёной тары (корзина 1-литровая)'] = {
        # Корзина 12x12x10-см, 0.08 кв.метра (8 метров прутьев)
        'Прутья ивовые диаметром 10 мм, очищенные (метр)':8,
        '_-Изготовление корзин из готовых ивовых прутьев (нормо-часов)':60 / 60,
        '_Корзинное производство (годовой оборот)':1 / 10000,
        }

#----
# Утилизация (плетёная тара)

metadict_detail['_Утилизация плетёной тары (килограмм)'] = {
        # TODO: Утилизация плетёной тары. Трудозатраты.
        '+Корзины старые (доступно/килограмм)':1,
        }

#----
# Производства (строительные материалы)
    # 1 квадратный метр пропила = 1 нормо-час (пилами)
    # Лесопильные станки с круглыми пилами (7-11 кВт) -- 500-2500 квадратных метров пропила/день
    # Кубометр бруса 50x150x6000 мм = 33 нормо-часа (пилами)
    # Кубометр бруса 150x150x6000 мм = 20 нормо-часов (пилами)
    # Кубометр доски 25x150x6000 мм = 54 нормо-часов (пилами)
    # Кубометр бруса 50x50x600 мм = 90 нормо-часов (пилами)
    # https://ru.wikisource.org/wiki/ЭСБЕ/Брусовой_лес

metadict_detail['_Производство пиломатериалов (кубометр)'] = {
        # Около 40% древесины отправляется в отходы:
            # http://baurum.ru/_library/?cat=wood_general_data&id=4864
            # https://ru.wikisource.org/wiki/ЭСБЕ/Лесопильное_производство
        # Производство: 50 кубометров бруса и доски в сутки; Расчёт: 8 бойцов.
            # https://web.archive.org/web/https://saper.isnet.ru/texnica/lrv.html
            # Лесопилка может переработать до 10 тысяч кубометров/год
            # Кантону требуется 2-4 тысячи кубометров.
            # Лесопилка обеспечивает 1-3 кантона и занята на 50%.
        '_-Производство пиломатериалов (кубометр)':1,
        'Лес круглый (кубометр)':1 / 0.6,
        '+Опилки древесные (доступно/кубометр)':1 / 0.6 -1,
        '_Лесопилка (годовой оборот)':1 / 5000,
        }

metadict_detail['_Производство досок паркетных (квадратный метр)'] = {
        # 1. Столярное и паркетное производство и плотничьи работы.
            # Дощечки 1000x125x25 мм
            # Размеры 1000x125 мм (площадь 0.125 кв.метра)
            # Толщина 25 мм (объём 0.003125 кубометра, масса 3.125 кг)
            # Аутсбургская фабрика, 30-50 рубочих -- 50-60 тыс. кв.метров/год
            # 1 кв.метр паркета = 1-1.5 нормо-час
            # https://istmat.org/node/27451
            # https://ru.wikisource.org/wiki/ЭСБЕ/Паркет
        # 8 штук/кв.метр
        '_-Производство досок паркетных (квадратный метр)':1,
        'Пиломатериалы (кубометр)':(0.003125 * 8) / 0.9,
        '+Опилки древесные (доступно/кубометр)':(0.003125 * 8) / 0.9 - (0.003125 * 8),
        '_Паркетное производство (годовой оборот)':1 / 50000,
        }

#----
# Лесозаготовка (полезный объём):
    # ОПРЕДЕЛЕНИЕ ОБЪЕМНО-РАЗМЕРНЫХ ХАРАКТЕРИСТИК ХЛЫСТА В РАСТУЩЕМ ДЕРЕВЕ
    # http://www.science-bsea.bgita.ru/2003/leskomp_2003/isaev_opred.htm
    # ЕДИНЫЕ НОРМЫ ВЫРАБОТКИ И РАСЦЕНКИ НА ЛЕСОЗАГОТОВИТЕЛЬНЫЕ РАБОТЫ (валка леса):
    # http://www.libussr.ru/doc_ussr/usr_14683.htm

metadict_model['_Валка среднего леса (кубометр)'] = {
        # ОПРЕДЕЛЕНИЕ ОБЪЕМНО-РАЗМЕРНЫХ ХАРАКТЕРИСТИК ХЛЫСТА В РАСТУЩЕМ ДЕРЕВЕ
        # http://www.science-bsea.bgita.ru/2003/leskomp_2003/isaev_opred.htm
        # Характеристика леса:
            # ХВОЙНЫЕ (КРОМЕ ЛИСТВЕННИЦЫ) И МЯГКОЛИСТВЕННЫЕ ПОРОДЫ
            # Средней крупности: диаметр ствола 24-32 см; диаметр пня до 26-34 см.
            # Объём хлыста -- 0.5 кубометра
        # Фитомасса усреднённой 50-летней дубравы -- 150 тонн/гектар.
            # Масса дерева (без воды) -- 1.5 тонна (ствол 1 кубометр)
            # На гектар получается -- 100 деревьев.
        # Фитомасса хвойного леса такого же возраста -- 125 тонн/гектар.
            # Сосновые леса России -- 114.3 млн. га, запас древесины 14.6 млрд. м³ (128 м³/га)
            # Сухая сосна -- полтонны (ствол 0.5 кубометра)
            # Всего получается -- 250 деревьев/гектар
        # Норма выработки (1930-е, Сибирь) -- 5 кубометров/человека (3-7 кубометров/человека)
            # _-Работа бригады лесорубов (нормо-часов) | 9
        '_Валка среднего леса (гектар)':(1 / 125) * 1.1,
        }

metadict_model['_Валка среднего леса (Зебрика) (кубометр)'] = {
        '_Валка среднего леса (Зебрика) (гектар)':(1 / 125) * 1.1,
        }

metadict_model['_Валка среднего леса (гектар)'] = {
        # Масса стволовой древесины составляет 60—85%, ветвей 5—25 и корней 5—30% общей массы дерева:
        # http://sinref.ru/000_uchebniki/04410_leso_proizvodstvo/000_lesnaia_taksacia_groshev/003.htm
        # Работает артель лесорубов со своим оборудованием и капитализацией.
        # 200 нормо-часов/гектар, артель лесорубов из 10 пегасок за год убирает 40-80 гектаров.
        'Участок под вырубку среднего леса (гектар)':1,
        '_-Очистка вырубки от порубочных остатков (кубометр)':125 * 0.2,
        '_-Валка среднего леса (дерево)':250,
        '+Валежник (доступно/кубометр)':125 * 0.2,
        '+Вырубленные леса, смоляк (доступно/гектар)':1,
        '_Артель лесорубов (годовой оборот)':1 / 60,
        }

metadict_model['_Валка среднего леса (Зебрика) (гектар)'] = {
        'Участок под вырубку среднего леса (Зебрика) (гектар)':1,
        '_-Очистка вырубки от порубочных остатков (кубометр)':125 * 0.2,
        '_-Валка среднего леса (дерево)':250,
        '+Валежник (доступно/кубометр)':125 * 0.2,
        '+Вырубленные леса, смоляк (доступно/гектар)':1,
        '_Артель лесорубов (годовой оборот)':1 / 60,
        }

metadict_model['_Корчёвка и распилка смоляка (кубометр)'] = {
        # Пни везут на передвижную лесопилку, чтобы не страдать с топорами.
        # Средний запас осмола составляет 5—9 скл. м3/га.
        # Число пней колеблется от 50 до 80 шт/га,
        # https://bibliotekar.ru/7-drevesina/49.htm
        '_-Корчёвка смоляка (кубометр)':1,
        '_-Распилка смоляка (кубометр)':1,
        '+Опилки древесные (доступно/кубометр)':1 / 0.9 -1,
        '-Вырубленные леса, смоляк (требуется/гектар)':1 / 7,
        '_Лесопилка (годовой оборот)':1 / 20000,
        }

metadict_detail['_Заготовка ивовых прутьев, очищенных (кубометр)'] = {
        # Техпроцесс:
            # 1) Набрать прутьев
            # 2) Снять кору (делается легко, щемилкой)
            # 3) Подсушить в кучах на месте сбора 4 часа.
            # 4) Просушить в пучках 8 суток.
            # https://www.activestudy.info/poluchenie-belogo-pruta-i-ego-xranenie/
        # После чистки коры и высыхания теряется 56% объёма.
        'Прутья ивовые (кубометр)':1 / 0.7,
        '_-Заготовка ивовых прутьев (кубометр)':1 / 0.7,
        '_-Очистка ивовых прутьев от коры (кубометр)':1,
        '_-Сушка ивовых прутьев (кубометр)':1,
        }

metadict_detail['_Заготовка ивовых прутьев, грубых (кубометр)'] = {
        'Прутья ивовые (кубометр)':1,
        '_-Заготовка ивовых прутьев (кубометр)':1,
        '_-Сушка ивовых прутьев (кубометр)':1,
        }

#----
# Производства (капитализация)

metadict_detail['_Артель лесорубов (годовой оборот)'] = {
        #'Артель лесорубов (капитализация)':1/2,
        #'Наёмные рабочие (лесорубы)':10,
        }

metadict_detail['_Лесопилка (годовой оборот)'] = {
        # Пример: Бернштейнъ -- Доски хвойных и лиственных пород
            # Доходы: 26 500 рублей/год,
            # Рабочие: 18 (1500 рублей/рабочего)
            # Техника: локомобиль 12 л.с.
        #'Лесопилка (капитализация)':1/10,
        #'Фабричные рабочие (лесопилка)':10,
        }

metadict_detail['_Паркетное производство (годовой оборот)'] = {
        #'Паркетное производство (капитализация)':1/10,
        #'Фабричные рабочие (паркет)':30,
        }

metadict_detail['_Бондарное производство (годовой оборот)'] = {
        #'Бондарное производство (капитализация)':1/10,
        #'Фабричные рабочие (бочки)':30,
        }

metadict_detail['_Корзинное производство (годовой оборот)'] = {
        #'Корзиночное производство (капитализация)':1/10,
        #'Фабричные рабочие (корзины)':15,
        }
