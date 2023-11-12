import math

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return area

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        area = self.side ** 2
        return area

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = (self.base * self.height) / 2
        return area

def calculate_and_display_area(figure):
    return figure.calculate_area()

circle = Circle(23)
print(calculate_and_display_area(circle))

