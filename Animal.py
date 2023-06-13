import random
from Coordinates import Coordinates
from Organism import Organism


class Animal(Organism):
    ADJOINING_TILES = 8

    def __init__(self, y: int, x: int, _world):
        super().__init__(y, x, _world)

    def action(self):
        n = self.get_possible_moves_number()
        if n > 0:
            move = random.randint(0, n - 1)
            coords = self.get_possible_moves_coords()
            y, x = coords[move]
            self.make_move(y, x)
            del coords
        else:
            self.info()
            print(" didn't make a move")

    def make_move(self, y: int, x: int):
        self.info()
        print(f" made a move to position ({y}, {x})")
        if self._world.is_occupied(y, x):
            self.collision(self._world.find_organism_on_tile(y, x))
        else:
            self._position = Coordinates(y, x)
            self._world.update_state()

    def collision(self, organism):
        self.info()
        print(" had a collision with ", end="")
        organism.info()
        print()
        if self._symbol == organism.get_symbol():
            self.multiplication(organism)
        else:
            if self._strength < organism.get_strength():
                self.info()
                print(" has been killed by ", end="")
                organism.info()
                print()
                self.kill(organism)
            else:
                self._position = Coordinates(organism.get_y(), organism.get_x())
                self._world.update_state()
                if organism.blocked_attack(self):
                    n = self._get_adjoining_clear_tile_number()
                    coords = self._get_adjoining_clear_tile_coords()
                    move = random.randint(0, n - 1)
                    y, x = coords[move]
                    self.make_move(y, x)
                else:
                    organism.info()
                    print(" has been killed by ", end="")
                    self.info()
                    print()
                    organism.kill(self)

    def multiplication(self, organism):
        y1 = self._position.y
        x1 = self._position.x
        y2 = organism.get_y()
        x2 = organism.get_x()
        possible_tiles = []
        counter = 0
        for y in range(y1 - 1, y1 + 2):
            for x in range(x1 - 1, x1 + 2):
                if (
                    self._world.coords_valid(y, x)
                    and not self._world.is_occupied(y, x)
                    and self._world.adjoining_tiles(y2, x2, y, x)
                ):
                    possible_tiles.append([y, x])
                    counter += 1
        if counter > 0:
            choice = random.randint(0, counter - 1)
            child = self._create_child(possible_tiles[choice][0], possible_tiles[choice][1])
            self._world.add_organism(child)
            print("A new organism has appeared: ", end="")
            child.info()
            print()

    def get_possible_moves_number(self):
        obj_y = self._position.y
        obj_x = self._position.x
        counter = 0
        for y in range(obj_y - 1, obj_y + 2):
            for x in range(obj_x - 1, obj_x + 2):
                if (
                    self._world.coords_valid(y, x)
                    and not (x == obj_x and y == obj_y)
                    and self._position.distance(y, x) < 2
                ):
                    counter += 1
        return counter

    def get_possible_moves_coords(self):
        obj_y = self._position.y
        obj_x = self._position.x
        coords = []
        counter = 0
        for y in range(obj_y - 1, obj_y + 2):
            for x in range(obj_x - 1, obj_x + 2):
                if (
                    self._world.coords_valid(y, x)
                    and not (x == obj_x and y == obj_y)
                    and self._position.distance(y, x) < 2
                ):
                    coords.append([y, x])
                    counter += 1
        return coords
