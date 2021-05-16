#----
# Заметки
# Железные дороги (Германия 1895 года, 52.5 млн. человек)
    # Грузы в год -- 181 млн. тонн (3.5 тонн/человека)
    # Грузооборот -- 25 млрд. тонно-километров (138 км/тонна груза, 476 тонно-километров/человека)
    # Протяжённость дорог -- 45 000 километров, 0.81 метра/человека (из них 33%, имеют 2+ колеи)
    # Служащие -- 30 на 10 000 граждан;
    # Рабочие -- 40 на 10 000 граждан
# Парк машин (1894-1895 годы) -- 16 000 паровозов, 23 000 км/паровоз-год
    # Пассажирские вагоны -- 30 000 штук, 69 000 осей (43 места/вагон, 120 км/день)
    # Товарные вагоны -- 322 000 штук (11 тонн/вагон, 57 км/день, 562 тонны/вагон-год, 77 639 ткм/вагон-год)
    # Пассажирский/скорый поезд -- 16 осей, 8 вагонов, 340 мест.
# Мощность паровозов:
    # 1 пегас = 30 кВт-час
    # 1 кВт-час = 1.4 килограмма каменного угля
    # Горизонтальный путь, 50 тонно-километров/час = 0.4 кВт-час
    # Подъём в 5 на 1000 метров, 50 тонно-километров/час = 1.1 кВт
# Работа поездов:
    # Товарный поезд с 33 вагонами (400 тонн) -- 640 кВт
    # Пассажирский поезд с 8+2 вагонами (150 тонн) -- 210 кВт
    # Курьерский поезд с 8+2 вагонами, 100 км-час (200 тонн) -- 710 кВт

#----
# Грузоперевозки (коррекция величин):

metadict_detail['Доставка промышленных товаров (тонн)'] = {
        # TODO:
            # Сначала из килограмм в тонны, затем из тонн в килограммы. Нафига?
        'Доставка промышленных товаров (брутто) (килограмм)':1000,
        }

metadict_detail['Доставка строительного сырья (тонн)'] = {
        # TODO:
            # Вообще-то лес сплавляют без тары, да и прочее навалом.
        'Доставка строительного сырья (брутто) (килограмм)':1000,
        }

metadict_detail['Доставка дров (тонн)'] = {
        'Доставка дров (брутто) (килограмм)':1000,
        }

metadict_detail['Доставка угля (тонн)'] = {
        'Доставка угля (брутто) (килограмм)':1000,
        }

metadict_detail['Вывоз мусора (тонн)'] = {
        'Вывоз мусора (брутто) (килограмм)':1000,
        }

metadict_detail['Доставка стройматериалов (тонн)'] = {
        # TODO:
            # А вот здесь всё иначе. Цемент-то возят в мешках, а стекло и вовсе в упаковке.
        'Доставка стройматериалов (брутто) (килограмм)':1000,
        }

#----
# Грузоперевозки (пирамиды снабжения):

metadict_detail['Доставка воды для хозяйства (брутто) (килограмм)'] = {
        # TODO:
            # Добавь трубопроводный транспорт.
            # Только 'нетто' поставь. А то будут летать бочки по водопроводу.
        'Домашние грузоперевозки воды (брутто) (килограмм)':1,
        }

metadict_detail['Доставка воды для промышленности (брутто) (килограмм)'] = {
        # TODO:
            # Воду для строительства считай отдельно.
            # Помни. Грузоперевозки воды считаются отдельно.
            # Хотя, особого смысла в этом нет.
        'Локальные грузоперевозки воды (брутто) (килограмм)':1,
        }

metadict_detail['Доставка грузов от ближайшего леса (брутто) (килограмм)'] = {
        # От 1 до 10 километров.
        'Локальные грузоперевозки (брутто) (килограмм)':0.3,
        'Местные грузоперевозки (брутто) (килограмм)':0.7,
        }

metadict_detail['Доставка напитков (брутто) (килограмм)'] = {
        # От 1 до 10 километров. село-деревня-поле
        'Локальные грузоперевозки (брутто) (килограмм)':0.7,
        'Местные грузоперевозки (брутто) (килограмм)':0.3,
        }

metadict_detail['Доставка зерновых (брутто) (килограмм)'] = {
        # От фермы к селению, дальше в город, часть в госзапасы, прошлогоднее на экспорт.
        'Местные грузоперевозки (брутто) (килограмм)':1,
        'Районные грузоперевозки (брутто) (килограмм)':0.75,
        'Междугородние грузоперевозки (брутто) (килограмм)':0.5,
        'Международные грузоперевозки (брутто) (килограмм)':0.4,
        }

metadict_detail['Доставка масличного сырья (брутто) (килограмм)'] = {
        # Аналогично зерну. Масло делают по мере надобности.
        'Местные грузоперевозки (брутто) (килограмм)':1,
        'Районные грузоперевозки (брутто) (килограмм)':0.75,
        'Междугородние грузоперевозки (брутто) (килограмм)':0.5,
        'Международные грузоперевозки (брутто) (килограмм)':0.4,
        }

metadict_detail['Доставка зернобобовых (брутто) (килограмм)'] = {
        # От села к городу, дальше на обмолот-сушку-переработку.
        'Местные грузоперевозки (брутто) (килограмм)':1,
        'Районные грузоперевозки (брутто) (килограмм)':0.75,
        'Междугородние грузоперевозки (брутто) (килограмм)':0.25,
        }

metadict_detail['Доставка орехов (брутто) (килограмм)'] = {
        # От села к городу, дальше на обмолот-сушку-переработку.
        'Местные грузоперевозки (брутто) (килограмм)':1,
        'Районные грузоперевозки (брутто) (килограмм)':0.75,
        'Междугородние грузоперевозки (брутто) (килограмм)':0.25,
        }

metadict_detail['Доставка сельскохозяйственного сырья (брутто) (килограмм)'] = {
        # От плантации к сахарному заводу (в основном это тростник)
        'Локальные грузоперевозки (брутто) (килограмм)':0.6,
        'Местные грузоперевозки (брутто) (килограмм)':0.4,
        }

metadict_detail['Доставка овощей (брутто) (килограмм)'] = {
        # От деревни в село. часть в город, часть на торговлю.
        'Локальные грузоперевозки (брутто) (килограмм)':1,
        'Местные грузоперевозки (брутто) (килограмм)':0.5,
        'Районные грузоперевозки (брутто) (килограмм)':0.25,
        'Междугородние грузоперевозки (брутто) (килограмм)':0.1,
        }

metadict_detail['Доставка фруктов (брутто) (килограмм)'] = {
        # TODO:
            # Воздушная доставка фруктов, это редкость.
        # Изрядную часть фруктов сушат и перерабатывают на месте.
        'Локальные грузоперевозки (брутто) (килограмм)':1,
        'Местные грузоперевозки (брутто) (килограмм)':0.5,
        'Районные грузоперевозки (брутто) (килограмм)':0.25,
        'Междугородние грузоперевозки (брутто) (килограмм)':0.25,
        #'Воздушные междугородние грузоперевозки (брутто) (килограмм)':0.05,
        }

metadict_detail['Доставка продовольствия (брутто) (килограмм)'] = {
        # Активная междугородняя и международная торговля. Мука, сухофрукты, масло, сидр.
        'Местные грузоперевозки (брутто) (килограмм)':1,
        'Районные грузоперевозки (брутто) (килограмм)':0.75,
        'Междугородние грузоперевозки (брутто) (килограмм)':0.5,
        'Международные грузоперевозки (брутто) (килограмм)':0.25,
        }

metadict_detail['Доставка импортных товаров (брутто) (килограмм)'] = {
        # Из Эверглейдса в Эквестрию. Морской путь.
        'Международные грузоперевозки (брутто) (килограмм)':1,
        'Междугородние грузоперевозки (брутто) (килограмм)':1,
        'Районные грузоперевозки (брутто) (килограмм)':0.75,
        }

metadict_detail['Доставка импортных фруктов (брутто) (килограмм)'] = {
        # Из Эверглейдса в Эквестрию. Перевозки на планёрах.
        'Воздушные международные грузоперевозки (брутто) (килограмм)':1,
        }

metadict_detail['Доставка строительного сырья (брутто) (килограмм)'] = {
        # TODO:
            # Сплав леса, перевозка глины. Надо бы разделить.
        'Местные грузоперевозки (брутто) (килограмм)':0.7,
        'Районные грузоперевозки (брутто) (килограмм)':0.3,
        }

metadict_detail['Доставка дров (брутто) (килограмм)'] = {
        'Местные грузоперевозки (брутто) (килограмм)':0.4,
        'Районные грузоперевозки (брутто) (килограмм)':0.6,
        }

metadict_detail['Доставка угля (брутто) (килограмм)'] = {
        'Местные грузоперевозки (брутто) (килограмм)':0.3,
        'Районные грузоперевозки (брутто) (килограмм)':0.7,
        }

metadict_detail['Доставка стройматериалов (брутто) (килограмм)'] = {
        # TODO:
            # Весьма трудозатратно получается.
        'Местные грузоперевозки (брутто) (килограмм)':0.5,
        'Районные грузоперевозки (брутто) (килограмм)':0.4,
        'Междугородние грузоперевозки (брутто) (килограмм)':0.1,
        }

metadict_detail['Вывоз мусора (брутто) (килограмм)'] = {
        'Локальные грузоперевозки мусора (брутто) (килограмм)':1,
        }

metadict_detail['Доставка промышленных товаров (брутто) (килограмм)'] = {
        'Районные грузоперевозки (брутто) (килограмм)':1,
        'Междугородние грузоперевозки (брутто) (килограмм)':0.75,
        'Международные грузоперевозки (брутто) (килограмм)':0.5,
        }

#----
# Грузоперевозки (коррекция величин):

metadict_detail['Воздушные междугородние грузоперевозки (брутто) (килограмм)'] = {
        'Воздушные междугородние грузоперевозки (тонн)':0.001,
        '|===Грузов перевезено (тонн)':0.001,
        }

metadict_detail['Воздушные международные грузоперевозки (брутто) (килограмм)'] = {
        'Воздушные международные грузоперевозки (тонн)':0.001,
        '|===Грузов перевезено (тонн)':0.001,
        }

metadict_detail['Междугородние грузоперевозки (брутто) (килограмм)'] = {
        'Междугородние грузоперевозки (брутто) (тонн)':0.001,
        '|===Грузов перевезено (тонн)':0.001,
        }

metadict_detail['Международные грузоперевозки (брутто) (килограмм)'] = {
        'Международные грузоперевозки (брутто) (тонн)':0.001,
        '|===Грузов перевезено (тонн)':0.001,
        }

metadict_detail['Районные грузоперевозки (брутто) (килограмм)'] = {
        'Районные грузоперевозки (брутто) (тонн)':0.001,
        '|===Грузов перевезено (тонн)':0.001,
        }

metadict_detail['Местные грузоперевозки (брутто) (килограмм)'] = {
        'Местные грузоперевозки (брутто) (тонн)':0.001,
        '|===Грузов перевезено (тонн)':0.001,
        }

metadict_detail['Локальные грузоперевозки (брутто) (килограмм)'] = {
        'Локальные грузоперевозки (брутто) (тонн)':0.001,
        '|===Грузов перевезено (тонн)':0.001,
        }

metadict_detail['Локальные грузоперевозки воды (брутто) (килограмм)'] = {
        'Локальные грузоперевозки воды (брутто) (тонн)':0.001,
        '|===Грузов перевезено (тонн)':0.001,
        }

metadict_detail['Локальные грузоперевозки мусора (брутто) (килограмм)'] = {
        'Локальные грузоперевозки мусора (брутто) (тонн)':0.001,
        #'|===Грузов перевезено (тонн)':0.001,
        }

metadict_detail['Домашние грузоперевозки (брутто) (килограмм)'] = {
        'Домашние грузоперевозки (брутто) (тонн)':0.001,
        '|===Грузов перевезено (тонн)':0.001,
        }

metadict_detail['Домашние грузоперевозки воды (брутто) (килограмм)'] = {
        'Домашние грузоперевозки воды (брутто) (тонн)':0.001,
        #'|===Грузов перевезено (тонн)':0.001,
        }

#----
# Виды транспорта:

metadict_detail['Международные грузоперевозки (брутто) (тонн)'] = {
        # 3000-4000 километров.
            # https://ru.wikisource.org/wiki/ЭСБЕ/Торговое_мореходство
            # https://ru.wikisource.org/wiki/ЭСБЕ/Торговое_судостроение
        'Морские международные грузоперевозки (тонн)':1,
        }

metadict_detail['Междугородние грузоперевозки (брутто) (тонн)'] = {
        # TODO:
            # Сделай отдельно почту и курьерские перевозки
        # 1000-2000 километров.
        'Железнодорожные междугородние грузоперевозки (тонн)':0.6,
        'Речные междугородние грузоперевозки (тонн)':0.15,
        'Морские междугородние грузоперевозки (тонн)':0.25,
        }

metadict_detail['Районные грузоперевозки (брутто) (тонн)'] = {
        # В пределах округа. 50-100 километров.
        'Речные районные грузоперевозки (тонн)':0.7,
        'Гужевые районные грузоперевозки (тонн)':0.3,
        }

metadict_detail['Местные грузоперевозки (брутто) (тонн)'] = {
        # В пределах кантона. Около 10 километров.
        'Гужевые местные грузоперевозки (тонн)':1,
        }

metadict_detail['Локальные грузоперевозки (брутто) (тонн)'] = {
        # Городок, село, деревня. Около 1 километра.
        'Гужевые локальные грузоперевозки (тонн)':1,
        }

metadict_detail['Локальные грузоперевозки воды (брутто) (тонн)'] = {
        'Гужевые локальные грузоперевозки воды (тонн)':1,
        }

metadict_detail['Локальные грузоперевозки мусора (брутто) (тонн)'] = {
        'Гужевые локальные грузоперевозки мусора (тонн)':1,
        }

metadict_detail['Домашние грузоперевозки (брутто) (тонн)'] = {
        # 300 метров.
        'Вьючные домашние грузоперевозки (тонн)':1,
        }

metadict_detail['Домашние грузоперевозки воды (брутто) (тонн)'] = {
        'Вьючные домашние грузоперевозки воды (тонн)':1,
        }

#----
# Транспорт (маршруты):

metadict_detail['Воздушные международные грузоперевозки (тонн)'] = {
        'Воздушный маршрут Кантерлот-Эверглейдс (тонн)':0.7,
        'Воздушный маршрут Кантерлот-острова (тонн)':0.3,
        '|===Грузонапряжённость воздушных путей (тонн)':1,
        }

metadict_detail['Воздушные междугородние грузоперевозки (тонн)'] = {
        'Воздушный маршрут Кантерлот-Балтимэр (тонн)':0.5,
        'Воздушный маршрут Сталлионград-Кантерлот (тонн)':0.5,
        '|===Грузонапряжённость воздушных путей (тонн)':1,
        }

metadict_detail['Железнодорожные междугородние грузоперевозки (тонн)'] = {
        # TODO: Переписывай направления. Карта грузоперевозок изменилась.
        'Железнодорожное направление Сталлионград-Кантерлот (тонн)':0.4,
        'Железнодорожное направление Кантерлот-Филлидельфия (тонн)':0.3,
        'Железнодорожное направление Филлидельфия-Мэйнхеттен (тонн)':0.2,
        'Железнодорожное направление Филлидельфия-Балтимэр (тонн)':0.1,
        '|===Грузонапряжённость железных дорог (тонн)':1,
        }

metadict_detail['Морские международные грузоперевозки (тонн)'] = {
        'Морское направление Балтимэр-Эверглейдс (тонн)':0.7,
        'Морское направление Мэйнхеттен-острова (тонн)':0.3,
        '|===Грузонапряжённость морских путей (тонн)':1,
        }

metadict_detail['Морские междугородние грузоперевозки (тонн)'] = {
        'Морское направление Филлидельфия-Мэйнхеттен (тонн)':0.6,
        'Морское направление Филлидельфия-Балтимэр (тонн)':0.4,
        '|===Грузонапряжённость морских путей (тонн)':1,
        }

metadict_detail['Речные междугородние грузоперевозки (тонн)'] = {
        'Речной маршрут Клаудсдейл-Кантерлот (тонн)':0.5,
        'Речной маршрут Кантерлот-Балтимэр (тонн)':0.5,
        '|===Грузонапряжённость речных путей (тонн)':1,
        }

metadict_detail['Речные районные грузоперевозки (тонн)'] = {
        'Речной маршрут село-город (тонн)':1,
        '|===Грузонапряжённость речных путей (тонн)':1,
        }

metadict_detail['Гужевые районные грузоперевозки (тонн)'] = {
        'Наземный маршрут село-город (тонн)':1,
        '|===Грузонапряжённость шоссейных дорог (тонн)':1,
        }

metadict_detail['Гужевые местные грузоперевозки (тонн)'] = {
        'Наземный маршрут поле-деревня (тонн)':1,
        '|===Грузонапряжённость шоссейных дорог (тонн)':1,
        }

metadict_detail['Гужевые локальные грузоперевозки (тонн)'] = {
        'Наземный маршрут город-мануфактура (тонн)':1,
        '|===Грузонапряжённость городских дорог (тонн)':1,
        }

metadict_detail['Гужевые локальные грузоперевозки воды (тонн)'] = {
        'Наземный маршрут стройплощадка-колодец (тонн)':1,
        '|===Грузонапряжённость городских дорог (тонн)':1,
        }

metadict_detail['Гужевые локальные грузоперевозки мусора (тонн)'] = {
        'Наземный маршрут город-свалка (тонн)':1,
        '|===Грузонапряжённость сельских дорог (тонн)':1,
        }

metadict_detail['Вьючные домашние грузоперевозки (тонн)'] = {
        'Наземный маршрут дом-опушка (тонн)':1,
        '|===Грузонапряжённость сельских дорог (тонн)':1,
        }

metadict_detail['Вьючные домашние грузоперевозки воды (тонн)'] = {
        'Наземный маршрут дом-колодец (тонн)':1,
        '|===Грузонапряжённость сельских дорог (тонн)':1,
        }

#----
# Транспорт (дистанции):
    # Экономика России, цифры и факты. Часть 3 Транспорт.
        # https://utmagazine.ru/posts/10280-ekonomika-rossii-cifry-i-fakty-chast-3-transport
        # Грузооброт в России 2015 года (146.2 млн человек) -- 5080 млрд. ткм (34 746 ткм/человека)
        # Российские железные дороги (894 тысячи работников) -- 3180 млрд. ткм (3 557 046 ткм/работника)
    # Среднее расстояние перевозки по видам транспорта:
        # Воздушный -- 4000 километров;
        # Железнодорожный -- 2134 километров;
        # Водный (морской и речной) -- 776 километров;
        # Автомобильный -- 45 километров.
    # Среднее расстояние перевозки по видам грузов:
        # Каменный уголь – 2 327 км.
        # Химические и минеральные удобрения – 1 620 км.
        # Нефть и нефтепродукты – 1 574 км.
        # Зерно и продукты помола – 1 567 км.
        # Лес и пиломатериалы – 1 541 км.
        # Черные металлы – 1 446 км.
        # Руды металлов – 1041 км.
        # Лом черных металлов – 877 км.
        # Цемент – 764 км.
        # Минеральные стройматериалы – 754 км.

metadict_detail['Воздушный маршрут Кантерлот-Балтимэр (тонн)'] = {
        # TODO:
            # Раздели погрузку и разгрузку транспорта на отдельные работы.
            # Эффективность погрузочно-разгрузочных работ зависит от механизации.
        'Воздушный маршрут Кантерлот-Балтимэр (тонно-километр)':2000,
        '_-Работы погрузочно-разгрузочные с планёра (тонн)':1 * 2,
        }

metadict_detail['Воздушный маршрут Кантерлот-острова (тонн)'] = {
        'Воздушный маршрут Кантерлот-острова (тонно-километр)':4000,
        '_-Работы погрузочно-разгрузочные с планёра (тонн)':1 * 2,
        }

metadict_detail['Воздушный маршрут Кантерлот-Эверглейдс (тонн)'] = {
        'Воздушный маршрут Кантерлот-Эверглейдс (тонно-километр)':4000,
        '_-Работы погрузочно-разгрузочные с планёра (тонн)':1 * 2,
        }

metadict_detail['Воздушный маршрут Сталлионград-Кантерлот (тонн)'] = {
        'Воздушный маршрут Сталлионград-Кантерлот (тонно-километр)':1500,
        '_-Работы погрузочно-разгрузочные с планёра (тонн)':1 * 2,
        }

metadict_detail['Железнодорожное направление Сталлионград-Кантерлот (тонн)'] = {
        # TODO:
            # Вот здесь, через грузонапряжённость, можно узнать число необходимых путей
            # Например, 400 тонн в поезде, 15 поездов/сутки, 360 дней в году, это 2.16 млн. тонн
        'Железнодорожное направление Сталлионград-Кантерлот (тонно-километр)':2500,
        #'Железнодорожное направление Сталлионград-Кантерлот (число путей)':1 / (400 * 15 * 360),
        }

metadict_detail['Железнодорожное направление Кантерлот-Филлидельфия (тонн)'] = {
        'Железнодорожное направление Кантерлот-Филлидельфия (тонно-километр)':2000,
        '_-Работы погрузочно-разгрузочные с поезда (тонн)':1 * 2,
        }

metadict_detail['Железнодорожное направление Филлидельфия-Балтимэр (тонн)'] = {
        'Железнодорожное направление Филлидельфия-Балтимэр (тонно-километр)':1000,
        '_-Работы погрузочно-разгрузочные с поезда (тонн)':1 * 2,
        }

metadict_detail['Железнодорожное направление Филлидельфия-Мэйнхеттен (тонн)'] = {
        'Железнодорожное направление Филлидельфия-Мэйнхеттен (тонно-километр)':1000,
        '_-Работы погрузочно-разгрузочные с поезда (тонн)':1 * 2,
        }

metadict_detail['Морское направление Балтимэр-Эверглейдс (тонн)'] = {
        'Морское направление Балтимэр-Эверглейдс (тонно-километр)':3000,
        '_-Работы погрузочно-разгрузочные с барка (тонн)':1 * 2,
        }

metadict_detail['Морское направление Мэйнхеттен-острова (тонн)'] = {
        'Морское направление Мэйнхеттен-острова (тонно-километр)':1500,
        '_-Работы погрузочно-разгрузочные с барка (тонн)':1 * 2,
        }

metadict_detail['Морское направление Филлидельфия-Балтимэр (тонн)'] = {
        'Морское направление Филлидельфия-Балтимэр (тонно-километр)':1000,
        '_-Работы погрузочно-разгрузочные с барка (тонн)':1 * 2,
        }

metadict_detail['Морское направление Филлидельфия-Мэйнхеттен (тонн)'] = {
        'Морское направление Филлидельфия-Мэйнхеттен (тонно-километр)':1000,
        '_-Работы погрузочно-разгрузочные с барка (тонн)':1 * 2,
        }

metadict_detail['Речной маршрут Кантерлот-Балтимэр (тонн)'] = {
        'Речной маршрут Кантерлот-Балтимэр (тонно-километр)':2000,
        '_-Работы погрузочно-разгрузочные с баржи (тонн)':1 * 2,
        }

metadict_detail['Речной маршрут Клаудсдейл-Кантерлот (тонн)'] = {
        'Речной маршрут Клаудсдейл-Кантерлот (тонно-километр)':1000,
        '_-Работы погрузочно-разгрузочные с баржи (тонн)':1 * 2,
        }

metadict_detail['Речной маршрут село-город (тонн)'] = {
        'Речной маршрут село-город (тонно-километр)':100,
        '_-Работы погрузочно-разгрузочные с баржи (тонн)':1 * 2,
        }

metadict_detail['Наземный маршрут село-город (тонн)'] = {
        'Наземный маршрут село-город (тонно-километр)':50,
        '_-Работы погрузочно-разгрузочные с телеги (тонн)':1 * 2,
        }

metadict_detail['Наземный маршрут поле-деревня (тонн)'] = {
        # TODO: в среднем 1.5 километра.
        'Наземный маршрут поле-деревня (тонно-километр)':10,
        '_-Работы погрузочно-разгрузочные с телеги (тонн)':1 * 2,
        }

metadict_detail['Наземный маршрут город-мануфактура (тонн)'] = {
        'Наземный маршрут город-мануфактура (тонно-километр)':1,
        '_-Работы погрузочно-разгрузочные с телеги (тонн)':1 * 2,
        }

metadict_detail['Наземный маршрут стройплощадка-колодец (тонн)'] = {
        # Исправь
            # Набор воды механическим насосом.
            # https://www.ampika.ru/oborudovanie.html?id=5782
            # http://www.hms.ru/pumps_catalog/?ELEMENT_ID=6401&SECTION_ID=667
        'Наземный маршрут стройплощадка-колодец (тонно-километр)':1,
        '_-Работы погрузочно-разгрузочные с телеги насосом (тонн)':1 * 2,
        }

metadict_detail['Наземный маршрут город-свалка (тонн)'] = {
        # Исправь
            # Телега-самосвал.
        'Наземный маршрут город-свалка (тонно-километр)':1,
        '_-Работы погрузочно-разгрузочные с телегой-самосвалом (тонн)':1,
        }

metadict_detail['Наземный маршрут дом-опушка (тонн)'] = {
        # TODO:
            # На самом деле опушка должна быть дальше.
        'Наземный маршрут дом-опушка (тонно-километр)':0.5,
        '_-Работы погрузочно-разгрузочные с тележки (тонн)':1 * 2,
        }

metadict_detail['Наземный маршрут дом-колодец (тонн)'] = {
        # TODO:
            # Шахтные колодцы и колонки здорово отличаются по эффективности набора воды.
        'Наземный маршрут дом-колодец (тонно-километр)':0.3,
        '_-Работы погрузочно-разгрузочные с тележки вёдрами (тонн)':1 * 2,
        }

#----
# Грузоперевозки (группировка):

metadict_detail['Воздушный маршрут Кантерлот-Балтимэр (тонно-километр)'] = {
        'Воздушные грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Воздушный маршрут Кантерлот-Эверглейдс (тонно-километр)'] = {
        'Воздушные грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Воздушный маршрут Кантерлот-острова (тонно-километр)'] = {
        'Воздушные грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Воздушный маршрут Сталлионград-Кантерлот (тонно-километр)'] = {
        'Воздушные грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Железнодорожное направление Кантерлот-Филлидельфия (тонно-километр)'] = {
        'Железнодорожные грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Железнодорожное направление Сталлионград-Кантерлот (тонно-километр)'] = {
        'Железнодорожные грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Железнодорожное направление Филлидельфия-Балтимэр (тонно-километр)'] = {
        'Железнодорожные грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Железнодорожное направление Филлидельфия-Мэйнхеттен (тонно-километр)'] = {
        'Железнодорожные грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Морское направление Балтимэр-Эверглейдс (тонно-километр)'] = {
        'Морские грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Морское направление Мэйнхеттен-острова (тонно-километр)'] = {
        'Морские грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Морское направление Филлидельфия-Балтимэр (тонно-километр)'] = {
        'Морские грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Морское направление Филлидельфия-Мэйнхеттен (тонно-километр)'] = {
        'Морские грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Речной маршрут Кантерлот-Балтимэр (тонно-километр)'] = {
        'Речные грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Речной маршрут Клаудсдейл-Кантерлот (тонно-километр)'] = {
        'Речные грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Речной маршрут село-город (тонно-километр)'] = {
        'Речные грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Наземный маршрут село-город (тонно-километр)'] = {
        'Гужевые грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Наземный маршрут поле-деревня (тонно-километр)'] = {
        'Гужевые грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Наземный маршрут город-мануфактура (тонно-километр)'] = {
        'Гужевые грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Наземный маршрут стройплощадка-колодец (тонно-километр)'] = {
        'Гужевые грузоперевозки воды (тонно-километр)':1,
        }

metadict_detail['Наземный маршрут город-свалка (тонно-километр)'] = {
        'Гужевые грузоперевозки мусора (тонно-километр)':1,
        }

metadict_detail['Наземный маршрут дом-опушка (тонно-километр)'] = {
        'Вьючные грузоперевозки (тонно-километр)':1,
        }

metadict_detail['Наземный маршрут дом-колодец (тонно-километр)'] = {
        'Вьючные грузоперевозки воды (тонно-километр)':1,
        }

#----
# Грузоперевозки (трудозатраты):

metadict_detail['Воздушные грузоперевозки (тонно-километр)'] = {
        # TODO:
            # Блум убеждена, что воздушные грузоперевозки в Эквестрии выгоднее, чем по дорогам.
            # Да и расчёты это подтверждают. Нужно только расходы на обслуживание планёра уточнить.
        # Тяжёлый планёр (18 пегасов) летит со скоростью 80 км/час, несёт 3 тонны груза:
        # Лёгкий планёр (1 пегас) летит со скоростью 80 км/час, несёт 0.1 тонны груза:
        '_-Путь грузового планёра (часов)':1 / (80 * 3),
        '|===Грузооборот (тонно-километр)':1,
        }

metadict_detail['Гужевые грузоперевозки (тонно-километр)'] = {
        # Пегас тащит телегу по щебёночному шоссе со скоростью 20 км/час и несёт 0.5 тонны груза.
        '_-Путь грузовой телеги (часов)':1 / (20 * 0.5),
        '|===Грузооборот (тонно-километр)':1,
        }

metadict_detail['Гужевые грузоперевозки воды (тонно-километр)'] = {
        '_-Путь грузовой телеги-водовозки (часов)':1 / (20 * 0.5),
        '|===Грузооборот (тонно-километр)':1,
        }

metadict_detail['Гужевые грузоперевозки мусора (тонно-километр)'] = {
        '_-Путь грузовой телеги-самосвала (часов)':1 / (20 * 0.5),
        '|===Грузооборот (тонно-километр)':1,
        }

metadict_detail['Вьючные грузоперевозки (тонно-километр)'] = {
        # Пони рысит со скоростью 5 км/час и тащит 0.1 тонны груза на тележке:
        '_-Путь грузовой тележки (часов)':1 / (5 * 0.1),
        '|===Грузооборот (тонно-километр)':1,
        }

metadict_detail['Вьючные грузоперевозки воды (тонно-километр)'] = {
        # TODO:
            # Неэффективно до безобразия.
        '_-Путь грузовой тележки-водовозки (часов)':1 / (5 * 0.1),
        '|===Грузооборот (тонно-километр)':1,
        }

metadict_detail['Железнодорожные грузоперевозки (тонно-километр)'] = {
        # В среднем поезд загружен наполовину:
            # https://f-husainov.livejournal.com/520006.html
            # https://f-husainov.livejournal.com/611645.html
        # Грузовой поезд идёт со скоростью 50 км/час и тащит 250 тонн груза (25 вагонов по 10 тонн)
        '_-Путь грузового поезда (часов)':1 / (50 * 250),
        '|===Грузооборот (тонно-километр)':1,
        }

metadict_detail['Морские грузоперевозки (тонно-километр)'] = {
        # Барк идёт со скоростью 7 узлов (12.6 км/час) и тащит 1400 тонн груза:
        # http://wiki.wargaming.net/ru/Navy:Крузенштерн_(1926)
        '_-Путь грузового барка (часов)':1 / (12.6 * 1400),
        '|===Грузооборот (тонно-километр)':1,
        }

metadict_detail['Речные грузоперевозки (тонно-километр)'] = {
        # Баржа идёт со скоростью 5 узлов (9 км/час) и тащит 200 тонн груза:
        '_-Путь грузовой баржи (часов)':1 / (9 * 200),
        '|===Грузооборот (тонно-километр)':1,
        }
