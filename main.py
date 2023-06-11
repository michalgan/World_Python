from Human import Human
from World import World
import time


def main():
    world = World(10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    human = Human(0, 0, world)
    # world.add_organism(human)
    for i in range(1):
        world.print_world_advanced()
        world.make_turn()
        time.sleep(1)


if __name__ == "__main__":
    main()
