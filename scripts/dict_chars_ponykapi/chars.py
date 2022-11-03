# Карточки персонажей в стиле Fallout 2.

##----
# Герои

metadict_army['Персонажи'] = {
        'Джина':1,
        'Квинта':1,
        }

metadict_army['Джина'] = {
        # Джина-алугви
        'Trait (Jinxed)':1,
        'Trait (Small Frame)':1,
        'Джина (параметры)':1,
        'Джина (жизнь в Кладже)':1,
        }

metadict_army['Квинта'] = {
        # Квинта Сидни
        'Trait (Sex Appeal)':1,
        'Trait (Good Natured)':1,
        'Квинта (параметры)':1,
        'Квинта (жизнь в Кладже)':1,
        }

metadict_army['Кумо'] = {
        # Кумо-керети
        'Trait (Gifted)':1,
        'Кумо (параметры)':1,
        'Кумо (жизнь в Кладже)':1,
        }

metadict_army['Тето'] = {
        # Тето-арройо
        'Trait (Kamikaze)':1,
        'Trait (Fast Shot)':1,
        'Тето (параметры)':1,
        'Тето (жизнь в Кладже)':1,
        }

metadict_army['Арики'] = {
        # Арики-арройо
        'Trait (Skilled)':1,
        'Арики (параметры)':1,
        'Арики (жизнь в Кладже)':1,
        }

##----
# Характеристики, параметры:

metadict_army['Джина (параметры)'] = {
        'Базовые способности':1,
        'Strenght (сила)':6,
        'Perception (восприятие)':7,
        'Endurance (выносливость)':6,
        'Charisma (харизма)':3,
        'Intelligence (интеллект)':7,
        'Agility (ловкость)':9,
        'Luck (удача)':2,
        }

metadict_army['Квинта (параметры)'] = {
        'Базовые способности':1,
        'Strenght (сила)':6,
        'Perception (восприятие)':4,
        'Endurance (выносливость)':5,
        'Charisma (харизма)':9,
        'Intelligence (интеллект)':5,
        'Agility (ловкость)':7,
        'Luck (удача)':4,
        }

metadict_army['Кумо (параметры)'] = {
        'Базовые способности':1,
        'Strenght (сила)':4,
        'Perception (восприятие)':7,
        'Endurance (выносливость)':4,
        'Charisma (харизма)':5,
        'Intelligence (интеллект)':8,
        'Agility (ловкость)':7,
        'Luck (удача)':5,
        }

metadict_army['Тето (параметры)'] = {
        'Базовые способности':1,
        'Strenght (сила)':7,
        'Perception (восприятие)':5,
        'Endurance (выносливость)':7,
        'Charisma (харизма)':4,
        'Intelligence (интеллект)':5,
        'Agility (ловкость)':7,
        'Luck (удача)':5,
        }

metadict_army['Арики (параметры)'] = {
        'Базовые способности':1,
        'Strenght (сила)':5,
        'Perception (восприятие)':5,
        'Endurance (выносливость)':5,
        'Charisma (харизма)':5,
        'Intelligence (интеллект)':10,
        'Agility (ловкость)':5,
        'Luck (удача)':5,
        }

##----
# Характеристики --> навыки:

metadict_army['Базовые способности'] = {
        'Action Points':5,
        'Hit Points (base)':15,
        'Melee Damage':-5,
        'Skill (Small Guns)':5,
        'Skill (Unarmed)':30,
        'Skill (Melee Weapons)':20,
        'Skill (Doctor)':5,
        'Skill (Sneak)':5,
        'Skill (Lockpick)':10,
        'Skill (Traps)':10,
        'Skill (Science)':10,
        }

metadict_army['Strenght (сила)'] = {
        # hp: 15 + Strenght + (2 * Endurance)
        # Unarmed
        '-Strenght':1,
        'Hit Points (base)':1,
        # Жеребята маленькие, 15 футов/ед.силы
        #'--Weight-max (lbs)':25,
        '--Weight-max (lbs)':15,
        'Melee Damage':1,
        'Skill (Unarmed)':2,
        'Skill (Melee Weapons)':2,
        }

metadict_army['Perception (восприятие)'] = {
        # https://fallout.fandom.com/wiki/Sequence
        'Sequence':2,
        '-Perception':1,
        'Skill (First Aid)':2,
        'Skill (Doctor)':1,
        'Skill (Lockpick)':1,
        'Skill (Traps)':1,
        'Skill (Pilot)':2,
        }

metadict_army['Endurance (выносливость)'] = {
        '-Endurance':1,
        'Hit Points (base)':2,
        'Skill (Outdoorsman)':2,
        }

metadict_army['Charisma (харизма)'] = {
        '-Charisma':1,
        'Skill (Speech)':5,
        'Skill (Barter)':4,
        }

metadict_army['Intelligence (интеллект)'] = {
        '-Intelligence':1,
        'Skill (First Aid)':2,
        'Skill (Doctor)':1,
        'Skill (Science)':2,
        'Skill (Repair)':3,
        'Skill (Outdoorsman)':2,
        }

metadict_army['Agility (ловкость)'] = {
        '-Agility':1,
        'Action Points':1/2,
        'Skill (Small Guns)':4,
        'Skill (Big Guns)':2,
        'Skill (Energy Weapons)':2,
        'Skill (Unarmed)':2,
        'Skill (Melee Weapons)':2,
        'Skill (Throwing)':4,
        'Skill (Sneak)':3,
        'Skill (Lockpick)':1,
        'Skill (Steal)':3,
        'Skill (Traps)':1,
        'Skill (Pilot)':2,
        }

metadict_army['Luck (удача)'] = {
        '-Luck':1,
        'Critical Chance (%)':1,
        'Skill (Gambling)':5,
        }

##----
# Traits

metadict_army['Trait (Heavy Handed)'] = {
        # https://fallout.fandom.com/wiki/Fallout_2_traits
        'Melee Damage':+4,
        '-Trait (Heavy Handed)':1,
        }

metadict_army['Trait (Jinxed)'] = {
        # https://fallout.fandom.com/wiki/Jinxed
        '-Trait (Jinxed)':1,
        }

metadict_army['Trait (Small Frame)'] = {
        '-Trait (Small Frame)':1,
        'Agility (ловкость)':+1,
        }

metadict_army['Trait (Fast Shot)'] = {
        # All throwing and firearm attacks cost 1 less AP
        # Cannot aim attacks
        '-Trait (Fast Shot)':1,
        }

metadict_army['Trait (Kamikaze)'] = {
        'Sequence':+5,
        '-Trait (Kamikaze)':1,
        }

metadict_army['Trait (Sex Appeal)'] = {
        '-Trait (Sex Appeal)':1,
        }

metadict_army['Trait (Gifted)'] = {
        # https://fallout.fandom.com/wiki/Gifted
            # +1 to all seven stats
            # -10% to all skills
            # 5 less skill Points per level
        '-Trait (Gifted)':1,
        'Strenght (сила)':+1,
        'Perception (восприятие)':+1,
        'Endurance (выносливость)':+1,
        'Charisma (харизма)':+1,
        'Intelligence (интеллект)':+1,
        'Agility (ловкость)':+1,
        'Luck (удача)':+1,
        # -10% to all skills
        'Skill (Unarmed)':-10,
        'Skill (Melee Weapons)':-10,
        'Skill (First Aid)':-10,
        'Skill (Doctor)':-10,
        'Skill (Lockpick)':-10,
        'Skill (Traps)':-10,
        'Skill (Outdoorsman)':-10,
        'Skill (Speech)':-10,
        'Skill (Barter)':-10,
        'Skill (First Aid)':-10,
        'Skill (Doctor)':-10,
        'Skill (Science)':-10,
        'Skill (Repair)':-10,
        'Skill (Outdoorsman)':-10,
        'Skill (Small Guns)':-10,
        'Skill (Big Guns)':-10,
        'Skill (Energy Weapons)':-10,
        'Skill (Unarmed)':-10,
        'Skill (Melee Weapons)':-10,
        'Skill (Throwing)':-10,
        'Skill (Sneak)':-10,
        'Skill (Lockpick)':-10,
        'Skill (Steal)':-10,
        'Skill (Traps)':-10,
        'Skill (Gambling)':-10,
        }

metadict_army['Trait (Skilled)'] = {
        # +5 skill Points per level
        # +1 Perk rate
        '-Trait (Skilled)':1,
        }

metadict_army['Trait (Good Natured)'] = {
        # +15% to First Aid, Doctor, Speech, and Barter
        '-Trait (Good Natured)':1,
        'Skill (First Aid)':+15,
        'Skill (Doctor)':+15,
        'Skill (Speech)':+15,
        'Skill (Barter)':+15,
        # -10% to Big Guns, Small Guns, Energy Weapons, Throwing, Melee Weapons, and Unarmed
        'Skill (Big Guns)':-10,
        'Skill (Small Guns)':-10,
        'Skill (Energy Weapons)':-10,
        'Skill (Throwing)':-10,
        'Skill (Melee Weapons)':-10,
        'Skill (Unarmed)':-10,
        }

metadict_army['Trait (Small Frame)'] = {
        # +1 Agility
        # Carry Weight = 25 + (15 x your Strength)
        'Agility (ловкость)':+1,
        }

##----
# Perks

metadict_army['Perk (Healer)'] = {
        # PE 7, IN 5, AG 6, First Aid 40%
        # 4-10 more hit points healed when using First Aid or Doctor skills
        '-Perk (Healer)':1,
        }

metadict_army['Perk (Kama Sutra Master)'] = {
        '-Perk (Kama Sutra Master)':1,
        }

metadict_army['Perk (Thief)'] = {
        # +10% to skills: Sneak, Lockpick, Steal and Traps
        'Skill (Sneak)':+10,
        'Skill (Lockpick)':+10,
        'Skill (Steal)':+10,
        'Skill (Traps)':+10,
        '-Perk (Thief)':1,
        }

##----
# Упрощения:

metadict_army['Hit Points (base)'] = {
        '--HP':1,
        }

metadict_army['Hit Points (level)'] = {
        '--HP':1,
        }

##----
# Бонусы предметов:

metadict_army['Book (First Aid Book)'] = {
        # https://fallout.fandom.com/wiki/Fallout_2_skill_books
            # In Fallout 2, the amount of skill Points gained is equal to 100,
            # subtract the current skill level, divide by 10, and then rounded down.
            # Thus, the maximum a skill can increased by books is up to 91%. 
        '|Book (First Aid Book)':1,
        'Skill (First Aid)':10,
        '--Weight':2,
        }

metadict_army['Book (Big Book of Science)'] = {
        '|Book (Big Book of Science)':1,
        'Skill (Science)':10,
        '--Weight':5,
        }

metadict_army['Book (Dean\'s Electronics)'] = {
        '|Book (Dean\'s Electronics)':1,
        'Skill (Repair)':10,
        '--Weight':2,
        }

metadict_army['Book (Scout Handbook)'] = {
        '|Book (Scout Handbook)':1,
        'Skill (Outdoorsman)':10,
        '--Weight':3,
        }

metadict_army['Book (Guns and Bullets)'] = {
        '|Book (Guns and Bullets)':1,
        'Skill (Small Guns)':10,
        '--Weight':3,
        }

##----
# Бонусы предметов:

metadict_army['Item (First Aid Kit)'] = {
        '|Item (First Aid Kit) (usage)':3,
        'Skill (First Aid)':20,
        }

metadict_army['Item (Doctor\'s bag)'] = {
        '|Item (Doctor\'s bag) (usage)':3,
        'Skill (Doctor)':20,
        }

metadict_army['Item (Tool)'] = {
        '|Item (Tool)':1,
        'Skill (Repair)':20,
        }

metadict_army['Item (Lock picks)'] = {
        '|Item (Lock picks)':1,
        'Skill (Lockpick)':20,
        }

metadict_army['Item (Motion sensor)'] = {
        '|Item (Motion sensor)':1,
        'Skill (Outdoorsman)':20,
        }

metadict_army['Item (Assault rifle)'] = {
        '|Item (Assault rifle)':1,
        '--Weight':7,
        }

metadict_army['Item (10mm SMG)'] = {
        '|Item (10mm SMG)':1,
        '--Weight':5,
        }

metadict_army['Item (Laser rifle)'] = {
        '|Item (Laser rifle)':1,
        '--Weight':7,
        }

metadict_army['Item (Light support weapon)'] = {
        '|Item (Light support weapon)':1,
        '--Weight':20,
        }

metadict_army['Item (Combat armor)'] = {
        # https://fallout.fandom.com/wiki/Combat_armor_(Fallout)
        # https://fallout.fandom.com/wiki/Armor_Class
        '|Item (Combat armor)':1,
        '--Weight':20,
        }

metadict_army['Item (Spectacles)'] = {
        '|Item (Spectacles)':1,
        # Очки Квинты
        }

metadict_army['Item (Camera)'] = {
        '|Item (Camera)':1,
        # Фотик Джин
        }

##----
# Развитие персонажей:
# https://fallout.fandom.com/wiki/Level

##----
# Джина-алугви:

metadict_army['Джина (жизнь в Кладже)'] = {
        'Джина lvl 1':1,
        'Book (First Aid Book)':1,
        'Item (First Aid Kit)':1,
        'Item (Doctor\'s bag)':1,
        'Item (10mm SMG)':1,
        'Item (Camera)':1,
        }

##----
#

metadict_army['Джина lvl 1'] = {
        # Skill Points: 5 + INT x 2
        # Hit Points: 2 + END / 2
        #'Hit Points (level)':2 + 6/2,
        #'Skill Points':5 + 7*2,
        'Skill (Doctor)':20,
        'Skill (Sneak)':20,
        'Skill (Small Guns)':20,
        }

##----
# Квинта Сидни

metadict_army['Квинта (жизнь в Кладже)'] = {
        # https://fallout.fandom.com/wiki/Pilot
        'Квинта lvl 1':1,
        'Book (First Aid Book)':1,
        'Item (First Aid Kit)':1,
        'Item (Spectacles)':1,
        }

##----
#

metadict_army['Квинта lvl 1'] = {
        #'Hit Points (level)':2 + 5/2,
        #'Skill Points':5 + 5*2,
        'Skill (Speech)':20,
        'Skill (Barter)':20,
        'Skill (Pilot)':20,
        }

##----
# Кумо-керети

metadict_army['Кумо (жизнь в Кладже)'] = {
        # Помогал Ниру с радиостанцией.
        'Кумо lvl 1':1,
        'Book (Scout Handbook)':1,
        'Book (Guns and Bullets)':1,
        'Item (Assault rifle)':1,
        'Item (Lock picks)':1,
        }

##----
# 

metadict_army['Кумо lvl 1'] = {
        #'Hit Points (level)':2 + 5/2,
        #'Skill Points':9*2,
        'Skill (Outdoorsman)':20,
        'Skill (Lockpick)':20,
        'Skill (Small Guns)':20,
        }

##----
# Тето-арройо

metadict_army['Тето (жизнь в Кладже)'] = {
        'Тето lvl 1':1,
        'Item (Combat armor)':1,
        'Item (Light support weapon)':1,
        }

##----
# 

metadict_army['Тето lvl 1'] = {
        # https://fallout.fandom.com/wiki/Unarmed#Fallout_2_and_Fallout_Tactics
            # Крутые атаки даются только на 5-6 уровне, но пофиг, Джин больно пинается:
            # Hammer Punch
                # Unarmed 75%, Agility 6, Strength 5, level 6
                # +5 DMG, +5% crit
            # Jab
                # Unarmed 75%, Agility 7, Strength 5, level 5
                # +3 DMG, +10% crit
            # Snap Kick
                # Unarmed 60%, Agility 6, Level 6
                # +7 DMG
            # Hip Kick
                # Unarmed 60%, Agility 7, Strength 6, Level 6
                # +7 DMG
        #'Hit Points (level)':2 + 7/2,
        #'Skill Points':5 + 5*2,
        'Skill (Unarmed)':20,
        'Skill (Throwing)':20,
        'Skill (Big Guns)':20,
        }

##----
# Арики-арройо

metadict_army['Арики (жизнь в Кладже)'] = {
        'Арики lvl 1':1,
        'Book (Big Book of Science)':1,
        'Item (Laser rifle)':1,
        'Item (Tool)':1,
        }

##----
# 

metadict_army['Арики lvl 1'] = {
        #'Hit Points (level)':2 + 5/2,
        #'Skill Points':10 + 10*2,
        'Skill (Science)':20,
        'Skill (Repair)':20,
        'Skill (Energy Weapons)':20,
        }
