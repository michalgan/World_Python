from Animal import Animal
from Coordinates import Coordinates


class Human(Animal):
    def __init__(self, y, x, world):
        super().__init__(y, x, world)
        self._ability_active = False
        self._ability_available = True
        self._ability_counter = 0
        self._strength = 5
        self._initiative = 4
        self._symbol = 'C'

    def info(self):
        print("Human", end='')
        super().info()

    def action(self):
        if self._ability_active or not self._ability_available:
            self._ability_counter += 1
            if self._ability_counter == 5:
                self._ability_counter = 0
                if self._ability_active:
                    self._ability_active = False
                    print("Human skill is now inactive")
                else:
                    self._ability_available = True
                    print("Human skill is now available")
        y = self._position.y
        x = self._position.x
        new_y = y
        new_x = x
        made_move = False
        self._world.update_state()
        while not made_move:
            zn = input()
            if zn == ' ' and not self._ability_active and self._ability_available:
                print("Human activated skill")
                self._ability_active = True
                self._ability_available = False
            elif zn == ' ':
                made_move = True
            elif zn in ('w', 'a', 's', 'd'):
                if zn == 'w':
                    new_y -= 1
                elif zn == 's':
                    new_y += 1
                elif zn == 'a':
                    new_x -= 1
                elif zn == 'd':
                    new_x += 1
                if self._world.coords_valid(new_y, new_x) and not (y == new_y and x == new_x):
                    self.info()
                    print(f"changed position to ({new_y}, {new_x})")
                    made_move = True
                    if self._world.is_occupied(new_y, new_x):
                        self.collision(self._world.find_organism_on_tile(new_y, new_x))
                    self._position = Coordinates(new_y, new_x)

    def is_ability_active(self):
        return self._ability_active

    def is_ability_available(self):
        return self._ability_available

    def get_ability_counter(self):
        return self._ability_counter

    def set_ability_active(self, value):
        self._ability_active = value

    def set_ability_available(self, value):
        self._ability_available = value

    def set_ability_counter(self, value):
        self._ability_counter = value

    def blocked_attack(self, aggressor):
        if self._ability_active:
            self.info()
            print("blocked attack of ", end="")
            aggressor.info()
            print(" thanks to Alzur's Shield")
        return self._ability_active
