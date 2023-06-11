import random
import tkinter as tk
import json

from Antelope import Antelope
from Dandelion import Dandelion
from Fox import Fox
from Grass import Grass
from Guarana import Guarana
from PineBorscht import PineBorscht
from Sheep import Sheep
from Turtle import Turtle
from Wolf import Wolf
from Wolfberries import Wolfberries

ANIMAL_SPECIES_NUMBER = 5
ORGANISMS_NUMBER_LIMIT = 200


class World:
    def __init__(self, size_y, size_x):
        self.size_y = size_y
        self.size_x = size_x
        self.turn_counter = 1
        self.occupied = [[False] * size_x for _ in range(size_y)]
        self.organisms = []

    def __init__(self, size_y, size_x, antelopes, foxes, sheep, turtles, wolves,
                 dandelions, grasses, guaranas, pine_borschtes, wolf_berries):

        self.turn_counter = 1
        self.size_y = size_y
        self.size_x = size_x
        self.occupied = [[False] * size_x for _ in range(size_y)]
        self.organisms = []

        self.root = tk.Tk()
        self.root.title("World")
        self.canvas = tk.Canvas(self.root, width=self.size_x * 20, height=self.size_y * 20)
        self.canvas.pack()

        def next_turn():
            self.make_turn()
            self.print_world_advanced()

        button = tk.Button(self.root, text="Next turn", command=next_turn)
        button.pack()

        button = tk.Button(self.root, text="Save", command=self.save)
        button.pack()

        button = tk.Button(self.root, text="Load", command=self.load)
        button.pack()

        for i in range(antelopes):
            y, x = self.generate_random_position()
            self.add_organism(Antelope(y, x, self))

        for i in range(foxes):
            y, x = self.generate_random_position()
            self.add_organism(Fox(y, x, self))

        for i in range(sheep):
            y, x = self.generate_random_position()
            self.add_organism(Sheep(y, x, self))

        for i in range(turtles):
            y, x = self.generate_random_position()
            self.add_organism(Turtle(y, x, self))

        for i in range(wolves):
            y, x = self.generate_random_position()
            self.add_organism(Wolf(y, x, self))

        for i in range(dandelions):
            y, x = self.generate_random_position()
            self.add_organism(Dandelion(y, x, self))

        for i in range(grasses):
            y, x = self.generate_random_position()
            self.add_organism(Grass(y, x, self))

        for i in range(guaranas):
            y, x = self.generate_random_position()
            self.add_organism(Guarana(y, x, self))

        for i in range(pine_borschtes):
            y, x = self.generate_random_position()
            self.add_organism(PineBorscht(y, x, self))

        for i in range(wolf_berries):
            y, x = self.generate_random_position()
            self.add_organism(Wolfberries(y, x, self))

    def generate_random_position(self):
        y = random.randint(0, self.size_y - 1)
        x = random.randint(0, self.size_x - 1)
        while self.occupied[y][x]:
            y = random.randint(0, self.size_y - 1)
            x = random.randint(0, self.size_x - 1)
        return y, x

    def create_animals(self, n):
        for _ in range(n):
            choice = random.randint(0, ANIMAL_SPECIES_NUMBER)
            y = random.randint(0, self.size_y - 1)
            x = random.randint(0, self.size_x - 1)
            while self.occupied[y][x]:
                y = random.randint(0, self.size_y - 1)
                x = random.randint(0, self.size_x - 1)
            if choice == 0:
                self.add_organism(Antelope(y, x, self))
            elif choice == 1:
                self.add_organism(Fox(y, x, self))
            elif choice == 2:
                self.add_organism(Sheep(y, x, self))
            elif choice == 3:
                self.add_organism(Turtle(y, x, self))
            elif choice == 4:
                self.add_organism(Wolf(y, x, self))
            else:
                print("No such an animal...")

    def create_plants(self, n):
        for _ in range(n):
            choice = random.randint(0, ANIMAL_SPECIES_NUMBER)
            y = random.randint(0, self.size_y - 1)
            x = random.randint(0, self.size_x - 1)
            while self.is_occupied(y, x):
                y = random.randint(0, self.size_y - 1)
                x = random.randint(0, self.size_x - 1)
            if choice == 0:
                self.add_organism(Dandelion(y, x, self))
            elif choice == 1:
                self.add_organism(Grass(y, x, self))
            elif choice == 2:
                self.add_organism(Guarana(y, x, self))
            elif choice == 3:
                self.add_organism(PineBorscht(y, x, self))
            elif choice == 4:
                self.add_organism(Wolfberries(y, x, self))
            else:
                print("No such a plant...")

    def make_turn(self):
        self.organisms = sorted(self.organisms, key=lambda item: item.get_initiative(), reverse=True)
        self.turn_counter += 1
        counter = 0
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.is_occupied(y, x):
                    counter += 1
        for organism in self.organisms:
            organism.action()
            self.update_state()

    def print_world(self):
        print("\n\nName: Michal,\tSurname: Ganczarenko\tIndex nr: 188818")
        print(f"Turn nr: {self.turn_counter}")
        print("+", end="")
        for _ in range(self.size_y):
            print("--", end="")
        print("-+")
        for y in range(self.size_y):
            print("|", end="")
            for x in range(self.size_x):
                print(" ", end="")
                if self.occupied[y][x]:
                    self.find_organism_on_tile(y, x).print_organism()
                else:
                    print(" ", end="")
            print(" |")
        print("+", end="")
        for _ in range(self.size_y):
            print("--", end="")
        print("-+")

    def print_world_advanced(self):
        self.canvas.delete("all")

        for y in range(self.size_y):
            for x in range(self.size_x):
                x1 = x * 20
                y1 = y * 20
                x2 = x1 + 20
                y2 = y1 + 20

                if self.occupied[y][x]:
                    organism = self.find_organism_on_tile(y, x)
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
                    self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=organism.get_symbol())
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")

        self.root.update()
        self.root.mainloop()

    def coords_valid(self, y, x):
        return 0 <= y < self.size_y and 0 <= x < self.size_x

    def is_occupied(self, y, x):
        return self.occupied[y][x]

    def update_state(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.occupied[y][x] = self.find_organism_on_tile(y, x) != 0

    def find_organism_on_tile(self, y, x):
        for organism in self.organisms:
            org_y = organism.get_y()
            org_x = organism.get_x()
            if y == org_y and x == org_x:
                return organism
        return 0

    def add_organism(self, organism):
        if len(self.organisms) < ORGANISMS_NUMBER_LIMIT:
            self.organisms.append(organism)
            self.update_state()
        else:
            print('To many organisms to add one more')

    def delete_organism(self, organism):
        index = self.organisms.index(organism)
        self.organisms.pop(index)

    def find_human_index(self):
        for organism in self.organisms:
            if organism.__class__.__name__ == 'Human':
                return self.organisms.index(organism)
            else:
                return -1

    def load(self):
        filename = input('Input filename: ')
        file = open(filename+'.txt', 'r')
        data = dict(json.loads(file.read()))
        file.close()
        print(data)



    def save(self):
        filename = input('Input filename: ')
        with open(filename + '.txt', "w") as file:
            file.write('{')
            file.write(f"sizeY:{self.size_y},sizeX:{self.size_x},")
            human_index = self.find_human_index()
            if human_index != -1:
                human = self.organisms[human_index]
                file.write(
                    f"human_ability_active:{int(human.is_ability_active())},"
                    f"human_ability_available:{int(human.is_ability_available())},"
                    f"human_ability_counter:{human.get_ability_counter()},")
            else:
                file.write("human_ability_active:-1,human_ability_available:-1,human_ability_counter:-1,")

            file.write("Organisms:[")
            for i in range(len(self.organisms) - 1, -1, -1):
                organism = self.organisms[i]
                file.write("{")
                file.write(
                    f"symbol:{organism.get_symbol()},y:{organism.get_y()},x:{organism.get_x()},"
                    f"strength:{organism.get_strength()},initiative:{organism.get_initiative()}")

                file.write("}")
                if i != 0:
                    file.write(",")

            file.write("]}")
        print('Saved')

    @staticmethod
    def adjoining_tiles(y1, x1, y2, x2):
        return abs(x1 - x2) + abs(y1 - y2) < 2 or (abs(x1 - x2) == 1 and abs(y1 - y2))
