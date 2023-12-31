from Animal import Animal
import random


class Turtle(Animal):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self._strength = 2
        self._initiative = 1
        self._symbol = 'Z'

    def action(self):
        if random.randint(0, 4) == 0:
            super().action()

    def collision(self, organism):
        if organism.get_strength() >= 5:
            super().collision(organism)

    def info(self):
        print("Turtle", end="")
        super().info()

    def blocked_attack(self, aggressor):
        if aggressor.get_strength() < 5:
            self.info()
            print(" blocked an attack of ", end="")
            aggressor.info()
            print()
        return aggressor.get_strength() < 5

    def _create_child(self, y: int, x: int):
        return Turtle(y, x, self._world)
