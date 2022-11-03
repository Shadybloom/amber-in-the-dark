## ----
# Заклинания Dungeons & Dragons 3.5-5.0 в стиле понячьего мира:
    # https://dndtools.net/spells/
    # http://www.d20srd.org/indexes/spells.htm
    # https://www.dnd-spells.com/spells
    # https://www.dandwiki.com/wiki/3.5e_Spells
    # https://www.dandwiki.com/wiki/3.5e_Sorcerer/Wizard_Spells
    # https://www.dandwiki.com/wiki/5e_Sorcerer_Spells
    # https://www.dandwiki.com/wiki/SRD:Divine_Abilities

## ----
# Сила рога и заклинания:
    # Вот, например, «ударная волна» в исполнении типичнейшей чародейки 1 lvl:
    # https://www.dandwiki.com/wiki/Sonic_Marble_(3.5e_Spell)
    # Сфера радиусом — 0.05 метра (с копыто)
        # Объём: 4*(3.14159265*0.05^3)/3 = 0.0052 м³,
        # Плотность воздуха — 1.225 кг/кубометр
        # В сфере: 1.225*0.0052=0.00637 кг воздуха (6 грамм)
    # Мы нагреваем воздух в сфере ровно 6 секунд, с тепловым потоком в 1 кВт.
        # Теплоёмкость воздуха — 1.006 кДж/(кг*К)
        # Уравнение: T = E / (C * m)
        # Где:
        # T — Температура (в кельвинах)
        # E — Энергия (6 кВт)
        # C — удельная теплоёмкость (1.006 кДж/к)
        # m — масса (0.006 килограмма)
        # Подстановка:
        # 6 / (1.006 * 0.006) = 994 кельвина
    # Нам известна температура нагретого воздуха, теперь можно вычислить давление:
        # Уравнение состояния идеального газа: p*Vm=R*T
        # Где:
        # p — давление (в Паскалях)
        # Vm — молярный объём (22.41 л/моль)
        # R — Универсальная газовая постоянная (8314.5 Дж/(киломоль*К)
        # T — Абсолютная температура (994 кельвинов)
        # Уравнение: p = (R * T) / Vm
        # Подстановка:
        # (8314.5 * 994) / 22.41 = 368791 Паскалей (3.6 атмосферы)
    # Скорость истечения реактивной струи зависит от давления и температуры:
        # https://ru.wikipedia.org/wiki/Сопло_Лаваля
        # V=sqrt((T*R/M)*(2*k/(k-1))*[1-(Pe/p)^((k-1)/k)])
        # Где:
        # V — Скорость газа на выходе из сопла, м/с
        # T — Абсолютная температура газа на входе (994 кельвинов).
        # R — Универсальная газовая постоянная (8314.5 Дж/(киломоль*К)
        # M — Молярная масса газа, кг/киломоль (для воздуха 29 кг/киломоль)
        # k — Показатель адиабаты (для сухого воздуха при 20°C — 1.4)
        # Pe — Давление газа на выходе из сопла (атмосфера -- 101 325 Паскалей).
        # P — Давление газа на входе в сопло (368 791 Паскалей).
        # Итак, подстановка:
        # math.sqrt((994*8314.5/29)*(2*1.4/(1.4-1))*math.fabs(1-(101325/368791)**((1.4-1)/1.4)))=785 м/с
    # Теперь нужно узнать аэродинамическое сопротивление.
        # https://ru.wikipedia.org/wiki/Лобовое_сопротивление
        # https://en.wikipedia.org/wiki/Drag_coefficient
        # Уравнение:
        # X=k*((p*V^2)/2)*S
        # X — сопротивление в Ньютонах
        # k — коэффициент аэродинамического сопротивления (0.47 для сферы)
        # p — плотность воздуха в кг/м³ (1.2 при 20°C)
        # V — скорость в м/с (30 м/с или 108 км/час -- как футбольный мяч)
        # S — площадь поперечного сечения (3.14159265*0.05^2=0.00785 кв.метра)
        # Подстановка:
        # 0.47*((1.2*30^2)/2)*0.00785=2 ньютона
    # Зная аэродинамическое сопротивление и скорость реактивной струи можно вычислить расход топлива:
        # Уравнения реактивной тяги:
        # F = m * a
        # F = V * (m / t)
        # t = V / ((1/m) * F)
        # Где:
        # F — сила (в ньютонах)
        # m — масса топлива (в килограммах)
        # a — ускорение (метрах/секунду^2)
            # V — скорость
            # t — время
        # Подстановка:
            # 907 / ((1/0.005) * 2) = 2.3 секунды полёта
            # Шар пролетает 36 метров за секунду с потерей половины энергии.
    # Эффект взрыва -- 360 кПа в сфере радиусом в 0.05 метра.
        # Правило квадратов-кубов, если увеличиваем радиус вдвое, то объём увеличивается в 8 раз.
        # На дистанции 10 сантиметров от центра взрыва ударная волна: 360/8=45 кПа (контузия)
    # Не впечатляет, конечно, но это всего лишь 1.4 грамм тротилового эквивалента.
        # Единорожка 4 уровня вкинет уже 21 грамм, единорожка 6 уровня (уровень огнешаров) -- 88 грамм
        # Для сравнения: в гранате РГД-5 -- 110 грамм тротила и осколочная рубашка 200 грамм.

## ----
# Заклинания волшебников и чародеев:

metadict_detail['Заклинания волшебников 0 lvl'] = {
        # Простые единороги -- миллионы их:
        # Энергия. Электричество рога, тепловой насос, углеродные мембраны и магнитная левитация.
        #'0 lvl Создать материал из угля (???)':1,
        '0 lvl Левитация предмета (0 lvl Mage Hand, 0 lvl Rock Throw, 5 lvl Telekinesis)':1,
        '0 lvl Оттолкнуть (2 lvl Bigby\'s Striking Fist)':1,
        '0 lvl Светлячок (0 lvl Dancing Lights)':1,
        '0 lvl Волшебные галоши (0 lvl Gloves)':1,
        '0 lvl Вспышка (0 lvl Flare, 0 lvl Apprentice\' Fireball)':1,
        '0 lvl Ударная волна (0 lvl Sonic Marble, 3 lvl Shockwave, 4 lvl Force Orb)':1,
        '0 lvl Дисковой щит (1 lvl Shield, 3 lvl Repelling Shield)':1,
        '0 lvl Шоковое касание (1 lvl Shocking Grasp, 5 lvl Storm Touch)':1,
        '0 lvl Электростатическое поле (0 lvl Zap, 0 lvl Static Field, Lesser)':1,
        '0 lvl Поиск магии (0 lvl Detect Magic)':1,
        '0 lvl Прочесть магию (0 lvl Read Magic)':1,
        '0 lvl Обнаружить пауков (0 lvl Sense Spiders)':1,
        '0 lvl Обнаружить болезнь (0 lvl Detect Disease)':1,
        '0 lvl Склеить предмет (0 lvl Mending)':1,
        '0 lvl Тишина (0 lvl Silent Gateway)':1,
        '0 lvl Изменить голос (0 lvl Sweet Talk)':1,
        '0 lvl Голосовое послание (0 lvl Message)':1,
        '0 lvl Направленный звук (0 lvl Sonic Beam)':1,
        '0 lvl Магическая надпись (0 lvl Arcane Mark)':1,
        '0 lvl Невидимые чернила (0 lvl Azore\'s Invisible Ink)':1,
        '0 lvl Говорящая книга (0 lvl Azore\'s Speaking Tome)':1,

        # TODO: разгрести заклинания из DnD 5e
        '0 lvl Лепка земли (0 lvl Mold Earth)':1,
        '0 lvl Формирование воды (0 lvl Shape Water)':1,
        '0 lvl Шквал (0 lvl Gust)':1,
        '0 lvl Сотворение костра (0 lvl Create Bonfire)':1,
        '0 lvl Власть над огнём (0 lvl Control Flames)':1,
        '0 lvl Малая иллюзия (0 lvl Minor Illusion)':1,
        '0 lvl Мистический заряд (0 lvl Eldritch Blast)':1,
        '0 lvl Огненный снаряд (0 lvl Fire Bolt)':1,
        '0 lvl Лассо молнии (0 lvl Lightning Lure)':1,
        '0 lvl Дружба (0 lvl Friends)':1,
        '0 lvl Вспышка мечей (0 lvl Sword Burst)':1,
        '0 lvl Электрошок (0 lvl Shocking Grasp)':1,

        '0 lvl Трауматургия (0 lvl Thaumaturgy)':1,
        '0 lvl Исскуство друидов (0 lvl Druidcraft)':1,
        '0 lvl Волшебный камень (0 lvl Magic Stone)':1,
        '0 lvl Терновый кнут (0 lvl Thorn Whip)':1,
        '0 lvl Священное пламя (0 lvl Sacred Flame)':1,
        '0 lvl Слово сияния (0 lvl Word of Radiance)':1,

        }

metadict_detail['Заклинания волшебников 1 lvl'] = {
        # Исправить
            # На самом деле очень мало заклинаний.
            # А должно быть превеликое множество, возможности-то есть.
        # Чародеи и волшебники 1-2 уровней -- сотни тысяч:
        # Материалы. Компонентные заклинания: излучатели, разрядники, лезвия, нити, щиты.
        #'1 lvl Создать композит (1 lvl Summon Component, 5 lvl Major Creation)':1,
        '1 lvl Живая верёвка (1 lvl Animate Rope)':1,
        '1 lvl Создать палатку (3 lvl Leomund\'s Tiny Hut)':1,
        '1 lvl Крепкая шкура (1 lvl Force Skin)':1,
        '1 lvl Доспехи мага (1 lvl Mage Armor, 3 lvl Golden Dragonmail)':1,
        '1 lvl Создать одежду (2 lvl Clothier\'s Closet)':1,
        '1 lvl Быстрая перевязка (1 lvl Snaking Bandage)':1,
        '1 lvl Починить предмет (1 lvl Repair Light Damage)':1,
        '1 lvl Скопировать текст (1 lvl Randal\'s Quick Copy)':1,
        '1 lvl Защитная сфера (2 lvl Resist Energy, 2 lvl Protection from Arrows, 3 lvl Barrier)':1,
        '1 lvl Удушающая сфера (2 lvl Choke)':1,
        '1 lvl Раскалить сферу (4 lvl Balor Nimbus, 5 lvl Shroud of Flame)':1,
        '1 lvl Зарядить сферу (2 lvl Electric Vengeance)':1,
        '1 lvl Опутывающая нить (3 lvl Ray of the Python, 4 lvl Wingbind)':1,
        '1 lvl Заряженая нить (2 lvl Spectral Hand, 3 lvl Siphon)':1,
        '1 lvl Тепловой насос (2 lvl Heat Leech)':1,
        '1 lvl Паутина нитей (2 lvl Web, 7 lvl Choking Cobwebs)':1,
        '1 lvl Мост из нитей (2 lvl Dark Way, 2 lvl Force Ladder)':1,
        '1 lvl Запирание нитью (2 lvl Arcane Lock, 1 lvl Hold Portal)':1,
        '1 lvl Отпирание нитью (2 lvl Knock)':1,
        '1 lvl Тепловидение (1 lvl Detect Heat)':1,
        '1 lvl Сумеречное зрение (1 lvl Low-light Vision)':1,
        '1 lvl Определить силу (1 lvl Detect Power Level)':1,
        '1 lvl Определить родство (1 lvl Detect Parentage)':1,
        '1 lvl Ходьба по облакам (4 lvl Air Walk)':1,
        '1 lvl Облако частиц (2 lvl Glitterdust, 2 lvl Luminous Swarm)':1,
        '1 lvl Облако сияющих частиц (4 lvl Radiant Fog, 4 lvl Sparkles)':1,
        '1 lvl Пёрышко (1 lvl Feather Fall, 1 lvl Jump, 2 lvl Balancing Lorecall)':1,
        '1 lvl Чревовещание (1 lvl Ventriloquism, 2 lvl Dissonant Chant)':1,
        '1 lvl Луч наведения (1 lvl Targeting Ray)':1,
        '1 lvl Магическая стрела (1 lvl Mage Arrow)':1,
        '1 lvl Магическое лезвие (1 lvl Persistent Blade, 2 lvl Cloud of Knives)':1,
        '1 lvl Пробивающая стрела (1 lvl Eonwe\'s Magic Bunker Buster)':1,
        '1 lvl Молния вблизи (2 lvl Seeking Ray, 2 lvl Witch Bolt)':1,
        }

metadict_detail['Заклинания волшебников 2 lvl'] = {
        # Волшебники и чародеи 3-4 уровней -- десятки тысяч:
        # Трансфигурация. Рекомбинация элементов. Композиты и сплавы, цвет и форма, молекулярный контроль.
        '2 lvl Контрлевитация (4 lvl Halaster\'s Shaking Hand)':1,
        '2 lvl Левитация пони (2 lvl Levitate, 3 lvl Mage Hand, Greater)':1,
        '2 lvl Создать светокристалл (3 lvl Nchaser\'s Glowing Orb, 3 lvl Glowing Orb)':1,
        '2 lvl Создать кристалл-накопитель (3 lvl Glowing Orb)':1,
        '2 lvl Скопировать пищу или напиток (???)':1,
        '2 lvl Репликация крови (2 lvl Bear\'s Endurance)':1,
        '2 lvl Соединить живые ткани (2 lvl False Life)':1,
        '2 lvl Защитная сфера-накопитель (2 lvl Resist Energy)':1,
        '2 lvl Магическая татуировка (2 lvl Create Magic Tattoo)':1,
        '2 lvl Восстановить предмет (4 lvl Rebirth of Iron)':1,
        '2 lvl Подавить магию предмета (2 lvl Suppress Magic)':1,
        '2 lvl Укрепить материал (2 lvl Fortify Metal or Stone, 6 lvl Hardening)':1,
        '2 lvl Перестроить металл (5 lvl Shape Metal)':1,
        '2 lvl Водные крылья (2 lvl Swim, 2 lvl Wings of the Sea)':1,
        '2 lvl Водное дыхание (3 lvl Water Breathing)':1,
        '2 lvl Сигнализация (2 lvl Alarm, Greater, 2 lvl Portal Alarm)':1,
        '2 lvl Усиление слуха (2 lvl Listening Lorecall)':1,
        '2 lvl Усиление ценой рога (2 lvl Suffer the Flesh)':1,
        '2 lvl Отразить переходом (2 lvl Deflect)':1,
        '2 lvl Видеть незримое (2 lvl See Invisibility)':1,
        '2 lvl Поисковая метка (2 lvl Marked Object)':1,
        '2 lvl Найти помеченный объект (2 lvl Locate Object)':1,
        '2 lvl Касание развеивания чар (2 lvl Dispelling Touch)':1,
        '2 lvl Ночное зрение (2 lvl Darkvision, 3 lvl Deeper Darkvision)':1,
        '2 lvl Нить дальней связи (2 lvl Speaking Stones)':1,
        '2 lvl Иллюзорная копия (2 lvl Minor Image, 3 lvl Deceptive Facade)':1,
        '2 lvl Иллюзия себя (2 lvl Alter Self, 3 Displacement)':1,
        '2 lvl Скрывающая иллюзия (2 lvl Blur, 2 lvl Invisibility)':1,
        '2 lvl Маскировка под другого (2 lvl Reflective Disguise, 5 lvl Seeming)':1,
        '2 lvl Маскировка от заклинаний (2 lvl Misdirection, 2 lvl Obscure Object)':1,
        '2 lvl Туманное облако (2 lvl Fog Cloud, 2 lvl Cloud of Bewildermen)':1,
        '2 lvl Паутина заряженных нитей (4 lvl Dancing Web)':1,
        '2 lvl Зарядить оружие (4 lvl Weapon of Energy)':1,
        '2 lvl Проникающее заклинание (1 lvl True Casting)':1,
        '2 lvl Разрушить конструкт (4 lvl Ray of Deanimation)':1,
        '2 lvl Рассекающие нити (2 lvl Scourge of Force, 4 lvl Bloodbriars, 5 lvl Streamers)':1,
        '2 lvl Раскалённые нити (4 lvl Bright Worms, 4 lvl Flame Whips)':1,
        '2 lvl Раскалённая стрела (3 lvl Flame Arrow)':1,
        '2 lvl Направленный взрыв (2 lvl Blast of Force, 5 lvl Channeled Sound Blast)':1,
        '2 lvl Огненная сфера (2 lvl flaming sphere, 4 lvl Channeled Pyroburst)':1,
        '2 lvl Коррозия металла (3 lvl Rust Ray, 4 lvl Ghorus Toth\'s Metal Melt)':1,
        '2 lvl Оглушающая вспышка (3 lvl Great Thunderclap)':1,
        '2 lvl Световой луч (2 lvl Distracting Ray, 5 lvl Lucent Lance, 6 lvl Ray of Light)':1,
        '2 lvl Молния вдали (3 lvl Lightning Bolt, 7 lvl Stun Ray)':1,
        }

metadict_detail['Заклинания волшебников 3 lvl'] = {
        # Волшебники и чародеи 5-6 уровней -- меньше десяти тысяч:
        # Транслокация. Телепортация сквозь кристаллические решётки. Переход, поиск и призывание.
        '3 lvl Левитация слона (2 lvl Levitate, 4 lvl Crushing Grip)':1,
        '3 lvl Найти произвольный объект (2 lvl Locate Object, 3 lvl Detect Ship)':1,
        '3 lvl Найти по метке (3 lvl Circle Dance)':1,
        '3 lvl Скрыть метку (3 lvl Nondetection, 6 lvl Hidden Truename)':1,
        '3 lvl Видеть магию (3 lvl Arcane Sight, 3 lvl Spellcaster\'s Bane)':1,
        '3 lvl Предвидеть магию (3 lvl Battlemagic Perception)':1,
        '3 lvl Видеть минералы (3 lvl Detect Metal and Minerals, 4 lvl Treasure Scent)':1,
        '3 lvl Видеть истинную форму (3 lvl Discern Shapechanger)':1,
        '3 lvl Удалённое видение (3 lvl Clairaudience/clairvoyance, 3 lvl Elemental Eye)':1,
        '3 lvl Следить за другим (3 lvl Enduring Scrutiny, 4 lvl Scrying)':1,
        '3 lvl Изучить портал (3 lvl Analyze Portal, 3 lvl Anticipate Teleportation)':1,
        '3 lvl Переход к порталу (3 lvl Node Door, 3 lvl Evacuation Rune, 6 lvl Gemjump)':1,
        '3 lvl Ближний переход (2 lvl Dimension Leap, 3 lvl Dimension Step)':1,
        '3 lvl Контрзаклинание (3 lvl Stifle Spell, 4 lvl Spell Snare)':1,
        '3 lvl Развеять магию (3 lvl Dispel Magic, 3 lvl Tenacious Dispelling)':1,
        '3 lvl Пополнить энергию из щита (3 lvl Siphon)':1,
        '3 lvl Защита от энергии (3 lvl Protection from Energy)':1,
        '3 lvl Мгновенная защита от энергии (3 lvl Energy Aegis)':1,
        '3 lvl Изолирующая мантия (3 lvl Ilyykur\'s Mantle)':1,
        '3 lvl Укрепить предмет (3 lvl Augment Object, 3 lvl Diamondsteel)':1,
        '3 lvl Сфера невидимости (3 lvl Invisibility Sphere)':1,
        '3 lvl Защитная сфера-отражатель (4 lvl Ray Deflection, 4 lvl Forceward)':1,
        '3 lvl Удерживающая сфера (4 lvl Otiluke\'s Resilient Sphere, 7 lvl Forcecage)':1,
        '3 lvl Сжимающаяся сфера (6 lvl Crushing Sphere, 8 lvl Halaster\'s Blacksphere)':1,
        '3 lvl Волшебные крылья (3 lvl Fly, 3 lvl Phantom Steed)':1,
        '3 lvl Осадить туман (2 lvl Dispel Fog)':1,
        '3 lvl Зона тишины (3 lvl Suspended Silence)':1,
        '3 lvl Иллюзия стены (4 lvl Illusory Wall)':1,
        '3 lvl Запутывающая иллюзия (2 lvl Vertigo Field)':1,
        '3 lvl Спрятаться от дракона (3 lvl Hide From Dragons, 7 lvl Hide from Dragons)':1,
        '3 lvl Резонансный взрыв (3 lvl Resonating Bolt, 3 lvl Rockburst)':1,
        '3 lvl Разрушить изнутри (4 lvl Finger of Agony)':1,
        '3 lvl Вихрь магических стрел (3 lvl Chain Missile, 3 lvl Stars of Arvandor)':1,
        '3 lvl Бросок серебряного копья (4 lvl Force Missile, 3 lvl Laeral\'s Silver Lance)':1,
        '3 lvl Удар призрачного рога (3 lvl Melf\'s Unicorn Arrow)':1,
        '3 lvl Слепящая вспышка (4 lvl Blistering Radiance)':1,
        '3 lvl Шаровая молния (3 lvl Scintillating Sphere, 5 lvl Ball Lightning)':1,
        '3 lvl Огненный шар (3 lvl Fireball, 4 lvl Incendiary Surge)':1,
        }

metadict_detail['Заклинания волшебников 4 lvl'] = {
        # Волшебники и чародеи 7-8 уровней -- несколько тысяч:
        # Воплощение. Управляемые заклинания. Призрачные помощники, реагирующие щиты, зачарованные вещи.
        '4 lvl Инстинктивный переход (3 lvl Blink, 3 lvl Shadow Phase)':1,
        '4 lvl Перестановка с иллюзией (4 lvl Halaster\'s Image Swap)':1,
        '4 lvl Летающий диск (4 Floating Disk, Greater)':1,
        '4 lvl Создать ловушку (3 lvl Glyph of Warding, 4 lvl Fire Trap)':1,
        '4 lvl Магический глаз (4 lvl Arcane Eye, 6 lvl Eye of Stone)':1,
        '4 lvl Метка наблюдения (5 lvl Watchware, 7 lvl Gem Tracer)':1,
        '4 lvl Зеракало связи (4 lvl Mirror Sending)':1,
        '4 lvl Найти существо (4 lvl Locate Creature)':1,
        '4 lvl Найти магическое чудовище (4 lvl Sense of the Dragon)':1,
        '4 lvl Совершенное ночное зрение (4 lvl Superior Darkvision, 3 lvl Tremorsense)':1,
        '4 lvl Изучить слабости (4 lvl Assay Spell Resistance, 4 lvl Know Vulnerabilities)':1,
        '4 lvl Совершенная иллюзия (3 lvl Major Image)':1,
        '4 lvl Иллюзорная карета (4 lvl Leomund\'s Spacious Carriage)':1,
        '4 lvl Иллюзорный помощник (3 lvl Unseen Servant)':1,
        '4 lvl Иллюзорные стражи (3 lvl Phantom Guardians)':1,
        '4 lvl Защита разума (4 lvl Nezram\'s Emerald Energy Shield)':1,
        '4 lvl Кровь неподчинения (3 lvl Disobedience, 5 Unicorn Blood)':1,
        '4 lvl Ранящая антимагия (4 lvl Backlash, 4 lvl Slashing Dispel)':1,
        '4 lvl Ранить через обратную связь чар (5 lvl Reciprocal Gyre)':1,
        '4 lvl Подавление магии создания (3 lvl Invoke the Cerulean Sign)':1,
        '4 lvl Защитная сфера антимагии (4 lvl Globe of Invulnerability, Lesser)':1,
        '4 lvl Каскад заклинаний (4 lvl Rary\'s Mnemonic Enhancer)':1,
        '4 lvl Усиленное щитом заклинание (4 lvl Mystic Surge, 4 lvl Spell Enhancer)':1,
        '4 lvl Ослабление магической защиты (4 lvl Enervation, 4 lvl Lower Spell Resistance)':1,
        '4 lvl Магнитное кольцо (6 lvl Ghorus Toth\'s Magnetism, 7 lvl Reverse Gravity)':1,
        '4 lvl Невидимость (4 Invisibility, Greater, 4 Improved Invisibility)':1,
        '4 lvl Скрытая надпись (3 lvl Illusory Script, 3 lvl Secret Page)':1,
        '4 lvl Взрывающаяся надпись (3 lvl Explosive Runes, 3 lvl Sign of Sealing)':1,
        '4 lvl Совершенный полёт (4 lvl Aerial Alacrity, 4 lvl Enduring Flight)':1,
        '4 lvl Маска очарования (3 lvl Mask of the Ideal)':1,
        '4 lvl Корона связи (5 lvl Rary\'s Telepathic Bond)':1,
        '4 lvl Корона отражения (3 lvl Crown of Protection)':1,
        '4 lvl Корона наблюдения (3 lvl Crown of Clarity)':1,
        '4 lvl Корона иллюзий (3 lvl Crown of Veils)':1,
        '4 lvl Корона силы (3 lvl Crown of Might)':1,
        '4 lvl Щит направленных взрывов (5 lvl Sonic Shield)':1,
        '4 lvl Щит антимагии (4 lvl Otiluke\'s Dispelling Screen)':1,
        '4 lvl Доспехи мага-лорда (5 lvl Mailed Might of the Magelords)':1,
        '4 lvl Запирание магией (4 lvl Arcane Seal, 6 lvl Gate Seal)':1,
        '4 lvl Зачаровать оружие (3 lvl Magic Weapon, Greater, 6 lvl Brilliant Blade)':1,
        '4 lvl Поток магических стрел (4 lvl Steelsting)':1,
        '4 lvl Бросок громового копья (4 lvl Thunderlance)':1,
        '4 lvl Танцующее лезвие (5 lvl Sword of Deception, 7 lvl Mordenkainen\'s Sword)':1,
        '4 lvl Ищущие конструкты (5 lvl Prying Eyes, 8 lvl Prying Eyes, Greater)':1,
        '4 lvl Чинящие конструкты (4 lvl Summon Clockwork Mender Swarm)':1,
        '4 lvl Назойливое копыто Бигби (3 lvl Bigby\'s Disrupting Hand)':1,
        '4 lvl Защищающее копыто Бигби (5 lvl Bigby\'s Interposing Hand)':1,
        '4 lvl Удерживающее копыто Бигби (7 lvl Bigby\'s Grasping Hand)':1,
        '4 lvl Стукающее копыто Бигби (8 lvl Bigby\'s Clenched Fist)':1,
        '4 lvl Молниевые пылинки (5 lvl Moonbow, 5 lvl Presper\'s Moonbow)':1,
        }

metadict_detail['Заклинания волшебников 5 lvl'] = {
        # Мастера магии 9-10 уровней -- несколько сотен:
        # Контроль. Подавление младших заклинаний, управление магией мира: воздуха, земли, воды.
        '5 lvl Дальний переход (4 lvl Dimension Door, 5 lvl Teleport)':1,
        '5 lvl Мгновенно переместить другого (5 lvl Etherealness, Swift)':1,
        '5 lvl Мгновенный переход (5 lvl Blink, Improved, 5 lvl Dimension Jumper)':1,
        '5 lvl Изменить портал (4 lvl Scramble Portal, 6 lvl Seal Portal)':1,
        '5 lvl Создать подобие себя (4 lvl Create Fetch)':1,
        '5 lvl Создать ледяной корабль (4 lvl Ice Ship)':1,
        '5 lvl Создать грань огромного щита (5 lvl Wall of Force)':1,
        '5 lvl Сконцентрированное заклинание (5 lvl Aiming At the Target)':1,
        '5 lvl Хранилище заклинаний (5 lvl Simbul\'s Spell Matrix, 7 lvl Simbul\'s Spell Sequencer)':1,
        '5 lvl Рассеивание энергии (5 lvl Energy Buffer)':1,
        '5 lvl Маскировка места (4 lvl Mordenkainen\'s Private Sanctum, 8 lvl Screen)':1,
        '5 lvl Масштабная маскировка от заклинаний (5 lvl False Vision, 5 lvl Disguise Ship)':1,
        '5 lvl Множественная иллюзия (4 lvl Mirror Image, Greater, 4 lvl Phantom Battle)':1,
        '5 lvl Масштабная иллюзия (4 lvl Hallucinatory Terrain, 5 lvl Mirage Arcana)':1,
        '5 lvl Иллюзия жилища (4 lvl Leomund\'s Secure Shelter, 4 lvl Stone Shape)':1,
        '5 lvl Иллюзия палящего Солнца (4 lvl Searing Exposure)':1,
        '5 lvl Иллюзия пустоты (4 lvl Sensory Deprivation, 7 lvl Solipism)':1,
        '5 lvl Нестабильность магии места (5 lvl Mana Flux)':1,
        '5 lvl Подавить магию места (4 lvl Otiluke\'s Supressing Field)':1,
        '5 lvl Подавить переход (4 lvl Dimensional Anchor, 4 lvl Desert Diversion)':1,
        '5 lvl Ускорить переход (5 lvl Quickshift)':1,
        '5 lvl Ускорить контрзаклинания (5 lvl Duelward)':1,
        '5 lvl Защитник мага (5 lvl Nezram\'s Sapphire Screen of Shielding)':1,
        '5 lvl Мысленное послание (5 lvl Sending, 6 lvl False Sending)':1,
        '5 lvl Ищущее послание (4 lvl Magic Mouth, 2 lvl Whispering Wind)':1,
        '5 lvl Сопротивляемость магии (5 lvl Spell Resistance, 8 lvl Protection from Spells)':1,
        '5 lvl Управление температурой (3 lvl Control Temperature, 5 lvl Unearthly Heat)':1,
        '5 lvl Разлом земли (5 lvl Earth Reaver, 5 lvl Passwall, 8 lvl Excavate)':1,
        '5 lvl Колонна земли (4 lvl Column of Ice, 4 lvl Battlefield Fortification)':1,
        '5 lvl Хватка земли (2 lvl Earthen Grasp, 4 lvl Heart of Earth, 6 lvl Entomb)':1,
        '5 lvl Водная стена (2 lvl Pressure Sphere, 4 lvl Wall of Water, 7 lvl Waterspout)':1,
        '5 lvl Воздушный поток (3 lvl Wingblast, 5 lvl Cyclonic Blast)':1,
        '5 lvl Буревая сфера (3 lvl Wind Wall, 3 lvl Defenestrating Sphere)':1,
        '5 lvl Управляемый вихрь (2 lvl Gust of Wind, 3 lvl Pebble Wind)':1,
        '5 lvl Громовой удар (5 lvl Shrieking Blast, 5 lvl Sonic Rumble)':1,
        '5 lvl Зона направленных взрывов (4 lvl Explosive Rune Field, 6 lvl Thunder Field)':1,
        '5 lvl Огненный переход (4 lvl Firestride Exhalation, 4 lvl Fire Stride)':1,
        '5 lvl Переход с молнией (5 lvl Lightning Leap)':1,
        '5 lvl Заряженное облако (4 lvl Lightning Fog)':1,
        '5 lvl Вихрь воющих цепей (6 lvl Howling Chain)':1,
        '5 lvl Огненный каскад (5 lvl Firebrand)':1,
        }

metadict_detail['Заклинания волшебников 6 lvl'] = {
        # Мастера магии 11-12 уровней -- больше сотни:
        # Трансмутация. Ядерные реакции. Разрушение материалов их же энергией, антиматерия, антимагия.
        '6 lvl Переход сквозь камень (7 lvl Phase Door, 8 lvl Earth Glide)':1,
        '6 lvl Призвать зная метку (3 lvl Regroup, 4 lvl Translocation Trick)':1,
        '6 lvl Переход для других (6 lvl Tactical Teleportation, 6 lvl Translocation Trick)':1,
        '6 lvl Переход для предмета (7 lvl Teleport Object)':1,
        '6 lvl Взгляд за сотни миль (6 lvl Scry Location)':1,
        '6 lvl Взгляд истины (6 lvl True Seeing)':1,
        '6 lvl Исследовать магию врага (6 lvl Analyze Dweomer)':1,
        '6 lvl Исследовать портал (6 lvl Anticipate Teleportation, Greater)':1,
        '6 lvl Сохранить заклинание в диске (6 lvl Shalantha\'s Delicate Disk)':1,
        '6 lvl Камень в песок (5 lvl Transmute Rock to Sand)':1,
        '6 lvl Камень в стекло (3 lvl Clearstone, 5 lvl Transmute Rock to Glass)':1,
        '6 lvl Живого в стекло (6 lvl Dhulark\'s Glasstrike, 6 lvl Trobriand\'s Glassee)':1,
        '6 lvl Стена развеивания магии (5 lvl Wall of Dispel Magic, 8 lvl Wall of Greater Dispel Magic)':1,
        '6 lvl Сфера неуязвимости (6 lvl Globe of Invulnerability, 6 lvl Starmantle, 6 lvl Forcefield)':1,
        '6 lvl Сковывающая защита разума (5 lvl Imprison Possessor)':1,
        '6 lvl Настраиваемая иллюзия (6 lvl Programmed Image)':1,
        '6 lvl Зачаровывающая иллюзия (4 lvl Rainbow Pattern, 4 lvl Trance of the Verdant Domain)':1,
        '6 lvl Зона защитной магии (5 lvl Field of Resistance, 6 lvl Guards and Wards)':1,
        '6 lvl Развеять магию, совершенно (6 lvl Dispel Magic, Greater)':1,
        '6 lvl Разрушить постоянные чары (5 lvl Break Enchantment)':1,
        '6 lvl Подавить призывание (4 lvl Distort Summons, 6 lvl Steal Summoning)':1,
        '6 lvl Управление водой (6 lvl Control Water, 6 lvl Move Snow and Ice)':1,
        '6 lvl Управление землёй (6 lvl Move Earth, 6 lvl Mudslide)':1,
        '6 lvl Управление воздухом (5 lvl Control Winds, 5 lvl Lord of the Sky)':1,
        '6 lvl Создать скрытый сундук (5 lvl Leomund\'s Secret Chest)':1,
        '6 lvl Барьер транслокации (5 lvl Cacophonic Shield, 5 lvl Precipitate Breach)':1,
        '6 lvl Сфера ищущего камня (5 lvl Stone Sphere)':1,
        '6 lvl Луч антимагиии (7 lvl Antimagic Ray)':1,
        '6 lvl Луч разрушения (5 lvl Break Enchantment, 6 lvl Disintegrate)':1,
        '6 lvl Цепная молния (6 lvl Chain Lightning)':1,
        '6 lvl Испепеляющее облако (6 lvl Lingering Flames, 8 lvl Incendiary Cloud)':1,
        '6 lvl Рой огненных пауков (6 lvl Fire Spiders)':1,
        }

metadict_detail['Заклинания волшебников 7 lvl'] = {
        # Ученики богини 13-14 уровней -- десятки:
        # Зачарование. Постоянные заклинания. Оживлённые предметы, кристаллы щитов, големы и разумные станки.
        '7 lvl Видеть магию и распознать (7 lvl Arcane Sight, Greater)':1,
        '7 lvl Следить за сотни миль (7 lvl Scrying, Greater)':1,
        '7 lvl Необнаружимость для магии (7 lvl Sequester)':1,
        '7 lvl Перенаправление заклинаний (7 lvl Spell Turning)':1,
        '7 lvl Сохранить заклинание в метке (7 lvl Spell Snare, Greater)':1,
        '7 lvl Аура антимагиии (7 lvl Antimagic Aura, 7 lvl Kiss of Draconic Defiance)':1,
        '7 lvl Зона преобразования заклинаний (7 lvl Energy Transformation Field)':1,
        '7 lvl Защитная сфера перенаправления (7 lvl Mysterious Redirection)':1,
        '7 lvl Создать портал (6 lvl Portal-to-Portal Redirect, 1 lvl Portal Stabilization)':1,
        '7 lvl Иллюзорная усадьба (7 lvl Mordenkainen\'s Magnificent Mansion)':1,
        '7 lvl Иллюзорная яхта (8 lvl Mordenkainen\'s Capable Caravel)':1,
        '7 lvl Иллюзорный вор (5 lvl Phantasmal Thief, 8 lvl Phantasmal Thief)':1,
        '7 lvl Вечная иллюзия (5 lvl Persistent Image, 6 lvl Permanent Image)':1,
        '7 lvl Орда иллюзорных помощников (5 lvl Servant Horde, 4 lvl Unseen Servant, Mass)':1,
        '7 lvl Иллюзия-ремесленник (2 lvl Unseen Crafter, 3 lvl Amanuensis)':1,
        '7 lvl Иллюзия-защитник (4 lvl Guardian Spirit, 5 lvl Mordenkainen\'s Faithful Hound)':1,
        '7 lvl Постоянное заклинание (5 lvl Permanency)':1,
        '7 lvl Постоянные волшебные крылья (5 lvl Overland Flight)':1,
        '7 lvl Оживить предмет (3 lvl Animate Weapon, 3 lvl Steeldance, 5 lvl Minor Servitor)':1,
        '7 lvl Призвать оживлённый предмет (7 lvl Drawmij\'s Instant Summons)':1,
        '7 lvl Создать каменный голем (7 lvl Changestones)':1,
        '7 lvl Подчинить тело другого (8 lvl Otto\'s Irresistible Dance)':1,
        '7 lvl Касание живого пламени (7 lvl Emerald Flame Fist, 7 lvl Scalding Touch)':1,
        '7 lvl Ищущий огненный шар (7 lvl Delayed Blast Fireball)':1,
        '7 lvl Кольцо молний (8 lvl Lightning Ring)':1,
        }

metadict_detail['Заклинания волшебников 8 lvl'] = {
        # Ученики богини 15-16 уровней -- единицы:
        # Аниморфия. Преобразование души. Очарование, внушение, подавление, чтение памяти.
        '8 lvl Заклинание за сотни миль (8 lvl Demand)':1,
        '8 lvl Ускорить любые заклинания (7 lvl Arcane Spellsurge)':1,
        '8 lvl Объединение заклинаний (8 lvl Arcane Fusion, Greater)':1,
        '8 lvl Сфера поглощения магии (8 lvl Spell Engine, 9 lvl Absorption)':1,
        '8 lvl Завораживающая иллюзия (8 lvl Scintillating Pattern)':1,
        '8 lvl Подчинить другого (6 lvl Dominate Person Or Ghost)':1,
        '8 lvl Уничтожить иллюзии (8 lvl Illusion Purge)':1,
        '8 lvl Совершенная невидимость (8 lvl Stalking Spell)':1,
        '8 lvl Вложить магию в предмет (8 lvl Blackstaff)':1,
        '8 lvl Цепное развеивание магии (8 lvl Chain Dispel)':1,
        '8 lvl Резонансный взрыв на мили (8 lvl Great Shout)':1,
        '8 lvl Сфера солнечного огня (8 lvl Sunburst)':1,
        }

metadict_detail['Заклинания волшебников 9 lvl'] = {
        # Исправить
            # Допилить
            # https://dndtools.net/spells/?name=&range=&spell_resistance=&area=&duration=&saving_throw=&casting_time=&school__slug=&sub_school__slug=&descriptors__slug=&verbal_component=1&somatic_component=1&material_component=1&arcane_focus_component=1&divine_focus_component=1&xp_component=1&rulebook__slug=&description=&class_levels__slug=wizard&spellclasslevel__level=9&domain_levels__slug=&_filter=Filter
        # Ученики богини 17-20 уровней -- в этот век никого:
        # Предвидение. Дополнение души. Мгновенное познание однажды увиденных заклинаний.
        '9 lvl История места (9 lvl Hindsight)':1,
        '9 lvl Создать врата перехода (9 lvl Gate)':1,
        '9 lvl Создать клетку перехода (9 lvl Halaster\'s Teleport Cage)':1,
        '9 lvl Мгновенный дальний переход (9 lvl Dimension Jumper, Greater)':1,
        '9 lvl Подготовленный мгновенный переход (9 lvl Instant Refuge)':1,
        '9 lvl Познать увиденное заклинание (9 lvl Alamanther\'s Return)':1,
        '9 lvl Подготовленное заклинание (5 lvl Contingency, 9 lvl Chain Contingency)':1,
        '9 lvl Поглотители магии (9 lvl Elminster\'s Effulgent Epuration)':1,
        '9 lvl Неизбежное копыто Бигби (9 lvl Bigby\'s Crushing Hand)':1,
        '9 lvl Паутина неснимаемых нитей (9 lvl Binding Chain of Fate)':1,
        '9 lvl Сфера уничтожения (9 lvl Sphere of Ultimate Destruction)':1,
        '9 lvl Лезвие разрушения (9 lvl Black Blade of Disaster)':1,
        '9 lvl Оживить камень (9 lvl Awaken Construct)':1,
        }

## ----
# Заклинания аликорнов:
# Старомодные, позабытые, запрещённые.

metadict_detail['Заклинания аликорнов 0 lvl'] = {
        }

metadict_detail['Заклинания аликорнов 1 lvl'] = {
        '1 lvl Опознание (1 lvl Identify)':1,
        '1 lvl Мгновенное чтение (1 lvl Scholar\'s Touch, 1 lvl Student\'s Boon)':1,
        '1 lvl Подавление (1 lvl Whelm, 2 lVl Whelming Blast)':1,
        '1 lvl Шёпот сна (1 lvl Sleep, 7 lvl Hiss of Sleep)':1,
        '1 lvl Управление снами (2 lvl Dream Lock)':1,
        }

metadict_detail['Заклинания аликорнов 2 lvl'] = {
        '2 lvl Взгляд антимагии (2 lvl Arcane Turmoil)':1,
        '2 lvl Найти мыслящих (2 lvl Detect Thoughts)':1,
        '2 lvl Облако тьмы (2 lvl Darkness, 3 lvl Blacklight)':1,
        '2 lvl Защита от очарования (2 lvl Protection from Charm)':1,
        '2 lvl Очаровать другого (2 lvl Charm Person, 2 lvl Mesmerizing Glare)':1,
        '2 lvl Коралловая стена (4 lvl Coral Growth, 4 lvl Fuse Sand)':1,
        '2 lvl Вязкая ловушка (4 lvl Viscid Glob)':1,
        '2 lvl Сопротивляемость (2 lvl Major Resistance, 5 lvl Superior Resistance)':1,
        '2 lvl Репликация крови (2 lvl Bear\'s Endurance, 2 lvl False Life)':1,
        '2 lvl Усиление связок (2 lvl Cat\'s Grace)':1,
        '2 lvl Усиление мышц (2 lvl Bull\'s Strength, 2 lvl Ray of Resurgence)':1,
        '2 lvl Ускорение нейрометаболизма (2 lvl Fox\'s Cunning)':1,
        '2 lvl Контроль нейрометаболизма (2 lvl Owl\'s Wisdom, 2 lvl Indifference)':1,
        '2 lvl Контроль феромонов (2 lvl Eagle\'s Splendor)':1,
        '2 lvl Каменные кости (2 lvl Stone Bones)':1,
        '2 lvl Видение чужими глазами (2 lvl Chain of Eyes)':1,
        '2 lvl Извлечь мысли (2 lvl Crystalline Memories, 2 lvl Mindburn)':1,
        '2 lvl Оглушить словом (2 lvl Rebuke)':1,
        '2 lvl Отравляющее касание (3 lvl Poison)':1,
        '2 lvl Болезнетворное касание (4 lvl Contagion)':1,
        '2 lvl Парализующее касание (5 lvl Touch of Vecna)':1,
        '2 lvl Оглушить/ослепить (2 lvl Blindness/Deafness)':1,
        '2 lvl Бурлящая кровь (2 Beltyn\'s Burning Blood)':1,
        '2 lvl Разрушить кровь (2 Thalassemia)':1,
        '2 lvl Сжигающий луч (2 lvl Scorching Ray)':1,
        '2 lvl Кислотная стрела (2 lvl Melf\'s Acid Arrow)':1,
        '2 lvl Усыпляющая стрела (2 lvl Melf\'s Slumber Arrows)':1,
        '2 lvl Отозвать фамильяра (2 lvl Familiar Pocket)':1,
        }

metadict_detail['Заклинания аликорнов 3 lvl'] = {
        '3 lvl Ближний переход (2 lvl Baleful Transposition)':1,
        '3 lvl Ползучая тьма (lvl 3 Pall of Twilight, lvl 4 Damning Darkness)':1,
        '3 lvl Лечащее касание (3 lvl Healing Touch)':1,
        '3 lvl Защитить от тления (3 lvl Gentle Repose)':1,
        '3 lvl Наградить радостью (3 lvl Elation, 3 lvl Heroism)':1,
        '3 lvl Наделить яростью (3 lvl Enhance Familiar, 3 lvl Fortify Familiar)':1,
        '3 lvl Зачаровывающий взгляд (3 lvl Mesmerizing Glare)':1,
        '3 lvl Уязвимость к заклинаниям (3 lvl Spell Vulnerability)':1,
        '3 lvl Подавить невидимость (3 lvl Invisibility Purge, 4 lvl Revelation)':1,
        '3 lvl Внушить бессвязность речи (3 lvl Bothersome Babble)':1,
        '3 lvl Внушить слабоумие (3 lvl Feeblemind, 7 lvl Insanity)':1,
        '3 lvl Внушить наивность (3 lvl Mind Poison)':1,
        '3 lvl Внушить поражение (3 lvl Inevitable Defeat)':1,
        '3 lvl Внушить жадность (3 lvl Miser\'s Envy)':1,
        '3 lvl Остановить другого (3 lvl Hold Person, 3 lvl Halt, 7 lvl Hold Person, Mass)':1,
        '3 lvl Бестелесная форма (3 lvl Permeable Form, 3 lvl Gaseous Form, 5 lvl Ghostform)':1,
        '3 lvl Песчанная форма (4 lvl Sandform, 4 lvl Passage of the Shifting Sands)':1,
        '3 lvl Слепое зрение (3 lvl Blindsight)':1,
        '3 lvl Ускорение (3 lvl Haste, 5 lvl Sakkratar\'s Triple Strike)':1,
        '3 lvl Замедление (3 lvl Slow)':1,
        '3 lvl Бесформенность другого (4 lvl Corporeal Instability)':1,
        '3 lvl Хватающая стена (3 lvl Grasping Wall, 3 lvl Stony Grasp, 5 lvl Wall of Limbs)':1,
        '3 lvl Отравляющий туман (3 lvl Contagious Fog, 3 lvl Venom Bolt)':1,
        '3 lvl Расщепить кости (5 lvl Fleshshiver)':1,
        '3 lvl Иссушение (2 lvl Dessicate, 2 lvl Escalating Enfeeblement, 3 lvl Wither)':1,
        '3 lvl Призвать тёмные щупальца (3 lvl Evard\'s Menacing Tentacles)':1,
        '3 lvl Соляная статуя (3 lvl Flesh to Salt)':1,
        '3 lvl Пыль эйфории (4 lvl Cone of Euphoria)':1,
        '3 lvl Пыль усыпления (3 lvl Dolorous Motes)':1,
        '3 lvl Пыль разрушения (3 lvl Haboob, 3 lvl Storm Mote)':1,
        '3 lvl Звуковое давление (5 lvl Horizikaul\'s Versatile Vibration)':1,
        '3 lvl Создать каменный конструкт (3 lvl Sticks and Stones)':1,
        '3 lvl Создать существо (3 lvl Create Crawling Claw)':1,
        '3 lvl Глубокий сон (3 lvl Deep Slumber, 6 lvl Endless Slumber)':1,
        '3 lvl Страшный сон (5 lvl Fever Dream)':1,
        '3 lvl Оживить сон (3 lvl Dream Spirit)':1,
        }

metadict_detail['Заклинания аликорнов 4 lvl'] = {
        '4 lvl Зрение всеведения (3 lvl Vision of the Omniscient Eye)':1,
        '4 lvl Предмет в портал (3 lvl Shadow Cache, 4 lvl Force Chest)':1,
        '4 lvl Мысленная связь (3 lvl Telepathic Bond, Lesser)':1,
        '4 lvl Очаровать чудовище (4 lvl Charm Monster, 3 lvl Suggestion)':1,
        '4 lvl Подманить чудовище (4 lvl Beckon Monster)':1,
        '4 lvl Снять проклятие (4 lvl Remove Curse)':1,
        '4 lvl Внушить приказ (4 lvl Geas, Lesser)':1,
        '4 lvl Внушить неумение (4 lvl Bestow Curse)':1,
        '4 lvl Внушить страх (4 lvl Fear)':1,
        '4 lvl Внушить ненависть к злу (6 lvl Wages of Sin)':1,
        '4 lvl Внушить враждебность к другому (5 lvl Friend to Foe, 6 lvl Incite Riot)':1,
        '4 lvl Парализующий взгляд (4 lvl Evil Glare, 6 lvl Transfix)':1,
        '4 lvl Касание старения (4 lvl Touch of Years)':1,
        '4 lvl Сокрушающая печаль (4 lvl Crushing Despair)':1,
        '4 lvl Облако истощения (4 lvl Sinsabur\'s Baleful Bolt)':1,
        '4 lvl Стальная кожа (3 lvl Improved Mage Armor, 4 lvl Stoneskin)':1,
        '4 lvl Боевая трансформация (6 lvl Tenser\'s Transformation)':1,
        '4 lvl Превратить себя (4 lvl Polymorph Self, 3 lvl Flexform)':1,
        '4 lvl Превратить в камень (4 lvl Call of Stone, 6 lvl Flesh to Stone, 7 lvl Statue)':1,
        '4 lvl Усилить бестелесного (4 lvl Incorporeal Enhancement)':1,
        '4 lvl Зона подавления бестелесных (4 lvl Zone of Revelation)':1,
        '4 lvl Создать обсидиановый конструкт (4 lvl Conjure Lesser Midnight Construct)':1,
        '4 lvl Облако ястребиных теней (4 lvl Raptor Cloud)':1,
        '4 lvl Клинок темноты (5 lvl Sword of Deception, 7 lvl Sword of Darkness)':1,
        '4 lvl Вихрь клыков (4 lvl Vortex of Teeth)':1,
        '4 lvl Иллюзорная армия (3 lvl Legion of Sentinels)':1,
        '4 lvl Теневое подобие (4 lvl Shadow Conjuration)':1,
        '4 lvl Теневой колодец (4 lvl Shadow Well)':1,
        '4 lvl Оживить пыль (2 lvl Ashstar, 3 lvl Capricious Zephyr)':1,
        '4 lvl Придушить отрубленным копытом (4 lvl Grim Revenge)':1,
        '4 lvl Стена бьющих цепей (4 lvl Wall of Deadly Chains)':1,
        '4 lvl Пылевые щупальца (4 lvl Evard\'s Black Tentacles)':1,
        '4 lvl Вампирьи скарабеи (3 lvl Doom Scarabs, 4 lvl Summon Pest Swarm)':1,
        '4 lvl Стрела мгновенной смерти (4 lvl Arrow of Bone)':1,
        '4 lvl Убить словом (4 lvl Vecna Malevolent Whisper)':1,
        }

metadict_detail['Заклинания аликорнов 5 lvl'] = {
        '5 lvl Кислотный панцирь (5 lvl Acid Sheath)':1,
        '5 lvl Отследить наблюдение (4 lvl Detect Scrying)':1,
        '5 lvl Создать скрытое жилище (5 lvl Hidden Lodge)':1,
        '5 lvl Зона подавления перехода (4 lvl Zone of Respite, 8 lvl Dimensional Lock)':1,
        '5 lvl Дальнее послание во сне (5 lvl Dream)':1,
        '5 lvl Иллюзорный пир (5 lvl Illusory Feast)':1,
        '5 lvl Подчинить другого (5 lvl Dominate Person)':1,
        '5 lvl Идеальная маскировка под другого (5 lvl Veil)':1,
        '5 lvl Развеять подавление воли (5 lvl Dispel Possession)':1,
        '5 lvl Подобие заклинания (5 lvl Shadow Evocation, 8 lvl Shadow Evocation, Greater)':1,
        '5 lvl Поглотить магию другого (5 lvl Channeled Lifetheft, 5 lvl Spell Theft)':1,
        '5 lvl Похитить знания призрака (5 lvl Leech Ghost Skill)':1,
        '5 lvl Оценка вероятностей (3 lvl Glimpse of Truth, 5 lvl Contact Other Plane)':1,
        '5 lvl Внушить кошмар (3 lvl Reality Blind, 5 lvl Nightmare, 7 lvl Symphonic Nightmare)':1,
        '5 lvl Внушить боль (5 lvl Wrack, 8 lvl Nybor\'s Wrathful Castigation)':1,
        '5 lvl Касание смертельной болезни (5 lvl Cryptwarden\'s Grasp)':1,
        '5 lvl Создать адамантин (5 lvl Touch of Adamantine)':1,
        '5 lvl Превратить большего в меньшего (5 lvl Baleful Polymorph)':1,
        '5 lvl Превратить меньшего в большего (5 lvl Animal Growth)':1,
        '5 lvl Превратить зверя в маг. чудовище (5 lvl Create Darkenbeast)':1,
        '5 lvl Передать память (3 lvl Glimpse of Eternity, 6 lvl Overwhelm)':1,
        '5 lvl Поднять немёртвых (5 lvl Animate Legion, 6 lvl Create Undead)':1,
        '5 lvl Восстановить немёртвых (6 lvl Revive Undead)':1,
        '5 lvl Стихийная форма (3 lvl Primal Form, 7 lvl Elemental Body)':1,
        '5 lvl Теневая форма (5 lvl Shadow Form, 7 lvl Eladrin Form, 7 lvl Ethereal Jaunt)':1,
        '5 lvl Теневые стражи (5 lvl Shadow Guardians)':1,
        '5 lvl Теневой помощник (5 lvl Shadow Hand)':1,
        '5 lvl Воплотить мысль (5 lvl Call Nightmare)':1,
        '5 lvl Кислотный дождь (5 lvl Acid Rain)':1,
        '5 lvl Облако усыпления (5 lvl Sleep Mote)':1,
        '5 lvl Облако смерти (5 lvl Cloudkill)':1,
        '5 lvl Облако разрушения (5 lvl Flaywind Burst, 5 lvl Shard Storm)':1,
        '5 lvl Призматический луч (3 lvl Rainbow Blast, 5 lvl Prismatic Ray)':1,
        '5 lvl Призвать свет Солнца (3 lvl Daylight, 5 lvl Radiance, 9 lvl Blinding Glory)':1,
        '5 lvl Призвать существ (5 lvl Call Lemure Horde)':1,
        '5 lvl Затмение (4 lvl Early Twilight)':1,
        }

metadict_detail['Заклинания аликорнов 6 lvl'] = {
        '6 lvl Аура ужаса (6 lvl Aura of Terror)':1,
        '6 lvl Изучить мысли другого (6 lvl Probe Thoughts)':1,
        '6 lvl Иллюзия себя и невидимость (6 lvl Mislead)':1,
        '6 lvl Купол теней (6 lvl Shadow Canopy)':1,
        '6 lvl Хватка из тени (6 lvl Shadowy Grappler)':1,
        '6 lvl Переход по метке тени (6 lvl Familiar Refuge)':1,
        '6 lvl Изменить волю другого (6 lvl Remorseless Charm)':1,
        '6 lvl Метка всеобщей ненависти (6 lvl Cloak of Hate)':1,
        '6 lvl Касание совершенства (6 lvl Chasing Perfection)':1,
        '6 lvl Внушить абсолютный приказ (6 lvl Geas/quest)':1,
        '6 lvl Дезинтегрировать (6 lvl Disintegrate)':1,
        '6 lvl Призматическая аура (6 lvl Prismatic Aura, 7 lvl Prismatic Spray)':1,
        '6 lvl Призматический глаз (6 lvl Prismatic Eye, 7 lvl Radiant Assault)':1,
        '6 lvl Призматическая стена (8 lvl Prismatic Wall)':1,
        '6 lvl Поток предсказаний (6 lvl Eyes of the Oracle, 6 lvl Glimpse of the Prophecy)':1,
        '6 lvl Зона запрещённой магии (5 lvl Refusal, 6 lvl Antimagic Field)':1,
        '6 lvl Запереть вне реальности (6 lvl Smoky Confinement, 6 lvl Snare Astral Traveler)':1,
        '6 lvl Иссушить мгновенно (4 lvl Ashen Union, 6 lvl Mummify, 8 lvl Blackfire)':1,
        '6 lvl Кольцо смерти (6 lvl Ring Of Death, 6 lvl Incorporeal Nova)':1,
        '6 lvl Убить взглядом (5 lvl Opalescent Glare, 7 lvl Righteous Glare)':1,
        '6 lvl Создать каменный конструкт (6 lvl Call of the Twilight Defender)':1,
        '6 lvl Создать полуночный конструкт (6 lvl Conjure Midnight Construct)':1,
        '6 lvl Создать немёртвого (6 lvl Animate Dread Warrior, 6 lvl Mineralize Warrior)':1,
        '6 lvl Призвать споровое облако (6 lvl Contagion, Mass, 6 lvl Spore Cloak)':1,
        '6 lvl Уничтожить немёртвых (6 lvl Undeath to Death, 8 lvl Devastate Undead)':1,
        '6 lvl Облако раскалённой пыли (6 lvl Haze of Smoldering Stone, 6 lvl Sandblast)':1,
        '6 lvl Луч восстановления реальности (6 lvl Ruby Ray of Reversal)':1,
        '6 lvl Коснуться спящего заклинанием (6 lvl Dream Casting)':1,
        '6 lvl Шторм льда и пламени (6 lvl Storm of Fire and Ice)':1,
        '6 lvl Штормовой переход (6 lvl Stormwalk)':1,
        }

metadict_detail['Заклинания аликорнов 7 lvl'] = {
        '7 lvl Дальнее перемещение других (6 lvl Trobriand\'s Baleful Teleport)':1,
        '7 lvl Восстановить себя (7 lvl Simbul\'s Synostodweomer)':1,
        '7 lvl Мысленная связь (7 lvl Soul Link)':1,
        '7 lvl Планарный переход (7 lvl Plane Shift)':1,
        '7 lvl Планарный шторм (7 lvl Reality Maelstrom)':1,
        '7 lvl Познать язык другого (7 lvl Tongues)':1,
        '7 lvl Похитить способность (7 lvl Ability Rip)':1,
        '7 lvl Запереть в стазисе (7 lvl Amber Sarcophagus, 8 lvl Temporal Stasis)':1,
        '7 lvl Адамантиновые крылья (7 lvl Adamantine Wings)':1,
        '7 lvl Невидимость армии (7 lvl Invisibility, Mass)':1,
        '7 lvl Щит архонтов (7 lvl Shield of the Archons)':1,
        '7 lvl Щит поглощения энергии (7 lvl Energy Absorption)':1,
        '7 lvl Исполнить ограниченное желание (7 lvl Limited Wish)':1,
        '7 lvl Создать теневое подобие (7 lvl Shadow Conjuration, 7 lvl Simulacrum)':1,
        '7 lvl Создать разумный конструкт (7 lvl Call Kolyarut)':1,
        '7 lvl Выдавить кровь (7 lvl Avasculate)':1,
        }

metadict_detail['Заклинания аликорнов 8 lvl'] = {
        '8 lvl Планарный лабиринт (8 lvl Maze)':1,
        '8 lvl Внушить безумие (8 lvl Maddening Scream)':1,
        '8 lvl Внушить трепет всем (8 lvl Crown of Glory)':1,
        '8 lvl Внушить фамильный приказ (8 lvl Familial Geas)':1,
        '8 lvl Двойная оболочка антимагии (8 lvl Resonating Resistance)':1,
        '8 lvl Совершенное удалённое видение (8 lvl Discern Location)':1,
        '8 lvl Абсолютная защита разума (8 lvl Mind Blank, 8 lvl Mind of the Labyrinth)':1,
        '8 lvl Стремительное действие (8 lvl Celerity, Greater)':1,
        '8 lvl Мгновение совершества (8 lvl Moment of Prescience)':1,
        '8 lvl Привлечение/отвращение места (8 lvl Antipathy, 8 lvl Sympathy)':1,
        '8 lvl Создать клон существа (8 lvl Clone)':1,
        '8 lvl Создать совершенный конструкт (8 lvl Conjure Greater Midnight Construct)':1,
        '8 lvl Превратить в бесформенного (8 lvl Simbul\'s Skeletal Deliquescence)':1,
        '8 lvl Превратить любого в любое (8 lvl Polymorph Any Object)':1,
        '8 lvl Похитить силу немёртвого (8 lvl Leech Undead)':1,
        '8 lvl Похитить силу живого (8 lvl Steal Life)':1,
        '8 lvl Иссушить местность (8 lvl Horrid Wilting)':1,
        '8 lvl Путешествие через сны (8 lvl Dream Travel)':1,
        '8 lvl Эпидемия (8 lvl Plague)':1,
        }

metadict_detail['Заклинания аликорнов 9 lvl'] = {
        '9 lvl Предвидение (9 lvl Foresight)':1,
        '9 lvl Создать дом вне мира (9 lvl Genesis)':1,
        '9 lvl Аватар-заклинатель (9 lvl Eye of Power)':1,
        '9 lvl Подчинить любого (6 lvl Dominate Monster)':1,
        '9 lvl Идеальная невидимость (9 lvl Superior Invisibility)':1,
        '9 lvl Переход из зоны антимагии (9 lvl Elminster\'s Evasion)':1,
        '9 lvl Подарить жизнь конструкту (9 lvl Incarnate Construct)':1,
        '9 lvl Создать конструкт, мгновенно (9 lvl Call Marut)':1,
        '9 lvl Заморозить местность (9 lvl Burst of Glacial Wrath, 9 lvl Frostfell)':1,
        '9 lvl Сокрушить местность (9 lvl Crushing Fist of Spite)':1,
        '9 lvl Солнечная вспышка (9 lvl Deadly Sunstroke)':1,
        '9 lvl Запереть (9 lvl Imprisonment)':1,
        '9 lvl Испепелить (9 lvl Detonate)':1,
        '9 lvl Освободить (9 lvl Freedom)':1,
        }

## ----
# Заклинания эглан, киринов и водных драконов.
# Магия друидов, клериков, немного некромантии и скорее эффектные, чем эффективные боевые заклинания.

metadict_detail['Заклинания Эглан 0 lvl'] = {
        # Магия слов и общения с духами
        '0 lvl Осветить (0 lvl Light, 1 lvl Faerie Fire)':1,
        '0 lvl Поиск магии (0 lvl Detect Magic)':1,
        '0 lvl Призвать воду (0 lvl Create Water)':1,
        '0 lvl Найти яд (0 lvl Detect Poison)':1,
        '0 lvl Очистить пищу или воду (0 lvl Purify Food and Drink)':1,
        '0 lvl Вылечить царапину (0 lvl Cure Minor Wounds)':1,
        '0 lvl Компас (0 lvl Know Direction)':1,
        '0 lvl Отразить клинок (0 lvl Blade Ward)':1,
        '0 lvl Сопротивляемость (0 lvl Resistance)':1,
        '0 lvl Руководство духа (0 lvl Guidance)':1,
        '0 lvl Касание усталости (0 lvl Touch of Fatigue)':1,
        '0 lvl Разрушить немёртвого (0 lvl Disrupt Undead)':1,
        }

metadict_detail['Заклинания Эглан 1 lvl'] = {
        # https://www.dandwiki.com/wiki/Ell%27s_Handy_Homunculus_(3.5e_Spell)
        '1 lvl Спаси-котик (1 lvl Safecat Homunculus)':1,
        '1 lvl Лев-художник (1 lvl Doodle Homunculus)':1,
        '1 lvl Птичка-певец (1 lvl Songbird Homunculus)':1,
        '1 lvl Кроль-посланник (1 lvl Speaker Homunculus)':1,
        '1 lvl Лампа-медуза (1 lvl Spritelight Homunculus)':1,
        '1 lvl Осьминог-хвататель (1 lvl Grabby Homunculus)':1,
        '1 lvl Жук-искатель-магии (1 lvl Spellshine Homunculus)':1,
        '1 lvl Черепашка-кондиционер (1 lvl Humidifier Homunculus)':1,
        '1 lvl Дракончик-обогреватель (1 lvl Flaredrake Homunculus)':1,
        '1 lvl Ползун-уборщик (1 lvl Scrubber Homunculus)':1,
        '1 lvl Обезьянка-писец (1 lvl Kopi Homunculus)':1,
        '1 lvl Обезьянка-мастеровой (1 lvl Stitcher Homunculus)':1,
        '1 lvl Пингвин-холодильник (1 lvl Cooler Homunculus)':1,
        '1 lvl Мышь-сортировщик (1 lvl Collector Homunculus)':1,
        '1 lvl Электромышка (1 lvl Jolt Homunculus)':1,
        '1 lvl Крыса-повар (1 lvl Chef Homunculus)':1,
        '1 lvl Ёжик-ёжик (1 lvl Spiky Homunculus)':1,
        '1 lvl Деревянный скрытник (1 lvl Beget Bogun)':1,
        '1 lvl Деревянный прислужник (1 lvl Wood Wose)':1,
        '1 lvl Оживить деревянный предмет (1 lvl Animate Wood)':1,
        '1 lvl Оживить огонь (1 lvl Animate Fire)':1,
        '1 lvl Слово боли (1 lvl Power Word Pain)':1,
        '1 lvl Слово утомления (1 lvl Power Word Fatigue)':1,
        '1 lvl Успокоить зверя (1 lvl Calm Animals)':1,
        '1 lvl Очаровать зверя (1 lvl Charm Animal)':1,
        '1 lvl Убрать запах (1 lvl Remove Scent':1,
        '1 lvl Спрятать от зверей (1 lvl Hide from Animals)':1,
        '1 lvl Говорить со зверем (1 lvl Speak With Animals)':1,
        '1 lvl Вылечить лёгкую рану (1 lvl Cure Light Wounds)':1,
        '1 lvl Найти воду (1 lvl Locate Water)':1,
        '1 lvl Найти живого (1 lvl Detect Animals Or Plants, 1 lvl Sense Life)':1,
        '1 lvl Найти ловушку (1 lvl Detect Snares and Pits)':1,
        '1 lvl Защита от непогоды (1 lvl Endure Elements)':1,
        '1 lvl Защита от пламени (1 lvl Aura Against Flame)':1,
        '1 lvl Опутывающая трава (1 lvl Entangle)':1,
        '1 lvl Дрожащая земля (1 lvl Impeding Stones)':1,
        '1 lvl Хрустящий снег (1 lvl Crunchy Snow)':1,
        '1 lvl Лечебный сон (1 lvl Healthful Rest)':1,
        '1 lvl Быстрое самолечение (1 lvl Vigor, Lesser)':1,
        '1 lvl Лечебные ягоды (1 lvl Goodberry)':1,
        '1 lvl Зачаровать клыки (1 lvl Magic Fang, 3 lvl Magic Fang, Greater)':1,
        '1 lvl Зачаровать посох/копьё (1 lvl Shillelagh)':1,
        '1 lvl Зачаровать метательные камни (1 lvl Magic Stone)':1,
        '1 lvl Камуфляж (1 lvl Camouflage)':1,
        '1 lvl Острый глаз (1 lvl Eyes of the Avoral, 1 lvl Hawkeye)':1,
        '1 lvl Копыта скалолаза (1 lvl Climb Walls)':1,
        '1 lvl Задержать болезнь (1 lvl Delay Disease)':1,
        '1 lvl Восстановить дыхание (1 lvl Deep Breath)':1,
        '1 lvl Камень-вспышка (5 lvl Emerald Burst)':1,
        '1 lvl Скрывающий туман (1 lvl Obscuring Mist, 2 Fog Cloud)':1,
        '1 lvl Дымная стена (1 lvl Wall of Smoke)':1,
        '1 lvl Путь без препятсвий (1 lvl Pass Without Trace, 1 lvl Surefooted Stride)':1,
        '1 lvl Крепкая стойка (1 lvl Foundation of Stone)':1,
        '1 lvl Найти быстрый путь (1 lvl Longstrider)':1,
        '1 lvl Прохладный ветер (1 lvl Darsson\'s Cooling Breeze)':1,
        '1 lvl Порыв ветра (1 lvl Updraft, 2 lvl Gust of Wind, 3 lvl Favorable Wind)':1,
        '1 lvl Шёпот сна (1 lvl Sleep, 7 lvl Hiss of Sleep)':1,
        '1 lvl Сформировать снег (1 lvl Snowdrift)':1,
        '1 lvl Призвать ледяного (1 lvl Conjure Ice Beast I)':1,
        '1 lvl Призвать дождевое облачко (1 lvl Cloudburst)':1,
        '1 lvl Призвать молниевое облачко (1 lvl Thunderhead)':1,
        '1 lvl Метательное пламя (1 lvl Produce Flame)':1,
        '1 lvl Ослабляющий холод (1 lvl Winter Chill)':1,
        '1 lvl Песчанный поток (1 lvl Sandblast)':1,
        '1 lvl Огненное копыто (1 lvl Handfire)':1,
        }

metadict_detail['Заклинания Эглан 2 lvl'] = {
        '2 lvl Слово болезни (3 lvl Contagion, 2 lvl Power Word Sicken)':1,
        '2 lvl Остановить другого (2 lvl Hold Animal)':1,
        '2 lvl Подозвать другого (2 lvl Entice Gift)':1,
        '2 lvl Ослабить другого (2 lvl Reduce Animal)':1,
        '2 lvl Животное-посланник (2 lvl Animal Messenger)':1,
        '2 lvl Ввести в транс (2 lvl Animal Trance)':1,
        '2 lvl Крепкая кожа (2 lvl Barkskin)':1,
        '2 lvl Острый коготь (2 lvl Razorfangs)':1,
        '2 lvl Плащ храбрости (2 lvl Cloak of Bravery)':1,
        '2 lvl Выносливость медведя (2 lvl Bear\'s Endurance)':1,
        '2 lvl Кошачья грация (2 lvl Cat\'s Grace)':1,
        '2 lvl Бычья сила (2 lvl Bull\'s Strength)':1,
        '2 lvl Лисий ум (2 lvl Fox\'s Cunning)':1,
        '2 lvl Совиная мудрость (2 lvl Owl\'s Wisdom)':1,
        '2 lvl Орлиное величие (2 lvl Eagle\'s Splendor)':1,
        '2 lvl Леденящий металл (2 lvl Chill Metal)':1,
        '2 lvl Раскалённый металл (2 lvl Flame Blade, 2 lvl Heat Metal)':1,
        '2 lvl Остановить яд (2 lvl Delay Poison)':1,
        '2 lvl Исцелить (2 lvl Restoration, Lesser)':1,
        '2 lvl Землю в грязь (2 lvl Soften Earth and Stone)':1,
        '2 lvl Взобраться как паук (2 lvl Spider Climb)':1,
        '2 lvl Укрыться в дереве (2 lvl Tree Shape)':1,
        '2 lvl Разрушить древесину (2 lvl Warp Wood)':1,
        '2 lvl Разрушить омертвевшее живое (4 lvl Miasma of Entropy)':1,
        '2 lvl Призвать рой насекомых (2 lvl Summon Swarm)':1,
        '2 lvl Призвать долгое пламя (2 lvl Continual Flame)':1,
        '2 lvl Призвать живой туман (3 lvl Prismatic Mist)':1,
        '2 lvl Ловушка живых стрел (2 lvl Cordon of Arrows)':1,
        '2 lvl Огненная ловушка (2 lvl Fire Trap)':1,
        }

metadict_detail['Заклинания Эглан 3 lvl'] = {
        '3 lvl Подчинить другого (3 lvl Dominate Animal)':1,
        '3 lvl Слово оглушения (3 lvl Power Word Deafen)':1,
        '3 lvl Слово неуклюжести (3 lvl Power Word Maladroit)':1,
        '3 lvl Слово ослабления (3 lvl Power Word Weaken)':1,
        '3 lvl Круг против зла (3 lvl Magic Circle Against Evil)':1,
        '3 lvl Говорить с растением (3 lvl Speak With Plants)':1,
        '3 lvl Найти коснувшегося воды (5 lvl Flowsight)':1,
        '3 lvl Нейтрализовать яд (3 lvl Neutralize Poison)':1,
        '3 lvl Исцелить болезнь (3 lvl Remove Disease)':1,
        '3 lvl Исцелить рану (3 lvl Cure Moderate Wounds)':1,
        '3 lvl Ускорить рост деревьев (3 lvl Plant Growth)':1,
        '3 lvl Остановить рост деревьев (3 lvl Diminish Plants)':1,
        '3 lvl Укрыться в камне (3 lvl Meld Into Stone)':1,
        '3 lvl Изменить форму камня (3 lvl Stone Shape)':1,
        '3 lvl Дыхательная вода (5 lvl Airy Water)':1,
        '3 lvl Воздушная стена (3 lvl Wind Wall)':1,
        '3 lvl Касание отравления (3 lvl Poison)':1,
        '3 lvl Призвать животное (5 lvl Halaster\'s Fetch Ii)':1,
        '3 lvl Остановить пожар (3 lvl Quench, 6 lvl Suppress Flame)':1,
        '3 lvl Создать западню (3 lvl Snare, 7 lvl Ghost Trap)':1,
        '3 lvl Призвать молнию (3 lvl Call Lightning)':1,
        '3 lvl Землю в шипы (3 lvl Spike Growth)':1,
        }

metadict_detail['Заклинания Эглан 4 lvl'] = {
        '4 lvl Утихомирить дракона (4 lvl Abate Dracorage)':1,
        '4 lvl Подчинить призрака (5 lvl Planar Binding, Lesser)':1,
        '4 lvl Подчинить магическое чудовище (5 lvl Hold Monster)':1,
        '4 lvl Форма подводного создания (5 lvl Transformation of the Deeps)':1,
        '4 lvl Форма полудракона (4 lvl Flight of the Dragon, 3 lvl Dragonskin)':1,
        '4 lvl Сверкающая чешуя (2 lvl Scintillating Scales)':1,
        '4 lvl Драконье дыхание (3 lvl Dragon Breath)':1,
        '4 lvl Подчиняющй голос (4 lvl Voice of the Dragon)':1,
        '4 lvl Изменить драконье дыхание (4 lvl Breath Weapon Substitution)':1,
        '4 lvl Выплюнуть змею (3 lvl Vipergout)':1,
        '4 lvl Скорпионий хвост (3 lvl Scorpion Tail)':1,
        '4 lvl Вампирье касание (3 lvl Vampiric Touch)':1,
        '4 lvl Огненная форма (5 lvl Heart of Fire)':1,
        '4 lvl Рассеивание энергии (4 lvl Glacial Ward)':1,
        '4 lvl Остановить сердце (5 lvl Stop Heart, 6 lvl Heartfreeze)':1,
        '4 lvl Защита духа (5 lvl Indomitability, 7 lvl Justice of the Wyrm King)':1,
        '4 lvl Перенести душу в предмет (5 lvl Magic Jar, 5 lvl Soul Shackles)':1,
        '4 lvl Призвать зубастых (3 lvl Manyjaws, 7 lvl Whirl of Fangs)':1,
        '4 lvl Призванный коготь (4 lvl Force Claw, 4 lvl Caligarde\'s Claw)':1,
        '4 lvl Змей из надписи (3 lvl Sepia Snake Sigil)':1,
        }

metadict_detail['Заклинания Эглан 5 lvl'] = {
        '5 lvl Подчинить духа места (6 lvl Control Elemental)':1,
        '5 lvl Стена духов (5 lvl Spiritwall)':1,
        '5 lvl Драконья сила (5 lvl Draconic Might)':1,
        '5 lvl Драконье зрение (5 lvl Dragonsight)':1,
        '5 lvl Драконья смена формы (5 lvl Draconic Polymorph)':1,
        '5 lvl Сопротивляемость магии (5 lvl Skin of the Steel Dragon)':1,
        '5 lvl Поразить призраков дыханием (5 lvl Ethereal Breath)':1,
        '5 lvl Символ боли (5 lvl Symbol of Pain)':1,
        '5 lvl Символ усыпления (5 lvl Symbol of Sleep)':1,
        '5 lvl Символ антимагии (5 lvl Symbol of Spell Loss)':1,
        '5 lvl Взять символ (6 lvl Transcribe Symbol, 8 lvl Transcribe Symbol)':1,
        '5 lvl Круг запрета (3 lvl Bane of the Archrival, 6 lvl Sign of Sealing)':1,
        '5 lvl Круг отталкивания (6 lvl Repulsion)':1,
        '5 lvl Круг лезвий (4 lvl Bladebane, 5 lvl Coat of Arms)':1,
        '5 lvl Щупальце тёмной воды (5 lvl Blackwater Tentacle)':1,
        '5 lvl Призвать подчинённых духов (5 lvl Call Faithful Servants)':1,
        '5 lvl Призвать прыгающий огонь (5 lvl Jumpgout)':1,
        '5 lvl Призвать градины (3 lvl Hailstones, 4 lvl Ice Storm)':1,
        '5 lvl Ледяной ветер (5 lvl Boreal Wind)':1,
        '5 lvl Морозный туман (5 lvl Freezing Fog)':1,
        '5 lvl Заморозить (5 lvl Flesh to Ice, 5 lvl Gelid Blood)':1,
        '5 lvl Оживить лёд (5 lvl Ice to Flesh)':1,
        '5 lvl Перестроить лёд (5 lvl Ice Shape)':1,
        }

metadict_detail['Заклинания Эглан 6 lvl'] = {
        '6 lvl Слово тошноты (6 lvl Power Word Nauseate)':1,
        '6 lvl Слово убийственной боли (7 lvl Nybor\'s Stern Reproof)':1,
        '6 lvl Символ жажды (6 lvl Symbol of Thirst)':1,
        '6 lvl Символ страха (6 lvl Symbol of Fear)':1,
        '6 lvl Символ очарования (6 lvl Symbol of Persuasion)':1,
        '6 lvl Единство с океаном (6 lvl Cloak of the Sea)':1,
        '6 lvl Извлечь водного духа из живого (6 lvl Extract Water Elemental)':1,
        '6 lvl Открыть тайны (6 lvl Legend Lore, 7 lvl Vision)':1,
        '6 lvl Отделить глаз (7 lvl Eye of the Beholder)':1,
        '6 lvl Взгляд ужаса (6 lvl Eyebite, 6 lvl Imperious Glare)':1,
        '6 lvl Леденящий взгляд (6 lvl Freezing Glance)':1,
        '6 lvl Взгляд уничтожения немёртвых (6 lvl Opalescent Glare)':1,
        '6 lvl Управление немёртвыми (7 lvl Control Undead)':1,
        '6 lvl Превратить в немёртвого (6 lvl Ghoul Gauntlet)':1,
        '6 lvl Огненный плащ (6 lvl Fires of Purity)':1,
        '6 lvl Форма волшебного чудовища (6 lvl Bite of the Werebear)':1,
        '6 lvl Форма живого льда (7 lvl As the Frost)':1,
        '6 lvl Каменное тело (6 lvl Stone Body)':1,
        '6 lvl Камень в плоть (6 lvl Stone to Flesh)':1,
        '6 lvl Изгнание духов (6 lvl Banishment)':1,
        '6 lvl Захватить вселившегося (6 lvl Impotent Possessor)':1,
        '6 lvl Управлять слизистым (6 lvl Ooze Puppet)':1,
        '6 lvl Призвать призрачного дракона (6 lvl Spectral Dragon)':1,
        '6 lvl Холод тёмной воды (6 lvl Blackwater Taint)':1,
        '6 lvl Расколоть лёд (6 lvl Ice Rift)':1,
        }

metadict_detail['Заклинания Эглан 7 lvl'] = {
        '7 lvl Слово ослепления (7 lvl Power Word Blind)':1,
        '7 lvl Символ оцепенения (7 lvl Symbol of Stunning)':1,
        '7 lvl Символ ослабления (7 lvl Symbol of Weakness)':1,
        '7 lvl Создать ледяной замок (7 lvl Ice Castle)':1,
        '7 lvl Охранный знак слабости (7 lvl Retributive Enervation)':1,
        '7 lvl Регенерация (7 lvl Regenerate)':1,
        '7 lvl Обманчивый путь (7 lvl Shifting Paths)':1,
        '7 lvl Форма немёртвого (7 lvl Kiss of the Vampire, 8 lvl Veil of Undeath)':1,
        '7 lvl Усилить помощников, всех (7 lvl Animalistic Power, Mass)':1,
        '7 lvl Форма немёртвого дракона (7 lvl Death Dragon)':1,
        '7 lvl Оживить драконье дыхание (7 lvl Animate Breath)':1,
        '7 lvl Дыхание развеивания чар (4 lvl Dispelling Breath)':1,
        '7 lvl Даровать разум немёртвому (7 lvl Awaken Undead)':1,
        '7 lvl Уничтожить вселившегося и жертву (7 lvl Lifebound)':1,
        '7 lvl Управление погодой (8 lvl Mastery of the Sky, 7 lvl Control Weather)':1,
        '7 lvl Призвать дракона (7 lvl Dragon Ally, 7 lvl Summon Aspect of Bahamut)':1,
        '7 lvl Призвать пламя и молнии (7 lvl Glorious Master of the Elements)':1,
        '7 lvl Призвать стену глаз (7 lvl Wall of Eyes)':1,
        }

metadict_detail['Заклинания Эглан 8 lvl'] = {
        '8 lvl Очаровать орду (8 lvl Charm Monster, Mass)':1,
        '8 lvl Подчинить другого, полностью (8 lvl True Domination)':1,
        '8 lvl Слово окаменения (8 lvl Power Word Petrify)':1,
        '8 lvl Слово оцепенения (8 lvl Power Word Stun)':1,
        '8 lvl Символ смерти (8 lvl Symbol, 8 lvl Symbol of Death)':1,
        '8 lvl Символ безумия (8 lvl Symbol of Insanity)':1,
        '8 lvl Шёпот безумия (8 lvl Maddening Whispers)':1,
        '8 lvl Создать каменное сердце (8 lvl Heart of Stone)':1,
        '8 lvl Стальное тело (8 lvl Iron Body)':1,
        '8 lvl Зверя в волшебное создание (8 lvl Axiomatic Creature)':1,
        '8 lvl Проклятие бессилия (8 lvl Bestow Curse, Greater)':1,
        '8 lvl Захватить душу в кристалл (8 lvl Trap the Soul)':1,
        '8 lvl Форма немёртвого рыцаря (8 lvl Unyielding Form of Inevitable Death)':1,
        '8 lvl Создать совершенного немёртвого (8 lvl Create Greater Undead)':1,
        '8 lvl Поле ледяных лезвий (8 lvl Zajimarn\'s Field of Icy Razors, 8 lvl Flensing)':1,
        '8 lvl Усилить драконье дыхание (8 lvl Breath Weapon Admixture)':1,
        '8 lvl Оглушающее драконье дыхание (8 lvl Deafening Breath)':1,
        '8 lvl Ледяной коготь (7 lvl Zajimarn\'s Ice Claw Prison, 8 lvl Icy Claw)':1,
        '8 lvl Вырвать внутренности и поглотить (8 lvl Gutwrench)':1,
        '8 lvl Пылающая земля (8 lvl Deadly Lahar)':1,
        '8 lvl Призвать зиму (8 lvl Fimbulwinter)':1,
        '8 lvl Цунами (8 lvl Depthsurge)':1,
        '8 lvl Призвать духа (8 lvl Summon Monster VIII)':1,
        '8 lvl Призвать орду (8 lvl Fierce Pride of the Beastlands)':1,
        }

metadict_detail['Заклинания Эглан 9 lvl'] = {
        '9 lvl Слово смерти (9 lvl Power Word Kill)':1,
        '9 lvl Создать духа места (9 lvl Genius Loci)':1,
        '9 lvl Разум в мир духов (9 lvl Astral Projection)':1,
        '9 lvl Спрятать душу в части тела (9 lvl Hide Life)':1,
        '9 lvl Подчинить чудовище, навсегда (9 lvl Monstrous Thrall)':1,
        '9 lvl Форма истинного дракона (9 lvl Dragonshape)':1,
        '9 lvl Дыхание ранящее души (9 lvl Enervating Breath)':1,
        '9 lvl Похитить душу живого (9 lvl Ensul\'s Soultheft)':1,
        '9 lvl Разлом до подземеного мира (9 lvl Abyssal Rift)':1,
        '9 lvl Создать подобие, убийцу оригинала (7 lvl Ice Assassin)':1,
        '9 lvl Призвать великого дракона (9 lvl Dragon Ally, Greater)':1,
        '9 lvl Призвать незлобных (9 lvl Heavenly Host)':1,
        '9 lvl Призвать злобных (9 lvl Abyssal Army)':1,
        '9 lvl Ослабить душу (9 lvl Energy Drain)':1,
        }

## ----
# Правила восстановления заклинаний:
# Это главное отличие от системы D&D. Там, чтобы восстановить использованное заклинание, волшебник должен отдохнуть положенные несколько часов, а волшебной единорожке нужно всего лишь несколько секунд/минут покоя.
# Восстановление заклинания (раундов медитации):
# `10 * (круг_заклинания + 1) - (концентрация + искусство_заклинаний + 1d20)`
# Например, Твайка 12 уровня, заклинание 4 круга:
# `10 * (4 + 1) - (16 + 22 + 10) = 2 раунда (12 секунд)`
# Обкастованная по уши Твайка, защищённая практически от всего:
# `10 * (4 + 1) - ((16-13) + 22 + 10) = 15 раундов (1.5 минуты)`
# Так получается, что волшебник, это либо танк, обкастованный по уши, но восстанавливающий свои огнешары по несколько минут, либо беззащитная, но крайне опасная гаубица, с впечатляющим темпом стрельбы. Есть ещё третий вариант -- атаки и отступления, чтобы снять щиты и восстановить заклинания, но это уже авиация.

metadict_detail['Восстановление заклинаний (RND)'] = {
        'Восстановление заклинаний (раундов)':-1,
        }

metadict_detail['Восстановление заклинаний (Концентрация)'] = {
        'Восстановление заклинаний (раундов)':-1,
        }

metadict_detail['Восстановление заклинаний (Магическое искусство)'] = {
        'Восстановление заклинаний (раундов)':-1,
        }

metadict_detail['Восстановление заклинаний (раундов)'] = {
        '0 lvl (заклинания) (восстановление/раундов)':1,
        '1 lvl (заклинания) (восстановление/раундов)':1,
        '2 lvl (заклинания) (восстановление/раундов)':1,
        '3 lvl (заклинания) (восстановление/раундов)':1,
        '4 lvl (заклинания) (восстановление/раундов)':1,
        '5 lvl (заклинания) (восстановление/раундов)':1,
        '6 lvl (заклинания) (восстановление/раундов)':1,
        '7 lvl (заклинания) (восстановление/раундов)':1,
        '8 lvl (заклинания) (восстановление/раундов)':1,
        '9 lvl (заклинания) (восстановление/раундов)':1,
        }

## ----
# Постоянные заклинания (ослабляют концетрацию):
# Единорожка может здорово обкастоваться, но толкни такую -- пискнет, и вся защита развалится.

metadict_army['-=0 lvl Дисковой щит (1 lvl Shield, 3 lvl Repelling Shield)'] = {
        # Поддержка постоянных/защитных заклинаний ослабляет концетрацию `(круг_заклинания + 1)`
        # https://dndtools.net/spells/players-handbook-v35--6/shield--2364/
        # https://dndtools.net/spells/complete-mage--58/repelling-shield--771/
        '=0 lvl Дисковой щит (1 lvl Shield, 3 lvl Repelling Shield)':1,
        '-= Навык (Концентрация) (Active Spells)':-(0 + 1),
        '---Дисковой щит (+4 Deflect)':1,
        '---| Класс доспеха, отражение (Armor Class, deflect)':+4,
        '=- Активные заклинания':+1,
        }

metadict_army['-=1 lvl Доспехи мага (1 lvl Mage Armor, 3 lvl Golden Dragonmail)'] = {
        # https://dndtools.net/spells/players-handbook-v35--6/mage-armor--2405/
        # https://dndtools.net/spells/champions-of-valor--28/golden-dragonmail--308/
        '=1 lvl Доспехи мага (1 lvl Mage Armor, 3 lvl Golden Dragonmail)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 1),
        '---Доспехи мага (+4 Armor)':1,
        '---| Класс доспеха, броня (Armor Class, armor)':+4,
        '=- Активные заклинания':+1,
        }

metadict_detail['-=1 lvl Защитная сфера (2 lvl Resist Energy, 2 lvl Protection from Arrows)'] = {
        # Будем реалистами, в азоте можно искупаться и с обычной защитной сферой.
        # Это же относится и к ударам токам, и к огню. Изоляция есть изоляция.
        # И, кстати говоря, звуком серьёзного урона не нанести. Плотность воздуха, все дела.
        # https://dndtools.net/spells/players-handbook-v35--6/resist-energy--2357/
        # https://dndtools.net/spells/players-handbook-v35--6/protection-from-arrows--2345/
        '=1 lvl Защитная сфера (2 lvl Resist Energy, 2 lvl Protection from Arrows)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 1),
        '---Сопротивляемость огню (Resistance, fire)':+5,
        '---Сопротивляемость холоду (Resistance, cold)':+5,
        '---Сопротивляемость электричеству (Resistance, electricity)':+5,
        '---Сопротивляемость оружию (Damage reduction, magic)':+5,
        '---Сопротивляемость вибрации (Resistance, sonic)':+5,
        '---Сопротивляемость кислоте (Resistance, acid)':+5,
        '=- Активные заклинания':+1,
        }

metadict_detail['-=1 lvl Пёрышко (1 lvl Feather Fall, 1 lvl Jump, 2 lvl Balancing Lorecall)'] = {
        '=1 lvl Пёрышко (1 lvl Feather Fall, 1 lvl Jump, 2 lvl Balancing Lorecall)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 1),
        '---| Скорость, галоп (километров/час)':+3 * 3,
        '---| Скорость, спринт (километров/час)':+3 * 6,
        '-= Навык (Акробатика) (ENC)':+10,                                                             
        '=- Активные заклинания':+1,
        }

metadict_army['-=2 lvl Маскировка под другого (2 lvl Reflective Disguise)'] = {
        '=2 lvl Маскировка под другого (2 lvl Reflective Disguise)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 2),
        '---Маскировка под другого (Reflective Disguise)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=2 lvl Ускорение нейрометаболизма (2 lvl Fox\'s Cunning)'] = {
        '=2 lvl Ускорение нейрометаболизма (2 lvl Fox\'s Cunning)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 2),
        '---Ускорение нейрометаболизма (+4 INT)':1,
        '---| Интеллект (зачарование)':+4,
        '=- Активные заклинания':+1,
        }

metadict_detail['-=2 lvl Защитная сфера-накопитель (2 lvl Resist Energy)'] = {
        # https://dndtools.net/spells/players-handbook-v35--6/resist-energy--2357/
        # https://dndtools.net/spells/players-handbook-ii--80/energy-aegis--2910/
        '=2 lvl Защитная сфера-накопитель (2 lvl Resist Energy)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 2),
        '---Сопротивляемость огню (Resistance, fire)':+10,
        '---Сопротивляемость холоду (Resistance, cold)':+10,
        '---Сопротивляемость электричеству (Resistance, electricity)':+10,
        '---Сопротивляемость оружию (Damage reduction, magic)':+10,
        '---Сопротивляемость вибрации (Resistance, sonic)':+10,
        '---Сопротивляемость кислоте (Resistance, acid)':+10,
        '=- Активные заклинания':+1,
        }

metadict_army['-=3 lvl Защитная сфера-отражатель (4 lvl Ray Deflection, 4 lvl Forceward)'] = {
        # https://dndtools.net/spells/spell-compendium--86/ray-deflection--4063/
        # https://dndtools.net/spells/spell-compendium--86/forceward--3795/
        '=3 lvl Защитная сфера-отражатель (4 lvl Ray Deflection, 4 lvl Forceward)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 3),
        '---Защитная сфера-отражатель (+8 Deflect)':1,
        '---| Класс доспеха, отражение (Armor Class, deflect)':+8,
        '=- Активные заклинания':+1,
        }

metadict_army['-=3 lvl Предвидеть магию (3 lvl Battlemagic Perception)'] = {
        # https://dndtools.net/spells/heroes-of-battle--69/battlemagic-perception--1403/
        '=3 lvl Предвидеть магию (3 lvl Battlemagic Perception)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 3),
        '---Предвидеть магию (Battlemagic Perception)':1,
        '=- Активные заклинания':+1,
        }

metadict_detail['-=4 lvl Корона силы (3 lvl Crown of Might)'] = {
        # Добавляет +2 к силе, или +8 на один раунд. Берём по максимуму.
        '=4 lvl Корона силы (3 lvl Crown of Might)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 4),
        '---Корона силы (+8 STR)':1,
        '---| Сила (зачарование)':+8,
        '=- Активные заклинания':+1,
        }

metadict_army['-=4 lvl Доспехи мага-лорда (5 lvl Mailed Might of the Magelords)'] = {
        # https://dndtools.net/spells/unapproachable-east--33/improved-mage-armor--3459/
        # https://dndtools.net/spells/lost-empires-of-faerun--30/mailed-might-of-the-magelords--1556/
        '=4 lvl Доспехи мага-лорда (5 lvl Mailed Might of the Magelords)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 4),
        '---Доспехи мага-лорда (+8 Armor)':1,
        '---| Класс доспеха, броня (Armor Class, armor)':+8,
        '---Сопротивляемость оружию (Damage reduction, magic)':+5,
        '=- Активные заклинания':+1,
        }

metadict_army['-=4 lvl Щит антимагии (4 lvl Otiluke\'s Dispelling Screen)'] = {
        # https://dndtools.net/spells/complete-arcane--55/otilukes-dispelling-screen--441/
        '=4 lvl Щит антимагии (4 lvl Otiluke\'s Dispelling Screen)':+1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 4),
        '---Щит антимагии (Otiluke\'s Dispelling Screen)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=5 lvl Рассеивание энергии (5 lvl Energy Buffer)'] = {
        # https://dndtools.net/spells/masters-of-the-wild-a-guidebook-to-barbarians-druids-and-rangers--44/protection-from-all-elements--1877/
        # https://dndtools.net/spells/tome-and-blood-a-guidebook-to-wizards-and-sorcerers--51/energy-buffer--3378/
        '=5 lvl Рассеивание энергии (5 lvl Energy Buffer)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 5),
        '---Сопротивляемость огню (Resistance, fire)':+20,
        '---Сопротивляемость холоду (Resistance, cold)':+20,
        '---Сопротивляемость электричеству (Resistance, electricity)':+20,
        '---Сопротивляемость вибрации (Resistance, sonic)':+20,
        '---Сопротивляемость кислоте (Resistance, acid)':+20,
        '=- Активные заклинания':+1,
        }

metadict_army['-=5 lvl Ускорить контрзаклинания (5 lvl Duelward)'] = {
        '=5 lvl Ускорить контрзаклинания (5 lvl Duelward)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 5),
        '---Ускорить контрзаклинания (Duelward)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=6 lvl Зона защитной магии (5 lvl Field of Resistance, 6 lvl Guards and Wards)'] = {
        '=6 lvl Зона защитной магии (5 lvl Field of Resistance, 6 lvl Guards and Wards)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 6),
        '---Зона защитной магии (Field of Resistance)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=6 lvl Взгляд истины (6 lvl True Seeing)'] = {
        '=6 lvl Взгляд истины (6 lvl True Seeing)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 6),
        '---Взгляд истины (True Seeing)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=7 lvl Щит поглощения энергии (7 lvl Energy Absorption)'] = {
        # https://dndtools.net/spells/complete-mage--58/energy-absorption--764/
        '=7 lvl Щит поглощения энергии (7 lvl Energy Absorption)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 7),
        '---Поглощение энергии (Energy Absorption)':1,
        '---Сопротивляемость огню (Resistance, fire)':+10,
        '---Сопротивляемость холоду (Resistance, cold)':+10,
        '---Сопротивляемость электричеству (Resistance, electricity)':+10,
        '---Сопротивляемость вибрации (Resistance, sonic)':+10,
        '---Сопротивляемость кислоте (Resistance, acid)':+10,
        '=- Активные заклинания':+1,
        }

metadict_army['-=8 lvl Абсолютная защита разума (8 lvl Mind Blank, 8 lvl Mind of the Labyrinth)'] = {
        '=8 lvl Абсолютная защита разума (8 lvl Mind Blank, 8 lvl Mind of the Labyrinth)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 8),
        '---Абсолютная защита разума (Mind of the Labyrinth)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=9 lvl Подготовленный мгновенный переход (9 lvl Instant Refuge)'] = {
        '=9 lvl Подготовленный мгновенный переход (9 lvl Instant Refuge)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 9),
        '---Подготовленный мгновенный переход (Instant Refuge)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=9 lvl Поглотители магии (9 lvl Elminster\'s Effulgent Epuration)'] = {
        # https://dndtools.net/spells/spell-compendium--86/effulgent-epuration--4433/
        # https://forgottenrealms.fandom.com/wiki/Elminster%27s_effulgent_epuration
        '=9 lvl Поглотители магии (9 lvl Elminster\'s Effulgent Epuration)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 9),
        '---Подлотители магии (Effulgent Epuration)':20,
        '=- Активные заклинания':+1,
        }

# ---

metadict_army['-=2 lvl Маскировка от заклинаний (2 lvl Misdirection, 2 lvl Obscure Object)'] = {
        # https://dndtools.net/spells/players-handbook-v35--6/misdirection--2685/
        # https://dndtools.net/spells/players-handbook-v35--6/obscure-object--2342/
        '=2 lvl Маскировка от заклинаний (2 lvl Misdirection, 2 lvl Obscure Object)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 2),
        '---Маскировка от заклинаний (Misdirection)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=2 lvl Усиление слуха (2 lvl Listening Lorecall)'] = {
        # https://dndtools.net/spells/complete-adventurer--54/listening-lorecall--381/
        '=2 lvl Усиление слуха (2 lvl Listening Lorecall)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 2),
        '-= Навык (Прислушивание) (ENC)':+4,
        '---Эхолокация (Blindsight)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=3 lvl Слепое зрение (3 lvl Blindsight)'] = {
        '=3 lvl Слепое зрение (3 lvl Blindsight)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 3),
        '---Слепое зрение (Blindsight)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=4 lvl Стальная кожа (3 lvl Improved Mage Armor, 4 lvl Stoneskin)'] = {
        '=4 lvl Стальная кожа (3 lvl Improved Mage Armor, 4 lvl Stoneskin)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 4),
        '---| Класс доспеха, броня (Armor Class, armor)':+8,
        '---Сопротивляемость оружию (Damage reduction, adamantine)':+10,
        '---Стальная кожа (+8 Armor)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=4 lvl Маска очарования (3 lvl Mask of the Ideal)'] = {
        '=4 lvl Маска очарования (3 lvl Mask of the Ideal)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 4),
        '-= Навык (Маскировка) (ENC)':+4,
        '-= Навык (Дипломатия) (ENC)':+4,
        '-= Навык (Обман) (ENC)':+4,
        '=- Активные заклинания':+1,
        }

metadict_army['-=5 lvl Идеальная маскировка под другого (5 lvl Veil)'] = {
        '=5 lvl Идеальная маскировка под другого (5 lvl Veil)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 5),
        '---Маскировка под другого (Veil)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=5 lvl Отследить наблюдение (4 lvl Detect Scrying)'] = {
        '=5 lvl Отследить наблюдение (4 lvl Detect Scrying)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 5),
        '---Отследить наблюдение (Detect Scrying)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=6 lvl Поток предсказаний (6 lvl Eyes of the Oracle, 6 lvl Glimpse of the Prophecy)'] = {
        # Даёт свободный раунд, этим завершая заклинание:
        # https://dndtools.net/spells/dragon-magic--62/eyes-of-the-oracle--1057/
        '=6 lvl Поток предсказаний (6 lvl Eyes of the Oracle, 6 lvl Glimpse of the Prophecy)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 6),
        '---Поток предсказаний (Eyes of the Oracle)':1,
        '---| Класс доспеха, интуиция (Armor Class, insight)':+2,
        '---| Спасбросок рефлексов (ENC)':+2,
        '=- Активные заклинания':+1,
        }

metadict_army['-=6 lvl Сковывающая защита разума (5 lvl Imprison Possessor)'] = {
        '=6 lvl Сковывающая защита разума (5 lvl Imprison Possessor)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 6),
        '---Сковывающая защита разума (Imprison Possessor)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=7 lvl Видеть магию и распознать (7 lvl Arcane Sight, Greater)'] = {
        # https://dndtools.net/spells/players-handbook-v35--6/arcane-sight--2476/
        # https://www.dandwiki.com/wiki/SRD:Greater_Arcane_Sight
        '=7 lvl Видеть магию и распознать (7 lvl Arcane Sight, Greater)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 7),
        '---Видеть магию и распознать (Arcane Sight, Greater)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=7 lvl Щит архонтов (7 lvl Shield of the Archons)'] = {
        # Поглощает магические атаки с 5% шансом развалитсья на уровень заклинания.
        # Сталоб быть, заклинание 9 круга сносит щит с вероятностью 50%.
        # https://dndtools.net/spells/book-of-exalted-deeds--52/shield-of-the-archons--12/
        '=7 lvl Щит архонтов (7 lvl Shield of the Archons)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 7),
        '---Щит архонтов (Shield of the Archons)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=9 lvl Идеальная невидимость (9 lvl Superior Invisibility)'] = {
        # https://dndtools.net/spells/complete-arcane--55/superior-invisibility--517/
        '=9 lvl Идеальная невидимость (9 lvl Superior Invisibility)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 9),
        '---Идеальная невидимость (Superior Invisibility)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=9 lvl Предвидение (9 lvl Foresight)'] = {
        # https://dndtools.net/spells/players-handbook-v35--6/foresight--2500/
        '=9 lvl Предвидение (9 lvl Foresight)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 9),
        '---| Класс доспеха, интуиция (Armor Class, insight)':+2,
        '---| Спасбросок рефлексов (ENC)':+2,
        '---Предвидение (Foresight)':1,
        '=- Активные заклинания':+1,
        }

metadict_army['-=9 lvl Аватар-заклинатель (9 lvl Eye of Power)'] = {
        '=9 lvl Аватар-заклинатель (9 lvl Eye of Power)':1,
        '-= Навык (Концентрация) (Active Spells)':-(1 + 9),
        '---Аватар-заклинатель (Eye of Power)':1,
        '=- Активные заклинания':+1,
        }
