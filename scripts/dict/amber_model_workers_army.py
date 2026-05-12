#----
# DnD 5.5e FoE/EaW Urban Warfare:
    # Fallout: Equestria and Equestria at War
    # https://equestriaatwar.wiki.gg/wiki/List_of_Countries
    # https://equestriaatwar.wiki.gg/wiki/World_Map_and_Geography
    # https://equestriaatwar.wiki.gg/wiki/Timeline_of_World_History
    # https://equestriaatwar.wiki.gg/wiki/Equestrian_events
    # https://hoi4.paradoxwikis.com/Hearts_of_Iron_4_Wiki
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
        # Party of 4 heroes 5 lvl with 4 Squads against castle garrison:
        # 1."Veteran_Squad, control the gate and shot anyone.". -- 10min.
        # 2."Artillery_Team, suppress them on the wall." -- 50 shells, 10min.
        # 3."Assault_Squad, follow us inside the castle and take captives."
        # 4."Recon_Team, watch the pass, be ready to aim Artillery_Team."
        # 5."Artillery_Team, be ready to control the pass."
        # 6."Veteran_Squad, protect Artillery_Team."
        # 6/12 Command Actions used, 6/12 for surprises.
    # This format useful with LLM for simulation:
        # Generate list of possible enemy decisions.
        # Use d4 roll to determine enemy decision:
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
        # - Crystallized_Spell for units without concentration.

#----
# Soldiers and Lieutenants:
    # 1 eqb (equestrian bit) = 50 USD (2024)
    # lvl | Soldier    | CR  | Exp   | Cost   | Commentary
    # --- | ---------- | --- | ----- | ------ | -----------------
    # 2   | Trooper    | 1/4 |  0    | 300eqb | 10hp, Proficiency
    # 3   | Corporal   | 1/2 | -1.2k | 600    | 20hp, Mastery
    # 4   | Sergeant   | 1   | -3.9k | 1200   | 30hp, Style
    # 5   | Lieutenant | 2   | +10.4 | 2400   | 40hp, Feat
    # Cost = equipment, you can equip unit with this money.
    # Exp = hero experience. +1 Lieutenant per 10k hero Exp.
    # Lieutenant can train up to 9 Corporals or 3 Sergeants.
    # Troopers can use only one weapon and medium armor.
    # - Ordinary Squad -- 1 Sergeant and 9 Troopers.
    # - Veteran Squad -- 1 Lieutenant and 9 Corporals.
    # - Elite Squad -- 3 Lieutenants and 9 Sergeants.
    # - SpecOps Squad -- up to 12 Lieutenants.
# Squad creation:
    # Squad consists of 3-12 soldiers and leader:
    # - 1 squad per 30ft hexagon of battlescape.
    # - 2+ squads per 30ft hex with Disadvantage.
    # - Squad have 30ft range of Opportunity_Attack.
    # - Squad have 50% hp and 50% Damage Rolls.
    # Soldier    | HP   | Attack | Dmg Rolls | Dmg mod
    # ---------- | ---- | ------ | --------- | -------
    # Trooper    | +5   | 1d20+2 | +0.5      | -
    # Corporal   | +10  | 1d20+3 | +0.5      | +1
    # Sergeant   | +15  | 1d20+4 | +0.5      | +2
    # Lieutenant | +20  | 1d20+5 | +1        | +3
    # Veteran Squad of corporals can use Weapon_Mastery.
    # Elite and SpecOps can use 2 attacks with 50% Dmg.
    # Crew will use heavy weapon instead of firearms.
    # Crew append vehicle hp to the Hit Points pool.
    # Crew have Damage Threshold (10-20 APC/tanks).
# Squad Hit Points represents combat endurance:
    # With 0hp squad incapacitated and suffer 1 Exhaustion.
    # Next -5hp means Trooper killed, -10hp Corporal killed.
    # Incapacitated squad can move, but cannot attack, react.
    # Incapacitated squad will be captured in any melee clash.
    # Squad with 0hp will lose their vehicle and heavy weapon.
    # Squad with killed soldiers cannot regain any Hit Points.
    # Otherwise they will regain Hit Points after short rest.
# Squads vulnerable to zonal attacks and melee:
    # R=10ft (10lb shell) --> ×2 damage, except 1/2 cover or prone.
    # R=20ft (≥50lb shell) --> ×2 damage, except 3/4 cover or prone.
    # Zonal spells (all) --> ×2 damage except 3/4 cover or Doge_Action.
    # Melee clash vs hero --> ×2 damage + Disadvantage, except elite.
    # Squads can be dangerous, but much less tough than monsters.

#----
# Army structure:
    # Hero rank, loyal Lieutenants and squad, vassal Leaders and army funds:
    # lvl | Rank    | Exp/lvl | Exp sum | Ltn | Squad  | Vassl | Army | Full Cost
    # --- | ------- | ------- | ------- | --- | ------ | ----- | ---- | ---------
    # 1   | Rookie  |       0 |      0  | -   | 1T     | -     | -    | 0.6+0.3
    # 2   | Lucky   |     300 |    300  | -   | 3T     | -     | -    | 1.2+0.9
    # 3   | Hero    |     900 |  1 200  | -   | 1C+3T  | -     | -    | 2.4+1.5
    # 4   | Hero    |   2 700 |  3 900  | -   | 3C+9T  | -     | -    | 3.6+4.5
    # 5   | Leader  |   6 500 | 10 000  | 1   | 9C     | -     | ≤30  | 12.6k
    # 6   | Leader  |  14 000 | 24 000  | 2   | 3S+9C  | -     | 30   | 21.6k
    # 7   | Captain |  23 000 | 47 000  | 4   | 12S    | 3     | 90   | 31+13×3
    # 8   | Captain |  34 000 | 81 000  | 8   | 4L+12S | 5     | 150  | 41+22×5
    # 9   | Major   |  48 000 | 129 000 | 12  | 3×4L   | 5×3   | 450  | 38+70×5
    # 10  | Major   |  64 000 | 193 000 | 19  | 2×8L   | 5×5   | 750  | 53+151×5
    # 11  | Colonel |  85 000 | 278 000 | 27  | 3×8L   | 5×5×3 | 2250 | 77+388×5
    # 12  | Colonel | 100 000 | 378 000 | 37  | 3×12L  | 5×5×5 | 3750 | 115+808×5
    # Promotions: Sergeant --> Lieutenant --> vassal Leader --> vassal Captain.
    # Tree of elite group will grow around leader, his friends, and downward.
    # Major 9 lvl can have 12 own Lieutenants and 5 Captains with 15 Leaders.
    # Major have battalion of 450 troopers and own squad of 3 SpecOps_Team.
    # Battalion funds: 450cap × 1200eqb/cap to MUSD = 27 million USD PPP
# Frontline and Assault:
    # Battalion Combat Width -- 1-2 mile in defense, 3000ft in offense.
    # - 100 howitzers support 1 Battalion in offense from 1-3 miles.
    # - 6300 shells/hour need to suppress 105 enemy positions.
    # Artillery should suppress 50% targets, Pegasi 25-50%.
    # Infantry must follow shelling with speed 300ft/min.
    # https://hoi4.paradoxwikis.com/Combat_tactics
# Artillery and Air Force:
    # To suppress 30ft hexagon effective you need 5 shells/minute and one gun.
    # Roll d20 (+1/shell) vs DC 15-25 to hit (consider distance and weather).
    # Roll CHA Save DC 10+1/shell or target suppressed and have Dodge_Action.
    # Cost | Range | Support Source   | Explosion      | Commentary
    # ---- | ----- | ---------------- | -------------- | ---------------------
    # 800  | 60mi  | Glider_Team      | 60ft 12d6 (42) | 800lb 600ft±2° R=40ft
    # 100  | 6mi   | Howitzer_Team    | 20ft 8d6 (28)  | 100lb shell, 5 r/min
    # 50   | 4mi   | Artillery_Team   | 20ft 4d6 (14)  | 50lb shell, 5 r/min
    # 10   | 2mi   | Cannon_Team      | 10ft 2d6 (7)   | 10lb shell, 5 r/min
    # Enemy should have strong AA defense because of cheap pegasi bombing.
    # Battery -- 8 howitzers (40 shoots/minute). Division -- 3 battery.
    # Optimal shelling 10 minutes (less no damage, more no surprise)
    # - 1914 (50lb shells) -- 3 shells/injured, 12.5 shells/killed.
    # - 1917 (50lb shells) -- 55 shells/injured, 221 shells/killed.
    # - 2024 (100lb shells) -- 10 shells/injured in open terrain.
    # - 2024 (100lb shells) -- 50 shells/injured inside buildings.
    # 70% steel into shells; 20% arms and ammo; 10% artillery and tanks.
    # 50lb shell (73% case; 13% explosives; 5% gunpowder) = 200lb steel.
    # Shrapnel: (50lb × 73% / 5g) / sphere_sa(20ft) to m² = 7 DR/m²
    # Explosion: (50lb × 13% × 4.184 kJ/g) / sphere(20ft) = 13kPa

#----
# War Economy:
    # Tooth-to-tail ratio:
        # 1% infantry (WW1) = 3% military = 15% GDP, population, workforce
        # 1% infantry (WW2) = 5% military = 25% GDP, population, workforce
        # 1200 eqb/soldier = 60k USD/soldier like modern India, Brazil.
        # https://www.globalmilitary.net/rankings/countries/budget-per-soldier/
    # Equestria (prewar):
        # 50M Equestria: 12 billion eqb × 1% to GUSD = 6 billion USD
        # The Equestrian Army: 12Geqb × 1% / 1200eqb = 100k soldiers (0.2%)
        # The Equestrian Navy: 12Geqb × 0.8% / 1200eqb = 80k soldiers (0.2%)
        # Divisions           | №  | Battalions        | Readiness
        # ------------------- | -- | ----------------- | ---------
        # Royal Guard         | 7  | 3 inf+rec+mp      | useless
        # Garrison Regiment   | 9  | 4 inf             | useless
        # Onhooves Division   | 2  | 7 inf+eng         | 20%
        # Pegasi Division     | 1  | 8 airborne        | 30%
        # Royal Armour        | 2  | 3 tanks, 4 minf   | 40%,50%
        # Total 100k ponypower
        # Battalion: 9 inf+art+eng+rec+log
        # https://equestriaatwar.wiki.gg/wiki/Equestria#Starting_Situation
    # Changeling Lands (prewar):
        # Divisions           | №  | Battalions        | Readiness
        # ------------------- | -- | ----------------- | ---------
        # Infanterie Division | 7  | 7 inf+art+rec+eng | -
        # Queen's Guard       | 1  | 4 inf+art+rec+eng | -
        # Jager Division      | 4  | 7 inf+art+rec+eng | -
        # Grenzinfanterie     | 5  | 4 infantry        | -
        # Panzer Division     | 3  | 3 tank, 4 minf    | -
        # Motorisierte Inf    | 5  | 8 minf+art+rec+en | -
        # Total 190k ponypower
        # https://equestriaatwar.wiki.gg/wiki/Changeling_Lands#Military

#----
# CR 1/8 - CR 2 for 1-2 lvl Party:
# <infantry_team>
    # Unit_Cost: 1.5k eqb
    # Infantry_Team: CR 1/2 (25hp, 13AC, 1atc+3, Hit: 8 (2d6+1) DPR 2-5)
    # From: Infantry Battalion, Garrison Regiment
    # Personnel: Corporal, 3 troopers
    # Behavior:
    # - Fireteam: Will move together from cover to cover.
    # - Rookies: Can make stupid mistakes during real fight.
    # Weapon: Breech-loaded rifles, rarely muzzle-loaded guns
    # Armor: Padded armor, Chain Shirts, rarely Breastplates.
    # https://equestriaatwar.wiki.gg/wiki/Infantry_technology
# </infantry_team>
# <skilled_infantry_team>
    # Unit_Cost: 2.4k eqb
    # Skilled_Infantry_Team: CR 1 (35hp, 14AC, 1atc+4, Hit: 10 (2d6+3) DPR 3-6)
    # From: Infantry Battalion, Garrison Regiment
    # Personnel: Sergeant, corporal, 2 troopers
    # Behavior:
    # - Entrenchment: Will use any resources around to fortify position.
    # - Survivalists: Will check possible cover first, follow order second.
    # Special Attacks:
    # - 1 rune Targeting_Ray (Sergeant): Aiming in smoke/fog/night.
    # - Bipods: Can shoot from prone position without Disadvantage.
    # Reactions:
    # - Rush: Up to 30ft to nearest cover if attacked.
    # Weapon: Breech-loaded rifles, rarely SMG.
    # Armor: Chain Shirts, rarely Breastplates.
# </skilled_infantry_team>
# <animated_dead_team>
    # Unit_Cost: 1.5k eqb
    # Animated_Dead_Team: CR 2 (52hp, 16AC, 1atc+3, Hit: 13 (2d6+6) DPR 4-8)
    # From: Animate_Dead on 4 corpses × 60 days × 2.2 eqb/day = 528 eqb
    # Personnel: 4 skeleton/zombies (always quadrupedal equines)
    # Behavior:
    # - Undead: Hated and considering prohibited weapon in most cases.
    # - Forgetful: Can perform simple orders, but no more than 1 hour.
    # - Untrustworthy: Without constant control can attack ally squad.
    # Special Attacks:
    # - Suicide bombers: If defeated in melee, R=20ft Hit: 14 (4d6)
    # Weapon:
    # - 50lb explosive charges.
    # - Melee weapon, usually spears.
    # Armor: Chain Shirts and shields.
# </animated_dead_team>
# <earthpony_veteran_team>
    # Unit_Cost: 3.0k eqb
    # Earthpony_Veteran_Team: CR 2 (45hp, 15AC, 1atc+4, Hit: 12 (2d6+5) DPR 4-7)
    # From: Equestrian Infantry Battalion, Onhooves division.
    # Personnel: Sergeant, 3 Corporals.
    # Physique:
    # - Ponies have hooves instead of hands and fingers.
    # - Ponies use mouth to hold weapon and interacts with objects.
    # Behavior:
    # - Geomanty: Can make trench in minute by using runes of Mold_Earth.
    # - Sluggish: Prefer to keep position, even if movement is better.
    # Special Attacks:
    # - 1 rune Targeting_Ray (Sergeant): Aiming in smoke/fog/night.
    # - Bipods: Can shoot from prone position without Disadvantage.
    # Reactions:
    # - 1 rune Absorb_Elements (50% less damage from one zonal spell).
    # Weapon: Breech-loaded rifles, rarely SMG.
    # Armor: Breastplates, rarely Half Plate.
# </earthpony_veteran_team>
# <pegasi_veteran_team>
    # Unit_Cost: 3.0k eqb
    # Pegasi_Veteran_Team: CR 2 (45hp, 14AC, 1atc+4, Hit: 12 (2d6+5) DPR 4-7)
    # From: Equestrian Airborne Battalion, Pegasi division.
    # Personnel: Sergeant, 3 Corporals.
    # Physique:
    # - Pegasi can use their wings to deftly grab items and throw grenades.
    # - Pegasi magnetic levitation allows them to fly at 60-120ft altitude.
    # Behavior:
    # - Aviators: Prefer bombardment at careless targets.
    # - Impatient: Can move without order, hard to control.
    # Special movement:
    # - Dash: Action to fly 120ft, land and take nearest cover.
    # Special Attacks:
    # - Throw Grenades: 60ft R=10ft DEX Save, Hit: 7 (2d6)  DPR 7
    # - Glide Bombs: 4×50lb, 600ft range from 120ft altitude, R=20ft 25% Hit: 14 (4d6)
    # Weapon: Mostly SMG and grenades.
    # Armor: runes of Mage_Armor.
# </pegasi_veteran_team>
# <unicorn_veteran_team>
    # Unit_Cost: 3.0k eqb
    # Unicorn_Veteran_Team: CR 2 (45hp, 14AC, 1atc+4, Hit: 12 (2d6+5) DPR 4-7)
    # From: Equestrian Infantry Battalion, Royal Guard division.
    # Personnel: Sergeant, 3 Corporals.
    # Physique:
    # - Unicorns horn glows when they use telekinesis to hold weapon.
    # Behavior:
    # - Bookish: Have opinion and knowledge about everything around.
    # - Timorous: Can ignore order and even retreat, if in danger.
    # Special Attacks:
    # - Telekinetic Throw Grenades: 60ft R=10ft DEX Save, Hit: 7 (2d6) DPR 7
    # - 1 rune Magic_Missile (Sergeant): 120ft 3atc Hit: 11 (1d4+1) DPR 11
    # Reactions:
    # - 1 rune Shield: +5 AC against bullets for few seconds.
    # Weapon: Breech-loaded rifles and grenades.
    # Armor: runes of Mage_Armor.
# </unicorn_veteran_team>
# <machinegun_team>
    # Unit_Cost: 4.8k eqb
    # Machinegun_Team CR 2 (35hp, 14AC, 1atc, Hit: 16 (4d6+2) DPR 5-10)
    # From: Infantry Battalion, Garrison Regiment
    # Personnel: Sergeant, 2 Corporals.
    # Behavior:
    # - Flanking fire: Prefer oblique fire at moving targets.
    # - Trigger happy: Tend to waste ammo even at moving rats.
    # Attack Effects:
    # - Suppression: 30ft hexagon (CHA Save DC 15 or Dodge_Action)
    # Special Attacks:
    # - Burst: If unnoticed can attack with Advantage.
    # Weapon:
    # - 7.62-mm machine-gun, 300 shot/minute, 2400ft±0.2° R=10ft
    # - 7.62-mm Maxim gun (1904) -- 1.7-2.2k eqb
# </machinegun_team>
# <cannon_team>
    # Unit_Cost: 4.8k eqb
    # Cannon_Team CR 2 (35hp, 15AC, 1atc, R=10ft Hit: 7 (2d6) DPR 7)
    # From: Infantry Battalion, Garrison Regiment
    # Personnel: Sergeant, 4 Troopers.
    # Features:
    # - Gun shield: Frontal protection against bullets (+2 AC).
    # Behavior:
    # - Slow aiming: No reaction fire, Cannon need full round to aim.
    # - Slow movement: Cannot attack during movement. No Dash_Action.
    # Attack Effects:
    # - Suppression: 30ft hexagon (CHA Save DC 15 or Dodge_Action).
    # - Demolition: ×2 damage against cover (trenches, walls, buildings).
    # Special Attacks:
    # - AP shell: atc+4 4d10+2 (24) DPR 4-7 (aim cone, re-aim 1 round).
    # Weapon:
    # - 76mm 800kg regimental cannon, range 2400ft±0.1° R=5ft
    # - 76mm cannon M1927 -- 1.6-2.4k eqb (0.8-1.2k manhours)
# </cannon_team>

#----
# CR 3-4 for 3-4 lvl Party:
# <infantry_squad>
    # Unit_Cost: 4.2k eqb
    # Infantry_Squad CR 3 (65hp, 13AC, 1atc+4, Hit: 18 (4d6+4) DPR 5-11)
    # From: Infantry Battalion, Garrison Regiment
    # Personnel: Sergeant, 2 Corporals, 6 Troopers
    # Weapon: Breech-loaded rifles, rarely submachine guns.
    # Armor: Padded armor, Chain Shirts, rarely Breastplates.
# </infantry_squad>
# <sapper_squad>
    # Unit_Cost: 5.0k eqb
    # Sapper_Team CR 3 (45hp, 14AC, 1atc+4, Hit: 12 (2d6+5) DPR 4-7)
    # From: Equestrian Engineer Company, Onhooves division.
    # Personnel: Sergeant, 3 Corporals.
    # Behavior:
    # - Combat Engineers: Will flavor any task with explosives.
    # - Touchy: Hate direct orders, always know more fiery way.
    # Special Attacks:
    # - Flamethrowers: Can clear minefields, 30ft cone Hit: 14 (2d6)
    # - Minefield: 1 hour, 240lb mines, 300×20ft zone, Hit: (2d6) (7)
    # - Blast Charge: 100lb ×2 damage to buildings, R=20ft Hit: 28 (8d6)
    # Weapon:
    # - 2000lb various explosives on 4 carts = 2k eqb
# </sapper_squad>
# <signal_squad>
    # Unit_Cost: 5.0k eqb
    # Signal_Team CR 3 (45hp, 14AC, 1atc+4, Hit: 12 (2d6+5) DPR 4-7)
    # From: Signal Company, Garrison Regiment.
    # Personnel: Sergeant, 3 Corporals.
    # Behavior:
    # - Spotter: Can aim indirect fire from artillery 1-3 miles.
    # - Wary: Should avoid firefights, if artillery can support.
    # Special Attacks:
    # - 2 Artillery Support: 40 shells/minute,, R=20ft 5% Hit: 14 (4d6)
    # Weapon:
    # - 40 × 50lb shells = 2000lb ammo = 2k eqb
# </signal_squad>
# <unicorn_mage_team>
    # Unit_Cost: 6.0k eqb
    # Unicorn_Magic_Team CR 3 (65hp, 15AC, 1atc+6 Hit: 20 (2d10+9) DPR 9-13)
    # From: Equestrian Mage Company, Royal Guard division.
    # Personnel: Lieutenant, 3 Sergeants
    # Physique:
    # - Unicorns horn shines when they use cantrips and spells.
    # Features:
    # - Enchanter (Lieutenant): Can recharge 1 rune during long rest.
    # - Utility Cantrips: Light, Message, Mending, Prestidigitation, etc.
    # Behavior:
    # - Magicians: Prefer offensive cantrips rather than weapon.
    # - Limited Focus: Cannot use Shielding and Cantrips at same time.
    # Defense:
    # - Arcane Shielding: Damage reduction 10 (4d4) during Dodge_Action.
    # Attacks:
    # - Offensive Cantrips: Fire_Bolt, Ray_of_Frost, Eldritch_Blast, etc.
    # Special Attacks:
    # - 1×4 runes Magic_Missile: 120ft 3atc  4d4+4 (42) DPR 42
    # Armor: runes of Mage_Armor.
    # https://equestriaatwar.wiki.gg/wiki/Horse#Racial_Technology
# </unicorn_mage_team>
# <pegasi_glider_team>
    # Unit_Cost: 6.0k eqb
    # Pegasi_Glider_Team CR 4 (65hp, 12AC, 1atc+4, Hit: 18 (4d6+4) DPR 5-11)
    # From: Pegasi Glider-Bomber Squadron, Equestrian Air Force.
    # Personnel: Sergeant, 2 Corporals, 6 Troopers
    # Physique:
    # - Pegasi magnetic levitation allows them to fly at 60-120ft altitude.
    # - Pegasi with glider can fly at 3000ft altitude up to 10 minutes.
    # Special Attacks:
    # - Dive Bomber: 800lb bomb, 600ft altitude, R=60ft Hit: 42 (12d6)
    # Transport:
    # - Glider, 800lb load, 30mi/h speed, cost 1k eqb.
    # Weapon:
    # - 800lb Bunker Buster Bomb = 0.8k eqb
# </pegasi_glider_team>

#----
# CR 5-6 for 5-6 lvl Party:
# <assault_squad>
    # Unit_Cost: 7.8k eqb
    # Assault_Squad CR 6 (150hp, 18AC, 1atc+6 Hit: 34 (6d6+13) DPR 10-20)
    # From: Mechanized Infantry Battalion, Royal Armour division.
    # Personnel: Lieutenant, 9 Corporals
    # Features:
    # - Inspiring_Leader: +30hp after short rest (counted)
    # Behavior:
    # - Courageous: Ready to charge even across open terrain.
    # - Greedy: Prefer to keep captured equipment for themselves.
    # - Magic haters: Strongly prefer trustworthy guns over runes.
    # Special Attacks:
    # - Throw Grenades: 60ft R=10ft DEX Save, Hit: 14 (6d6) DPR 14
    # Weapon: Submachine guns, rarely melee weapon
    # Armor: Half Plates and shields.
# </assault_squad>
# <robot_machinegun_team>
    # Unit_Cost: 9.6k eqb
    # Robot_Machinegun_Team CR 5 (95hp, 15AC, 2atc+6 Hit: 14 (2d6+7) DPR 8-17)
    # From: Equestrian Mage Company, Royal Guard division.
    # Personnel: Lieutenant, Sergeant, 2 Corporals
    # Behavior:
    # - Robot control: let machine deal with battle tasks.
    # - Wary: avoid firefights, while have robot under command.
    # Attack Effects:
    # - Hex: if robot shoot someone target is impaired.
    # - Sap: if robot shoot someone return fire have Disadvantage.
    # Weapon:
    # - Rare 4tier Arcane_Robotics Hex+Sap, 2atc+7 Hit: 12 (1d8+4+1d6)
# </robotic_machinegun_team>
# <artillery_team>
    # Unit_Cost: 9.6k eqb
    # Artillery_Team CR 5 (80hp, 15AC, 1atc R=10ft Hit: 14 (4d6) DPR 14)
    # From: Artillery Battery, Garrison Regiment
    # Personnel: Sergeant, 2 Corporals, 8 Troopers.
    # Features:
    # - Gun shield: Frontal protection against bullets (+2 AC).
    # Behavior:
    # - Slow aiming: No reaction fire, Cannon need full round to aim.
    # - Slow movement: Cannot attack during movement. No Dash_Action.
    # Attack Effects:
    # - Suppression: 30ft hexagon (CHA Save DC 15 or Dodge_Action).
    # - Demolition: ×2 damage against cover (trenches, walls, buildings).
    # Special Attacks:
    # - AP shell: atc+6 Hit: 47 (8d10+3) DPR 7-14 (aim cone, re-aim 1 round).
    # Weapon:
    # - 105mm 2t howitzer, range 2400ft±0.1° R=5ft
    # - 105mm howitzer leFH 18 (1943) -- 4.6k eqb (16.4k RM, 3.2k manhours)
# </artillery_team>

#----
# CR 7-8 for 7-8 lvl Party:
# <specops_team>
    # Unit_Cost: 9.6k eqb
    # SpecOps_Team CR 7 (80hp, 18AC, 2atc+8 Hit: 15 (2d8+6) DPR 16-22)
    # From: Equestrian Recon Company, Royal Guard division.
    # Personnel: 4 Lieutenants.
    # Features:
    # - Sharpshooters: Can snipe from unusual distances up to 1200ft.
    # Behavior:
    # - Battle plan: Will use enemy mistakes to sabotage weak spot.
    # - Battle instincts: Hide, recon, fire, move to cover. Repeat.
    # - Evacuation plan: Usually have pegasi glider team nearby.
    # Attack Effects:
    # - Graze: Even if burst miss, some bullets will reach enemy (6 dmg/atc).
    # Special Attacks:
    # - 1 rune Fireball: 1atc R=20 Hit: 28 (8d6) DEX Save.
    # - 1 rune Kinetic_Dome: R=10ft +33hp redirect enemy projectiles.
    # Reactions:
    # - Ambush: If unnoticed, can attack and rush 30ft under cover.
    # - 1 rune Absorb_Elements: 50% less damage from one zonal spell.
    # - 1 rune Shield: +5 AC against bullets for few seconds.
    # Weapon: Various modern SALW
    # Armor: Enchanted Half Plates.
# </specops_team>

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

