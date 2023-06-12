from random import randint

from Organism import Organism


class Plant(Organism):
    PROBABILITY = 0.01

    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self.initiative = 0

    def action(self):
        n = self._get_adjoining_clear_tile_number()
        coords = self._get_adjoining_clear_tile_coords()
        if n > 0 and randint(0, 99) < 100 * self.PROBABILITY:
            move = randint(0, n - 1)
            y, x = coords[move]
            child = self._create_child(y, x)
            print("A new organism has shown: ", end="")
            child.info()
            print()
            self._world.add_organism(child)
