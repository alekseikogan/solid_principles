# Open/Closed Principle (OCP)

# Нарушение приниципа
# При добавлении новой фигуры (например, треугольника) нужно изменять метод calculate_area.
class BadShapeCalculator:
    def calculate_area(self, shape, *args):
        if shape == "circle":
            radius = args[0]
            return 3.14 * radius ** 2
        elif shape == "rectangle":
            width, height = args
            return width * height


# Правильное решение
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class ShapeCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()


# Использование
circle = Circle(5)
rectangle = Rectangle(4, 6)
calculator = ShapeCalculator()
print(calculator.calculate_area(circle))  # 78.5
print(calculator.calculate_area(rectangle))  # 24
