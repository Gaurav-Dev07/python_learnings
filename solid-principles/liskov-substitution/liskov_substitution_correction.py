from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        pass

    def calculate_area(self,length,width):
        self.length = length
        self.width = width
        return self.length * self.width

class Square(Shape):
    def __init__(self):
        pass
    def calculate_area(self,side):
        self.side = side
        return self.side * self.side

rectangle = Rectangle()
square = Square()

print("square area with length of 4 and width of 5 = ", rectangle.calculate_area(5,4))
print("square with side of length 4 = ", square.calculate_area(4))
    