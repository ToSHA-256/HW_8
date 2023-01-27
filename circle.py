class Point():
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_r = abs(self.radius - other.radius)
        return Circle(new_x, new_y, new_r) if new_r else Point(new_x, new_y)


one = Circle(1, 1, 5)
two = Circle(2, 2, 4)
third = Circle(-1, -1, 1)
sub = one.__sub__(two)
print(f"Результат вычитания {type(sub)}: \n{sub.__dict__}")
point = sub.__sub__(third)
print(f"Результат вычитания {type(point)}: \n{point.__dict__}")
