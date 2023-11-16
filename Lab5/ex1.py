import math
from abc import abstractmethod, ABC


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


if __name__ == '__main__':
    circle = Circle(5)
    print("Circle area: ", circle.area())
    print("Circle perimeter: ", circle.perimeter(), '\n')

    rectangle = Rectangle(14, 25)
    print("Rectangle area: ", rectangle.area())
    print("Rectangle perimeter: ", rectangle.perimeter(), '\n')

    triangle = Triangle(5, 6, 7)
    print("Triangle area: ", triangle.area())
    print("Triangle perimeter: ", triangle.perimeter(), '\n')
