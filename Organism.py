from Coordinates import Coordinates


class Organism:
    ADJOINING_TILES = 8

    def __init__(self, y: int, x: int, world):
        self._strength = 0
        self._initiative = 0
        self._symbol = ''
        self._position = Coordinates(y, x)
        self._world = world

    def get_y(self) -> int:
        return self._position.y

    def get_x(self) -> int:
        return self._position.x

    def get_strength(self) -> int:
        return self._strength

    def get_initiative(self) -> int:
        return self._initiative

    def get_symbol(self) -> str:
        return self._symbol

    def set_strength(self, value: int):
        self._strength = value

    def set_initiative(self, value: int):
        self._initiative = value

    def info(self):
        print("(S {}, I {}, Y {}, X {})".format(self._strength, self._initiative, self._position.y,
                                                self._position.x), end='')

    def action(self):
        pass

    def collision(self, organism):
        pass

    def print_organism(self):
        print(self._symbol, end='')

    def kill(self, killer):
        self._world.delete_organism(self)

    def _create_child(self, y: int, x: int):
        return Organism(y, x, self._world)

    def _get_adjoining_clear_tile_number(self) -> int:
        obj_y = self._position.y
        obj_x = self._position.x
        counter = 0
        for y in range(obj_y-1, obj_y+2):
            for x in range(obj_x-1, obj_x+2):
                if self._world.coords_valid(y, x) and not self._world.is_occupied(y, x):
                    counter += 1
        return counter

    def _get_adjoining_clear_tile_coords(self):
        coords = []
        obj_y = self._position.y
        obj_x = self._position.x
        counter = 0
        for y in range(obj_y-1, obj_y+2):
            for x in range(obj_x-1, obj_x+2):
                if self._world.coords_valid(y, x) and not self._world.is_occupied(y, x):
                    coords.append([y, x])
                    counter += 1
        return coords

    def blocked_attack(self, aggressor):
        return False
