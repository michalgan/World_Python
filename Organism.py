from Coordinates import Coordinates


class Organism:
    ADJOINING_TILES = 8

    def __init__(self, y: int, x: int, world):
        self.strength = 0
        self.initiative = 0
        self.symbol = ''
        self.position = Coordinates(y, x)
        self.lastPosition = Coordinates(y, x)
        self.world = world

    def get_y(self) -> int:
        return self.position.y

    def get_x(self) -> int:
        return self.position.x

    def get_strength(self) -> int:
        return self.strength

    def get_initiative(self) -> int:
        return self.initiative

    def get_symbol(self) -> str:
        return self.symbol

    def set_strength(self, value: int):
        self.strength = value

    def set_initiative(self, value: int):
        self.initiative = value

    def info(self):
        print("(S {}, I {}, Y {}, X {})".format(self.strength, self.initiative, self.position.y, self.position.x), end='')

    def action(self):
        pass

    def collision(self, organism):
        pass

    def print_organism(self):
        print(self.symbol, end='')

    def kill(self, killer):
        self.world.delete_organism(self)

    def create_child(self, y: int, x: int):
        return Organism(y, x, self.world)

    def get_adjoining_clear_tile_number(self) -> int:
        obj_y = self.position.y
        obj_x = self.position.x
        counter = 0
        for y in range(obj_y-1, obj_y+2):
            for x in range(obj_x-1, obj_x+2):
                if self.world.coords_valid(y, x) and not self.world.is_occupied(y, x):
                    counter += 1
        return counter

    def get_adjoining_clear_tile_coords(self):
        coords = []
        obj_y = self.position.y
        obj_x = self.position.x
        counter = 0
        for y in range(obj_y-1, obj_y+2):
            for x in range(obj_x-1, obj_x+2):
                if self.world.coords_valid(y, x) and not self.world.is_occupied(y, x):
                    coords.append([y, x])
                    counter += 1
        return coords

    def blocked_attack(self, aggressor):
        return False
