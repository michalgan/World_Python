from Plant import Plant


class Grass(Plant):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self._strength = 0
        self._symbol = 'T'

    def create_child(self, y: int, x: int):
        return Grass(y, x, self._world)

    def info(self):
        print("Grass", end="")
        super().info()
