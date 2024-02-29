#1.1. Siemens Simcenter Femap. Класс – свойство поперечного сечения балки. В свойстве находятся 22 переменных, которые задаёт пользователь: площадь, периметр, различные моменты инерции и прочее. 
#Кроме балок есть ещё другие типы элементов (оболочки, трёхмерные массивы и прочее) и, скорее всего, каждый из этих типов элементов реализован в виде класса со своим набором данных.
#Microsoft Word. Класс – текст. В качестве атрибутов выступают размер текста, его цвет, цвет выделения и другие параметры
#1.2. Игра «Мир кораблей».
class aviation_carrier:
    number_air_attack = 8 # максимальное число самолётов-штурмовиков в ангаре
    numer_air_torpedo = 12 # максимальное число торпедоносцев в ангаре
    number_air_bombers = 18 # максимальное число бомбардировщиков в ангаре
    reload_air_attack = 120 # время респауна штурмовика в ангаре
    reload_air_torpedos = 60 # время респауна торпедоносца в ангаре
    reload_air_bombers = 60 # время респауна бомбардировщика в ангаре
class torpedo_aircraft:
    number_planes = 8 # общее количество самолётов
    number_of_atacking_groups = 4 # количество атакующих групп
    torpedoes = 2 # количество торпед на одном самолёте
    speed = 200 # скорость самолёта
    detection_distance = 8 # дальность обнаружения самолётов
class aviation_torpedoes:
    variant = 'Глубоководные торпеды' #такие торпеды не могут поражать эсминцы
    speed = 67 # скорость торпеды, узлов
    max_distance = 5 # дальность хода, км
    damage = 6000 # урон от одной торпеды, ед. 
    detection_distance = 2.2 # дальность обнаружения, км
    
Nahimov_torpedo_aircraft = torpedo_aircraft ()

Nahimov_torpedo_aircraft.number_planes = 6
Nahimov_torpedo_aircraft.number_of_atacking_groups = 1
print('У авианосца Нахимов', Nahimov_torpedo_aircraft.number_planes, 'торпедоносцев, которые атакуют', Nahimov_torpedo_aircraft.number_of_atacking_groups, 'группой')
#1.3
class torpedo_aircraft:
    number_planes = 8 # общее количество самолётов
    number_of_atacking_groups = 4 # количество атакующих групп
    torpedoes = 2 # количество торпед на одном самолёте
    speed = 200 # скорость самолёта
    detection_distance = 8 # дальность обнаружения самолётов
    
Nahimov = torpedo_aircraft ()

Nahimov.number_planes = 6
Rihtgoffen = Nahimov

Rihtgoffen.number_planes = 4
# побочный эффект - меняем количество торпедоносцев у авианосца Рихтгоффен, а вместе с ним меняеся и количество торпедоносцев авианосца Нахимов
