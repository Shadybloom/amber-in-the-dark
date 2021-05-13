#----
# Производства (промышленность)
    # Список фабрик и заводов Российской империи (1907-1909 годы):
    # http://istmat.info/node/26498
    # https://ru.wikisource.org/wiki/Категория:ЭСБЕ:Производство
    # Справочная книга для фабрикантов заводчиков и владельцев промышленных зданий 1898 год:
    # https://rusneb.ru/catalog/000199_000009_002415658/

#----
# Производства (мебель)
    # Справочная книга столяра-строителя и мебельщика 4. Нормы и расценки
        # http://mebel.townevolution.ru/books/item/f00/s00/z0000010/st099.shtml
    # ТИПОВЫЕ НОРМЫ ВРЕМЕНИ НА ИЗГОТОВЛЕНИЕ СТОЛЯРНЫХ ИЗДЕЛИЙ
        # http://www.libussr.ru/doc_ussr/usr_15369.htm
        # http://www.up-pro.ru/library/production_management/productivity/schitajte_vremja_i_snizhajte_zatraty.html

#----
# Производства (промышленные товары)

metadict_detail['_Производство хозяйственного мыла (килограмм)'] = {
        # Тонна мыла = 667 кг жиров (67%), 167 кг кальцированной соды, 83 кг извести, 70 кг соли.
        # TODO: Добавляют каолин для смягчения щёлочи. Канифоль, чтобы защитить от прогоркания.
            # Производят из арахисового и худшего оливкового масла.
            # Варят 10 дней при 121°C, обрабатывают щелочным раствором, отстаивают 2 дня.
            # Один рабочий в день может изготовить 100 кг. мыла (10 кг/нормо-час).
                # - мыло для белья (опт, 4 раб) -- 0.24 руб/килограмм (0.016 нормо/часа)
                # - мыло простое и туалетное (опт, 41 раб) -- 0.4 руб/килограмм (0.4 нормо/часа)
            # https://ru.wikipedia.org/wiki/Хозяйственное_мыло
            # https://ru.wikisource.org/wiki/ЭСБЕ/Мыло
            # https://istmat.info/node/27455
        '_-Варка хозяйственного мыла (килограмм)':1,
        '_-Отстаивание хозяйственного мыла (килограмм)':1,
        '_-Формовка хозяйственного мыла (килограмм)':1,
        'Масло арахисовое (килограмм)':0.67,
        'Сода негашёная (килограмм)':0.17,
        'Известь негашёная (килограмм)':0.085,
        'Соль (килограмм)':0.07,
        '_Мыловарня (годовой оборот)':1 / 500000,
        }

metadict_detail['_Производство соломенных ковров (квадратный метр)'] = {
        # "Наставление к изготовлению соломенно-ковровых несгораемых крыш"
        # Фермы красноуфимского реального училища.
            # Пуда бечевы хватает на 400-520 аршин ковра (284-370 метров)
            # Ширина станка -- 1.25 аршина (0.89 метра).
            # Квадратный метр ковра -- 56 грамм бечевы.
        # Ткётся двумя рабочими по 80-130 аршин/день, (57-92 метра, 50-82 кв.метра)
            # Производительность труда -- 2.5-4 кв.метров/нормо-час
        '_-Производство соломенных ковров (квадратный метр)':1,
        'Солома сухая (килограмм)':2.5,
        'Пеньковая нить (килограмм)':0.06,
        #'_Производство соломенных ковров (годовой оборот)':1 / 20000,
        }


#----
# Производства (строительные материалы)

metadict_detail['_Производство пиломатериалов (кубометр)'] = {
        # Около 40% древесины отправляется в отходы:
            # http://baurum.ru/_library/?cat=wood_general_data&id=4864
            # https://ru.wikisource.org/wiki/ЭСБЕ/Лесопильное_производство
        # Производство: 50 кубометров бруса и доски в сутки; Расчёт: 8 бойцов.
            # http://saper.isnet.ru/texnica/lrv.html
            # Лесопилка может переработать до 10 тысяч кубометров/год
            # Кантону требуется 2-4 тысячи кубометров.
            # Лесопилка обеспечивает 1-3 кантона и занята на 50%.
        '_-Производство пиломатериалов (кубометр)':1,
        'Лес круглый (кубометр)':1 / 0.6,
        '+Опилки древесные (доступно/кубометр)':1 / 0.6 -1,
        '_Лесопилка (годовой оборот)':1 / 5000,
        }

metadict_model['_Производство керамической черепицы (квадратный метр)'] = {
        # Производство керамической черепицы:
            # http://works.doklad.ru/view/xG7K2Qs8qQg/all.html
            # https://ru.wikisource.org/wiki/ЭСБЕ/Черепица
        # Длина 0.36 метра, ширина 0.18 (площадь 0.065 кв. метра)
        # Толщина 0.015 (объём 0.001 кубометра, масса 1.6 килограмма)
        # 16 штук на квадратный метр.
        'Глина мятая (кубометр)':(0.001 * 16) * 1.3 * 1.2,
        '_-Формирование сырца черепицы (штук)':16,
        '_-Сушка сырца кирпича (кубометр)':0.016,
        '_-Обжиг кирпича в штабелях (кубометр)':0.016,
        '_Кирпичный завод (годовой оборот)':1 / 10000,
        }

metadict_model['_Производство кирпича (кубометр)'] = {
        # https://ru.wikisource.org/wiki/ЭСБЕ/Кирпичное_производство
        # Основные технико-экономические показатели на выработку кирпича
        # http://www.arhplan.ru/materials/bricks/osnovnye-tehniko-ekonomicheskie-pokazateli-na-vyrabotku-kirpicha
        # При ручной формовке и обжиге в напольных печах -- 8 человеко-дней на 1000 кирпичей (2 кубометра)
            # Плотность глины -- 2.6 тонны/кубометр; плотность кирпича -- 2.12 тонны/кубометр;
            # Влажность глины -- 30%; потери сырца -- 20% (коэффициенты 1.3 и 1.2)
        # Один-два завода на округ, простой кирпич возят в пределах 100 км.
        'Глина мятая (кубометр)':1 / (2.6 / 2.12 / 1.3 / 1.2),
        '_-Формирование сырца кирпича (кубометр)':1,
        '_-Сушка сырца кирпича (кубометр)':1,
        '_-Обжиг кирпича в штабелях (кубометр)':1,
        '_Кирпичный завод (годовой оборот)':1 / 10000,
        }

metadict_detail['_Производство глины мятой (кубометр)'] = {
        # Плотность обычной глины -- 1.9 тонны/кубометр; а мятой -- 2.6 тонны/кубометр
            # https://ru.wikisource.org/wiki/ЭСБЕ/Глина,_в_технике
        '_-Замачивание глины (кубометр)':1 / (1.9 / 2.6),
        '_-Уплотнение глины (кубометр)':1 / (1.9 / 2.6),
        'Глина необработанная (кубометр)':1 / (1.9 / 2.6),
        #'_Глиномялка (годовой оборот)':1 / 5000,
        }

metadict_detail['_Производство прессованной соломы (кубометр)'] = {
        # - пресс для сена (тюки 25.6x15.7x14.4 верш. 0.5 кубометра, 60-70 кг, пресс 615 кг)
            # 2 рабочих для пресса, 3 для прочих работ -- 75 тюков/день (38 кубометров, 5 тонн/день)
            # плотность сена -- 130 кг/кубометр
        # Плотность сухой соломы -- 0.05 тонны/кубометр; прессованной -- 0.13 тонны/кубометр
        '_-Уплотнение соломы (кубометр)':1 / (0.05 / 0.13),
        'Солома сухая (килограмм)':130,
        #'_Пресс для соломы (годовой оборот)':1 / 7500,
        }

metadict_detail['_Производство прессованного жмыха (кубометр)'] = {
        # Тот же пресс, что и для соломы. Плотность повыше.
        # Плотность пресованного подсолнечного жмыха -- 0.15 тонны/кубометр
        '_-Уплотнение соломы (кубометр)':1 / (0.05 / 0.15),
        '-Жмых (требуется/килограмм)':200,
        #'_Пресс для соломы (годовой оборот)':1 / 7500,
        }

metadict_detail['_Производство прессованных отрубей (кубометр)'] = {
        '_-Уплотнение соломы (кубометр)':1 / (0.05 / 0.15),
        '-Отруби зерновые (требуется/килограмм)':200,
        #'_Пресс для соломы (годовой оборот)':1 / 7500,
        }

metadict_detail['_Пропитка глиной соломенных ковров (квадратный метр)'] = {
        # 1) Ковёр в яму первым слоем. Залить глиной на 2 вершка.
        # 2) Топтать, пока не выйдет воздух. Повторить со вторым слоем и т.д.
        # 3) Прижать тяжестью, оставить замачиваться на ночь (12 часов)
        # Размеры ямы:
            # Ширина ямы -- 1 метр; длина ямы -- 3.6-7.1 метров
            # Глубина ямы (для удобства пони) -- 0.5 метра
            # Объём ямы: 1 x 5.35 x 0.5 = 2.7 кубометра (106 кв.метров ковров за раз).
            # На обычный дом требуется 324 кв.метра ковров и ~300 нормо-часов кровельщиков.
            # Одной ямы на дом достаточно для кровельных работ.
        # Также можно пропустить ковёр между валами в ящике с глиной. Два раза достаточно.
        '_-Пропитка глиной соломенных ковров (квадратный метр)':1,
        'Соломенные ковры 25-мм (квадратный метр)':1,
        'Глина необработанная (кубометр)':0.01,
        'Котлован (кубометр)':(2 * 5.35 * 0.5) / 300,
        }

#----
# Производства (добыча ресурсов)

metadict_model['_Добыча глины (кубометр)'] = {
        # Мощность пласта -- 2 метра, глубина -- 2 метра
        'Котлован (кубометр)':2 / 2,
        'Земляные работы немеханизированные (кубометр)':1,
        }

metadict_model['_Добыча песка (кубометр)'] = {
        'Котлован (кубометр)':1,
        'Земляные работы немеханизированные (кубометр)':1,
        }

metadict_model['_Добыча гравия (кубометр)'] = {
        # Это обкатанные водой камешки, добывают на берегах рек.
        'Котлован (кубометр)':2,
        'Земляные работы немеханизированные (кубометр)':2,
        }

metadict_detail['_Добыча щебня (кубометр)'] = {
        # Месторождение бутового камня взрывают. Затем дробят на дробилках "грохотах" -- 30% потерь.
        'Котлован (кубометр)':1 / 0.7,
        'Подрывные работы (кубометр)':1 / 0.7,
        'Земляные работы немеханизированные (кубометр)':1 / 0.7,
        '_-Дробление щебня в дробилке (кубометр)':1 / 0.7,
        }

metadict_detail['_Добыча бутового камня (кубометр)'] = {
        # Земляные работы.
        # Это ками ~50 кг весом. Подрыв неэффективен. Нужно работать кирками.
        'Котлован (кубометр)':2,
        'Земляные работы немеханизированные (кубометр)':2,
        }

#----
# Лесозаготовка (полезный объём):
    # ОПРЕДЕЛЕНИЕ ОБЪЕМНО-РАЗМЕРНЫХ ХАРАКТЕРИСТИК ХЛЫСТА В РАСТУЩЕМ ДЕРЕВЕ
    # http://www.science-bsea.bgita.ru/2003/leskomp_2003/isaev_opred.htm

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
        '_Валка среднего леса (гектар)':(1 / 125) * 1.1,
        }

metadict_model['_Валка среднего леса (гектар)'] = {
        # TODO:
            # Работает артель лесорубов со своим оборудованием и капитализацией.
            # 200 нормо-часов/гектар, артель лесорубов из 10 пегасок за год убирает 40-80 гектаров.
        # Масса стволовой древесины составляет 60—85%, ветвей 5—25 и корней 5—30% общей массы дерева:
        # http://sinref.ru/000_uchebniki/04410_leso_proizvodstvo/000_lesnaia_taksacia_groshev/003.htm
        '_-Очистка вырубки от порубочных остатков (кубометр)':125 * 0.2,
        '_-Валка среднего леса (дерево)':250,
        'Участок под вырубку среднего леса (гектар)':1,
        '+Валежник (доступно/кубометр)':125 * 0.2,
        '+Вырубленные леса (доступно/гектар)':1,
        '_Артель лесорубов (годовой оборот)':1 / 60,
        }

#----
# Производства (капитализация)

metadict_detail['_Лесопилка (годовой оборот)'] = {
        # Пример: Бернштейнъ -- Доски хвойных и лиственных пород
            # Доходы: 26 500 рублей/год,
            # Рабочие: 18 (1500 рублей/рабочего)
            # Техника: локомобиль 12 л.с.
        #'Лесопилка (капитализация)':1/10,
        #'Фабричные рабочие (лесопилка)':10,
        }

metadict_detail['_Кирпичный завод (годовой оборот)'] = {
        #'Кирпичный завод (капитализация)':1/10,
        #'Фабричные рабочие (кирпичники)':60,
        }

metadict_detail['_Артель лесорубов (годовой оборот)'] = {
        #'Артель лесорубов (капитализация)':1/2,
        #'Наёмные рабочие (лесорубы)':10,
        }

metadict_detail['_Мыловарня (годовой оборот)'] = {
        #'Мыловарня (капитализация)':1/5,
        #'Наёмные рабочие (мыловары)':20,
        }

##----
## Производство дёгтя (смолокурение):
#    # TODO: Перенести это в техпроцессы. work_factories
#    # Здесь нам нужны предприятия. Персонал, капитализация, годовое производство.
#
#metadict_model['Производство дёгтя (килограмм)'] = {
#        'Производство дёгтя (литр)':1.05,
#        }
#
#metadict_model['Производство дёгтя (литр)'] = {
#        'Производство дёгтя (кубометр)':0.001,
#        }
#
#metadict_model['Производство дёгтя (кубометр)'] = {
#        # Смоло-скипидарные аппараты — минские реторты емкостью 8 м³ (цикл 56 часов, восемь рабочих)
#            # http://www.findpatent.ru/patent/257/2578695.html
#        # Каждый аппарат производит по 330 литров смолы, требуется 3 аппарата (или цикла).
#        'Смоляк (кубометр)':8 * 3,
#        '_-Работа персонала смолокурни (нормо-часов)':8 * (56/2.4) * 3,
#        'Использование печи 8-кубометровой смоляной (часов)':56 * 3,
#        }
#
#metadict_model['Корчёвка смоляка (кубометр)'] = {
#        # Характеристика осмольного сырья, способы его получения
#            # http://geolike.ru/page/gl_2140.htm
#        # Смолокурение трудозатраты (на 0.1 кубометра смолы) -- 10 человеко-дней на сырьё (3-6 м³ смолья).
#            # http://sanatatur.ru/forum/viewtopic.php?f=9&t=27691
#        # Смолокурение в имении Красный бор:
#            # http://vln.by/node/220
#            # Штабель смоляка (локоть 0.5 метра): 1.5x1.25x1.25 (2.34 кубометра) -- 12 дней работы двора.
#        # Сборник Е13 Расчистка трассы линейных сооружений от леса
#        # http://www.gosthelp.ru/text/SbornikE13Raschistkatrass.html
#        # §Е13-8. Корчевка пней
#            # Нормы времени и расценки на 10 пней (около кубометра); диаметр пней, см 30;
#            # Трактор Трактор Т-100М (тяговое усилие 6000 кгс, мощность 81 кВт)
#            # Трудозатраты:
#                # Для бульдозеристов: 0.81 нормо-часа
#                # Для рабочих: 0.81 нормо-часа
#        # В Россиии 2016 года пни на осмол стоят 6.6 рублей/килограмм, 3400 рублей/кубометр.
#            # Взрывной способ -- 4 кубометра/смену
#            # Корчеватель АКП-1 -- 25 кубометров/смену
#        # ЕДИНЫЕ НОРМЫ ВЫРАБОТКИ И РАСЦЕНКИ НА ЛЕСОЗАГОТОВИТЕЛЬНЫЕ РАБОТЫ
#            # http://pravo.levonevsky.org/baza/soviet/sssr1641.htm
#            # 3.1.2. Спиливание пней заподлицо с землей
#            # Диаметр комлей деревьев, см: св. 24 до 32
#            # Трудозатраты -- 0.108 нормо-часа/пень (около часа на кубометр)
#        '_-Корчёвка сосновых пней (нормо-часов)':20,
#        '_-Колка пней на смоляк (нормо-часов)':5,
#        '|-Сосновая вырубка (гектар)':10 / 250,
#        }
#
##----
## Лесозаготовка (оценочно):
#
##----
## Производство корзин (трудозатраты):
#    # ТИПОВЫЕ НОРМЫ ВЫРАБОТКИ НА МЕХАНИЗИРОВАННЫЕ И РУЧНЫЕ РАБОТЫ В САДОВОДСТВЕ
#        # http://www.libussr.ru/doc_ussr/usr_14391.htm
#    # Конструирование и производство плетеной мебели
#        # http://splesti.ru/books/item/f00/s00/z0000004/index.shtml
#        # https://ru.wikisource.org/wiki/ЭСБЕ/Корзиночное_производство
#
#metadict_model['Изготовление плетёных корзин объёмом 50 литров (штука)'] = {
#        # Вес корзины:
#            # Прутья диаметром 10 мм (75% объёма),
#            # Площадь стенок 0.95 кв.метра (95 метров прутьев),
#            # Объём прутьев: 0.95*0.01*0.75=0.007 кубометра.
#        # http://www.junradio.com/olim2/korz.htm
#        'Заготовка прутьев для плетения корзин (кубометр)':0.01,
#        'Изготовление корзин из готовых ивовых прутьев (штука)':1,
#        }
#
#metadict_model['Изготовление корзин из готовых ивовых прутьев (штука)'] = {
#        # 1) Подобрать прутья по размеру, поднести к месту работы,
#        # 2) сплести корзины размером 50 х 50 х 35 см, изготовить и закрепить ручки
#            # 4 корзины за 7 часов; 1.75 часа на корзину.
#        # http://splesti.ru/books/item/f00/s00/z0000004/st027.shtml
#            # Дзержинский лесхоз 930 корзин по 5.25 кг на мастера -- 1.72 часа на корзину.
#        '_-Работа на плетении корзин (нормо-часов)':1.75,
#        }
#
#metadict_model['Заготовка прутьев для плетения корзин (кубометр)'] = {
#        # http://splesti.ru/books/item/f00/s00/z0000004/st013.shtml
#        # Нарезать прутья толщиной 8-12 мм, вынести на расстояние до 50 м, уложить в кучи
#            # 0.25 кубометра за 7 часов, 0.036 кубометра/час, 28 нормо-часов/кубометр
#        '_-Работа на заготовке ивовых прутьев (нормо-часов)':28,
#        'Ивовые прутья диаметром 10 мм (метр)':10000,
#        }
#
#metadict_model['Ивовые прутья диаметром 10 мм (метр)'] = {
#        'Ивовые прутья (кубометр)':0.0001,
#        }
#
#metadict_model['Ивовые прутья (кубометр)'] = {
#        # Плотность при влажности 12% -- 490 кг/м³
#        'Ивовые прутья (тонн)':0.49,
#        }
#
##----
## Производство ящиков (трудозатраты):
#    # Общесоюзные нормы технологического проектирования предприятий
#    # машиностроения, приборостроения и металлообработки. Деревообрабатывающие цехи.
#        # http://www.gosthelp.ru/text/ONTP0286Obshhesoyuznyenor2.html
#    # ГОСТ 10198-91 Ящики деревянные для грузов массой свыше 200 до 20000 кг.
#        # http://www.gosthelp.ru/text/GOST1019891YAshhikiderevy.html
#    # ГОСТ 20463-75 Ящики деревянные проволокоармированные для овощей и фруктов.
#        # http://docs.cntd.ru/document/1200011163
#
#metadict_model['Изготовление щитовых деревянных ящиков под 50 кг груза (штука)'] = {
#        'Изготовление щитовых деревянных ящиков под 50 кг груза (100 штук)':1 / 100,
#        }
#
#metadict_model['Изготовление решётчатых деревянных ящиков под 50 кг груза (штука)'] = {
#        'Изготовление решётчатых деревянных ящиков под 50 кг груза (100 штук)':1 / 100,
#        }
#
#metadict_model['Изготовление щитовых деревянных ящиков под 50 кг груза (100 штук)'] = {
#        # TODO:
#            # Понячье производство не настолько автоматизированно.
#        # Нормы расхода материалов на изготовление деревянных ящиков
#        # http://www.gosthelp.ru/text/ONTP0286Obshhesoyuznyenor2.html
#            # ГОСТ 2991-76, на 100 щитовых ящиков по 50 кг груза:
#        '_-Работа плотника (нормо-часов)':17,
#        'Пиломатериалы (кубометр)':2.4,
#        'Гвозди стальные (килограмм)':36,
#        'Лента стальная (килограмм)':18,
#        }
#
#metadict_model['Изготовление решётчатых деревянных ящиков под 50 кг груза (100 штук)'] = {
#        '_-Работа плотника (нормо-часов)':17,
#        'Пиломатериалы (кубометр)':1.2,
#        'Гвозди стальные (килограмм)':18,
#        'Лента стальная (килограмм)':9,
#        }
#
#metadict_model['Ремонт ящиков для упаковки яблок (штука)'] = {
#        # http://www.libussr.ru/doc_ussr/usr_14391.htm
#            # Прибить, заменить 2 - 3 дощечки (10 часов на 100 ящиков)
#            # 70 ящиков за 7 часов, 0.1 часа/ящик.
#        '_-Работа по ремонту ящиков (нормо-часов)':0.1,
#        'Пиломатериалы (кубометр)':0.0012,
#        'Гвозди стальные (килограмм)':0.018,
#        'Лента стальная (килограмм)':0.009,
#        }
#
##----
## Производство бочек (трудозатраты):
#    # 3. Бондарное производство.
#    # https://istmat.info/node/27453
#    # Дубовая бочка своими руками:
#        # http://sam-stroy.info/plotnik/bondar-start.htm
#        # https://dom-vinokura.ru/samogon/oborudovanie/dubovaya-bochka-svoimi-rukami.html#i-10
#    # ЕДИНЫЕ НОРМЫ ВЫРАБОТКИ И ВРЕМЕНИ НА ИЗГОТОВЛЕНИЕ ДЕРЕВЯННЫХ БОЧЕК
#        # http://www.libussr.ru/doc_ussr/usr_15368.htm
#    # ГОСТ 8777-80 Бочки деревянные заливные и сухотарные.
#        # http://docs.cntd.ru/document/1200011181
#    # Из энциклопедии 1894 года:
#        # https://ru.wikisource.org/wiki/ЭСБЕ/Бочка
#        # https://ru.wikisource.org/wiki/ЭСБЕ/Бочарные_или_бондарные_изделия
#        # https://ru.wikisource.org/wiki/ЭСБЕ/Бочарный_или_бондарный_лес
#
#metadict_model['Изготовление деревянных бочек объёмом 500 литров (штука)'] = {
#        # http://wine.historic.ru/books/item/f00/s00/z0000015/st036.shtml
#            # высота - 1000; диаметр (min) - 805; диаметр (max) - 985
#        'Обруч стальной для бочки 3100x50x2.5 мм (штука)':8,
#        'Клёпки боковика 1100x100x36 мм (штука)':27,
#        'Клёпки донника 800x100x36 мм (штука)':8 * 2,
#        'Изготовление остовов бочек (100 штук)':1/100,
#        'Изготовление донец (100 штук)':1/100,
#        'Сборка бочек (100 штук)':1/100,
#        }
#
#metadict_model['Изготовление деревянных бочек объёмом 100 литров (штука)'] = {
#        # TODO:
#            # На самом деле очень быстрый техпроцесс. Земнопони осуждают.
#                # Так-то основные операции занимают где-то 50% времени.
#                # Нужно отделить операции от ресурсов и ввести коэффициент.
#            # Дерево требуется несколько месяцев сушить.
#        # Габариты бочки: 0.675x0.515x0.515
#        'Обруч стальной для бочки 1600x45x1.8 мм (штука)':6,
#        'Клёпки боковика 700x70x20 мм (штука)':27,
#        'Клёпки донника 450x70x20 мм (штука)':6 * 2,
#        'Изготовление остовов бочек (100 штук)':1/100,
#        'Изготовление донец (100 штук)':1/100,
#        'Сборка бочек (100 штук)':1/100,
#        #'Вощение бочки (штука)':1,
#        }
#
#metadict_model['Обруч стальной для бочки 3100x50x2.5 мм (штука)'] = {
#        'Прокат из нержавеющей стали 2.5 мм (квадратный метр)':3.1 * 0.05,
#        'Изготовление обручей (1000 штук)':1/1000,
#        }
#
#metadict_model['Обруч стальной для бочки 1600x45x1.8 мм (штука)'] = {
#        # 23 клёпки шириной 0.07 метра. Требуется 1600x45x1.8 стальная полоса:
#        'Прокат из нержавеющей стали 1.8 мм (квадратный метр)':1.6 * 0.045,
#        'Изготовление обручей (1000 штук)':1/1000,
#        }
#
#metadict_model['Клёпки донника 800x100x36 мм (штука)'] = {
#        'Обработка заготовки клёпки донника (1000 штук)':1/1000,
#        'Заготовки клёпки донника 800x100x36 мм (штука)':1,
#        }
#
#metadict_model['Клёпки донника 450x70x20 мм (штука)'] = {
#        'Обработка заготовки клёпки донника (1000 штук)':1/1000,
#        'Заготовки клёпки донника 450x70x20 мм (штука)':1,
#        }
#
#metadict_model['Клёпки боковика 1100x100x36 мм (штука)'] = {
#        'Обработка заготовки клёпки боковика (1000 штук)':1/1000,
#        'Заготовки клёпки боковика 1100x100x36 мм (штука)':1,
#        }
#
#metadict_model['Клёпки боковика 700x70x20 мм (штука)'] = {
#        'Обработка заготовки клёпки боковика (1000 штук)':1/1000,
#        'Заготовки клёпки боковика 700x70x20 мм (штука)':1,
#        }
#
#metadict_model['Заготовки клёпки донника 800x100x36 мм (штука)'] = {
#        'Изготовление заготовок клёпки (кубометр)':0.800 * 0.100 * 0.036,
#        }
#
#metadict_model['Заготовки клёпки донника 450x70x20 мм (штука)'] = {
#        'Изготовление заготовок клёпки (кубометр)':0.45 * 0.07 * 0.02,
#        }
#
#metadict_model['Заготовки клёпки боковика 1100x100x36 мм (штука)'] = {
#        'Изготовление заготовок клёпки (кубометр)':1.100 * 0.100 * 0.036,
#        }
#
#metadict_model['Заготовки клёпки боковика 700x70x20 мм (штука)'] = {
#        'Изготовление заготовок клёпки (кубометр)':0.7 * 0.07 * 0.02,
#        }
#
##----
## Производство бочек (технологические процессы):
#
#metadict_model['Сборка бочек (100 штук)'] = {
#        'Вставка доньев в остов бочки (100 штук)':1,
#        'Осадка обручей на обручеосадочном прессе (100 штук)':1,
#        'Зачистка бочек вручную (100 штук)':1,
#        }
#
#metadict_model['Изготовление остовов бочек (100 штук)'] = {
#        'Сборка остовов бочек в сборочной форме (100 штук)':1,
#        'Пропарка остовов бочек в пропарочной установке (100 штук)':1,
#        'Стяжка остовов бочек в стяжном механическом винтовом вороте (100 штук)':1,
#        'Выравнивание провесов (100 штук)':1,
#        'Термическая обработка остовов (100 штук)':1,
#        'Зауторка остовов бочек (100 штук)':1,
#        }
#
#metadict_model['Изготовление донец (100 штук)'] = {
#        'Сортировка клёпок донника и подборка донных щитов (100 штук)':1,
#        'Сшивка донных щитов (100 штук)':1,
#        'Вырезка доньев на донновырезных станках (100 штук)':1,
#        'Подборка комплектов доньев для бочки (100 штук)':1,
#        'Сверление шкантовых отверстий в доньях (100 штук)':1,
#        'Сверление отверстий в клепках и изготовление деревянных пробок (100 штук)':1,
#        }
#
#metadict_model['Изготовление обручей (1000 штук)'] = {
#        'Резка и вальцовка обручей на бондарно-обручном станке (1000 штук)':1,
#        'Сварка обручей на машинах для точечной сварки (1000 штук)':1,
#        'Изготовление обручей из обрезков (1000 штук)':1,
#        #'Окраска обручей бочек (100 штук)':10,
#        }
#
#metadict_model['Обработка заготовки клёпки боковика (1000 штук)'] = {
#        'Сортировка клёпок (1000 штук)':1,
#        'Фуговка клёпок боковика на клепкофуговальных станках (1000 штук)':1,
#        'Строжка клёпок боковика на клепкострогальных станках (1000 штук)':1,
#        'Двусторонняя торцовка черновых заготовок клёпок (1000 штук)':1,
#        }
#
#metadict_model['Обработка заготовки клёпки донника (1000 штук)'] = {
#        'Сортировка клёпок (1000 штук)':1,
#        'Фуговка клёпок донника на клепкофуговальных станках (1000 штук)':1,
#        'Строжка клёпок донника на клепкострогальных станках (1000 штук)':1,
#        }
#
##----
## Производство бочек (старомодное):
#
#metadict_model['Вощение бочки (штука)'] = {
#        # Бочка на 100 литров с площадью 1.3 кв.метра
#        '_-Работа бригады бондарей (нормо-часов)':0.2,
#        'Льняное масло (килограмм)':0.15,
#        'Воск (килограмм)':0.25,
#        }
#
##----
## Производство бочек (технологические процессы):
#
#metadict_model['Зачистка бочек вручную (100 штук)'] = {
#        # С зачисткой провесов
#        '_-Работа бригады бондарей (нормо-часов)':1.55,
#        }
#
#metadict_model['Осадка обручей на обручеосадочном прессе (100 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':1.19,
#        }
#
#metadict_model['Вставка доньев в остов бочки (100 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':2.17,
#        }
#
#metadict_model['Окраска обручей бочек (100 штук)'] = {
#        # Меделнно и аккуратно, кисточкой.
#        '_-Работа бригады бондарей (нормо-часов)':5.13,
#        }
#
#metadict_model['Изготовление обручей из обрезков (1000 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':1.94,
#        }
#
#metadict_model['Сварка обручей на машинах для точечной сварки (1000 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':3.02,
#        }
#
#metadict_model['Резка и вальцовка обручей на бондарно-обручном станке (1000 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':2.21,
#        }
#
#metadict_model['Сверление отверстий в клепках и изготовление деревянных пробок (100 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':0.201 + 0.255,
#        }
#
#metadict_model['Сверление шкантовых отверстий в доньях (100 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':0.233,
#        }
#
#metadict_model['Подборка комплектов доньев для бочки (100 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':0.128,
#        }
#
#metadict_model['Вырезка доньев на донновырезных станках (100 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':0.47,
#        }
#
#metadict_model['Сшивка донных щитов (100 штук)'] = {
#        # 3.22. СШИВКА ДОННЫХ ЩИТОВ ВРУЧНУЮ
#        '_-Работа бригады бондарей (нормо-часов)':2.13,
#        }
#
#metadict_model['Сортировка клёпок донника и подборка донных щитов (100 штук)'] = {
#        # Сотня клёпок, или сотня щитов?
#        '_-Работа бригады бондарей (нормо-часов)':0.6,
#        }
#
#metadict_model['Зауторка остовов бочек (100 штук)'] = {
#        # 3.15. ЗАУТОРКА ОСТОВОВ БОЧЕК НА ДВУХСТОРОННЕМ БОНДАРНО-УТОРНОМ СТАНКЕ БУ
#            # Вырезание уторов, пазов для донца.
#        '_-Работа бригады бондарей (нормо-часов)':1.2,
#        }
#
#metadict_model['Термическая обработка остовов (100 штук)'] = {
#        # Обжиг в электромангальной печи, 8 мангалов
#        '_-Работа бригады бондарей (нормо-часов)':1.2,
#        }
#
#metadict_model['Выравнивание провесов (100 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':1.5,
#        }
#
#metadict_model['Стяжка остовов бочек в стяжном механическом винтовом вороте (100 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':1.1,
#        }
#
#metadict_model['Пропарка остовов бочек в пропарочной установке (100 штук)'] = {
#        # Установка периодического действия на 8 остовов
#        '_-Работа бригады бондарей (нормо-часов)':3,
#        }
#
#metadict_model['Сборка остовов бочек в сборочной форме (100 штук)'] = {
#        # Бочки вместимостью 100 литров
#        '_-Работа бригады бондарей (нормо-часов)':2,
#        }
#
#metadict_model['Сортировка клёпок (1000 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':0.667,
#        }
#
#metadict_model['Фуговка клёпок донника на клепкофуговальных станках (1000 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':0.876,
#        }
#
#metadict_model['Строжка клёпок донника на клепкострогальных станках (1000 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':1.7,
#        }
#
#metadict_model['Фуговка клёпок боковика на клепкофуговальных станках (1000 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':5.87,
#        }
#
#metadict_model['Строжка клёпок боковика на клепкострогальных станках (1000 штук)'] = {
#        '_-Работа бригады бондарей (нормо-часов)':1.7,
#        }
#
#metadict_model['Двусторонняя торцовка черновых заготовок клёпок (1000 штук)'] = {
#        # Прямоугольные доски в скруглённую форму для бочки.
#        '_-Работа бригады бондарей (нормо-часов)':0.446,
#        }
#
#metadict_model['Изготовление заготовок клёпки (кубометр)'] = {
#        # 3.2.1. Изготовление заготовок клёпок для деревянных заливных и сухотарных бочек
#        # Норма расхода необрезных пиломатериалов на 1 куб. м клепки составляет:
#            # хвойных пород - 1,62 куб. м, мягких пород - 1,93; твердых пород - 2,01 куб. м.
#        # Заготовка клепки для деревянных заливных и сухотарных бочек. Технические условия
#        # https://engenegr.ru/gost-8821-75
#        'Лес круглый (кубометр)':2,
#        '_-Работа бригады бондарей (нормо-часов)':15,
#        }
