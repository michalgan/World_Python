from Plant import Plant


class Guarana(Plant):
    def __init__(self, y: int, x: int, world):
        super().__init__(y, x, world)
        self.strength = 0
        self.symbol = 'G'

    def create_child(self, y: int, x: int):
        return Guarana(y, x, self.world)

    def info(self):
        print("Guarana", end="")
        super().info()

    def kill(self, killer):
        killer.set_strength(killer.get_strength() + 3)
        self.info()
        print(" increased the strength of ", end="")
        killer.info()
        print(" by 3")
        super().kill(killer)
