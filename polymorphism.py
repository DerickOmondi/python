class Shape:
    def area(self):
        return 0
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area_of_circle = 3.14 * (self.radius**2)
        return area_of_circle

class Rectangle(Shape):
    def __init__(self,length,width):
        self.width = width
        self.length = length

    def area(self):
        area_of_rectangle = self.length * self.width
        return area_of_rectangle
    

class Triangle(Shape): 
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        area_of_triangle = 0.5 * self.base * self.height
        return area_of_triangle
    

circle1 = Circle(26)

print({circle1.area()}) 
rectangle1 = Rectangle(13,56)

print({rectangle1.area()})

triangle1 = Triangle(50,40)

print({triangle1.area()})


# breaka and continue statements
# regular expressions 
# modules and parameters(importing and use)
# exceptions - try and except