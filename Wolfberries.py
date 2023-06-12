from Plant import Plant


class Wolfberries(Plant):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self._strength = 99
        self._symbol = 'J'

    def _create_child(self, y: int, x: int):
        return Wolfberries(y, x, self._world)

    def info(self):
        print("Wolfberries", end="")
        super().info()
