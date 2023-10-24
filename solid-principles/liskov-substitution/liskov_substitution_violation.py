# subclass objects should be able to substitue bases class object

class Shape:
    def __init__(self,side1,side2):
        self.side1 = side1
        self.side2 = side2
    
    def calculate_area(self):
        return self.side1 * self.side2

class Rectangle(Shape):
    def __init__(self,length,breadth):
        super().__init__(length,breadth)
        
class Square(Shape):
    def __init__(self,side):
        super().__init__(side,side)
    
rectangle = Rectangle(4,3)
print("area = ", rectangle.calculate_area())
square = Square(4)
print("area = ",square.calculate_area())

# here by this design we are able to calculate area but we this design violates liskov substitution principle