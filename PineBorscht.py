from Plant import Plant


class PineBorscht(Plant):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self._strength = 10
        self._symbol = 'B'

    def action(self):
        obj_y = self._position.y
        obj_x = self._position.x
        for y in range(obj_y - 1, obj_y + 2):
            for x in range(obj_x - 1, obj_x + 2):
                if (
                    self._world.coords_valid(y, x)
                    and not (y == obj_y and x == obj_x)
                    and self._world.is_occupied(y, x)
                ):
                    organism = self._world.find_organism_on_tile(y, x)
                    organism.info()
                    print(" got poisoned by nearby ", end="")
                    self.info()
                    print()
                    organism.kill(self)

    def info(self):
        print("PineBorscht", end="")
        super().info()

    def _create_child(self, y: int, x: int):
        return PineBorscht(y, x, self._world)
