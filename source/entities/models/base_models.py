#объекты для наследования
import copy

#todo: добавить пайгейм
class Bacteria:
    division_coefficient: float = .75
    division_timer: float = 1

    def __init__(self):
        self.network = Network()
        self.max_energy = 100
        self.energy = self.max_energy
        self.speed = 1
        self.position: None #vector
        # self.resistance = 0.01
        self.energy_coefficient = 1
        self.last_divided = 0 # time

    def can_divide(self, current_time):
        return (self.max_energy * self.division_coefficient <= self.energy
                and current_time >= self.last_divided + self.division_timer)

    def divide(self):
        self.energy /= 2
        #перемещение при делении
        return copy.copy(Bacteria)


    def mutate(self):
        ...
