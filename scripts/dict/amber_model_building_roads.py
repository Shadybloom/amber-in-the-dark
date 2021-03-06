#----
# Дорожная система Эквестрии:

metadict_model['Потребность в дорогах (метр)'] = {
        # https://ru.wikisource.org/wiki/ЭСБЕ/Дорога
        # Во Франции 1885 года 1.22 км дорог/кв.километр территории (17 метров/жителя)
        # 5.6% дорог -- национальные; 4.4% дорог -- департаментские; 90% дорог -- просёлочные.
        'Эквестрийские дороги (километр)':1 / 1000,
        }

metadict_model['Эквестрийские дороги (километр)'] = {
        # В США 1889 было 260 000 км. железных дорог, 0.028 км/кв.километр территории (4 метра/жителя)
            # https://ru.wikisource.org/wiki/ЭСБЕ/Железные_дороги
        # Темпы строительства железных дорог до 1917 года, Российская империя (2000-3000 км/год)
        # При населении 129 миллионов (1897) строилось 2000 км/год (0.016 метра/человека в год)
            # https://f-husainov.livejournal.com/524212.html
        'Эквестрийские шоссейные дороги (километр)':0.3,
        'Эквестрийские грунтовые дороги (километр)':0.6,
        'Эквестрийские железные дороги (километр)':0.1,
        }

metadict_model['Эквестрийские шоссейные дороги (километр)'] = {
        # Исправить
            # Строительство дорог зависит от роста населения
        # https://ru.wikisource.org/wiki/ЭСБЕ/Шоссе
        'Обслуживание шоссейных дорог (километр)':1,
        'Строительство шоссейных дорог (километр)':1 / 50,
        'Эквестрийские главные мосты (метр)':25 / 10,
        }

metadict_model['Эквестрийские грунтовые дороги (километр)'] = {
        'Обслуживание грунтовых дорог (километр)':1,
        'Строительство грунтовых дорог (километр)':1 / 50,
        'Эквестрийские местные мосты (метр)':25 / 10,
        }

metadict_model['Обслуживание шоссейных дорог (километр)'] = {
        # Исправить
            # Износ дороги: 1 телега/день = 0.04 мм щебёночного полотна/год.
            # 100 телег/сутки = 4 мм (2.7% толщины покрытия)
            # Дороги в Эквестрии используются на 4% (20 телег/сутки)
        # Пропускная способность 500 грузовиков/сутки, допустимая скорость 30 км/час
        '-Предельный грузооборот шоссейных дорог (тонно-километров)':(500 * 1) * 360,
        'Ремонт полотна щебёночного шоссе (километр)':1 / 5,
        'Восстановление щебёночного шоссе (километр)':1 / 50,
        }

metadict_model['Строительство шоссейных дорог (километр)'] = {
        'Строительство щебёночного шоссе (километр)':1,
        }

metadict_model['Обслуживание грунтовых дорог (километр)'] = {
        '-Предельный грузооборот грунтовых дорог (тонно-километров)':(100 * 1) * 360,
        'Восстановление грунтовой дороги (километр)':1 / 50,
        }

metadict_model['Строительство грунтовых дорог (километр)'] = {
        'Строительство грунтовой дороги (километр)':1,
        }

#----
# Железные дороги (эксплуатация и ремонт путей):

metadict_model['Эквестрийские железные дороги (километр)'] = {
        'Обслуживание железных дорог (километр)':1,
        'Строительство железных дорог (километр)':1 / 30,
        'Эквестрийские железнодорожные мосты (метр)':25 / 3,
        '-Железнодорожная дистанция':1 / 300,
        '-Железнодорожный околоток':1 / 30,
        '-Железнодорожный пост':1 / 10,
        }

metadict_model['Обслуживание железных дорог (километр)'] = {
        # Исправить
            # Обязательно добавь ремонт пути (текущий, средний, капитальный)
            # Содержание и ремонт железнодорожного пути
                # http://railway-transport.ru/books/item/f00/s00/z0000003/index.shtml
            # ТЕХНИЧЕСКИЕ УСЛОВИЯ НА ПРОВЕДЕНИЕ ПЛАНОВО-ПРЕДУПРЕДИТЕЛЬНЫХ РЕМОНТОВ
            # ИНЖЕНЕРНЫХ СООРУЖЕНИЙ ЖЕЛЕЗНЫХ ДОРОГ РОССИИ
                # http://aquagroup.ru/normdocs/254
        'Обслуживание главных путей (километр)':1,
        'Обслуживание подъездных путей (километр)':0.2,
        'Обслуживание станционных путей (километр)':0.2,
        }

metadict_model['Обслуживание главных путей (километр)'] = {
        # Исправить
            # Обязательно добавь периодическую смену шпал. Деревянные же!
            # Попробуй найти старые нормативы, хотя бы на начало 20 века. А заодно и инструменты уточни.
                # Железнодорожные войска России, Книга 1. На службе Российской империи: 1851–1917
                # http://militera.lib.ru/h/zheleznodorozhnye_voyska_rossii/index.html
        # Нормы затрат труда на текущее содержание пути при выполнении работ вручную:
            # Обслуживание железных дорог требует около 0.3-0.6 работников на километр пути.
                # https://vunivere.ru/work65674
            # В России 737 тыc. сотрудников РЖД, длина путей 85 000 км (9 человек/километр)
            # Железные дороги Якутии 947 человек, длина путей 360 км (2.6 человека/километр)
            # В Соединённых штатах 221-235 тыс. рабочих на 230 000 км (1 человек/километр)
                # https://f-husainov.livejournal.com/325827.html
        '_-Работа бригады путевых смотрителей (нормо-часов)':(8 * 200),
        'Ремонт балластного слоя (километр)':1 / 30,
        }

metadict_model['Обслуживание подъездных путей (километр)'] = {
        '_-Работа бригады путевых смотрителей (нормо-часов)':(8 * 200) * 0.5,
        'Ремонт балластного слоя (километр)':1 / 30,
        }

metadict_model['Обслуживание станционных путей (километр)'] = {
        '_-Работа бригады путевых смотрителей (нормо-часов)':(8 * 200) * 0.5,
        'Ремонт балластного слоя (километр)':1 / 30,
        }

metadict_model['Строительство железных дорог (километр)'] = {
        'Строительство главных путей (километр)':1,
        'Строительство подъездных путей (километр)':0.2,
        'Строительство станционных путей (километр)':0.2,
        }

metadict_model['Строительство главных путей (километр)'] = {
        # Исправить
            # Дистанции и посты можно привязать к станциям.
        'Двухколейная железная дорога (километр)':1,
        'Железнодорожный вокзал (строительство)':1 / 300,
        'Железнодорожная станция (строительство)':1 / 30,
        'Железнодорожный пост (строительство)':1 / 10,
        }

metadict_model['Строительство подъездных путей (километр)'] = {
        'Одноколейная железная дорога (километр)':1,
        }

metadict_model['Строительство станционных путей (километр)'] = {
        'Одноколейная железная дорога (километр)':1,
        }

#----
# Строительство желеных дорог (справочник 1894 года):
        # https://ru.wikisource.org/wiki/ЭСБЕ/Железные_дороги,_в_техническом_отношении
    # СП 119.13330.2012 Железные дороги колеи 1520 мм. Актуализированная редакция СНиП 32-01-95:
        # http://docs.cntd.ru/document/1200095541

metadict_model['Двухколейная железная дорога (километр)'] = {
        # Исправить
            # Нужно учесть крупные мосты
            # Нужны входные семафоры на перегона. Каждые 2.6 километра.
        # Грузонапряжённость транссибирской железной дороги (2010) -- 100 млн. тонн в год.
            # При поездах с грузоподъёмностью в 5000 тонн (100 вагонов), это 60 поездов/сутки
        # Грузонапряжённость Николаевской железной дороги (1910) -- 11.5 млн. тонн/год
            # При поездах с грузоподъёмностью в 500 тонн (50 вагонов), это 60 поездов/сутки
        # Грузонапряжённость Николаевской железной дороги (1860) -- 1.12 млн. тонн/год
            # При поездах с грузоподъёмностью в 100 тонн (15 вагонов), это 30 поездов/сутки
        # В России 30 000 мостов на 85 000 километров эксплуатируемых путей
            # Средняя длина железнодорожного моста в России -- 31 метр (11 метров/километр пути)
            # Водопропускные трубы встречаются каждые 1-1.5 км дороги.
        'Строительство грунтовой дороги (километр)':1,
        'Устройство 1400-мм железобетонной водопропускной трубы (10 метров)':2,
        'Земляное полотно железной дороги (километр)':1,
        'Деревянный железнодорожный мост (25 метров)':1/3,
        'Железнодорожный путь (километр)':2,
        #'Железная дорога (проектирование) (километр)':1,
        #'Гектар пахатной земли (покупка)':10,
        #'-Грузооборот предельный (тонно-километров/сутки)':10 * 50 * 60,
        }

metadict_model['Одноколейная железная дорога (километр)'] = {
        'Строительство грунтовой дороги (километр)':1,
        'Устройство 1400-мм железобетонной водопропускной трубы (10 метров)':2,
        'Земляное полотно железной дороги (километр)':1,
        'Деревянный железнодорожный мост (25 метров)':1/3,
        'Железнодорожный путь (километр)':1,
        #'-Грузооборот предельный (тонно-километров/сутки)':10 * 50 * 30,
        }

metadict_model['Железнодорожный путь (километр)'] = {
        # Исправить
            # Установку противоугонов забыли!
        # Технологический процесс:
            # Расчистка и разметка пути,
            # Подъездная грунтовая дорога;
            # Устройство земляного полотна;
            # Устройство балластного слоя;
            # Сборка верхнего строения железнодорожного пути;
            # Укладка верхнего строения железнодорожного пути;
            # Выправка и рихтовка железнодорожного пути;
            # Отделка железнодорожного пути;
        'Укладка пути отдельными элементами (километр)':1,
        'Укладка стрелочных переводов поэлементно (штук)':2,
        'Выправка пути (километр)':1,
        }

metadict_model['Земляное полотно железной дороги (километр)'] = {
        # Высота насыпи -- 3 метра, ширина -- 10 метров
            # https://znaytovar.ru/gost/2/SP_3210498_Proektirovanie_zeml.html
        # Профильный объем земляных работ: 30 000 кубометров/километр (вторая категория)
            # 25.4. РАЗБИВКА ЗЕМЛЯНОГО ПОЛОТНА ДОРОГИ
            # http://lib4all.ru/base/B2005/B2005Part121-381.php
        # Балластировка пути:
            # http://www.rails.ru/Spravochnye-materialy/Ballastnaya-prizma
            # https://ru.wikisource.org/wiki/ЭСБЕ/Баласт,_на_железной_дороге
        # СН 449-72 Указания по проектированию земляного полотна железных и автомобильных дорог
            # https://znaytovar.ru/gost/2/SN_44972_Ukazaniya_po_proektir.html
        'Расчистка среднего леса киркомотыгами (квадратый метр)':10 * 1000,
        'Насыпь (кубометр)':3 * 7 * 1000,
        'Вывоз грунта (кубометр)':3 * 7 * 1000,
        'Уплотнение грунта пневматическими трамбовками (кубометр)':1 * 7 * 1000,
        'Балластировка пути тракторами (кубометр)':0.3 * 6 * 1000,
        }

metadict_model['Ремонт балластного слоя (километр)'] = {
        'Уплотнение грунта пневматическими трамбовками (кубометр)':1 * 7 * 1000,
        'Балластировка пути тракторами (кубометр)':0.3 * 6 * 1000,
        }

metadict_model['Устройство 1400-мм железобетонной водопропускной трубы (10 метров)'] = {
        # Исправить
            # Слишком современно для понек. В Эквестрии делают кирпичные.
            # А с чего бы? В кирпичном доме вдвое больше цемента, чем в этой трубе.
        # Длина 10 метров (2 блока), средний диаметр 1.5 метра.
        # Технологический процесс:
            # Укладка лекальных блоков
            # Укладка звеньев трубы
            # Сооружение оголовок труб
        'Укладка лекальных блоков (кубометр)':1.2 * 4 * 2,
        'Укладка звеньев железобетонной трубы (кубометр)':2.66 * 1 * 2,
        'Сооружение оголовок водопропускных труб (кубометр)':2.66,
        'Лекальный блок железобетонной трубы (штук)':4 * 2,
        'Железобетонная труба 1.4x5 метров (штук)':1 * 2,
        }

#----
# Строительство дорог:
    # https://ru.wikisource.org/wiki/ЭСБЕ/Дорога

metadict_model['Городская мостовая (метр)'] = {
        'Городская мостовая (километр)':1 / 1000,
        }

metadict_model['Городская мостовая (километр)'] = {
        # Исправить
            # мостовые в городах часто шире 7 метров
            # а к тому же мосты там каменные, а водоотводные трубы кирпичные
        # https://ru.wikisource.org/wiki/ЭСБЕ/Мостовая
        'Строительство щебёночного шоссе (километр)':1,
        'Устройство булыжной мостовой (квадратный метр)':7 * 1000,
        }

metadict_model['Ремонт полотна щебёночного шоссе (километр)'] = {
        'Устройство щебёночного шоссе (квадратный метр)':0.1 * (7 * 1000),
        }

metadict_model['Строительство щебёночного шоссе (километр)'] = {
        # Исправить
            # Рассыпка материалов для баластного слоя по дороге требует вдвое больше работы,
            # Чем вырытие такого же количества. 
        # https://ru.wikisource.org/wiki/ЭСБЕ/Шоссе
        'Насыпь (кубометр)':0.2 * 7 * 1000,
        'Расчистка среднего леса киркомотыгами (квадратый метр)':10 * 1000,
        'Уплотнение грунта пневматическими трамбовками (кубометр)':0.15 * 7 * 1000,
        'Строительство водоотводной деревянной трубы (штук)':1,
        'Строительство деревянного моста (25 метров)':1 / 10,
        'Устройство щебёночного шоссе (квадратный метр)':7 * 1000,
        }

metadict_model['Строительство грунтовой дороги (километр)'] = {
        # Устройство землевозных дорог
        # http://stroy-technics.ru/article/ustroistvo-zemlevoznykh-dorog
            # 1) Удаление растительного грунта
            # 2) Нарезка треугольных кюветов
            # 3) Планировка проезжей части
            # 4) Уплотнение проезжей части
        # https://ru.wikisource.org/wiki/ЭСБЕ/Грунтовые_дороги
        'Насыпь (кубометр)':0.2 * 7 * 1000,
        'Расчистка среднего леса киркомотыгами (квадратый метр)':10 * 1000,
        'Уплотнение грунта пневматическими трамбовками (кубометр)':0.15 * 7 * 1000,
        'Строительство водоотводной деревянной трубы (штук)':1,
        'Строительство деревянного моста (25 метров)':1 / 10,
        }

metadict_model['Восстановление щебёночного шоссе (километр)'] = {
        'Разборка щебёночного шоссе (квадратный метр)':7 * 1000,
        'Насыпь (кубометр)':0.2 * 7 * 1000,
        'Расчистка среднего леса киркомотыгами (квадратый метр)':10 * 1000,
        'Уплотнение грунта пневматическими трамбовками (кубометр)':0.15 * 7 * 1000,
        'Строительство водоотводной деревянной трубы (штук)':1,
        'Восстановление щебёночного шоссе (квадратный метр)':7 * 1000,
        }

metadict_model['Восстановление грунтовой дороги (километр)'] = {
        'Насыпь (кубометр)':0.2 * 7 * 1000,
        'Расчистка среднего леса киркомотыгами (квадратый метр)':10 * 1000,
        'Уплотнение грунта пневматическими трамбовками (кубометр)':0.15 * 7 * 1000,
        'Строительство водоотводной деревянной трубы (штук)':1,
        }

#----
# Строительство мостов:

metadict_model['Деревянный железнодорожный мост (25 метров)'] = {
        # Деревянные железнодорожные эстакады:
            # https://masterok.livejournal.com/2607019.html
        'Деревянный 60-тонный мост (метр)':25,
        }

metadict_model['Строительство деревянного моста (25 метров)'] = {
        'Деревянный 10-тонный мост (метр)':25,
        }

metadict_model['Деревянный 60-тонный мост (метр)'] = {
        # Исправить
            # Добавь погружение свай:
                # Таблица ГЭСН 05-01-015 Погружение деревянных свай в мостостроении
                # http://www.norm-load.ru/SNiP/Data1/54/54266/index.htm#i684612
        'Устройство деревянных пролётов (железнодорожных) (кубометр)':1,
        'Устройство деревянных опор (кубометр)':1,
        }

metadict_model['Деревянный 10-тонный мост (метр)'] = {
        'Устройство деревянных пролётов (с настилом) (кубометр)':0.75,
        'Устройство деревянных опор (кубометр)':0.25,
        }

#----
# Проектирование мостов:

metadict_model['Низководный мост (метр)'] = {
        # Мостовой взвод собирает 15 метров моста в час (из готовых конструкций)
        # В метре низководного моста грузоподъёмностью в 60 тонн около 2 кубометров древесины.
        'Низководный мост (100 метров)':0.01,
        }

metadict_model['Низководный мост (100 метров)'] = {
        # Пособие по расчету сечений балочных деревянных мостов с разбросными прогонами
            # http://www.gosthelp.ru/text/PosobiePosobieporaschetus.html
        # Справочник офицера инженерных войск (стр 156-184)
            # Основная грузоподъёмность (60 тонн)
            # Расход материалов -- 120 кубометра дерева (190 хлыстов); 0.52 тонны металла.
            # Пролёты: 4.5 x 0.42 м
        'Пролётное строение низководного моста':100 / 4.5,
        }

metadict_model['Пролётное строение низководного моста'] = {
        # Исправить
            # Раздели на опору и пару колейных блоков.
        # Справочник офицера инженерных войск (стр 171)
            # Грузоподъёмность НГ-60 (60 тонн), проезжая часть 4.2 метра.
        # Строение моста (снизу вверх):
            # http://text.gosthelp.ru/images/text/49717.files/image010.jpg
            # http://saper.isnet.ru/texnica-2/usm-02.jpg
            # https://vunivere.ru/work27781
            # Опора:
                # Сваи (по 4 штуки, диаметр в тонком конце 0.33, углубление в грунт 4+ метров)
                # Насадки (поперечные балки, лежат на сваях, диаметр 0.31 м)
                # Схватки опоры (6 см доски размерами 5.2 x 18)
            # Колейные блоки (x2 для 60 тонн грузоподъёмности)
                # Прогоны (продольные балки, лежат на насадках, диаметр 0.29 м) 
                # Настил (доски толщиной 5 см, или накат в один слой):
                    # Поперечный настил (поперечные доски, рабочий настил)
                    # Защитный настил (продольные доски, поверхность)
                    # Колёсоотбои (брёвна, барьерное ограждение)
        'Свая низководного моста':4,
        'Насадка низководного моста':1,
        'Схватка опоры низководного моста':4,
        'Прогон низководного моста':10,
        'Доски связей блоков низководного моста (квадратный метр)':3.6 * 0.22 * 6,
        'Поперечный настил низководного моста (квадратный метр)':2.24 * 0.22 * 34,
        'Защитный настил низководного моста (квадратный метр)':3.8 * 0.22 * 12,
        'Колёсоотбой низководного моста':2,
        'Поковки из квадратных заготовок (килограмм)':90,
        }

#----
# Элементы железной дороги:

metadict_model['Звено железной дороги Р65 (штук)'] = {
        # Исправить
            # Перенести всё это к остальным материалам.
            # Перенеси сюда сборку звеньев, или назови "комплект для сбора звена"
            # Лучше комплектами назвать, потому что звенья собирают на месте.
        # http://www.norm-load.ru/SNiP/Data1/56/56052/index.htm#i36814
        # Длина звена -- 25 метров (40 на километр), масса -- 8.7 тонн.
        'Шпалы деревянные Р65 (штук)':50,
        'Скобы шпальные (штук)':100,
        'Рельсы железнодорожные Р65 (метр)':50,
        'Болты стыковые Р65 (штук)':8,
        'Накладки стыковые Р65 (штук)':4,
        'Костыли путевые Р65 (штук)':405,
        'Подкладки шпальные Р65 (штук)':100,
        'Прокладки амортизационные (штук)':100,
        'Масла каменноугольные для пропитки древесины (килограмм)':1.825,
        }

metadict_model['Звено железной дороги Р33 (штук)'] = {
        # В Российской Империи 1894 года ставили 1-1.3 шпалы на метр железной дороги.
        # https://ru.wikisource.org/wiki/ЭСБЕ/Железные_дороги,_в_техническом_отношении
        'Шпалы деревянные Р33 (штук)':30,
        'Скобы шпальные (штук)':60,
        'Рельсы железнодорожные Р33 (метр)':50,
        'Болты стыковые Р33 (штук)':8,
        'Накладки стыковые Р33 (штук)':4,
        'Костыли путевые Р33 (штук)':243,
        'Подкладки шпальные Р33 (штук)':60,
        'Масла каменноугольные для пропитки древесины (килограмм)':1.1,
        #'Прокладки амортизационные (штук)':60,
        }

metadict_model['Материалы для монтажа стрелочного перевода Р65 (комплект)'] = {
        # http://www.norm-load.ru/SNiP/Data1/56/56052/index.htm#i334685
        'Шпалы деревянные Р65 (штук)':5,
        'Скобы шпальные (штук)':85,
        'Шурупы путевые (штук)':410,
        'Костыли путевые Р65 (штук)':605,
        'Брусья для стрелочных переводов (кубометр)':15.5,
        'Прокладки амортизационные (штук)':220,
        }

metadict_model['Материалы для монтажа стрелочного перевода Р33 (комплект)'] = {
        # http://www.norm-load.ru/SNiP/Data1/56/56052/index.htm#i334685
        'Шпалы деревянные Р33 (штук)':5,
        'Скобы шпальные (штук)':85,
        'Шурупы путевые (штук)':410,
        'Костыли путевые Р33 (штук)':605,
        'Брусья для стрелочных переводов (кубометр)':15.5,
        #'Прокладки амортизационные (штук)':220,
        }

#----
# Элементы низководного моста (штучные):

metadict_model['Свая низководного моста'] = {
        # Глубина реки до 2 метров, не меньше 4 метров углубления в грунт.
        # Комлевой конец крепится к насадке, вершинный заостряется и забивается в грунт.
        'Брёвна диаметром 200 мм (метр)':6.5,
        }

metadict_model['Насадка низководного моста'] = {
        # Насадки (поперечные балки, лежат на сваях)
        # Обтёсываются на два канта (с двух сторон)
        'Брёвна диаметром 250 мм (метр)':5.2,
        }

metadict_model['Схватка опоры низководного моста'] = {
        # Продольное укрепление свай, диагональные доски.
        'Доска обрезная 50 мм (квадратный метр)':0.52 * 0.18,
        }

metadict_model['Прогон низководного моста'] = {
        # Прогоны (продольные балки, лежат на насадках) 
        'Брёвна диаметром 200 мм (метр)':5,
        }

metadict_model['Доски связей блоков низководного моста (квадратный метр)'] = {
        'Доска обрезная 50 мм (квадратный метр)':1,
        }

metadict_model['Поперечный настил низководного моста (квадратный метр)'] = {
        'Доска обрезная 50 мм (квадратный метр)':1,
        }

metadict_model['Защитный настил низководного моста (квадратный метр)'] = {
        'Доска обрезная 50 мм (квадратный метр)':1,
        }

metadict_model['Колёсоотбой низководного моста'] = {
        # Барьерное ограждение
        'Брёвна диаметром 200 мм (метр)':3.8,
        }

#----
# Элементы железной дороги (штучные):

metadict_model['Железобетонная труба 1.4x5 метров (штук)'] = {
        # ТБ 140.50-3
            # Длина: 5 000, диаметр 1.4
            # Объём бетона 2.66; масса 6.7 тонн
        # http://www.sbtbeton.ru/truba-sbt/truby-zhelezobetonnye-beznapornye/tip-tb/
        'Железобетон тяжёлый (кубометр)':2.66,
        }

metadict_model['Строительство водоотводной деревянной трубы (штук)'] = {
        # Исправить
            # Нужно определить трудозатраты на строительство.
            # Вообще, типичный ручей восточного побережья
            # при водоотводе с 25 кв.километров даёт 1 кубометр/секунду
            # Труба с диаметром 1.4 метра, это 1.54 кв. метра, что избыточно
            # ведь скорость течения может быть больше метра/секунду.
        # Справочник офицера инженерных войск (стр 101)
        'Доска обрезная (кубометр)':2.5,
        'Поковки из квадратных заготовок (килограмм)':6,
        }

metadict_model['Лекальный блок железобетонной трубы (штук)'] = {
        # Лекальный блок Ф 20.4
            # Ø 1500 мм 1600 мм
            # 2000х1620х520, R-930
            # 1,20 кубометра, 3 тонны.
        # http://www.sbtbeton.ru/road-building/trubopereezd-sbt/lekalnye-bloki/
        'Железобетон тяжёлый (кубометр)':1.2,
        }

metadict_model['Шпалы деревянные Р65 (штук)'] = {
        # Длина: 2.75 метра Ширина: 0.25 Толщина: 0.18 Объём 0.1237 кубометра
            # Пропитка антисептиком (хлорид цинка?) -- 100 кг/кубометр шпалы.
            # https://ru.wikisource.org/wiki/ЭСБЕ/Дерево,_материал
        # http://www.rails.ru/Spravochnye-materialy/shpaly-i-brusya
        # http://www.shpala.ru/index.shtml?sleeper.html
        'Брусья для шпал (кубометр)':0.12375,
        }

metadict_model['Шпалы деревянные Р33 (штук)'] = {
        # Длина: 2.75, Ширина: 0.23, Толщина: 0.16 Объём 0.1 кубомер
            # Дубовые шпалы без пропитки служат 7-9 лет (Россия), 14-16 лет (Германия)
        # https://ru.wikisource.org/wiki/ЭСБЕ/Железные_дороги,_в_техническом_отношении
        'Брусья для шпал (кубометр)':0.1,
        }

metadict_model['Скобы шпальные (штук)'] = {
        # http://vs-group.biz/store/shpaly/skoba_s-obraznaya_dlya_shpal/
        'Скобы шпальные (килограмм)':0.08,
        }

metadict_model['Шурупы путевые (штук)'] = {
        # http://www.zaoportal.ru/product/view/267
        'Шурупы путевые (килограмм)':0.56,
        }

metadict_model['Перевод стрелочный Р65 (комплект)'] = {
        # Стрелочный перевод тип Р65 марка 1/9 проект 2769.00.000
        # http://www.murom-switch.ru/page/318
        'Перевод стрелочный (килограмм)':14500,
        }

metadict_model['Перевод стрелочный Р33 (комплект)'] = {
        # Ширококолейная железная дорога, поэтому масса больше:
        # http://www.zaoportal.ru/content/katalog_strelochnyh_perevodov#423
        'Перевод стрелочный (килограмм)':6000,
        }

#----
# Элементы рельсов Р65:

metadict_model['Болты стыковые Р65 (штук)'] = {
        # В сборе с шайбами
        # http://www.zaoportal.ru/product/view/272
        'Болты стыковые (килограмм)':1.128,
        }

metadict_model['Костыли путевые Р65 (штук)'] = {
        # http://www.zaoportal.ru/product/view/265
        'Костыли путевые (килограмм)':0.38,
        }

metadict_model['Накладки стыковые Р65 (штук)'] = {
        # http://promputsnab.ru/nakladki-geleznodorognie.html
        'Накладки стыковые (килограмм)':30,
        }

metadict_model['Подкладки шпальные Р65 (штук)'] = {
        # http://www.vsp74.ru/podkladki/55-podkladka-d-65.html
        'Подкладки шпальные (килограмм)':7.66,
        }

metadict_model['Прокладки амортизационные (штук)'] = {
        # http://vs-group.biz/store/rti/prokladka_pod_d65_cp362/
        'Прокладки амортизационные (килограмм)':0.6,
        }

metadict_model['Рельсы железнодорожные Р65 (метр)'] = {
        # Рельсы железнодорожные типа Р-65 категории Т1
        'Рельсы железнодорожные (килограмм)':65,
        }

#----
# Элементы рельсов Р33:

metadict_model['Болты стыковые Р33 (штук)'] = {
        # https://rails.com.ua/bolt-stykovoi22x115.html
        'Болты стыковые (килограмм)':0.595,
        }

metadict_model['Костыли путевые Р33 (штук)'] = {
        # https://rails.com.ua/kostyl-putevoi-14x14x130.html
        'Костыли путевые (килограмм)':0.27,
        }

metadict_model['Накладки стыковые Р33 (штук)'] = {
        # https://rails.com.ua/nakladka-r33.html
        'Накладки стыковые (килограмм)':6.3,
        }

metadict_model['Подкладки шпальные Р33 (штук)'] = {
        # https://rails.com.ua/podkladka-p33.html
        'Подкладки шпальные (килограмм)':2.83,
        }

metadict_model['Рельсы железнодорожные Р33 (метр)'] = {
        'Рельсы железнодорожные (килограмм)':33,
        }
