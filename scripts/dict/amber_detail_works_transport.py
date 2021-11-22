#----
# Железные дороги, работа путевых смотрителей:

metadict_detail['_-Обслуживание двухколейных главных путей (нормо-часов)'] = {
        '_-Работа бригады путевых смотрителей (нормо-часов)':1,
        }

metadict_detail['_-Обслуживание одноколейных главных путей (нормо-часов)'] = {
        '_-Работа бригады путевых смотрителей (нормо-часов)':1,
        }

metadict_detail['_-Обслуживание подъездных путей (нормо-часов)'] = {
        '_-Работа бригады путевых смотрителей (нормо-часов)':1,
        }

metadict_detail['_-Обслуживание станционных путей (нормо-часов)'] = {
        '_-Работа бригады путевых смотрителей (нормо-часов)':1,
        }

#----
# Транспортные средства (погрузка-разгрузка):

metadict_detail['_-Работы погрузочно-разгрузочные с баржи (тонн)'] = {
        # Погрузочно - разгрузочные работы с применением простейших приспособлений
        # http://www.6pl.ru/gost/pMt_76nvp3.htm
            # Перемещение груза без механизации -- 20 метров
            # Грузы в кипах, тюках, ящиках, связках -- до 15 килограмм
            # Трудозатраты -- 0.5 нормо-часа
        # На разгрузке работаю 20 грузчиков (то есть каждая тонна разгружается за 0.025 часа).
        # Грузчики работают в две смены, 16 часов в сутки.
        '_-Работа бригады грузчиков (нормо-часов)':0.5,
        '_-Простой грузовой баржи (часов)':0.5 / 20 / (16/24),
        }

metadict_detail['_-Работы погрузочно-разгрузочные с барка (тонн)'] = {
        # TODO:
            # Добавить использование крана, ускорить процесс.
        # 20 грузчиков, экипаж следит.
        '_-Работа бригады грузчиков (нормо-часов)':0.5,
        '_-Простой грузового барка (часов)':0.5 / 20 / (16/24),
        }

metadict_detail['_-Работы погрузочно-разгрузочные с поезда (тонн)'] = {
        # 20 грузчиков, экипаж следит.
        '_-Работа бригады грузчиков (нормо-часов)':0.5,
        '_-Простой товарного поезда (часов)':0.5 / 20 / (16/24),
        }

metadict_detail['_-Работы погрузочно-разгрузочные с планёра (тонн)'] = {
        # 10 грузчиков, экипаж отдыхает.
        '_-Работа бригады грузчиков (нормо-часов)':0.5,
        '_-Простой грузового планёра (часов)':0.5 / 10 / (16/24),
        }

metadict_detail['_-Работы погрузочно-разгрузочные с телеги (тонн)'] = {
        # 2 грузчика, возничий помогает.
        '_-Работа бригады грузчиков (нормо-часов)':0.5,
        '_-Простой грузовой телеги (часов)':0.5 / 2 / (16/24),
        }

metadict_detail['_-Работы погрузочно-разгрузочные с телеги (Зебрика) (тонн)'] = {
        '_-Работа бригады грузчиков-зебр (нормо-часов)':0.5,
        '_-Простой грузовой телеги (часов)':0.5 / 2 / (16/24),
        }

metadict_detail['_-Работы погрузочно-разгрузочные с телеги вёдрами (тонн)'] = {
        '_-Работа водовоза (нормо-часов)':0.5,
        '_-Простой грузовой телеги (часов)':0.5 / 1 / (16/24),
        }

metadict_detail['_-Работы погрузочно-разгрузочные с телеги насосом (тонн)'] = {
        # насосы поршневые чугунные:
        # - насос всасывающий обыкновенный:
            # поршень 56 мм, 31 мм труба, 1200 литров/час -- 11 рублей
            # поршень 87 мм, 40 мм труба, 2400 литров/час -- 17 рублей
        '_-Работа водовоза (нормо-часов)':0.5,
        '_-Простой грузовой телеги (часов)':0.5 / 1 / (16/24),
        'Использование насоса 35 литров/минуту гидравлического (часов)':0.5,
        }

metadict_detail['_-Работы погрузочно-разгрузочные с телегой-самосвалом (тонн)'] = {
        # Наклонить телегу и сбросить песок-щебень-мусор. Это по силам и одному пегасу.
        '_-Работа грузчика (нормо-часов)':5 / 60,
        '_-Простой грузовой телеги (часов)':5 / 60,
        }

metadict_detail['_-Работы погрузочно-разгрузочные с тележки (тонн)'] = {
        # Возничий разгружает сам.
        '_-Работа грузчика (нормо-часов)':0.5,
        '_-Простой грузовой тележки (часов)':0.5 / 1 / (16/24),
        }

metadict_detail['_-Работы погрузочно-разгрузочные с тележки вёдрами (тонн)'] = {
        # Бадья, два ведра с коромыслом.
        # Это, получается, 33 литра/минуту, ~2000 литров/час.
        '_-Работа водовоза (нормо-часов)':0.5,
        '_-Простой грузовой тележки (часов)':0.5 / 1 / (16/24),
        }

metadict_detail['_-Работы погрузочно-разгрузочные с тележки насосом (тонн)'] = {
        '_-Работа водовоза (нормо-часов)':0.5,
        '_-Простой грузовой тележки (часов)':0.5 / 1 / (16/24),
        'Использование насоса 35 литров/минуту гидравлического (часов)':0.5,
        }

#----
# Транспортные средства (пассажирские):

metadict_detail['_-Путь лёгкого пассажирского планёра (часов/пассажир)'] = {
        # 2 пегаса. До 4 пассажиров, среднее заполнение 0.5
        '_-Путь лёгкого пассажирского планёра, 4 пассажира, 80 км/час, 60 кВт (часов)':1 / (4 * 0.5),
        '-Пассажирооборот воздушных путей (пассажиро-километров)':80,
        }

metadict_detail['_-Путь тяжёлого пассажирского планёра (часов/пассажир)'] = {
        # 18 пегасов. До 36 пассажиров, среднее заполнение 0.75
        '_-Путь тяжёлого пассажирского планёра, 36 пассажиров, 80 км/час, 540 кВт (часов)':1 / (36 * 0.75),
        '-Пассажирооборот воздушных путей (пассажиро-километров)':80,
        }

metadict_detail['_-Путь пассажирского поезда (часов/пассажир)'] = {
        # TODO: ты не учитываешь простой пассажирского поезда.
        # 36 мест/вагон, 8+2 вагонов/поезд, 288 пассажиров, заполнение 0.75
        '_-Путь пассажирского поезда, 288 пассажиров, 100 км/час, 710 кВт-час (часов)':1 / (288 * 0.75),
        '-Пассажирооборот железнодорожных путей (пассажиро-километров)':100,
        }

metadict_detail['_-Путь пассажирской баржи (часов/пассажир)'] = {
        # 108 пассажиров, заполнение 0.5
        '_-Путь пассажирской баржи, 108 пассажиров, 9 км/час, 240 кВт (часов)':1 / (108 * 0.5),
        '-Пассажирооборот речных путей (пассажиро-километров)':9,
        }

metadict_detail['_-Путь пассажирского барка (часов/пассажир)'] = {
        # TODO: лучше сделай яхты на 108 пассажиров.
        # 288 пассажиров, заполнение 0.75
        '_-Путь пассажирского барка, 288 пассажиров, 12.6 км/час, 720 кВт (часов)':1 / (288 * 0.75),
        '-Пассажирооборот морских путей (пассажиро-километров)':12.6,
        }

#----
# Транспортные средства (использование в пути):

metadict_detail['_-Путь лёгкого пассажирского планёра, 4 пассажира, 80 км/час, 60 кВт (часов)'] = {
        # Два пегаса, прежде всего для безопасности.
        '_Работа экипажа лёгкого пассажирского планёра, 4 пассажира, 80 км/час, 60 кВт (рабочих часов)':1,
        'Использование пассажирского планёра, 4 пассажира, 80 км/час, 60 кВт (часов)':1,
        '-Путь лёгкого пассажирского планёра, всего (километров)':80,
        }

metadict_detail['_-Путь лёгкого санитарного планёра, 4 пассажира, 80 км/час, 60 кВт (часов)'] = {
        '_Работа экипажа лёгкого санитарного планёра, 4 пассажира, 80 км/час, 60 кВт (рабочих часов)':1,
        'Использование санитарного планёра, 4 пассажира, 80 км/час, 60 кВт (часов)':1,
        '-Путь лёгкого санитарного планёра, всего (километров)':80,
        }

metadict_detail['_-Путь грузового планёра, 3 тонны, 80 км/час, 540 кВт (часов)'] = {
        # TODO:
            # Уменьшай экипаж до 4 пегасов
            # этому планёру достаточно 68 кВт в полёте. Толпа пегасов для отрыва от земли.
        # 18 пегасов.
        '_Работа экипажа грузового планёра, 3 тонны, 80 км/час, 540 кВт (рабочих часов)':1,
        'Использование грузового планёра, 3 тонны, 80 км/час, 540 кВт (часов)':1,
        '-Путь грузового планёра, всего (километров)':80,
        }

metadict_detail['_-Путь тяжёлого пассажирского планёра, 36 пассажиров, 80 км/час, 540 кВт (часов)'] = {
        '_Работа экипажа пассажирского планёра, 36 пассажиров, 80 км/час, 540 кВт (рабочих часов)':1,
        'Использование пассажирского планёра, 36 пассажиров, 80 км/час, 540 кВт (часов)':1,
        '-Путь тяжёлого пассажирского планёра, всего (километров)':80,
        }

metadict_detail['_-Путь грузового поезда, 250 тонн, 50 км/час 640 кВт-час (часов)'] = {
        '_Работа экипажа товарного поезда, 400 тонн, 50 км/час 640 кВт-час (рабочих часов)':1,
        'Использование товарного поезда, 400 тонн, 50 км/час 640 кВт-час (часов)':1,
        '-Путь грузового поезда, всего (километров)':50,
        }

metadict_detail['_-Путь пассажирского поезда, 288 пассажиров, 100 км/час, 710 кВт-час (часов)'] = {
        '_Работа экипажа пассажирского поезда, 288 пассажиров, 100 км/час 710 кВт-час (рабочих часов)':1,
        'Использование пассажирского поезда, 288 пассажиров, 100 км/час 710 кВт-час (часов)':1,
        '-Путь пассажирского поезда, всего (километров)':50,
        }

metadict_detail['_-Путь грузового барка, 1400 тонн, 12.6 км/час, 720 кВт (часов)'] = {
        # Барк идёт на парусах, а в штиль на силе пегасов.
            # Площадь парусов: 2600 м² (20 парусов: 10 прямых, 9 косых, один широкий гафель)
            # Длина такелажа — 30 000 метров.
            # https://ru.wikisource.org/wiki/ЭСБЕ/Парусность_баркаса
            # https://ru.wikisource.org/wiki/ЭСБЕ/Паруса
        # Грузовой барк:
            # Длина такелажа — 30 000 метров.
            # Диаметры стоячего такелажа (сталь) -- 12 мм, 14 мм, 19 мм, 24 мм, 27 мм
            # Диаметры бегущего такелажа (пенька) -- от 20 до 60 мм.
            # Диаметр основания грот-мачты -- 0.75 метра
        # Стоячий такелаж (30 000 × 0.3) / 50 = 180 тросов в среднем по 50 метров.
        '_Работа экипажа грузового барка, 1400 тонн, 12.6 км/час, 720 кВт (рабочих часов)':1,
        'Использование грузового барка, 1400 тонн, 12.6 км/час, 720 кВт (часов)':1,
        'Использование паруса морского судна (часов/квадратный метр)':3000,
        'Использование стоячего такелажа морского судна (часов/метр)':30000 * 0.3,
        'Использование бегущего такелажа морского судна (часов/метр)':30000 * 0.7,
        '-Путь грузового барка, всего (километров)':12.6,
        }

metadict_detail['_-Путь пассажирского барка, 288 пассажиров, 12.6 км/час, 720 кВт (часов)'] = {
        '_Работа экипажа пассажирского барка, 288 пассажиров, 12.6 км/час, 720 кВт (рабочих часов)':1,
        'Использование пассажирского барка, 288 пассажиров, 12.6 км/час, 720 кВт (часов)':1,
        'Использование паруса морского судна (часов/квадратный метр)':3000,
        'Использование стоячего такелажа морского судна (часов/метр)':30000 * 0.3,
        'Использование бегущего такелажа морского судна (часов/метр)':30000 * 0.7,
        '-Путь пассажирского барка, всего (километров)':12.6,
        }

metadict_detail['_-Путь грузовой баржи, 200 тонн, 9 км/час, 240 кВт (часов)'] = {
        # Безмачтовое судно. Тащат пегасы силой своих крыльев.
        '_Работа экипажа грузовой баржи, 200 тонн, 9 км/час, 240 кВт (рабочих часов)':1,
        'Использование грузовой баржи, 200 тонн, 9 км/час, 240 кВт (часов)':1,
        '-Путь грузовой баржи, всего (километров)':9,
        }

metadict_detail['_-Путь пассажирской баржи, 108 пассажиров, 9 км/час, 240 кВт (часов)'] = {
        '_Работа экипажа пассажирской баржи, 108 пассажиров, 9 км/час, 240 кВт (рабочих часов)':1,
        'Использование пассажирской баржи, 108 пассажиров, 9 км/час, 240 кВт (часов)':1,
        '-Путь пассажирской баржи, всего (километров)':9,
        }

metadict_detail['_-Путь грузовой телеги, 0.5 тонны, 20 км/час (часов)'] = {
        '_-Работа пегаса-возничего (нормо-часов)':1,
        'Использование телеги 0.5-тонной грузовой (часов)':1,
        '-Путь грузовой телеги, всего (километров)':20,
        }

metadict_detail['_-Путь грузовой телеги, 0.3 тонны, 5 км/час (Зебрика) (часов)'] = {
        '_-Работа зебры-возничего (нормо-часов)':1 * 2,
        'Использование телеги 0.5-тонной грузовой (часов)':1,
        '-Путь грузовой телеги, всего (километров)':5,
        }

metadict_detail['_-Путь грузовой телеги-самосвала, 0.5 тонны, 20 км/час (часов)'] = {
        '_-Работа пегаса-возничего (нормо-часов)':1,
        'Использование телеги 0.5-тонной грузовой (часов)':1,
        '-Путь грузовой телеги, всего (километров)':20,
        }

metadict_detail['_-Путь грузовой телеги-водовозки, 0.5 тонны, 20 км/час (часов)'] = {
        '_-Работа пегаса-водовоза (нормо-часов)':1,
        'Использование телеги 0.5-тонной грузовой (часов)':1,
        'Использование бочки 500-литровой для перевозки воды (часов)':1,
        '-Путь грузовой телеги, всего (километров)':20,
        }

metadict_detail['_-Путь грузовой тележки, 0.1 тонны, 5 км/час (часов)'] = {
        '_-Работа грузчика с тележкой (нормо-часов)':1,
        'Использование тележки 200-литровой грузовой (часов)':1,
        '-Путь грузовой тележки, всего (километров)':5,
        }

metadict_detail['_-Путь грузовой тележки, 0.1 тонны, 5 км/час (Зебрика) (часов)'] = {
        '_-Работа грузчика-зебры с тележкой (нормо-часов)':1,
        'Использование тележки 200-литровой грузовой (часов)':1,
        '-Путь грузовой тележки, всего (километров)':5,
        }

metadict_detail['_-Путь грузовой тележки-водовозки, 0.1 тонны, 5 км/час (часов)'] = {
        '_-Работа водовоза с тележкой (нормо-часов)':1,
        'Использование тележки 200-литровой грузовой (часов)':1,
        'Использование бочки 100-литровой для перевозки воды (часов)':1,
        '-Путь грузовой тележки, всего (километров)':5,
        }

#----
# Транспортные средства (простой, ожидание):

metadict_detail['_-Простой грузового планёра (часов)'] = {
        '_Работа экипажа грузового планёра, 3 тонны, 80 км/час, 540 кВт (рабочих часов)':1,
        'Использование грузового планёра, 3 тонны, 80 км/час, 540 кВт (часов)':1,
        '-Путь грузового планёра, всего (километров)':80,
        }

metadict_detail['_-Простой товарного поезда (часов)'] = {
        '_Работа экипажа товарного поезда, 400 тонн, 50 км/час 640 кВт-час (рабочих часов)':1,
        'Использование товарного поезда, 400 тонн, 50 км/час 640 кВт-час (часов)':1,
        }

metadict_detail['_-Простой грузового барка (часов)'] = {
        '_Работа экипажа грузового барка, 1400 тонн, 12.6 км/час, 720 кВт (рабочих часов)':1,
        'Использование грузового барка, 1400 тонн, 12.6 км/час, 720 кВт (часов)':1,
        'Использование паруса морского судна (часов/квадратный метр)':3000,
        'Использование стоячего такелажа морского судна (часов/метр)':30000 * 0.3,
        'Использование бегущего такелажа морского судна (часов/метр)':30000 * 0.7,
        }

metadict_detail['_-Простой грузовой баржи (часов)'] = {
        '_Работа экипажа грузовой баржи, 200 тонн, 9 км/час, 240 кВт (рабочих часов)':1,
        'Использование грузовой баржи, 200 тонн, 9 км/час, 240 кВт (часов)':1,
        }

metadict_detail['_-Простой грузовой телеги (часов)'] = {
        'Использование телеги 0.5-тонной грузовой (часов)':1,
        }

metadict_detail['_-Простой грузовой тележки (часов)'] = {
        'Использование тележки 200-литровой грузовой (часов)':1,
        }
