class torp_air():

    def __init__(self, air_numb_plan,air_atack_gr, air_speed, air_weapon, air_height, torpedos):
        self.num_plan = air_numb_plan # общее количество самолётов
        self.atack_gr = air_atack_gr # количество атакующих групп
        self.speed = air_speed # скорость самолёта
        self.weapon = air_weapon # количество вооружения на одном самолёте
        self.height = air_height # высота полёта
        self.type_weapon = torpedos
    
    def torpedos_attack(self):
        self.speed = 60
        self.height = 10

class bomb_air():
    
    def __init__(self, air_numb_plan,air_atack_gr, air_speed, air_weapon, air_height, bombs):
        self.num_plan = air_numb_plan # общее количество самолётов
        self.atack_gr = air_atack_gr # количество атакующих групп
        self.speed = air_speed # скорость самолёта
        self.weapon = air_weapon # количество вооружения на одном самолёте
        self.height = air_height # высота полёта
        self.type_weapon = bombs
    
    def bombers_attack(self):
        self.speed = 400
        self.height = 500
        
class aviacareer():

    def __init__(self, air_numb_plan, air_atack_gr, air_speed, air_weapon, air_height, torpedos):
        self.torp_air = torp_air(self, air_numb_plan,air_atack_gr, air_speed, air_weapon, air_height, torpedos)
        sels.bomb_air = bomb_air(self, air_numb_plan,air_atack_gr, air_speed, air_weapon, air_height, bombs)       

    def prepare_Attack(self):
        self.atack_gr -= 1 # от общего количества отделяется 1 ударная группа

    def weapon_launch(self):
        self.weapon = 0 # отделяется вооружение с ударной группы самолётов

B7A = aviacareer(4, 2, 137, 2, 200, 'Торпеды')
B7A.prepare_Attack() # группа отделяется для удара
B7A.torpedos_attack() # выполняет заход
B7A.weapon_launch() # и сбрасывает торпеды

  
