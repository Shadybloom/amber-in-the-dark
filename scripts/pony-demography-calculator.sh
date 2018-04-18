#!/bin/bash

# Pony demographic calculator v1.06
# Author: one not a very clever pony
# License: WTFPL2 http://www.wtfpl.net/about/
# Скрипт вычисляет возрастной/половой/расовый состав популяции эквестрийских пони, а также подходит для статистики профессий. Можно использовать и для других животных, и для людей — только нужно коэффициенты правильно подобрать.
# На совместимость с командными оболочками кроме zsh и bash не проверялся.

#Распределение Гомпертца-Мейкхама неплохо работает в демографических расчётах для самых разных популяций. Единственный недостаток — оно склонно занижать смертность в начале и завышать в конце (экспонента, что поделать). Для популяции людей даёт хорошие результаты в диапазоне возрастов — 30-70 лет.
#Формула: p=a+b*(c^x)
#Где:
#p — вероятность смерти в процентах
#a — независимый от возраста риск (0.0001%)
#b — коэффициент 2 (0.000113)
#c — коэффициент 3 (1.09)
#Коэффициенты подобраны с учётом исследования: "Parametric models for life insurance mortality data: gompertz's law". Независимый от возраста компонент статистически ничтожен из-за эффектов "понячьего миролюбия" и "вмешательства Селестии".

#-----------------------------------------------------------------------------
# Опции:

# Год новой эры — год начала отсчёта, принимаются любые целые числа больше нуля:
year_real=1210
# Год конца отсчёта.
year_max=1300
# Историческая поправка (нужна, если отсчёт для популяции начинается, например, с 300 года новой эры). Иначе ставь ноль:
year_history=300
# Файл для вывода данных.
pony_file=~/pony-population.txt


# Переменные распределения Гомпертца-Мейкхама:
# Компонент Мейкхама. Независимый от возраста риск:
component_a=0.0001
# Коэффициент b:
coefficient_b=0.000113
# Коэффициент c:
coefficient_c=1.09

# Уменьшение коэффициента c для стариков повышает их выживаемость, а значит частично компенсирует экспоненциальный рост смертности. За каждый год сверх возраста старости коэффициент уменьшается на это значение:
c_old_age_mortality_correction=0.015
# Младенческая смертность (записывается как 0.003 — обозначает 0.3% или 3‰). Прибавляется к риску за первый год жизни:
a_infant_mortality_correction=0.001

# Эффект катаклизма (война, пандемия, стихийное бедствие). Задаётся год:
#year_cataclysm=1280
# И прибавка к уровню смертности за этот год (0.5 значит 50% погибших):
#a_cataclysm_correction=0.5


# Переменные геометрической прогрессии роста населения:
# Начальная численность:
population=200000
# Годовой прирост (переменная вида 1.0018 означает 0.18% или 1.8‰):
increase_coefficient=1.0018
# Уровень рождаемости (например: 0.016 что значит 1.6% или 16 новорожденных на 1000 населения в год):
fertility_rate=0.015


# Возрастное распределение, используется для расчётов социальных слоёв:
# Возраст перехода дети>подростки.
age_teenager=11
# Возраст перехода подростки>взрослые.
age_adult=19
# Возраст стариков. С этого возраста начинает работать c_old_age_mortality_correction.
age_older=60
# Минимальный возраст деторождения (используется в вычислении суммарного коэффициента рождаемости):
age_fertile_min=15
# Максимальный возраст деторождения:
age_fertile_max=50

# Половой и расовый состав населения:
# Опирается на исследование популяции эквестрийских пони:
# http://tabun.everypony.ru/blog/science/27575.html
# Кобылок — 60%
# Среди кобылок:
# Земнопоньки — 56% Пегаски — 26% Единорожки — 18%
# Жеребцов — 40%
# Среди жеребцов: Земнопони — 60% Пегасы — 21% Единороги — 19%

# Если в популяции меньше трёх рас, лишние переменные можно просто закоментировать.
# Раса 1:
race1_male_name="Земнопони"
# Процент от населения. Можно задать выражением, например "0.4*0.6" — будет означать 40% жеребцов и 60% земнопоней из них.
race1_male_percent="0.4*0.6"
race1_female_name="Земнопоньки"
race1_female_percent="0.6*0.56"

# Раса 2
race2_male_name="Пегасы"
race2_male_percent="0.4*0.21"
race2_female_name="Пегаски"
race2_female_percent="0.6*0.26"

# Раса 3
race3_male_name="Единороги"
race3_male_percent="0.4*0.19"
race3_female_name="Единорожки"
race3_female_percent="0.6*0.18"


# Социальные слои:
# Для какого числа профессий проводить расчёты? Максимум — 7.
profession_numbers=7

# Далее идёт длинный список опций для профессий, завёрнутых в функции:
function_profession_1 () {
	# Предполагаемый процент. Например 0.005 — значит 0.5% (5 из тысячи).
	profession_percent=0.015
	# Какие расы учитывать? 0 — не учитывать. 1 — учитывать. Если все нули или строки закоментированы, тогда вычисление не производится.
	race1_male_switch=0
	race1_female_switch=0
	race2_male_switch=0
	race2_female_switch=0
	race3_male_switch=1
	race3_female_switch=1
	# Названия кругов:
	name_apprentice="Ученики школы волшебства"
	name_expert="Дипломированные чародеи"
	name_retiree="Волшебники в отставке"
	# Возраст начала ученичества:
	age_apprentice=$age_teenager
	# Возраст перехода в мастера:
	age_expert=$age_adult
	# Возраст отставки:
	age_retiree=$age_older
}

function_profession_2 () {
	profession_percent=0.0033
	race1_male_switch=1
	race1_female_switch=1
	race2_male_switch=0
	race2_female_switch=0
	race3_male_switch=0
	race3_female_switch=0
	name_apprentice="Воинственные жеребята-земнопони"
	name_expert="Стражники-земнопони"
	name_retiree="Стражники-земнопони в отставке"
	age_apprentice=$age_teenager
	age_expert=$age_adult
	age_retiree=$age_older
}

function_profession_3 () {
	profession_percent=0.01
	race1_male_switch=0
	race1_female_switch=0
	race2_male_switch=1
	race2_female_switch=1
	race3_male_switch=0
	race3_female_switch=0
	name_apprentice="Воинственные жеребята-пегасы"
	name_expert="Стражники-пегасы"
	name_retiree="Стражники-пегасы в отставке"
	age_apprentice=$age_teenager
	age_expert=$age_adult
	age_retiree=$age_older
}

function_profession_4 () {
	profession_percent=0.004
	race1_male_switch=0
	race1_female_switch=0
	race2_male_switch=0
	race2_female_switch=0
	race3_male_switch=1
	race3_female_switch=1
	name_apprentice="Воинственные жеребята-единороги"
	name_expert="Стражники-единороги"
	name_retiree="Стражники-единороги в отставке"
	age_apprentice=$age_teenager
	age_expert=$age_adult
	age_retiree=$age_older
}

function_profession_5 () {
	profession_percent=0.001
	race1_male_switch=1
	race1_female_switch=1
	race2_male_switch=0
	race2_female_switch=0
	race3_male_switch=0
	race3_female_switch=0
	name_apprentice="Драчливые жеребята-земнопони"
	name_expert="Гвардейцы-земнопони"
	name_retiree="Гвардейцы-земнопони в отставке"
	age_apprentice=$age_teenager
	age_expert=$age_adult
	age_retiree=$age_older
}

function_profession_6 () {
	profession_percent=0.004
	race1_male_switch=0
	race1_female_switch=0
	race2_male_switch=1
	race2_female_switch=1
	race3_male_switch=0
	race3_female_switch=0
	name_apprentice="Драчливые жеребята-пегасы"
	name_expert="Гвардейцы-пегасы"
	name_retiree="Гвардейцы-пегасы в отставке"
	age_apprentice=$age_teenager
	age_expert=$age_adult
	age_retiree=$age_older
}

function_profession_7 () {
	profession_percent=0.0035
	race1_male_switch=0
	race1_female_switch=0
	race2_male_switch=0
	race2_female_switch=0
	race3_male_switch=1
	race3_female_switch=1
	name_apprentice="Драчливые жеребята-единороги"
	name_expert="Гвардейцы-единороги"
	name_retiree="Гвардейцы-единороги в отставке"
	age_apprentice=$age_teenager
	age_expert=$age_adult
	age_retiree=$age_older
}



#----------------------------
# Опции — алмазные псы

#year_real=1240
#year_max=1300
#year_history=1000
#pony_file=~/pony-population.txt
#
#component_a=0.0115
#coefficient_b=0.000115
#coefficient_c=1.13
#
#c_old_age_mortality_correction=0.04
#a_infant_mortality_correction=0.06
#
#population=40000
#increase_coefficient=1.0035
#fertility_rate=0.035
#
#
#age_teenager=10
#age_adult=15
#age_older=40
#age_fertile_min=15
#age_fertile_max=40
#
#race1_male_name="Алмазные псы самцы"
#race1_male_percent="0.5"
#race1_female_name="Алмазные псы самки"
#race1_female_percent="0.5"
#
#profession_numbers=2
#
#function_profession_1 () {
#	profession_percent=0.2
#	race1_male_switch=1
#	race1_female_switch=1
#	name_apprentice="Воинственные щенки"
#	name_expert="Ополченцы"
#	name_retiree="Ополченцы-ветераны"
#	age_apprentice=$age_teenager
#	age_expert=$age_adult
#	age_retiree=$age_older
#}
#
#function_profession_2 () {
#	profession_percent=0.015
#	race1_male_switch=1
#	race1_female_switch=1
#	name_apprentice="Щенки из воинских родов"
#	name_expert="Королевские стражи"
#	name_retiree="Стражи-ветераны"
#	age_apprentice=$age_teenager
#	age_expert=$age_adult
#	age_retiree=$age_older
#}


#----------------------------
# Опции — зебры

#year_real=1230
#year_max=1300
#year_history=300
#pony_file=~/pony-population.txt
#
#component_a=0.0026
#coefficient_b=0.000122
#coefficient_c=1.11
#
#c_old_age_mortality_correction=0.015
#a_infant_mortality_correction=0.052
#
##year_cataclysm=1280
##a_cataclysm_correction=0.5
#
#population=30000
#increase_coefficient=1.0029
#fertility_rate=0.022
#
#
#age_teenager=10
#age_adult=15
#age_older=50
#age_fertile_min=15
#age_fertile_max=40
#
#race1_male_name="Зебры"
#race1_male_percent="0.44"
#race1_female_name="Зеброчки"
#race1_female_percent="0.56"
#
#profession_numbers=5
#
#function_profession_1 () {
#	profession_percent=0.015
#	race1_male_switch=1
#	race1_female_switch=1
#	name_apprentice="Зебрята из воинских родов"
#	name_expert="Стражи Белой Гавани"
#	name_retiree="Стражи в отставке"
#	age_apprentice=$age_teenager
#	age_expert=$age_adult
#	age_retiree=$age_older
#}
#
#function_profession_2 () {
#	profession_percent=0.003
#	race1_male_switch=1
#	race1_female_switch=1
#	name_apprentice="Послушники Аскари"
#	name_expert="Адепты Аскари"
#	name_retiree="Ветераны Ордена"
#	age_apprentice=$age_teenager
#	age_expert=$age_adult
#	age_retiree=$age_older
#}
#
#function_profession_3 () {
#	profession_percent=0.06
#	race1_male_switch=1
#	race1_female_switch=1
#	name_apprentice="Воинственне зебрята"
#	name_expert="Вооружённые зебры"
#	name_retiree="Вооружённые зебры-старики"
#	age_apprentice=$age_teenager
#	age_expert=$age_adult
#	age_retiree=$age_older
#}
#
#function_profession_4 () {
#	profession_percent=0.08
#	race1_male_switch=1
#	race1_female_switch=1
#	name_apprentice="Юнги"
#	name_expert="Моряки"
#	name_retiree="Моряки в отставке"
#	age_apprentice=$age_teenager
#	age_expert=$age_adult
#	age_retiree=$age_older
#}
#
#function_profession_5 () {
#	profession_percent=0.004
#	race1_male_switch=1
#	race1_female_switch=1
#	name_apprentice="Ученики Академии"
#	name_expert="Схоласты"
#	name_retiree="Философы"
#	age_apprentice=20
#	age_expert=25
#	age_retiree=$age_older
#}
#

#----------------------------
# Опции — импалы.

#year_real=1275
#year_max=1300
#year_history=100
#pony_file=~/pony-population.txt
#
#component_a=0.015
#coefficient_b=0.000123
#coefficient_c=1.46
#
#a_infant_mortality_correction=0.12
#
##year_cataclysm=1280
##a_cataclysm_correction=0.5
#
#population=30000
#increase_coefficient=1.0031
#fertility_rate=0.08
#
#age_teenager=10
#age_adult=12
#age_older=20
#age_fertile_min=12
#age_fertile_max=19
#
#race1_male_name="Импалы-самцы"
#race1_male_percent="0.1"
#race1_female_name="Импалы-самки"
#race1_female_percent="0.9"

#----------------------------
# Опции — львы.

#year_real=1245
#year_max=1300
#year_history=100
#pony_file=~/pony-population.txt
#
#component_a=0.016
#coefficient_b=0.000110
#coefficient_c=1.13
#
#c_old_age_mortality_correction=0.01
#a_infant_mortality_correction=0.08
#
#population=200
#increase_coefficient=1.0027
#fertility_rate=0.045
#
#
#age_teenager=10
#age_adult=13
#age_older=40
#age_fertile_min=13
#age_fertile_max=40
#
#race1_male_name="Львы"
#race1_male_percent="0.2"
#race1_female_name="Львицы"
#race1_female_percent="0.8"
#
#profession_numbers=2
#
#function_profession_1 () {
#	profession_percent=1
#	race1_male_switch=1
#	race1_female_switch=0
#	name_apprentice="Львята-самцы"
#	name_expert="Львы"
#	name_retiree="Старые львы"
#	age_apprentice=0
#	age_expert=$age_adult
#	age_retiree=$age_older
#}
#
#function_profession_2 () {
#	profession_percent=1
#	race1_male_switch=0
#	race1_female_switch=1
#	name_apprentice="Львята-самки"
#	name_expert="Львицы"
#	name_retiree="Старые львицы"
#	age_apprentice=0
#	age_expert=$age_adult
#	age_retiree=$age_older
#}


#----------------------------
# Опции — лемуры

#year_real=1240
#year_max=1300
#year_history=100
#pony_file=~/pony-population.txt
#
#component_a=0.0023
#coefficient_b=0.000121
#coefficient_c=1.13
#
#c_old_age_mortality_correction=0.01
#a_infant_mortality_correction=0.049
#
#population=40000
#increase_coefficient=1.0027
#fertility_rate=0.025
#
#
#age_teenager=10
#age_adult=15
#age_older=50
#age_fertile_min=15
#age_fertile_max=40
#
#race1_male_name="Лемуры-самцы"
#race1_male_percent="0.48"
#race1_female_name="Лемуры-самки"
#race1_female_percent="0.52"


#----------------------------
# Опции — красные панды

#year_real=1220
#year_max=1300
#year_history=300
#pony_file=~/pony-population.txt
#
### Компонент Мейкхама. Независимый от возраста риск:
##component_a=0.0001
### Коэффициент b:
##coefficient_b=0.000113
### Коэффициент c:
##coefficient_c=1.09
#
#component_a=0.001
#coefficient_b=0.000120
#coefficient_c=1.10
#
#c_old_age_mortality_correction=0.02
#a_infant_mortality_correction=0.11
#
#population=20000
#increase_coefficient=1.0032
#fertility_rate=0.021
#
#age_teenager=10
#age_adult=20
#age_older=60
#age_fertile_min=15
#age_fertile_max=50
#
#race1_male_name="Краснопанды"
#race1_male_percent="0.46"
#race1_female_name="Краснопандочки"
#race1_female_percent="0.54"
#
#profession_numbers=1
#
#function_profession_1 () {
#	profession_percent=0.012
#	race1_male_switch=1
#	race1_female_switch=0
#	name_apprentice="Жеребята из чародейских семей"
#	name_expert="Чародеи-новички"
#	name_retiree="Чародеи-мастера"
#	age_apprentice=0
#	age_expert=$age_adult
#	age_retiree=$age_older
#}


#-----------------------------------------------------------------------------
# Начало работы скрипта.

# Очистка используемого файла.
cat /dev/null > $pony_file

# Создание пустых переменных, которые будет использоваться для вычисления общей численности популяции. Иначе basic calculator не хочет с ними работать.
generations_all=0
all_dying=0
# Для распределения возрастов:
population_childs=0
population_teenagers=0
population_adults=0
population_olders=0
# Для вычисления суммарного коэффициента рождаемости:
population_parturition=0
population_race1_fertile_female=0
population_race2_fertile_female=0
population_race3_fertile_female=0
# Для вычисления числа представителей социального слоя:
apprentices=0
experts=0
retirees=0
all_profession1_apprentices=0
all_profession1_experts=0
all_profession1_retirees=0
all_profession2_apprentices=0
all_profession2_experts=0
all_profession2_retirees=0
all_profession3_apprentices=0
all_profession3_experts=0
all_profession3_retirees=0
all_profession4_apprentices=0
all_profession4_experts=0
all_profession4_retirees=0
all_profession5_apprentices=0
all_profession5_experts=0
all_profession5_retirees=0
all_profession6_apprentices=0
all_profession6_experts=0
all_profession6_retirees=0
all_profession7_apprentices=0
all_profession7_experts=0
all_profession7_retirees=0

# Если переменная year_cataclysm не указана в опция, то она равна нулю — то есть не учитывается.
if [ -z $year_cataclysm ]
then
	year_cataclysm=0
fi

if [ -z $c_old_age_mortality_correction ]
then
	c_old_age_mortality_correction=0
fi

if [ -z $a_infant_mortality_correction ]
then
	a_infant_mortality_correction=0
fi

if [ -z $profession_numbers ]
then
	profession_numbers=0
fi


#-----------------------------------------------------------------------------
# Начинается главный цикл скрипта, который выведет общий результат.

# Перебираются годы от минимального значения до максимального.
while [ $year_real -lt $year_max ]
do
	# Увеличивает год (шаг цикла) на один.
	year_real=$(( $year_real + 1 ))
	
	# Вносится историческая поправка. Например: 1300 год н.э. - 300 год н.э. = 1000 лет для прогрессии роста населения.
	if [ $year_real -ge $year_history ]
	then
		year=$(( $year_real - $year_history ))
	else
		echo 'Ошибка: year_real меньше year_history'
		exit
	fi

#-----------------------------------------------------------------------------
# Начинаются вычисления для распределения Гомпертца-Мейкхама.

# Определяется возраст поколения.
age_real=$(( $year_max - $year_real ))

# Вычисляется возраст заставших катаклизм.
age_cataclysm=$(( $year_max - $year_cataclysm ))

# Обнуляется переменные перед каждым циклом вычислений.
result=0
chance_of_dying=0
age=0

# "Рабочие" коэффициенты возвращаются в нормальное значение.
a=$component_a
b=$coefficient_b
c=$coefficient_c

# Внутренний цикл суммирует риски за каждый год жизни поколения. Он продолжается, пока переменные не сравняются.
while [ $age -le $age_real ]
do

	# Для родившихся до катаклизма меняется компонента Мейкхама.
	if [ $age -eq $age_cataclysm ]
	then
		a=`echo "$component_a+$a_cataclysm_correction" | bc`
	else
		a=$component_a
	fi

	# Учитывается младенческая смертность. Правка компоненты Мейкхама.
	if [ $age -eq 0 ]
	then
		a=`echo "$component_a+$a_infant_mortality_correction" | bc`
	else
		a=$component_a
	fi

	# Вычисление с подстановкой возраста. Экспонентальная функция с меняющимся значением age.
	# В вычислениях с дробными числами используется bc — стандартный калькулятор Linux.
	calculate=`echo "$a+$b*($c^$age)" | bc`

	# Если возраст соответствует реальному, шанс умереть записывается в переменную и используется дальше.
	if [ $age -eq $age_real ]
	then
	chance_of_dying=$calculate
	fi

	# К возрасту добавляется один год.
	age=$(( $age + 1 ))

	# Если возраст считается преклонным коэффициент c уменьшается.
	if [ $age -ge $age_older ]
	then
		c=`echo "$coefficient_c-$c_old_age_mortality_correction" | bc`
	fi
	# Результат, это сумма всех калькуляций.
	result=`echo "$result+$calculate" | bc`
done

# Проверка результата цикла. Переменная result должна быть дробным числом меньше 1, так как она обозначает проценты.
result_test=`echo " $result >= 1 " | bc -l`
# Если проверка покажет, что result был больше/равен единице…
if [ $result_test -eq 1  ]
then
	# …Значит выживших в поколении нет. result=1 (100% мертвы).
	result=1
fi

# Точно так же проверяется шанс смерти.
chance_of_dying_test=`echo " $chance_of_dying >= 1 " | bc -l`
if [ $chance_of_dying_test -eq 1  ]
then
	chance_of_dying=1
fi

#-----------------------------------------------------------------------------
# Результат функции Гомпертца используются дальше для определения численности выживших из поколения.

# Геометрическая прогрессия — динамика роста населения. Имеет примерно такой вид:
# 200000*1.0018^(1000-1)=1205803
# Результат умножается на уровень рождаемости:
# 200000*1.0018^(1000-1)*0.016=19293
# что даёт численность поколения, родившегося в нужный год.
generation=`echo "$population*$increase_coefficient^($year-1)*$fertility_rate" | bc`

# Определяется число выживших из годового поколения. Если result=1 даёт ноль.
generation_alive=`echo "$generation*(1-$result)" | bc`

# Высчитывается количество умерших в год.
generation_dying=`echo "scale=5; $generation*$chance_of_dying" | bc -l`

#-----------------------------------------------------------------------------
# Основные вычисления завершены. Теперь можно работать с числом выживших из поколения. Разделить их по половому, расовому, профессиональному признаку и так далее.

# Процент выживших из поколения. scale=5 — параметр для bc, обозначает количество нулей после запятой.
generation_alive_percent=`echo "scale=5; $generation_alive/$generation*100" | bc -l`

# Процент смертности в году.
generation_dying_percent=`echo "scale=5; $chance_of_dying*100" | bc -l`

# Проверка, нужно ли добавлять строку к выводу в файл. Число живых должно быть не равно нулю.
if [ "$generation_alive" != 0 ]
then
	dying_output_string="Умершие: ${generation_dying%.*} ("$generation_dying_percent"%)"
	# Заодно подсчитываеться общее число умерших.
	all_dying=`echo "$all_dying+$generation_dying" | bc -l`
fi

# Результаты в файл. Добавляются построчно с каждым проходом цикла. Конструкции вроде ${generation%.*} используют встроенные в bash регулярные выражения, убирающие лишние цифры после запятой.
echo "Год: $year_real Возраст: $age_real Родившиеся: ${generation%.*} Живые: ${generation_alive%.*} ("$generation_alive_percent"%) $dying_output_string" >> $pony_file


#----------------------------
# Расы:

# Если численность первой расы не нулевая начинается вычисление.
if [ -n "$race1_male_percent" ] && [ -n "$race1_female_percent" ]
then
	# Вычисляется количество представителей расы из поколения.
	generation_race1_male=`echo "$generation_alive*$race1_male_percent" | bc -l`
	generation_race1_female=`echo "$generation_alive*$race1_female_percent" | bc -l`
	# Результат отправляется в файл.
	echo "$race1_male_name: ${generation_race1_male%.*} $race1_female_name: ${generation_race1_female%.*}" >> $pony_file
else 
	# Иначе численность представителей расы в поколении считается нулевой.
	generation_race1_male=0
	generation_race1_female=0
fi

# Теперь проверяется численность второй расы. Если она не на нуле вычисление продолжается.
if [ -n "$race2_male_percent" ] && [ -n "$race2_female_percent" ]
then
	generation_race2_male=`echo "$generation_alive*$race2_male_percent" | bc -l`
	generation_race2_female=`echo "$generation_alive*$race2_female_percent" | bc -l`
	echo "$race2_male_name: ${generation_race2_male%.*} $race2_female_name: ${generation_race2_female%.*}" >> $pony_file
else 
	generation_race2_male=0
	generation_race2_female=0
fi

# И наконец, третья раса.
if [ -n "$race3_male_percent" ] && [ -n "$race3_female_percent" ]
then
	generation_race3_male=`echo "$generation_alive*$race3_male_percent" | bc -l`
	generation_race3_female=`echo "$generation_alive*$race3_female_percent" | bc -l`
	echo "$race3_male_name: ${generation_race3_male%.*} $race3_female_name: ${generation_race3_female%.*}" >> $pony_file
else 
	generation_race3_male=0
	generation_race3_female=0
fi


#----------------------------
# Возрастные группы:

# Дети:
# Если возраст проверяемой группы соответствует возрасту детей, значит выполняется…
if [ $age_real -lt $age_teenager  ]
then
	# …Подсчёт общего числа детей.
	population_childs=`echo "$population_childs+$generation_alive" | bc`
fi

# Подростки:
# Учитывается промежуток, например от 10 до 20 лет.
if [ $age_real -ge $age_teenager -a $age_real -lt $age_adult ]
then
	population_teenagers=`echo "$population_teenagers+$generation_alive" | bc`
fi

# Взрослые:
if [ $age_real -ge $age_adult -a $age_real -lt $age_older ]
then
	population_adults=`echo "$population_adults+$generation_alive" | bc`
fi

# Пожилые:
if [ $age_real -ge $age_older ]
then
	population_olders=`echo "$population_olders+$generation_alive" | bc`
fi


#----------------------------
# Суммарный коэффициент рождаемости. Количество рождённых жеребят одной пони фертильного возраста.

# Определяется возраст, родившиеся до которого будут учитываться в дальнейших вычислениях.
age_parturition=`echo "$age_fertile_max-$age_fertile_min" | bc -l`

# Определяется количество родившихся в период, когда самки расчётной популяции были в фертильном возрасте.
if [ $age_real -lt $age_parturition ]
then
	population_parturition=`echo "$population_parturition+$generation" | bc -l`
fi

# Проверка. Если переменная расы пуста вычисление не выполняется.
if [ -n "$race1_female_percent" ]
then
	# Если возраст поколения соответствует возрасту фертильности, тогда это поколение добавляется к расчётному числу.
	if [ $age_real -ge $age_fertile_min -a $age_real -lt $age_fertile_max ]
	then
		population_race1_fertile_female=`echo "$population_race1_fertile_female+$generation_race1_female" | bc -l`
	fi
else
	population_race1_fertile_female=0
fi

if [ -n "$race2_female_percent" ]
then
	if [ $age_real -ge $age_fertile_min -a $age_real -lt $age_fertile_max ]
	then
		population_race2_fertile_female=`echo "$population_race2_fertile_female+$generation_race2_female" | bc -l`
	fi
else
	population_race2_fertile_female=0
fi

if [ -n "$race3_female_percent" ]
then
	if [ $age_real -ge $age_fertile_min -a $age_real -lt $age_fertile_max ]
	then
		population_race3_fertile_female=`echo "$population_race3_fertile_female+$generation_race3_female" | bc -l`
	fi
else
	population_race3_fertile_female=0
fi

# Вычисляется общее число самок всех рас фертильного возраста:
population_fertile_female=`echo "$population_race1_fertile_female+$population_race2_fertile_female+$population_race3_fertile_female" | bc -l`

# Вычисляется суммарный коэффициент рождаемости:
# Но сначала проверяется, не равна ли популяция фертильных самок нулю.
if [ $population_fertile_female != 0 ]
then
	total_fertility_rate=`echo "scale=3; $population_parturition/$population_fertile_female" | bc -l`
	# Вычисляется общий процент самок всех рас в популяции:
	female_percent=`echo "scale=3; ($generation_race1_female+$generation_race2_female+$generation_race3_female)/$generation" | bc -l`
	# Суммарный коэффициент рождаемости переводится в человеческую форму (то есть в 50/50 распределение полов):
	human_form_total_fertility_rate=`echo "scale=3; ($total_fertility_rate*2)*$female_percent" | bc -l`
fi


#----------------------------
# Социальные слои:

# Первая профессия из списка. Рабочей переменной задаётся начальное значение.
profession_number_begin=1

# Начинается внутренний цикл расчётов для профессий.
while [ $profession_number_begin -le $profession_numbers ]
do
	# Оператор case выбирает: опции для какой профессии учитывать в дальнейшем вычислении.
	case $profession_number_begin in
		1)
			profession_options="function_profession_1"
		;;
		2)
			profession_options="function_profession_2"
		;;
		3)
			profession_options="function_profession_3"
		;;
		4)
			profession_options="function_profession_4"
		;;
		5)
			profession_options="function_profession_5"
		;;
		6)
			profession_options="function_profession_6"
		;;
		7)
			profession_options="function_profession_7"
		;;
	esac

	# Вводятся опции для расчётной профессии (вставляется нужная функция):
	$profession_options

	# Скрипт должен узнать, какие расы учитывать в вычислении. Если переменная в опциях пуста или занулена, число представителей расы считается равным нулю.
	if [ -z "$race1_male_switch" ] || [ $race1_male_switch = 0 ]
	then
		amount_race1_male=0
	else
		amount_race1_male=$generation_race1_male
	fi
	
	if [ -z "$race1_female_switch" ] || [ $race1_female_switch = 0 ]
	then
		amount_race1_female=0
	else
		amount_race1_female=$generation_race1_female
	fi

	if [ -z "$race2_male_switch" ] || [ $race2_male_switch = 0 ]
	then
		amount_race2_male=0
	else
		amount_race2_male=$generation_race2_male
	fi

	if [ -z "$race2_female_switch" ] || [ $race2_female_switch = 0 ]
	then
		amount_race2_female=0
	else
		amount_race2_female=$generation_race2_female
	fi

	if [ -z "$race3_male_switch" ] || [ $race3_male_switch = 0 ]
	then
		amount_race3_male=0
	else
		amount_race3_male=$generation_race3_male
	fi

	if [ -z "$race3_female_switch" ] || [ $race3_female_switch = 0 ]
	then
		amount_race3_female=0
	else
		amount_race3_female=$generation_race3_female
	fi

	# Численность поколений суммируется:
	profession_race=`echo "$amount_race1_male+$amount_race1_female+$amount_race2_male+$amount_race2_female+$amount_race3_male+$amount_race3_female" | bc -l`

	# Проверка. Получившееся число не должно равняться нулю.
	if [ $profession_race != 0 ]
	then
		# Вычисление для выбранных представителей рас.
		# Процентное значение превращается в целое число представителей профессии в поколении:
		generation_profession=`echo "$profession_race*$profession_percent" | bc -l`
	
		# Проверка группы от возраста учеников до возраста мастеров.
		if [ $age_real -ge $age_apprentice -a $age_real -lt $age_expert ]
		then
			# Число учеников в переменную.
			apprentices=$generation_profession
			# Запись в файл. Число учеников под числом подходящего им по возрасту поколения.
			echo "$name_apprentice: ${apprentices%.*}" >> $pony_file
			# Вычисление общего количества учеников.
			case $profession_number_begin in
				1)
					all_profession1_apprentices=`echo "$all_profession1_apprentices+$apprentices" | bc`
				;;
				2)
					all_profession2_apprentices=`echo "$all_profession2_apprentices+$apprentices" | bc`
				;;
				3)
					all_profession3_apprentices=`echo "$all_profession3_apprentices+$apprentices" | bc`
				;;
				4)
					all_profession4_apprentices=`echo "$all_profession4_apprentices+$apprentices" | bc`
				;;
				5)
					all_profession5_apprentices=`echo "$all_profession5_apprentices+$apprentices" | bc`
				;;
				6)
					all_profession6_apprentices=`echo "$all_profession6_apprentices+$apprentices" | bc`
				;;
				7)
					all_profession7_apprentices=`echo "$all_profession7_apprentices+$apprentices" | bc`
				;;
			esac
		fi

		# Проверка группы от возраста мастерства до возраста ухода в отставку.
		if [ $age_real -ge $age_expert -a $age_real -lt $age_retiree ]
		then
			# Число специалистов в переменную.
			experts=$generation_profession
			# Запись в файл числа специалистов.
			echo "$name_expert: ${experts%.*}" >> $pony_file
			# Вычисление общего количества специалистов.
			case $profession_number_begin in
				1)
					all_profession1_experts=`echo "$all_profession1_experts+$experts" | bc`
				;;
				2)
					all_profession2_experts=`echo "$all_profession2_experts+$experts" | bc`
				;;
				3)
					all_profession3_experts=`echo "$all_profession3_experts+$experts" | bc`
				;;
				4)
					all_profession4_experts=`echo "$all_profession4_experts+$experts" | bc`
				;;
				5)
					all_profession5_experts=`echo "$all_profession5_experts+$experts" | bc`
				;;
				6)
					all_profession6_experts=`echo "$all_profession6_experts+$experts" | bc`
				;;
				7)
					all_profession7_experts=`echo "$all_profession7_experts+$experts" | bc`
				;;
			esac
		fi

		# И наконец, проверка группы ветеранов.
		if [ $age_real -ge $age_retiree ]
		then
			# Число ветеранов в переменную.
			retirees=$generation_profession
			# Запись в файл числа ветеранов.
			echo "$name_retiree: ${retirees%.*}" >> $pony_file
			# Вычисление общего количества ветеранов.
			case $profession_number_begin in
				1)
					all_profession1_retirees=`echo "$all_profession1_retirees+$retirees" | bc`
				;;
				2)
					all_profession2_retirees=`echo "$all_profession2_retirees+$retirees" | bc`
				;;
				3)
					all_profession3_retirees=`echo "$all_profession3_retirees+$retirees" | bc`
				;;
				4)
					all_profession4_retirees=`echo "$all_profession4_retirees+$retirees" | bc`
				;;
				5)
					all_profession5_retirees=`echo "$all_profession5_retirees+$retirees" | bc`
				;;
				6)
					all_profession6_retirees=`echo "$all_profession6_retirees+$retirees" | bc`
				;;
				7)
					all_profession7_retirees=`echo "$all_profession7_retirees+$retirees" | bc`
				;;
			esac
		fi
	fi
	# Переход к следующей профессии из списка.
	profession_number_begin=$(( $profession_number_begin + 1 ))
# Завершается внутренний цикл расчётов для профессий.
done


#-----------------------------------------------------------------------------
# Завершается главный цикл, проверяется результат:

# Создаётся разметка в файле.
echo '	***' >> $pony_file

# Суммируются все годовые поколения для проверки общего числа.
generations_all=`echo "$generations_all+$generation_alive" | bc`

# Для проверки сравнением с помощью прогрессии роста вычисляется численность населения.
generations_all_expected=`echo "$population*$increase_coefficient^($year-1)" | bc`

#Проверка, интерактивный вывод в командную строку.
echo "Год: $year_real Сумма поколений: ${generations_all%.*} Численность населения: ${generations_all_expected%.*}"

# Конец главного цикла.
done


#-----------------------------------------------------------------------------
# Вывод данных:

# Вычисление общего процента умерших.
all_dying_percent=`echo "scale=5; $all_dying/$generations_all*100" | bc -l`
# Вычисляется ожидаемый коэффициент смертности (по значениям из опций).
dying_rate_percent=`echo "($fertility_rate-$increase_coefficient+1)*100" | bc -l`

# Вычисление процентного соотношения возрастов.
population_childs_percent=`echo "scale=5; $population_childs/$generations_all*100" | bc -l`
population_teenagers_percent=`echo "scale=5; $population_teenagers/$generations_all*100" | bc -l`
population_adults_percent=`echo "scale=5; $population_adults/$generations_all*100" | bc -l`
population_olders_percent=`echo "scale=5; $population_olders/$generations_all*100" | bc -l`

# Результаты вычислений отправляются в конец файла.
echo "Общие результаты:" >> $pony_file
echo "Сумма поколений: ${generations_all%.*} Численность населения: ${generations_all_expected%.*}" >> $pony_file
echo "Умершие в $year_max году: ${all_dying%.*} Коэффициент смертности: "$all_dying_percent"% (Ожидаемое значение: "$dying_rate_percent"%)" >> $pony_file
# Разделитель
echo "	---" >> $pony_file
# Возрастной состав:
echo "Возрастной состав популяции:" >> $pony_file
echo "Дети младше $age_teenager лет: ${population_childs%.*} (${population_childs_percent%.*}%)" >> $pony_file
echo "Юные $age_teenager-$age_adult лет: ${population_teenagers%.*} (${population_teenagers_percent%.*}%)" >> $pony_file
echo "Взрослые $age_adult-$age_older лет: ${population_adults%.*} (${population_adults_percent%.*}%)" >> $pony_file
echo "Пожилые $age_older+ лет: ${population_olders%.*} (${population_olders_percent%.*}%)" >> $pony_file
# Суммарный коэффициент рождаемости (если нужен):
if [ $population_fertile_female != 0 ]
	then
	echo "На одну самку фертильного возраста приходится $total_fertility_rate детей. Что соответствует $human_form_total_fertility_rate в популяции людей (минимальный показатель воспроизводства населения для стран с низкой смертностью равен 2.1)" >> $pony_file
fi

# Вывод данных о профессиях:
echo "	---" >> $pony_file
# Номеру профессий снова присваивается начальное значение.
profession_number_begin=1
# Цикл обрабатывает все профессии.
while [ $profession_number_begin -le $profession_numbers ]
do
	case $profession_number_begin in
		1)
			# Используются переменные из профессии 1 (для названий)
			profession_options="function_profession_1"
			$profession_options
			# Вывод в файл:
			echo "$name_expert: ${all_profession1_experts%.*} $name_apprentice: ${all_profession1_apprentices%.*} $name_retiree: ${all_profession1_retirees%.*} " >> $pony_file
		;;
		2)
			profession_options="function_profession_2"
			$profession_options
			echo "$name_expert: ${all_profession2_experts%.*} $name_apprentice: ${all_profession2_apprentices%.*} $name_retiree: ${all_profession2_retirees%.*} " >> $pony_file
		;;
		3)
			profession_options="function_profession_3"
			$profession_options
			echo "$name_expert: ${all_profession3_experts%.*} $name_apprentice: ${all_profession3_apprentices%.*} $name_retiree: ${all_profession3_retirees%.*} " >> $pony_file
		;;
		4)
			profession_options="function_profession_4"
			$profession_options
			echo "$name_expert: ${all_profession4_experts%.*} $name_apprentice: ${all_profession4_apprentices%.*} $name_retiree: ${all_profession4_retirees%.*} " >> $pony_file
		;;
		5)
			profession_options="function_profession_5"
			$profession_options
			echo "$name_expert: ${all_profession5_experts%.*} $name_apprentice: ${all_profession5_apprentices%.*} $name_retiree: ${all_profession5_retirees%.*} " >> $pony_file
		;;
		6)
			profession_options="function_profession_6"
			$profession_options
			echo "$name_expert: ${all_profession6_experts%.*} $name_apprentice: ${all_profession6_apprentices%.*} $name_retiree: ${all_profession6_retirees%.*} " >> $pony_file
		;;
		7)
			profession_options="function_profession_7"
			$profession_options
			echo "$name_expert: ${all_profession7_experts%.*} $name_apprentice: ${all_profession7_apprentices%.*} $name_retiree: ${all_profession7_retirees%.*} " >> $pony_file
		;;
	esac
	# Переход к следующей профессии из списка.
	profession_number_begin=$(( $profession_number_begin + 1 ))
done
