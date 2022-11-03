#----
# Заметки
    # Суэцкий канал (1859-1869 годы):
        # Предтеча: античный канал от Нила: ширина 8 по дну, 17 по поверхности, глубина 2 метра.
        # Длина: 160 км; ширина по поверхности 60-110 м; по дну 22 м (позже расширено до 37 м)
        # Глубина: 8 метров (впоследствии 9 метров)
        # Габариты: 1 / 2 * (22 + 80) * 8 * 1000 = 0.41 млн кубометров/километр (65.6 млн всего)
        # Объём работ: 75 млн. кубометров земли; 20-40 тысяч рабочих (1863 год)
        # Объём работ (зарплаты): оценочно 100 млн. рублей на рабочих за 10 лет.
        # Стоимость (1892 год): 576 млн франков (220 млн. рублей, 2.9 рубля/кубометр работ)
        # Оборот (1895 год): 3341 судов, 7 659 000 тонн груза (10 франков/тонн, 3.8 руб/тонна)
        # Доход (1895 год): 80.7 млн франков, 25 млн расходы, 55.7 млн чистыми.
    # Никарагуанский канал (не был построен):
        # Длина: 271 км (64 км прорыть) по дну 24-36 метров, по поверхности 56-87 метров.
        # Глубина 8.5 метров. 3 шлюза 200x25 метров,
        # Стоимость: 100 млн. долларов (200 млн. рублей)
        # https://ru.wikisource.org/wiki/ЭСБЕ/Никарагуанский_канал
        # https://ru.wikipedia.org/wiki/Файл:Nicaragua_canal_proposals_-_ru.svg
    # Панамский канал:
        # Длина: 82 км; по дну 33 метра, глубина 12 метров (???)
        # Объём работ: 150 млн. кубометров, 70 000 рабочих (1904-1913 годы)
            # Длина: 160 км; ширина по поверхности 60-110 м; по дну 22 м (позже расширено до 37 м)
            # Выемка и вывоз грунта -- 0.27 копеек/кубометр
            # Выемка грунта экскаватором -- до 0.24 млн м³/день на 100 машин
            # Землесосы в устье канала -- 2 машины, по 1000 и 1500 кубометров/час
            # Вывоз грунта -- 50 паровозов, 650 вагонов-самосвалов, железная дорога
            # Взрывные работы (перевал Кулебра) -- 200 пневматических буровых машин, 7 атмосфер, воздухопровод
        # Стоимость (1910 год) -- 1120 млн. руб (400 млн США)
        # https://ru.wikisource.org/wiki/ВЭ/ВТ/Земляные_работы
        # https://ru.wikisource.org/wiki/ЭСБЕ/Панамский_канал
        # https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Panama_Canal_Map-ru.svg/991px-Panama_Canal_Map-ru.svg.png
    # Мариинский канал (Тифлис): длина 20 км,
        # Размеры 2x15 метров, один шлюз,
        # Стоимость: 0.8 млн рублей
    # Бриджватерский канал: длина 150 км,
        # 91 шлюз (169 метров подъёма),
        # 126 мостов и водопроводов, 6 туннелей.
        # https://ru.wikisource.org/wiki/ЭСБЕ/Бриджватерский_канал

#----
# Реки Эквестрии (по площади страны):
    # Реки России (всего 12.4 млн. км):
        # Диапазон длин | Длина общая  | Процент | Рек     | Длина средняя
        # ------------- | ------------ | ------- | ------- | -------------
        # >500 км       | -            | -       |  214    | -
        # 101-500       | -            | -       | 2833    | -
        #  10-100       | 2 843 046    | 23      | 134 тыс | 21 км
        # <10 км        | 5 118 642    | 41      | 2.6 млн | 2 км
        # https://ru.wikipedia.org/wiki/Воды_России
    # Расчёт осадков в регионе по водостоку:
        # Волжский бассейн (средние осадки 662 мм/год, испарение 475 мм/год, сток 187 мм/год)
        # Волга (3500 км, 254 км³/год, бассейн 1 360 000 км², сток по осадкам 187 мм/год)
        # Формула:
        # 1 360 000 км² × (x / 10^6) = 254 км³/год; x = 187 мм/год
        # Реальные осадки: 187 / 0.28 = 668 мм/год
        # Формула (с коэффициентом испарения):
        # 1 360 000 км² × (x * 0.28 / 10^6) = 254 км³/год; x = 667
    # Расчёт бассейна реки по осадкам и водостоку:
        # Формула: y × (667 * 0.28 / 10^6) = 254 км³/год; y = 1 360 000 км²
    # Испарение воды за лето (7 месяцев):
        # Бавария:
        # - В поле            -- 377 мм (100%)
        # - в лесу            -- 158 мм (42%)
        # - под палой листвой -- 62 мм (16%)
        # https://ru.wikisource.org/wiki/ЭСБЕ/Испарение
    # Коэффициенты испарения:
        # Западная Европа    -- 0.3-0.33
        # Огайо              -- 0.24
        # Миссури            -- 0.15
        # Верхней Миссисипи  -- 0.24
        # Арканзаса и Вайта  -- 0.15
        # Ред-Ривер          -- 0.20
        # Язу и С.Френсиса   -- 0.90 (влажные леса?)
        # Москва-река        -- 0.40 (0.72 снег, 0.19 дождь)
        # Волга выше Сызрани -- 0.44 (не совпадает)
        # https://ru.wikisource.org/wiki/ЭСБЕ/Реки

metadict_detail['|----Суша Эквестрии (квадратный километр)'] = {
        # Площадь рек Земли (без озёр) -- 773 тысячи км² (0.52% суши)
            # Длина рек России -- 12.4 млн км (0.72 км/км² страны)
                # Площадь озёр, рек и болот России -- 2 123 523 км² (12.4% площади страны)
                # Площадь озёр России -- 408 856 км² (2.4% площади страны)
                # Площадь поверхности рек России (оценочно) -- >89 000 км²
                # Водосток -- 4258,6 км³ (343 435 м³/километр)
                # 248 674 м³/кв.км страны, 2500 м³/гектар, 250 мм/гектар
            # Длина рек США -- 5.633 млн км (0.59 км/км² страны)
                # Площадь озёр, рек и болот США -- 686 000 км² (7% площади страны)
                # Площадь рек и озёр США -- 218 500 км² (2.3% площади страны)
                # Площадь поверхности рек США (оценочно) -- 50 000 км²
        'Эквестрийские реки (километр)':0.6,
        'Эквестрийские озёра (квадратный километр)':0.023,
        'Эквестрийские болота (квадратный километр)':0.07,
        }

metadict_detail['Эквестрийские болота (квадратный километр)'] = {
        # Болота России (9% страны) -- 1 750 000 кубометров/кв.километр болот (1750 мм воды на болотах)
        # Торфяные месторождения России (4.7% страны) -- среднее 12 км² на 26 кв.км болота, 46% болот
        # Запасы торфа -- 3.6 млн тонн/месторождение (0.3 млн тонн/км², 3000 тонн/гектар, +10-40 тонн/год)
        '+Торфяники, 3000 тонн/гектар (доступно/гектар)':(12/26) * 100,
        '|--Болота (гектар)':100,
        '|----Водные пространства (гектар)':100,
        }

metadict_detail['Эквестрийские озёра (квадратный километр)'] = {
        '|--Озёра (гектар)':100,
        '|----Водные пространства (гектар)':100,
        }

metadict_detail['Эквестрийские реки (километр)'] = {
        # 0.6% суши, гектар водной глади на километр усреднённой реки.
        'Эквестрийские реки, большие (>500 км) (километр)':0.03,
        'Эквестрийские реки, средние (101-500 км) (километр)':0.11,
        'Эквестрийские реки, малые (10-100 км) (километр)':0.23,
        'Эквестрийские реки, ручьи (<10 км) (километр)':0.41,
        #'Эквестрийские реки, водосток (кубометр) (проверка)':350000,
        #'Эквестрийские реки, площадь (квадратный километр) (проверка)':0.01,
        }

metadict_detail['Эквестрийские реки, большие (>500 км) (километр)'] = {
        # TODO: Допиливай русла рек и уточни водостоки.
            # Водосток должен понижаться от меньших рек к большим. Испарение.
            # Посчитай испарение с поверхности воды, площадь же известна.
        # Бассейн Кантеры (при коэффициенте испарения 0.35):
            # Вычисление:
            # y × (500 * 0.35 / 10^6) = 200 км³/год; y = 1 430 000 км²
            # 500 мм/год осадки, 200 км³/год водосток, 32% лесов.
        # Ширина 100-500 метров (150 метров), длина средняя 700 км (???)
        # Поперечное сечение реки -- трапеция
        'Эквестрийские реки, большие (квадратный километр)':0.15,
        'Эквестрийские реки, большие, объём (кубометр)':1 / 2 * (50 + 150) * 5 * 1000,
        'Эквестрийские реки, большие, водосток (кубометр)':1 / 2 * (50 + 150) * 5 * 1000 * (3 *24*360 / 700),
        # Главные судоходные:
        'Река Кантер, всего (километр)':0.4,
        'Река Филли, всего (километр)':0.13,
        'Река Мэйнхен, всего (километр)':0.11,
        'Река Шайен, всего (километр)':0.09,
        # Реки поменьше:
        'Река Пайвиль, всего (километр)':0.11,
        'Река Энфильд, всего (километр)':0.08,
        'Река Горхон, всего (километр)':0.08,
        }

metadict_detail['Эквестрийские реки, средние (101-500 км) (километр)'] = {
        # Ширина 30-100 метров (30 метров), длина средняя 200 км (???)
        'Эквестрийские реки, средние (квадратный километр)':0.03,
        'Эквестрийские реки, средние, объём (кубометр)':1 / 2 * (10 + 30) * 2 * 1000,
        'Эквестрийские реки, средние, водосток (кубометр)':1 / 2 * (10 + 30) * 2 * 1000 * (2 *24*360 / 200),
        }

metadict_detail['Эквестрийские реки, малые (10-100 км) (километр)'] = {
        # Ширина 5-30 метров (10 метров), длиня средняя 21 км
        'Эквестрийские реки, малые (квадратный километр)':0.01,
        'Эквестрийские реки, малые, объём (кубометр)':1 / 2 * (3 + 10) * 0.4 * 1000,
        'Эквестрийские реки, малые, водосток (кубометр)':1 / 2 * (3 + 10) * 0.4 * 1000 * (1.5 *24*360 / 21),
        }

metadict_detail['Эквестрийские реки, ручьи (<10 км) (километр)'] = {
        # Ширина <5 метров (2 метра), длина средняя 2 км
        # Водосборы ручьёв от 0.27 кв. километра до 21.2 кв.километра.
            # Осадки 561 мм/год (июнь-ноябрь 50-100 мм, зимой 10-30 мм):
            # Исследования по Магаданской области (7 ручьёв):
            # http://naperekate.narod.ru/nachireki02.html
        'Эквестрийские реки, ручьи (квадратный километр)':0.003,
        'Эквестрийские реки, ручьи, объём (кубометр)':1 / 2 * (0.5 + 2) * 0.15 * 1000,
        'Эквестрийские реки, ручьи, водосток (кубометр)':1 / 2 * (0.5 + 2) * 0.15 * 1000 * (1.5 *24*360 / 2),
        }

#----
# Реки Эквестрии (суммируем параметры):

metadict_detail['Эквестрийские реки, большие (квадратный километр)'] = {
        'Эквестрийские реки (квадратный километр)':1,
        }

metadict_detail['Эквестрийские реки, средние (квадратный километр)'] = {
        'Эквестрийские реки (квадратный километр)':1,
        }

metadict_detail['Эквестрийские реки, малые (квадратный километр)'] = {
        'Эквестрийские реки (квадратный километр)':1,
        }

metadict_detail['Эквестрийские реки, ручьи (квадратный километр)'] = {
        'Эквестрийские реки (квадратный километр)':1,
        }

metadict_detail['Эквестрийские реки, большие, объём (кубометр)'] = {
        'Эквестрийские реки, объём (кубометр)':1,
        }

metadict_detail['Эквестрийские реки, средние, объём (кубометр)'] = {
        'Эквестрийские реки, объём (кубометр)':1,
        }

metadict_detail['Эквестрийские реки, малые, объём (кубометр)'] = {
        'Эквестрийские реки, объём (кубометр)':1,
        }

metadict_detail['Эквестрийские реки, ручьи, объём (кубометр)'] = {
        'Эквестрийские реки, объём (кубометр)':1,
        }

metadict_detail['Эквестрийские реки, большие, водосток (кубометр)'] = {
        'Эквестрийские реки, водосток (кубометр)':1,
        }

metadict_detail['Эквестрийские реки, средние, водосток (кубометр)'] = {
        'Эквестрийские реки, водосток (кубометр)':1,
        }

metadict_detail['Эквестрийские реки, малые, водосток (кубометр)'] = {
        'Эквестрийские реки, водосток (кубометр)':1,
        }

metadict_detail['Эквестрийские реки, ручьи, водосток (кубометр)'] = {
        'Эквестрийские реки, водосток (кубометр)':1,
        }

#----
# Реки Эквестрии (суммируем параметры):

metadict_detail['Эквестрийские реки (квадратный километр)'] = {
        # TODO: здесь можно уточнить испарение вод.
            # Северная Двина -- 320-360 мм
            # Западная Двина -- 350-430 мм
            # https://waterjournal.ru/files/wj/1572331122.pdf
        '|--Реки (гектар)':100,
        '|----Водные пространства (гектар)':100,
        }

metadict_detail['Эквестрийские реки, водосток (кубометр)'] = {
        # TODO: Пили гидроэлектростанции. Нужно только знать перепады высот.
        }

metadict_detail['Эквестрийские реки, объём (кубометр)'] = {
        # TODO: добавь озёра, и будет объём водохранилищ + регулирующие мощности.
        }

#----
# Реки и каналы Эквестрии (судоходные):

metadict_detail['Потребность в водных путях (метр)'] = {
        'Судоходные реки и каналы (километр)':1 / 1000,
        }

metadict_detail['Судоходные реки и каналы (километр)'] = {
        # Судоходные реки Франции (1894) -- 7476 км, 14 метров/кв.километр (0.2 метра/человека)
        # Судоходные каналы Франции (1894) -- 4777 км, 9 метров/кв.километр  (0.12 метра/человека)
        'Эквестрийские реки, судоходные (километр)':0.7,
        'Эквестрийские каналы, судоходные (километр)':0.3,
        }

metadict_detail['Эквестрийские реки, судоходные (километр)'] = {
        # Судоходные реки Эквестрии:
            # Река Кантер с притоками -- 3128 км
            # Река Филли с притоком -- 983 км
            # Река Мэйнхен -- 823 км
            # Река Шайен -- 677 км
        # Верховье реки Кантер:
            # Кантерлотский регион.
            # Клаудсдэйл, Кантерлот, Хуффингтон, 10 речных округов:
            # (по радиусу речных округов, 0.7 изгибы)
            # (47 + 43 + 52 + 40 * 10) * 2 / 0.7 = 1548 км
        # Низовье реки Кантер:
            # Филлидельфийский регион
            # Троттингем, 5 речных округов
            # (55 + 42 * 5) * 2 / 0.7 = 757 км
        # Устье реки Кантер:
            # Балтимэрский регион
            # Балтимэр, 5 речных округов
            # (73 + 43 * 5) * 2 / 0.7 = 823 км
        # Бассейн реки Филли:
            # Филлидельфийский регион
            # Филлидельфия, Камильхиль, Мэрэй, 5 речных округов
            # (63 + 29 + 42 + 42 * 5) * 2 / 0.7 = 983 км
        # Бассейн реки Мэйнхен
            # Мэйнхеттенский регион
            # Мэйнхеттен, Сталлионград, Нэйгара Фолс, 4 речных округа
            # (76 + 42 + 34 + 34 * 4) * 2 / 0.7 = 823 км
        # Бассейн реки Шайен
            # Ванхуверский регион
            # Ванхувер, Инхарнэс, Шайен, 2 речных округа
            # (45 + 34 + 26 + 33 * 4) * 2 / 0.7 = 677 км
        # Главные реки:
        'Река Кантер, судоходная (километр)':0.4,
        'Река Филли, судоходная (километр)':0.13,
        'Река Мэйнхен, судоходная (километр)':0.11,
        'Река Шайен, судоходная (километр)':0.09,
        # Реки поменьше:
        'Река Пайвиль, судоходная (километр)':0.11,
        'Река Энфильд, судоходная (километр)':0.08,
        'Река Горхон, судоходная (километр)':0.08,
        }

metadict_detail['Эквестрийские каналы, судоходные (километр)'] = {
        # Связывают окружные города и понивили.
        'Река Кантер, судоходные каналы (километр)':0.4 + 0.11,
        'Река Филли, судоходные каналы (километр)':0.13 + 0.08,
        'Река Мэйнхен, судоходные каналы (километр)':0.13 + 0.04,
        'Река Шайен, судоходные каналы (километр)':0.13 + 0.04,
        }

#----
# Реки Эквестрии:

metadict_detail['Река Кантер, судоходная (километр)'] = {
        # TODO: Реки и каналы нуждаются в оборудовании. Знаках, ночном освещении, углублении русла.
        # Обеспечение судоходной реки (Волга, 1890 год, от Рыбинска до устья, 2200 км?)
            # - Предостерегающие знаки -- 2790 (освещённые ночью, это важно!)
            # - Помещения при постах -- 552 (605 гребных судов, 1589 человек)
            # - Речная полиция, Рыбинск (4 пожарных парохода) -- 100 000 рублей
            # - углубление реки Волга, участок Тверь-Рыбинск, 20 мелей (1864-1872 годы) -- 1.1 млн рублей
            # - устройство гавани Рыбинска на 20 пароходов, 40 больших барж, 60 мелких судов -- 0.5 млн рублей
        # Современная классификация рек (грузооборот в тонно-километрах):
            # сверхмагистрали (глубина 3.2 метра) -- 500 000 - 16 000 000 ткм/километр,
            # магистрали (глубина 2.5-3.2 метра) -- 150 000 - 2 500 000 ткм/километр,
            # местного значения 5 класс (1.1-1.5) -- 50 000 - 500 000 ткм/километр,
            # местного значения 7 класса (<0.7 м) -- <100 000 ткм/километр,
            # https://ru.wikipedia.org/wiki/Классификация_российских_внутренних_водных_путей
            # https://ru.wikipedia.org/wiki/Классификация_европейских_внутренних_водных_путей
        # Пропускная способность реки:
            # Баржи 400 тонн (200 тонн груза) -- с полной нагрузкой только для магистралей.
            # Пениши (длина 32 м; ширина 4.9 м; осадка 0.35-2.15 м; груз до 250 тонн)
            # Скорость 2.3 узла (4.3 км/час), динамический габарит x10 длины (300 метров):
            # (1000 / 300) * 4.3 = 14 барж/час (168-336 барж/сутки, 6 720 000 ткм/километр в год)
        '+Грузооборот реки Кантер (доступно/тонно-километров)':(14 * 200) * 12 * 200,
        }

metadict_detail['Река Мэйнхен, судоходная (километр)'] = {
        '+Грузооборот реки Мэйнхен (доступно/тонно-километров)':(14 * 200) * 12 * 200,
        }

metadict_detail['Река Филли, судоходная (километр)'] = {
        '+Грузооборот реки Филли (доступно/тонно-километров)':(14 * 200) * 12 * 200,
        }

metadict_detail['Река Шайен, судоходная (километр)'] = {
        '+Грузооборот реки Шайен (доступно/тонно-километров)':(14 * 200) * 12 * 200,
        }

metadict_detail['Река Пайвиль, судоходная (километр)'] = {
        # Меньшие реки в диколесье, почти не обслуживаются.
        # - расчистка и регулировка мелких речек для сплава дров (в ценах 1913 года) -- 50-70 руб/верста
        '+Грузооборот реки Пайвиль (доступно/тонно-километров)':(4 * 200) * 6 * 200,
        }

metadict_detail['Река Горхон, судоходная (километр)'] = {
        '+Грузооборот реки Горхон (доступно/тонно-километров)':(4 * 200) * 6 * 200,
        }

metadict_detail['Река Энфильд, судоходная (километр)'] = {
        '+Грузооборот реки Энфильд (доступно/тонно-километров)':(4 * 200) * 6 * 200,
        }

#----
# Реки Эквестрии:

metadict_detail['Река Кантер, судоходные каналы (километр)'] = {
        # По земляным работам:
            # Каналы для речных барж: 1 / 2 * (5 + 18) * 2.2 * 1000 = 25 300 кубометров/километр
            # Суэцкий канал для барков: 1 / 2 * (22 + 80) * 8 * 1000 = 410 000 кубометров/километр
        # Часть ирригация, часть судоходные.
        # Габариты шлюзов (40x5x2.2, 300-350-тонные баржи):
        # https://ru.wikipedia.org/wiki/Габарит_Фрейсине
        }

metadict_detail['Река Мэйнхен, судоходные каналы (километр)'] = {
        }

metadict_detail['Река Филли, судоходные каналы (километр)'] = {
        }

metadict_detail['Река Шайен, судоходные каналы (километр)'] = {
        }

#----
# Осушение болот:

metadict_detail['Участок торфяника под добычу (гектар)'] = {
        # Плотность сухого торфа -- 150-250 кг/кубометр
            # 1 кубометр сухого торфа = 3.5 кубометра просушенного болота.
            # 1 кубометр сухого торфа = 5 кубометров торфяного слоя.
        # Отвод воды канавой -- 5-40 рублей/десятина (торфянник оседает до 66-75% объёма)
            # Это 8-70 трудодней землекопа, от 25-220 до 77-670 кубометров грунта
            # Буровые скважины, когда под водоносным слоем есть сухой слой песка/гравия.
        # Плинтовка болота (2-3 раза) -- 30-60 рублей/десятина, до 140 человек/десятина
            # Удаление пней, коряг, верхнего слоя мха, засыпание впадин.
            # https://ru.wikisource.org/wiki/ЭСБЕ/Угли_бурые_и_их_переработка
            # https://ru.wikisource.org/wiki/ЭСБЕ/Торфяная_культура
            # https://ru.wikisource.org/wiki/ЭСБЕ/Болота
        'Участок торфяника под добычу (эксплуатация) (гектар)':1,
        'Участок торфяника под добычу (строительство) (гектар)':1 / 20,
        }

metadict_detail['Участок торфяника под добычу (эксплуатация) (гектар)'] = {
        # Сезонные работы на участке торфяника.
        # Вспашка не требуется, у нас работают скреперы.
        # Торф начинают вынимать вдоль канавы, постепенно расширяя область добычи.
        '-Торфяники, эксплуатируется за сезон (требуется/гектар)':1,
        }

metadict_detail['Участок торфяника под добычу (строительство) (гектар)'] = {
        # Помни, управляемая погода:
            # Пегасы могут осушить болото, просто не пуская дожди.
            # Но без дренирования всё равно просыхать будет вечность.
        # 1) Участок ограждается насыпью и осушается постепенно наращиваемым по глубине каналом.
        # 2) Когда болото просохнет строится 100 метров грунтовой дороги.
        # 3) Вырубается лес, убираются корни и коряги (плинтовка болота).
        'Строительство грунтовой дороги (километр)':1 / 10,
        '_-Насыпь (кубометр)':(1/2 * (1 + 4) * 3) * 100,
        '_-Траншея (кубометр)':(1/2 * (1 + 4) * 3) * 100,
        '_-Расчистка среднего леса киркомотыгами (квадратный метр)':(100 * 100) * 0.5,
        '-Торфяники, истощается за сезон (требуется/гектар)':1,
        }
