#----
# Железнодорожные инструменты (дистанции пути):

metadict_detail['Оборудование дистанции пути'] = {
        # https://ru.wikisource.org/wiki/ЭСБЕ/Мастерские_железнодорожные
        'Тяжёлые машины дистанции пути':1,
        'Средства механизации путевых работ':1,
        'Контрольно-измерительные приборы дистанции пути':1,
        'Цеховое оборудование дистанции пути':1,
        'Оборудование малярного цеха':1,
        }

metadict_detail['Тяжёлые машины дистанции пути'] = {
        # Исправить
            # Маневровые локомотивы относятся к станциям.
        '|Дрезина (грузовая)':2,
        '|Дрезина (стреловой кран)':1,
        '|Кран железнодорожный козловой (10 тонн)':1,
        '|Кран железнодорожный портальный (для перевозки рельсов)':1,
        '|Дренажная машина железнодорожная':1,
        '|Локомотив маневровый':1,
        }

metadict_detail['Средства механизации путевых работ'] = {
        # http://www.tdesant.ru/info/item/6
        '|Домкрат винтовой (10 тонн)':10,
        '|Компрессор винтовой (30 кВт)':2,
        '|Домкрат гидравлический (20 тонн)':4,
        '|Насос для водоотлива механический':2,
        '|Молоток клепальный пневматический (2 кВт)':2,
        '|Перфоратор пневматический (1.5 кВт)':2,
        '|Бетонолом пневматический (2 кВт)':2,
        '|Дрель пневматическая (0.5 кВт)':1,
        '|Растворомешалка механическая':1,
        '|Бетономешалка механическая':1,
        }

metadict_detail['Контрольно-измерительные приборы дистанции пути'] = {
        '|Штангенциркуль (для измерения износа стрелочного перевода)':1,
        '|Тележка (для измерения волнообразного износа рельсов)':1,
        '|Термометр (для измерения температуры рельсов)':1,
        '|Прибор оптический (для рихтовки пути)':1,
        '|Шаблон КОР (для стрелочных переводов)':1,
        '|Скоба (для измерения износа рельс)':1,
        '|Тележка путеизмерительная':1,
        '|Шаблон путеизмерительный':1,
        '|Теодолит':1,
        '|Нивелир':1,
        }

metadict_detail['Цеховое оборудование дистанции пути'] = {
        # Исправить
            # Хорошая такая механическая мастерская.
            # Слишком хорошая для 19 века маленьких поняш.
            # Да нормально. Все эти упряжные грейдеры, скреперы, хай-тек телеги.
        # ЛТ-10 Станок токарно-винторезный универсальный
        # http://stanki-katalog.ru/sprav_lt10.htm
        # 2Г125 станок вертикально-сверлильный универсальный одношпиндельный
        # http://stanki-katalog.ru/sprav_2g125.htm
        '|Станок заточный (1 кВт)':2,
        '|Станок токарно-винторезный (3 кВт)':2,
        '|Станок поперечно-строгальный (7 кВт)':1,
        '|Станок универсально-фрезерный (3 кВт)':1,
        '|Станок универсально-шлифовальный (3 кВТ)':1,
        '|Станок вертикально-сверлильный (25 мм) (3 кВт)':2,
        '|Станок вертикально-сверлильный (75 мм) (12 кВт)':1,
        '|Молот ковочный пневматический (15 кВт)':2,
        '|Пресс гидравлический (40 тонн)':1,
        '|Лебёдка (0.5 тонны)':1,
        '|Таль (0.5 тонны)':1,
        }

metadict_detail['Оборудование малярного цеха'] = {
        '|Краскопульт':1,
        '|Моечная машина':1,
        '|Красконагнетательный бак':1,
        '|Краскораспылитель пневматический':1,
        '|Компрессор винтовой (30 кВт)':1,
        }

#----
# Железнодорожные инструменты (монтажной бригады):

metadict_detail['||Инструменты железнодорожника (комплект)'] = {
        # Бригада, это мобильное подразделение дистанции пути (ПЧ).
        'Инструменты железнодорожника (комплект бригады)':1 / 12,
        }

metadict_detail['Инструменты железнодорожника (комплект бригады)'] = {
        'Инструменты путевые (комплект бригады)':1,
        'Измерительные приборы путевые (комплект бригады)':1,
        'Инструменты путевые механизированные (комплект бригады)':1,
        'Инструменты для земляных работ (комплект бригады)':1,
        'Инструменты уборщика (комплект бригады)':1,
        'Инструменты слесаря (комплект бригады)':1,
        'Инструменты столяра (комплект бригады)':1,
        }

metadict_detail['Инструменты путевые (комплект бригады)'] = {
        # http://www.tdesant.ru/info/item/6
        '|Клещи шпальные':8,
        '|Шпалоноска':8,
        '|Лом лапчатый':8,
        '|Лом остроконечный':8,
        '|Молоток костыльный':8,
        '|Кувалда (5 килограмм)':1,
        '|Ключ путевой рожковый':8,
        '|Шпалоподбойка торцовая':10,
        '|Скоба (для перегонки шпал)':8,
        '|Дексель (для затёски шпал)':4,
        '|Ключ торцовый (гаечный)':10,
        '|Ключ торцовый (шурупный)':4,
        '|Наддёргиватель путевых костылей':10,
        '|Прибор стяжной (для перешивки пути)':2,
        '|Струбница (для стягивания накладок)':4,
        }

metadict_detail['Инструменты путевые механизированные (комплект бригады)'] = {
        '|Домкрат винтовой (10 тонн)':10,
        '|Станок рельсорезный (1.5 кВт)':1,
        '|Станок рельсосверлильный (1.5 кВт)':1,
        '|Станок рельсошлифовальный (1 кВт)':1,
        '|Путевой ключ механичесикй (0.4 кВт)':1,
        '|Шуруповёрт механический (1.7 кВт)':1,
        '|Пила механическая цепная (2 кВт)':2,
        '|Шпалоподбойка пневматическая (0.4 кВт)':1,
        '|Дрель пневматическая (0.5 кВт)':1,
        '|Компрессор винтовой (30 кВт)':2,
        '|Рихтовщик гидравлический':7,
        '|Разгонщик гидравлический':1,
        }

metadict_detail['Инструменты для земляных работ (комплект бригады)'] = {
        '|Вилы щебёночные':10,
        '|Когти для щебня':4,
        '|Трамбовка простая':3,
        '|Кирка остроконечная':12,
        '|Кружка мерная (для суфляжа)':2,
        '|Лопата штыковая':20,
        '|Лопата совковая':15,
        '|Лопата деревянная':25,
        '|Лопата суфляжная':4,
        }

metadict_detail['Инструменты слесаря (комплект бригады)'] = {
        '|Коловорот (по металлу)':4,
        '|Напильник трёхгранный (150 мм)':1,
        '|Клещи обыкновенные':1,
        '|Молоток слесарный':1,
        '|Зубило кузнечное':6,
        }

metadict_detail['Инструменты столяра (комплект бригады)'] = {
        # Исправить
            # Допиливай, вот список инструментов:
        # https://ru.wikisource.org/wiki/ЭСБЕ/Столярное_дело
        '|Коловорот (по дереву)':2,
        '|Зубило слесарное':4,
        '|Топор плотничий':4,
        '|Пила поперечная':3,
        '|Пила-ножовка':1,
        '|Рубанок':1,
        '|Долото':1,
        '|Стаместка':1,
        }

metadict_detail['Инструменты уборщика (комплект бригады)'] = {
        # Исправить
            # Вообще-то это для работы железнодорожников
        '|Ведро деревянное (10 литров)':6,
        '|Метла':2,
        }

metadict_detail['Измерительные приборы путевые (комплект бригады)'] = {
        '|Прозорник стыковой':1,
        '|Прозорник-прокладка':2,
        '|Угольник путевой (для проверки стыков)':2,
        '|Линейка метровая (для измерения неровностей рельсов)':1,
        '|Визирки (для определения величины просадок)':1,
        '|Зеркало (для осмотра рельсов)':4,
        '|Молоток (для остукивания рельсов)':2,
        '|Лупа (для осмотра рельсов)':4,
        '|Рулетка (30 метров)':1,
        '|Метр металлический':1,
        '|Обводной привод':1,
        '|Щуп (комплект)':2,
        '|Бинокль':1,
        }

#----
# Инструменты каменщика:

metadict_detail['||Инструменты каменщика (комплект)'] = {
        'Инструменты каменщика (комплект бригады)':1 / 12,
        }

metadict_detail['Инструменты каменщика (комплект бригады)'] = {
        # Технологическая карта на кладку стен из кирпича с расшивкой швов
        # http://www.gosthelp.ru/text/Texnologicheskayakartanak2.html
        # http://gardenweb.ru/instrument-prisposobleniya-inventar-kamenshchika
        '|Бункер для раствора (кубометр)':1,
        '|Ящик для раствора (0.35 кубометра)':4,
        '|Подмости панельные для кирпичной кладки':10,
        '|Футляр траверсный (грузоподъёмность 1.5 тонны)':1,
        '|Поддон с металлическими крючьями':1,
        '|Строп 4-х ветвевой (6 метров)':2,
        '|Строп кольцевой (20 метров)':1,
        '|Кельма для каменных работ':8,
        '|Молоток-кирочка':10,
        '|Отвес строительный':8,
        '|Уровень строительный':4,
        '|Рейка-порядовка':4,
        '|Правило':4,
        '|Рулетка металлическая':4,
        '|Лопата растворная':4,
        '|Линейка измерительная металлическая':4,
        '|Расшивка (выпуклая и вогнутая)':4,
        '|Лом монтажный':2,
        '|Шнур причальный (30 метров)':2,
        '|Скобы литые':8,
        '|Угольник для каменных работ':2,
        '|Ножовка по дереву широкая':2,
        '|Каска строительная пластиковая':12,
        '|Пояс монтажный':12,
        }

#----
# Инструменты штукатура:

metadict_detail['||Инструменты штукатура (комплект)'] = {
        'Инструменты штукатура (комплект бригады)':1 / 12,
        }

metadict_detail['Инструменты штукатура (комплект бригады)'] = {
        # Исправить
            # Отдели хотя бы измерительные приборы.
        # ТЕХНОЛОГИЧЕСКАЯ КАРТА НА ОШТУКАТУРИВАНИЕ ВНУТРЕННИХ КИРПИЧНЫХ ПОВЕРХНОСТЕЙ
        # ПРИ ПРОСТОЙ, УЛУЧШЕННОЙ И ВЫСОКОКАЧЕСТВЕННОЙ ШТУКАТУРКЕ
        # http://aquagroup.ru/normdocs/27#i2042671
        '|Кельма штукатурная':10,
        '|Отрезовка':8,
        '|Сокол дюралюминиевый':10,
        '|Ковш для отделочных работ':8,
        '|Лопата растворная':8,
        '|Кисть маховая':10,
        '|Кисть-макловица':10,
        '|Тёрка деревянная':10,
        '|Тёрка поролоновая':10,
        '|Гладилка стальная большая':8,
        '|Гладилка стальная малая':8,
        '|Полутёрка деревянная':10,
        '|Правило окованное':4,
        '|Правило усеночное':4,
        '|Правило прижимное':4,
        '|Шаблон для устройства откосов':4,
        '|Рейкодержатель универсальный':8,
        '|Рейкодержатель винтовой':5,
        '|Рейкодержатель дуговой':4,
        '|Рейкодержатель штыревой':10,
        '|Скребок':5,
        '|Бучарда штукатурная':5,
        '|Молоток штукатурный':8,
        '|Расшивка':8,
        '|Линейка для расшивки швов':8,
        '|Ножницы для резки металла':3,
        '|Острогубцы (кусачки)':3,
        '|Пила ножовка поперечная по дереву':5,
        '|Скрапели диаметром 8 и 10 мм':8,
        '|Уровень строительный':4,
        '|Уровень гибкий':2,
        '|Рулетки измерительные металлические':4,
        '|Шнур разметочный':8,
        '|Угольник специальный':4,
        '|Угольник деревянный':4,
        '|Метр складной металлический':8,
        '|Рейка с отвесом':2,
        '|Поэтажная ёмкость 0.35':2,
        '|Ведро деревянное (10 литров)':8,
        '|Инвентарные шарнирно-панельные подмостки':4,
        '|Вышка передвижная сборно-разборная':8,
        }

#----
# Инструменты маляра:

metadict_detail['||Инструменты маляра (комплект)'] = {
        # Звено из двух человек
        'Инструменты маляра (комплект бригады)':1 / 2,
        }


metadict_detail['Инструменты маляра (комплект бригады)'] = {
        # ТИПОВАЯ ТЕХНОЛОГИЧЕСКАЯ КАРТА НА ВОДОЭМУЛЬСИОННУЮ И МАСЛЯНУЮ ОКРАСКУ СТЕН И ПОТОЛКОВ
        # http://aquagroup.ru/normdocs/473
        '|Нож штукатурный':2,
        '|Шпатель малярный ШД-45':2,
        '|Шнур разметочный в корпусе':2,
        '|Шпатель малярный ШМ-75':2,
        '|Скребок металлический':1,
        '|Ванночка с сеткой':1,
        '|Кисть-ручник КР-35':2,
        '|Кисть флейцовая КФ-62':2,
        '|Кисть филенчатая':2,
        '|Кисть-макловица':2,
        '|Очки защитные':2,
        '|Респиратор ШБ1':2,
        '|Щётка торцевая ЩТ-1':2,
        '|Шпатель с ванночкой':2,
        '|Ведро деревянное (10 литров)':2,
        '|Рейка контрольная длиной 2 м':2,
        '|Столик складной двух высотный':2,
        '|Валик для окраски поверхностей':1,
        '|Приспособление для шлифовки поверхностей':2,
        }

#----
# Утварь домашняя:

metadict_detail['|Утварь кухонная (комплект)'] = {
        # http://www.molohovetc.ru/liv-ii/dinner_table/
        # http://www.molohovetc.ru/liv-ii/accessories/
        'Инструменты печные (комплект)':1,
        'Инструменты кухонные (комплект)':1,
        'Ёмкости кухонные (комплект)':1,
        'Приборы столовые (комплект)':1,
        }

metadict_detail['Инструменты печные (комплект)'] = {
        '|Кочерга литая':1,
        '|Метёлка печная':1,
        '|Щипцы для дров':1,
        '|Лопата печная':1,
        '|Совок печной':1,
        '|Ухват литой':2,
        '|Сковородник':1,
        '|Горшок для углей (10 литров)':1,
        }

metadict_detail['Инструменты кухонные (комплект)'] = {
        '|Жернова (1-кг/час)':1,
        '|Полотенце кухонное':4,
        '|Воронка кухонная':1,
        '|Доска для овощей':2,
        '|Доска для теста':1,
        '|Тёрка для овщей':2,
        '|Скалка кухонная':3,
        '|Ступка кухонная':2,
        '|Сито для муки':1,
        '|Дуршлаг кухонный':1,
        '|Лопатка кухонная':5,
        '|Нож-овощечистка':1,
        '|Щётка-овощемойка':1,
        '|Тесак кухонный (20 см)':1,
        '|Нож кухонный (10 см)':1,
        '|Нож кухонный (6 см)':1,
        '|Ножницы кухонные':1,
        '|Поварёшка стальная':2,
        '|Поварёшка деревянная':2,
        '|Решето рогожно-деревянное':1,
        }

metadict_detail['Ёмкости кухонные (комплект)'] = {
        '|Квашня деревянная (50 литров)':1,
        '|Ведро деревянное (10 литров)':1,
        '|Ковш деревянный (5 литров)':2,
        '|Миска глиняная (5 литров)':2,
        '|Миска глиняная (3 литра)':2,
        '|Котёл чугунный (50 литров)':1,
        '|Чугунок эмалированый (5 литров)':1,
        '|Таз эмалированный (10 литров)':1,
        '|Чайник фарфоровый (1 литр)':1,
        '|Самовар медный (5 литров)':1,
        '|Горшок печной (5 литров)':1,
        '|Горшок печной (2 литра)':2,
        '|Горшок печной (1 литр)':1,
        '|Сковорода (5 литров)':1,
        '|Сковорода (2 литра)':1,
        '|Сотейник (2 литра)':1,
        '|Чугунок (5 литров)':1,
        '|Чугунок (3 литра)':1,
        '|Чугунок (1 литр)':1,
        '|Кувшин (5 литров)':1,
        '|Кувшин (3 литра)':1,
        '|Форма для выпечки':5,
        '|Противень жестяной':2,
        }

metadict_detail['Приборы столовые (комплект)'] = {
        # А ложками пони не пользуются
        '|Нож столовый':2,
        '|Блюдо для еды (2 литра)':2,
        '|Миска для еды (1 литр)':5,
        '|Блюдце для еды (0.5 литра)':5,
        '|Кружка для питья (1.5 литра)':5,
        '|Чашка для питья (0.5 литра)':5,
        '|Ковшик для питья (1 литр)':2,
        }