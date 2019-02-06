class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def x(self):
        return self.x

    def y(self):
        return self.y

    def __add__(self, c):
        return Coordinates(self.x + c.x, self.y + c.y)

    def __sub__(self, c):
        return Coordinates(self.x - c.x, self.y - c.y)

    def __eq__(self, c):
        return self.x == c.x and self.y == c.y

    def to_tuple(self):
        return self.x, self.y
