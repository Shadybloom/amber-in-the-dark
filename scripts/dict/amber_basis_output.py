#----
# Обжитые земли: 

metadict_detail['|----Обжитые земли (гектар)'] = {
        # Определяем радиус круга полей:
        # Например, Понивиль (38.4 кв.километров)
        # (38.4 / 3.14159265) ** (1/2) = 3.496155 километра
        '|----Обжитые земли (квадратный километр)':1 / 100,
        #'|----Обжитые земли (радиус, километр)':'(x / 100 / 3.14159265) ** (1/2)',
        '|----Обжитые земли (радиус, километр)':[
            '(x / 3.14159265) ** (1/2)',
            '|----Обжитые земли (квадратный километр)',
            ],
        # Иногда полезно:
        '|----Обжитые земли (радиус, метр)':[
            '((x * 10000) / 3.14159265) ** (1/2)',
            '|----Обжитые земли (гектар)',
            ],
        # Периметр круга: P=2*Pi*r
        # Границы реальных государств требуют коэффициента: 0.24 (Россия) - 0.35 (США)
        '|----Обжитые земли (периметр, километр)':[
            '2 * 3.14159265 * (x / 3.14159265) ** (1/2)',
            '|----Обжитые земли (квадратный километр)',
            ],
        # Плотность населения:
        #'+++++--Население (пони/квадратный километр)':[
        #    'x / y',
        #    '++++ Население',
        #    '|----Обжитые земли (квадратный километр)',
        #    ],
        }

metadict_detail['|----Обжитые земли (радиус, метр)'] = {
        }

#----
# Обжитые земли: 

#metadict_detail['|---Леса (гектар)'] = {
#        # Процент от площади обжитых земель.
#        '|---Леса (%)':[
#            '(value / x) * 100',
#            '|----Обжитые земли (гектар)',
#            ],
#        }
#
#metadict_detail['|---Луга (гектар)'] = {
#        '|---Луга (%)':[
#            '(value / x) * 100',
#            '|----Обжитые земли (гектар)',
#            ],
#        }
#
#metadict_detail['|---Огороды (гектар)'] = {
#        '|---Огороды (%)':[
#            '(value / x) * 100',
#            '|----Обжитые земли (гектар)',
#            ],
#        }
#
#metadict_detail['|---Пашня (гектар)'] = {
#        '|---Пашня (%)':[
#            '(value / x) * 100',
#            '|----Обжитые земли (гектар)',
#            ],
#        }
#
#metadict_detail['|---Плантации (гектар)'] = {
#        '|---Плантации (%)':[
#            '(value / x) * 100',
#            '|----Обжитые земли (гектар)',
#            ],
#        }
#
#metadict_detail['|---Сады (гектар)'] = {
#        '|---Сады (%)':[
#            '(value / x) * 100',
#            '|----Обжитые земли (гектар)',
#            ],
#        }
#
#metadict_detail['|--Усадьбы (гектар)'] = {
#        '|---Усадьбы (%)':[
#            '(value / x) * 100',
#            '|----Обжитые земли (гектар)',
#            ],
#        }

#----
# Население (расы):

metadict_detail['++-- Пегасы'] = {
        # Процент от численности населения:
        '++-- Пегасы (%)':[
            '(value / x) * 100',
            '++++ Население',
            ],
        }

metadict_detail['++-- Единороги'] = {
        '++-- Единороги (%)':[
            '(value / x) * 100',
            '++++ Население',
            ],
        }

metadict_detail['++-- Земнопони'] = {
        '++-- Земнопони (%)':[
            '(value / x) * 100',
            '++++ Население',
            ],
        }

#----
# Население (классы):

metadict_detail['--Бедняки'] = {
        # Процент от численности населения:
        '+++- Бедняки (%)':[
            '(value / x) * 100',
            '++++ Население',
            ],
        }

metadict_detail['--Богатеи'] = {
        # Процент от численности населения:
        '+++- Богатеи (%)':[
            '(value / x) * 100',
            '++++ Население',
            ],
        }

metadict_detail['--Середняки'] = {
        # Процент от численности населения:
        '+++- Середняки (%)':[
            '(value / x) * 100',
            '++++ Население',
            ],
        }

metadict_detail['--Единороги бедняки'] = {
        # Процент от численности населения:
        '++-- Единороги бедняки (%)':[
            '(value / x) * 100',
            '++-- Единороги',
            #'++++ Население',
            ],
        }

metadict_detail['--Единороги богатеи'] = {
        '++-- Единороги богатеи (%)':[
            '(value / x) * 100',
            '++-- Единороги',
            #'++++ Население',
            ],
        }

metadict_detail['--Единороги середняки'] = {
        '++-- Единороги середняки (%)':[
            '(value / x) * 100',
            '++-- Единороги',
            #'++++ Население',
            ],
        }

metadict_detail['--Земнопони бедняки'] = {
        '++-- Земнопони бедняки (%)':[
            '(value / x) * 100',
            '++-- Земнопони',
            #'++++ Население',
            ],
        }

metadict_detail['--Земнопони богатеи'] = {
        '++-- Земнопони богатеи (%)':[
            '(value / x) * 100',
            '++-- Земнопони',
            #'++++ Население',
            ],
        }

metadict_detail['--Земнопони середняки'] = {
        '++-- Земнопони середняки (%)':[
            '(value / x) * 100',
            '++-- Земнопони',
            #'++++ Население',
            ],
        }

metadict_detail['--Пегасы бедняки'] = {
        '++-- Пегасы бедняки (%)':[
            '(value / x) * 100',
            '++-- Пегасы',
            #'++++ Население',
            ],
        }

metadict_detail['--Пегасы богатеи'] = {
        '++-- Пегасы богатеи (%)':[
            '(value / x) * 100',
            '++-- Пегасы',
            #'++++ Население',
            ],
        }

metadict_detail['--Пегасы середняки'] = {
        '++-- Пегасы середняки (%)':[
            '(value / x) * 100',
            '++-- Пегасы',
            #'++++ Население',
            ],
        }

#----
# Население (поселения):

metadict_detail['+--1 Жители мегаполисов'] = {
        '+--1 Жители мегаполисов (%)':[
            '(value / x) * 100',
            '++++ Население',
            ],
        }

metadict_detail['+--2 Жители городов'] = {
        '+--2 Жители городов (%)':[
            '(value / x) * 100',
            '++++ Население',
            ],
        }

metadict_detail['+--3 Жители городков'] = {
        '+--3 Жители городков (%)':[
            '(value / x) * 100',
            '++++ Население',
            ],
        }

metadict_detail['+--4 Жители селений'] = {
        '+--4 Жители селений (%)':[
            '(value / x) * 100',
            '++++ Население',
            ],
        }

metadict_detail['+--5 Жители деревень'] = {
        '+--5 Жители деревень (%)':[
            '(value / x) * 100',
            '++++ Население',
            ],
        }

metadict_detail['+--6 Жители ферм'] = {
        '+--6 Жители ферм (%)':[
            '(value / x) * 100',
            '++++ Население',
            ],
        }

#----

metadict_detail['+--1 Жители мегаполисов (%)'] = {
        }

metadict_detail['+--2 Жители городов (%)'] = {
        }

metadict_detail['+--3 Жители городков (%)'] = {
        }

metadict_detail['+--4 Жители селений (%)'] = {
        }

metadict_detail['+--5 Жители деревень (%)'] = {
        }

metadict_detail['+--6 Жители ферм (%)'] = {
        }

#----

metadict_detail['++-- Единороги (%)'] = {
        }

metadict_detail['++-- Земнопони (%)'] = {
        }

metadict_detail['++-- Пегасы (%)'] = {
        }

metadict_detail['+++- Бедняки (%)'] = {
        }

metadict_detail['+++- Богатеи (%)'] = {
        }

metadict_detail['+++- Середняки (%)'] = {
        }

metadict_detail['++-- Единороги бедняки (%)'] = {
        }

metadict_detail['++-- Единороги богатеи (%)'] = {
        }

metadict_detail['++-- Единороги середняки (%)'] = {
        }

metadict_detail['++-- Земнопони бедняки (%)'] = {
        }

metadict_detail['++-- Земнопони богатеи (%)'] = {
        }

metadict_detail['++-- Земнопони середняки (%)'] = {
        }

metadict_detail['++-- Пегасы бедняки (%)'] = {
        }

metadict_detail['++-- Пегасы богатеи (%)'] = {
        }

metadict_detail['++-- Пегасы середняки (%)'] = {
        }

#----
# Административное деление:

metadict_detail['---1 Мегаполисы'] = {
        }

metadict_detail['-----Округа'] = {
        }

metadict_detail['----Кантоны'] = {
        }

metadict_detail['---2 Города'] = {
        }

metadict_detail['---3 Городки'] = {
        }

metadict_detail['---5 Деревни'] = {
        }

metadict_detail['---4 Селения'] = {
        }

metadict_detail['---6 Фермы'] = {
        }

#----
# Убираем лишние параметры из вывода (их можно вызвать по ключу -e)

metadict_detail['-Уксусная кислота (грамм)'] = {
        }

metadict_detail['-Масло растительное (килограмм)'] = {
        }

metadict_detail['--Питательные вещества (грамм)'] = {
        }

metadict_detail['|-Сосновая вырубка (гектар)'] = {
        }

metadict_detail['|--Дровяные деревья'] = {
        }

metadict_detail['|--Прутовые деревья'] = {
        }

metadict_detail['|--Строевые деревья'] = {
        }

metadict_detail['|--Плодовые деревья'] = {
        }

#----
# Складские помещения.

metadict_detail['-Площадь амбара (квадратный метр)'] = {
        '--Площадь складских помещений (квадратный метр)':1,
        }

metadict_detail['-Площадь полуподвала (квадратный метр)'] = {
        '--Площадь складских помещений (квадратный метр)':1,
        }

metadict_detail['-Площадь погреба (квадратный метр)'] = {
        '--Площадь складских помещений (квадратный метр)':1,
        }

metadict_detail['-Площадь ледника (квадратный метр)'] = {
        '--Площадь складских помещений (квадратный метр)':1,
        }

metadict_detail['-Площадь чердака (квадратный метр)'] = {
        '--Площадь складских помещений (квадратный метр)':1,
        }

metadict_detail['--Площадь складских помещений (квадратный метр)'] = {
        }

metadict_detail['-Площадь жилых помещений (квадратный метр)'] = {
        }

metadict_detail['-Площадь общественных помещений (квадратный метр)'] = {
        }

metadict_detail['-Площадь хозяйственных помещений (квадратный метр)'] = {
        }

metadict_detail['-Объём помещений (кубометр)'] = {
        }

metadict_detail['|==Зерновые (литр)'] = {
        # Сравниваем со статистикой 19 века.
        # Четверть зерна = 209 литров
        }

#----
# Грузонапряжённость путей
    # TODO: таки почему так мало используются железные дороги?

metadict_detail['|===Грузонапряжённость городских дорог (тонн)'] = {
        }

metadict_detail['|===Грузонапряжённость железных дорог (тонн)'] = {
        }

metadict_detail['|===Грузонапряжённость морских путей (тонн)'] = {
        }

metadict_detail['|===Грузонапряжённость речных путей (тонн)'] = {
        }

metadict_detail['|===Грузонапряжённость воздушных путей (тонн)'] = {
        }

metadict_detail['|===Грузонапряжённость сельских дорог (тонн)'] = {
        }

metadict_detail['|===Грузонапряжённость шоссейных дорог (тонн)'] = {
        }

#----
# Возможности путей:

metadict_detail['-Предельный грузооборот шоссейных дорог (тонно-километров)'] = {
        }

metadict_detail['-Предельный грузооборот грунтовых дорог (тонно-километров)'] = {
        }

#----
# Площадь распила
    # TODO: так мы будем вычислять затраты энергии и труда на обработку древесины

metadict_detail['-Распил пиломатериалов (квадратный метр)'] = {
        }

#----
# Смазочные материлы

metadict_detail['-Колёсная мазь (требуется/килограмм)'] = {
        }

#----
# Предполагаемый вес тары:

metadict_detail['-Тарные бочки (килограмм)'] = {
        # TODO: Пили производство тары.
        }

metadict_detail['-Тарные горшки (килограмм)'] = {
        }

metadict_detail['-Тарные корзины (килограмм)'] = {
        }

metadict_detail['-Тарные мешки (килограмм)'] = {
        }

metadict_detail['-Тарные ящики (килограмм)'] = {
        }

metadict_detail['-Тарные банки (килограмм)'] = {
        }

#----
# Площадь поселений:

metadict_detail['|-Усадьба (квадратный метр)'] = {
        # TODO: Перенеси, хм, к планам поселений (которых пока нет).
        '|--Усадьбы (гектар)':1 / 10000,
        }

#----
# Расчёты отопления:

metadict_detail['-Объём помещений (кубометр)'] = {
        # На каждый кубометр утеплённого помещения требуется 40 ватт зимой
        '--Необходимо отопление (киловатт)':0.04,
        }

metadict_detail['--Необходимо отопление (киловатт)'] = {
        }

#----
# Показатели водопровода:

metadict_detail['-Расход воды (литр)'] = {
        }

metadict_detail['-Очистка воды (кубометров/сутки)'] = {
        # 250 литров в сутки. Много на самом деле.
        '--Очистка воды (пони)':1 / 0.25,
        }

metadict_detail['--Очистка воды (пони)'] = {
        }

metadict_detail['-Хранение питьевой воды (кубометров)'] = {
        # Должно обеспечивать 40% суточной потребности в воде.
        '--Хранение питьевой воды (пони)':1 / 0.25 / 0.4,
        }

metadict_detail['--Хранение питьевой воды (пони)'] = {
        }

#----
# Возобновляемые ресурсы (лесные):

metadict_detail['+Валежник (доступно/кубометр)'] = {
        '+Валежник (%)':[
            '(value / x) * 100',
            '-Валежник (требуется/кубометр)',
            ],
        }

metadict_detail['-Валежник (требуется/килограмм)'] = {
        '-Валежник (требуется/кубометр)':1 / 200,
        }

metadict_detail['-Валежник (требуется/кубометр)'] = {
        }

metadict_detail['+Сок кленовый (доступно/килограмм)'] = {
        '+Сок кленовый (%)':[
            '(value / x) * 100',
            '-Сок кленовый (требуется/килограмм)',
            ],
        }

metadict_detail['-Сок кленовый (требуется/килограмм)'] = {
        }

metadict_detail['+Дикорастущие грибы (доступно/килограмм)'] = {
        '+Дикорастущие грибы (%)':[
            '(value / x) * 100',
            '-Дикорастущие грибы (требуется/килограмм)',
            ],
        }

metadict_detail['-Дикорастущие грибы (требуется/килограмм)'] = {
        }

metadict_detail['+Дикорастущие орехи (каштан) (доступно/килограмм)'] = {
        }

metadict_detail['+Дикорастущие орехи (пекан) (доступно/килограмм)'] = {
        }

metadict_detail['-Дикорастущие орехи (требуется/килограмм)'] = {
        }

metadict_detail['+Дикорастущие растения (доступно/килограмм)'] = {
        '+Дикорастущие растения (%)':[
            '(value / x) * 100',
            '-Дикорастущие растения (требуется/килограмм)',
            ],
        }

metadict_detail['-Дикорастущие растения (требуется/килограмм)'] = {
        }

metadict_detail['+Дикорастущие ягоды (доступно/килограмм)'] = {
        '+Дикорастущие ягоды (%)':[
            '(value / x) * 100',
            '-Дикорастущие ягоды (требуется/килограмм)',
            ],
        }

metadict_detail['-Дикорастущие ягоды (требуется/килограмм)'] = {
        }

#----
# Возобновляемые ресурсы (площади):

metadict_detail['+Луга дикоросов (доступно/гектар)'] = {
        '+Луга дикоросов (%)':[
            '(value / x) * 100',
            '-Луга дикоросов (требуется/гектар)',
            ],
        }

metadict_detail['-Луга дикоросов (требуется/гектар)'] = {
        }

metadict_detail['+Луга медоносов (доступно/гектар)'] = {
        '+Луга медоносов (%)':[
            '(value / x) * 100',
            '-Луга медоносов (требуется/гектар)',
            ],
        }

metadict_detail['-Луга медоносов (требуется/гектар)'] = {
        }

#----
# Побочные продукты:

metadict_detail['+Солома гречишная (доступно/килограмм)'] = {
        '++Солома сухая (доступно/килограмм)':1,
        }

metadict_detail['+Солома овсяная (доступно/килограмм)'] = {
        '++Солома сухая (доступно/килограмм)':1,
        }

metadict_detail['+Солома просяная (доступно/килограмм)'] = {
        '++Солома сухая (доступно/килограмм)':1,
        }

metadict_detail['+Солома пшеничная (доступно/килограмм)'] = {
        '++Солома сухая (доступно/килограмм)':1,
        }

metadict_detail['+Солома ржаная (доступно/килограмм)'] = {
        '++Солома сухая (доступно/килограмм)':1,
        }

metadict_detail['+Солома рисовая (доступно/килограмм)'] = {
        '++Солома сухая (доступно/килограмм)':1,
        }

metadict_detail['+Солома ячменная (доступно/килограмм)'] = {
        '++Солома сухая (доступно/килограмм)':1,
        }

metadict_detail['+Мякина гречишная (доступно/килограмм)'] = {
        '++Мякина сухая (доступно/килограмм)':1,
        }

metadict_detail['+Мякина овсяная (доступно/килограмм)'] = {
        '++Мякина сухая (доступно/килограмм)':1,
        }

metadict_detail['+Мякина пшеничная (доступно/килограмм)'] = {
        '++Мякина сухая (доступно/килограмм)':1,
        }

metadict_detail['+Мякина ржаная (доступно/килограмм)'] = {
        '++Мякина сухая (доступно/килограмм)':1,
        }

metadict_detail['+Мякина ячменная (доступно/килограмм)'] = {
        '++Мякина сухая (доступно/килограмм)':1,
        }

metadict_detail['+Мякина просяная (доступно/килограмм)'] = {
        '++Мякина сухая (доступно/килограмм)':1,
        }

metadict_detail['+Мякина рисовая (доступно/килограмм)'] = {
        '++Мякина сухая (доступно/килограмм)':1,
        }

metadict_detail['+Жмых арахисовый (доступно/килограмм)'] = {
        '++Жмых (доступно/килограмм)':1,
        }

metadict_detail['+Жмых конопляный (доступно/килограмм)'] = {
        '++Жмых (доступно/килограмм)':1,
        }

metadict_detail['+Жмых кунжутный (доступно/килограмм)'] = {
        '++Жмых (доступно/килограмм)':1,
        }

metadict_detail['+Жмых льняной (доступно/килограмм)'] = {
        '++Жмых (доступно/килограмм)':1,
        }

metadict_detail['+Жмых подсолнечный (доступно/килограмм)'] = {
        '++Жмых (доступно/килограмм)':1,
        }

metadict_detail['+Бульон бобовый (доступно/килограмм)'] = {
        '+Бульон бобовый (%)':[
            '(value / x) * 100',
            '-Бульон бобовый (требуется/килограмм)',
            ],
        }

metadict_detail['-Бульон бобовый (требуется/килограмм)'] = {
        }

metadict_detail['+Бульон грибной (доступно/килограмм)'] = {
        '+Бульон грибной (%)':[
            '(value / x) * 100',
            '-Бульон грибной (требуется/килограмм)',
            ],
        }

metadict_detail['-Бульон грибной (требуется/килограмм)'] = {
        }

metadict_detail['+Зола (доступно/килограмм)'] = {
        '+Зола (%)':[
            '(value / x) * 100',
            '-Зола (требуется/килограмм)',
            ],
        }

metadict_detail['-Зола (требуется/килограмм)'] = {
        }

metadict_detail['-Мезга яблочная (требуется/килограмм)'] = {
        }

metadict_detail['-Мезга лимонная (требуется/килограмм)'] = {
        }

metadict_detail['-Рассол свекольный (требуется/килограмм)'] = {
        }

metadict_detail['-Рассол огуречный (требуется/килограмм)'] = {
        }

metadict_detail['-Ботва свекольная (требуется/килограмм)'] = {
        }

metadict_detail['-Ботва морковная (требуется/килограмм)'] = {
        }

metadict_detail['+Мезга овощная (доступно/килограмм)'] = {
        '+Пищевые отходы овощные (доступно/килограмм)':1,
        }

metadict_detail['+Мезга оливковая (доступно/килограмм)'] = {
        '+Пищевые отходы фруктовые (доступно/килограмм)':1,
        }

metadict_detail['+Мезга виноградная (доступно/килограмм)'] = {
        '+Пищевые отходы фруктовые (доступно/килограмм)':1,
        }

metadict_detail['+Мезга вишнёвая (доступно/килограмм)'] = {
        '+Пищевые отходы фруктовые (доступно/килограмм)':1,
        }

metadict_detail['+Мезга клюквенная (доступно/килограмм)'] = {
        '+Пищевые отходы фруктовые (доступно/килограмм)':1,
        }

metadict_detail['+Мезга гранатовая (доступно/килограмм)'] = {
        '+Пищевые отходы фруктовые (доступно/килограмм)':1,
        }

metadict_detail['+Мезга лимонная (доступно/килограмм)'] = {
        '+Пищевые отходы фруктовые (доступно/килограмм)':1,
        }

metadict_detail['+Мезга ревеня (доступно/килограмм)'] = {
        '+Пищевые отходы овощные (доступно/килограмм)':1,
        }

metadict_detail['+Мезга томатная (доступно/килограмм)'] = {
        '+Пищевые отходы овощные (доступно/килограмм)':1,
        }

metadict_detail['+Мезга яблочная (доступно/килограмм)'] = {
        '+Пищевые отходы фруктовые (доступно/килограмм)':1,
        }

metadict_detail['+Отруби бобовые (доступно/килограмм)'] = {
        '+Пищевые отходы бобовые (доступно/килограмм)':1,
        }

metadict_detail['+Отруби кукурузные (доступно/килограмм)'] = {
        '+Пищевые отходы зерновые (доступно/килограмм)':1,
        }

metadict_detail['+Отруби гречневые (доступно/килограмм)'] = {
        '++Отруби зерновые (доступно/килограмм)':1,
        }

metadict_detail['+Отруби овсяные (доступно/килограмм)'] = {
        '++Отруби зерновые (доступно/килограмм)':1,
        }

metadict_detail['+Отруби просяные (доступно/килограмм)'] = {
        '++Отруби зерновые (доступно/килограмм)':1,
        }

metadict_detail['+Отруби пшеничные (доступно/килограмм)'] = {
        '++Отруби зерновые (доступно/килограмм)':1,
        }

metadict_detail['+Отруби ржаные (доступно/килограмм)'] = {
        '++Отруби зерновые (доступно/килограмм)':1,
        }

metadict_detail['+Отруби рисовые (доступно/килограмм)'] = {
        '++Отруби зерновые (доступно/килограмм)':1,
        }

metadict_detail['+Отруби ячменные (доступно/килограмм)'] = {
        '++Отруби зерновые (доступно/килограмм)':1,
        }

metadict_detail['+Початки кукурузные пустые (доступно/килограмм)'] = {
        '++Отруби зерновые (доступно/килограмм)':1,
        }

metadict_detail['+Маринад грибной (доступно/килограмм)'] = {
        '+Маринад (доступно/килограмм)':1,
        }

metadict_detail['+Маринад оливковый (доступно/килограмм)'] = {
        '+Маринад (доступно/килограмм)':1,
        }

metadict_detail['+Маринад морковный (доступно/килограмм)'] = {
        '+Маринад (доступно/килограмм)':1,
        }

metadict_detail['+Маринад овощной (доступно/килограмм)'] = {
        '+Маринад (доступно/килограмм)':1,
        }

metadict_detail['+Рассол кабачковый (доступно/килограмм)'] = {
        '+Рассол (доступно/килограмм)':1,
        }

metadict_detail['+Рассол капустный (доступно/килограмм)'] = {
        '+Рассол (доступно/килограмм)':1,
        }

metadict_detail['+Рассол овощной (доступно/килограмм)'] = {
        '+Рассол (доступно/килограмм)':1,
        }

metadict_detail['+Рассол грибной (доступно/килограмм)'] = {
        '+Рассол (доступно/килограмм)':1,
        }

metadict_detail['+Рассол огуречный (доступно/килограмм)'] = {
        '+Рассол (доступно/килограмм)':1,
        }

metadict_detail['+Рассол репяный (доступно/килограмм)'] = {
        '+Рассол (доступно/килограмм)':1,
        }

metadict_detail['+Рассол свекольный (доступно/килограмм)'] = {
        '+Рассол (доступно/килограмм)':1,
        }

metadict_detail['+Рассол томатный (доступно/килограмм)'] = {
        '+Рассол (доступно/килограмм)':1,
        }

metadict_detail['+Рассол фруктовый (доступно/килограмм)'] = {
        '+Рассол (доступно/килограмм)':1,
        }

metadict_detail['+Сусло виноградное (доступно/килограмм)'] = {
        '+Сусло (доступно/килограмм)':1,
        }

metadict_detail['+Сусло вишнёвое (доступно/килограмм)'] = {
        '+Сусло (доступно/килограмм)':1,
        }

metadict_detail['+Сусло грушевое (доступно/килограмм)'] = {
        '+Сусло (доступно/килограмм)':1,
        }

metadict_detail['+Сусло квасное (доступно/килограмм)'] = {
        '+Сусло (доступно/килограмм)':1,
        }

metadict_detail['+Сусло соевое (доступно/килограмм)'] = {
        '+Сусло (доступно/килограмм)':1,
        }

metadict_detail['+Сусло яблочное (доступно/килограмм)'] = {
        '+Сусло (доступно/килограмм)':1,
        }

metadict_detail['+Масло снятое (доступно/килограмм)'] = {
        # От фритюра, от бульона на обжаренных овощах
        }

metadict_detail['-Бумага газетная старая (требуется/квадратный метр)'] = {
        }

#----
# Мусор, компост:

metadict_detail['+Маринад (доступно/килограмм)'] = {
        }

metadict_detail['+Рассол (доступно/килограмм)'] = {
        }

metadict_detail['+Сусло (доступно/килограмм)'] = {
        '++Пищевые отходы (доступно/килограмм)':1,
        }

metadict_detail['+Пищевые отходы грибные (доступно/килограмм)'] = {
        '++Пищевые отходы (доступно/килограмм)':1,
        }

metadict_detail['+Пищевые отходы корнеплодов (доступно/килограмм)'] = {
        '++Пищевые отходы (доступно/килограмм)':1,
        }

metadict_detail['+Пищевые отходы овощные (доступно/килограмм)'] = {
        '++Пищевые отходы (доступно/килограмм)':1,
        }

metadict_detail['+Пищевые отходы ореховые (доступно/килограмм)'] = {
        '++Пищевые отходы (доступно/килограмм)':1,
        }

metadict_detail['+Пищевые отходы травяные (доступно/килограмм)'] = {
        '++Пищевые отходы (доступно/килограмм)':1,
        }

metadict_detail['+Пищевые отходы фруктовые (доступно/килограмм)'] = {
        '++Пищевые отходы (доступно/килограмм)':1,
        }

metadict_detail['+Пищевые отходы бобовые (доступно/килограмм)'] = {
        '++Пищевые отходы (доступно/килограмм)':1,
        }

metadict_detail['+Пищевые отходы зерновые (доступно/килограмм)'] = {
        '++Пищевые отходы (доступно/килограмм)':1,
        }

metadict_detail['++Отруби зерновые (доступно/килограмм)'] = {
        '++Отруби зерновые (%)':[
            '(value / x) * 100',
            '-Отруби зерновые (требуется/килограмм)',
            ],
        }

metadict_detail['-Отруби зерновые (требуется/килограмм)'] = {
        }


#----

metadict_detail['++Пищевые отходы (доступно/килограмм)'] = {
        # TODO: Уточни плотность в компостной яме.
        '++Пищевые отходы (доступно/кубометр)':1 / 700,
        }

metadict_detail['++Солома сухая (доступно/килограмм)'] = {
        '++Солома сухая (доступно/кубометр)':1 / 50,
        }

metadict_detail['++Мякина сухая (доступно/килограмм)'] = {
        '++Мякина сухая (доступно/кубометр)':1 / 50,
        }

metadict_detail['-Солома сухая (требуется/килограмм)'] = {
        '-Солома сухая (требуется/кубометр)':1 / 50,
        }

metadict_detail['++Пищевые отходы (доступно/кубометр)'] = {
        }

metadict_detail['-Солома сухая (требуется/кубометр)'] = {
        }

metadict_detail['-Опилки древесные (требуется/кубометр)'] = {
        }

metadict_detail['+Опилки древесные (доступно/кубометр)'] = {
        '++Опилки древесные (%)':[
            '(value / x) * 100',
            '-Опилки древесные (требуется/кубометр)',
            ],
        }

metadict_detail['+Вырубленные леса (доступно/гектар)'] = {
        }

metadict_detail['+Солома на растопку (доступно/килограмм)'] = {
        '++Солома на растопку (%)':[
            '(value / x) * 100',
            '-Солома на растопку (требуется/килограмм)',
            ],
        }

metadict_detail['-Солома на растопку (требуется/килограмм)'] = {
        }

metadict_detail['++Солома сухая (доступно/кубометр)'] = {
        '++Солома сухая (%)':[
            '(value / x) * 100',
            '-Солома сухая (требуется/кубометр)',
            ],
        }

metadict_detail['++Мякина сухая (доступно/кубометр)'] = {
        }

metadict_detail['++Жмых (доступно/килограмм)'] = {
        '++Жмых (доступно/тонн)':1 / 1000,
        '++Жмых (%)':[
            '(value / x) * 100',
            '-Жмых (требуется/килограмм)',
            ],
        }

metadict_detail['-Жмых (требуется/килограмм)'] = {
        }

metadict_detail['++Жмых (доступно/тонн)'] = {
        '++Жмых (доступно/кубометр)':2,
        }

metadict_detail['++Жмых (доступно/кубометр)'] = {
        }

#----
# Побочные продукты (утилизация):

metadict_army['+Вата техническая (доступно/кубометр)'] = {
        '+Вата техническая (доступно/килограмм)':25,
        }

metadict_army['+Вата техническая (доступно/килограмм)'] = {
        }

metadict_army['+Резина вулканизированная (доступно/килограмм)'] = {
        }

metadict_army['+Ткань кирзовая (доступно/килограмм)'] = {
        }

metadict_army['+Ткань льняная, лоскуты (доступно/квадратный метр)'] = {
        '++Ткань, лоскуты (доступно/квадратный метр)':1,
        }

metadict_army['+Ткань хлопковая, лоскуты (доступно/квадратный метр)'] = {
        '++Ткань, лоскуты (доступно/квадратный метр)':1,
        }

metadict_army['++Ткань, лоскуты (доступно/квадратный метр)'] = {
        '++Ткань, лоскуты (%)':[
            '(value / x) * 100',
            '-Ткань, лоскуты (требуется/квадратный метр)',
            ],
        }

metadict_army['-Ткань, лоскуты (требуется/квадратный метр)'] = {
        }

#----
# Побочные продукты:

metadict_detail['+Бульон бобовый (%)'] = {
        }

metadict_detail['+Бульон грибной (%)'] = {
        }

metadict_detail['+Валежник (%)'] = {
        }

metadict_detail['+Дикорастущие грибы (%)'] = {
        }

metadict_detail['+Дикорастущие растения (%)'] = {
        }

metadict_detail['+Дикорастущие ягоды (%)'] = {
        }

metadict_detail['+Зола (%)'] = {
        }

metadict_detail['+Луга дикоросов (%)'] = {
        }

metadict_detail['+Луга медоносов (%)'] = {
        }

metadict_detail['+Сок кленовый (%)'] = {
        }

metadict_detail['++Солома сухая (%)'] = {
        }

metadict_detail['++Солома на растопку (%)'] = {
        }

metadict_detail['++Опилки древесные (%)'] = {
        }

metadict_detail['++Отруби зерновые (%)'] = {
        }

metadict_detail['++Жмых (%)'] = {
        }

metadict_army['++Ткань, лоскуты (%)'] = {
        }

#----
# Энергетическая ценность пищи:

metadict_detail['-Белки (грамм)'] = {
        '--Калорийность белков (килокалорий)':4,
        '--Питательные вещества (грамм)':1,
        }

metadict_detail['-Жиры (грамм)'] = {
        '--Калорийность жиров (килокалорий)':9,
        '--Питательные вещества (грамм)':1,
        }

metadict_detail['-Углеводы (грамм)'] = {
        '--Калорийность углеводов (килокалорий)':4,
        '--Питательные вещества (грамм)':1,
        }

metadict_detail['-Этанол (грамм)'] = {
        '--Этанол (миллилитров)':1 / 0.7893,
        '--Калорийность этанола (килокалорий)':7.1,
        '--Питательные вещества (грамм)':1,
        }

#----
# Энергетическая ценность (группировка):

metadict_detail['--Калорийность этанола (килокалорий)'] = {                                          
        '----Калорийность пищи (килокалорий)':1,
        '---Калорийность этанола (%)':[
            '(value / x) * 100',
            '----Калорийность пищи (килокалорий)',
            ],
        }

metadict_detail['--Калорийность белков (килокалорий)'] = {
        '----Калорийность пищи (килокалорий)':1,
        '---Калорийность белков (%)':[
            '(value / x) * 100',
            '----Калорийность пищи (килокалорий)',
            ],
        }

metadict_detail['--Калорийность жиров (килокалорий)'] = {
        '----Калорийность пищи (килокалорий)':1,
        '---Калорийность жиров (%)':[
            '(value / x) * 100',
            '----Калорийность пищи (килокалорий)',
            ],
        }

metadict_detail['--Калорийность углеводов (килокалорий)'] = {
        '----Калорийность пищи (килокалорий)':1,
        '---Калорийность углеводов (%)':[
            '(value / x) * 100',
            '----Калорийность пищи (килокалорий)',
            ],
        }

metadict_detail['----Калорийность пищи (килокалорий)'] = {
        '++Энергия пищи (килокалорий)':1,
        }

metadict_detail['++Энергия пищи (килокалорий)'] = {
        '++Энергия пищи (МДж)':4.1868 / 1000,
        }

metadict_detail['++Энергия пищи (МДж)'] = {
        }

metadict_detail['---Калорийность белков (%)'] = {
        }

metadict_detail['---Калорийность жиров (%)'] = {
        }

metadict_detail['---Калорийность углеводов (%)'] = {
        }

metadict_detail['---Калорийность этанола (%)'] = {
        }

#----
# Считаем потребление алкоголя:
    # https://ru.wikipedia.org/wiki/Этанол

metadict_detail['--Этанол (миллилитров)'] = {
        '---Алкоголь (литров)':1 / 1000,
        }

metadict_detail['---Алкоголь (литров)'] = {
        }

#----
# Расход энергии:

metadict_detail['-Кипячение воды в печи (килограмм)'] = {
        # Удельная теплоёмкость воды — 4.187 кДж/(кг*°C)
        # Необходимая_энергия = удельная_теплоёмкость * масса * температура_испарения
        # 4.187*1*100=418.7 кДж (0.419 МДж), чтобы вскипятить литр воды при 100% КПД.
        '-Кипячение воды (МДж)':0.42 / 0.7,
        }

metadict_detail['-Кипячение воды в чане (килограмм)'] = {
        # КПД процесса: 0.2 костёр, 0.4 конфорка, 0.7 протопленная теплушка.
        '-Кипячение воды (МДж)':0.42 / 0.4,
        }

metadict_detail['-Кипячение воды в самоваре (килограмм)'] = {
        '-Кипячение воды (МДж)':0.42 / 0.4,
        }

metadict_detail['-Кипячение воды в котле (килограмм)'] = {
        '-Кипячение воды (МДж)':0.42 / 0.4,
        }

metadict_detail['-Кипячение воды на очаге (килограмм)'] = {
        '-Кипячение воды (МДж)':0.42 / 0.4,
        }

metadict_detail['-Кипячение воды на костре (килограмм)'] = {
        '-Кипячение воды (МДж)':0.42 / 0.3,
        }

metadict_detail['-Испарение воды в печи (килограмм)'] = {
        # Испарение воды с температурой 100 °C = 2260 кДж.
        '-Испарение воды (МДж)':(0.42 + 2.26) / 0.7,
        '-Испарение воды (грамм)':1000,
        }

metadict_detail['-Испарение воды в чане (килограмм)'] = {
        '-Испарение воды (МДж)':(0.42 + 2.26) / 0.4,
        '-Испарение воды (грамм)':1000,
        }

metadict_detail['-Испарение воды в котле (килограмм)'] = {
        '-Испарение воды (МДж)':(0.42 + 2.26) / 0.4,
        '-Испарение воды (грамм)':1000,
        }

metadict_detail['-Испарение воды на очаге (килограмм)'] = {
        '-Испарение воды (МДж)':(0.42 + 2.26) / 0.4,
        '-Испарение воды (грамм)':1000,
        }

metadict_detail['-Испарение воды на костре (килограмм)'] = {
        '-Испарение воды (МДж)':(0.42 + 2.26) / 0.3,
        '-Испарение воды (грамм)':1000,
        }

metadict_detail['-Испарение воды на воздухе (килограмм)'] = {
        '-Испарение воды (грамм)':1000,
        }

metadict_detail['-Испарение воды в кадке (килограмм)'] = {
        '-Испарение воды (грамм)':1000,
        }

#----
# Баланс воды:

#metadict_detail['-Испарение воды (грамм)'] = {
#        # Сколько остаётся воды в продукте?
#        '-Вода для готовки в продукте (%)':[
#            '((x - value) / x) * 100',
#            'Вода для готовки (грамм)',
#            ],
#        }

metadict_detail['-Испарение воды (грамм)'] = {
        }

#----
# Расход энергии:

metadict_detail['+Энергия костра рабочая (МДж)'] = {
        '+-| Энергия полезная (МДж)':1,
        }

metadict_detail['+Энергия очага рабочая (МДж)'] = {
        '+-| Энергия полезная (МДж)':1,
        }

metadict_detail['+Энергия печи рабочая (МДж)'] = {
        '+-| Энергия полезная (МДж)':1,
        }

metadict_detail['+Энергия печи на отопление (МДж)'] = {
        }

metadict_detail['+Энергия очага на отопление (МДж)'] = {
        }

metadict_detail['+Энергия топлива (МДж)'] = {
        '+-| Энергия затраченная (МДж)':1,
        }

metadict_detail['-Кипячение воды (МДж)'] = {
        '--| Энергия на готовку (МДж)':1,
        }

metadict_detail['-Испарение воды (МДж)'] = {
        '--| Энергия на готовку (МДж)':1,
        }

#----
# Расход энергии:

#metadict_detail['-Кипячение воды (МДж)'] = {
#        }

#metadict_detail['-Тепловая энергия печи (МДж)'] = {
#        }

metadict_detail['-Механическая энергия (киловатт-час)'] = {
        '--Механическая энергия (МДж)':3.6,
        }

metadict_detail['-Пневматическая энергия (киловатт-час)'] = {
        # Учитывается в механической (работа компрессоров)
        }

metadict_detail['--Механическая энергия (МДж)'] = {
        #'--Механическая энергия (ГДж)':1 / 1000,
        }

#----
# Трудовые ресурсы:

metadict_detail['_+Работа единорога (нормо-часов)'] = {
        '-|+ Работа единорога (нормо-часов)':1,
        '-|+ Работа (нормо-часов)':1,
        }

metadict_detail['_+Работа пегаса (нормо-часов)'] = {
        '-|+ Работа пегаса (нормо-часов)':1,
        '-|+ Работа (нормо-часов)':1,
        }

metadict_detail['_+Работа земнопони (нормо-часов)'] = {
        '-|+ Работа земнопони (нормо-часов)':1,
        '-|+ Работа (нормо-часов)':1,
        }

metadict_detail['_+Работа врача (нормо-часов)'] = {
        }

metadict_detail['_+Работа специалиста (нормо-часов)'] = {
        }

metadict_detail['_+Работа учёного (нормо-часов)'] = {
        }
