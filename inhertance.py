import math
class Shape:
    pass
    
class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius **2
    
    def perimeter(self):
        return 2*math.pi*self.radius
    
class Square(Shape):
    def __init__(self,side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length**2
    
    def perimeter(self):
        return 4* self.side_length

circle = Circle(5)
print(circle.area())
square = Square(4)
print(square.perimeter())

