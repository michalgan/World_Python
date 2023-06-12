from Human import Human
from World import World
import time


def main():
    world = World(10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    y, x = world.generate_random_position()
    human = Human(y, x, world)
    world.add_organism(human)
    world.print_world_advanced()


if __name__ == "__main__":
    main()
