from Plant import Plant


class Wolfberries(Plant):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self.strength = 99
        self.symbol = 'J'

    def create_child(self, y: int, x: int):
        return Wolfberries(y, x, self.world)

    def info(self):
        print("Wolfberries", end="")
        super().info()
