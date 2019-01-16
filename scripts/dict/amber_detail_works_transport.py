#----
# Транспортные стредства (погрузка-разгрузка):

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
        # Исправить
            # Добавить использование крана, ускорить процесс.
        # 20 грузчиков, экипаж следит.
        '_-Работа бригады грузчиков (нормо-часов)':0.5,
        '_-Простой грузового барка (часов)':0.5 / 20 / (16/24),
        }

metadict_detail['_-Работы погрузочно-разгрузочные с поезда (тонн)'] = {
        # 20 грузчиков, экипаж следит.
        '_-Работа бригады грузчиков (нормо-часов)':0.5,
        '_-Простой грузового поезда (часов)':0.5 / 20 / (16/24),
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

metadict_detail['_-Работы погрузочно-разгрузочные с телеги насосом (тонн)'] = {
        # Исправить
            # Добавь использование насоса. Грузчики не нужны.
        '_-Работа бригады грузчиков (нормо-часов)':0.5,
        '_-Простой грузовой телеги (часов)':0.5 / 2 / (16/24),
        }

metadict_detail['_-Работы погрузочно-разгрузочные с телегой-самосвалом (тонн)'] = {
        # Наклонить телегу и сбросить песок-щебень-мусор. Это по силам и одному пегасу.
        '_-Простой грузовой телеги (часов)':0.1,
        }

metadict_detail['_-Работы погрузочно-разгрузочные с тележки (тонн)'] = {
        # Возничий разгружает сам.
        '_-Работа грузчика (нормо-часов)':0.5,
        '_-Простой грузовой тележки (часов)':0.5 / 1 / (16/24),
        }

metadict_detail['_-Работы погрузочно-разгрузочные с тележки вёдрами (тонн)'] = {
        # Исправить
            # Это, получается, 33 литра/минуту.
            # Бадья, два ведра с коромыслом, или механический насос.
        '_-Работа грузчика (нормо-часов)':0.5,
        '_-Простой грузовой тележки (часов)':0.5 / 1 / (16/24),
        }

#----
# Транспортные стредства (использование в пути):

metadict_detail['_-Путь грузового планёра (часов)'] = {
        '_-Работа экипажа грузового планёра (нормо-часов)':1,
        'Использование грузового планёра 18-пегасного (часов)':1,
        }

metadict_detail['_-Путь грузового поезда (часов)'] = {
        '_-Работа экипажа грузового поезда (нормо-часов)':1,
        'Использование грузового поезда 25-вагонного 18-пегасного (часов)':1,
        }

metadict_detail['_-Путь грузового барка (часов)'] = {
        '_-Работа экипажа грузового барка (нормо-часов)':1,
        'Использование грузового барка 3000-тонного 24-пегасного (часов)':1,
        }

metadict_detail['_-Путь грузовой баржи (часов)'] = {
        '_-Работа экипажа грузовой баржи (нормо-часов)':1,
        'Использование грузовой баржи 400-тонной 8-пегасной (часов)':1,
        }

metadict_detail['_-Путь грузовой телеги (часов)'] = {
        # Одноконная телега ППО-55
        # http://sinref.ru/000_uchebniki/03400metalurg/002_kolhozni_kuznec_medvukov_1958/128.htm
        '_-Работа пегаса-возничего (нормо-часов)':1,
        'Использование телеги 0.5-тонной грузовой (часов)':1,
        }

metadict_detail['_-Путь грузовой телеги-самосвала (часов)'] = {
        '_-Работа пегаса-возничего (нормо-часов)':1,
        'Использование телеги 0.5-тонной грузовой (часов)':1,
        }

metadict_detail['_-Путь грузовой телеги-водовозки (часов)'] = {
        '_-Работа пегаса-возничего (нормо-часов)':1,
        'Использование телеги 0.5-тонной грузовой (часов)':1,
        'Использование бочки 500-литровой для перевозки воды (часов)':1,
        }

metadict_detail['_-Путь грузовой тележки (часов)'] = {
        '_-Работа грузчика с тележкой (нормо-часов)':1,
        'Использование тележки 200-литровой грузовой (часов)':1,
        }

metadict_detail['_-Путь грузовой тележки-водовозки (часов)'] = {
        '_-Работа грузчика с тележкой (нормо-часов)':1,
        'Использование тележки 200-литровой грузовой (часов)':1,
        'Использование бочки 100-литровой для перевозки воды (часов)':1,
        }

#----
# Транспортные стредства (простой, ожидание):

metadict_detail['_-Простой грузового планёра (часов)'] = {
        '_-Работа экипажа грузового планёра (нормо-часов)':1,
        'Использование грузового планёра 18-пегасного (часов)':1,
        }

metadict_detail['_-Простой грузового поезда (часов)'] = {
        '_-Работа экипажа грузового поезда (нормо-часов)':1,
        'Использование грузового поезда 25-вагонного 18-пегасного (часов)':1,
        }

metadict_detail['_-Простой грузового барка (часов)'] = {
        '_-Работа экипажа грузового барка (нормо-часов)':1,
        'Использование грузового барка 3000-тонного 24-пегасного (часов)':1,
        }

metadict_detail['_-Простой грузовой баржи (часов)'] = {
        '_-Работа экипажа грузовой баржи (нормо-часов)':1,
        'Использование грузовой баржи 400-тонной 8-пегасной (часов)':1,
        }

metadict_detail['_-Простой грузовой телеги (часов)'] = {
        'Использование телеги 0.5-тонной грузовой (часов)':1,
        }

metadict_detail['_-Простой грузовой тележки (часов)'] = {
        'Использование тележки 200-литровой грузовой (часов)':1,
        }