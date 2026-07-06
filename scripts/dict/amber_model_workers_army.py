#----
# DnD 5.5e FoE/EaW Urban Warfare:
    # Fallout: Equestria and Equestria at War
    # https://equestriaatwar.wiki.gg/wiki/List_of_Countries
    # https://equestriaatwar.wiki.gg/wiki/World_Map_and_Geography
    # https://equestriaatwar.wiki.gg/wiki/Timeline_of_World_History
    # https://equestriaatwar.wiki.gg/wiki/Equestrian_events
    # https://hoi4.paradoxwikis.com/Hearts_of_Iron_4_Wiki
    # https://www.moddb.com/mods/equestria-at-war
# Combined Arms:
    # Each Character have 1 specialized unit:
    # 1-2 lvl Party can hire 4 helpful gunners.
    # 3-4 lvl Party have Squad up to 4 fireteams.
    # 5-6 lvl Party have Platoon of 4 veteran squads.
    # 7-8 lvl Party have Platoon of 4 elite squads.
    # 9-10 lvl Party have Company of 4 elite platoons.
    # 11+ lvl National political power with SpecOps squads.
# Command and Control:
    # Command Actions = Proficiency Bonus per Short Rest.
    # Without Command Actions units can only defend themselves.
    # Battle Plan is a list of Command Actions on the Battlescape.
        # Party of 4 heroes 5 lvl with 4 squads vs castle garrison:
        # 1."Sapper_Squad, minefield to protect Cannon_Squad."
        # 2."Cannon_Squad, suppress the wall. 50 shells, 10min."
        # 3."Halftrack, take us with Assault_Squad to the gate."
        # 4."Assault_Squad, follow us inside and take captives."
        # 5."Sapper_Squad, prepare blast to cause an avalanche."
        # 6."Cannon_Squad, be ready to control Mountain pass."
        # 6/12 Command Actions used, 6/12 for surprises.
    # This format useful with LLM for simulation:
        # Generate list of possible enemy decisions.
        # Use d4-d20 roll to determine enemy decision:
        # 1) Garrison will prepare ambush inside.
        # 2) Garrison will call for reinforcement.
        # 3) Garrison will try to hold the walls.
        # 4) Garrison was not prepared for attack.
        # Generate firefights, dangers, occurrences.
        # Overall this is CYOA-mode for DnD games.
    # Consider to allow for 5+ lvl Party:
        # - Order for ally, locals, civilians per 2 Command.
        # - Animate_Dead without time limitation per 2 Command.
        # - Arcane_Robotics without concentration per 2 Command.
        # - Pegasi gliders for airdrop/bombardment per 2 Command.
        # - Artillery Support from 1-3 mile distance per 2 Command.

#----
# Soldiers and Lieutenants:
    # lvl | Soldier    | CR  | Exp   | Cost  | Commentary
    # --- | ---------- | --- | ----- | ----- | -----------------
    # 2   | Trooper    | 1/4 |  0    | ₡300  | 10hp, Proficiency
    # 3   | Corporal   | 1/2 | -1.2k | ₡600  | 20hp, Mastery
    # 4   | Sergeant   | 1   | -3.9k | ₡1200 | 30hp, Style
    # 5   | Lieutenant | 2   | +10.4 | ₡2400 | 40hp, Feat
    # Cost = equipment, you can equip unit with this money.
    # Exp = hero experience. +1 Lieutenant per 10k hero Exp.
    # Lieutenant can train up to 9 Corporals or 3 Sergeants.
    # Troopers can use only simple weapon and medium armor.
    # - Ordinary Squad -- 1 Sergeant and 9 Troopers.
    # - Veteran Squad -- 1 Lieutenant and 9 Corporals.
    # - Elite Squad -- 3 Lieutenants and 9 Sergeants.
    # - SpecOps Squad -- up to 12 Lieutenants.
# Squad creation:
    # Squad consists of 3-12 soldiers and leader:
    # - 1 squad per 30ft hexagon of battlescape.
    # - 2+ squads per 30ft hex with Disadvantage.
    # - Squad have 30ft range of Opportunity_Attack.
    # - Squad have AC of worst armor + worst Dmg mod.
    # - Squad have 50% hp and 50% combined Damage Rolls.
    # Soldier    | HP   | Attack | Dmg Rolls | Dmg mod
    # ---------- | ---- | ------ | --------- | -------
    # Trooper    | +5   | 1d20+2 | +0.5      | -
    # Corporal   | +10  | 1d20+3 | +0.5      | +1
    # Sergeant   | +15  | 1d20+4 | +0.5      | +2
    # Lieutenant | +20  | 1d20+5 | +1        | +3
# Weapon balanced by performance vs combat endurance:
    # Firearms: 1d6-1d12 rifles; 2d4 SMG; 3d6 LMG; 2d12 HMG.
    # 1 Damage Roll = 1 projectile for shrapnel and firearms.
    # Troopers are just spotters for squad's machine-gun.
    # Veteran Squad of corporals can use Weapon_Mastery.
    # Elite and SpecOps can use 2 attacks with 50% Dmg.
    # Crew will use heavy weapon instead of firearms.
    # Crew append vehicle hp to the Hit Points pool.
    # Crew have Damage Threshold (10-30 APC/tanks).
# Squad Hit Points represents combat endurance:
    # With 0hp squad incapacitated and suffer 1 Exhaustion.
    # Next -5hp means Trooper killed, -10hp Corporal killed.
    # Incapacitated squad can move, but cannot attack, react.
    # Incapacitated squad will be captured in any melee clash.
    # Squad with 0hp will lose their vehicle and heavy weapon.
    # Squad with killed soldiers need reinforcement long rest.
    # Otherwise they will regain Hit Points after short rest.
# Squads vulnerable to zonal attacks and melee:
    # R=10ft (10lb shell) --> ×2 damage, except 1/2 cover and prone.
    # R=20ft (≥50lb shell) --> ×2 damage, except 3/4 cover and prone.
    # Zonal spells (all) --> ×2 damage except 3/4 cover and Doge_Action.
    # Melee clash vs hero --> ×2 damage + Advantage (they are prone).
    # Squads can be dangerous, but much less tough than monsters.

#----
# Army structure:
    # Hero rank, loyal Lieutenants and squad, vassal Leaders and army funds:
    # lvl | Rank    | Exp/lvl | Exp sum | Ltn | Squad  | Vassl | Army | Full Cost
    # --- | ------- | ------- | ------- | --- | ------ | ----- | ---- | ---------
    # 1   | Rookie  |       0 |      0  | -   | 1Trpr  | -     | -    | ₡0.6+₡0.3
    # 2   | Lucky   |     300 |    300  | -   | 3T     | -     | -    | ₡1.2+₡0.9
    # 3   | Hero    |     900 |  1 200  | -   | 1C+3T  | -     | -    | ₡2.4+₡1.5
    # 4   | Hero    |   2 700 |  3 900  | -   | 3C+9T  | -     | -    | ₡3.6+₡4.5
    # 5   | Leader  |   6 500 | 10 000  | 1   | 9C     | -     | ≤30  | ₡12.6k
    # 6   | Leader  |  14 000 | 24 000  | 2   | 3S+9C  | -     | 30   | ₡21.6k
    # 7   | Captain |  23 000 | 47 000  | 4   | 12S    | 3     | 90   | ₡31+₡13×3
    # 8   | Captain |  34 000 | 81 000  | 8   | 4L+12S | 5     | 150  | ₡41+₡22×5
    # 9   | Major   |  48 000 | 129 000 | 12  | 3×4L   | 5×3   | 450  | ₡38+₡70×5
    # 10  | Major   |  64 000 | 193 000 | 19  | 2×8L   | 5×5   | 750  | ₡53+₡151×5
    # 11  | Colonel |  85 000 | 278 000 | 27  | 3×8L   | 5×5×3 | 2250 | ₡77+₡388×5
    # 12  | Colonel | 100 000 | 378 000 | 37  | 3×12L  | 5×5×5 | 3750 | ₡115+₡808×5
    # Promotions: Sergeant --> Lieutenant --> vassal Leader --> vassal Captain.
    # Tree of elite group will grow around leader, his friends, and downward.
    # Major 9 lvl can have 12 own Lieutenants and 5 Captains with 15 Leaders.
    # Major 9 lvl have squad of 3 SpecOps_Team and battalion of 450 troopers.
# Frontline and Assault:
    # Battalion Combat Width -- 1-2 mile in defense, 3000ft in offense.
    # - 8-16 howitzers support 1 Battalion in defense from 1-3 miles.
        # - Battalion have 15 mortars, 10 antitank and support cannons.
        # - 48 machine-guns/mile, 6-12 per trench in 3000×3000ft zone.
        # - 1000 antitank and 350 antipersonnel mines in 3000ft zone.
        # - Or 6000 various antipersonnel mines against Dread League.
        # Mines + LMGs and HMGs + Mortars + Cannons = basic defense.
    # - 100+ howitzers support 1 Battalion in offense from 1-3 miles.
        # - 24 guns to make 6/12 breaches in barbed wire and mines.
        # - 60-120 howitzers for suppression, 16-64 counter-battery.
        # - 6-12k shells allocated to suppress 100 enemy positions.
        # - Practically suppression = 30% wounded 5-10% killed.
        # Artillery should suppress 50% targets, Pegasi 25-50%.
        # - First 10 minutes to injure 5-10% unwary soldiers.
        # - Then 40 minutes to make breaches and clear mines.
        # - Then 60 minutes for suppression during assault.
        # - During suppression best time for dive bombers.
        # Infantry must follow shelling with speed 300ft/min.
        # - Infantry should stay mounted as long as possible.
        # - 96% fragments ≤2g ≤3.2kJ can't penetrate 5mm armor.
        # - 1 Motorized infantry loses vs 8 foot infantry loses.
        # - 5 assaults = 7 days of operation = 10% wounded.
        # https://hoi4.paradoxwikis.com/Combat_tactics
        # https://rkka.ru/analys/art/ch5.htm

#----
# Artillery and Air Force:
    # To suppress squad on 30ft hexagon you need 2 shells/minute and one gun.
    # Roll d20 (+1/shell) vs DC 15-30 to hit (depends on distance and weather).
    # Roll CHA Save DC 10+1/shell or target Frightened and have Dodge_Action.
    # Cost | Weight | Range | Support Source   | Shrapnel dmg   | 90% targets
    # ---- | ------ | ----- | ---------------- | -------------- | ---------------
    # ₡500 | 500lb  | 60mi  | Glider_Bomb      | 30ft 12d6 (42) | R=40ft 100kPa
    # ₡100 | 100lb  | 3mi   | Howitzer_Squad   | 20ft 8d6 (28)  | 72×39ft 2800ft²
    # ₡50  | 50lb   | 2mi   | Howitzer_Squad   | 20ft 4d6 (14)  | 60×26ft 1600ft²
    # ₡10  | 10lb   | 1mi   | Cannon_Squad     | 10ft 2d6 (7)   | 26×16ft 450ft²
    # Battery = 4 howitzers. Artillery Battalion = 3 Battery (60 shells/minute).
    # Indirect fire accuracy: ±30ft dispersion per 6000ft distance, 3mi R=90ft.
    # Artillery Statistic:
        # Year   | Shell | To wound     | To kill | lb/kill | Cost
        # ------ | ----- | ------------ | ------- | ------- | ------
        # 1914   | 50lb  | 3 shells     | 12.5    | 625     | ₡625
        # 1917   | 50lb  | 55           | 221     | 11.05k  | ₡11k
        # 1944   | 100lb | 46           | 156     | 15.6k   | ₡16k
        # 1970   | 50lb  | tank field   | 1100    | 55k     | ₡55K
        # 1970   | 100lb | tank field   | 750     | 75k     | ₡75K
        # 2024   | 100lb | 10 in fields | 70      | 7k      | ₡7K
        # 2024   | 100lb | 50 in trench | 350     | 35k     | ₡35k
        # 2024   | 100lb | tank field   | 100     | 10k     | ₡10k
        # 2024   | 100lb | tank shelter | 200     | 20k     | ₡20k
        # d20+10 | 50lb  | 0.5dmg/shell | 150     | 7.5k    | ₡7.5k
        # Practical shelling 10 minutes (less no damage, more no surprise).
        # In 1917 200-250lb shells/soldier per month = 7-9% wounded/month.
    # Artillery Economy:
        # 80 shells = cost of 1 howitzer = 20 days of frontline shelling.
        # 50lb shell = 20 man-hours + ₡13 steel + ₡7 TNT + logistics = ₡50
        # 50lb shell (73% case; 13% explosives; 5% gunpowder) = 200lb steel.
        # 70% steel into shells; 20% arms and ammo; 10% artillery and tanks.
        # In WW1 30% of all steel production was used to manufacture shells.
        # https://paul-atrydes.livejournal.com/108785.html
        # https://paul-atrydes.livejournal.com/108959.html
    # Artillery Physics:
        # Blast: (50lb × 13% × kcal/g) / sphere(20ft) = 13kPa (176dB shell-shock)
        # Fragments: (50lb × 73% × 70% / 1.5g) / sphere_sa(20ft) to m² = 17 frag/m²
        # 70% fragment mass is 1-2g 1300-1800m/s = 0.85-3.2kJ (like .223 bullets)
        # For prone position or 3/4 cover 17 frag/m² × 25% = 4d6 dmg
    # Shelling Simulation:
        # 100 squads × 65hp + Dodge_Action + 3/4 cover (+7 DEX Save vs DC 15):
        # - 12k shells (suppression) = 5k dmg, 25/100 >30hp; 70/100 >0hp; 80 KIA.
        # - 6k shells (not enough) = 2.5k dmg, 75/100 >30hp; 97/100 >0hp; 5 KIA.
        # - 6k shells (no cover) = 7.5k dmg, 17/100 >30hp; 43/100 >0hp; 300 KIA.
        # - 2k shells (no cover) = 2.5k dmg, 70/100 >30hp; 92/100 >0hp; 28 KIA.
        # - 2k shells (vehicle) = 1.0k dmg, 96/100 >30hp; 100/100 >0hp; 0 KIA.
        # Unlike Germany USSR created detached assault artillery divisions.
        # In 1943-1945 years 400 howitzers/mile for breakthrough was usual.
        # More howitzers --> more tasks at time --> less ammo expenditure.
        # First day 80-160 shells/gun, 2-7 days 40s/gun, total 320-400s/gun.
    # Air Force:
        # Bombers from 600ft altitude always hit, but 6+ LMGs will react.
        # Bombers from 2400ft±2° R=167ft 13% to hit Rolls like Artillery.
        # Bombers from 1-5mi R=1000ft 7% to hit can bomb industrial zones.
        # Familiar-guided bombs is combination of Find_Familiar + Glider.
        # Strategic Bombers can use them and tracers to guide the swarm.
        # AA-defense will counter this with familiar-guided missiles.

#----
# Magic Factor:
    # Magic items 1.2% GDP; Spells and components 6% GDP.
    # Funds: ₡600k for 12k shells; ₡1200k for 1k Battalion.
    # Battalion can use 10% or ₡200k for magic items and spells.
    # Rituals:
    # 1tier = ₡0.1 (Alarm, Unseen_Servant, ₡10 Find_Familiar)
    # 2tier = ₡0.15 (Gentle_Repose, Beast_Sense, Skywrite)
    # 3tier = ₡0.22 (Nondetection, Water_Walk, Phantom_Steed)
    # 4tier = ₡0.7 (₡250 Divination)
    # Spells:
    # 1tier = ₡1 (Mage_Armor, Silent_Image, Goodberry, Cure_Wounds)
    # 2tier = ₡1.5 (Darkness, See_Invisibility, Lesser_Restoration)
    # 3tier = ₡2.2 (Clairvoyance, Fly, Dispel_Magic, ₡300 Revivify)
    # 4tier = ₡7 (Major_Image, Arcane_Eye, Death_Ward, ₡100 Stoneskin)
    # Runes, magic items:
    # 1tier = ₡100 (Shield, Absorb_Elements, False_Life, Fog_Cloud, Hex)
    # 2tier = ₡500 (Rope_Trick, Gentle_Repose, Invisibility, Flaming_Sphere)
    # 3tier = ₡10k (Leomunds_Tiny_Hut, Kinetic_Dome, Animate_Dead, Fireball)
    # 4tier = ₡100k (Greater_Invisibility, Resilent_Sphere, Dimension_Door)
    # Crystallized_Spell:
    # 4tier = ₡125 (60) (limited by wizard 9lvl concentration up to 1 hour)
    # 5tier = ₡625 (20) (Seeming, Scrying, Geas, Passwall, Dawn, Cloudkill)
    # 6tier = ₡3125 (12) (Arcane_Gate, Move_Earth, Wind_Walk, Circle_of_Death)
    # 7tier = ₡16k (4) (Teleport, Etherealness, Mirage_Arcane, Project_Image)
    # 8tier = ₡78k (1) (Control_Weather, Mighty_Fortress, Earthquake, Tsunami)
    # + ₡130 to Teleport Crystallized_Spell from Capital city.
    # Mage-tech:
    # 2tier Arcane_Robotics = ₡1200 power armor with Piercing Resistance.
    # 3tier Arcane_Robotics = ₡2400 light power armor with ability to fly.
    # Arch-magic:
    # 8tier Arcane_Robotics = ₡78k CR 16 20AC 160hp 3Atk+10 4d10+5 (27)
    # 9tier = ₡600+ (1) (Gate, Foresight, Meteor_Swarm)

#----
# War Economy:
    # Currency and GDP:
        # 1007 ALB Equestria (₡300/capita) ≈ 1913 USA ($400/capita).
        # ₡1 EQB (equestrian bit) = 0.4 gp (DnD 5.5e) = 50 USD PPP (2024)
        # ₡1 EQB (equestrian bit) = 15g silver = 0.75g gold = 50lb wheat
        # ₡50 = yearly ration; ₡300 = GDP/pony; ₡900 = medial family income.
        # ₡1200/soldier = 60k USD/soldier like modern India, Brazil.
    # Tooth-to-tail ratio:
        # 1% infantry (WW1) = 3% military = 15% GDP, workforce, population.
        # 1% infantry (WW2) = 5% military = 25% GDP, workforce, population.
        # https://hoi4.paradoxwikis.com/Supply
        # https://hoi4.paradoxwikis.com/Production
        # https://www.globalmilitary.net/rankings/countries/budget-per-soldier/
    # Infantry Division structure (German infantry division 1939):
        # Support    | 1 Regiment  | 2 Regiment  | 3 Regiment  | 4 Regiment
        # ---------- | ----------- | ----------- | ----------- | ------------
        # Recon      | Infantry    | Infantry    | Infantry    | L. Artillery
        # Signal     | Infantry    | Infantry    | Infantry    | L. Artillery
        # Anti-Tank  | Infantry    | Infantry    | Infantry    | L. Artillery
        # Engineer   | Sup.Gun C.  | Sup.Gun C.  | Sup.Gun C.  | M. Artillery
        # Logistics  | Antitank C. | Antitank C. | Antitank C. | -
        # 17.2k soldiers, 527 LMGs, 136 HMGs, 135 mortars, 60 guns, 48 howitzers.
        # ₡15M soldiers (50% reinforcements); 20k lb/day munition, ₡7.2M yearly.
        # - In 1915 France 68 rifles per LMG; Germany 111; Russia 174.
        # - In 1916 France 18 rifles per LMG; Germany 56; Russia 118.
        # - In 1915 -- 15% wounds artillery; 85% LMGs, rifles and grenades.
        # - In 1917 -- 70% wounds artillery; 20% LMGs; 10% rifles, grenades.
        # - ×50 increased division firepower because of artillery regiment.
        # - ×3 increased battalion firepower because of machine-guns.
        # https://hoi4.paradoxwikis.com/Division_template
        # https://www.generalstaff.org/NAF/Pt_I_1939-1940/939gxid.pdf
        # https://web.archive.org/web/http://www.wwiidaybyday.com/kstn/kstnmain.htm
    # Equestria (50M, 249k military):
        # 50M Equestria: ₡12 billion × 1% to billion $ = 6 billion USD
        # The Equestrian Army: ₡12 billion × 1% / ₡1200 = 100k soldiers
        # The Equestrian Navy: ₡12 billion × 0.8% / ₡1200 = 80k soldiers
        # Divisions           | №  | Battalions        | Readiness
        # ------------------- | -- | ----------------- | ---------
        # Royal Guard         | 7  | 3 inf+rec+mp      | useless
        # Garrison Regiment   | 9  | 4 inf             | useless
        # Onhooves Division   | 2  | 7 inf+eng         | 20%
        # Pegasi Division     | 1  | 8 airborne        | 30%
        # Royal Armour        | 2  | 3 tank, 4 minf    | 40%,50%
        # Total 100k military
        # https://equestriaatwar.wiki.gg/wiki/Equestria#Starting_Situation
    # Changeling Lands (37M, 456k military):
        # Divisions           | №  | Battalions        | Readiness
        # ------------------- | -- | ----------------- | ---------
        # Infanterie Division | 7  | 7 inf+art+rec+eng | -
        # Queen's Guard       | 1  | 4 inf+art+rec+eng | -
        # Jager Division      | 4  | 7 inf+art+rec+eng | -
        # Grenzinfanterie     | 5  | 4 infantry        | -
        # Panzer Division     | 3  | 3 tank, 4 minf    | -
        # Motorisierte Inf    | 5  | 8 minf+art+rec+en | -
        # Total 190k military
        # https://equestriaatwar.wiki.gg/wiki/Changeling_Lands#Military
    # Griffonian Empire (6/28M, 37k military):
        # Divisions           | №  | Battalions        | Readiness
        # ------------------- | -- | ----------------- | ---------
        # Imperial guard      | 11 | 6 inf+art+eng     | -
        # Imperial knights    | 2  | 6 air+rec         | -
        # Panzer division     | 1  | 3 tank, 2 minf    | -
        # Panzergrenadier     | 1  | 3 tank, 2 minf    | changelings

#----
# Units Lorebook for LLM:
    # Interface block for each LLM post looks like this:
    # ```
    # Squads: Assault_Squad, Halftrack, Cannon_Squad.
    # Enemy: Animated_Dead_Team, Gluba (Animated Hill GIant).
    # ```
    # Lorebook entities will be loaded from this names.
    # Details about hp, attacks, behaviour will be used.
    # Also Gemini knows monsters from MM and dndwiki.

#----
# CR 1/8 - CR 2 for 1-2 lvl Party:
# <infantry_team>
    # Unit_Cost: ₡1500
    # Infantry_Team: CR 1/2 (25hp, 12AC, 1Atk+3, Hit: 8 (2d6+1) DPR 2-5)
    # From: Infantry Battalion, Garrison Regiment
    # Personnel: Corporal, 3 troopers
    # Personality: ESFP + Gullible + Awkward
    # Behavior:
    # - Fireteam: Will move together from cover to cover.
    # - Rookies: Can make stupid mistakes during real fight.
    # Weapon:
    # - 7.92mm Kar98k 9lb 6MOA 150/600ft±1ft -- ₡20 (55 RM, 22 man-hours)
    # - 7.92×57mm ammo 3.5kJ 15r/lb -- ₡15 per 1000 rounds (15 man-hours)
    # Armor:
    # - Uniform and helmets (11AC).
    # https://grokipedia.com/page/Gewehr_98
    # https://grokipedia.com/page/Karabiner_98k
    # https://grokipedia.com/page/7.92×57mm_Mauser
    # https://equestriaatwar.wiki.gg/wiki/Infantry_technology
# </infantry_team>
# <animated_dead_team>
    # Unit_Cost: ₡1000
    # Animated_Dead_Team: CR 1 (25hp, 14AC, 1Atk+3, Hit: 11 (2d6+4) DPR 3-7)
    # From: Infantry Battalion, Crumbling Dead division, Dread League.
    # Personnel: 4 skeleton/zombies (quadrupedal equines or griffins)
    # Personality: Yandere + Meek + Traumatized
    # Features:
    # - Undead: Hated and considering prohibited weapon in most cases.
    # Behavior:
    # - Forgetful: Can perform simple orders, but no more than 1 hour.
    # - Untrustworthy: Without constant control can attack ally units.
    # Special Attacks:
    # - Suicide bombers: If defeated in melee, R=20ft Hit: 14 (4d6)
    # Weapon:
    # - Melee weapon, usually spears.
    # - 4 × 50lb shrapnel charges -- ₡200
    # - Animate_Dead: 4 corpses × 60 days × ₡2.2/day = ₡528
    # Armor:
    # - Helmets and shields (13AC).
    # https://equestriaatwar.wiki.gg/wiki/Dread_League
# </animated_dead_team>
# <antitank_rifle_team>
    # Unit_Cost: ₡1800
    # Antitank_Rifle_Team CR 1 (25hp, 12AC, 1Atk+6 Hit: 14 (2d10+3) DPR 4-8)
    # From: Infantry Battalion, Garrison Regiment.
    # Personnel: Sergeant, Corporal
    # Personality: ISTJ + Dedicated + Timorous
    # Behavior:
    # - Ambushers: Prefer hidden positions and oblique fire.
    # - Slow movement: Cannot use anti-tank rifle during movement.
    # - Slow aiming: No reaction fire, anti-tank rifle to heavy and long.
    # Attack Effects:
    # - Armor Piercing: Ignores piercing Resistance.
    # - Anti-Cover: Pierces walls easily, ignores 3/4 cover.
    # - Tripod: Can shoot from prone position without Disadvantage.
    # - Precision: Sergeant knows weapon perfectly (+2 Attack)
    # - Vex: If shoot hit next attack have Advantage.
    # Weapon:
    # - 14.5mm PTRS-41 50lb 6MOA 150/1200ft±1ft -- ₡300 (200-300 man-hours)
    # - 14.5×114mm ammo 32kJ 1r/lb -- ₡1 per round
    # Armor:
    # - Uniform and helmets (11AC).
    # https://grokipedia.com/page/PTRS-41
    # https://grokipedia.com/page/14.5×114mm
# </antitank_rifle_team>
# <machinegun_team>
    # Unit_Cost: ₡1500
    # Machinegun_Team CR 1 (25hp, 12AC, 1Atk+3, Hit: 13 (3d6+1) DPR 4-7)
    # From: Infantry Battalion, Garrison Regiment
    # Personnel: Corporal, 3 Troopers.
    # Personality: ENFJ + Trigger happy + Moody
    # Attack Effects:
    # - Suppression: 30ft hexagon (CHA Save DC 10 or Dodge_Action)
    # - Anti-Air: Can pin down winged units (Pegasi, Griffins, etc)
    # - Topple: If attack hit CON Save or fall Prone.
    # Special Attacks:
    # - Suppressive Fire: 150 r/min, 3000ft 12MOA R=10ft Hit: 4 (1d6)
    # Weapon:
    # - 7.62mm Maxim gun 150lb 5MOA 180/720ft±1ft -- ₡700 (700 man-hours)
    # - 7.62x54mmR ammo 3.5kJ 15r/lb -- ₡15 per 1000 rounds (15 man-hours)
    # Armor:
    # - Uniform and helmets (11AC).
    # https://grokipedia.com/page/Maxim_gun
    # http://militera.lib.ru/science/merkatz_f/index.html
# </machinegun_team>
# <lmg_team>
    # Unit_Cost: ₡2400
    # LMG_Team: CR 2 (35hp, 14AC, 1Atk+4, Hit: 13 (3d6+2) DPR 4-8)
    # From: Infantry Battalion, Royal Guard division.
    # Personnel: Sergeant, corporal, 2 troopers
    # Personality: ESFJ + Cheeky + Sly
    # Behavior:
    # - Flanking fire: Prefer reaction oblique fire at moving targets.
    # - Entrenchment: Will use any resources around to fortify position.
    # Attack Effects:
    # - Suppression: 30ft hexagon (CHA Save DC 10 or Dodge_Action)
    # - Anti-Air: Can pin down winged units (Pegasi, Griffins, etc)
    # - Tripod: Can shoot from prone position without Disadvantage.
    # - Topple: If attack hit CON Save or fall Prone.
    # Special Attacks:
    # - Suppressive Fire: 120 r/min, 3000ft 12MOA R=10ft Hit: 4 (1d6)
    # - 1 rune Targeting_Ray (Sergeant): Aiming in smoke/fog/night.
    # Reactions:
    # - Burst: If unnoticed can attack with Advantage.
    # Weapon:
    # - 7.92mm MG34 70lb 3MOA 300/1200ft±1ft -- ₡100 (312 RM, 100-150 man-hours)
    # - 7.92×57mm ammo 3.5kJ 15r/lb -- ₡15 per 1000 rounds (15 man-hours)
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
    # https://grokipedia.com/page/MG_34
# </lmg_team>
# <hmg_team>
    # Unit_Cost: ₡3000 (₡600 heavy machine-gun)
    # HMG_Team: CR 2 (35hp, 14AC, 1Atk+4, Hit: 15 (2d12+2) DPR 5-9)
    # From: Infantry Battalion, Royal Armour division.
    # Personnel: Sergeant, 1 corporal, 2 troopers.
    # Personality: ISTP + Prudent + Importunate
    # Behavior:
    # - Anti-Armor bursts: Prefer oblique fire at armored targets.
    # - Slow movement: Cannot use heavy machine-gun during movement.
    # Attack Effects:
    # - Suppression: 30ft hexagon (CHA Save DC 10 or Dodge_Action)
    # - Armor Piercing: Ignores piercing Resistance.
    # - Anti-Cover: Can pierce brick walls, ignores 3/4 cover.
    # - Tripod: Can shoot from prone position without Disadvantage.
    # - Vex: If shoot hit next attack have Advantage.
    # Special Attacks:
    # - Suppressive Fire: 120 r/min, 3000ft 12MOA R=10ft Hit: 7 (1d12)
    # - 1 rune Targeting_Ray (Sergeant): Aiming in smoke/fog/night.
    # Weapon:
    # - 12.7mm DShK 350lb 1.5MOA 600/2400ft±1ft -- ₡600 (300-600 man-hours)
    # - 12.7×108mm ammo 16kJ 2r/lb -- ₡500 per 1000 rounds
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
    # https://grokipedia.com/page/DShK
    # https://grokipedia.com/page/12.7×108mm
# </hmg_team>
# <earthpony_veteran_team>
    # Unit_Cost: ₡3000
    # Earthpony_Veteran_Team: CR 2 (45hp, 15AC, 1Atk+4, Hit: 13 (3d6+2) DPR 4-8)
    # From: Equestrian Infantry Battalion, Onhooves division.
    # Personnel: Sergeant, 3 Corporals.
    # Personality: ESTJ + Stubborn + Caring
    # Behavior:
    # - Geomanty: Can make trench in minute by using runes of Mold_Earth.
    # - Sluggish: Prefer to keep position, even if movement is better.
    # Physique:
    # - Ponies have hooves instead of hands and fingers.
    # - Ponies use mouth to hold weapon and interacts with objects.
    # Attack Effects:
    # - Suppression: 30ft hexagon (CHA Save DC 10 or Dodge_Action)
    # - Anti-Air: Can pin down winged units (Pegasi, Griffins, etc)
    # - Tripod: Can shoot from prone position without Disadvantage.
    # - Topple: If attack hit CON Save or fall Prone.
    # Special Attacks:
    # - Rifle Grenades: 150ft R=10ft DEX Save, Hit: 7 (2d6) DPR 7
    # - Suppressive Fire: 120 r/min, 3000ft 12MOA R=10ft Hit: 4 (1d6)
    # - 1 rune Targeting_Ray (Sergeant): Aiming in smoke/fog/night.
    # Reactions:
    # - 1 rune Absorb_Elements (50% less damage from one zonal spell).
    # Weapon:
    # - 7.92mm MG34 70lb 3MOA 300/1200ft±1ft -- ₡85 (312 RM, 100 man-hours)
    # - 7.92×57mm ammo 3.5kJ 15r/lb -- ₡15 per 1000 rounds (15 man-hours)
    # - Gewehr-Sprenggranate 2r/lb -- ₡2 per lb
    # Armor:
    # - Breastplates (14AC), rarely Half Plate (15AC).
    # https://grokipedia.com/page/Schiessbecher
# </earthpony_veteran_team>
# <pegasi_veteran_team>
    # Unit_Cost: ₡3000
    # Pegasi_Veteran_Team: CR 2 (45hp, 15AC, 1Atk+4, Hit: 15 (4d4+5) DPR 5-9)
    # From: Equestrian Airborne Battalion, Pegasi division.
    # Personnel: Sergeant, 3 Corporals.
    # Personality: ESTP + Boastful + Impatient
    # Behavior:
    # - Commando: Prefer fast approaching, attack and rapid retreat.
    # Physique:
    # - Pegasi can soar up to 3000 altitude with their wind control magic.
    # - Pegasi can use their wings to deftly grab items and throw grenades.
    # Special Movement:
    # - Dash: Action to fly 120ft, land and take nearest cover.
    # Special Attacks:
    # - Gust Guided Grenades: 120ft R=10ft DEX Save, Hit: 7 (2d6) DPR 7
    # Weapon:
    # - 80 × M39 grenades -- ₡160
    # - 9mm MP40 9lb 12MOA 60/300ft±1ft -- ₡20 (57 RM, 18 man-hours)
    # - 9×19mm ammo 0.45kJ 35r/lb -- ₡10 per 1000 rounds (10.3-13 man-hours)
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
    # https://grokipedia.com/page/MP_40
    # https://grokipedia.com/page/9×19mm_Parabellum
# </pegasi_veteran_team>
# <unicorn_veteran_team>
    # Unit_Cost: ₡3000
    # Unicorn_Veteran_Team: CR 2 (45hp, 14AC, 1Atk+4, Hit: 15 (4d4+5) DPR 5-9)
    # From: Equestrian Infantry Battalion, Royal Guard division.
    # Personnel: Sergeant, 3 Corporals.
    # Personality: ISTJ + Naive + Bookish
    # Behavior:
    # - Grenadiers: Telekinetic guided grenades can reach any position.
    # Physique:
    # - Unicorns horn glows when they use telekinesis to hold weapon.
    # Special Attacks:
    # - Telekinetic Guided Grenades: 120ft R=10ft DEX Save, Hit: 7 (2d6) DPR 7
    # - 1 rune Magic_Missile (Sergeant): 120ft 3Atk Hit: 11 (1d4+1) DPR 11
    # Reactions:
    # - 1 rune Shield: +5 AC against bullets for few seconds.
    # Weapon:
    # - 80 × M39 grenades -- ₡160
    # - 9mm MP40 9lb 12MOA 60/300ft±1ft -- ₡20 (57 RM, 18 man-hours)
    # - 9×19mm ammo 0.45kJ 35r/lb -- ₡10 per 1000 rounds (10.3-13 man-hours)
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
    # https://grokipedia.com/page/Model_39_grenade
# </unicorn_veteran_team>
# <mortar_team>
    # Unit_Cost: ₡2700 (₡900 mortar and ammo)
    # Mortar_Team CR 1 (30hp, 12AC, 1Atk R=10ft Hit: 7 (2d6) DPR 7)
    # From: Infantry Battalion, Onhooves division
    # Personnel: Corporal, 4 troopers
    # Personality: ISFJ + Playful + Emotional
    # Behavior:
    # - Support Artillery: Will follow infantry to destroy obstacles.
    # Attack Effects:
    # - Demolition: ×2 damage against cover (trenches, walls, buildings).
    # - Suppression: 30ft hexagon (CHA Save DC 15 or Dodge_Action).
    # Special Attacks:
    # - Indirect Fire: 3000ft, d20+1/shell vs DC 15 to hit.
    # Weapon:
    # - 82mm Granatwerfer 34 130lb -- ₡300 (810 RM, 200-300 man-hours)
    # - 60 shells × 82mm HE 10lb = ₡600 (10 man-hours/shell)
    # Armor:
    # - Uniform and helmets (11AC).
# </mortar_team>
# <pegasi_dive_bombers>
    # Unit_Cost: ₡1700 (₡200 bombs)
    # Pegasi_Dive_Bombers: CR 2 (25hp, 14AC, 1Atk R=20ft Hit: 14 (4d6) DPR 14)
    # From: Pegasi Bombers Squadron, Equestrian Air Force.
    # Personnel: Corporal, 3 Troopers.
    # Personality: INFP + Timid + Observant
    # Behavior:
    # - Whirligig: Will circling above target and dive to 600ft altitude.
    # - Flyby Retreat: If under anti-air fire will fly away at low altitude.
    # Physique:
    # - Pegasi can soar up to 3000 altitude with their wind control magic.
    # Attack Effects:
    # - Demolition: ×2 damage against cover (trenches, walls, buildings).
    # - Suppression: 30ft hexagon (CHA Save DC 15 or Dodge_Action).
    # Weapon:
    # - 4 × 50lb Bombs = ₡200
    # - 9mm MP40 9lb 12MOA 60/300ft±1ft -- ₡20 (57 RM, 18 man-hours)
    # - 9×19mm ammo 0.45kJ 35r/lb -- ₡10 per 1000 rounds (10.3-13 man-hours)
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
# </pegasi_dive_bombers>

#----
# CR 3-4 for 3-4 lvl Party:
# <infantry_squad>
    # Unit_Cost: ₡4200
    # Infantry_Squad CR 3 (65hp, 14AC, 1Atk+4 Hit: 18 (4d6+4) DPR 5-11)
    # From: Infantry Battalion, Royal Guard division
    # Personnel: Sergeant, 2 Corporals, 6 Troopers
    # Personality: INFP + Childish + Coy
    # Behavior:
    # - Spotters: In offense half of squad will recon to aim machine-gun.
    # - Fire plan: In defense each soldier know position to cover others.
    # Attack Effects:
    # - Suppression: 30ft hexagon (CHA Save DC 10 or Dodge_Action)
    # - Anti-Air: Can pin down winged units (Pegasi, Griffins, etc)
    # - Tripod: Can shoot from prone position without Disadvantage.
    # - Topple: If attack hit CON Save or fall Prone.
    # Special Attacks:
    # - Rifle Grenades: 150ft R=10ft DEX Save, Hit: 7 (2d6) DPR 7
    # - Suppressive Fire: 120 r/min, 3000ft 12MOA R=10ft Hit: 4 (1d6)
    # - 1 rune Targeting_Ray (Sergeant): Aiming in smoke/fog/night.
    # Reactions:
    # - Cover fire: If squad attacked, machine-gun will suppress the threat.
    # Weapon:
    # - 7.92mm MG34 70lb 3MOA 300/1200ft±1ft -- ₡100 (312 RM, 100-150 man-hours)
    # - 7.92mm Kar98k 9lb 6MOA 150/600ft±1ft -- ₡20 (55 RM, 22 man-hours)
    # - 7.92×57mm ammo 3.5kJ 15r/lb -- ₡15 per 1000 rounds (15 man-hours)
    # - Gewehr-Sprenggranate 2r/lb -- ₡2 per lb
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
# </infantry_squad>
# <sapper_squad>
    # Unit_Cost: ₡4000 (₡1000 explosives)
    # Sapper_Squad CR 3 (45hp, 14AC, 1Atk+4, Hit: 12 (2d6+5) DPR 4-7)
    # From: Equestrian Engineer Company, Onhooves division.
    # Personnel: Sergeant, 3 Corporals.
    # Personality: INTP + Autistic + Touchy
    # Behavior:
    # - Combat Engineers: Will flavor any task with explosives.
    # Special Attacks:
    # - Blast Charge: 100lb ×2 damage to buildings, R=20ft Hit: 28 (8d6)
    # - Antipersonnel Mines: 1 hour per 300×300ft, 1lb/ft, Hit: 14 (4d6)
    # - Antitank Minefield: 1 hour per 300×60ft, 2lb/ft, Hit: 28 (8d6)
    # - Flamethrower: Effective clear minefields, 30ft cone Hit: 7 (2d6)
    # Weapon:
    # - 1000lb explosives on 2 carts = ₡1000
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
    # https://hoi4.paradoxwikis.com/Support_companies#Engineers_(ENG)
    # https://web.archive.org/web/20211129055945/http://saper.isnet.ru/mines-3/prm.html
    # https://web.archive.org/web/20220705185533/http://saper.isnet.ru/mines-2/tmd-40-1.html
# </sapper_squad>
# <signal_squad>
    # Unit_Cost: ₡4000 (₡1000 artillery support)
    # Signal_Squad CR 3 (45hp, 14AC, 1Atk+4, Hit: 12 (2d6+5) DPR 4-7)
    # From: Signal Company, Garrison Regiment.
    # Personnel: Sergeant, 3 Corporals.
    # Personality: ENTP + Sassy + Risible
    # Behavior:
    # - Spotter: Can aim indirect artillery fire from 1-3 miles.
    # - Wary: Should avoid firefights, if battery can support.
    # Special Attacks:
    # - Indirect Fire: 1-2 mile, d20+1/shell vs DC 15-30 to hit, R=20ft Hit: 14 (4d6)
    # - 1 rune Targeting_Ray (Sergeant): Aiming in smoke/fog/night.
    # Artillery Fire Effects:
    # - Demolition: ×2 damage against cover (trenches, walls, buildings).
    # - Suppression: 30ft hexagon (CHA Save DC 15 or Dodge_Action).
    # Weapon:
    # - 20 shells/minute × 50lb shell = ₡1000/minute
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
    # https://hoi4.paradoxwikis.com/Support_companies#Signal_(SIG)
# </signal_squad>
# <anti_air_squad>
    # Unit_Cost: ₡6000 (₡3000 turret with HMG)
    # Anti_Air_Squad CR 3 (75hp, 14AC, 1Atk+7 Hit: 16 (2d12+3) DPR 5-10)
    # From: Anti-Air Company, Royal Armour division.
    # Personnel: Sergeant, 3 Corporals.
    # Personality: ISFP + Lazy + Bonhomous
    # Behavior:
    # - Anti-Suppression: Robotic turret cannot be frightened.
    # - Quick Reaction: Turret always alert with Earthbind ready.
    # Attack Effects:
    # - Anti-Air: Can pin down winged units (Pegasi, Griffins, etc)
    # - Topple: If attack hit CON Save or fall Prone.
    # Reactions:
    # - 4 rune Earthbind: 2400ft, STR Save, Hit: 21 (6d6) by rough landing.
    # - 1 rune Absorb_Elements: 50% less damage from one zonal spell.
    # Weapon:
    # - Uncommon 3tier Arcane_Robotics turret 500lb -- ₡2400
    # - 12.7mm DShK 350lb 1.5MOA 600/2400ft±1ft -- ₡600 (300-600 man-hours)
    # - 12.7×108mm ammo 16kJ 2r/lb -- ₡500 per 1000 rounds
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
# </anti_air_squad>
# <medevac_squad>
    # Unit_Cost: ₡6000
    # Medevac_Squad CR 3 (75hp, 14AC, 1Atk+6 Hit: 20 (3d6+9) DPR 9-13)
    # From: Field Hospital, Royal Guard division.
    # Personnel: Lieutenant, Sergeant, 4 Corporals.
    # Personality: Kudere + Gloomy humor + Prodigy
    # Behavior:
    # - Medical Evacuation: Will evacuate wounded by Floating Disks to Lieutenant.
    # - Kind: Will use weapon only to defend wounded and treat enemy wounded too.
    # Features:
    # - Healer (Lieutenant): Can heal 8 (1d8+3) per minute by 1 Hit Point Dice.
    # - Ministry of Peace: Usually enemy don't shoot at them without a reason.
    # Special Movement:
    # - 8 rune Floating Disk: 500lb load, 3ft above surface, magnetic levitation.
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
# </medevac_squad>
# <unicorn_mage_squad>
    # Unit_Cost: ₡6000
    # Unicorn_Mage_Squad CR 3 (65hp, 15AC, 1Atk+6 Hit: 20 (2d10+9) DPR 9-13)
    # From: Equestrian Mage Company, Royal Guard division.
    # Personnel: Lieutenant, 3 Sergeants
    # Personality: Himedere + Arrogant + Witty
    # Behavior:
    # - Magicians: Prefer offensive cantrips rather than weapon.
    # - Limited Focus: Cannot use Shielding and Cantrips at same time.
    # Physique:
    # - Unicorns horn shines when they use cantrips and spells.
    # Features:
    # - Enchanter (Lieutenant): Can recharge 1 rune during long rest.
    # - Utility Cantrips: Light, Message, Mending, Prestidigitation, etc.
    # Defense:
    # - Arcane Shielding: Damage reduction 10 (4d4) during Dodge_Action.
    # Attacks:
    # - Offensive Cantrips: Fire_Bolt, Ray_of_Frost, Eldritch_Blast, etc.
    # Special Attacks:
    # - 1×4 runes Magic_Missile: 120ft 3Atk 4d4+4 (42) DPR 42
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
    # https://equestriaatwar.wiki.gg/wiki/Horse#Racial_Technology
# </unicorn_mage_squad>
# <antitank_cannon_squad>
    # Unit_Cost: ₡5200 (₡2200 anti-tank cannon and ammo)
    # Antitank_Cannon_Squad CR 3 (45hp, 14AC, 1Atk+6 Hit: 24 (4d10+2) DPR 7-14)
    # From: Support Anti-Tank Company, Royal Guard division
    # Personnel: Sergeant, Corporal, 4 troopers
    # Personality: INFJ + Kind + Cunning
    # Behavior:
    # - Ambushers: Prefer hidden positions and flanking shots.
    # - Slow movement: Cannot attack during movement. No Dash_Action.
    # Attack Effects:
    # - Armor Piercing: Ignores piercing Resistance.
    # - Anti-Cover: Pierces walls easily, ignores 3/4 cover.
    # - Precision: Sergeant knows weapon perfectly (+2 Attack)
    # - Vex: If shoot hit next attack have Advantage.
    # Weapon:
    # - 37mm Pak 36 0.5t 1MOA 1200/3600ft±1ft -- ₡1600 (5.73k RM, 0.9k man-hours)
    # - 120 shells × 37×249mmR AP 190kJ 2lb -- ₡600 (5 man-hours/shell)
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
    # - Gun shield: Frontal protection against bullets (3/4 cover +5AC)
    # https://grokipedia.com/page/3.7_cm_Pak_36
    # https://grokipedia.com/page/Panzerjäger
# </antitank_cannon_squad>
# <cannon_squad>
    # Unit_Cost: ₡5600 (₡2600 infantry support gun and ammo)
    # Cannon_Squad CR 4 (45hp, 14AC, 1Atk+6 Hit: 46 (8d10+2) DPR 7-14)
    # From: Support Artillery Company, Onhooves division
    # Personnel: Sergeant, Corporal, 4 Troopers.
    # Personality: ENTJ + Hot-tempered + Destructive Curious
    # Behavior:
    # - Support Artillery: Will follow infantry to destroy obstacles.
    # - Slow rate of fire: Crew need 2 rounds to reload gun and aim.
    # - Slow movement: Cannot attack during movement. No Dash_Action.
    # Attack Effects:
    # - HEAT shell: Damage inside cover/vehicle R=10ft Hit: 7 (2d6)
    # - Demolition: ×2 damage against cover (trenches, walls, buildings).
    # - Suppression: 30ft hexagon (CHA Save DC 15 or Dodge_Action).
    # - Precision: Sergeant knows weapon perfectly (+2 Attack)
    # Special Attacks:
    # - Indirect Fire: ≤1 mile, d20+1/shell vs DC 15-30 to hit, R=10ft Hit: 7 (2d6)
    # Weapon:
    # - 76mm M1927 0.8t 1MOA 1200/3600ft±1ft -- ₡1600-2400 (0.8-1.2k man-hours)
    # - 60 shells × 76mm HEAT 2.5MJ 10lb -- ₡600 (10 man-hours/shell)
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
    # - Gun shield: Frontal protection against bullets (3/4 cover +5AC)
# </cannon_squad>
# <glider_bomb>
    # Unit_Cost: ₡4700 (₡500 Glider Bomb 10hp)
    # Glider_Bomb CR 3 (10hp, 14AC, 1Atk R=30ft Hit: 42 (12d6))
    # From: Pegasi Bombers Squadron, Equestrian Air Force.
    # Personnel: Sergeant, Corporal, 8 Troopers
    # Personality: Bakadere + Genki + Derpy
    # Physique:
    # - Pegasi can lift glider up to 3000ft and accelerate to 60mph.
    # Behavior:
    # - Carriers: Pegasi will release Glider Bomb in 1-3mi range and retreat.
    # - Familiar-guided bomb: Tiny animal spirit will guide glider to target.
    # - Slow flight: Glider Bomb is fragile and vulnerable to machine-guns.
    # Weapon:
    # - 500lb Glider Bomb 250lb TNT -- ₡500
    # https://grokipedia.com/page/Circular_error_probable
    # https://grokipedia.com/page/Unguided_bomb
    # https://grokipedia.com/page/Guided_bomb
# <glider_bomb>
# <halftrack>
    # Unit_Cost: ₡8100 (₡6300 half-track 80hp)
    # Halftrack CR 3 (105hp, 18AC, 1Atk+4 Hit: 13 (3d6+2) DPR 4-8)
    # From: Mechanized Infantry Battalion, Royal Armour division.
    # Personnel: 1 Sergeant, 1 Corporals.
    # Personality: ESTJ + Bratty + Courageous
    # Features:
    # - Personnel Carrier: 10 passengers. Practical speed 1200ft/minute.
    # Attack Effects:
    # - Suppression: 30ft hexagon (CHA Save DC 15 or Dodge_Action)
    # - Anti-Air: Can pin down winged units (Pegasi, Griffins, etc)
    # - Topple: If attack hit CON Save or fall Prone.
    # Special Attacks:
    # - Suppressive Fire: 300 r/min, 3000ft 12MOA R=10ft Hit: 7 (2d6)
    # Weapon:
    # - Sd.Kfz.251, 75kW 7.8t -- ₡6300 (22.56k RM)
    # - 7.92mm MG34 70lb 3MOA 300/1200ft±1ft -- ₡100 (312 RM, 100-150 man-hours)
    # - 7.92×57mm ammo 3.5kJ 15r/lb -- ₡15 per 1000 rounds (15 man-hours)
    # Armor:
    # - 5-15mm steel plating: Against small arms Damage Threshold 10.
    # - Gun shield: Frontal protection against bullets (3/4 cover +5AC)
    # https://grokipedia.com/page/Sd.Kfz._251
    # https://grokipedia.com/page/Panzergrenadier
# </halftrack>

#----
# CR 5-6 for 5-6 lvl Party:
# TODO: Отделение снайперов с 1MOA как СВД. Kudere + Lonely + Quiet.
# TODO: Военная полиция, при Royal Guard есть. Riot_Squad. 20AC, латы + щиты.
# TODO: Отряд злых киринов/нириков Valiants с Flame_Blade и Flaming_Sphere.
# <assault_squad>
    # Unit_Cost: ₡7200
    # Assault_Squad CR 6 (125hp, 18AC, 1Atk+6 Hit: 31 (8d4+11) DPR 9-19)
    # From: Mechanized Infantry Battalion, Royal Armour division.
    # Personnel: Lieutenant, Sergeant, 6 Corporals
    # Personality: Tsundere + Resourceful + Fierce independent
    # Behavior:
    # - Bounding Overwatch: Half squad will move, half suppress enemy.
    # - Greedy: Prefer to keep captured equipment for themselves.
    # Features:
    # - Inspiring_Leader: +30hp after short rest (counted)
    # Attack Effects:
    # - Suppression: 30ft hexagon (CHA Save DC 15 or Dodge_Action).
    # - Sap: if attack hit return fire have Disadvantage.
    # Special Attacks:
    # - Throw Grenades: 60ft R=10ft DEX Save, Hit: 14 (4d6) DPR 14
    # - 1 rune Flaming_Sphere: Harass for minute. DEX Save. Hit: 7 (2d6)
    # Reactions:
    # - 1 rune Absorb_Elements (50% less damage from one zonal spell).
    # - Rush: 30ft to nearest cover if attacked.
    # Weapon:
    # - 9mm MP40 9lb 12MOA 60/300ft±1ft -- ₡20 (57 RM, 18 man-hours)
    # - 9×19mm ammo 0.45kJ 35r/lb -- ₡10 per 1000 rounds (10.3-13 man-hours)
    # Armor:
    # - Half Plates and shields (17AC).
# </assault_squad>
# <assault_robot_team>
    # Unit_Cost: ₡10200 (₡5400 iron golem 40hp with built-in HMG)
    # Assault_Robot_Team CR 6 (95hp, 17AC, 2Atk+6 Hit: 17 (2d12+4) DPR 10-20)
    # Appearance: Gilded elegant quadrupedal robot with chest-mounted HMG.
    # From: Mechanized infantry battalion, Royal Armor division.
    # Personnel: Lieutenant, Sergeant, 2 Corporals
    # Personality: ISFJ + Shy + Innocently Passionate
    # Behavior:
    # - Assault Robot: Machine comes first, control team follows.
    # - Anti-Suppression: Assault robot cannot be frightened.
    # Attack Effects:
    # - Armor Piercing: Ignores piercing Resistance.
    # - Anti-Cover: Can pierce brick walls, ignores 3/4 cover.
    # - Suppression: 30ft hexagon (CHA Save DC 15 or Dodge_Action)
    # Special Attacks:
    # - Suppressive Fire: 300 r/min, 3000ft 12MOA R=10ft Hit: 7 (2d6)
    # - 1 rune Targeting_Ray (Assault_Robot): Aiming in smoke/fog/night.
    # Special Movement:
    # - 1 rune Grasp (Assault_Robot): Strong Telekinesis to remove obstacles.
    # - 1 rune Levitation (Assault_Robot): Can hover 30ft above ground.
    # Reactions:
    # - Counter Fire (Assault_Robot): Quick burst if attacked.
    # Weapon:
    # - Rare 4tier Arcane_Robotics iron golem 3.3kW 1000lb -- ₡4800
    # - 12.7mm DShK 350lb 1.5MOA 600/2400ft±1ft -- ₡600 (300-600 man-hours)
    # - 12.7×108mm ammo 16kJ 2r/lb -- ₡500 per 1000 rounds
    # - 7.92mm MG34 70lb 3MOA 300/1200ft±1ft -- ₡100 (312 RM, 100-150 man-hours)
    # - 7.92×57mm ammo 3.5kJ 15r/lb -- ₡15 per 1000 rounds (15 man-hours)
    # Armor:
    # - 5mm steel plating (Robot): Anti-fragmentation Damage Threshold 10.
    # - 50mm Shock-absorption layer (Robot): Piercing Resistance 50%.
    # - Uniform with rune of Mage_Armor (13AC).
# </assault_robot_team>
# <howitzer_squad>
    # Unit_Cost: ₡13400 (₡8600 howitzer and ammo)
    # Howitzer_Squad CR 6 (80hp, 14AC, 1Atk+6 Hit: 66 (12d10+2) DPR 10-20)
    # From: Artillery Battalion, Garrison Regiment
    # Personnel: Sergeant, 2 Corporals, 8 Troopers.
    # Personality: ENFJ + Bored + Sportive
    # Behavior:
    # - Slow rate of fire: Crew need 2 rounds to reload gun and aim.
    # - Slow movement: Cannot attack during movement. No Dash_Action.
    # Attack Effects:
    # - HEAT shell: Damage inside cover/vehicle R=10ft Hit: 14 (4d6)
    # - Demolition: ×2 damage against cover (trenches, walls, buildings).
    # - Suppression: 30ft hexagon (CHA Save DC 15 or Dodge_Action).
    # - Precision: Sergeant knows weapon perfectly (+2 Attack)
    # Special Attacks:
    # - HEAT shell: 1Atk+6 Hit: 47 (8d10+3) DPR 7-14 (aim cone, re-aim 1 round).
    # - Indirect Fire: 1-2 mile, d20+1/shell vs DC 15-30 to hit, R=20ft Hit: 14 (4d6)
    # Weapon:
    # - 105mm leFH18 2t 2MOA 400/1600ft±1ft -- ₡4600 (16.4k RM, 3.2k man-hours)
    # - 80 shells × 105mm HE 7.7MJ 33/50lb = ₡4000 (20 man-hours/shell)
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
    # - Gun shield: Frontal protection against bullets (3/4 cover +5AC)
    # https://grokipedia.com/page/10.5_cm_leFH_18
# </Howitzer_squad>

#----
# CR 7-8 for 7-8 lvl Party:
# <steel_rangers_team>
    # Unit_Cost: ₡10800 (₡4800 power armor 4×20hp)
    # Steel_Rangers_Team CR 8 (145hp, 18AC, 1Atk+6 Hit: 37 (8d6+9) DPR 11-22)
    # From: Mechanized infantry battalion, Royal Armor division.
    # Personnel: 1 Lieutenant, 3 Sergeants.
    # Personality: INTJ + Straightforward + Overconfident
    # Behavior:
    # - Stormtroopers: Will move fast and suppress enemy with heavy fire.
    # - Bulky: Should maintain Concentration or Restrained by armor.
    # Attack Effects:
    # - Suppression: 30ft hexagon (CHA Save DC 15 or Dodge_Action)
    # - Sap: if attack hit return fire have Disadvantage.
    # Special Attacks:
    # - Suppressive Fire: 4 × 150 r/min, 3000ft 12MOA R=10ft Hit: 14 (4d6)
    # - HEAT Rockets: 1Atk+6 Hit: 53 (8d10+9) DPR 16-32
    # - HE Rockets: R=10ft Hit: 14 (4d6) DPR 14
    # - 1 rune Targeting_Ray: Aiming in smoke/fog/night.
    # Special Movement:
    # - Powered Exoskeleton: 500lb load. Dash_Action by Bonus_Action.
    # Reactions:
    # - 1 rune Absorb_Elements (50% less damage from one zonal spell).
    # Weapon:
    # - 4 × 7.92mm MG34 70lb 3MOA 300/1200ft±1ft -- ₡100 (312 RM, 100-150 man-hours)
    # - 7.92×57mm ammo 3.5kJ 15r/lb -- ₡15 per 1000 rounds (15 man-hours)
    # - 4 × 88mm Panzerschreck 24lb 8MOA 150/450ft±1ft -- ₡50 (70 RM, 50 man-hours)
    # - 16 × 88mm HE/HEAT Rocket 10lb -- ₡160
    # Armor:
    # - 4 × Uncommon 2tier Arcane_Robotics power armor 1.5kW 500lb 18AC -- ₡1200
    # - 5mm steel plating 180lb: Anti-fragmentation Damage Threshold 10.
    # - 50mm Shock-absorption layer: Piercing Resistance 50%.
    # - Isolation: Toxin and gas immunity.
    # https://falloutequestria.fandom.com/wiki/Steel_Rangers
# </steel_rangers_team>
# <specops_team>
    # Unit_Cost: ₡9600
    # SpecOps_Team CR 7 (80hp, 16AC, 2Atk+8 Hit: 20 (4d6+6) DPR 18-25)
    # From: Recon Company, Royal Guard division.
    # Personnel: 4 Lieutenants.
    # Personality: Bokodere + Adventurous + Taciturn
    # Behavior:
    # - Infiltrators: Trained to imitate enemy troops.
    # - Battle plan: Will use enemy mistakes to sabotage weak spot.
    # - Battle instincts: Hide, recon, fire, move to cover. Repeat.
    # - Evacuation plan: Usually have pegasi glider team nearby.
    # Attack Effects:
    # - Graze: Even if burst miss, some bullets will reach enemy (6 dmg/Atk).
    # - Sharpshooters: Can snipe without Disadvantage up to 600ft.
    # - Precision: knows weapon perfectly (+2 Attack)
    # Special Attacks:
    # - 1×4 rune Disguise_Self: Imitate enemy appearance for hour.
    # - 1×4 rune Flaming_Sphere: Harass for minute. DEX Save. Hit: 28 (8d6)
    # - Blast Charge: 100lb ×2 damage to buildings, R=20ft Hit: 28 (8d6)
    # Special Movement:
    # - 1 rune Jump: minute of 30ft high leaps, super-maneuverability.
    # Reactions:
    # - Ambush: If unnoticed, can attack and rush 30ft under cover.
    # - 1 rune Absorb_Elements: 50% less damage from one zonal spell.
    # - 1 rune Shield: +5 AC against bullets for few seconds.
    # Weapon:
    # - 7.92mm StG 44 12lb 6MOA 150/600ft±1ft -- ₡20 (78 RM, 19 man-hours)
    # - 7.92×33mm ammo 1.9kJ 25r/lb -- ₡15 per 1000 rounds (15 man-hours)
    # Armor:
    # - Uniform with rune of Mage_Armor (13AC).
    # https://hoi4.paradoxwikis.com/Support_companies#Reconnaissance_(REC)
    # https://falloutequestria.fandom.com/wiki/Zebra_Rifle
# </specops_team>

#----
# CR 9-10 for 9-10 lvl Party:
# TODO: Истребители начинаются отсюда. Strafing: Suppress enemy from above and drop the bomb.
# TODO: Средние танки начинаются отсюда. Пили Т-34.
    # - 10-20mm броня у Т-34, 45-52mm лоб и башня, 36-32t.
    # - 80 снарядов у 76.2mm, 60 снарядов у 85mm пушки.
    # - 500hp на 26 тонн, 14kW/t, 100-200 часов службы, 0.7 kg/cm² траки.
    # - 200-300 литров на 100 км вне дорог.
# <sentinel>
    # TODO: Всё же Sentinel это робот. Лёгкий танкв EaW назывался Breezy.
    # Unit_Cost: ₡22800 (₡19200 Sentinel)
    # Sentinel CR 10 (155hp, 18AC, 2Atk+8 Hit: 27 (4d10+5) DPR 16-32)
    # Appearance: Quadrupedal vaguely ponyesque mecha, each leg having a treaded ball to move.
    # From: Tank Battalion, Royal Armor division.
    # Personnel: Lieutenant, Sergeant.
    # Personality: Tsun-pure + Devoted + Fervid
    # Behavior:
    # - Anti-Suppression: Crew cannot be frightened.
    # Attack Effects:
    # - Armor Piercing: Ignores piercing Resistance.
    # - Anti-Cover: Pierces walls easily, ignores 3/4 cover.
    # - Precision: Lieutenant knows weapon perfectly (+2 Attack)
    # - Topple: If attack hit CON Save or fall Prone.
    # Special Attacks:
    # - HE shells: 3600ft, 2Atk R=10ft DEX Save, Hit: 14 (4d6) DPR 28
    # - Anti-Air Cannon: HE shells effective against gliders.
    # - 1 rune Targeting_Ray: Aiming in smoke/fog/night.
    # Armor:
    # - 5-15mm steel plating: Against small arms Damage Threshold 10.
    # - Isolation: Toxin and gas immunity.
    # Weapon:
    # - 37mm SK C/30 600lb 1MOA 1200/3600ft±1ft -- ₡1600 (≈900 man-hours)
    # - 120 shells × 37×249mmR AP 190kJ 2lb -- ₡600 (5 man-hours/shell)
    # - Rare 6tier Arcane_Robotics Sentinel 60kW 6t -- ₡19200
# </sentinel>

#----
# Lieutenant Feats:
    # d20| Feat             | Влияние
    # -- | ---------------- | -------------------------------------
    #  1 | Shield Master    | Нет урона при спасброске Ловкости.
    #  2 | Inspiring_Leader | +30 бонусных хитов.
    #  3 | Tough            | +20 хитов отряду.
    #  4 | Sharpshooter     | +2 атака.
    #  5 | Heavily Armored  | 17AC отряда.
    #  6 | Thrown Weapon    | Гранаты 2d6+4 10ft радиус.
    #  7 | Charger          | ×2 урона если вне укрытий.
    #  8 | Magic_Initiate   | +2 кантрипа, 1 заклинание.
    #  9 | Healer           | Короткий отдых за 10 минут.
    # 10 | Chief            | ×2 лечение на коротком отдыхе.
    # 11 | Poisoner         | Попадая отравляет на раунд СЛ 15.
    # 12 | Mage_Slayer      | Помеха концентрации при попадании.
    # 13 | Weapon Master    | Vex, Sap или Topple при попадании.
    # 14 | Protection       | Помеха атакам по герою в зоне отряда.
    # 15 | Interception     | Снижение урона герою 1d10+2 реакцией.
    # 16 | Speedy           | Ход без помех по сложной местности.
    # 17 | Observant        | Активное обнаружение вместо пассивного.
    # 18 | Alert            | Не теряют ход при внезапно атаке.
    # 19 | Skulker          | Прячутся при Dash/Disengage.
    # 20 | Two-Weapon       | Нет помехи в ближнем бою.
    # https://www.aidedd.org/public/feat/

#----
# Тесты, армия:

metadict_army['Полк гвардии'] = {
        # amber -sm Полк гвардии -E 'lvl'
        # amber -sm Полк гвардии -E заклинания
        # amber -sm Полк гвардии -E 'заклинаний/год'
        # amber -sm Полк гвардии -E Волшебный предмет
        # Старшие офицеры 10% героев 9+ lvl (правящие элиты)
        # При норме 16 века в 40 солдат на 10k населения:
        # 9 lvl -- 30 героев (капитан, до 250 солдат)
        # 10 lvl -- 20 героев (майор, до 500 солдат)
        # 11 lvl -- 10 героев (подполковник, до 1000 солдат)
        # 12+ lvl -- 10 героев (полковник, до 1000 солдат)
        # У них 5.6 млн бит доходов с капитала, 1.1M трудовых.
        # Младшие офицеры 3.5% героев 5-8 lvl (национальные элиты)
        # 8 lvl -- 70 героев
        # 7 lvl -- 90 героев
        # 6 lvl -- 90 героев
        # 5 lvl -- 130 героев
        # У них 3.8 млн бит доходов с капитала, 1.3M трудовых.
        'Батальон бойцов-пегасов':3,
        'Батальон варваров-пегасов':4,
        'Батальон единорогов-чародеев':1,
        'Батальон земнопони-паладинов':1,
        'Батальон земнопони-следопытов':1,
        #'Батальон тылового обеспечения':1,
        }

metadict_army['Батальон бойцов-пегасов'] = {
        # Рыцарский орден, живущий с доходов командиров.
        # Бюджет: 391/750k бит (42% оборота, 1173 бит/бойца, 37% солдатам)
        # Wealth | lvl | Штат | Звание       | Бит/год
        # ------ | --- | ---- | ------------ | -------
        # 3000   | 12+ | -    | Полковник    | ~500k
        # 400    | 11  | 1    | Подполковник | ~200k
        # 100    | 10  | 2    | Майор        | ~50k
        # 13.2   | 9   | 3    | Знаменосец * | 6600
        # 6.8    | 7-8 | 16   | Капитан      | 3400
        # 3.6    | 5-6 | 31   | Лейтенант    | 1800
        # 2      | 4   | 45   | Сержант      | 1000
        # 1.4    | 3   | 81   | Капрал       | 700
        # 1      | 2   | 162  | Солдат       | 500
        # 0.8    | 1   | -    | Рекрут       | 400
        # * Прапорщик -- избираемый бойцами офицер.
        # Статусный разрыв: правящая элита vs пегасы.
        # Для солдат учтено +200 бит еды и жилья.
        'Управление батальона бойцов-пегасов':1,
        'Рота бойцов-пегасов':3,
        }

metadict_army['Батальон варваров-пегасов'] = {
        'Управление батальона варваров-пегасов':1,
        'Рота варваров-пегасов':3,
        }

metadict_army['Батальон единорогов-чародеев'] = {
        'Управление батальона единорогов-чародеев':1,
        'Рота единорогов-чародеев':3,
        }

metadict_army['Батальон земнопони-паладинов'] = {
        'Управление батальона земнопони-паладинов':1,
        'Рота земнопони-паладинов':3,
        }

metadict_army['Батальон земнопони-следопытов'] = {
        'Управление батальона земнопони-следопытов':1,
        'Рота земнопони-следопытов':3,
        }

metadict_detail['Управление батальона бойцов-пегасов'] = {
        '-Герои-пегасы (бойцы) (11 lvl)':1,
        '-Герои-пегасы (бойцы) (10 lvl)':2,
        '-Герои-пегасы (бойцы) (8 lvl)':4,
        '-Герои-пегасы (бойцы) (6 lvl)':4,
        }

metadict_detail['Управление батальона варваров-пегасов'] = {
        '-Герои-пегасы (варвары) (11 lvl)':1,
        '-Герои-пегасы (варвары) (10 lvl)':2,
        '-Герои-пегасы (варвары) (8 lvl)':4,
        '-Герои-пегасы (варвары) (6 lvl)':4,
        }

metadict_detail['Управление батальона единорогов-чародеев'] = {
        '-Герои-единороги (чародеи) (11 lvl)':1,
        '-Герои-единороги (чародеи) (10 lvl)':2,
        '-Герои-единороги (чародеи) (8 lvl)':4,
        '-Герои-единороги (чародеи) (6 lvl)':4,
        }

metadict_detail['Управление батальона земнопони-паладинов'] = {
        '-Герои-земнопони (паладины) (11 lvl)':1,
        '-Герои-земнопони (паладины) (10 lvl)':2,
        '-Герои-земнопони (паладины) (8 lvl)':4,
        '-Герои-земнопони (паладины) (6 lvl)':4,
        }

metadict_detail['Управление батальона земнопони-следопытов'] = {
        '-Герои-земнопони (следопыты) (11 lvl)':1,
        '-Герои-земнопони (следопыты) (10 lvl)':2,
        '-Герои-земнопони (следопыты) (8 lvl)':4,
        '-Герои-земнопони (следопыты) (6 lvl)':4,
        }

metadict_detail['Рота бойцов-пегасов'] = {
        'Управление роты бойцов-пегасов':1,
        'Взвод бойцов-пегасов':3,
        }

metadict_detail['Рота варваров-пегасов'] = {
        'Управление роты варваров-пегасов':1,
        'Взвод варваров-пегасов':3,
        }

metadict_detail['Рота единорогов-чародеев'] = {
        'Управление роты единорогов-чародеев':1,
        'Взвод единорогов-чародеев':3,
        }

metadict_detail['Рота земнопони-паладинов'] = {
        'Управление роты земнопони-паладинов':1,
        'Взвод земнопони-паладинов':3,
        }

metadict_detail['Рота земнопони-следопытов'] = {
        'Управление роты земнопони-следопытов':1,
        'Взвод земнопони-следопытов':3,
        }

metadict_detail['Управление роты бойцов-пегасов'] = {
        '-Герои-пегасы (бойцы) (9 lvl)':1,
        '-Герои-пегасы (бойцы) (8 lvl)':1,
        }

metadict_detail['Управление роты варваров-пегасов'] = {
        '-Герои-пегасы (варвары) (9 lvl)':1,
        '-Герои-пегасы (варвары) (8 lvl)':1,
        }

metadict_detail['Управление роты единорогов-чародеев'] = {
        '-Герои-единороги (чародеи) (9 lvl)':1,
        '-Герои-единороги (чародеи) (8 lvl)':1,
        }

metadict_detail['Управление роты земнопони-паладинов'] = {
        '-Герои-земнопони (паладины) (9 lvl)':1,
        '-Герои-земнопони (паладины) (8 lvl)':1,
        }

metadict_detail['Управление роты земнопони-следопытов'] = {
        '-Герои-земнопони (следопыты) (9 lvl)':1,
        '-Герои-земнопони (следопыты) (8 lvl)':1,
        }

metadict_detail['Взвод бойцов-пегасов'] = {
        'Управление взвода бойцов-пегасов':1,
        'Отделение бойцов-пегасов (ветеранов)':1,
        'Отделение бойцов-пегасов':2,
        }

metadict_detail['Взвод варваров-пегасов'] = {
        'Управление взвода варваров-пегасов':1,
        'Отделение варваров-пегасов (ветеранов)':1,
        'Отделение варваров-пегасов':2,
        }

metadict_detail['Взвод единорогов-чародеев'] = {
        'Управление взвода единорогов-чародеев':1,
        'Отделение единорогов-чародеев (ветеранов)':1,
        'Отделение единорогов-чародеев':2,
        }

metadict_detail['Взвод земнопони-паладинов'] = {
        'Управление взвода земнопони-паладинов':1,
        'Отделение земнопони-паладинов (ветеранов)':1,
        'Отделение земнопони-паладинов':2,
        }

metadict_detail['Взвод земнопони-следопытов'] = {
        'Управление взвода земнопони-следопытов':1,
        'Отделение земнопони-следопытов (ветеранов)':1,
        'Отделение земнопони-следопытов':2,
        }

metadict_detail['Управление взвода бойцов-пегасов'] = {
        '-Герои-пегасы (бойцы) (7 lvl)':1,
        '-Герои-пегасы (бойцы) (4 lvl)':2,
        }

metadict_detail['Управление взвода варваров-пегасов'] = {
        '-Герои-пегасы (варвары) (7 lvl)':1,
        '-Герои-пегасы (варвары) (4 lvl)':2,
        }

metadict_detail['Управление взвода единорогов-чародеев'] = {
        '-Герои-единороги (чародеи) (7 lvl)':1,
        '-Герои-единороги (чародеи) (4 lvl)':2,
        }

metadict_detail['Управление взвода земнопони-паладинов'] = {
        '-Герои-земнопони (паладины) (7 lvl)':1,
        '-Герои-земнопони (паладины) (4 lvl)':2,
        }

metadict_detail['Управление взвода земнопони-следопытов'] = {
        '-Герои-земнопони (следопыты) (7 lvl)':1,
        '-Герои-земнопони (следопыты) (4 lvl)':2,
        }

metadict_detail['Отделение бойцов-пегасов (ветеранов)'] = {
        '-Герои-пегасы (бойцы) (6 lvl)':1,
        '-Герои-пегасы (бойцы) (4 lvl)':1,
        '-Герои-пегасы (бойцы) (3 lvl)':9,
        }

metadict_detail['Отделение варваров-пегасов (ветеранов)'] = {
        '-Герои-пегасы (варвары) (6 lvl)':1,
        '-Герои-пегасы (варвары) (4 lvl)':1,
        '-Герои-пегасы (варвары) (3 lvl)':9,
        }

metadict_detail['Отделение единорогов-чародеев (ветеранов)'] = {
        '-Герои-единороги (чародеи) (6 lvl)':1,
        '-Герои-единороги (чародеи) (4 lvl)':1,
        '-Герои-единороги (чародеи) (3 lvl)':9,
        }

metadict_detail['Отделение земнопони-паладинов (ветеранов)'] = {
        '-Герои-земнопони (паладины) (6 lvl)':1,
        '-Герои-земнопони (паладины) (4 lvl)':1,
        '-Герои-земнопони (паладины) (3 lvl)':9,
        }

metadict_detail['Отделение земнопони-следопытов (ветеранов)'] = {
        '-Герои-земнопони (следопыты) (6 lvl)':1,
        '-Герои-земнопони (следопыты) (4 lvl)':1,
        '-Герои-земнопони (следопыты) (3 lvl)':9,
        }

metadict_detail['Отделение бойцов-пегасов'] = {
        '-Герои-пегасы (бойцы) (5 lvl)':1,
        '-Герои-пегасы (бойцы) (4 lvl)':1,
        '-Герои-пегасы (бойцы) (2 lvl)':9,
        }

metadict_detail['Отделение варваров-пегасов'] = {
        '-Герои-пегасы (варвары) (5 lvl)':1,
        '-Герои-пегасы (варвары) (4 lvl)':1,
        '-Герои-пегасы (варвары) (2 lvl)':9,
        }

metadict_detail['Отделение единорогов-чародеев'] = {
        '-Герои-единороги (чародеи) (5 lvl)':1,
        '-Герои-единороги (чародеи) (4 lvl)':1,
        '-Герои-единороги (чародеи) (2 lvl)':9,
        }

metadict_detail['Отделение земнопони-паладинов'] = {
        '-Герои-земнопони (паладины) (5 lvl)':1,
        '-Герои-земнопони (паладины) (4 lvl)':1,
        '-Герои-земнопони (паладины) (2 lvl)':9,
        }

metadict_detail['Отделение земнопони-следопытов'] = {
        '-Герои-земнопони (следопыты) (5 lvl)':1,
        '-Герои-земнопони (следопыты) (4 lvl)':1,
        '-Герои-земнопони (следопыты) (2 lvl)':9,
        }

