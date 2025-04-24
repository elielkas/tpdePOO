from abc import ABC

class Shape(ABC):
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

class Triangle(Shape):
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur
    def area(self):
            return (self.base * self.hauteur)/2


square = Square(4)
square_area = square.area()
print(square_area)

print("-------------------------")

triangle1 = Triangle(5,7)
triangle_area = triangle1.area()
print(triangle_area)

triangle2 = Triangle(10,15)
triangle_area = triangle2.area()
print(triangle_area)

