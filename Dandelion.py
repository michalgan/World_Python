from Plant import Plant


class Dandelion(Plant):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self._strength = 0
        self._symbol = 'M'

    def action(self):
        for _ in range(3):
            super().action()

    def info(self):
        print("Dandelion", end="")
        super().info()

    def _create_child(self, y: int, x: int):
        return Dandelion(y, x, self._world)
