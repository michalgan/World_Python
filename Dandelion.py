from Plant import Plant


class Dandelion(Plant):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self.strength = 0
        self.symbol = 'M'

    def action(self):
        for _ in range(3):
            super().action()

    def create_child(self, y: int, x: int):
        return Dandelion(y, x, self.world)

    def info(self):
        print("Dandelion", end="")
        super().info()
