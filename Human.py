from Animal import Animal


class Human(Animal):
    def __init__(self, y, x, world):
        super().__init__(y, x, world)
        self.ability_active = False
        self.ability_available = True
        self.ability_counter = 0
        self.strength = 5
        self.initiative = 4
        self.symbol = 'C'

    def info(self):
        print("Human")
        super().info()

    def action(self):
        self.world.print_world()
        if self.ability_active or not self.ability_available:
            self.ability_counter += 1
            if self.ability_counter == 5:
                self.ability_counter = 0
                if self.ability_active:
                    self.ability_active = False
                    print("Human skill is now inactive")
                else:
                    self.ability_available = True
                    print("Human skill is now available")
        y = self.position.y
        x = self.position.x
        new_y = y
        new_x = x
        made_move = False
        while not made_move:
            zn = input()  # Use appropriate input method to capture user input
            if zn == ' ' and not self.ability_active and self.ability_available:
                print("Human activated skill")
                self.ability_active = True
                self.ability_available = False
            elif zn in ('w', 'a', 's', 'd'):
                if zn == 'w':
                    new_y -= 1
                elif zn == 's':
                    new_y += 1
                elif zn == 'a':
                    new_x -= 1
                elif zn == 'd':
                    new_x += 1
                if self.world.coords_valid(new_y, new_x) and not (y == new_y and x == new_x):
                    self.info()
                    print(f"changed position to ({new_y}, {new_x})")
                    made_move = True
                    if self.world.is_occupied(new_y, new_x):
                        self.collision(self.world.find_organism_on_tile(new_y, new_x))
                    self.position = (new_y, new_x)

    def is_ability_active(self):
        return self.ability_active

    def is_ability_available(self):
        return self.ability_available

    def get_ability_counter(self):
        return self.ability_counter

    def set_ability_active(self, value):
        self.ability_active = value

    def set_ability_available(self, value):
        self.ability_available = value

    def set_ability_counter(self, value):
        self.ability_counter = value

    def blocked_attack(self, aggressor):
        if self.ability_active:
            self.info()
            print("blocked attack of ", end="")
            aggressor.info()
            print(" thanks to Alzur's Shield")
        return self.ability_active
