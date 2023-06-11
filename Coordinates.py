class Coordinates:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x

    def distance(self, y: int, x: int) -> int:
        return abs(self.y - y) + abs(self.x - x)
