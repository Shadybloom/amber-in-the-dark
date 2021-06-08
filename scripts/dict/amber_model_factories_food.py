#----
# Фабрики (продовольствие)
    # Список фабрик и заводов Российской империи (1907-1909 годы):
    # http://istmat.info/node/26498

metadict_detail['_Обмолот зерновых (килограмм)'] = {
        # Молотилка (4 кВт, 12 рабочих) -- 6000 килограмм/день (сезон 60 дней/год)
        '_-Обмолот растений фабричный (килограмм)':1,
        '_Молотилка (годовой оборот)':1 / 360000,
        }

metadict_detail['_Обмолот масличных культур (килограмм)'] = {
        '_-Обмолот растений фабричный (килограмм)':1,
        '_Молотилка (годовой оборот)':1 / 360000,
        }

metadict_detail['_Обмолот пряных растений (килограмм)'] = {
        '_-Обмолот растений фабричный (килограмм)':1,
        '_Молотилка (годовой оборот)':1 / 360000,
        }

metadict_detail['_Чистка и сушка бобов (килограмм)'] = {
        '_-Обмолот растений фабричный (килограмм)':1,
        '_Молотилка (годовой оборот)':1 / 360000,
        }

metadict_detail['_Помол зерна (килограмм)'] = {
        # Производство: 5 тонн/сутки, 1000 тонн/год (снабжение кантона)
            # https://ru.wikisource.org/wiki/ЭСБЕ/Мельницы
        # Пример №2: 100 тонн/сутки, 30 000 тонн/год (снабжение округа)
            # 13 рабочих в смене, 39 рабочих на 3 смены/день (0.00312 нормо-часа/килограмм муки)
            # Машина в 150-185 киловатт.
            # https://istmat.info/node/27392
        '_-Помол зерна (килограмм)':1,
        '_Мельница (годовой оборот)':1 / 1000000,
        }

metadict_detail['_Помол крупы (килограмм)'] = {
        '_-Помол крупы (килограмм)':1,
        '_Мельница (годовой оборот)':1 / 1000000,
        }

metadict_detail['_Чистка и дробление зерна (килограмм)'] = {
        '_-Чистка и дробление зерна (килограмм)':1,
        '_Мельница (годовой оборот)':1 / 1000000,
        }

metadict_detail['_Чистка и шлифование зерна (килограмм)'] = {
        '_-Чистка и шлифование зерна (килограмм)':1,
        '_Мельница (годовой оборот)':1 / 1000000,
        }

metadict_detail['_Чистка и обжаривание зерна (килограмм)'] = {
        '_-Чистка и обжаривание зерна (килограмм)':1,
        '_Мельница (годовой оборот)':1 / 1000000,
        }

metadict_detail['_Производство шоколада (килограмм)'] = {
        # Производство: 0.5 тонн/сутки, 100 тонн/год (снабжение округа)
        '_-Производство шоколада (килограмм)':1,
        '_Кондитерская фабрика (годовой оборот)':1 / 100000,
        }

metadict_detail['_Производство картофельного крахмала (килограмм)'] = {
        # Производство: 0.5 тонны/сутки, 100 тонн/год (снабжение округа)
            # https://ru.wikisource.org/wiki/ЭСБЕ/Крахмальное_производство
            # https://znaytovar.ru/s/Texnologicheskaya_liniya_proizvod33.html
            # http://howtogetrid.ru/kak-sdelat-kraxmal-v-domashnix-usloviyax/
            # https://propozitsiya.com/druge-narodzhennya-krohmalnoyi-galuzi-keys-vid-pbp-vimal
        'Картофель (килограмм)':20,
        '_-Переработка картофеля в крахмал (килограмм)':20,
        '_Крахмальный завод (годовой оборот)':1 / 100000,
        }

metadict_detail['_Производство агар-агара (килограмм)'] = {
        # TODO:
            # Уточни расход водорослей
        'Водоросли красные (килограмм)':20,
        '_-Переработка водорослей в агар-агар (килограмм)':20,
        '_Крахмальный завод (годовой оборот)':1 / 100000,
        }

metadict_detail['_Производство тростникового сахара (килограмм)'] = {
        # Производство: 5 тонн/сутки, 1000 тонн/год (снабжение округа)
        # Эффективность производства: 10 тонн/рабочего в год
            # Очень неточно, по годовому обороту и рыночным ценам сахара-песка (1914 год)
            # Список фабрик и заводов Российской империи
        'Сахар-сырец тростниковый (килограмм)':1.1,
        '_-Рафинирование тростникового сахара-сырца (килограмм)':1.1,
        '_Рафинадный завод (годовой оборот)':1 / 1000000,
        }

metadict_detail['_Производство тростникового сахара-сырца (килограмм)'] = {
        # Производство: 5 тонн/сутки, 1000 тонн/год (снабжение округа)
        # Примитивный техпроцесс, из 10% сахарозы в стеблях извлекают только 5% сахара.
        'Сахарный тростник (килограмм)':20,
        'Известь свежегашёная (килограмм)':0.014,
        '_-Переработка сахарного тростника в сахар-сырец (килограмм)':20,
        '_Сахарный завод (годовой оборот)':1 / 1000000,
        }

metadict_detail['_Производство чёрной патоки (килограмм)'] = {
        # TODO:
            # Уточнить. Побочный продукт сахарного производства.
        'Сахарный тростник (килограмм)':20,
        'Известь свежегашёная (килограмм)':0.014,
        '_-Переработка сахарного тростника в сахар-сырец (килограмм)':20,
        '_Сахарный завод (годовой оборот)':1 / 1000000,
        }

metadict_detail['_Производство соли (килограмм)'] = {
        # Солеварение:
            # https://ru.wikisource.org/wiki/ЭСБЕ/Соль_поваренная
            # http://historic.ru/books/item/f00/s00/z0000171/st011.shtml
        # Соликамск 1742 года (sic!), "Путешествие в Сибирь" Гмелина:
            # https://uraloved.ru/starosti/gmelin-puteshestvie-v-sibir
            # Сковорода 7.9x7.7x0.36 -- 61 кв.метр, 21 кубометр (46 000 МДж при 100% КПД)
            # 21 кубометр рассола = 28 мешков соли (4 пуда/мешок, 65 кг/мешок, 1800 кг всего)
            # 1800 кг соли за 67 кубометра дров (37 тонн, 15 МДж/кг, 555 000 МДж всего, 8% КПД)
            # Металлические листы менять раз в неделю-другую из-за прогорания. 
        # Производство: 1.8 тонны/сутки, 360 тонн/год (снабжение округа)
        # 12 литров рассола на килограмм соли. Выпаривают 24 часа.
        'Солевой раствор 9% природный (литр)':12,
        '_-Выпаривание воды из рассола (килограмм)':12,
        '_Солеварня (годовой оборот)':1 / 360000,
        }

#----
# Фабрики (масло)
    # Содержание масла (Российская империя 1900 года):
    # | Растение           | Жира (%)       | Белков        | Воды
    # | ------------------ | -------------- | ------------- | ----------
    # | Рапс озимый*       | 43.96          | 19.25         | 5
    # | Рапс яровой*       | 37.33          | 24.50         | 5
    # | Сурепица           | 30.90 - 37.11  | 23.13 - 27.00 | 4.8 - 15.6
    # | Лён                | 32.50 - 34.00  | 23.00 - 24.70 | 6.6 - 7.0 
    # | Конопля            | 30.36 - 34.00  | 23.12 - 24.30 | 5.6 - 10.0
    # | Мак                | 38.46 - 43.00  | 23.40 - 24.09 | 4.2 - 6.4 
    # | Лаллеманция        | 22.12 - 28.24  | -             | 6.63      
    # | Кунжут             | 55.17          | -             | 3.63      
    # * Рапсовое масло -- техническое. Оно токсично без современных методов рафинирования.
    # Содержание масла (Европейская торговля 1900 года):
    # | Растение           | Жира (%) 
    # | ------------------ | ---------
    # | Лён                | 37.0     
    # | Рапс               | 42.5     
    # | Конопля            | 33.6     
    # | Мак                | 41.0     
    # | Magia семя         | 38.8     
    # | Рыжиковое семя     | 30.0     
    # | Подсолнечник*      | 23.6     
    # | Хлопчатник         | 30.3     
    # | Кунжут             | 37.0     
    # | Арахис             | 41.2     
    # | Оливки*            | 50 - 70
    # * Оливки обезвоженные -- в свежих 15% жира
    # https://fdc.nal.usda.gov/fdc-app.html#/food-details/1103679/nutrients
    # Подсолнечник с учётом 40% лузги, в самих семенах содержится 33-34% масла.
    # - Прессование. В льняных жмыхах остаётся -- 6.6-16.5% масла (11% масла)
    # - Прессование. Остатки от прессования оливок -- 12-28% масла (20% масла)
    # - Экстракция бензином (аппарат Мерца). В экстракционных остатках -- 2% масла
    # https://ru.wikisource.org/wiki/ЭСБЕ/Маслобойное_и_маслоэкстракционное_производства
    # https://ru.wikisource.org/wiki/ЭСБЕ/Жмыхи
    # http://vidkormov.narod.ru/card/n351.html

metadict_detail['_Производство подсолнечного масла (килограмм)'] = {
        # Доступно масла:
            # - Жира -- 23.6%.
            # - Прессование даёт -- 13%
            # - Экстракция даёт -- 21%
            # - Остаток -- 2.6%
            # https://ru.wikisource.org/wiki/ЭСБЕ/Подсолнечник
            # https://farmet.com.ua/?page_id=210
        # Сначала прессование, затем экстракция
            # Производство 500+ тыс. кг/год даёт возможность эффективно использовать экстракцию.
            # Лузга -- 40% семени подсолнечника.
        '_-Очистка семян на сетчатом барабане (килограмм)':1 / 0.21,
        '_-Лущение семян на вальцовой молотилке (килограмм)':1 / 0.21 * 0.95,
        '_-Помол семян на вальцовой мельнице (килограмм)':1 / 0.21 * 0.55,
        '_-Подогревание муки на паровой сковороде (килограмм)':1 / 0.21 * 0.55,
        '_-Отжим масла из муки гидравлическим прессом (килограмм)':1 / 0.21 * 0.55,
        '_-Экстракция масла из муки сернистым эфиром (килограмм)':1 / 0.21 * 0.42,
        '_-Отстаивание масла в чане (килограмм)':1.07,
        '_-Фильтрование масла паклей и опилками (килограмм)':1.04,
        '_-Рафинирование масла серной кислотой (килограмм)':1.02,
        'Семена подсолнечника (килограмм)':1 / 0.21,
        '+Отруби подсолнечные (доступно/килограмм)':1 / 0.21 * (0.95 - 0.55),
        '+Жмых подсолнечный (доступно/килограмм)':1 / 0.21 * (0.55 - 0.21),
        '_Маслоэкстракционный завод (годовой оборот)':1 / 500000,
        }

metadict_detail['_Производство льняного масла (килограмм)'] = {
        # Каталог 12-й осенней сельско-хозяйственной и промышленной выставки Ростов на Дону, 1908 год
            # - масло льняное, олифа (опт, 30 раб) -- 0.3 руб/кг (0.073 нормо-часа)
            # - масло подсолнечное (опт, 40 раб) -- 0.24 руб/кг (0.04 нормо-часа)
            # - масло льняное -- 362 рублей/тонна
        # Список фабрик и заводов российской империи, 1912 год
            # Владимирская губерния, Бр. Бабушкины, Маслобойный завод
            # Выработка: льняное масло, 137 000 рублей/год (год. производство 186 000 рублей)
                # Оценочно: 137000 / 0,36 = 380 555 кг масла (1 463 673 кг семени льна, 26%)
            # Число рабочих -- 18
                # Оценочно: ((137000 / 0,36) × 0,073) / (8 × 200) ≈ 17,36284722 рабочих
            # Двигатели нефтяные, 50 лс -- 35.5 кВт
        # Доступно масла:
            # - Жира -- 37.0%.
            # - Прессование даёт -- 26%
            # - Экстракция даёт -- 34%
            # - Остаток -- 2.6%
        # Только прессование, без экстракции (выход 0.26).
            # Производство 300+ тыс. кг/год позволяет эффективно использовать 300-кг/час 30-кВт прессы.
        '_-Очистка семян на сетчатом барабане (килограмм)':1 / 0.26,
        '_-Лущение семян на вальцовой молотилке (килограмм)':1 / 0.26 * 0.95,
        '_-Помол семян на вальцовой мельнице (килограмм)':1 / 0.26 * 0.7,
        '_-Подогревание муки на паровой сковороде (килограмм)':1 / 0.26 * 0.7,
        '_-Отжим масла из муки гидравлическим прессом (килограмм)':1 / 0.26 * 0.7,
        '_-Отстаивание масла в чане (килограмм)':1.07,
        '_-Фильтрование масла паклей и опилками (килограмм)':1.04,
        '_-Рафинирование масла серной кислотой (килограмм)':1.02,
        'Семена льна (килограмм)':1 / 0.26,
        '+Отруби льняные (доступно/килограмм)':1 / 0.26 * (0.95 - 0.7),
        '+Жмых льняной (доступно/килограмм)':1 / 0.26 * (0.7 - 0.26),
        '_Маслобойный завод (годовой оборот)':1 / 300000,
        }

metadict_detail['_Производство конопляного масла (килограмм)'] = {
        # Доступно масла:
            # - Жира -- 33.6%.
            # - Прессование даёт -- 23%
            # - Экстракция даёт -- 31%
            # - Остаток -- 2.6%
        # Только прессование, без экстракции (выход 0.23).
        '_-Очистка семян на сетчатом барабане (килограмм)':1 / 0.23,
        '_-Лущение семян на вальцовой молотилке (килограмм)':1 / 0.23 * 0.95,
        '_-Помол семян на вальцовой мельнице (килограмм)':1 / 0.23 * 0.7,
        '_-Подогревание муки на паровой сковороде (килограмм)':1 / 0.23 * 0.7,
        '_-Отжим масла из муки гидравлическим прессом (килограмм)':1 / 0.23 * 0.7,
        '_-Отстаивание масла в чане (килограмм)':1.07,
        '_-Фильтрование масла паклей и опилками (килограмм)':1.04,
        '_-Рафинирование масла серной кислотой (килограмм)':1.02,
        'Семена конопли (килограмм)':1 / 0.23,
        '+Отруби конопляные (доступно/килограмм)':1 / 0.23 * (0.95 - 0.7),
        '+Жмых конопляный (доступно/килограмм)':1 / 0.23 * (0.7 - 0.23),
        '_Маслобойный завод (годовой оборот)':1 / 300000,
        }

metadict_detail['_Производство оливкового масла (килограмм)'] = {
        # Техпроцессы:
            # 1) Лучший сорт (прованское масло) -- слабое прессование на холоде.
                # - Горизонтальные жернова, без дробления ядер.
            # 2) Вторая выжимка -- обычное прессование с нагреванием горячей водой.
                # - Осаждение ядер -- к мезге добавляют воды, тяжёлые ядра оседают.
            # 3) Третья выжимка -- кипячение для отделения воды, прессование твёрдой массы
                # - Часть масла всплывает при кипячении, часть от прессования.
            # 4) Экстракция масла сернистым углеродом (деревянное масло, техническое масло)
            # https://ru.wikisource.org/wiki/ЭСБЕ/Маслобойное_и_маслоэкстракционное_производства
        # Доступно масла (сырые оливки):
            # - Жира -- 15%.
            # - Прессование даёт -- 7%
            # - Экстракция даёт -- 12%
            # - Остаток -- 3%
        # Прессование и экстракция (выход 0.12).
        # Калибр оливок -- 300 штук/килограмм
        # Доля ядер (косточек) -- 20% плода?
        # Жмых и косточки на топливо.
        '_-Очистка оливок на сетчатом барабане (килограмм)':1 / 0.12 * 1.1,
        '_-Мытьё оливок в кадке с ситом и мешалкой (килограмм)':1 / 0.12,
        '_-Дробление оливок на вальцовой молотилке (килограмм)':1 / 0.12,
        '_-Отжим масла из мезги гидравлическим прессом, холодный (килограмм)':1 / 0.12,
        '_-Отжим масла из мезги гидравлическим прессом, горячий (килограмм)':1 / 0.12 * 0.97,
        '_-Отстаивание оливковой мезги для осаждения косточек (килограмм)':1 / 0.12 * 0.95,
        '_-Кипячение мезги на паровой сковороде (килограмм)':1 / 0.12 * 0.75,
        '_-Отжим масла из муки гидравлическим прессом (килограмм)':1 / 0.12 * 0.35,
        '_-Экстракция масла из мезги сернистым эфиром (килограмм)':1 / 0.12 * 0.35,
        '_-Отстаивание масла в чане (килограмм)':1.07,
        '_-Фильтрование масла паклей и опилками (килограмм)':1.04,
        '_-Рафинирование масла серной кислотой (килограмм)':1.02,
        'Оливки (килограмм)':1 / 0.12,
        '+Косточки оливковые (доступно/килограмм)':1 / 0.12 * (0.95 - 0.75),
        '+Жмых оливковый (доступно/килограмм)':1 / 0.12 * (0.35 - 0.07),
        '_Маслоэкстракционный завод (годовой оборот)':1 / 500000,
        }

metadict_detail['_Производство арахисового масла (килограмм)'] = {
        # Доступно масла:
            # - Жира -- 41.2%.
            # - Прессование даёт -- 30%
            # - Экстракция даёт -- 39%
            # - Остаток -- 2.2%
        # Прессование и экстракция (выход 0.39).
        # http://www.bestoilmillplant.com/peanut-oil-production.html
        # Массовая доля шелухи: от 15 до 47% (30%)
        '_-Очистка бобов на сетчатом барабане (килограмм)':1 / 0.39,
        '_-Лущение бобов на вальцовой молотилке (килограмм)':1 / 0.39 * 0.95,
        '_-Помол бобов на вальцовой мельнице (килограмм)':1 / 0.39 * 0.65,
        '_-Подогревание муки на паровой сковороде (килограмм)':1 / 0.39 * 0.65,
        '_-Отжим масла из муки гидравлическим прессом (килограмм)':1 / 0.39 * 0.65,
        '_-Экстракция масла из муки сернистым эфиром (килограмм)':1 / 0.39 * 0.35,
        '_-Отстаивание масла в чане (килограмм)':1.07,
        '_-Фильтрование масла паклей и опилками (килограмм)':1.04,
        '_-Рафинирование масла серной кислотой (килограмм)':1.02,
        'Бобы арахиса в шелухе (килограмм)':1 / 0.39,
        '+Отруби арахисовые (доступно/килограмм)':1 / 0.39 * (0.95 - 0.65),
        '+Жмых арахисовый (доступно/килограмм)':1 / 0.39 * (0.65 - 0.35),
        '_Маслоэкстракционный завод (годовой оборот)':1 / 500000,
        }

metadict_detail['_Производство кунжутного масла (килограмм)'] = {
        # Доступно масла:
            # - Жира -- 37.0%.
            # - Прессование даёт -- 26%
            # - Экстракция даёт -- 34%
            # - Остаток -- 3%
        # Только прессование, без экстракции (выход 0.26).
        '_-Очистка семян на сетчатом барабане (килограмм)':1 / 0.26,
        '_-Лущение семян на вальцовой молотилке (килограмм)':1 / 0.26 * 0.95,
        '_-Помол семян на вальцовой мельнице (килограмм)':1 / 0.26 * 0.7,
        '_-Подогревание муки на паровой сковороде (килограмм)':1 / 0.26 * 0.7,
        '_-Отжим масла из муки гидравлическим прессом (килограмм)':1 / 0.26 * 0.7,
        '_-Отстаивание масла в чане (килограмм)':1.07,
        '_-Фильтрование масла паклей и опилками (килограмм)':1.04,
        '_-Рафинирование масла серной кислотой (килограмм)':1.02,
        'Семена кунжута (килограмм)':1 / 0.26,
        '+Отруби кунжутные (доступно/килограмм)':1 / 0.26 * (0.95 - 0.7),
        '+Жмых кунжутный (доступно/килограмм)':1 / 0.26 * (0.7 - 0.26),
        '_Маслобойный завод (годовой оборот)':1 / 300000,
        }

metadict_detail['_Производство какао-масла (килограмм)'] = {
        # Доступно масла:
            # - Жира -- 54.0%.
            # - Прессование даёт -- 37%
            # - Экстракция даёт -- 51%
            # - Остаток -- 3%
            # https://ru.wikisource.org/wiki/ЭСБЕ/Шоколад
            # https://helpiks.org/6-86678.html
        # Только прессование, без экстракции (выход 0.37).
        # Жмых -- какао порошок. Масло не рафинируют.
        # Какао-порошок содержит 17% жира
        '_-Очистка бобов на сетчатом барабане (килограмм)':1 / 0.37,
        '_-Сортировка бобов на сетчатом барабане (килограмм)':1 / 0.37,
        '_-Лущение бобов на вальцовой молотилке (килограмм)':1 / 0.37 * 0.95,
        '_-Обжаривание бобов на фабричном противене (килограмм)':1 / 0.37 * 0.55,
        '_-Помол бобов на вальцовой мельнице (килограмм)':1 / 0.37 * 0.55,
        '_-Отжим масла из муки гидравлическим прессом (килограмм)':1 / 0.37 * 0.55,
        '_-Отстаивание масла в чане (килограмм)':1.07,
        '_-Фильтрование масла паклей и опилками (килограмм)':1.04,
        'Какао-бобы сухие (килограмм)':1 / 0.37,
        'Бобы арахиса в шелухе (килограмм)':1 / 0.37,
        '+Отруби какао (доступно/килограмм)':1 / 0.37 * (0.95 - 0.55),
        '+Какао-порошок (доступно/килограмм)':1 / 0.37 * (0.55 - 0.37),
        '_Маслобойный завод (годовой оборот)':1 / 300000,
        }

metadict_detail['_Производство какао-порошка (килограмм)'] = {
        # Без прессования масла.
        '_-Очистка бобов на сетчатом барабане (килограмм)':1 / 0.43,
        '_-Сортировка бобов на сетчатом барабане (килограмм)':1 / 0.43,
        '_-Лущение бобов на вальцовой молотилке (килограмм)':1 / 0.43 * 0.95,
        '_-Обжаривание бобов на фабричном противене (килограмм)':1 / 0.43 * 0.55,
        '_-Помол бобов на вальцовой мельнице (килограмм)':1 / 0.43 * 0.55,
        '_-Отжим масла из муки гидравлическим прессом (килограмм)':1 / 0.43 * 0.55,
        '_-Отстаивание масла в чане (килограмм)':1.07,
        '_-Фильтрование масла паклей и опилками (килограмм)':1.04,
        'Какао-бобы сухие (килограмм)':1 / 0.43,
        'Бобы арахиса в шелухе (килограмм)':1 / 0.43,
        '+Отруби какао (доступно/килограмм)':1 / 0.43 * (0.95 - 0.55),
        '+Какао-порошок (доступно/килограмм)':1 / 0.43 * (0.55 - 0.43),
        '_Маслобойный завод (годовой оборот)':1 / 300000,
        }

#----
# Фабрики (ферментация)

metadict_detail['_Производство солода (килограмм)'] = {
        # 1 кг солода = 1.33 кг зерна ячменя
        # Замачивание -- 48-120 часов (смена воды каждые 12-24 часа)
        # Проращивание -- 7-10 дней (перелопачивание каждые 6-12 часов)
        # Высушивание -- 16-48 часов (перелопачивают каждый час)
            # Сушильни: 0.2 кг угля (6 МДж) на 1 кг солода
            # Испарение воды -- 0.6 кг на 1 кг солода.
        # https://ru.wikisource.org/wiki/ЭСБЕ/Пиво
        '_-Замачивание зерна фабричное (килограмм)':1,
        '_-Проращивание зерна фабричное (килограмм)':1.6,
        '_-Высушивание зерна фабричное (килограмм)':1.6,
        '_Производство солода (годовой оборот)':1 / 500000,
        }

metadict_detail['_Производство пива ячменного (килограмм)'] = {
        # TODO: допиливай производство пива.
        # Пивоварение в Германии (1890 год, 52.5 млн. населения)
            # Производство -- 5 250 млн. литров (100 литров/человека)
            # Производительность -- 47 300 - 119 000 литров-год/рабочего (0.03-0.06 нормо-часа/литр)
            # * Скорее всего это производительность на готовом солоде.
            # https://istmat.info/node/27395
        # Каталог 12-й осенней сельско-хозяйственной и промышленной выставки
        # Ростов на Дону сентябрь 1908 года
            # - пиво (опт, 35 раб) -- 0.4 руб/литр (0.45 нормо-часа)
            # Лубны, завод существует с 1888 года,
            # Бриных Франц Антонович, Чешский пивоваренный завод
            # Годовое производство -- 10 000 вёдер (123 000 литров)
            # Годовой оборот -- 50 000 рублей
            # Рабочих -- 35 человек,
            # * Скорее всего соложение делают сами. Без фабричного оборудования.
        # Понивилю (3700 жителей) требуется 1250 литров/день, 187 000 литров/год
        # У нас получается (работы пивоваров, без соложения) 0.092 часа/литр пива (16 пивоваров/городок)
        # Пропорции ингредиентов в food_cooking, здесь только процесс.
        '_-Затирание пивного сусла (килограмм)':1.5,
        '_-Кипячение пивного сусла в медном чане (килограмм)':1.5,
        '_-Охлаждение пивного сусла (килограмм)':1,
        '_-Брожение пивного сусла (килограмм)':1,
        '_-Послеброжение пивного сусла (килограмм)':1,
        '_Пивоваренный завод (годовой оборот)':1 / 200000,
        }

#----
# Фабрики (капитализация)

metadict_detail['_Мельница (годовой оборот)'] = {
        # TODO:
            # Пока что трудозатраты в техпроцессах.
            # Станки, землю, здание, аммортизацию производства -- всё в капитализацию
        # Оплата помола (начало 1809-1853 годы) -- 10-17% от стоимости зерна.
            # Лященко П.И. Русская мукомольная промышленность и торговля мукою
            # https://scepsis.net/library/id_1270.html
        #'Мельница (капитализация)':1/10,
        #'Фабричные рабочие':50,
        }

metadict_detail['_Производство солода (годовой оборот)'] = {
        #'Маслозавод (капитализация)':1/10,
        #'Фабричные рабочие':30,
        }

metadict_detail['_Маслоэкстракционный завод (годовой оборот)'] = {
        #'Маслозавод (капитализация)':1/10,
        #'Фабричные рабочие':65,
        }

metadict_detail['_Маслобойный завод (годовой оборот)'] = {
        #'Маслозавод (капитализация)':1/10,
        #'Фабричные рабочие':35,
        }

metadict_detail['_Крахмальный завод (годовой оборот)'] = {
        #'Крахмальный завод (капитализация)':1/10,
        #'Фабричные рабочие':30,
        }

metadict_detail['_Рафинадный завод (годовой оборот)'] = {
        #'Рафинадный завод (капитализация)':1/10,
        #'Фабричные рабочие':200,
        }

metadict_detail['_Сахарный завод (годовой оборот)'] = {
        #'Сахарный завод (капитализация)':1/10,
        #'Фабричные рабочие':300,
        }

metadict_detail['_Кондитерская фабрика (годовой оборот)'] = {
        #'Производство агар-агара (капитализация)':1/10,
        #'Фабричные рабочие':30,
        }

metadict_detail['_Солеварня (годовой оборот)'] = {
        # Соликамск 1742 года (sic!), "Путешествие в Сибирь" Гмелина:
            # https://uraloved.ru/starosti/gmelin-puteshestvie-v-sibir
        #'Производство поваренной соли (капитализация)':1/10,
        #'Фабричные рабочие':12,
        }

metadict_detail['_Пивоваренный завод (годовой оборот)'] = {
        #'Пивоварение завод (капитализация)':1/10,
        #'Фабричные рабочие':10,
        }

metadict_detail['_Молотилка (годовой оборот)'] = {
        #'Молотилка (капитализация)':1/10,
        #'Фабричные рабочие':12,
        }
