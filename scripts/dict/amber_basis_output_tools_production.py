#----
# Заметки
# Пользуйся регекспами, ёпт!
    # %s/        '_Производство \(.*\),/        '_Производство \1,\r        '_Утилизация \1,/gic
    # %s/_Утилизация \(.*\)':\(.*\),/_Утилизация \1':\2 * 0.5,/gic

#----
# Отделка зданий (обновление, ремонт):

metadict_detail['|||Кафель (квадратный метр)'] = {
        'Устройство кафельного покрытия (квадратный метр)':1,
        }

metadict_detail['|||Паркет (квадратный метр)'] = {
        'Устройство покрытий из паркетных досок (квадратный метр)':1,
        }

metadict_detail['|||Обои (квадратный метр)'] = {
        'Оклейка обоями (квадратный метр)':1,
        }

#----
# Текстильная промышленность (паруса):

metadict_detail['|||Инструмент текстильный (парус брезентовый) (квадратный метр)'] = {
        # TODO: проблема зацикливания скрипта. Перевозка парусов, которые используются для перевозки.
        #'_Производство утвари, парус 100x100 (брезент)':1,
        #'_Утилизация утвари, парус 100x100 (брезент)':1 * 0.75,
        '-Парус морской (требуется/квадратный метр)':1,
        }

#----
# Текстильная промышленность (ковры, шторы):

metadict_detail['|||Утварь текстильная (ковёр соломенный) (квадратный метр)'] = {
        '_Производство утвари, ковёр 100x100 (солома)':1,
        '_Утилизация утвари, ковёр 100x100 (солома)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (ковёр джутовый) (квадратный метр)'] = {
        '_Производство утвари, ковёр 100x100 (джут)':1,
        '_Утилизация утвари, ковёр 100x100 (джут)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (ковёр хлопчатый) (квадратный метр)'] = {
        '_Производство утвари, ковёр 100x100 (хлопок)':1,
        '_Утилизация утвари, ковёр 100x100 (хлопок)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (шторы оконные 100x100-см)'] = {
        '_Производство утвари, шторы 100x100 (хлопок)':1,
        '_Утилизация утвари, шторы 100x100 (хлопок)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (шторы водонепроницаемые 100x100-см)'] = {
        '_Производство утвари, шторы 100x100 (брезент)':1,
        '_Утилизация утвари, шторы 100x100 (брезент)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (полотенце 40x60 вафельное)'] = {
        '_Производство утвари, полотенце 40x60 вафельное (хлопок)':1,
        '_Утилизация утвари, полотенце 40x60 вафельное (хлопок)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (полотенце 50x90 вафельное)'] = {
        '_Производство утвари, полотенце 50x90 вафельное (хлопок)':1,
        '_Утилизация утвари, полотенце 50x90 вафельное (хлопок)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (полотенце 70x140 махровое)'] = {
        '_Производство утвари, полотенце 70x140 махровое (хлопок)':1,
        '_Утилизация утвари, полотенце 70x140 махровое (хлопок)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (скатерть 220x130)'] = {
        '_Производство утвари, скатерть 220x130 (хлопок)':1,
        '_Утилизация утвари, скатерть 220x130 (хлопок)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (холст 80x120)'] = {
        '_Производство утвари, холст 80x120 (лён)':1,
        '_Утилизация утвари, холст 80x120 (лён)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (мешочек)'] = {
        '_Производство утвари, мешочек (лён)':1,
        '_Утилизация утвари, мешочек (лён)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (сито)'] = {
        '_Производство утвари, сито (джут)':1,
        '_Утилизация утвари, сито (джут)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (решето)'] = {
        '_Производство утвари, решето (джут)':1,
        '_Утилизация утвари, решето (джут)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (мешок 100-литровый, 50x50x60)'] = {
        '_Производство утвари, мешок 100-литровый, 50x50x60 (джут)':1,
        '_Утилизация утвари, мешок 100-литровый, 50x50x60 (джут)':1 * 0.75,
        }

metadict_detail['|||Утварь текстильная (ветошь, 40x60-см)'] = {
        '_Производство утвари, ветошь (лоскуты)':1,
        '_Утилизация утвари, ветошь (лоскуты)':1 * 0.75,
        }

#----
# Текстильная промышленность (бельё, постели):

metadict_detail['|||Бельё, матрац стёганный (вата)'] = {
        # Старые постели идут на ветошь и лоскуты.
        '_Производство белья, матрац (вата)':1,
        '_Утилизация белья, матрац (вата)':1 * 0.75,
        }

metadict_detail['|||Бельё, одеяло лоскутное (вата)'] = {
        '_Производство белья, одеяло лоскутное (вата)':1,
        '_Утилизация белья, одеяло лоскутное (вата)':1 * 0.75,
        }

metadict_detail['|||Бельё, одеяло стёганное (вата)'] = {
        '_Производство белья, одеяло стёганное (вата)':1,
        '_Утилизация белья, одеяло стёганное (вата)':1 * 0.75,
        }

metadict_detail['|||Бельё, подушка стёганная (вата)'] = {
        '_Производство белья, подушка стёганная (вата)':1,
        '_Утилизация белья, подушка стёганная (вата)':1 * 0.75,
        }

metadict_detail['|||Бельё, простыня (парусина)'] = {
        '_Производство белья, простыня (парусина)':1,
        '_Утилизация белья, простыня (парусина)':1 * 0.75,
        }

metadict_detail['|||Бельё, простыня (хлопок)'] = {
        '_Производство белья, простыня (хлопок)':1,
        '_Утилизация белья, простыня (хлопок)':1 * 0.75,
        }

metadict_detail['|||Бельё, простыня махровая (хлопок)'] = {
        '_Производство белья, простыня махровая (хлопок)':1,
        '_Утилизация белья, простыня махровая (хлопок)':1 * 0.75,
        }

metadict_detail['|||Бельё, чехол тюфяка (мешковина)'] = {
        '_Производство белья, чехол тюфяка (мешковина)':1,
        '_Утилизация белья, чехол тюфяка (мешковина)':1 * 0.75,
        }

#----
# Текстильная промышленность (одежда):

metadict_detail['|||Одежда, бушлат (хлопок)'] = {
        # Только 50% одежды режут на лоскуты.
        '_Производство одежды, бушлат (хлопок)':1,
        '_Утилизация одежды, бушлат (хлопок)':1 * 0.5,
        }

metadict_detail['|||Одежда, ветровка (брезент)'] = {
        '_Производство одежды, ветровка (брезент)':1,
        '_Утилизация одежды, ветровка (брезент)':1 * 0.5,
        }

metadict_detail['|||Одежда, жакет (хлопок)'] = {
        '_Производство одежды, жакет (хлопок)':1,
        '_Утилизация одежды, жакет (хлопок)':1 * 0.5,
        }

metadict_detail['|||Одежда, жилет (хлопок)'] = {
        '_Производство одежды, жилет (хлопок)':1,
        '_Утилизация одежды, жилет (хлопок)':1 * 0.5,
        }

metadict_detail['|||Одежда, жилет (парусина)'] = {
        '_Производство одежды, жилет (парусина)':1,
        '_Утилизация одежды, жилет (парусина)':1 * 0.5,
        }

metadict_detail['|||Одежда, кафтан (хлопок)'] = {
        '_Производство одежды, кафтан (хлопок)':1,
        '_Утилизация одежды, кафтан (хлопок)':1 * 0.5,
        }

metadict_detail['|||Одежда, пальто (хлопок)'] = {
        '_Производство одежды, пальто (хлопок)':1,
        '_Утилизация одежды, пальто (хлопок)':1 * 0.5,
        }

metadict_detail['|||Одежда, пиджак (хлопок)'] = {
        '_Производство одежды, пиджак (хлопок)':1,
        '_Утилизация одежды, пиджак (хлопок)':1 * 0.5,
        }

metadict_detail['|||Одежда, платье (хлопок)'] = {
        '_Производство одежды, платье (хлопок)':1,
        '_Утилизация одежды, платье (хлопок)':1 * 0.5,
        }

metadict_detail['|||Одежда, плащ (брезент)'] = {
        '_Производство одежды, плащ (брезент)':1,
        '_Утилизация одежды, плащ (брезент)':1 * 0.5,
        }

metadict_detail['|||Одежда, плащ (хлопок)'] = {
        '_Производство одежды, плащ (хлопок)':1,
        '_Утилизация одежды, плащ (хлопок)':1 * 0.5,
        }

metadict_detail['|||Одежда, чепчик (хлопок)'] = {
        '_Производство одежды, чепчик (хлопок)':1,
        '_Утилизация одежды, чепчик (хлопок)':1 * 0.5,
        }

metadict_detail['|||Одежда, маска (хлопок)'] = {
        '_Производство одежды, маска (хлопок)':1,
        '_Утилизация одежды, маска (хлопок)':1 * 0.5,
        }

metadict_detail['|||Одежда, шапка (хлопок)'] = {
        '_Производство одежды, шапка (хлопок)':1,
        '_Утилизация одежды, шапка (хлопок)':1 * 0.5,
        }

metadict_detail['|||Одежда, шляпа (солома)'] = {
        '_Производство одежды, шляпа (солома)':1,
        '_Утилизация одежды, шляпа (солома)':1 * 0.5,
        }

metadict_detail['|||Одежда, шляпа (хлопок)'] = {
        '_Производство одежды, шляпа (хлопок)':1,
        '_Утилизация одежды, шляпа (хлопок)':1 * 0.5,
        }

metadict_detail['|||Одежда, чулки (хлопок)'] = {
        '_Производство одежды, чулки (хлопок)':1,
        '_Утилизация одежды, чулки (хлопок)':1 * 0.5,
        }

metadict_detail['|||Одежда, пояс страховой (джут)'] = {
        '_Производство одежды, пояс страховой (джут)':1,
        '_Утилизация одежды, пояс страховой (джут)':1 * 0.5,
        }

#----
# Текстильная промышленность (обувь):

metadict_detail['|||Обувь, ботинки (кирза)'] = {
        '_Производство обуви, ботинки (кирза)':1,
        '_Утилизация обуви, ботинки (кирза)':1 * 0.25,
        }

metadict_detail['|||Обувь, туфли (кирза)'] = {
        '_Производство обуви, туфли (кирза)':1,
        '_Утилизация обуви, туфли (кирза)':1 * 0.25,
        }

metadict_detail['|||Обувь, туфли (джут)'] = {
        '_Производство обуви, туфли (джут)':1,
        '_Утилизация обуви, туфли (джут)':1 * 0.25,
        }

metadict_detail['|||Обувь, галоши (резина)'] = {
        '_Производство обуви, галоши (резина)':1,
        '_Утилизация обуви, галоши (резина)':1 * 0.25,
        }

#----
# Бумажная промышленность (печать):

metadict_detail['|||Продукция печатная (книга)'] = {
        '_Производство книг (штук)':1,
        #'+Бумага газетная старая (доступно/квадратный метр)':4,
        '+Книги библиотечные (доступно/штук)':1,
        '|=Книги (килограмм)':0.5,
        }

metadict_detail['|||Продукция печатная (учебник)'] = {
        # Вес 130 листов бумаги + вес картона переплёта
        '_Производство книг (штук)':1,
        #'+Бумага газетная старая (доступно/квадратный метр)':4,
        '|=Книги (килограмм)':0.5,
        }

metadict_detail['|||Продукция печатная (газета)'] = {
        '_Производство газет (штук)':1,
        '+Бумага газетная старая (доступно/квадратный метр)':0.75,
        '+Газеты библиотечные (доступно/штук)':1,
        '|=Газеты (килограмм)':0.04,
        }

metadict_detail['|||Продукция печатная (журнал)'] = {
        '_Производство журналов (штук)':1,
        '+Бумага газетная старая (доступно/квадратный метр)':1.5,
        '+Журналы библиотечные (доступно/штук)':1,
        '|=Журналы (килограмм)':0.21,
        }

metadict_detail['|||Продукция печатная (тетрадь)'] = {
        # Для старших школьников и студентов. Жеребята учатся на грифельных досках.
        '_Производство тетрадей (штук)':1,
        #'+Бумага газетная старая (доступно/квадратный метр)':1.6,
        '|=Тетради (килограмм)':0.21,
        }

metadict_detail['|||Письмо (конверт и почтовая марка)'] = {
        # Лист А4 -- 0.0625 кв.метра, 5 грамм (80 грамм/кв.метр)
        # Среднее письмо -- 20 грамм (лист, конверт, марка)
        '|=Письма (килограмм)':0.02,
        }

metadict_detail['|||Посылка (почтовая бандероль)'] = {
        # TODO: Картонные коробки, это тара для писем. Их учитываем в goods.
            # Тара не только картонная. Также плетёная, берестяная, жестяная.
            # Пони используют коробки для посылок по несколько раз.
        # Объёмный вес 200 кг/кубометр. Средний вес посылки -- 0.7 кг.
            # Это коробка 260×170×80 мм (0.2 кв.метра картона, считая крышку)
            # Типичные посылки, в порядке уменьшения доли:
                # посуда, одежда, инструменты, книги, игрушки, сувениры,
                # лекарства, мыло, семена, пряности, сладкое, чай и кофе.
            # https://ru.wikipedia.org/wiki/Объёмный_вес_отправления
        '|=Посылки (килограмм)':0.7,
        }

metadict_detail['|||Продукция печатная (конверт)'] = {
        '_Производство почтовых конвертов (штук)':1,
        }

metadict_detail['|||Продукция печатная (почтовая бандероль)'] = {
        '_Производство почтовых бандеролей (штук)':1,
        }

metadict_detail['|||Продукция печатная (почтовая марка)'] = {
        '_Производство почтовых марок (штук)':1,
        }

#----
# Производство канцелярских товаров:

metadict_detail['|||Инструмент канцелярский (грифель)'] = {
        }

metadict_detail['|||Инструмент канцелярский (грифельная доска)'] = {
        }

metadict_detail['|||Инструмент канцелярский (ластик)'] = {
        }

metadict_detail['|||Инструмент канцелярский (ручка перьевая)'] = {
        }

#----
# Производство измерительных приборов:

metadict_detail['|||Инструмент измерительный (линейка)'] = {
        }

metadict_detail['|||Инструмент измерительный (отвес)'] = {
        }

metadict_detail['|||Инструмент измерительный (рейка)'] = {
        }

metadict_detail['|||Инструмент измерительный (рулетка)'] = {
        }

metadict_detail['|||Инструмент измерительный (угольник)'] = {
        }

metadict_detail['|||Инструмент измерительный (уровень)'] = {
        }

metadict_detail['|||Инструмент измерительный (штангенциркуль)'] = {
        }

metadict_detail['|||Инструмент измерительный ртутный (термометр)'] = {
        }

#----
# Производство мебели (ценная, обитая):

metadict_detail['|||Мебель деревянная обитая (диван, 160x80x90-см)'] = {                            
        }

metadict_detail['|||Мебель деревянная обитая (колыбель, 60x40x30-см)'] = {
        }

metadict_detail['|||Мебель деревянная обитая (кровать двуспальная, 160x180x30-см)'] = {
        }

metadict_detail['|||Мебель деревянная обитая (кровать односпальная, 90x180x30-см)'] = {
        }

#----
# Производство мебели (ценная):

metadict_detail['|||Мебель деревянная лакированная (дверь внешняя, 150x80x5-см)'] = {
        # Красное и чёрное дерево, орех. Латунные детали. Лак.
        }

metadict_detail['|||Мебель деревянная лакированная (дверь внутренняя, 150x80x2.5-см)'] = {
        }

metadict_detail['|||Мебель деревянная лакированная (стол обеденный, 200x180x50-см)'] = {
        }

metadict_detail['|||Мебель деревянная лакированная (стол письменный, 120x70x50-см)'] = {
        }

metadict_detail['|||Мебель деревянная лакированная (стол туалетный, 120x70x50-см)'] = {
        }

metadict_detail['|||Мебель деревянная лакированная (сундуков 100-литровый, 120x70x50-см)'] = {
        }

metadict_detail['|||Мебель деревянная лакированная (шкаф-буфет продуктовый 500-литровый, 80x60x150-см)'] = {
        }

metadict_detail['|||Мебель деревянная лакированная (шкаф-витрина вещевой 500-литровый, 80x60x150-см)'] = {
        }

metadict_detail['|||Мебель деревянная лакированная (шкаф-гардероб 600-литровый, 80x60x150-см)'] = {
        }

metadict_detail['|||Мебель деревянная лакированная (шкаф-комод вещевой 200-литровый, 100x60x70-см)'] = {
        }

metadict_detail['|||Мебель деревянная лакированная (шкаф-стеллаж книжный 600-литровый, 80x60x150-см)'] = {
        }

metadict_detail['|||Мебель деревянная лакированная (шкаф-стеллаж туалетный 600-литровый, 80x60x150-см)'] = {
        }

#----
# Производство мебели (простая):

metadict_detail['|||Мебель деревянная шлифованная (дверь амбарная, 300x400x5-см)'] = {
        # Древесина дуба и сосны, шлифовка, окраска масляными красками.
        }

metadict_detail['|||Мебель деревянная шлифованная (дверь внешняя, 150x80x5-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (дверь внутренняя, 150x80x2.5-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (классная доска, 200x100x2-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (колыбель, 60x40x30-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (кровать двуспальная, 160x180x30-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (кровать односпальная, 90x180x30-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (лавка, 160x60x30-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (люк подвальный, 150x80x5-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (люк чердачный, 150x80x5-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (стол кухонный, 140x90x50-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (стол обеденный, 200x180x50-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (стол парта, 120x70x50-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (стол письменный, 120x70x50-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (сундук 100-литровый, 65x40x45-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (шкаф-буфет продуктовый 500-литровый, 80x60x150-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (шкаф-гардероб 600-литровый, 80x60x150-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (шкаф-стеллаж вещевой 600-литровый, 80x60x150-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (шкаф-стеллаж книжный 600-литровый, 80x60x150-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (шкаф-стеллаж посудный 600-литровый, 80x60x150-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (шкаф-стеллаж продуктовый 600-литровый, 80x60x150-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (шкаф-стеллаж рабочий 600-литровый, 80x60x150-см)'] = {
        }

metadict_detail['|||Мебель деревянная шлифованная (шкаф-стеллаж туалетный 600-литровый, 80x60x150-см)'] = {
        }

#----
# Производство мебели (станки):

metadict_detail['|||Станок простой (верстак слесарный, 200x90x50-см)'] = {
        }

metadict_detail['|||Станок простой (верстак столярный, 200x90x50-см)'] = {
        }

metadict_detail['|||Станок простой (касса наборная типографская)'] = {
        }

metadict_detail['|||Станок простой (ткацкий)'] = {
        }

#----
# Стекольное производство (лампы):

metadict_detail['|||Утварь стеклянная (люстра светокристальная 40x40x20-см, 1200 Лм)'] = {
        }

metadict_detail['|||Утварь стеклянная (люстра светокристальная 30x30x20-см, 600 Лм)'] = {
        }

metadict_detail['|||Утварь стеклянная (лампа светокристальная 10x10x20-см, 200 Лм)'] = {
        }

metadict_detail['|||Утварь стеклянная (лампа светляковая 10x10x20-см, 100 Лм)'] = {
        }

metadict_detail['|||Утварь стеклянная (лампа светляковая 10x10x20-см, 200 Лм)'] = {
        }

#----
# Стекольное производство:

metadict_detail['|||Инструмент стеклянный (очки защитные)'] = {
        }

metadict_detail['|||Утварь стеклянная (картина в раме 50x25x3-см)'] = {
        }

metadict_detail['|||Утварь стеклянная (фотография в раме 50x25x3-см)'] = {
        }

metadict_detail['|||Утварь стеклянная (зеркало 50x150x5-см)'] = {
        }

#----
# Гончарное производство (фаянс):

metadict_detail['|||Утварь керамическая (бассейн 2-кубометровый, 200x200x80-см)'] = {
        # Керамика и стеклянная глазурь.
        }

metadict_detail['|||Утварь керамическая (раковина напольная 50-литровая, 60x50x30-см)'] = {
        }

metadict_detail['|||Утварь керамическая (раковина настенная 15-литровая, 50x30x20-см)'] = {
        }

metadict_detail['|||Утварь керамическая (умывальник 25-литровый, 30x30x40-см)'] = {
        }

#----
# Гончарное производство:

metadict_detail['|||Ёмкость керамическая (горшок 100-литровый)'] = {
        }

metadict_detail['|||Ёмкость керамическая (горшок цветочный 10-литровый)'] = {
        }

metadict_detail['|||Посуда керамическая (горшок печной 10-литровый)'] = {
        }

metadict_detail['|||Посуда керамическая (горшок печной 5-литровый)'] = {
        }

metadict_detail['|||Посуда керамическая (горшок печной 3-литровый)'] = {
        }

metadict_detail['|||Посуда керамическая (горшок печной 1-литровый)'] = {
        }

metadict_detail['|||Посуда керамическая (кофейник 1-литровый)'] = {
        }

metadict_detail['|||Посуда керамическая (чайник 1-литровый)'] = {
        }

metadict_detail['|||Посуда керамическая (кружка 0.5-литровая)'] = {
        }

metadict_detail['|||Посуда керамическая (кувшин 3-литровый)'] = {
        }

metadict_detail['|||Посуда керамическая (кувшин 5-литровый)'] = {
        }

metadict_detail['|||Посуда керамическая (миска 0.5-литровая)'] = {
        }

metadict_detail['|||Посуда керамическая (миска 3-литровая)'] = {
        }

metadict_detail['|||Посуда керамическая (миска 5-литровая)'] = {
        }

metadict_detail['|||Посуда керамическая (ступа 5-литровая, 25x25x12-см)'] = {
        }

metadict_detail['|||Посуда керамическая (чашка 0.25-литровая)'] = {
        }

#----
# Бондарное производство:

metadict_detail['|||Ёмкость бондарная (бочка 300-литровая, 83x83x83-см)'] = {
        }

metadict_detail['|||Ёмкость бондарная (бочка 100-литровая, 56x53x53-см)'] = {
        }

metadict_detail['|||Ёмкость бондарная (ведро 10-литровое, 35x27x27-см)'] = {
        }

metadict_detail['|||Ёмкость бондарная (кадка 500-литровая)'] = {
        }

metadict_detail['|||Ёмкость бондарная (кадка 300-литровая, 60x83x83-см)'] = {
        }

metadict_detail['|||Ёмкость бондарная (кадка 100-литровая, 56x53x53-см)'] = {
        }

metadict_detail['|||Ёмкость бондарная (кадка 50-литровая, 48x45x45-см)'] = {
        }

#----
# Столярные работы:

metadict_detail['|||Ёмкость деревянная долблёная (корыто 50-литровое, 60x30x25-см)'] = {
        }

metadict_detail['|||Посуда деревянная долблёная (ковш 1-литровый)'] = {
        }

metadict_detail['|||Посуда деревянная долблёная (ковш 5-литровый)'] = {
        }

metadict_detail['|||Посуда деревянная долблёная (ложка)'] = {
        }

metadict_detail['|||Посуда деревянная долблёная (солонка 0.25-литровая)'] = {
        }

metadict_detail['|||Посуда деревянная долблёная (уголок для сбора сока)'] = {
        }

metadict_detail['|||Инструмент деревянный долблёный (лопатка)'] = {
        }

metadict_detail['|||Инструмент деревянный долблёный (половник 0.25-литровый)'] = {
        }

metadict_detail['|||Инструмент деревянный долблёный (скалка)'] = {
        }

#----
# Плотницкие работы:

metadict_detail['|||Ёмкость деревянная пиленая (лоток 12-литровый)'] = {
        }

metadict_detail['|||Ёмкость деревянная пиленая (ящик 50-литровый)'] = {
        }

metadict_detail['|||Инструмент деревянный пиленый (вышка сборная)'] = {
        }

metadict_detail['|||Инструмент деревянный пиленый (поддон)'] = {
        }

metadict_detail['|||Инструмент деревянный пиленый (подмостки)'] = {
        }

metadict_detail['|||Инструмент деревянный шлифованный (доска 40x60x3-см кухонная)'] = {
        }

metadict_detail['|||Инструмент деревянный шлифованный (доска 40x60x3-см стиральная)'] = {
        }

metadict_detail['|||Инструмент деревянный шлифованный (доска 60x75x3-см кухонная)'] = {
        }

metadict_detail['|||Инструмент деревянный шлифованный (лопата печная)'] = {
        }

metadict_detail['|||Инструмент деревянный шлифованный (лопата)'] = {
        }

metadict_detail['|||Инструмент деревянный шлифованный (совок печной)'] = {
        }

metadict_detail['|||Инструмент деревянный шлифованный (совок)'] = {
        }

metadict_detail['|||Инструмент деревянный шлифованный (сокол)'] = {
        }

metadict_detail['|||Инструмент деревянный шлифованный (трамбовка)'] = {
        }

metadict_detail['|||Инструмент деревянный шлифованный (тёрка)'] = {
        }

#----
# Производство канатов:

metadict_detail['|||Инструмент стальной плетёный (канат стоящего такелажа) (метр)'] = {
        # Из проволоки.
        }

metadict_detail['|||Инструмент пеньковый плетёный (канат такелажный) (метр)'] = {
        }

metadict_detail['|||Инструмент джутовый плетёный (канат строительный) (метр)'] = {
        }

metadict_detail['|||Инструмент джутовый плетёный (шнур) (метр)'] = {
        }

metadict_detail['|||Инструмент мочальный плетёный (валик)'] = {
        # Липовое мочало.
        }

metadict_detail['|||Инструмент мочальный плетёный (кисть)'] = {
        }

metadict_detail['|||Инструмент мочальный плетёный (метёлка печная)'] = {
        }

#----
# Производство корзин и веников:

metadict_detail['|||Ёмкость ивовая плетёная (корзина 10-литровая)'] = {
        }

metadict_detail['|||Ёмкость ивовая плетёная (корзина 50-литровая)'] = {
        }

metadict_detail['|||Ёмкость ивовая плетёная (корзина для мусора 10-литровая, 35x27x27-см)'] = {
        }

metadict_detail['|||Ёмкость ивовая плетёная (корзинка 1-литровая)'] = {
        }

metadict_detail['|||Инструмент ивовый связанный (веник)'] = {
        }

metadict_detail['|||Инструмент ивовый связанный (венчик)'] = {
        }

#----
# Машиностроение (колёсный транспорт):

metadict_detail['|||Механизм колёсный упряжной (грейдер)'] = {
        }

metadict_detail['|||Механизм колёсный упряжной (каток 8-тонный)'] = {
        }

metadict_detail['|||Механизм колёсный упряжной (скрепер, 0.5-кубометра)'] = {
        }

metadict_detail['|||Транспорт колёсный грузовой (телега, 0.5 тонны груза)'] = {
        }

metadict_detail['|||Транспорт колёсный грузовой (тележка, 200-литровая)'] = {
        }

#----
# Машиностроение (планёры):

metadict_detail['|||Транспорт воздушный грузовой (5-тонный планёр, 3 тонны груза)'] = {
        }

metadict_detail['|||Транспорт воздушный пассажирский (1-тонный планёр, 4 пассажира)'] = {
        }

metadict_detail['|||Транспорт воздушный пассажирский (5-тонный планёр, 36 пассажиров)'] = {
        }

metadict_detail['|||Транспорт воздушный санитарный (1-тонный планёр, 4 пассажира)'] = {
        }

#----
# Машиностроение (железные дороги):

metadict_detail['|||Транспорт железнодорожный (вагон пассажирский 10-тонный, 36 мест)'] = {
        }

metadict_detail['|||Транспорт железнодорожный (вагон товарный 6-тонный, 10 тонн груза)'] = {
        }

metadict_detail['|||Транспорт железнодорожный (платформа 6-тонная, 10 тонн груза)'] = {
        }

metadict_detail['|||Транспорт железнодорожный (локомотив маневровый, 400-кВт)'] = {
        }

metadict_detail['|||Транспорт железнодорожный (локомотив основной, 800-кВт)'] = {
        }

#----
# Машиностроение (флот):

metadict_detail['|||Транспорт морской грузовой (барк, 3000 тонн, 1400 тонн груза)'] = {
        }

metadict_detail['|||Транспорт морской пассажирский (барк, 3000 тонн, 288 пассажиров)'] = {
        }

metadict_detail['|||Транспорт речной грузовой (баржа, 400 тонн, 200 тонн груза)'] = {
        }

metadict_detail['|||Транспорт речной пассажирский (баржа, 400 тонн, 108 пассажиров)'] = {
        }

#----
# Машиностроение (станки):

metadict_detail['|||Станок механический (глиномялка)'] = {
        }

metadict_detail['|||Станок механический (кирпичнорезный)'] = {
        }

metadict_detail['|||Станок механический (металлорежущий)'] = {
        }

metadict_detail['|||Станок механический (паркетно-строгательный)'] = {
        }

metadict_detail['|||Станок механический (паркетно-шлифовальный)'] = {
        }

metadict_detail['|||Станок механический (переплётный)'] = {
        }

metadict_detail['|||Станок механический (печатный ротационный обойный)'] = {
        }

metadict_detail['|||Станок механический (печатный ротационный)'] = {
        }

metadict_detail['|||Станок механический (сверлильно-шлифовальный)'] = {
        }

metadict_detail['|||Станок механический (сверлильный)'] = {
        }

metadict_detail['|||Станок механический (ткацкий)'] = {
        }

metadict_detail['|||Станок механический (шлифовальный)'] = {
        }

#----
# Машиностроение (строительные машины):

metadict_detail['|||Механизм строительный (башенный кран)'] = {
        }

metadict_detail['|||Механизм строительный (буровой станок)'] = {
        }

metadict_detail['|||Механизм строительный (копатель)'] = {
        }

metadict_detail['|||Механизм строительный (лебёдка)'] = {
        }

#----
# Машиностроение (гидравлика):

metadict_detail['|||Механизм гидравлический (домкрат 10-тонный)'] = {
        }

metadict_detail['|||Механизм гидравлический (насос высокого давления)'] = {
        }

metadict_detail['|||Механизм гидравлический (насос, 35 литров/минуту)'] = {
        }

metadict_detail['|||Механизм гидравлический (пресс для волокна, 5-кубометров/час)'] = {
        }

metadict_detail['|||Механизм гидравлический (пресс для масла, 300-кг/час)'] = {
        }

#----
# Машиностроение (пневматика):

metadict_detail['|||Механизм пневматический (компрессор, 700 кПа 5-кубометров/минуту)'] = {
        }

metadict_detail['|||Механизм пневматический (трамбовка)'] = {
        }

metadict_detail['|||Механизм пневматический (шпалоподбойка)'] = {
        }

#----
# Машиностроение (механика):

metadict_detail['|||Механизм винтовой (дрель)'] = {
        }

metadict_detail['|||Механизм винтовой (жернова кухонные, 1-кг/час)'] = {
        }

metadict_detail['|||Механизм винтовой (костылевыдёргиватель)'] = {
        }

metadict_detail['|||Механизм винтовой (пресс для фруктов, 50-кг/час)'] = {
        }

metadict_detail['|||Механизм винтовой (пресс кафельный)'] = {
        }

metadict_detail['|||Механизм винтовой (пресс черепичный)'] = {
        }

metadict_detail['|||Механизм винтовой (пресс-пюре)'] = {
        }

metadict_detail['|||Механизм винтовой (разгонщик)'] = {
        }

metadict_detail['|||Механизм винтовой (рихтовщик)'] = {
        }

#----
# Машиностроение (фабричные машины):

metadict_detail['|||Механизм фабричный (барабан сетчатый)'] = {
        }

metadict_detail['|||Механизм фабричный (бумагодельная машина)'] = {
        }

metadict_detail['|||Механизм фабричный (вальцовый пресс мощный)'] = {
        }

metadict_detail['|||Механизм фабричный (вентилятор)'] = {
        }

metadict_detail['|||Механизм фабричный (выколачивающая машина)'] = {
        }

metadict_detail['|||Механизм фабричный (генератор пар --> механ, 5 кВт, пара 50 кг/час, 110x90x90-см)'] = {
        }

metadict_detail['|||Механизм фабричный (диффузионная батарея-маслоэкстрактор)'] = {
        }

metadict_detail['|||Механизм фабричный (дробилка)'] = {
        }

metadict_detail['|||Механизм фабричный (коттон-джин)'] = {
        }

metadict_detail['|||Механизм фабричный (ленточный конвейер 1.2-тонны/час)'] = {
        }

metadict_detail['|||Механизм фабричный (ленточный конвейер 3.6-тонны/час)'] = {
        }

metadict_detail['|||Механизм фабричный (ленточный конвейер 30-тонн/час, 2 метра/секунда)'] = {
        }

metadict_detail['|||Механизм фабричный (лесопильная рама)'] = {
        }

metadict_detail['|||Механизм фабричный (мельница барабанная)'] = {
        }

metadict_detail['|||Механизм фабричный (мельница вальцовая)'] = {
        }

metadict_detail['|||Механизм фабричный (мельница жерновная)'] = {
        }

metadict_detail['|||Механизм фабричный (мельница шаровая)'] = {
        }

metadict_detail['|||Механизм фабричный (мешалка)'] = {
        }

metadict_detail['|||Механизм фабричный (моечная машина)'] = {
        }

metadict_detail['|||Механизм фабричный (молотилка вальцовая)'] = {
        }

metadict_detail['|||Механизм фабричный (молотилка)'] = {
        }

metadict_detail['|||Механизм фабричный (мяльная машина)'] = {
        }

metadict_detail['|||Механизм фабричный (рафинирочное сито)'] = {
        }

metadict_detail['|||Механизм фабричный (ровничная машина)'] = {
        }

metadict_detail['|||Механизм фабричный (сковорода паровая)'] = {
        }

metadict_detail['|||Механизм фабричный (тестомесильная машина)'] = {
        }

metadict_detail['|||Механизм фабричный (тонкопрядильная машина)'] = {
        }

metadict_detail['|||Механизм фабричный (трепальная машина)'] = {
        }

metadict_detail['|||Механизм фабричный (тёрочный барабан)'] = {
        }

metadict_detail['|||Механизм фабричный (цементный пресс)'] = {
        }

metadict_detail['|||Механизм фабричный (чесальная машина)'] = {
        }

#----
# Машиностроение (фабричные машины, детали):

metadict_detail['|||Механизм фабричный, деталь (сито проволочное) (квадратный метр)'] = {
        }

#----
# Машиностроение (оборудование домов):

metadict_detail['|||Оборудование чугунное литое (водонагревный котёл, 50 кВт, 200x100x200-см)'] = {
        }

metadict_detail['|||Оборудование чугунное литое (душ 10-литое/минуту)'] = {
        }

metadict_detail['|||Оборудование чугунное литое (кран 10-литое/минуту)'] = {
        }

metadict_detail['|||Оборудование чугунное литое (паровой котёл, 50 кг/час, 60 кВт, 110x90x90-см)'] = {
        }

metadict_detail['|||Оборудование чугунное литое (радиатор отопления, 1 кВт, 6 секций, 72x60x12-см)'] = {
        }

#----
# Металлургия, кузнечное дело (детали):

metadict_detail['|||Деталь чугунная литая (дверца каминная)'] = {
        }

metadict_detail['|||Деталь чугунная литая (дверца поддувала)'] = {
        }

metadict_detail['|||Деталь чугунная литая (дверца прочистная)'] = {
        }

metadict_detail['|||Деталь чугунная литая (дверца топки)'] = {
        }

metadict_detail['|||Деталь чугунная литая (задвижка дымохода)'] = {
        }

metadict_detail['|||Деталь чугунная литая (задвижка печная)'] = {
        }

metadict_detail['|||Деталь чугунная литая (решётка колосниковая)'] = {
        }

metadict_detail['|||Деталь чугунная литая (самоварник)'] = {
        }

#----
# Металлургия, кузнечное дело (инструменты металлические):

metadict_detail['|||Инструмент железный кованый (щипцы для дров)'] = {
        }

metadict_detail['|||Инструмент жестяной штампованный (воронка кухонная)'] = {
        }

metadict_detail['|||Инструмент жестяной штампованный (дуршлаг 0.25-литровый)'] = {
        }

metadict_detail['|||Инструмент жестяной штампованный (ложка мерная)'] = {
        }

metadict_detail['|||Инструмент жестяной штампованный (ложка столовая)'] = {
        }

metadict_detail['|||Инструмент жестяной штампованный (половник 0.125-литровый)'] = {
        }

metadict_detail['|||Инструмент жестяной штампованный (тёрка кухонная)'] = {
        }

metadict_detail['|||Инструмент жестяной штампованный (шумовка 0.125-литровая)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (вилы)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (гладилка)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (зубило)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (каска)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (кельмо)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (кирка)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (клещи)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (ключ гаечный)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (крюк)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (лом)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (лопата)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (мегафон)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (молоток)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (нож столовый, 10-см)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (нож, 10-см)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (нож, 6-см)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (нож-овощечистка)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (ножницы, 10-см)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (ножовка)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (рубанок)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (скоба)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (скребок)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (струбница)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (тесак, 20-см)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (топор)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (шпатель)'] = {
        }

metadict_detail['|||Инструмент стальной кованый (щипцы)'] = {
        }

metadict_detail['|||Инструмент чугунный литой (кочерга)'] = {
        }

metadict_detail['|||Инструмент чугунный литой (кувалда)'] = {
        }

metadict_detail['|||Инструмент чугунный литой (мангал 45x30-см)'] = {
        }

metadict_detail['|||Инструмент чугунный литой (прут)'] = {
        }

metadict_detail['|||Инструмент чугунный литой (сковородник)'] = {
        }

metadict_detail['|||Инструмент чугунный литой (утюг)'] = {
        }

metadict_detail['|||Инструмент чугунный литой (ухват)'] = {
        }

#----
# Металлургия, кузнечное дело (ёмкости металлические):

metadict_detail['|||Ёмкость жестяная кованая (форма для выпечки 2-литровая)'] = {
        }

metadict_detail['|||Ёмкость жестяная кованая (формочка для выпечки)'] = {
        }

metadict_detail['|||Ёмкость медная лужёная (чан 300-литровый)'] = {
        }

metadict_detail['|||Ёмкость стальная кованая (противень 300-литровый)'] = {
        }

metadict_detail['|||Ёмкость стальная кованая (чан 300-литровый)'] = {
        }

metadict_detail['|||Ёмкость чугунная литая (реторта 6-кубометровая)'] = {
        }

metadict_detail['|||Ёмкость чугунная литая (чан 20-кубометровый)'] = {
        }

metadict_detail['|||Посуда жестяная штампованная (противень 12-литровый)'] = {
        }

metadict_detail['|||Посуда медная лужёная (самовар 5-литровый)'] = {
        }

metadict_detail['|||Посуда стальная никелированная (сотейник 2-литровый)'] = {
        }

metadict_detail['|||Посуда чугунная литая (котелок 10-литровый)'] = {
        }

metadict_detail['|||Посуда чугунная литая (котёл 25-литровый)'] = {
        }

metadict_detail['|||Посуда чугунная литая (сковорода 1-литровая)'] = {
        }

metadict_detail['|||Посуда чугунная литая (таз эмалированный 10-литровый)'] = {
        }

metadict_detail['|||Посуда чугунная литая (чугунок 1-литровый)'] = {
        }

metadict_detail['|||Посуда чугунная литая (чугунок 3-литровый)'] = {
        }

metadict_detail['|||Посуда чугунная литая (чугунок эмалированный 5-литровый)'] = {
        }