from math import pi, sqrt

class Shape:
    def __init__(self, side1, side2):
        print("this is shape's constructor")
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        return self.side1 * self.side2
    
    def __str__(self):
        return f'The area of this {self.__class__.__name__} is: {self.get_area()}'
    
# inheritance
# this class is inherting from parent class
class Rectangle(Shape):
    pass

rectangle= Rectangle(4,5)
print(rectangle.__str__())

# polymorphism 
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

square = Square(4)
print(square)

# implementing triangle class
class Triangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)
        
    def get_area(self):
        area = super().get_area()
        return area / 2

triangle = Triangle(2,4)

print(triangle)

class Circle(Square):
    def __init__(self, radius):
        super().__init__(radius)

    def get_area(self):
       area =  super().get_area()
       return (22/7) * area
    
circle = Circle(10);
print(circle)

# doc solution method overriding
class Circle2(Shape):
	def __init__(self, radius):
		self.radius = radius
 
	def get_area(self):
		return pi * (self.radius ** 2)

circle2 = Circle2(10)
print(circle2)


class Hexagon(Rectangle):
	
	def get_area(self):
		return (3 * sqrt(3) * self.side1 ** 2) / 2
hexagon = Hexagon(6)
print(hexagon)