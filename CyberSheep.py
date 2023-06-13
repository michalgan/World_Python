from Sheep import Sheep


class CyberSheep(Sheep):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self._strength = 11
        self._symbol = 'X'

    def info(self):
        print("Cyber", end="")
        super().info()

    def get_possible_moves_number(self):
        if self._find_nearest_pine_borscht() is not None:
            return 1
        else:
            return super().get_possible_moves_number()

    def get_possible_moves_coords(self):
        if self._find_nearest_pine_borscht() is not None:
            y, x = self._find_nearest_pine_borscht()
            y -= self._position.y
            x -= self._position.x
            result = []
            if y != 0:
                if y > 0:
                    result.append([self._position.y+1, self._position.x])
                else:
                    result.append([self._position.y-1, self._position.x])
            else:
                if x > 0:
                    result.append([self._position.y, self._position.x+1])
                else:
                    result.append([self._position.y, self._position.x-1])
            return result
        else:
            return super().get_possible_moves_coords()

    def _find_nearest_pine_borscht(self):
        min_distance = float('inf')
        nearest_y, nearest_x = None, None

        for y in range(self._world.get_size_y()):
            for x in range(self._world.get_size_x()):
                if not self._world.is_occupied(y, x):
                    continue
                else:
                    organism = self._world.find_organism_on_tile(y, x)
                    if organism != 0 and organism.get_symbol() == 'B':
                        distance = abs(y - self._position.y) + abs(x - self._position.x)
                        if distance < min_distance:
                            min_distance = distance
                            nearest_y = y
                            nearest_x = x

        if nearest_y is not None and nearest_x is not None:
            return [nearest_y, nearest_x]
        else:
            return None

    def kill(self, killer):
        if killer.get_symbol() != 'B':
            super().kill(killer)

    def _create_child(self, y: int, x: int):
        return CyberSheep(y, x, self._world)
