from Animal import Animal


class Sheep(Animal):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self._strength = 4
        self._initiative = 4
        self._symbol = 'O'

    def _create_child(self, y: int, x: int):
        return Sheep(y, x, self._world)

    def info(self):
        print("Sheep", end="")
        super().info()
