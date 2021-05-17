#----
# Производства (шитьё)
    # Плотность материалов:
        # бязь -- 120 грамм/кв.метр
        # сатин -- 120 грамм/кв.метр
        # сатин-жаккард -- 140 грамм/кв.метр
        # Льняная ткань -- 150 грамм/кв.метр
        # фланель -- 200 грамм/кв.метр
        # бархат -- 300 грамм/кв.метр
        # Хопчатобумажная замша -- 410 грамм/кв.метр
        # Льняная парусина -- 450-550 грамм/кв.метр
        # Вата швейная (набивка) -- 25 кг/кубометр
        # https://tessuti-ital.ru/news/plotnost-tkanej/

#----
# Производства (утварь)

metadict_army['_Производство утвари, скатерть (хлопок)'] = {
        # Сатин -- весьма дорогой материал. Но так заведено.
        # 2.2 × 1.3 = 2.86 м²
        '_Производство утвари текстильной (нормо-часов)':5 / 60,
        'Ткань хлопчатая, сатин (квадратный метр)':2.2 * 1.3,
        'Нить хлопчатая швейная (метр)':(2.2 + 1.3) * 2 * 4,
        }

metadict_army['_Производство утвари, шторы (хлопок)'] = {
        # 1.0 × 1.0 = 1 м²
        '_Производство утвари текстильной (нормо-часов)':5 / 60,
        'Ткань хлопчатая, сатин (квадратный метр)':1.0 * 1.0,
        'Нить хлопчатая швейная (метр)':(1.0 + 1.0) * 2 * 4,
        }

metadict_army['_Производство утвари, полотенце (хлопок)'] = {
        # 0.4 × 0.6 = 0.24 м²
        '_Производство утвари текстильной (нормо-часов)':1 / 60,
        'Ткань хлопчатая, бязь (квадратный метр)':0.4 * 0.6,
        'Нить хлопчатая швейная (метр)':(0.4 + 0.6) * 2 * 4,
        }

metadict_army['_Производство утвари, холст (лён)'] = {
        # 0.8 × 1.2 = 0.96 м²
        '_Производство утвари текстильной (нормо-часов)':1 / 60,
        'Ткань льняная, мешковина (квадратный метр)':0.9 * 1.2,
        'Нить хлопчатая швейная (метр)':(0.9 + 1.2) * 2 * 4,
        }

metadict_army['_Производство утвари, мешочек (лён)'] = {
        # 0.2 × 0.2 = 0.04 м²
        '_Производство утвари текстильной (нормо-часов)':1 / 60,
        'Ткань льняная, мешковина (квадратный метр)':0.2 * 0.2 * 2,
        'Нить хлопчатая швейная (метр)':(0.2 + 0.2) * 2 * 4,
        }

metadict_army['_Производство утвари, сито (джут)'] = {
        # 0.2 × 0.2 = 0.04 м²
        '_Производство утвари текстильной (нормо-часов)':1 / 60,
        'Ткань джутовая (квадратный метр)':0.2 * 0.2,
        }

metadict_army['_Производство утвари, ветошь (лоскуты)'] = {
        # Бывшее полотенце, кусок простыни, скатерти, одежды.
        # 0.4 × 0.6 = 0.24 м²
        '_Производство утвари текстильной (нормо-часов)':1 / 60,
        '-Ткань, лоскуты (требуется/квадратный метр)':0.4 * 0.6,
        }

#----
# Производства (бельё)
    # Площадь одежды (размеры для людей):
        # Площадь тела человека — 1.8 м²
        # Простыня: 1.5 × 2 = 3 м²
        # Одеяло: 1.5 × 2 × 2 = 6 м²
        # Подушка: 0.6 × 0.6 × 2 = 0.72 м²
        # Матрац: 0.7 × 1.9 × 2 = 2.7 м²

metadict_detail['_Производство белья, матрац (вата)'] = {
        # Вата 6 см -- 1.5 кг/кв.метр
        # Чехол (бязь) -- 2.7 кв.метра
        # Пикование (прошивка): 40+40 нитей на метр матраца
        '_Производство белья (нормо-часов)':60 / 60,
        'Ткань хлопчатая, бязь (квадратный метр)':0.7 * 1.9 * 2,
        'Вата хлопчатая швейная (кубометр)':0.7 * 1.9 * 0.06,
        'Нить хлопчатая швейная (метр)':(0.7 * 1.9) * (40 + 40),
        }

metadict_detail['_Производство белья, одеяло стёганное (вата)'] = {
        # Вата 3 см -- 0.75 кг/кв.метр
        # Чехол (бязь) -- 6 кв.метра
        # Пикование (прошивка): 40+40 нитей на метр матраца
        '_Производство белья (нормо-часов)':60 / 60,
        'Ткань хлопчатая, бязь (квадратный метр)':1.5 * 2.0 * 2,
        'Вата хлопчатая швейная (кубометр)':1.5 * 2.0 * 0.03,
        'Нить хлопчатая швейная (метр)':(1.5 * 2.0) * (40 + 40),
        }

metadict_detail['_Производство белья, подушка стёганная (вата)'] = {
        # Вата 12 см -- 3 кг/кв.метр
        # Чехол (бязь) -- 0.72 кв.метра
        # Есть мнение, что вата для набивки не годится.
        '_Производство белья (нормо-часов)':10 / 60,
        'Ткань хлопчатая, бязь (квадратный метр)':0.6 * 0.6 * 2,
        'Вата хлопчатая швейная (кубометр)':0.6 * 0.6 * 0.12,
        }

metadict_detail['_Производство белья, простыня (хлопок)'] = {
        '_Производство белья (нормо-часов)':6 / 60,
        'Ткань хлопчатая, бязь (квадратный метр)':1.5 * 2.0,
        'Нить хлопчатая швейная (метр)':(1.5 + 2.0) * 2 * 4,
        }

metadict_detail['_Производство белья, одеяло лоскутное (вата)'] = {
        # Делается сельской единорожкой из старой одежды, поэтому трудозатраты выше.
        # Вата 3 см -- 0.75 кг/кв.метр
        # Чехол (бязь) -- 6 кв.метра
        # Пикование (прошивка): 20+20 нитей на метр матраца
        '_Производство белья (нормо-часов)':120 / 60,
        'Вата хлопчатая швейная (кубометр)':1.5 * 2.0 * 0.03,
        'Нить хлопчатая швейная (метр)':(1.5 * 2.0) * (20 + 20),
        '-Ткань, лоскуты (требуется/квадратный метр)':1.5 * 2.0 * 2,
        }

metadict_detail['_Производство белья, простыня (парусина)'] = {
        # Прошивается по краю в 4 нити
        '_Производство белья (нормо-часов)':6 / 60,
        'Ткань полульняная, парусина (квадратный метр)':1.5 * 2.0,
        'Нить льняная швейная (метр)':(1.5 + 2.0) * 2 * 4,
        }

metadict_detail['_Производство белья, чехол тюфяка (мешковина)'] = {
        # По сути мешок, набитый соломой.
        '_Производство белья (нормо-часов)':6 / 60,
        'Ткань льняная, мешковина (квадратный метр)':0.9 * 2.0,
        'Нить льняная швейная (метр)':(0.9 + 2.0) * 2 * 4,
        }

#----
# Производства (одежда)
    # Нормы расхода швейных ниток на различные виды швейных изделий
        # http://www.modnaya.ru/library/012/012.htm
        # http://www.modnaya.ru/library/012/013.htm
    # Производство одежды:
        # Брюки (фабрика) -- 2.5 нормо-часов/пара
        # Жилеты (фабрика) -- 0.37 нормо-часа/штука
        # Жакеты (фабрика) -- 0.92 нормо-часа/штука
        # Костюмы (фабрика) -- 8 нормо-часов/штука
        # Пальто (фабрика) -- 8 нормо-часов/штука
        # Рубаха (ручной труд) -- 4 нормо-часов/штука
        # Износ -- 3 комплекта белья/год, 1 костюм, 1 пальто, 1 ботинки.
        # https://istmat.info/node/27433
    # Пропорции пони:
        # https://raw.githubusercontent.com/Shadybloom/amber-in-the-dark/master/images/glow.png
        # Рост в холке — 75 см
        # Рост в ушках — 120 см
        # Длина передних ног — 50 см (до перехода в грудь, если смотреть спереди)
        # Длина задней ноги до сустава — 48 см
        # Диаметр копыта (мера длины, хуф) — 10 см
        # Длина тела (от хвоста до груди) — 45 см
        # Ширина тела (груди) — 35 см
        # Размеры головы:
            # Длина — 40 см (от кончика носа до затылка)
            # Ширина — 40 см (от скулы до скулы)
            # Высота — 32 см (от затылка до шеи)
        # Площадь тела пони — 1.75 м²

metadict_detail['_Производство одежды, бушлат (хлопок)'] = {
        # Замшевый бушлат, короткое пальто, Peacoat.
        # https://derpibooru.org/images/2383102
        # https://derpibooru.org/images/2225845
        # https://upload.wikimedia.org/wikipedia/commons/2/22/US_Navy_p_coat_wiki.jpg
        # На 20 см ниже живота:
            # Грудь, круп: 0,4 × 0,4 × 2 = 0,32 м²
            # Спина, живот: 0,5 × 0,4 × 2 = 0.4 м²
            # Рукава, на все 4 ноги: ((2 × 3,14 × 0,05 × (0,05 + (20 / 50))) × (20 / 50)) × 4 = 0.23 м²
            # Бока, круп, полы: 0.5 × (0,4 + 0.2) × 3 = 0,9 м²
        # Всего 1.85 кв.м ткани. Выкройка 85%
        '_Производство одежды (нормо-часов)':8,
        'Ткань хлопчатая, замша (квадратный метр)':1.85 / 0.85,
        'Ткань хлопчатая, сатин (квадратный метр)':1.85 / 0.85 * 2,
        'Вата хлопчатая швейная (кубометр)':1.85 * 0.01,
        'Нить хлопчатая швейная (метр)':600,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':((1.85 / 0.85) - 1.85) * 3,
        }

metadict_detail['_Производство одежды, пальто (хлопок)'] = {
        # Простонародная одежда. Trenchcoat
            # Всепогодное защитное снаряжение пегасов и множества прочих работяг.
            # В огромном количестве производится для погодной службы. Без одежды невесело летать.
            # https://derpibooru.org/images/1931802
        # Всего 1.85 кв.м ткани. Выкройка 85%
        '_Производство одежды (нормо-часов)':8,
        'Ткань льняная, брезент (квадратный метр)':1.85 / 0.85,
        'Ткань хлопчатая, бязь (квадратный метр)':1.85 / 0.85 * 2,
        'Вата хлопчатая швейная (кубометр)':1.85 * 0.01,
        'Нить хлопчатая швейная (метр)':600,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':((1.85 / 0.85) - 1.85) * 3,
        }

metadict_detail['_Производство одежды, кафтан (хлопок)'] = {
        # Зимний, с поясом. Удобно надевать и снимать для земнопони.
        # На 30 см ниже живота:
            # Грудь: 0,4 × 0,4 × 1 = 0,16 м²
            # Спина, живот: 0,5 × 0,4 × 2 = 0.4 м²
            # Рукава, на 2 ноги: ((2 × 3,14 × 0,05 × (0,05 + (30 / 50))) × (30 / 50)) × 2 = 0.25 м²
            # Бока, круп, полы: 0.5 × (0,4 + 0.3) × 3 = 1,05 м²
            # https://derpibooru.org/images/2224134
            # https://derpibooru.org/images/1640096
        # Всего 1.86 кв.м ткани. Выкройка 85%
        '_Производство одежды (нормо-часов)':8,
        'Ткань хлопчатая, бархат (квадратный метр)':1.85 / 0.85,
        'Ткань хлопчатая, сатин (квадратный метр)':1.85 / 0.85 * 2,
        'Вата хлопчатая швейная (кубометр)':1.85 * 0.01,
        'Нить хлопчатая швейная (метр)':430,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':((1.85 / 0.85) - 1.85) * 3,
        }

metadict_detail['_Производство одежды, платье (хлопок)'] = {
        # Красиво облегает всё тело. Если собственная шёрстка недостаточно хороша.
        # На 30 см ниже живота:
            # Грудь, круп: 0,4 × 0,4 × 2 = 0,32 м²
            # Спина, живот: 0,5 × 0,4 × 2 = 0.4 м²
            # Рукава, на все 4 ноги: ((2 × 3,14 × 0,05 × (0,05 + (30 / 50))) × (30 / 50)) × 4 = 0.5 м²
            # Бока, круп, полы: 0.5 × (0,4 + 0.3) × 3 = 1,05 м²
            # https://derpibooru.org/images/2609193
        # Всего 2.3 кв.м ткани. Выкройка 85%
        '_Производство одежды (нормо-часов)':8,
        'Ткань хлопчатая, бархат (квадратный метр)':2.3 / 0.85,
        'Нить хлопчатая швейная (метр)':450,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':((2.3 / 0.85) - 2.3),
        }

metadict_detail['_Производство одежды, жакет (хлопок)'] = {
        # Рубаха с рукавами на половину длины передних ног:
        # На 30 см ниже живота:
            # Грудь, круп: 0,4 × 0,4 × 2 = 0,32 м²
            # Спина, живот, бока: 0,5 × 0,4 × 4 = 0.8 м²
            # Рукава, на 2 ноги: ((2 × 3,14 × 0,05 × (0,05 + (30 / 50))) × (30 / 50)) × 2 = 0.25 м²
            # https://derpibooru.org/images/1188131
        # Всего 1.37 кв.м ткани. Выкройка 85%
        '_Производство одежды (нормо-часов)':2,
        'Ткань хлопчатая, замша (квадратный метр)':1.4 / 0.85,
        'Ткань хлопчатая, сатин (квадратный метр)':1.4 / 0.85,
        'Нить хлопчатая швейная (метр)':280,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':((1.4 / 0.85) - 1.4) * 2,
        }

metadict_detail['_Производство одежды, пиджак (хлопок)'] = {
        # Рубаха с рукавами на половину длины передних ног:
        # Всего 1.37 кв.м ткани. Выкройка 85%
        '_Производство одежды (нормо-часов)':2,
        'Ткань хлопчатая, замша (квадратный метр)':1.4 / 0.85,
        'Ткань хлопчатая, сатин (квадратный метр)':1.4 / 0.85,
        'Нить хлопчатая швейная (метр)':250,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':((1.4 / 0.85) - 1.4) * 2,
        }

metadict_detail['_Производство одежды, жилет (хлопок)'] = {
        # Безрукавка, защита груди под упряжь. Как у Брейбёрна.
            # Грудь, круп: 0,4 × 0,4 × 2 = 0,32 м²
            # Спина, живот, бока: (0,5 / 2) × 0,4 × 4 = 0.4 м²
            # https://mlp.fandom.com/wiki/Braeburn
        # Всего 0.7 кв.м ткани. Выкройка 85%
        '_Производство одежды (нормо-часов)':1,
        'Ткань хлопчатая, замша (квадратный метр)':0.7 / 0.85,
        'Ткань хлопчатая, сатин (квадратный метр)':0.7 / 0.85,
        'Нить хлопчатая швейная (метр)':200,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':((0.7 / 0.85) - 0.7) * 2,
        }

metadict_detail['_Производство одежды, жилет (парусина)'] = {
        # Всего 0.7 кв.м ткани. Выкройка 85%
        '_Производство одежды (нормо-часов)':0.4,
        'Ткань полульняная, парусина (квадратный метр)':0.7 / 0.85,
        'Нить льняная швейная (метр)':200,
        '+Ткань льняная, лоскуты (доступно/квадратный метр)':((0.7 / 0.85) - 0.7),
        }

metadict_detail['_Производство одежды, плащ (хлопок)'] = {
        # Зимний, с завязкой на груди. С капюшоном и ушками.
        # На 30 см ниже живота:
            # Грудь: 0,4 × 0,4 × 1 = 0,16 м²
            # Спина: 0,5 × 0,4 × 1 = 0.2 м²
            # Бока, круп, полы: 0.5 × (0,4 + 0.3) × 3 = 1,05 м²
            # Голова, шея, капюшон: 0.4 × 0.4 × 3 = 0.48 м²
            # Ушки: 0.15 × 0.25 × 2 × 2 = 0.15 м²
        # Всего 2.04 кв.м ткани. Выкройка 95%
        '_Производство одежды (нормо-часов)':1,
        'Ткань хлопчатая, замша (квадратный метр)':2.1 / 0.95,
        'Ткань хлопчатая, сатин (квадратный метр)':2.1 / 0.95 * 2,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':((2.1 / 0.95) - 2.1) * 3,
        'Вата хлопчатая швейная (кубометр)':2.1 * 0.01,
        'Нить хлопчатая швейная (метр)':380,
        }

metadict_detail['_Производство одежды, плащ (брезент)'] = {
        # Тёплый и непромокаемый. Для простых и практичных пони.
        # Всего 2.04 кв.м ткани. Выкройка 95%
        '_Производство одежды (нормо-часов)':1,
        'Ткань льняная, брезент (квадратный метр)':2.1 / 0.95,
        'Ткань льняная, простая (квадратный метр)':2.1 / 0.95,
        '+Ткань льняная, лоскуты (доступно/квадратный метр)':((2.1 / 0.95) - 2.1) * 2,
        'Вата хлопчатая швейная (кубометр)':2.1 * 0.01,
        'Нить льняная швейная (метр)':380,
        }

metadict_detail['_Производство одежды, ветровка (брезент)'] = {
        # Рубаха с рукавами на половину длины передних ног. С капюшоном и ушками.
        # На 30 см ниже живота:
            # Грудь, круп: 0,4 × 0,4 × 2 = 0,32 м²
            # Спина, живот, бока: 0,5 × 0,4 × 4 = 0.8 м²
            # Рукава, на 2 ноги: ((2 × 3,14 × 0,05 × (0,05 + (30 / 50))) × (30 / 50)) × 2 = 0.25 м²
            # Голова, шея, капюшон: 0.4 × 0.4 × 3 = 0.48 м²
            # Ушки: 0.15 × 0.25 × 2 × 2 = 0.15 м²
            # https://derpibooru.org/images/1605206
            # https://derpibooru.org/images/1065758
        # Всего 2.0 кв.м ткани. Выкройка 85%
        '_Производство одежды (нормо-часов)':0.5,
        'Ткань полульняная, парусина (квадратный метр)':2.0 / 0.85,
        '+Ткань льняная, лоскуты (доступно/квадратный метр)':((2.0 / 0.85) - 2.0),
        'Нить льняная швейная (метр)':380,
        }

metadict_detail['_Производство одежды, чепчик (лён)'] = {
        # Тканевый платок, чтобы гриву не замарать.
            # Голова, шея, капюшон: 0.4 × 0.4 × 3 = 0.48 м²
            # Ушки: 0.15 × 0.25 × 2 × 2 = 0.15 м²
        # Всего 0.65 кв.м ткани. Выкройка 95%
        '_Производство одежды (нормо-часов)':0.2,
        'Ткань льняная, простая (квадратный метр)':0.65 / 0.95,
        '+Ткань льняная, лоскуты (доступно/квадратный метр)':((0.65 / 0.95) - 0.65),
        'Нить льняная швейная (метр)':100,
        }

metadict_detail['_Производство одежды, чепчик (хлопок)'] = {
        # Всего 0.65 кв.м ткани. Выкройка 95%
        '_Производство одежды (нормо-часов)':0.2,
        'Ткань хлопчатая, бязь (квадратный метр)':0.65 / 0.95,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':((0.65 / 0.95) - 0.65),
        'Нить хлопчатая швейная (метр)':100,
        }

metadict_detail['_Производство одежды, шапка (хлопок)'] = {
        # Тёплая зимняя шапочка.
        # Всего 0.65 кв.м ткани. Выкройка 85%
        '_Производство одежды (нормо-часов)':1,
        'Ткань хлопчатая, замша (квадратный метр)':0.65 / 0.85,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':((0.65 / 0.85) - 0.65),
        'Нить хлопчатая швейная (метр)':100,
        }

metadict_detail['_Производство одежды, шляпа (солома)'] = {
        # Широкополая, 10 см.
            # Голова, шляпа, круг: 3.14 × (0.2 + 0.1) ^ 2 = 0.28 м²
            # Голова, шляпа, цилиндр: (2 × 3,14 × 0,2) × 0,2 = 0.25 м²
        # Всего 0.53 кв.м ткани. Выкройка 85%
        '_Производство одежды (нормо-часов)':0.3,
        'Ткань соломенная, домотканная (квадратный метр)':0.53 / 0.85,
        'Нить льняная швейная (метр)':50,
        }

metadict_detail['_Производство одежды, шляпа (хлопок)'] = {
        # Летняя, с ремешком на подбородок.
        # Всего 0.53 кв.м ткани. Выкройка 85%
        '_Производство одежды (нормо-часов)':0.3,
        'Ткань хлопчатая, замша (квадратный метр)':0.53 / 0.85,
        'Нить хлопчатая швейная (метр)':50,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':((0.53 / 0.85) - 0.53),
        }

metadict_detail['_Производство одежды, чулки (хлопок)'] = {
        # На всю длину ног:
            # Рукава, на 4 ноги: ((2 × 3,14 × 0,05 × (0,05 + 0.5)) × 0.5) × 4 = 0.34 м²
            # Онучи были бы практичнее, но земным чулки удобнее.
            # https://ru.wikipedia.org/wiki/Онучи
        # Всего 0.35 кв.м ткани. Выкройка 95%
        '_Производство одежды (нормо-часов)':0.2,
        'Ткань хлопчатая, бязь (квадратный метр)':0.35 / 0.95,
        'Нить хлопчатая швейная (метр)':220,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':((0.35 / 0.95) - 0.35),
        }

#----
# Производства (обувь)
    # Производство обуви:
        # ботинки (ручной труд) -- 8 нормо-часов/пара,
        # ботинки (фабрика, 200 рабочих) -- 1.83 нормо-часа/пара.
        # Пара кожаной обуви -- 0.8 кг (материал 0.375 стоимости). Срок службы -- 1 год
        # https://istmat.info/node/27431
        # Нормы расходования ниток, клея, краски, растворителей, воска, парафина, грунта и т.д. на 100 пар обуви. 
        # http://shoeslib.ru/books/item/f00/s00/z0000004/index.shtml

metadict_detail['_Производство обуви, ботинки (кирза)'] = {
        # Пони не имитируют текстуру кожи. Их накопытники обычно повторяют цвет верхней одежды.
        # Пони -- четвероногие, посему и носят по четыре сапога.
        '_Производство обуви (нормо-часов)':4 * 2,
        'Ткань кирзовая (килограмм)':0.8 * 2,
        }

metadict_detail['_Производство обуви, туфли (кирза)'] = {
        '_Производство обуви (нормо-часов)':2 * 2,
        'Ткань кирзовая (килограмм)':0.4 * 2,
        }

metadict_detail['_Производство обуви, галоши (каучук)'] = {
        '_Производство обуви (нормо-часов)':1 * 2,
        'Резина вулканизированная (килограмм)':0.4 * 2,
        }

metadict_detail['_Производство обуви, туфли (джут)'] = {
        '_Производство обуви (нормо-часов)':0.3 * 2,
        'Ткань джутовая (килограмм)':0.4 * 2,
        }

#----
# Утилизация (утварь)

metadict_army['_Утилизация утвари, шторы (хлопок)'] = {
        '_-Утилизация утвари (нормо-часов)':1 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':1.0 * 1.0,
        }

metadict_army['_Утилизация утвари, полотенце (хлопок)'] = {
        '_-Утилизация утвари (нормо-часов)':1 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':0.4 * 0.6,
        }

metadict_army['_Утилизация утвари, скатерть (хлопок)'] = {
        '_-Утилизация утвари (нормо-часов)':3 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':2.2 * 1.3,
        }

metadict_army['_Утилизация утвари, холст (лён)'] = {
        '_-Утилизация утвари (нормо-часов)':1 / 60,
        '+Ткань льняная, лоскуты (доступно/квадратный метр)':0.9 * 1.2,
        }

metadict_army['_Утилизация утвари, мешочек (лён)'] = {
        '_-Утилизация утвари (нормо-часов)':1 / 60,
        '+Ткань льняная, лоскуты (доступно/квадратный метр)':0.2 * 0.2,
        }

metadict_army['_Утилизация утвари, сито (джут)'] = {
        }

metadict_army['_Утилизация утвари, ветошь (лоскуты)'] = {
        }


#----
# Утилизация (бельё)

metadict_detail['_Утилизация белья, матрац (вата)'] = {
        # Disassemble!
        '_-Утилизация белья (нормо-часов)':10 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':0.7 * 1.9 * 2,
        '+Вата техническая (доступно/кубометр)':0.7 * 1.9 * 0.06,
        }

metadict_detail['_Утилизация белья, одеяло лоскутное (вата)'] = {
        #'+Ветошь (доступно/квадратный метр)':1.5 * 2.0 * 2,
        '+Вата техническая (доступно/кубометр)':1.5 * 2.0 * 0.03,
        '_-Утилизация белья (нормо-часов)':10 / 60,
        }

metadict_detail['_Утилизация белья, одеяло стёганное (вата)'] = {
        '_-Утилизация белья (нормо-часов)':10 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':1.5 * 2.0 * 2,
        '+Вата техническая (доступно/кубометр)':1.5 * 2.0 * 0.03,
        }

metadict_detail['_Утилизация белья, подушка стёганная (вата)'] = {
        '_-Утилизация белья (нормо-часов)':5 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':0.6 * 0.6 * 2,
        '+Вата техническая (доступно/кубометр)':0.6 * 0.6 * 0.12,
        }

metadict_detail['_Утилизация белья, простыня (хлопок)'] = {
        '_-Утилизация белья (нормо-часов)':5 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':1.5 * 2.0,
        }

metadict_detail['_Утилизация белья, простыня (парусина)'] = {
        '_-Утилизация белья (нормо-часов)':5 / 60,
        '+Ткань льняная, лоскуты (доступно/квадратный метр)':1.5 * 2.0,
        }

metadict_detail['_Утилизация белья, чехол тюфяка (мешковина)'] = {
        '_-Утилизация белья (нормо-часов)':5 / 60,
        '+Ткань льняная, лоскуты (доступно/квадратный метр)':0.9 * 2.0,
        }

#----
# Утилизация (одежда)

metadict_detail['_Утилизация одежды, бушлат (хлопок)'] = {
        '_-Утилизация одежды (нормо-часов)':20 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':1.85 * 3,
        '+Вата техническая (доступно/кубометр)':1.85 * 0.01,
        }

metadict_detail['_Утилизация одежды, пальто (хлопок)'] = {
        '_-Утилизация одежды (нормо-часов)':20 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':1.85 * 3,
        '+Вата техническая (доступно/кубометр)':1.85 * 0.01,
        }

metadict_detail['_Утилизация одежды, платье (хлопок)'] = {
        '_-Утилизация одежды (нормо-часов)':10 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':2.3,
        }

metadict_detail['_Утилизация одежды, кафтан (хлопок)'] = {
        '_-Утилизация одежды (нормо-часов)':20 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':1.85 * 3,
        '+Вата техническая (доступно/кубометр)':1.85 * 0.01,
        }

metadict_detail['_Утилизация одежды, плащ (хлопок)'] = {
        '_-Утилизация одежды (нормо-часов)':10 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':2.1 * 3,
        '+Вата техническая (доступно/кубометр)':2.1 * 0.01,
        }

metadict_detail['_Утилизация одежды, жакет (хлопок)'] = {
        '_-Утилизация одежды (нормо-часов)':5 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':1.4 * 2,
        }

metadict_detail['_Утилизация одежды, пиджак (хлопок)'] = {
        '_-Утилизация одежды (нормо-часов)':5 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':1.4 * 2,
        }

metadict_detail['_Утилизация одежды, жилет (хлопок)'] = {
        '_-Утилизация одежды (нормо-часов)':5 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':0.7 * 2,
        }

metadict_detail['_Утилизация одежды, чепчик (хлопок)'] = {
        '_-Утилизация одежды (нормо-часов)':2 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':0.65,
        }

metadict_detail['_Утилизация одежды, шапка (хлопок)'] = {
        '_-Утилизация одежды (нормо-часов)':2 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':0.65,
        }

metadict_detail['_Утилизация одежды, шляпа (хлопок)'] = {
        '_-Утилизация одежды (нормо-часов)':2 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':0.53,
        }

metadict_detail['_Утилизация одежды, чулки (хлопок)'] = {
        '_-Утилизация одежды (нормо-часов)':2 / 60,
        '+Ткань хлопчатая, лоскуты (доступно/квадратный метр)':0.95,
        }

metadict_detail['_Утилизация одежды, жилет (парусина)'] = {
        '_-Утилизация одежды (нормо-часов)':2 / 60,
        '+Ткань льняная, лоскуты (доступно/квадратный метр)':0.7,
        }

metadict_detail['_Утилизация одежды, ветровка (брезент)'] = {
        '_-Утилизация одежды (нормо-часов)':2 / 60,
        '+Ткань льняная, лоскуты (доступно/квадратный метр)':2.0,
        }

metadict_detail['_Утилизация одежды, плащ (брезент)'] = {
        '_-Утилизация одежды (нормо-часов)':10 / 60,
        '+Ткань льняная, лоскуты (доступно/квадратный метр)':2.1 * 3,
        '+Вата техническая (доступно/кубометр)':2.1 * 0.01,
        }

metadict_detail['_Утилизация одежды, шляпа (солома)'] = {
        # Лол, зачем?
        }

#----
# Утилизация (обувь)

metadict_detail['_Утилизация обуви, ботинки (кирза)'] = {
        '_-Утилизация обуви (нормо-часов)':5 / 60,
        '+Ткань кирзовая (доступно/килограмм)':0.8 * 2,
        }

metadict_detail['_Утилизация обуви, галоши (каучук)'] = {
        '_-Утилизация обуви (нормо-часов)':5 / 60,
        '+Резина вулканизированная (доступно/килограмм)':0.4 * 2,
        }

metadict_detail['_Утилизация обуви, туфли (кирза)'] = {
        '_-Утилизация обуви (нормо-часов)':5 / 60,
        '+Ткань кирзовая (доступно/килограмм)':0.4 * 2,
        }

metadict_detail['_Утилизация обуви, туфли (джут)'] = {
        }

#----
# Производства (текстильная промышленность)
    # Германия (1895 год)
        # https://istmat.info/node/27434
        # Расход льняного полотна -- 0.8 кг/человека
        # Производство шерстяной ткани -- 0.8 кг/человека (потребность 2 кг/человека)
    # Производительность:
        # 100 кг хлопка-сырца = 90 кг пряжи = 88 кг ткани
        # 100 кг грязной шерсти = 50 кг чистой = 42 кг пряжи = 40 кг ткани
        # 1 веретено (200 ватт) = 0.0084 кг пряжи/час (42 кг пряжи/год, 16 часов работы/день, 300 дней/год)
        # 1 рабочий на 250 веретен (0.5 нормо-часа/килограмм пряжи)
        # 1 рабочий на 2 ткацких станка (0.6 нормо-часа/метр ткани, 2600 метров/год)
    # Чистка и беление ткани (1890 год):
        # В Лонкшире употребляют следующие операции:
        # 1) бучение в извести,
        # 2) промывку,
        # 3) пропускание через кислоту,
        # 4) промывку,
        # 5) бучение с кальцинированным натром,
        # 6) промывку,
        # 7) химическое Б.,
        # 8) промывку,
        # 9) пропускание через кислоту,
        # 10) промывку,
        # 11) кипячение с содой,
        # 12) промывку,
        # 13) химическое Б.,
        # 14) промывку,
        # 15) пропускание через кислоту
        # 16) промывку и сушку.
        # http://wiki.laser.ru/index.php/Беление_тканей_и_пряжи
        # http://wiki.laser.ru/index.php/Белильная_известь

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
        'Бечева пеньковая швейная (метр)':120,
        #'_Производство соломенных ковров (годовой оборот)':1 / 20000,
        }


