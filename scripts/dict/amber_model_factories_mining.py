#----
# Заметки:
    # Рудник Тетюхе, Сихоте-Алинь, свинцово-цинковые руды, 1914 год
    # Ресурсы (~8 млн кубометров руды) -- 131 000 тонн свинца, 250 000 тонн меди, 268 тонн серебра
        # Экспорт:
        # - Цинковые руды, галмея (обжиг, 55% цинка) -- 44.3 рубля/тонна
        # - Серебро-свинцовые руды (концентрат, 71% свинца, 4.5% цинк, 1.1 кг серебра) -- 1068 рублей/тонна
        # Себестоимость:
        # - Оплата труда к добытой руде -- 11 рублей/тонна
        # - Себестоимость руды -- 22.18 рублей (64% транспортировка)
        # 42 км узкоколейная железная дорога до бухты, конные дрезины
    # Посёлок (1912 год) 120 дворов, 1072 жителей, 641 временных работника
        # Владения АГОТ с рудниками -- 145 000 гектаров
        # Акционерное общество Тетюхе (АГОТ, 1909 год) -- 1 млн рублей (4 тысячи акций)
        # 37 домов (84 квартиры, 103 комнаты) -- 52 кубометра/комната, 15 кв.метров/комната
        # 43 казармы (по 15-30 рабочих) -- 423 кубометра/казарма, 61 кв.метр/казарма
        # Рудообогатительная фабрика -- 80 тонн сырой руды за 10-часовую смену (8 тонн/час)
        # Три паровых котла на 237 м² нагрева; паровая машина с 250 л холодильником; динамо-машина на 37 кВт
        # Зарплаты (38% капитала/год) -- 95 рублей/год-рабочего (считая сезонных)
        # Зарплаты шахтёров (12 часов смена) -- 1.26-2.86 руб/день, 21-31 рублей/месяц
        # 75% рабочих -- китайцы
    # Добыча (1914 год) -- 4 рудника 32 штольни
        # - Пройдено 465 000 кубометров/год
        # - цинковых руд (галмея) -- 20 300 тонн
        # - серебро-свинцовых руд -- 13 800 тонн
        # Руда сортировалась вручную. 33% худшей сразу в отвалы.
        # Сортированная руда -- 17.9% цинка, 12.78% свинца, 0.025% серебра
        # После обжига руда теряла 30% пустого веса (вода и углекислота)
    # http://www.bryners.ru/content.php?material=38

#----
# Добыча открытым способом (мелкие карьеры)
    # ЭКСКАВАЦИЯ И ТРАНСПОРТИРОВАНИЕ ГОРНОЙ МАССЫ АВТОСАМОСВАЛАМИ
        # http://www.libussr.ru/doc_ussr/usr_14571.htm
    # ОБ УТВЕРЖДЕНИИ ЕДИНЫХ НОРМ ВЫРАБОТКИ И ВРЕМЕНИ НА ПРОИЗВОДСТВО ЩЕБНЯ
        # http://www.libussr.ru/doc_ussr/usr_15964.htm

metadict_detail['_Добыча торфа с прессованием (кубометр)'] = {
        # Артель (2 резчика, 2 с подводами, 2 кладчика) -- 12 000 плиток/день (до 200 метров отвоза)
            # Производительность -- 9.2 кубометров/день-рабочего (4 кубометра сухого, 848 кг/день)
            # Трудозатраты -- 0.012-0.014 нормо-часа/кг (при 10-12 часах работы в день)
            # https://ru.wikisource.org/wiki/ЭСБЕ/Угли_бурые_и_их_переработка
        # За лето снимают слой 0.133 метра (один ряд плиток) -- 1330 кубов сырого торфа
            # 1330 кубометров сырого торфа = 580 кубометров сухого (124 тонны, 4% запаса)
            # 580 кубометров сухого торфа = 265 кубометров прессованного
            # https://ru.wikisource.org/wiki/ЭСБЕ/Торфяная_культура
            # https://ru.wikisource.org/wiki/ЭСБЕ/Болота
        'Участок торфяника под добычу (гектар)':1 / 265,
        '_-Резка торфа упряжными скреперами (кубометр)':1 / ((265 / 580) * (580 / 1330)),
        '_-Сушка торфа на подготовленном поле (кубометр)':1 / ((265 / 580) * (580 / 1330)),
        '_-Прессование торфа на мобильном прессе (кубометр)':1 / (265 / 580),
        '_Артель добычи торфа (годовой оборот)':1 / (265 * 10),
        }

metadict_model['_Добыча глины (кубометр)'] = {
        # Местечковые карьеры. Есть почти в каждом кантоне.
        # Мощность пласта -- 1-3 метра, глубина -- 2-4 метра
        '_-Котлован (кубометр)':2 / 2,
        '_-Разработка грунта упряжными скреперами, с помощью Mold_Earth (кубометр)':1,
        '_Карьер, глина (годовой оборот)':1 / 5000,
        }

metadict_model['_Добыча песка (кубометр)'] = {
        '_-Котлован (кубометр)':1,
        '_-Разработка грунта упряжными скреперами, с помощью Mold_Earth (кубометр)':1,
        '_Карьер, песок (годовой оборот)':1 / 5000,
        }

metadict_model['_Добыча гравия (кубометр)'] = {
        # Это обкатанные водой камешки, добывают на берегах рек.
        '_-Котлован (кубометр)':1,
        '_-Разработка щебня упряжными скреперами, с помощью Mold_Earth (кубометр)':1,
        '_Карьер, гравий (годовой оборот)':1 / 5000,
        }

#----
# Добыча открытым способом (крупные карьеры)

metadict_detail['_Добыча щебня (кубометр)'] = {
        # Месторождение бутового камня взрывают. Затем дробят на дробилках "грохотах" -- 30% потерь.
        # Каменоломни Европейской России (1895 год?) -- 3.2 млн.кубов, 50 000 кубометров/карьер.
        '_-Котлован (кубометр)':1 / 0.7,
        '_-Подрывные работы (кубометр)':1 / 0.7,
        '_-Разработка щебня упряжными скреперами, с помощью Mold_Earth (кубометр)':1 / 0.7,
        '_-Дробление щебня в дробилке (кубометр)':1 / 0.7,
        '_Карьер, щебень (годовой оборот)':1 / 50000,
        }

metadict_detail['_Добыча известняка (кубометр)'] = {
        # Тот же щебень.
        '_-Котлован (кубометр)':1 / 0.7,
        '_-Подрывные работы (кубометр)':1 / 0.7,
        '_-Разработка щебня упряжными скреперами, с помощью Mold_Earth (кубометр)':1 / 0.7,
        '_-Дробление известняка в дробилке (кубометр)':1 / 0.7,
        '_Карьер, известняк (годовой оборот)':1 / 50000,
        }

metadict_detail['_Добыча бутового камня (кубометр)'] = {
        # Это камни ~50 кг весом. Подрыв неэффективен, булыжники раскалывают расширением льда.
        '_-Котлован (кубометр)':1 / 0.9,
        '_-Ударно-вращательное бурение скважин (кубометр)':1 / 0.9,
        '_-Разработка бутового камня гидродинамическая, с помощью Shape_Water (кубометр)':1 / 0.9,
        '_Карьер, бутовый камень (годовой оборот)':1 / 50000,
        }

metadict_detail['_Добыча асбестовой руды (кубометр)'] = {
        # В карьерах, открытым способом. Не сложнее добычи щебня.
        '_-Котлован (кубометр)':1 / 0.9,
        '_-Подрывные работы (кубометр)':1 / 0.9,
        '_-Разработка руды упряжными скреперами, с помощью Mold_Earth (кубометр)':1 / 0.9,
        '_Карьер, асбестовая руда (годовой оборот)':1 / 50000,
        }

#----
# Производства (строительные материалы)

metadict_detail['_Производство глины мятой (кубометр)'] = {
        # Плотность обычной глины -- 1.9 тонны/кубометр; а мятой -- 2.6 тонны/кубометр
            # https://ru.wikisource.org/wiki/ЭСБЕ/Глина,_в_технике
            # https://ru.wikisource.org/wiki/ЭСБЕ/Глиномятка
        '_-Замачивание глины (кубометр)':1 / (1.9 / 2.6),
        '_-Уплотнение глины (кубометр)':1 / (1.9 / 2.6),
        'Глина необработанная (кубометр)':1 / (1.9 / 2.6),
        '_Производство глины мятой (годовой оборот)':1 / 5000,
        }

metadict_detail['_Производство извести негашёной (тонн)'] = {
        # 1) Раздробить.
        # 2) Обжечь.
        # 3) Размолоть.
        # Плотность известняка -- 1.6 тонны/кубометр
        'Известняк (килограмм)':1000 / 0.9,
        '_-Дробление известняка в дробилке (кубометр)':(1 / 0.9) / 1.6,
        '_-Обжиг известняка в шахтной печи (тонн)':1 / 0.9,
        '_-Помол известняка на шаровой мельнице (тонн)':1 / 0.9,
        '_-Процеживание извести на проволочном сите (тонн)':1 / 0.9,
        '_Производство извести негашёной (годовой оборот)':1 / 5000,
        }

metadict_detail['_Производство мелового порошка (тонн)'] = {
        # Мел, это известняк.
        # 1) Раздробить с водой (чтобы вымыть примеси)
        # 2) Высушить
        # 3) Размолоть.
        # Насыпная плотность мелового порошка -- 1100 кг/кубометр
        # Плотность известняка -- 1.6 тонны/кубометр
        'Известняк (килограмм)':1000 / 0.9,
        '_-Дробление известняка в дробилке (кубометр)':(1 / 0.9) / 1.6,
        '_-Помол известняка на шаровой мельнице (тонн)':1 / 0.9,
        '_Производство мелового порошка (годовой оборот)':1 / 5000,
        }

metadict_detail['_Производство асбеста (тонн)'] = {
        # Сортировочная фабрика
            # 1) Сушка руды во вращающихся печах
            # 2) Дробление руды на грохоте (предварительное)
            # 3) Сортировка руды на вращающихся барабанах
            # 4) Дробление на шаровой мельнице (низкие сорта в пыль)
            # 5) Провеивание пыли вентиляторами (отделяем пустую породу)
            # - Вентиляторное отделение --> упаковочное отделение (не более 3% примесей)
            # - Пустая порода --> отвал
            # https://istmat.org/node/59230
        # Выход асбеста (1918-1929 годы, Канада) -- 53-57 кг/тонну руды
        # Содержание волокон асбеста в руде 5-9%, влажность ~5%
            # Влажность руды, это проблема грунтовых вод Баженовского месторождения.
            # https://ru.wikipedia.org/wiki/Баженовское_месторождение
        # Плотность асбестовой руды 2.5 тонны/кубометр
        'Асбестовая руда (килограмм)':1000 / 0.05,
        '_-Сушка асбестовой руды в шахтной печи, 5% влажность (кубометр)':1 / 0.05 / 2.5,
        '_-Дробление руды в дробилке (кубометр)':1 / (0.05 / 0.95) / 2.5,
        # Далее в тоннах руды (0.05 асбеста)
        '_-Сортировка руды на сетчатом барабане (тонн)':1 / (0.05 / 0.95),
        '_-Помол руды на шаровой мельнице (тонн)':1 / (0.05 / 0.8),
        '_-Провеивание руды на сетчатом барабане с вентилятором (тонн)':1 / (0.05 / 0.8),
        # Высшие сорта асбеста отделяют сортировкой (мельница их испортит):
        '_Обогатительный комбинат, асбест (годовой оборот)':1 / 20000,
        '+Асбест-сырец высшего сорта (доступно/килограмм)':50,
        }

metadict_detail['_Производство цемента (тонн)'] = {
        # TODO: Провеивание цемента. Гашение извести -- 20 дней
        # Технологическая карта:
            # 1) Гашёную известь и сухую глину в мелкий порошок.
            # 2) Порошок спрессовать в куски.
            # 3) Куски смеси обжечь.
            # 4) Раздробить в мелкий порошок.
            # https://istmat.org/node/27439
            # https://ru.wikisource.org/wiki/ЭСБЕ/Цементы
        # Цементные заводы (Дисдорф, 1895 год, 150 рабочих, 410 кВт) -- 25 500 тонн/год
            # 170 тонн/рабочего, 9.4 нормо-часа/тонна
            # Шаровая мельница для цемента (17 кВт) -- 1062 тонн/год (~3.54 тонны/день, ~0.22 тонны/час)
        # Цементные заводы (Манингейм, 1895 год, 900 рабочих, 850 кВт) -- 51 000 тонн/год
            # 56 тонн/рабочего, 28.6 нормо-часа/тонна
        # Состав:
            # 80% -- углекислой извести.
            # 20% -- глины.
            # 45% воды в тесте, 2-3 недели перемешивания и перетирания в мельницах.
        'Известняк (килограмм)':800 / 0.9,
        'Глина мятая (килограмм)':200 / 0.9,
        'Вода для промышленности (литр)':500 / 0.9,
        '_-Помол известняка на шаровой мельнице (тонн)':0.8 / 0.9,
        '_-Помол глины мятой на шаровой мельнице (тонн)':0.2 / 0.9,
        '_-Процеживание глино-известнякового теста на проволочном сите (тонн)':1.5 / 0.9,
        '_-Формирование глино-известнякового теста для обжига (тонн)':1.5 / 0.9,
        '_-Обжиг глино-известнякового теста в шахтной печи (тонн)':1.5 / 0.9,
        '_-Дробление цемента в дробилке (тонн)':1 / 0.9,
        '_-Помол цемента на шаровой мельнице (тонн)':1 / 0.9,
        '_-Процеживание цемента на проволочном сите (тонн)':1 / 0.9,
        '_-Уплотнение цемента (тонн)':1,
        '_Производство цемента (годовой оборот)':1 / 20000,
        }

#----
# Производства (капитализация)

metadict_detail['_Карьер, глина (годовой оборот)'] = {
        #'Карьер, глина (капитализация)':1/10,
        #'Наёмные рабочие (карьер)':5,
        }

metadict_detail['_Карьер, гравий (годовой оборот)'] = {
        #'Карьер, гравий (капитализация)':1/10,
        #'Наёмные рабочие (карьер)':5,
        }

metadict_detail['_Карьер, песок (годовой оборот)'] = {
        #'Карьер, песок (капитализация)':1/10,
        #'Наёмные рабочие (карьер)':5,
        }

metadict_detail['_Производство глины мятой (годовой оборот)'] = {
        #'Цементная фабрика (капитализация)':1/10,
        #'Наёмные рабочие (цементная фабрика)':5,
        }

metadict_detail['_Производство мелового порошка (годовой оборот)'] = {
        #'Цементная фабрика (капитализация)':1/10,
        #'Наёмные рабочие (цементная фабрика)':5,
        }

metadict_detail['_Производство извести негашёной (годовой оборот)'] = {
        #'Цементная фабрика (капитализация)':1/10,
        #'Наёмные рабочие (цементная фабрика)':30,
        }

metadict_detail['_Производство цемента (годовой оборот)'] = {
        #'Цементная фабрика (капитализация)':1/10,
        #'Наёмные рабочие (цементная фабрика)':200,
        }

metadict_detail['_Обогатительный комбинат, асбест (годовой оборот)'] = {
        #'Карьер, щебень (капитализация)':1/10,
        #'Наёмные рабочие (карьер)':400,
        }

metadict_detail['_Карьер, бутовый камень (годовой оборот)'] = {
        #'Карьер, бутовый камень (капитализация)':1/10,
        #'Наёмные рабочие (карьер)':150,
        }

metadict_detail['_Карьер, известняк (годовой оборот)'] = {
        #'Карьер, известняк (капитализация)':1/10,
        #'Наёмные рабочие (карьер)':50,
        }

metadict_detail['_Карьер, щебень (годовой оборот)'] = {
        #'Карьер, щебень (капитализация)':1/10,
        #'Наёмные рабочие (карьер)':50,
        }

metadict_detail['_Карьер, асбестовая руда (годовой оборот)'] = {
        #'Карьер, щебень (капитализация)':1/10,
        #'Наёмные рабочие (карьер)':50,
        }

metadict_detail['_Артель добычи торфа (годовой оборот)'] = {
        #'Артель добычи торфа (капитализация)':1/2,
        #'Наёмные рабочие (торф)':10,
        }
