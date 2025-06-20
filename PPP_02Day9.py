## Build a Rectangle class with length and width, and a method to compute area
class Rectangle:
    def __init__(self, length, breadth):
        self.len = length
        self.bre = breadth

    def Calculate_area(self):
        return self.len * self.bre
    
a =Rectangle(3,4)
print("The area of rectangle is", a.Calculate_area())        