#----
# Планировка городов (генеральные планы):
# . - поля (50x50 метров, 1/4 гектара)
# ---- - грунтовки (шириной 5-15 метров)
# ==== - шоссе, мостовые (шириной 15-30 метров)
# hhhh - пригороды (700 000 кв. метров, 1200 домов)
# HHHH - кварталы (600 000 метров, до 3000 домов)
# mmmm - рынки, ярмарочные площади (40 000 кв. метров)
# MMMM - магазины, торговые ряды (10 000 кв. метров)
# !!!! - центральная площадь (15 000 кв. метров)
# CCCC - культурные здания (25 000 кв. метров)
# FFFF - фабрики, мануфактуры (80 000 кв. метров)
# pppp - пристани, пирсы, порты (500 метров, до 20 барж)
# ssss - амбары, элеваторы, овощехранилища (100 000 кв. метров)
# SSSS - товарные склады, промышленные склады (100 000 кв. метров)
# &1 - водопровод (водозаборная станция)
# &2 - водопровод (водоочистная станция)
# &3 - водопровод (водонапорная станция)
# &4 - канализация (стокоподъёмная станция)
# &5 - канализация (оросительные каналы)
# ^^^ - станционные пути, вагонная станция
# ^ - железная дорога (Филлидельфия-Мэйнхеттен)
# # - взлётная полоса (для пегасьих планёров)
# R - водохранилище, река (водосбор 10 000 км², 800 мм/год, коэффициент стока 0.25 -- 64 м³/секунду)
# ]&- плотина с ГЭС (высота сброса -- 5 метров, механическая энергия: 2.2 МВт)
# http://wikimapia.org/#lang=ru&lat=54.434140&lon=21.012661&z=17&m=bs&show=/14801861/ru/Правдинская-ГЭС-3
# RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR]...^...........
# RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR]RRR^RRRRRRRRRRR
# .&1.RRRRRRRRRRRRRRppppRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRpppppp]&..^........&4.
# ===============================================================^===========
# |hhhhhhhhhh|hhhhhhssmm=HHHH=HHHH=HHHH=HHHH=HHHH=HHHH=FFFF=FFFFF^^^SSSSS.hh|
# |..........|......ssmm=H,,H=H,,H=HHHH=HHHH=HHHH=HHHH=FFFF=FFFFF^^^SSSSS...|
# |..........|......ssmm=H,,H=H,,H=HHHH=HHHH=HHHH=HHHH=FFFF=FFFFF^^^SSSSS...|
# |hhhhhhhhhh|hhhhhhssmm=HHHH=HHHH=HHHH=HHHH=MMMM=HHHH=FFFF=FFFFF^^^SSSSS.hh|
# ----------------------=========================================^^^---------
# |hhhhhhhhhh|hhhhhhhhhh=HHHH=HHHH=CCCC=HHHH=HHHH=HHHH=ssss=#####^^^hhhhhhhh|
# |..........|.........h=H,,H=H,,H=C!!C=HHHH=HHHH=HHHH=ssss=h...#^^^........|
# |..........|.........h=H,,H=H,,H=C!!C=HHHH=HHHH=HHHH=ssss=h...#^^^........|
# |hhhhhhhhhh|hhhhhhhhhh=HHHH=HHHH=C!!C=HHHH=HHHH=HHHH=ssss=hhh.#^^^hhhhhhhh|
# ----------------------====================================----#^^^---------
# |hhhhhhhhhh|hhhhhhhhhh=HHHH=HHHH=HHHH=HHHH=HHHH=HHHH=mmss=hhh.#^^^hhhhhhhh|
# |..........|.........h=H,,H=H,,H=H,,H=H,,H=H,,H=H,,H=mmss=h...#^^^........|
# |..........|.........h=H,,H=H,,H=H,,H=H,,H=H,,H=H,,H=mmss=h...#^^^........|
# |hhhhhhhhhh|hhhhhhhhhh=HHHH=HHHH=HHHH=HHHH=HHHH=HHHH=mmss=hhh.#^^^hhhhhhhh|
# ----------------------====================================----#^----------|
# |hhhhhhhhhh|hhhhhhhhhh=hhhhhhhhh|hhhhhhhhh|hhhhhhhhh=hhhhhhhh.#^.hhhhhhhhh|
# |..........|.........h=.........|.........|.........=.........#^..........|
# |&&2.......|.........h=.........|.........|.........=.........#^..........|
# |&&2..hhhhh|hhhhhhhhhh=&3..hhhhh|hhhhhhhhh|hhhhhhhhh=hhhhhhhh.#^.hhhhh..&5|
# ----------------------=-----------------------------=----------^-----------

metadict_model['-Город (строительство)'] = {
        # Каменных зданий всего 30-50%
            # https://ru.wikisource.org/wiki/ЭСБЕ/Рыбинск
        '-Жилой квартал 50x200 метров':50,
        '-Городской водопровод (50 кварталов)':1,
        }

metadict_model['-Жилой квартал 50x200 метров'] = {
        # https://en.wikipedia.org/wiki/Terraced_house
        # https://upload.wikimedia.org/wikipedia/commons/7/72/Bath%2C_Somerset_Panorama_-_April_2011.jpg
        # https://upload.wikimedia.org/wikipedia/commons/9/91/Bathwick_Hill%2C_Bath%2C_Somerset%2C_UK_-_Diliff.jpg
        # H - густая застройка 3-этажками (40 домов).
        # = - взлётная полоса для планёров.
        # ----------------------
        # |HHHHHHHHHHHHHHHHHHHH|
        # |....................|
        # |====================|
        # |....................|
        # |HHHHHHHHHHHHHHHHHHHH|
        # ----------------------
        'Городской двор (строительство)':40,
        'Городская мостовая (метр)':(50 + 200) * 2,
        'Взлётная полоса для лёгких планёров (метр)':200,
        }

#----
# Железнодорожные здания (оборудование):

metadict_model['-Железнодорожная дистанция'] = {
        # TODO:
            # Пили устройство, пили оборудование.
        # https://ru.wikisource.org/wiki/ЭСБЕ/Станции_железных_дорог
        }

metadict_model['-Железнодорожный околоток'] = {
        }

metadict_model['-Железнодорожный пост'] = {
        }

metadict_model['-Железнодорожное депо'] = {
        }

metadict_model['-Железнодорожный вокзал'] = {
        }

metadict_model['-Железнодорожная станция'] = {
        }

#----
# Железнодорожные здания (строительство):

metadict_model['Железнодорожный вокзал (строительство)'] = {
        # TODO:
            # Хватит заглушек, допиливай!
        }

metadict_model['Железнодорожная станция (строительство)'] = {
        }

metadict_model['Железнодорожный пост (строительство)'] = {
        }

#----
# Общежития:

metadict_model['Городское жильё, общежитие (квадратный метр)'] = {
        'Городское жильё, общежитие (эксплуатация) (квадратный метр)':1,
        'Городское жильё, общежитие (строительство) (квадратный метр)':1 / 50,
        }

metadict_army['Городское жильё, общежитие (эксплуатация) (квадратный метр)'] = {
        'Городской двор, общежитие (эксплуатация)':1 / 600,
        }

metadict_army['Городское жильё, общежитие (строительство) (квадратный метр)'] = {
        'Городской двор, общежитие (строительство)':1 / 600,
        }

metadict_model['Городской двор, общежитие (эксплуатация)'] = {
        'Отделка трёхэтажного общежития':1,
        #'Отделка шахтного колодца':1,
        '|-Усадьба (квадратный метр)':40 * 40,
        }

metadict_model['Городской двор, общежитие (строительство)'] = {
        'Трёхэтажное общежитие (смета)':1,
        #'Шахтный колодец (смета)':1 / 5,
        }

#----
# Школы (упрощение):

metadict_army['Школьное жильё, класс, начальная школа (квадратный метр)'] = {
        'Школьное жильё, класс (квадратный метр)':1,
        }

metadict_army['Школьное жильё, аудитория, средняя школа (квадратный метр)'] = {
        'Школьное жильё, аудитория (квадратный метр)':1,
        }

metadict_army['Школьное жильё, аудитория, старшая школа (квадратный метр)'] = {
        'Школьное жильё, аудитория (квадратный метр)':1,
        }

metadict_army['Школьное жильё, аудитория, университет (квадратный метр)'] = {
        'Школьное жильё, аудитория (квадратный метр)':1,
        }

#----
# Школы (начальные):

metadict_model['Школьное жильё, класс (квадратный метр)'] = {
        'Школьное жильё, класс (эксплуатация) (квадратный метр)':1,
        'Школьное жильё, класс (строительство) (квадратный метр)':1 / 30,
        }

metadict_army['Школьное жильё, класс (эксплуатация) (квадратный метр)'] = {
        'Сельский двор, школа (эксплуатация)':1 / 80,
        }

metadict_army['Школьное жильё, класс (строительство) (квадратный метр)'] = {
        'Сельский двор, школа (строительство)':1 / 80,
        }

metadict_model['Сельский двор, школа (эксплуатация)'] = {
        'Отделка одноэтажной школы':1,
        #'Отделка шахтного колодца':1,
        '|-Усадьба (квадратный метр)':30 * 60,
        }

metadict_model['Сельский двор, школа (строительство)'] = {
        'Одноэтажная школа (смета)':1,
        #'Шахтный колодец (смета)':1 / 5,
        }


#----
# Школы (городские):

metadict_model['Школьное жильё, аудитория (квадратный метр)'] = {
        'Школьное жильё, аудитория (эксплуатация) (квадратный метр)':1,
        'Школьное жильё, аудитория (строительство) (квадратный метр)':1 / 50,
        }

metadict_army['Школьное жильё, аудитория (эксплуатация) (квадратный метр)'] = {
        'Городской двор, школа (эксплуатация)':1 / 600,
        }

metadict_army['Школьное жильё, аудитория (строительство) (квадратный метр)'] = {
        'Городской двор, школа (строительство)':1 / 600,
        }

metadict_model['Городской двор, школа (эксплуатация)'] = {
        'Отделка трёхэтажной школы':1,
        #'Отделка шахтного колодца':1,
        '|-Усадьба (квадратный метр)':40 * 100,
        }

metadict_model['Городской двор, школа (строительство)'] = {
        'Трёхэтажная школа (смета)':1,
        #'Шахтный колодец (смета)':1 / 5,
        }

#----
# Амбулатории:

metadict_model['Больничное жильё, кабинет (квадратный метр)'] = {
        'Больничное жильё, кабинет (эксплуатация) (квадратный метр)':1,
        'Больничное жильё, кабинет (строительство) (квадратный метр)':1 / 50,
        }

metadict_army['Больничное жильё, кабинет (эксплуатация) (квадратный метр)'] = {
        'Городской двор, больница (эксплуатация)':1 / 600,
        }

metadict_army['Больничное жильё, кабинет (строительство) (квадратный метр)'] = {
        'Городской двор, больница (строительство)':1 / 600,
        }

#----
# Больницы:

metadict_model['Больничное жильё, палаты (квадратный метр)'] = {
        'Больничное жильё, палаты (эксплуатация) (квадратный метр)':1,
        'Больничное жильё, палаты (строительство) (квадратный метр)':1 / 50,
        }

metadict_army['Больничное жильё, палаты (эксплуатация) (квадратный метр)'] = {
        'Городской двор, больница (эксплуатация)':1 / 600,
        }

metadict_army['Больничное жильё, палаты (строительство) (квадратный метр)'] = {
        'Городской двор, больница (строительство)':1 / 600,
        }

metadict_model['Городской двор, больница (эксплуатация)'] = {
        # Длинное здание 40x10 метров, 120 больничных коек.
            # Взлётная полоса для планёров и подъездная дорога.
            # Сад 3000 кв.метров (25 кв.метров на больного)
        'Отделка трёхэтажной больницы':1,
        #'Отделка шахтного колодца':1,
        '|-Усадьба (квадратный метр)':40 * 100,
        }

metadict_model['Городской двор, больница (строительство)'] = {
        'Трёхэтажная больница (смета)':1,
        #'Шахтный колодец (смета)':1 / 5,
        }

#----
# Городской двор (богатый):

metadict_model['Городское жильё, особняк (квадратный метр)'] = {
        # Городские дома обновляются с периодом в 50 лет:
        'Городское жильё, особняк (эксплуатация) (квадратный метр)':1,
        'Городское жильё, особняк (строительство) (квадратный метр)':1 / 50,
        }

metadict_army['Городское жильё, особняк (эксплуатация) (квадратный метр)'] = {
        'Городской двор, особняк (эксплуатация)':1 / 300,
        }

metadict_army['Городское жильё, особняк (строительство) (квадратный метр)'] = {
        'Городской двор, особняк (строительство)':1 / 300,
        }

metadict_model['Городской двор, особняк (эксплуатация)'] = {
        'Отделка двухэтажного особняка':1,
        #'Отделка шахтного колодца':1,
        '|-Усадьба (квадратный метр)':40 * 100,
        }

metadict_model['Городской двор, особняк (строительство)'] = {
        'Двухэтажный особняк (смета)':1,
        #'Шахтный колодец (смета)':1 / 5,
        }

#----
# Городской двор (средний класс):

metadict_model['Городское жильё, квартира (квадратный метр)'] = {
        # Городские дома обновляются с периодом в 50 лет:
        'Городское жильё, квартира (эксплуатация) (квадратный метр)':1,
        'Городское жильё, квартира (строительство) (квадратный метр)':1 / 50,
        }

metadict_model['Городское жильё, квартира (эксплуатация) (квадратный метр)'] = {
        # О жилищном строительстве в 2016 году
        # http://www.gks.ru/bgd/free/B04_03/IssWWW.exe/Stg/d01/21.htm
        'Городской двор, трёхэтажный кирпичный дом (эксплуатация)':1 / 150,
        }

metadict_model['Городское жильё, квартира (строительство) (квадратный метр)'] = {
        'Городской двор, трёхэтажный кирпичный дом (строительство)':1 / 150,
        }

metadict_model['Городской двор, трёхэтажный кирпичный дом (эксплуатация)'] = {
        'Отделка трёхэтажного дома':1,
        #'Отделка шахтного колодца':1 / 5,
        '|-Усадьба (квадратный метр)':10 * 20,
        }

metadict_model['Городской двор, трёхэтажный кирпичный дом (строительство)'] = {
        'Трёхэтажный кирпичный дом (смета)':1,
        #'Шахтный колодец (смета)':1 / 5,
        }

#----
# Городской двор (бедный):

metadict_army['Городское жильё, фахверк (квадратный метр)'] = {
        'Городское жильё, фахверк (эксплуатация) (квадратный метр)':1,
        'Городское жильё, фахверк (строительство) (квадратный метр)':1 / 30,
        }

metadict_model['Городское жильё, фахверк (квадратный метр)'] = {
        'Городское жильё, фахверк (эксплуатация) (квадратный метр)':1,
        'Городское жильё, фахверк (строительство) (квадратный метр)':1 / 30,
        }

metadict_model['Городское жильё, фахверк (эксплуатация) (квадратный метр)'] = {
        'Городской двор, двухэтажный фахверк (эксплуатация)':1 / 120,
        }

metadict_model['Городское жильё, фахверк (строительство) (квадратный метр)'] = {
        'Городской двор, двухэтажный фахверк (строительство)':1 / 120,
        }

metadict_model['Городской двор, двухэтажный фахверк (эксплуатация)'] = {
        'Отделка двухэтажного фахверка':1,
        #'Отделка шахтного колодца':1 / 5,
        '|-Усадьба (квадратный метр)':10 * 20,
        }

metadict_model['Городской двор, двухэтажный фахверк (строительство)'] = {
        'Двухэтажный фахверк (смета)':1,
        #'Шахтный колодец (смета)':1 / 5,
        }

#----
# Сельский двор (богатый):

metadict_model['Сельское жильё, усадьба (квадратный метр)'] = {
        'Сельское жильё, усадьба (эксплуатация) (квадратный метр)':1,
        'Сельское жильё, усадьба (строительство) (квадратный метр)':1 / 50,
        }

metadict_model['Сельское жильё, усадьба (эксплуатация) (квадратный метр)'] = {
        'Сельский двор, усадьба (эксплуатация)':1 / 300,
        }

metadict_model['Сельское жильё, усадьба (строительство) (квадратный метр)'] = {
        'Сельский двор, усадьба (строительство)':1 / 300,
        }

metadict_model['Сельский двор, усадьба (эксплуатация)'] = {
        'Отделка двухэтажной усадьбы':1,
        'Отделка дощатого амбара':1,
        #'Отделка шахтного колодца':1,
        '|-Усадьба (квадратный метр)':40 * 100,
        }

metadict_model['Сельский двор, усадьба (строительство)'] = {
        'Двухэтажная усадьба (смета)':1,
        'Дощатый амбар (смета)':1,
        #'Шахтный колодец (смета)':1,
        }

#----
# Сельский двор (средний класс):

metadict_army['Сельское жильё, фахверк (квадратный метр)'] = {
        'Сельское жильё, фахверк (эксплуатация) (квадратный метр)':1,
        'Сельское жильё, фахверк (строительство) (квадратный метр)':1 / 30,
        }

metadict_model['Сельское жильё, фахверк (квадратный метр)'] = {
        'Сельское жильё, фахверк (эксплуатация) (квадратный метр)':1,
        'Сельское жильё, фахверк (строительство) (квадратный метр)':1 / 30,
        }

metadict_model['Сельское жильё, фахверк (эксплуатация) (квадратный метр)'] = {
        'Сельский двор, двухэтажный фахверк (эксплуатация)':1 / 120,
        }

metadict_model['Сельское жильё, фахверк (строительство) (квадратный метр)'] = {
        'Сельский двор, двухэтажный фахверк (строительство)':1 / 120,
        }

metadict_model['Сельский двор, двухэтажный фахверк (эксплуатация)'] = {
        'Отделка двухэтажного фахверка':1,
        #'Отделка шахтного колодца':1 / 5,
        '|-Усадьба (квадратный метр)':30 * 60,
        }

metadict_model['Сельский двор, двухэтажный фахверк (строительство)'] = {
        'Двухэтажный фахверк (смета)':1,
        #'Шахтный колодец (смета)':1 / 5,
        }

#----
# Сельский двор (среднеземный):

metadict_model['Сельское жильё, каркасный дом (квадратный метр)'] = {
        # Сельские дома обновляются раз в 30 лет:
        'Сельское жильё, каркасный дом (эксплуатация) (квадратный метр)':1,
        'Сельское жильё, каркасный дом (строительство) (квадратный метр)':1 / 30,
        }

metadict_model['Сельское жильё, каркасный дом (эксплуатация) (квадратный метр)'] = {
        # Учитываются только жилые комнаты:
        'Сельский двор, каркасный дом (эксплуатация)':1 / 80,
        }

metadict_model['Сельское жильё, каркасный дом (строительство) (квадратный метр)'] = {
        'Сельский двор, каркасный дом (строительство)':1 / 80,
        }

metadict_model['Сельский двор, каркасный дом (эксплуатация)'] = {
        'Отделка одноэтажного дома':1,
        'Отделка дощатого амбара':1 / 5,
        #'Отделка шахтного колодца':1 / 10,
        '|-Усадьба (квадратный метр)':30 * 60,
        }

metadict_model['Сельский двор, каркасный дом (строительство)'] = {
        'Каркасный дом (смета)':1,
        'Дощатый амбар (смета)':1 / 5,
        #'Шахтный колодец (смета)':1 / 10,
        }

#----
# Сельский двор (североморский):

metadict_model['Сельское жильё, изба (квадратный метр)'] = {
        # Сельские дома обновляются раз в 30 лет:
        'Сельское жильё, изба (эксплуатация) (квадратный метр)':1,
        'Сельское жильё, изба (строительство) (квадратный метр)':1 / 30,
        }

metadict_model['Сельское жильё, изба (эксплуатация) (квадратный метр)'] = {
        'Сельский двор, изба (эксплуатация)':1 / 120,
        }

metadict_model['Сельское жильё, изба (строительство) (квадратный метр)'] = {
        'Сельский двор, изба (строительство)':1 / 120,
        }

metadict_model['Сельский двор, изба (эксплуатация)'] = {
        'Отделка хаты':1,
        'Отделка дощатого амбара':1 / 5,
        #'Отделка шахтного колодца':1 / 10,
        '|-Усадьба (квадратный метр)':30 * 60,
        }

metadict_model['Сельский двор, изба (строительство)'] = {
        # Типы дворовых усадеб и связей жилых и хозяйственных построек (19 век)
            # https://www.gumer.info/bibliotek_Buks/History/milov/01_9_clip_image006_0000.gif
            # https://www.gumer.info/bibliotek_Buks/History/milov/01_9_clip_image009.gif
        'Брусчатый дом (смета)':1,
        'Дощатая уборная (смета)':1,
        'Брусчатая баня (смета)':1 / 5,
        'Дощатый амбар (смета)':1 / 5,
        }

#----
# Сельский двор (южноморский):

metadict_model['Сельское жильё, хата (квадратный метр)'] = {
        'Сельское жильё, хата (эксплуатация) (квадратный метр)':1,
        'Сельское жильё, хата (строительство) (квадратный метр)':1 / 30,
        }

metadict_model['Сельское жильё, хата (эксплуатация) (квадратный метр)'] = {
        'Сельский двор, хата (эксплуатация)':1 / 120,
        }

metadict_model['Сельское жильё, хата (строительство) (квадратный метр)'] = {
        'Сельский двор, хата (строительство)':1 / 120,
        }

metadict_model['Сельский двор, хата (эксплуатация)'] = {
        'Отделка хаты':1,
        'Отделка дощатого амбара':1 / 5,
        #'Отделка шахтного колодца':1 / 10,
        '|-Усадьба (квадратный метр)':30 * 60,
        }

metadict_model['Сельский двор, хата (строительство)'] = {
        'Хата (смета)':1,
        'Дощатая уборная (смета)':1,
        'Брусчатая баня (смета)':1 / 5,
        'Дощатый амбар (смета)':1 / 5,
        }
