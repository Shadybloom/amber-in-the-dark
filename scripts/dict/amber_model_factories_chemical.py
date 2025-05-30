#----
# Заметки:
    # https://ru.wikisource.org/wiki/ЭСБЕ/Свечи_и_производство_их
    # https://ru.wikisource.org/wiki/ЭСБЕ/Сало,_производство
    # https://ru.wikisource.org/wiki/ЭСБЕ/Стеарин
    # https://ru.wikisource.org/wiki/ЭСБЕ/Парафин
    # https://ru.wikisource.org/wiki/ЭСБЕ/Рейхенбах,_Карл

#----
# Производства (промышленные товары)

metadict_detail['_Производство дёгтя (килограмм)'] = {
        # У нас получается дорогой дёготь (225 бит/тонна).
            # Смоляк -- 69 бит (30%)
            # Дрова -- 36 бит (16%)
        # Реальные цены:
            # Дёготь -- 98|122 рублей/тонна
            # Уголь древесный -- 122|152.5 рублей/тонна (sic!)
            # Кокс крупный -- 18.3|24.4 рублей/тонна
            # Кокс мелкий -- 9.15|17.08 рублей/тонна
        # Минские реторты емкостью 20 м³ (цикл 99-111 часов)
            # Кубометр смоляка (1000 кг) -- 20 кг скипидара, 47 кг дёгтя, 80 кг угля.
            # Кубометр смоляка -- 0.6 кубометра дров на нагрев реторты.
            # "ПОДСОЧКА ЛЕСА" Н. П. Ковбаса
        # Минские реторты емкостью 8 м³ (цикл 56 часов)
            # Аппарат производит 330 литров смолы из 8 кубометров смоляка
            # Основной продукт: 1 кг дёгтя = 24 кг смоляка (4.2%)
            # Побочный продукт: 0.4 кг скипидара на 1 кг дёгтя
            # https://eduherald.ru/ru/article/view?id=18925
            # http://www.findpatent.ru/patent/257/2578695.html
            # https://ru.wikisource.org/wiki/ЭСБЕ/Вар
            # https://ru.wikisource.org/wiki/ЭСБЕ/Терпентин,_вещество
            # http://www.sewboat.narod.ru/shnjaka/tar.htm
        # От массы сухого сырья 50-55% жидких продуктов (смольница):
            # - растворимые смолы..... 4.5-14% (~3.5% скипидар)
            # - уксусная кислота...... 4-7%
            # - метанол............... 1-2%
            # - прочие соединения..... 5-6%
            # - вода.................. 67-81% (8 кг воды на 24 кг сырья)
            # Испарение 8 кг воды в печи, это 31 МДж (2 кг дров)
        # Требуется 8 кг дров для нагрева реторты (120 МДж)
        '_-Переработка смоляка на дёготь (килограмм)':24,
        'Смоляк (килограмм)':24,
        '+Уголь древесный (доступно/килограмм)':1.7,
        '+Уксусная кислота, древесная (доступно/килограмм)':0.5,
        '+Скипидар (доступно/килограмм)':0.4,
        '+Метанол (доступно/килограмм)':0.2,
        '_Смолокурня (годовой оборот)':1 / 50000,
        }

metadict_detail['_Производство древесного угля (килограмм)'] = {
        # Выход угля 20% -- 5 кг дров на 1 кг угля.
        # Сухая перегонка в ретортах (выход по весу):
            # Древесина | Дёготь | Уголь  | Древесная кислота
            # --------- | ------ | ------ | -----------------
            # ель       | 13.66% | 21.65% | 41.4%
            # сосна     | 11.91% | 21.65% | 42.37%
            # берёза    | 8.59%  | 24.41% | 44.90%
            # https://ru.wikisource.org/wiki/ЭСБЕ/Уголь_древесный
            # https://ru.wikisource.org/wiki/ЭСБЕ/Древесно-уксусная_кислота_и_древесный_спирт
            # https://ru.wikisource.org/wiki/ЭСБЕ/Дерево,_материал
            # https://web.archive.org/web/20240616000427/https://bigenc.ru/c/piroliz-drevesiny-db4847
        # Требуется +1.6 кг дров для нагрева реторты
        '_-Переработка древесины на уголь (килограмм)':5,
        'Дрова для промышленности (килограмм)':5,
        '+Дёготь побочный (доступно/килограмм)':0.2,
        '+Уксусная кислота, древесная (доступно/килограмм)':0.1,
        '+Скипидар (доступно/килограмм)':0.08,
        '+Метанол (доступно/килограмм)':0.04,
        '_Смолокурня (годовой оборот)':1 / 250000,
        }

metadict_detail['_Производство кокса торфяного (килограмм)'] = {
        # TODO: побочные продукты коксохимии
            # CO -- газ, топливо
            # сульфат аммония -- удобрения
            # битум, бензол, толуол -- нефтехимия
            # карболовая кислота -- дезинсекция жилища
            # Коксохимические печи в Европе в 1881 году, в США – в 1895-м
            # "Энергия и цивилизация" Вацлав Смил
            # https://ru.wikisource.org/wiki/ЭСБЕ/Фенол
        # Выход угля 20% -- 5 кг дров на 1 кг угля.
        # Требуется +1.6 кг дров для нагрева реторты (нагревают газом)
        '_-Коксование торфа (килограмм)':5,
        'Торф для промышленности (килограмм)':5,
        '+Битум торфяной (доступно/килограмм)':0.25,
        '_Смолокурня (годовой оборот)':1 / 250000,
        }

metadict_detail['_Производство канифоли (килограмм)'] = {
        # В живице 7-10% сора (50% живицы с <7% сора)
        # Обработка:
            # Очищение:
            # - Расплавление в 1500-литровых котлах (4-5 часов до 85-90°C)
            # - Процеживание через трубу с металлической сеткой
            # Перегонка:
            # - Перегонка в 300-литровых котлах паром в 3 атмосферы (135°C)
            # - за 8 часов испаряется эфирное масло и вода
            # - канифоль фильтруют через сетчатые барабаны
            # Выход скипидара 16-18%
            # "ПОДСОЧКА ЛЕСА" Н. П. Ковбаса
            # https://ru.wikisource.org/wiki/ЭСБЕ/Живица_и_ее_переработка
            # https://patents.google.com/patent/RU2543163C2/ru
        # Тесты:
            # amber -sm "Канифоль (килограмм)" -n 1000 -S -E "нормо-час"
            # amber -sm "Канифоль (килограмм)" -n 100000 -S -E "@"
            # amber -sm "Канифоль (килограмм)" -n 100000 -S -E "||"
        # Смола сосновая -- 366|458 рублей/тонна
        # Скипидар французский -- 299|372 рублей/тонна
        # Канифоль -- 256|323 рублей/тонна
        '_-Дробление живицы на вальцовой мельнице (килограмм)':1.2 / 0.93,
        '_-Расплавление и процеживание живицы (килограмм)':1.2 / 0.93,
        '_-Перегонка живицы в чане паром (килограмм)':1.2,
        'Живица (килограмм)':1.2 / 0.93,
        '+Скипидар (доступно/килограмм)':0.15,
        '_Смоловарня (годовой оборот)':1 / 500000,
        }

metadict_detail['_Производство канифольного масла (килограмм)'] = {
        # Канифольное масло: перегонка канифоли в котле при 160-200°C до 345°C (75% выход)
        # с 5%-ным хлористым цинком в качестве катализатора при 120-200°C с выходом 75%
            # Продукт перегонки     | Массовая доля
            # --------------------- | -------------
            # Газы (метан)          | 9.0
            # Уксусная кислота      | 3.5
            # Пинолин               | 3.5
            # Мутное желтое масло   | 5.0
            # Светлое желтое масло  | 58.0
            # Синее масло           | 14.0
            # Вар                   | 6.0
            # Потери                | 1.0
            # https://msd.com.ua/kanifol/kanifolnoe-maslo-abieten-i-abietin/
            # https://bibliotekar.ru/4-1-34-smola-skipidar/51.htm
        # Метан 0,72 кг/м³, 39,8 МДж/м³, 90 грамм метана = 5 МДж
        '_-Перегонка канифоли в чане паром (килограмм)':1.35,
        'Канифоль (килограмм)':1.35,
        '+Дёготь побочный (доступно/килограмм)':0.06,
        '+Уксусная кислота, древесная (доступно/килограмм)':0.035,
        }

metadict_detail['_Производство смазки кальциевой канифольной (килограмм)'] = {
        # Колёсная мазь: канифольное масло + гашёная известь
        '_-Варка канифоли в чане паром (килограмм)':1,
        '_-Отстаивание канифольного масла (килограмм)':1,
        'Масло канифольное (килограмм)':0.85,
        'Гидроксид кальция (килограмм)':0.15,
        '_Смоловарня (годовой оборот)':1 / 500000,
        }

metadict_detail['_Производство канифольного клея (килограмм)'] = {
        # 96 кг канифоли + 2 кг гидроксида натрия + 2 кг крахмала (варка в котле 2 часа)
        # Сухие вещества 70%
        '_-Варка канифольного клея (килограмм)':1,
        '_-Отстаивание канифольного клея (килограмм)':1,
        'Канифоль (килограмм)':0.96,
        'Гидроксид натрия (килограмм)':0.02,
        'Крахмал (килограмм)':0.02,
        '_Смоловарня (годовой оборот)':1 / 500000,
        }

metadict_detail['_Производство хозяйственного мыла (килограмм)'] = {
        # Производят из арахисового и худшего оливкового масла.
            # Варят 10 дней при 121°C, обрабатывают щелочным раствором, отстаивают 2 дня.
            # Один рабочий в день может изготовить 100 кг. мыла (0.1 нормо-часа/кг).
                # - мыло для белья (опт, 4 раб) -- 0.24 руб/килограмм (0.016 нормо-часа/кг)
                # - мыло простое и туалетное (опт, 41 раб) -- 0.4 руб/килограмм (0.4 нормо-часа/кг)
                # Мыло каолиновое -- 171|214 рублей/тонна
                # Мыло простое -- 232|256 рублей/тонна
            # https://ru.m.wikipedia.org/wiki/Хозяйственное_мыло
            # https://ru.wikisource.org/wiki/ЭСБЕ/Мыло
            # https://istmat.org/node/27455
            # https://en.m.wikipedia.org/wiki/Saponification
        # Используется масло снятое, остающееся после фритюра:
            # Каолин (каолинит) для смягчения щёлочи.
            # Канифоль, чтобы защитить от прогоркания и повысить мягкость
            # Канифоль + едкий натр (или едкий калий) = канифольное мыло
            # мыло на основе натрия твёрдое, а на основе калия жидкое.
            # до 50% канифоли в хозяйственном мыле
            # до 10% канифоли в туалетном мыле
            # http://florant.ru/book/124/
        # Оливковое мыло Алеппо (мягкое и нежное):
            # 1) оливковое масло + сода из растения salsola kali.
            # 2) варят при температуре более 200°C с кипящей водой.
            # 3) после омыления масло распадается на глицерин и щелочь.
            # 4) каустическую соду и щелочь удаляют, промывая мыло.
            # 5) добавить лавровое масло.
            # 6) сушить 9 месяцев
            # http://www.popadancev.net/mylo/
        # Зелёное мыло Sapoviridis (противопаразитное):
            # Мыло зелёное -- 287|357 рублей/тонна
            # 100 частей льняного/конопляного масла
            # 22 частей твёрдого едкого калия
            # 6 частей поташа
        # Тонна мыла = 667 кг жиров (67%), 167 кг кальцированной соды, 83 кг извести, 70 кг соли.
        '_-Варка хозяйственного мыла (килограмм)':1,
        '_-Отстаивание хозяйственного мыла (килограмм)':1,
        '_-Формовка хозяйственного мыла (килограмм)':1,
        '-Масло снятое (требуется/килограмм)':0.42 * 0.5,
        'Масло арахисовое (килограмм)':0.42 * 0.5,
        'Канифоль (килограмм)':0.25,
        'Сода негашёная, карбонат натрия (килограмм)':0.17,
        'Известь негашёная (килограмм)':0.09,
        'Соль (килограмм)':0.07,
        '_Мыловарня (годовой оборот)':1 / 500000,
        }

#----
# Производства (капитализация)

metadict_detail['_Мыловарня (годовой оборот)'] = {
        #'Мыловарня (капитализация)':1/5,
        #'Наёмные рабочие (мыловары)':20,
        }

metadict_detail['_Смоловарня (годовой оборот)'] = {
        #'Смоловарня (капитализация)':1/5,
        #'Наёмные рабочие (смоловары)':12,
        }

metadict_detail['_Смолокурня (годовой оборот)'] = {
        #'Смолокурня (капитализация)':1/5,
        #'Наёмные рабочие (смолокуры)':12,
        }
