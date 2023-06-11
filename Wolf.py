from Animal import Animal


class Wolf(Animal):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self.strength = 9
        self.initiative = 5
        self.symbol = 'W'

    def create_child(self, y: int, x: int):
        return Wolf(y, x, self.world)

    def info(self):
        print("Wolf", end="")
        super().info()
