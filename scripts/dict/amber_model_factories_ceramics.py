#----
# Заметки:
    # TODO: Трубы гончарные для дренажа и сельской канализации.
        # Трубы гончарные -- диаметр 150-мм (стенки 15 мм), 0.07 кубометра глины, масса метра -- 112 кг
        # Выделываются машиной с 1843 года, это самый дешёвый способ осушения мокрых полей.
        # Укладывают на глубину 1.5-3 метра, сетка труб x10 - x25 грубины залегания.
        # Вода проникает в трубы через щели на стыках сегментов.
        # Расход на десятину дренируемой земли -- 60 рублей.
        # В ГЭСНах есть нормативы для укладки керамических канализационных труб.
        # https://ru.wikisource.org/wiki/ЭСБЕ/Дренаж
    # Гончарное дело:
        # Тестообразная глина -- 0.6-0.8 кг воды на 1 кг сухой глины (40% воды)
        # Глину промывают струёй воды в глиномялке и очищают осаждением в двух бассейнах последовательно.
        # Глиняные растворы готовят отдельно, смешивают в чане с отметками, отжимают прессом и сушат на воздухе.
        # Глазирование солью (муравление) -- соль в печь при обжигании, испаряется и реагирует с глиной.
        # Капсель -- керамический ящик с креплениями для обжига тонких изделий в печи.
        # https://ru.wikisource.org/wiki/ЭСБЕ/Гончарное_производство
        # https://ru.wikisource.org/wiki/ЭСБЕ/Глина,_в_технике
        # https://ru.wikisource.org/wiki/ЭСБЕ/Фаянс
        # https://ru.wikisource.org/wiki/ЭСБЕ/Фарфор
        # https://upload.wikimedia.org/wikipedia/commons/3/37/Brockhaus_and_Efron_Encyclopedic_Dictionary_b69_387-0.jpg

#----
# Производства (строительные материалы)
    # Кирпичное производство (Германия 1895 года, 52.5 млн. человек)
        # 6000 заводов (по 30 рабочих) -- 420 000 кирпичей (800 м³) на завод.
            # 14 000 кирпичей/рабочего
            # Оценочно: 114-214 нормо-часов/1000 кирпичей (60-110 нормо-часов/кубометр)
            # 1 черепица на 70 произведённых кирпичей
        # Кирпичный завод (Америка, 275 рабочих, 1065 кВт)
            # 3.9 кВт/рабочего,
            # 360 000 кирпичей/рабочего
            # Оценочно: 4.4-8.3 нормо-часа/1000 кирпичей (2.3-4.4 нормо-часа/кубометр)
            # Машина для формирования кирпичей (7 рабочих) -- 12-16 тыс. кирпичей/день
            # https://istmat.org/node/27438

metadict_model['_Производство керамического кирпича (кубометр)'] = {
        # https://ru.wikisource.org/wiki/ЭСБЕ/Кирпичное_производство
        # Основные технико-экономические показатели на выработку кирпича
        # http://www.arhplan.ru/materials/bricks/osnovnye-tehniko-ekonomicheskie-pokazateli-na-vyrabotku-kirpicha
        # При ручной формовке и обжиге в напольных печах -- 8 человеко-дней на 1000 кирпичей (2 кубометра)
            # Плотность глины -- 2.6 тонны/кубометр; плотность кирпича -- 2.12 тонны/кубометр;
            # Влажность глины -- 30%; потери сырца -- 20% (коэффициенты 1.3 и 1.2)
        # 512 штук/кубометр. 10% брака после обжига
        # Кирпич-половняк, это брак производства.
        '_-Формирование сырца кирпича (кубометр)':1,
        '_-Сушка сырца кирпича (кубометр)':1,
        '_-Обжиг кирпича в штабелях (кубометр)':1,
        'Глина мятая (кубометр)':1 / (2.6 / 2.12 / 1.3 / 1.2),
        '+Кирпич-половняк (доступно/кубометр)':0.1,
        '_Кирпичный завод (годовой оборот)':1 / 10000,
        }

metadict_model['_Производство керамической черепицы (квадратный метр)'] = {
        # Длина 360 мм, ширина 180 мм (площадь 0.065 кв.метра)
        # Толщина 15 мм (объём 0.001 кубометра, масса 1.6 килограмма)
        # Слой глазури -- 0.3 мм/кв.метр (с двух сторон 0.0006 м³)
        # Производство черепицы:
            # http://works.doklad.ru/view/xG7K2Qs8qQg/all.html
            # https://ru.wikisource.org/wiki/ЭСБЕ/Черепица
        # 16 штук/кв.метр. 25% брака после обжига (коэффициент 0.75)
        'Глина мятая (кубометр)':(0.001 * 16) * 1.3 * 1.2 / 0.75,
        'Глазурь стеклянная (кубометр)':0.0006 / 0.75,
        '_-Формирование сырца черепицы (штук)':16 / 0.75,
        '_-Сушка сырца черепицы (кубометр)':0.016 / 0.75,
        '_-Обжиг черепицы в печи (кубометр)':0.016 / 0.75,
        '_-Глазурование черепицы окунанием и обжигом (кубометр)':0.016 / 0.9,
        '_Черепичный завод (годовой оборот)':1 / 60000,
        }

metadict_model['_Производство керамического кафеля (квадратный метр)'] = {
        # Размеры 150x150 мм (площадь 0.0225 кв.метра)
        # Толщина 10 мм (объём 0.000225 кубометра, масса 0.36 килограмма)
        # Слой глазури -- 0.3 мм/кв.метр (с двух сторон 0.0006 м³)
        # Производство кафеля, изразцы:
            # https://ru.wikisource.org/wiki/ЭСБЕ/Кафли
            # https://ru.wikisource.org/wiki/ЭСБЕ/Глазурь
            # https://ru.wikisource.org/wiki/ЭСБЕ/Гончарное_производство
            # http://www.remotvet.ru/questions/21803-kak-samostojatelno-sdelat-glazur-dlja-kafelnoj-plitki.html
        # 45 штук/кв.метр. 25% брака после обжига (коэффициент 0.75)
        'Глина мятая (кубометр)':(0.000225 * 45) * 1.3 * 1.2 / 0.75,
        'Глазурь стеклянная (кубометр)':0.0006 / 0.75,
        '_-Формирование сырца кафеля (штук)':45 / 0.75,
        '_-Сушка сырца кафеля (кубометр)':(0.000225 * 45) / 0.75,
        '_-Обжиг кафеля в печи (кубометр)':(0.000225 * 45) / 0.75,
        '_-Глазурование кафеля окунанием и обжигом (кубометр)':(0.000225 * 45) / 0.9,
        '_Кафельный завод (годовой оборот)':1 / 60000,
        }

#----
# Производства (утварь)

metadict_detail['_Производство керамической утвари (раковина напольная 50-литровая, 60x50x30-см)'] = {
        # Масса изделия -- 40 килограмм, влажность глины 0.3, плотность глины 2600 кг/кубометр, 25% брака
        # Форма раковины. Площадь глазури, это площадь сферы (двух полусфер, внешней и внутренней).
        '_Лепка глиняных изделий (рабочих часов)':1,
        'Глина мятая (кубометр)':(40 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.6/2) ** 2) * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.6*0.5*0.3) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.6*0.5*0.3) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.6*0.5*0.3) / 0.75,
        }

metadict_detail['_Производство керамической утвари (раковина настенная 15-литровая, 50x30x20-см)'] = {
        # Масса изделия -- 14 килограмм
        '_Лепка глиняных изделий (рабочих часов)':1,
        'Глина мятая (кубометр)':(14 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.5/2) ** 2) * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.5*0.3*0.2) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.5*0.3*0.2) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.5*0.3*0.2) / 0.75,
        }

metadict_detail['_Производство керамической утвари (умывальник 25-литровый, 30x30x40-см)'] = {
        # Масса изделия -- 8 килограмм
        # Форма шара. Площадь глазури, это площадь двух сфер по наибольшему радиусу.
        # В отличии от людей, единорожкам легче всего лепить кувшины сферической формы.
        '_Лепка глиняных изделий (рабочих часов)':1,
        'Глина мятая (кубометр)':(8 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.4/2) ** 2) * 2 * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.3*0.3*0.4) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.3*0.3*0.4) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.3*0.3*0.4) / 0.75,
        }

#----
# Производства (тара)

metadict_detail['_Производство керамической тары (горшок 100-литровый)'] = {
        # Пифос на 100 литров = 40 кг.
        # Габариты 500x500x600-мм (пони невысокие)
        '_Лепка глиняных изделий (рабочих часов)':30 / 60,
        'Глина мятая (кубометр)':(40 / 0.7) / 2600 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.5*0.5*0.6) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.5*0.5*0.6) / 0.75,
        }

#----
# Производства (посуда)
    # Хороший гончар делает 70-140 горшков/день (15 000 за год, 5-15 минут/горшок)
    # Обжигают горшки партиями по 3000 (раз в месяц) в земляном горне или в шахтной печи.
    # http://avtor-dona.ru/kazachij-kuren/kukhnya-kazakov/kukhonnaya-posuda-i-utvar

metadict_detail['_Производство керамической посуды (горшок 10-литровый)'] = {
        # Площадь глазури, это площадь двух сфер по наибольшему радиусу.
        # Габариты 300x300x300-мм, масса 4 кг.
        '_Лепка глиняных изделий (рабочих часов)':10 / 60,
        'Глина мятая (кубометр)':(4 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.3/2) ** 2) * 2 * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.3*0.3*0.3) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.3*0.3*0.3) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.3*0.3*0.3) / 0.75,
        }

metadict_detail['_Производство керамической посуды (горшок 5-литровый)'] = {
        # Габариты 250x250x250-мм, масса 3 кг.
        '_Лепка глиняных изделий (рабочих часов)':7 / 60,
        'Глина мятая (кубометр)':(3 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.25/2) ** 2) * 2 * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.25*0.25*0.25) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.25*0.25*0.25) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.25*0.25*0.25) / 0.75,
        }

metadict_detail['_Производство керамической посуды (горшок 3-литровый)'] = {
        # Габариты 200x200x200-мм, масса 1.2 кг.
        '_Лепка глиняных изделий (рабочих часов)':5 / 60,
        'Глина мятая (кубометр)':(1.2 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.2/2) ** 2) * 2 * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.2*0.2*0.2) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.2*0.2*0.2) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.2*0.2*0.2) / 0.75,
        }

metadict_detail['_Производство керамической посуды (горшок 1-литровый)'] = {
        # Габариты 150x150x150-мм, масса 0.6 кг.
        '_Лепка глиняных изделий (рабочих часов)':5 / 60,
        'Глина мятая (кубометр)':(0.6 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.15/2) ** 2) * 2 * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.15*0.15*0.15) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.15*0.15*0.15) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.15*0.15*0.15) / 0.75,
        }

metadict_detail['_Производство керамической посуды (кувшин 5-литровый)'] = {
        # Габариты 250x250x250-мм, масса 3 кг.
        '_Лепка глиняных изделий (рабочих часов)':7 / 60,
        'Глина мятая (кубометр)':(3 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.25/2) ** 2) * 2 * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.25*0.25*0.25) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.25*0.25*0.25) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.25*0.25*0.25) / 0.75,
        }

metadict_detail['_Производство керамической посуды (кувшин 3-литровый)'] = {
        # Габариты 200x200x200-мм, масса 1.2 кг.
        '_Лепка глиняных изделий (рабочих часов)':5 / 60,
        'Глина мятая (кубометр)':(1.2 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.2/2) ** 2) * 2 * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.2*0.2*0.2) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.2*0.2*0.2) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.2*0.2*0.2) / 0.75,
        }

metadict_detail['_Производство керамической посуды (кофейник 1-литровый)'] = {
        # Габариты 150x150x150-мм, масса 0.6 кг.
        '_Лепка глиняных изделий (рабочих часов)':30 / 60,
        'Глина мятая (кубометр)':(0.6 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.15/2) ** 2) * 2 * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.15*0.15*0.15) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.15*0.15*0.15) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.15*0.15*0.15) / 0.75,
        }

metadict_detail['_Производство керамической посуды (чайник 1-литровый)'] = {
        # Габариты 150x150x150-мм, масса 0.6 кг.
        '_Лепка глиняных изделий (рабочих часов)':30 / 60,
        'Глина мятая (кубометр)':(0.6 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.15/2) ** 2) * 2 * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.15*0.15*0.15) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.15*0.15*0.15) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.15*0.15*0.15) / 0.75,
        }

metadict_detail['_Производство керамической посуды (ступа 5-литровая)'] = {
        # Габариты 400x400x150-мм, масса 3 кг.
        # Площадь глазури, это площадь сферы (двух полусфер).
        '_Лепка глиняных изделий (рабочих часов)':10 / 60,
        'Глина мятая (кубометр)':(3 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.4/2) ** 2) * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.4*0.4*0.15) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.4*0.4*0.15) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.4*0.4*0.15) / 0.75,
        }

metadict_detail['_Производство керамической посуды (миска 5-литровая)'] = {
        # Габариты 400x400x150-мм, масса 3 кг.
        '_Лепка глиняных изделий (рабочих часов)':5 / 60,
        'Глина мятая (кубометр)':(3 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.4/2) ** 2) * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.4*0.4*0.15) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.4*0.4*0.15) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.4*0.4*0.15) / 0.75,
        }

metadict_detail['_Производство керамической посуды (миска 3-литровая)'] = {
        # Габариты 300x300x100-мм, масса 1.2 кг.
        '_Лепка глиняных изделий (рабочих часов)':5 / 60,
        'Глина мятая (кубометр)':(1.2 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.3/2) ** 2) * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.3*0.3*0.1) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.3*0.3*0.1) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.3*0.3*0.1) / 0.75,
        }

metadict_detail['_Производство керамической посуды (миска 0.5-литровая)'] = {
        # Габариты 200x200x50-мм, масса 0.4 кг.
        '_Лепка глиняных изделий (рабочих часов)':5 / 60,
        'Глина мятая (кубометр)':(0.4 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(4 * 3.14 * (0.2/2) ** 2) * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.2*0.2*0.05) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.2*0.2*0.05) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.2*0.2*0.05) / 0.75,
        }

metadict_detail['_Производство керамической посуды (кружка 0.5-литровая)'] = {
        # Габариты 150x150x150-мм, масса 0.6 кг.
        # Площадь глазури, это площадь двух цилиндров.
        # https://www.townsends.us/collections/food-drink/products/english-tankard
        '_Лепка глиняных изделий (рабочих часов)':5 / 60,
        'Глина мятая (кубометр)':(0.6 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(2 * 3.14 * (0.15/2) * (0.15 + (0.15/2))) * 2 * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.15*0.15*0.15) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.15*0.15*0.15) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.15*0.15*0.15) / 0.75,
        }

metadict_detail['_Производство керамической посуды (чашка 0.25-литровая)'] = {
        # Габариты 70x70x100-мм, масса 0.3 кг.
        '_Лепка глиняных изделий (рабочих часов)':5 / 60,
        'Глина мятая (кубометр)':(0.3 / 0.7) / 2600 / 0.75,
        'Глазурь стеклянная (кубометр)':(2 * 3.14 * (0.07/2) * (0.1 + (0.07/2))) * 2 * 0.0003 / 0.75,
        '_-Сушка глиняного изделия (кубометр)':(0.07*0.07*0.1) / 0.75,
        '_-Обжиг керамики в печи (кубометр)':(0.07*0.07*0.1) / 0.75,
        '_-Глазурование керамики окунанием и обжигом (кубометр)':(0.07*0.07*0.1) / 0.75,
        }

#----
# Производства (лепка)

metadict_detail['_Лепка глиняных изделий (рабочих часов)'] = {
        # Лепка, это около 50% работы в мастерской.
        '_-Работа на производстве керамических изделий (нормо-часов)':1,
        'Использование простого гончарного станка (часов)':1,
        '_Гончарная мастерская (годовой оборот)':1 / 1600,
        }

#----
# Утилизация (утварь и посуда)

metadict_detail['_Утилизация керамической утвари (килограмм)'] = {
        # Битые горшки --> помол на мельнице --> мука для улучшения качеств глины
        # Используют по надобности, а так накапливается в куче за мастерской.
        '+Керамическая утварь, битая (доступно/килограмм)':1,
        }

#----
# Производства (капитализация)

metadict_detail['_Кирпичный завод (годовой оборот)'] = {
        #'Кирпичный завод (капитализация)':1/10,
        #'Фабричные рабочие (кирпич)':60,
        }

metadict_detail['_Кафельный завод (годовой оборот)'] = {
        #'Кирпичный завод (капитализация)':1/10,
        #'Фабричные рабочие (кафель)':80,
        }

metadict_detail['_Черепичный завод (годовой оборот)'] = {
        #'Кирпичный завод (капитализация)':1/10,
        #'Фабричные рабочие (черепица)':50,
        }

metadict_detail['_Гончарная мастерская (годовой оборот)'] = {
        #'Гончарная мастерская (капитализация)':1/10,
        #'Фабричные рабочие (керамика)':10,
        }
