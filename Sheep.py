from Animal import Animal


class Sheep(Animal):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self.strength = 4
        self.initiative = 4
        self.symbol = 'O'

    def create_child(self, y: int, x: int):
        return Sheep(y, x, self.world)

    def info(self):
        print("Sheep", end="")
        super().info()
