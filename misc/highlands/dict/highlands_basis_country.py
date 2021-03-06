#----
# География мира:

metadict_army['Мир'] = {
        # Повёрнутая ориентация климата.
            # Северные страны жаркие, южные холодные.
        'Центр событий':1,
        #'Ближние страны':1,
        #'Дальний север (Страна чудес)':1,
        #'Дальний запад (Западный мир)':1,
        #'Дальний юг (Страна лесов)':1,
        }

metadict_army['Центр событий'] = {
        # https://ru.wikisource.org/wiki/ЭСБЕ/Кавказский_край
        'Страна центрального предгорья':1,
        }

metadict_army['Ближние страны'] = {
        # Исправить
        # Уточнить
            # Не мешало бы узнать число жителей.
        'Страна северного загорья':1,
        'Страна северной загорной реки':1,
        'Страна южная степная (Племена кочевников)':1,
        'Страна юго-восточная (Горного прохода)':1,
        }

metadict_army['Дальний запад (Западный мир)'] = {
        # Исправить
        # Уточнить
            # Это группа стран, нужно знать число жителей (хотя бы в общем).
            # Ибо больше жителей --> больше богатеев --> больше торговцев на пути --> больше грузооборот
            # А если грузооборота не хватает, то растёт ценность редких товаров.
        }

metadict_army['Дальний север (Страна чудес)'] = {
        }

metadict_army['Дальний юг (Страна лесов)'] = {
        }

#----
# Страны:

metadict_army['Страна центрального предгорья'] = {
        # Исправить
        # Уточнить
            # Кавказские горы -- 500 км. хребет между морями.
            # Страна примерно 500x500 километров, 250 000 км², три Андалузии, три Грузии.
            # Население: селяне 1 млн; горожане 150 тыс (4.6 человека/кв.километр)
                # Населения явно недостаточно.
            # https://ru.wikipedia.org/wiki/Грузинское_царство
                # Площадь 1213-1245 г. - Более 380 000 км² Население 5 млн. (13 чел/кв.км)
            # Вероятно, границы регионов совпадают с расселением племён (отдельные языки/диалекты)
                # http://wikiredia.ru/wiki/Лезгинские_народы
        'Регион северный приграничный горный':3,
        'Регион северный загорный прибрежный':1,
        'Регион северный предгорный':1,
        'Регион столичный прибрежный':1,
        'Регион центральный речной':1,
        'Регион восточный речной':3,
        'Регион южный приграничный степной':4,
        }

#----
# Регионы:

metadict_army['Регион северный загорный прибрежный'] = {
        # Торговля зерном
        'Владение северного загорного прибрежного города':1,
        'Владение северных загорных латифундрий':6,
        'Владение северных загорных кланов':4,
        '-----Регионы':1,
        }

metadict_army['Регион столичный прибрежный'] = {
        # Судостроение, путь в Западный мир
        'Владение столичного прибрежного города':1,
        'Владение западных прибрежных латифундрий':4,
        'Приграничье западных равнинных кланов':2,
        'Владение западных равнинных кланов':6,
        '-----Регионы':1,
        }

metadict_army['Регион центральный речной'] = {
        # Место событий
        'Владение центрального речного города':1,
        'Владение срединных равнинных кланов':4,
        '-----Регионы':1,
        }

metadict_army['Регион восточный речной'] = {
        'Владение восточного речного города':1,
        'Владение восточных равнинных кланов':4,
        '-----Регионы':1,
        }

metadict_army['Регион северный предгорный'] = {
        # Торговый путь через горный проход.
        'Владение северного приграничного города':1,
        'Владение северных горных кланов':4,
        '-----Регионы':1,
        }

metadict_army['Регион северный приграничный горный'] = {
        # Приграничные укреплённые селения
        'Приграничье северных горных кланов':1,
        'Владение северных горных кланов':2,
        '-----Регионы':1,
        }

metadict_army['Регион южный приграничный степной'] = {
        'Приграничье южных степных кланов':1,
        'Владение южных степных кланов':2,
        '-----Регионы':1,
        }

#----
# Округа:

metadict_army['Владение северного загорного прибрежного города'] = {
        # Крупные землевладельцы давно скупили/захватили все земли близ города.
        # Латифундрии поставляют зерно как на рынок города, так и на экспорт.
        'Город северный загорный прибрежный':1,
        'Латифундрия равнинная':50,
        '----Округа':1,
        }

metadict_army['Владение столичного прибрежного города'] = {
        'Город столичный прибрежный':1,
        'Латифундрия равнинная':50,
        '----Округа':1,
        }

metadict_army['Владение центрального речного города'] = {
        'Город центральный речной':1,
        'Латифундрия равнинная':25,
        '----Округа':1,
        }

metadict_army['Владение восточного речного города'] = {
        'Город восточный речной':1,
        'Латифундрия равнинная':25,
        '----Округа':1,
        }

metadict_army['Владение северного приграничного города'] = {
        # Город на перевале и торговом пути. Вероятно, импортирует еду.
        'Город северный предгорный':1,
        'Городище северное горное':2,
        'Селение горное':15,
        '----Округа':1,
        }

metadict_army['Приграничье северных горных кланов'] = {
        # Исправить
            # Укреплённые сёла на перевалах и сторожевые башни.
        'Городище северное горное':5,
        '----Округа':1,
        }

metadict_army['Приграничье западных равнинных кланов'] = {
        'Городище северное равнинное':5,
        '----Округа':1,
        }

metadict_army['Приграничье южных степных кланов'] = {
        # Исправить
            # Крепости с 50-100 всадников на расстоянии 25 км друг от друга.
        'Городище южное степное':10,
        '----Округа':1,
        }

metadict_army['Владение северных загорных латифундрий'] = {
        'Латифундрия равнинная':25,
        '----Округа':1,
        }

metadict_army['Владение западных прибрежных латифундрий'] = {
        'Латифундрия равнинная':25,
        '----Округа':1,
        }

metadict_army['Владение северных загорных кланов'] = {
        'Городище северное равнинное':1,
        'Селение равнинное':25,
        '----Округа':1,
        }

metadict_army['Владение западных равнинных кланов'] = {
        'Городище западное равнинное':1,
        'Селение равнинное':25,
        '----Округа':1,
        }

metadict_army['Владение срединных равнинных кланов'] = {
        'Городище срединное равнинное':1,
        'Селение равнинное':25,
        '----Округа':1,
        }

metadict_army['Владение восточных равнинных кланов'] = {
        'Городище восточное равнинное':1,
        'Селение равнинное':25,
        '----Округа':1,
        }

metadict_army['Владение северных горных кланов'] = {
        'Городище северное горное':1,
        'Селение горное':25,
        '----Округа':1,
        }

metadict_army['Владение южных степных кланов'] = {
        'Городище южное степное':1,
        'Селение степное':25,
        '----Округа':1,
        }

#----
# Города:

metadict_army['Город северный загорный прибрежный'] = {
        # Исправить
            # Позже разделим гильдии по их специализации.
            # Пока что гильдии по числу Данбара (50-250 членов, медиана 150)
            # Не забудь, что есть семьи и вне гильдий (а также торговые представители)
        # Городское население:
            # Потомки переселенцев -- 70%
            # Местные горцы -- 25%
            # Приезжие/торговцы -- 5% (4.5 тысячи человек на всю страну)
        # 5% карлов
        'Гильдия ремесленников':190,
        'Община карликов-рабов':10,
        '---Города':1,
        }

metadict_army['Город столичный прибрежный'] = {
        # 30% карлов
        'Гильдия ремесленников':140,
        'Община карликов-рабов':60,
        '---Города':1,
        }

metadict_army['Город центральный речной'] = {
        # Место событий
        # 40% карлов
        'Гильдия ремесленников':80,
        'Община карликов-рабов':50,
        '---Города':1,
        }

metadict_army['Город восточный речной'] = {
        # 20% карлов.
        'Гильдия ремесленников':80,
        'Община карликов-рабов':20,
        '---Города':1,
        }

metadict_army['Город северный предгорный'] = {
        # Стоит на торговом пути через перевал.
        # 10% карлов
        'Гильдия ремесленников':60,
        'Община карликов-рабов':7,
        '---Города':1,
        }

metadict_army['Городище северное горное'] = {
        # Исправить
        # Уточнить
            # Живут селяне, но по задачам это административные центры, то есть города.
            # Здесь может быть клан чисто воинского сословия, а заодно и самый богатый в регионе.
            # Здесь должен быть клан воинского сословия. 50 всадников, не меньше.
        # Приграничные укреплённые поселения (2-5k жителей)
        'Клан горцев':12,
        'Община крестьян-арендаторов':4,
        '---Городища':1,
        }

metadict_army['Городище южное степное'] = {
        'Клан степняков':12,
        'Община крестьян-арендаторов':4,
        '---Городища':1,
        }

metadict_army['Городище восточное равнинное'] = {
        'Клан равнин':12,
        'Община крестьян-арендаторов':4,
        '---Городища':1,
        }

metadict_army['Городище западное равнинное'] = {
        'Клан равнин':12,
        'Община крестьян-арендаторов':4,
        '---Городища':1,
        }

metadict_army['Городище северное равнинное'] = {
        'Клан равнин':12,
        'Община крестьян-арендаторов':4,
        '---Городища':1,
        }

metadict_army['Городище срединное равнинное'] = {
        'Клан равнин':12,
        'Община крестьян-арендаторов':4,
        '---Городища':1,
        }

#----
# Селения:

metadict_army['Латифундрия равнинная'] = {
        # Исправить
            # Позже раздели латифундрии на специализированные хозяйства.
            # Табак, виноград, лён, маслины.
        # Усадьба, где живёт глава латифундрии с семьёй и челядью, плюс 3-4 поселения колонов/рабов.
            # https://ru.wikipedia.org/wiki/Колон_(сословие)
            # Владельцы и челядь -- потомки переселенцев, 
            # Платят налоги прилегающему городу.
        'Клан землевладельцев латифундрии':1,
        'Община крестьян-колонов':2,
        'Община крестьян-арендаторов':1,
        '---Селения':1,
        }

metadict_army['Селение равнинное'] = {
        # Клан -- родственники, община -- соседи (часто арендаторы)
            # 2-4 клана мирно сосуществуют, женятся между собой.
        # Общинники арендуют землю у землевладельцев и живут под защитой клана.
            # Это неудачливые семьи, должники, бывшие рабы.
        # Пшеница, ячмень, чечевица, виноград (на изюм).
        'Клан равнин':3,
        'Община крестьян-арендаторов':1,
        '---Селения':1,
        }

metadict_army['Селение горное'] = {
        # В горах и степях приграничья общин арендаторов нет (уходят на равнины)
        'Клан горцев':3,
        '---Селения':1,
        }

metadict_army['Селение степное'] = {
        'Клан степняков':4,
        '---Селения':1,
        }

#----
# Гильдии, кланы:

metadict_army['Гильдия ремесленников'] = {
        'Семья владельцев гильдии':4,
        'Семья ремесленников':16,
        '--Общины':1,
        }

metadict_army['Клан землевладельцев латифундрии'] = {
        # Усадьба -- коллективная собственность.
        # Наследование, от главы к преемнику (в пределах семьи)
        'Семья землевладельцев латифундрии':4,
        'Семья челяди латифундрии':16,
        '--Общины':1,
        }

metadict_army['Клан равнин'] = {
        # Род - это общность семей, где самый старший - старейшина,
        # Наследование, к самому старшему или авторитетному члену.
        'Семья землевладельцев клана':1,
        'Семья землепользователей клана':4 * 2,
        'Семья скотоводов клана':4 * 2,
        '--Общины':1,
        }

metadict_army['Клан горцев'] = {
        # Исправить
        # Уточнить
            # Пока что скотоводов и земледельцев поровну.
            # За образец берём лезгинские тохумы:
                # Земельные отчуждения в пользу чужеродцев не допускаются
                # https://ru.wikisource.org/wiki/ЭСБЕ/Тохум
        'Семья землевладельцев клана':1,
        'Семья землепользователей клана':4 * 2,
        'Семья скотоводов клана':4 * 2,
        '--Общины':1,
        }

metadict_army['Клан степняков'] = {
        'Семья землевладельцев клана':1,
        'Семья скотоводов клана':4 * 3,
        'Семья землепользователей клана':4 * 1,
        '--Общины':1,
        }

metadict_army['Община крестьян-колонов'] = {
        'Семья крестьян-колонов':20,
        '--Общины':1,
        }

metadict_army['Община крестьян-арендаторов'] = {
        # https://ru.wikisource.org/wiki/ЭСБЕ/Задруга
        # https://ru.wikisource.org/wiki/ЭСБЕ/Поземельная_община
        'Семья крестьян-арендаторов':20,
        '--Общины':1,
        }

metadict_army['Община карликов-рабов'] = {
        # Семьи в 30 членов
        'Семья карликов-рабов':5,
        '--Общины':1,
        }

#----
# Семьи:

metadict_army['Семья ремесленников'] = {
        # Структура дворохозяйства
            # http://vln.by/book-village/part3_5.htm
        'Горожане-бедняки':6,
        'Семейные рабы горожан':1,
        '-Семьи':1,
        }

metadict_army['Семья землепользователей клана'] = {
        # Модель жизненного цикла крестьянского дворохозяйства
            # http://vln.by/node/117
        'Крестьяне-бедняки землевладельцы':6,
        'Семейные рабы землевладельцев':1,
        '-Семьи':1,
        }

metadict_army['Семья скотоводов клана'] = {
        'Крестьяне-бедняки скотоводы':8,
        'Семейные рабы скотоводов':1,
        '-Семьи':1,
        }

metadict_army['Семья владельцев гильдии'] = {
        'Знать городская':8,
        'Семейные рабы горожан':2,
        '-Семьи':1,
        }

metadict_army['Семья землевладельцев клана'] = {
        'Знать клановая':8,
        'Семейные рабы землевладельцев':4,
        '-Семьи':1,
        }

metadict_army['Семья землевладельцев латифундрии'] = {
        'Знать латифундрии':5,
        'Семейные рабы землевладельцев':4,
        '-Семьи':1,
        }

metadict_army['Семья челяди латифундрии'] = {
        'Челядь латифундрии':5,
        'Семейные рабы землевладельцев':2,
        '-Семьи':1,
        }

metadict_army['Семья крестьян-колонов'] = {
        'Крестьяне-бедняки колоны':6,
        '-Семьи':1,
        }

metadict_army['Семья крестьян-арендаторов'] = {
        'Крестьяне-бедняки арендаторы':6,
        '-Семьи':1,
        }

metadict_army['Семья карликов-рабов'] = {
        'Карлики-рабы':30,
        '-Семьи':1,
        }
