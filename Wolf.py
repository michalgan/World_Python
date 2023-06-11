from Animal import Animal


class Wolf(Animal):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self._strength = 9
        self._initiative = 5
        self._symbol = 'W'

    def create_child(self, y: int, x: int):
        return Wolf(y, x, self._world)

    def info(self):
        print("Wolf", end="")
        super().info()
