from Plant import Plant


class Grass(Plant):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self.strength = 0
        self.symbol = 'T'

    def create_child(self, y: int, x: int):
        return Grass(y, x, self.world)

    def info(self):
        print("Grass", end="")
        super().info()
