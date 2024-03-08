# Задание 5.1
class torp_air:
    
    def __init__(self, torp_air_numb_plan,torp_air_atack_gr, torp_air_torp,torp_air_speed,torp_air_det_dis):
        self.__num_plan = torp_air_numb_plan # общее количество самолётов
        self.__atack_gr = torp_air_atack_gr # количество атакующих групп
        self.__torp = torp_air_torp # количество торпед на одном самолёте
        self.__speed = torp_air_speed # скорость самолёта
        self.__det_dis = torp_air_det_dis # дальность обнаружения самолётов
    
    def __Attack__(self): #в питон тьюторе для создания праватного метода 2 подчёркивания нужны не только в начале, но и в конце
        self.__atack_gr -= 1 # от общего количества отделяется 1 ударная группа
        self.__torp = 0 # сбрасываются торпеды с отделившихся самолётов
        
B7A = torp_air(8, 4, 2, 137, 7)
B7A.__Attack__()

# Задание 5.2
# Первая пара классов с наследованием
class aviation:
    def __init__(self,air_numb_plan, air_atack_gr, air_speed, air_weapon, air_height):
        self.num_plan = air_numb_plan # общее количество самолётов
        self.atack_gr = air_atack_gr # количество атакующих групп
        self.speed = air_speed # скорость самолёта
        self.weapon = air_weapon # количество вооружения на одном самолёте
        self.height = air_height # высота полёта

    def prepare_Attack(self):
        self.atack_gr -= 1 # от общего количества отделяется 1 ударная группа

    def weapon_launch(self):
        self.weapon = 0 # отделяется вооружение с ударной группы самолётов


class torp_air(aviation):

    def __init__(self, torpedos, air_numb_plan,air_atack_gr, air_speed, air_weapon, air_det_dis):
        super().__init__(air_numb_plan,air_atack_gr, air_speed, air_weapon, air_det_dis)
        self.type_weapon = torpedos
    
    def torpedos_attack(self):
        self.speed = 60
        self.height = 10

class bomb_air(aviation):
    
    def __init__(self, bombs, air_numb_plan,air_atack_gr, air_speed, air_weapon, air_det_dis):
        super().__init__(air_numb_plan,air_atack_gr, air_speed, air_weapon, air_det_dis)
        self.type_weapon = bombs
    
    def bombers_attack(self):
        self.speed = 400
        self.height = 500

        
B7A = torp_air('Торпеды', 4, 2, 137, 2, 200)
B7A.prepare_Attack() # группа отделяется для удара
B7A.torpedos_attack() # выполняет заход
B7A.weapon_launch() # и сбрасывает торпеды

B7A = bomb_air('Бомбы', 12, 4, 170, 4, 200)
B7A.prepare_Attack() # группа отделяется для удара
B7A.bombers_attack() # выполняет заход
B7A.weapon_launch() # и сбрасывает бомбы

# Вторая пара классов с наследованием
class animal_transport_container: # просто переноска
    def __init__(self, l, t, h, g, name_animal):
        self.dlina = l 
        self.shirina = t 
        self.visota = h
        self.napolnennost = g # 0 - переноска пуста, 1 - в переноске животное
        self.name = name_animal # Имя того, кто сидит в переноске
        
    def zahvat(self, name_animal):
        if self.napolnennost == 0:
            self.napolnennost = 1
            self.name = name_animal

class dragon_container(animal_transport_container): # переноска для дракона
    def __init__(self, ne_gorit, l, t, h, g, name_animal):
        super().__init__(l, t, h, g, name_animal)
        self.ne_gorit = ne_gorit
        
    def rename_dragon(self):
        self.name = 'Иннокентий'
        
class cat_container(animal_transport_container): # переноска для кота
    def rename_cat(self):
        self.name = 'Андрей'    

kletka1 = dragon_container('Yes', 100, 100, 100, 0, '')
kletka1.zahvat('Андрей') # захватываем дракона Андрей
kletka1.rename_dragon() # и переименовываем его в Иннокентия
kletkaI = cat_container(100, 100, 100, 0, '')
kletkaI.zahvat('Иннокентий') # захватываем кота Иннокентия
kletkaI.rename_cat() # и переименовываем его в Андрея
