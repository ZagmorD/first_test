class torp_air:
    
    def __init__(self, torp_air_numb_plan,torp_air_atack_gr, torp_air_torp,torp_air_speed,torp_air_det_dis):
        self.num_plan = torp_air_numb_plan # общее количество самолётов
        self.atack_gr = torp_air_atack_gr # количество атакующих групп
        self.torp = torp_air_torp # количество торпед на одном самолёте
        self.speed = torp_air_speed # скорость самолёта
        self.det_dis = torp_air_det_dis # дальность обнаружения самолётов
    
    def Attack(self):
        self.atack_gr -= 1 # от общего количества отделяется 1 ударная группа
        self.torp = 0 # сбрасываются торпеды с отделившихся самолётов
        
B7A = torp_air(8, 4, 2, 137, 7)
B7A.Attack()

class avia_torp:
    
    def __init__(self, avia_torp_var, avia_torp_speed, avia_torp_max_dist, avia_torp_dam, avia_torp_det_dist):
        self.var = avia_torp_var # Тип торпед: 0 - обычные, 1 - глубоководные
        self.speed = avia_torp_speed # скорость торпеды, узлов
        self.max_dist = avia_torp_max_dist # дальность хода, км
        self.dam = avia_torp_dam # урон от одной торпеды, ед. 
        self.det_dis = avia_torp_det_dist # дальность обнаружения торпеды, км
    
    def out_of_range(self): # если торпеда не попала, то
        self.speed = 0 # обнуляем её скорость,
        self.dam = 0 # урон и 
        self.det_dis = 0 # дистанцию обнаружения

B7A_torp = avia_torp(0, 40, 3, 4000, 3)
#каким то образом посчитали какое расстояние прошла торпеда и
B7A_torp.out_of_range()
