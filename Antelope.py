from Animal import Animal
from Coordinates import Coordinates
import random


class Antelope(Animal):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self.strength = 4
        self.initiative = 4
        self.symbol = 'A'

    def collision(self, organism):
        if (
                self.strength <= organism.get_strength()
                or self.get_adjoining_clear_tile_number() == 0
                or random.randint(0, 1) == 1
        ):
            n = self.get_adjoining_clear_tile_number()
            coords = self.get_adjoining_clear_tile_coords()
            move = random.randint(0, n - 1)
            y, x = coords[move]
            self.position = Coordinates(y, x)
            self.world.update_state()
            self.info()
            print(" escaped from ", end="")
            organism.info()
            print()
        else:
            super().collision(organism)

    def get_possible_moves_number(self):
        obj_y = self.position.y
        obj_x = self.position.x
        counter = 0
        for y in range(obj_y - 1, obj_y + 2):
            for x in range(obj_x - 1, obj_x + 2):
                if self.world.coords_valid(y, x) and not (y == obj_y and x == obj_x):
                    counter += 1
        if self.world.coords_valid(obj_y + 2, obj_x):
            counter += 1
        if self.world.coords_valid(obj_y, obj_x + 2):
            counter += 1
        if self.world.coords_valid(obj_y - 2, obj_x):
            counter += 1
        if self.world.coords_valid(obj_y, obj_x - 2):
            counter += 1
        return counter

    def get_possible_moves_coords(self):
        obj_y = self.position.y
        obj_x = self.position.x
        counter = 0
        coords = []
        for y in range(obj_y - 1, obj_y + 2):
            for x in range(obj_x - 1, obj_x + 2):
                if self.world.coords_valid(y, x) and not (y == obj_y and x == obj_x):
                    coords.append([y, x])
                    counter += 1
        extra_coords = [[obj_y + 2, obj_x], [obj_y, obj_x + 2], [obj_y - 2, obj_x], [obj_y, obj_x - 2]]
        for extra_coord in extra_coords:
            y, x = extra_coord
            if self.world.coords_valid(y, x):
                coords.append([y, x])
                counter += 1
        return coords

    def info(self):
        print("Antelope", end="")
        super().info()