# Add these dunder methods to Rectangle:

    # __str__ → returns clean string description
    # __add__ → adds areas of two rectangles and returns total area
    # __eq__ → returns True if two rectangles have same area
    # __gt__ → returns True if this rectangle has bigger area than other

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
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)
        
    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}"

    def __add__(self, other):
        return self.area() + other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

class Circle(Shape):
    def __init__(self):
        self.radius = float(input("enter radius of circle: "))

    def area(self):
        return math.pi*(self.radius**2)

    def perimeter(self):
        return 2*math.pi*self.radius

rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(4, 2)
rectangle3 = Rectangle(1,2)

print(rectangle1)
print(rectangle1 + rectangle2)
print(rectangle1 == rectangle2)
print(rectangle1 > rectangle2)


            
