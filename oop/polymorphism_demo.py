import math

# Base class - Shape
class Shape:
    def area(self):
        """A method that should be overridden by derived classes."""
        raise NotImplementedError("Subclasses must implement this method")

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initializes the attributes of a Rectangle."""
        self.length = length
        self.width = width

    def area(self):
        """Overrides the base class method to calculate the area of a Rectangle."""
        return self.length * self.width

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initializes the attributes of a Circle."""
        self.radius = radius

    def area(self):
        """Overrides the base class method to calculate the area of a Circle."""
        return math.pi * (self.radius ** 2)
