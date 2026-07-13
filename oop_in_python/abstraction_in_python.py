# Build an abstract class Shape with:
    # Abstract method area()
    # Abstract method perimeter()
    # Regular method describe() that prints "I am a {shape_name} with area {area} and perimeter {perimeter}"

    # Then create two child classes:

    # Rectangle — takes width and height
    # Circle — takes radius (use math.pi for π)

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print(f"I am a {self.__class__.__name__} with area {round(self.area(), 2)} and perimeter {round(self.perimeter(), 2)}")

class Rectangle(Shape):
    def __init__(self):
        self.width = float(input("enter width of rectangle: "))
        self.height = float(input("enter height of rectangle: "))

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)
        
    # def describe(self):
    #     super().describe("rectangle", self.area(), self.perimeter())

class Circle(Shape):
    def __init__(self):
        self.radius = float(input("enter radius of circle: "))

    def area(self):
        return math.pi*(self.radius**2)

    def perimeter(self):
        return 2*math.pi*self.radius

rectangle = Rectangle()
rectangle.describe()

circle = Circle()
circle.describe()
