from Animal import Animal
import random


class Fox(Animal):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self._strength = 3
        self._initiative = 7
        self._symbol = 'L'

    def _create_child(self, y: int, x: int):
        return Fox(y, x, self._world)

    def action(self):
        n = self.get_possible_moves_number()
        if n > 0:
            counter = 0
            coords = self.get_possible_moves_coords()
            new_coords = []
            for i in range(n):
                y, x = coords[i]
                if not (self._world.is_occupied(y, x)
                        and self._world.find_organism_on_tile(y, x).get_strength() > self._strength):
                    new_coords.append([y, x])
                    counter += 1
            if counter > 0:
                move = random.randint(0, counter - 1)
                y, x = new_coords[move]
                self.make_move(y, x)
            else:
                self.info()
                print(" didn't make a move")
        else:
            self.info()
            print(" didn't make a move")

    def info(self):
        print("Fox", end="")
        super().info()
