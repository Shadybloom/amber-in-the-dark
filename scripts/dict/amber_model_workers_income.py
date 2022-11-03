#----
# Заметки:
    # Монетная масса в обороте (1896 год):
        # США (на 10 жителей) -- 159 рублей золота + 108 руб серебра, 84 рубля банкнот и разменных монет.
        # Россия (на 10 жителей) -- 97 рублей золота, 25 рублей банкнот и разменных монет.
        # Рубль (1897 года) = 0.774 грамма чистого золота (18 грамм серебра)
    # Монетная масса на 10 тысяч жителей:
        # Страна          | Золото      | Серебро      | Разменная монета | Непокрытые билеты
        # --------------- | ----------- | ------------ | ---------------- | -----------------
        # США (76 млн)    | 123 кг      | 1 950 кг     | 15 кг зол. экв.  | 50 кг зол. эвк.
        # Германия (52.5) | 199         |   495        | 33               | 46
        # Россия (97)     |  75         |    11        |  7               | 12
        # Рубль (1897 года) = 0.774 грамма чистого золота (18 грамм серебра)
    # Монетная масса и запасы казначейств (1895 год) -- в тоннах драгоценных металлов:
        # Страна          | Золото      | Серебро      | Разменная монета | Непокрытые билеты
        # --------------- | ----------- | ------------ | ---------------- | -----------------
        # Франция         |  1 334 тонн |  16 640 тонн |   76 т зол. экв. |    28 т зол. экв.
        # Англия          |  1 044      |   3 640      |  203             |     -
        # Германия        |  1 044      |   2 600      |  174             |   242
        # Австро-Венгрия  |    267      |   2 132      |   61             |   152
        # Голландия       |     41      |   1 508      |    5             |    60
        # Италия          |    154      |     416      |   38             |   236
        # Россия          |    728      |     104      |   67             |   118
        # Испания         |     58      |   2 860      |   59             |   155
        # Бельгия         |     81      |   1 076      |   12             |   104
        # США             |    931      |  14 820      |  116             |   377
        # Итого           |  5 786      |  42 120      |  810             | 1 527 
        # Оттомар Гаупт "Reuler’s Finanz Chronik" (1896 г. № 7)
        # https://ru.wikisource.org/wiki/ЭСБЕ/Монетная_регалия
    # Добыча золота (1900 год): 
        # Страна             | Золота
        # ------------------ | ---------------
        # США (всего)        | 118.2 тонны/год
        # США (Аляска)       |  33.5
        # Австралия          | 113.2
        # Африка             |  58.5
        # Канада             |  39.1
        # Россия (всего)     |  34.7
        # Россия (Сибирь)    |  26.0
        # Мексика            |  15.2
        # Британская Империя |  14.4
        # Китай              |  13.1
        # Корея              |   5.2
        # Колумбия           |   3.8
        # Итого              | 415.4
        # Золотой запас России (1914 год) -- 2 196 тонн (1 312 центробанк, 362 тонн обращ, добыча 62 тонн/год)
        # Монетная масса (1914) -- 362.1 тонн золота, 2 198 тонн серебра; 18.5 млн. рублей в медной монете.
        # История российской золотодобычи в датах. Факты и события начиная с 1900 года
        # https://zolotodb.ru/article/11637
        # https://zolotodb.ru/article/12327

#----
# Разовые услуги --> почасовая оплата

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 1 круг (1_бит/ячейка*10_минут)'] = {
        # Число ячеек заклинаний ограничено правилами DnD 5e. Таблицы в spells
        '_-$Обслуживание-медицина, волшебник-врач, 1 круг (6_бит*нормо-час)':1 / 6,
        '-Заклинания использованные, стоимость (бит)':1,
        }

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 1 круг (1_бит/ячейка*60_минут)'] = {
        '_-$Обслуживание-медицина, волшебник-врач, 1 круг (1_бит*нормо-час)':1 / 1,
        '-Заклинания использованные, стоимость (бит)':1,
        }

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 2 круг (1.5_бит/ячейка*10_минут)'] = {
        '_-$Обслуживание-медицина, волшебник-врач, 2 круг (9_бит/нормо-час)':1 / 6,
        '-Заклинания использованные, стоимость (бит)':1.5,
        }

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 3 круг (2.2_бит/ячейка*10_минут)'] = {
        '_-$Обслуживание-медицина, волшебник-врач, 3 круг (12_бит/нормо-час)':1 / 6,
        '-Заклинания использованные, стоимость (бит)':2.2,
        }

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 4 круг (7_бит/ячейка*10_минут)'] = {
        '_-$Обслуживание-медицина, волшебник-врач, 4 круг (42_бит/нормо-час)':1 / 6,
        '-Заклинания использованные, стоимость (бит)':7,
        }

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 5 круг (20_бит/ячейка*60_минут)'] = {
        '_-$Обслуживание-медицина, волшебник-врач, 5 круг (20_бит/нормо-час)':1 / 1,
        '-Заклинания использованные, стоимость (бит)':20,
        }

metadict_model['_-$Промышленность-кустари, волшебник-светокристаллы, 2 круг (1.5_бит/ячейка*10_минут)'] = {
        '_-$Промышленность-кустари, волшебник-светокристаллы, 2 круг (9_бит/нормо-час)':1 / 6,
        '-Заклинания использованные, стоимость (бит)':1.5,
        }

#----
# Категории профессиий

metadict_model['_-$Земледелие, бобовые (0.3_бит*нормо-час)'] = {
        '_-$$Земледелие (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Земледелие, грибовод (0.4_бит*нормо-час)'] = {
        '_-$$Земледелие (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Земледелие, зебра (0.1_бит*нормо-час)'] = {
        '_-$$Земледелие (0.1_бит*нормо-час)':1,
        }

metadict_model['_-$Земледелие, зерновые (0.3_бит*нормо-час)'] = {
        '_-$$Земледелие (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Земледелие, лесник (0.4_бит*нормо-час)'] = {
        '_-$$Земледелие (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Земледелие, масличные (0.2_бит*нормо-час)'] = {
        '_-$$Земледелие (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Земледелие, масличные (0.3_бит*нормо-час)'] = {
        '_-$$Земледелие (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Земледелие, огородник (0.2_бит*нормо-час)'] = {
        '_-$$Земледелие (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Земледелие, пчеловод (0.5_бит*нормо-час)'] = {
        '_-$$Земледелие (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Земледелие, садовод (0.2_бит*нормо-час)'] = {
        '_-$$Земледелие (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Земледелие, технические (0.2_бит*нормо-час)'] = {
        '_-$$Земледелие (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Земледелие, технические (0.3_бит*нормо-час)'] = {
        '_-$$Земледелие (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Земледелие, сушка (0.2_бит*нормо-час)'] = {
        '_-$$Земледелие (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-культура, библиотекарь (0.5_бит*нормо-час)'] = {
        '_-$$Обслуживание-культура (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 1 круг (1_бит*нормо-час)'] = {
        '_-$$Обслуживание-медицина (1_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 1 круг (6_бит*нормо-час)'] = {
        '_-$$Обслуживание-медицина (6_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 2 круг (1.5_бит*нормо-час)'] = {
        '_-$$Обслуживание-медицина (1.5_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 2 круг (9_бит/нормо-час)'] = {
        '_-$$Обслуживание-медицина (9_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 3 круг (2_бит*нормо-час)'] = {
        '_-$$Обслуживание-медицина (2_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 3 круг (12_бит/нормо-час)'] = {
        '_-$$Обслуживание-медицина (12_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 4 круг (42_бит/нормо-час)'] = {
        '_-$$Обслуживание-медицина (42_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, волшебник-врач, 5 круг (20_бит/нормо-час)'] = {
        '_-$$Обслуживание-медицина (20_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, врач, больница (1_бит*нормо-час)'] = {
        '_-$$Обслуживание-медицина (1_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, врач, поликлиника (1_бит*нормо-час)'] = {
        '_-$$Обслуживание-медицина (1_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, фельдшер, больница (0.5_бит*нормо-час)'] = {
        '_-$$Обслуживание-медицина (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, фельдшер, поликлиника (0.5_бит*нормо-час)'] = {
        '_-$$Обслуживание-медицина (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, фельдшер, скорая помощь (0.5_бит*нормо-час)'] = {
        '_-$$Обслуживание-медицина (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-медицина, фельдшер, скорая помощь, пегас (0.5_бит*нормо-час)'] = {
        '_-$$Обслуживание-медицина (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-образование, учитель, начальная школа (0.5_бит*нормо-час)'] = {
        '_-$$Обслуживание-образование (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-образование, учитель, средняя школа (0.5_бит*нормо-час)'] = {
        '_-$$Обслуживание-образование (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-образование, учитель, старшая школа (0.5_бит*нормо-час)'] = {
        '_-$$Обслуживание-образование (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-образование, учитель, университет (1_бит*нормо-час)'] = {
        '_-$$Обслуживание-образование (1_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-кулинария, повар (0.5_бит*нормо-час)'] = {
        '_-$$Обслуживание-кулинария (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-кулинария, поварёнок (0.3_бит*нормо-час)'] = {
        '_-$$Обслуживание-кулинария (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-хозяйство, прачка (0.3_бит*нормо-час)'] = {
        '_-$$Обслуживание-хозяйство (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Обслуживание-хозяйство, уборщик (0.3_бит*нормо-час)'] = {
        '_-$$Обслуживание-хозяйство (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-добыча, волшебник-шахтёр, 0 круг (1_бит*нормо-час)'] = {
        '_-$$Промышленность-добыча (1_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-добыча, рабочий, лесоруб (0.3_бит*нормо-час)'] = {
        '_-$$Промышленность-добыча (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-добыча, рабочий, лесоруб (0.2_бит*нормо-час)'] = {
        '_-$$Промышленность-добыча (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-добыча, землекоп, глина (0.2_бит*нормо-час)'] = {
        '_-$$Промышленность-добыча (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-добыча, землекоп, торф (0.3_бит*нормо-час)'] = {
        '_-$$Промышленность-добыча (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-добыча, рабочий, сапёр (2_бит*нормо-час)'] = {
        '_-$$Промышленность-добыча (2_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-добыча, рабочий, шахтёр (0.5_бит*нормо-час)'] = {
        '_-$$Промышленность-добыча (0.5_бит*нормо-час)':1,
        }

metadict_detail['_-$Промышленность-добыча, рабочий, обогащение (0.5_бит*нормо-час)'] = {
        '_-$$Промышленность-добыча (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-добыча, рабочий, шахтёр, щебень (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-добыча (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-кустари, рабочий, портной (1_бит*нормо-час)'] = {
        '_-$$Промышленность-кустари (1_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-кустари, рабочий, сапожник (1_бит*нормо-час)'] = {
        '_-$$Промышленность-кустари (1_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-кустари, рабочий, ткач (0.2_бит*нормо-час)'] = {
        '_-$$Промышленность-кустари (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-кустари, рабочий, швец (0.5_бит*нормо-час)'] = {
        '_-$$Промышленность-кустари (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-кустари, рабочий, керамика (0.5_бит*нормо-час)'] = {
        '_-$$Промышленность-кустари (0.5_бит*нормо-час)':1,
        }

metadict_detail['_-$Промышленность-кустари, рабочий, корзины (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-кустари (0.4_бит*нормо-час)':1,
        }

metadict_detail['_-$Промышленность-кустари, рабочий, бондарь (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-кустари (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-кустари, волшебник-светокристаллы, 2 круг (9_бит/нормо-час)'] = {
        '_-$$Промышленность-кустари (9_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, дёготь (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, известь (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, кафель (0.5_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, кирпич (0.3_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, кирпич саманный (0.2_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, кирпич саманный (0.3_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, красильщик (0.3_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, красильщик (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, лесопилка (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, маслозавод (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, мыловар (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, опилкобетон (0.3_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, паркет (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, мукомол (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, пивоварня (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, прядильщик (0.3_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, прядильщик (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, солевар (0.5_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, солод (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, типография (0.5_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, типография (1_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (1_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, ткач (0.5_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, хлебозавод (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Промышленность-фабрики, рабочий, цемент (0.4_бит*нормо-час)'] = {
        '_-$$Промышленность-фабрики (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Собирательство, валежник (0.1_бит*нормо-час)'] = {
        '_-$$Собирательство (0.1_бит*нормо-час)':1,
        }

metadict_model['_-$Собирательство, водоросли (0.3_бит*нормо-час)'] = {
        '_-$$Собирательство (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Собирательство, дикорастущие грибы (0.1_бит*нормо-час)'] = {
        '_-$$Собирательство (0.1_бит*нормо-час)':1,
        }

metadict_model['_-$Собирательство, дикорастущие орехи (0.1_бит*нормо-час)'] = {
        '_-$$Собирательство (0.1_бит*нормо-час)':1,
        }

metadict_model['_-$Собирательство, дикорастущие растения (0.1_бит*нормо-час)'] = {
        '_-$$Собирательство (0.1_бит*нормо-час)':1,
        }

metadict_model['_-$Собирательство, дикорастущие ягоды (0.1_бит*нормо-час)'] = {
        '_-$$Собирательство (0.1_бит*нормо-час)':1,
        }

metadict_model['_-$Собирательство, зебры, дикорастущие растения (0.1_бит*нормо-час)'] = {
        '_-$$Собирательство (0.1_бит*нормо-час)':1,
        }

metadict_model['_-$Собирательство, кленовый сок (0.1_бит*нормо-час)'] = {
        '_-$$Собирательство (0.1_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, волшебник-сварщик, 0 круг (1_бит*нормо-час)'] = {
        '_-$$Строительство (1_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, дорожный строитель (0.2_бит*нормо-час)'] = {
        '_-$$Строительство (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, железнодорожный монтёр (0.3_бит*нормо-час)'] = {
        '_-$$Строительство (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, землекоп (0.1_бит*нормо-час)'] = {
        '_-$$Строительство (0.1_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, землекоп (0.2_бит*нормо-час)'] = {
        '_-$$Строительство (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, каменщик (0.3_бит*нормо-час)'] = {
        '_-$$Строительство (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, каменщик, печник (0.5_бит*нормо-час)'] = {
        '_-$$Строительство (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, кровельщик (0.2_бит*нормо-час)'] = {
        '_-$$Строительство (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, маляр (0.3_бит*нормо-час)'] = {
        '_-$$Строительство (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, плотник (0.2_бит*нормо-час)'] = {
        '_-$$Строительство (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, плотник (0.3_бит*нормо-час)'] = {
        '_-$$Строительство (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, разнорабочий (0.2_бит*нормо-час)'] = {
        '_-$$Строительство (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, разнорабочий-пегас (0.2_бит*нормо-час)'] = {
        '_-$$Строительство (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Строительство, штукатур (0.3_бит*нормо-час)'] = {
        '_-$$Строительство (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, водовоз (0.1_бит*нормо-час)'] = {
        '_-$$Транспорт (0.1_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, водовоз-пегас (0.2_бит*нормо-час)'] = {
        '_-$$Транспорт (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, водовоз-земнопони (0.2_бит*нормо-час)'] = {
        '_-$$Транспорт (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, водопроводчик (0.4_бит*нормо-час)'] = {
        '_-$$Транспорт (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, возничий-зебра (0.1_бит*нормо-час)'] = {
        '_-$$Транспорт (0.1_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, возничий-пегас (0.2_бит*нормо-час)'] = {
        '_-$$Транспорт (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, возничий-земнопони (0.2_бит*нормо-час)'] = {
        '_-$$Транспорт (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, грузчик (0.2_бит*нормо-час)'] = {
        '_-$$Транспорт (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, грузчик-зебра (0.1_бит*нормо-час)'] = {
        '_-$$Транспорт (0.1_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, железнодорожник (0.4_бит*нормо-час)'] = {
        '_-$$Транспорт (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, железнодорожник-пегас (0.3_бит*нормо-час)'] = {
        '_-$$Транспорт (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, лётчик-пегас (0.5_бит*нормо-час)'] = {
        '_-$$Транспорт (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, лётчик-пегас (1_бит*нормо-час)'] = {
        '_-$$Транспорт (1_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, моряк (0.3_бит*нормо-час)'] = {
        '_-$$Транспорт (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, моряк (1_бит*нормо-час)'] = {
        '_-$$Транспорт (1_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, моряк (2_бит*нормо-час)'] = {
        '_-$$Транспорт (2_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, моряк (4_бит*нормо-час)'] = {
        '_-$$Транспорт (4_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, моряк-пегас (0.3_бит*нормо-час)'] = {
        '_-$$Транспорт (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, почтальон-пегас (0.4_бит*нормо-час)'] = {
        '_-$$Транспорт (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, почтовый служащий (0.5_бит*нормо-час)'] = {
        '_-$$Транспорт (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, путевой смотритель (0.4_бит*нормо-час)'] = {
        '_-$$Транспорт (0.4_бит*нормо-час)':1,
        }

metadict_model['_-$Транспорт, таксист-пегас (0.5_бит*нормо-час)'] = {
        '_-$$Транспорт (0.5_бит*нормо-час)':1,
        }

metadict_model['_-$Домохозяйство, повар (0.3_бит*нормо-час)'] = {
        '_-$$Домохозяйство (0.3_бит*нормо-час)':1,
        }

metadict_model['_-$Домохозяйство, поварёнок (0.2_бит*нормо-час)'] = {
        '_-$$Домохозяйство (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Домохозяйство, прачка (0.2_бит*нормо-час)'] = {
        '_-$$Домохозяйство (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Домохозяйство, уборщик (0.2_бит*нормо-час)'] = {
        '_-$$Домохозяйство (0.2_бит*нормо-час)':1,
        }

metadict_model['_-$Домохозяйство, разнорабочий (0.2_бит*нормо-час)'] = {
        '_-$$Домохозяйство (0.2_бит*нормо-час)':1,
        }

metadict_detail['_-$Домохозяйство, водовоз (0.2_бит*нормо-час)'] = {
        '_-$$Домохозяйство (0.2_бит*нормо-час)':1,
        }

#----
# Почасовой оклад

metadict_model['_-$$Земледелие (0.1_бит*нормо-час)'] = {
        # Заработная плата для расчётов соотношения зарплат в output
        'Заработная плата (0.1_бит*нормо-час)':1,
        '_-$$$Земледелие (бит*нормо-час)':0.1,
        }

metadict_model['_-$$Земледелие (0.2_бит*нормо-час)'] = {
        'Заработная плата (0.2_бит*нормо-час)':1,
        '_-$$$Земледелие (бит*нормо-час)':0.2,
        }

metadict_model['_-$$Земледелие (0.3_бит*нормо-час)'] = {
        'Заработная плата (0.3_бит*нормо-час)':1,
        '_-$$$Земледелие (бит*нормо-час)':0.3,
        }

metadict_model['_-$$Земледелие (0.4_бит*нормо-час)'] = {
        'Заработная плата (0.4_бит*нормо-час)':1,
        '_-$$$Земледелие (бит*нормо-час)':0.4,
        }

metadict_model['_-$$Земледелие (0.5_бит*нормо-час)'] = {
        'Заработная плата (0.5_бит*нормо-час)':1,
        '_-$$$Земледелие (бит*нормо-час)':0.5,
        }

metadict_model['_-$$Обслуживание-культура (0.5_бит*нормо-час)'] = {
        'Заработная плата (0.5_бит*нормо-час)':1,
        '_-$$$Обслуживание-культура (бит*нормо-час)':0.5,
        }

metadict_model['_-$$Обслуживание-медицина (0.5_бит*нормо-час)'] = {
        'Заработная плата (0.5_бит*нормо-час)':1,
        '_-$$$Обслуживание-медицина (бит*нормо-час)':0.5,
        }

metadict_model['_-$$Обслуживание-медицина (1_бит*нормо-час)'] = {
        'Заработная плата (1_бит*нормо-час)':1,
        '_-$$$Обслуживание-медицина (бит*нормо-час)':1,
        }

metadict_model['_-$$Обслуживание-медицина (1.5_бит*нормо-час)'] = {
        'Заработная плата (1.5_бит*нормо-час)':1,
        '_-$$$Обслуживание-медицина (бит*нормо-час)':1.5,
        }

metadict_model['_-$$Обслуживание-медицина (2_бит*нормо-час)'] = {
        'Заработная плата (2_бит*нормо-час)':1,
        '_-$$$Обслуживание-медицина (бит*нормо-час)':2,
        }

metadict_model['_-$$Обслуживание-медицина (6_бит*нормо-час)'] = {
        'Заработная плата (6_бит*нормо-час)':1,
        '_-$$$Обслуживание-медицина (бит*нормо-час)':6,
        }

metadict_model['_-$$Обслуживание-медицина (9_бит*нормо-час)'] = {
        'Заработная плата (9_бит*нормо-час)':1,
        '_-$$$Обслуживание-медицина (бит*нормо-час)':9,
        }

metadict_model['_-$$Обслуживание-медицина (12_бит*нормо-час)'] = {
        'Заработная плата (12_бит*нормо-час)':1,
        '_-$$$Обслуживание-медицина (бит*нормо-час)':12,
        }

metadict_model['_-$$Обслуживание-медицина (20_бит*нормо-час)'] = {
        'Заработная плата (20_бит*нормо-час)':1,
        '_-$$$Обслуживание-медицина (бит*нормо-час)':20,
        }

metadict_model['_-$$Обслуживание-медицина (42_бит*нормо-час)'] = {
        'Заработная плата (42_бит*нормо-час)':1,
        '_-$$$Обслуживание-медицина (бит*нормо-час)':42,
        }

metadict_model['_-$$Обслуживание-образование (0.5_бит*нормо-час)'] = {
        'Заработная плата (0.5_бит*нормо-час)':1,
        '_-$$$Обслуживание-образование (бит*нормо-час)':0.5,
        }

metadict_model['_-$$Обслуживание-образование (1_бит*нормо-час)'] = {
        'Заработная плата (1_бит*нормо-час)':1,
        '_-$$$Обслуживание-образование (бит*нормо-час)':1,
        }

metadict_model['_-$$Обслуживание-кулинария (0.3_бит*нормо-час)'] = {
        'Заработная плата (0.3_бит*нормо-час)':1,
        '_-$$$Обслуживание-кулинария (бит*нормо-час)':0.3,
        }

metadict_model['_-$$Обслуживание-кулинария (0.5_бит*нормо-час)'] = {
        'Заработная плата (0.5_бит*нормо-час)':1,
        '_-$$$Обслуживание-кулинария (бит*нормо-час)':0.5,
        }

metadict_model['_-$$Обслуживание-хозяйство (0.3_бит*нормо-час)'] = {
        'Заработная плата (0.3_бит*нормо-час)':1,
        '_-$$$Обслуживание-хозяйство (бит*нормо-час)':0.3,
        }

metadict_model['_-$$Промышленность-добыча (0.2_бит*нормо-час)'] = {
        'Заработная плата (0.2_бит*нормо-час)':1,
        '_-$$$Промышленность-добыча (бит*нормо-час)':0.2,
        }

metadict_model['_-$$Промышленность-добыча (0.3_бит*нормо-час)'] = {
        'Заработная плата (0.3_бит*нормо-час)':1,
        '_-$$$Промышленность-добыча (бит*нормо-час)':0.3,
        }

metadict_model['_-$$Промышленность-добыча (0.4_бит*нормо-час)'] = {
        'Заработная плата (0.4_бит*нормо-час)':1,
        '_-$$$Промышленность-добыча (бит*нормо-час)':0.2,
        }

metadict_model['_-$$Промышленность-добыча (0.5_бит*нормо-час)'] = {
        'Заработная плата (0.5_бит*нормо-час)':1,
        '_-$$$Промышленность-добыча (бит*нормо-час)':0.5,
        }

metadict_model['_-$$Промышленность-добыча (1_бит*нормо-час)'] = {
        'Заработная плата (1_бит*нормо-час)':1,
        '_-$$$Промышленность-добыча (бит*нормо-час)':1,
        }

metadict_model['_-$$Промышленность-добыча (2_бит*нормо-час)'] = {
        'Заработная плата (2_бит*нормо-час)':1,
        '_-$$$Промышленность-добыча (бит*нормо-час)':2,
        }

metadict_model['_-$$Промышленность-кустари (0.2_бит*нормо-час)'] = {
        'Заработная плата (0.2_бит*нормо-час)':1,
        '_-$$$Промышленность-кустари (бит*нормо-час)':0.2,
        }

metadict_model['_-$$Промышленность-кустари (0.4_бит*нормо-час)'] = {
        'Заработная плата (0.2_бит*нормо-час)':1,
        '_-$$$Промышленность-кустари (бит*нормо-час)':0.2,
        }

metadict_model['_-$$Промышленность-кустари (0.5_бит*нормо-час)'] = {
        'Заработная плата (0.5_бит*нормо-час)':1,
        '_-$$$Промышленность-кустари (бит*нормо-час)':0.5,
        }

metadict_model['_-$$Промышленность-кустари (1_бит*нормо-час)'] = {
        'Заработная плата (1_бит*нормо-час)':1,
        '_-$$$Промышленность-кустари (бит*нормо-час)':1,
        }

metadict_model['_-$$Промышленность-кустари (9_бит*нормо-час)'] = {
        'Заработная плата (9_бит*нормо-час)':1,
        '_-$$$Промышленность-кустари (бит*нормо-час)':9,
        }

metadict_model['_-$$Промышленность-фабрики (0.2_бит*нормо-час)'] = {
        'Заработная плата (0.2_бит*нормо-час)':1,
        '_-$$$Промышленность-фабрики (бит*нормо-час)':0.2,
        }

metadict_model['_-$$Промышленность-фабрики (0.3_бит*нормо-час)'] = {
        'Заработная плата (0.3_бит*нормо-час)':1,
        '_-$$$Промышленность-фабрики (бит*нормо-час)':0.3,
        }

metadict_model['_-$$Промышленность-фабрики (0.4_бит*нормо-час)'] = {
        'Заработная плата (0.4_бит*нормо-час)':1,
        '_-$$$Промышленность-фабрики (бит*нормо-час)':0.4,
        }

metadict_model['_-$$Промышленность-фабрики (0.5_бит*нормо-час)'] = {
        'Заработная плата (0.5_бит*нормо-час)':1,
        '_-$$$Промышленность-фабрики (бит*нормо-час)':0.5,
        }

metadict_model['_-$$Промышленность-фабрики (1_бит*нормо-час)'] = {
        'Заработная плата (1_бит*нормо-час)':1,
        '_-$$$Промышленность-фабрики (бит*нормо-час)':1,
        }

metadict_model['_-$$Собирательство (0.1_бит*нормо-час)'] = {
        'Заработная плата (0.1_бит*нормо-час)':1,
        '_-$$$Собирательство (бит*нормо-час)':0.1,
        }

metadict_model['_-$$Собирательство (0.3_бит*нормо-час)'] = {
        'Заработная плата (0.3_бит*нормо-час)':1,
        '_-$$$Собирательство (бит*нормо-час)':0.3,
        }

metadict_model['_-$$Строительство (0.1_бит*нормо-час)'] = {
        'Заработная плата (0.1_бит*нормо-час)':1,
        '_-$$$Строительство (бит*нормо-час)':0.1,
        }

metadict_model['_-$$Строительство (0.2_бит*нормо-час)'] = {
        'Заработная плата (0.2_бит*нормо-час)':1,
        '_-$$$Строительство (бит*нормо-час)':0.2,
        }

metadict_model['_-$$Строительство (0.3_бит*нормо-час)'] = {
        'Заработная плата (0.3_бит*нормо-час)':1,
        '_-$$$Строительство (бит*нормо-час)':0.3,
        }

metadict_model['_-$$Строительство (0.5_бит*нормо-час)'] = {
        'Заработная плата (0.5_бит*нормо-час)':1,
        '_-$$$Строительство (бит*нормо-час)':0.5,
        }

metadict_model['_-$$Строительство (1_бит*нормо-час)'] = {
        'Заработная плата (1_бит*нормо-час)':1,
        '_-$$$Строительство (бит*нормо-час)':1,
        }

metadict_model['_-$$Строительство (2_бит*нормо-час)'] = {
        'Заработная плата (2_бит*нормо-час)':1,
        '_-$$$Строительство (бит*нормо-час)':2,
        }

metadict_model['_-$$Транспорт (0.1_бит*нормо-час)'] = {
        'Заработная плата (0.1_бит*нормо-час)':1,
        '_-$$$Транспорт (бит*нормо-час)':0.1,
        }

metadict_model['_-$$Транспорт (0.2_бит*нормо-час)'] = {
        'Заработная плата (0.2_бит*нормо-час)':1,
        '_-$$$Транспорт (бит*нормо-час)':0.2,
        }

metadict_model['_-$$Транспорт (0.3_бит*нормо-час)'] = {
        'Заработная плата (0.3_бит*нормо-час)':1,
        '_-$$$Транспорт (бит*нормо-час)':0.3,
        }

metadict_model['_-$$Транспорт (0.4_бит*нормо-час)'] = {
        'Заработная плата (0.4_бит*нормо-час)':1,
        '_-$$$Транспорт (бит*нормо-час)':0.4,
        }

metadict_model['_-$$Транспорт (0.5_бит*нормо-час)'] = {
        'Заработная плата (0.5_бит*нормо-час)':1,
        '_-$$$Транспорт (бит*нормо-час)':0.5,
        }

metadict_model['_-$$Транспорт (1_бит*нормо-час)'] = {
        'Заработная плата (1_бит*нормо-час)':1,
        '_-$$$Транспорт (бит*нормо-час)':1,
        }

metadict_model['_-$$Транспорт (2_бит*нормо-час)'] = {
        'Заработная плата (2_бит*нормо-час)':1,
        '_-$$$Транспорт (бит*нормо-час)':2,
        }

metadict_model['_-$$Транспорт (4_бит*нормо-час)'] = {
        'Заработная плата (4_бит*нормо-час)':1,
        '_-$$$Транспорт (бит*нормо-час)':4,
        }

metadict_model['_-$$Домохозяйство (0.2_бит*нормо-час)'] = {
        #'Заработная плата (0.2_бит*нормо-час)':1,
        '_-$$$Домохозяйство (бит*нормо-час)':0.2,
        }

metadict_model['_-$$Домохозяйство (0.3_бит*нормо-час)'] = {
        #'Заработная плата (0.3_бит*нормо-час)':1,
        '_-$$$Домохозяйство (бит*нормо-час)':0.3,
        }

#----
# Доходы суммарно.

metadict_model['_-$$$Земледелие (бит*нормо-час)'] = {
        '_-$$ Продукция, стоимость (бит)':1,
        }

metadict_model['_-$$$Обслуживание-культура (бит*нормо-час)'] = {
        '_-$$ Продукция, стоимость (бит)':1,
        }

metadict_model['_-$$$Обслуживание-медицина (бит*нормо-час)'] = {
        '_-$$ Продукция, стоимость (бит)':1,
        }

metadict_model['_-$$$Обслуживание-образование (бит*нормо-час)'] = {
        '_-$$ Продукция, стоимость (бит)':1,
        }

metadict_model['_-$$$Обслуживание-кулинария (бит*нормо-час)'] = {
        # TODO: кулинария и хозяйство смешиваются с домохозяйством.
        # Всё же учитываем в продукции, для удобства.
        '_-$$ Продукция, стоимость (бит)':1,
        }

metadict_model['_-$$$Обслуживание-хозяйство (бит*нормо-час)'] = {
        '_-$$ Продукция, стоимость (бит)':1,
        }

metadict_model['_-$$$Промышленность-добыча (бит*нормо-час)'] = {
        '_-$$ Продукция, стоимость (бит)':1,
        }

metadict_model['_-$$$Промышленность-кустари (бит*нормо-час)'] = {
        '_-$$ Продукция, стоимость (бит)':1,
        }

metadict_model['_-$$$Промышленность-фабрики (бит*нормо-час)'] = {
        '_-$$ Продукция, стоимость (бит)':1,
        }

metadict_model['_-$$$Собирательство (бит*нормо-час)'] = {
        '_-$$ Продукция, стоимость (бит)':1,
        }

metadict_model['_-$$$Строительство (бит*нормо-час)'] = {
        '_-$$ Продукция, стоимость (бит)':1,
        }

metadict_model['_-$$$Транспорт (бит*нормо-час)'] = {
        '_-$$ Продукция, стоимость (бит)':1,
        }

metadict_model['_-$$$Домохозяйство (бит*нормо-час)'] = {
        # Не считается в продукции, это дела по дому.
        #'_-$$ Продукция, стоимость (бит)':1,
        }
