# """

from os import system
system("cls")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the addition operator (+)
    def __add__(self, other_point):
        if isinstance(other_point, Point):
            return Point(self.x + other_point.x, self.y + other_point.y)
        else:
            raise TypeError("Unsupported operand type. Must be a Point.")

    # Overloading the equality operator (==)
    def __eq__(self, other_point):
        if isinstance(other_point, Point):
            return self.x == other_point.x and self.y == other_point.y
        else:
            return False

    # String representation of the object
    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Usage
point1 = Point(1, 2)
point2 = Point(3, 4)

sum_point = point1 + point2
print(sum_point)  # Output: Point(4, 6)

equality_check = (point1 == point2)
print(equality_check)  # Output: False

"""
from os import system
system("cls")

class Point:
    def __init__(self,x, y) -> None:
        self.x=x
        self.y=y
    
    def __add__(self, other):
        if isinstance(other, Point):
            return "+ overloded"
        else:
            return "inappropriate operands"
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return "== overloaded"
        else:
            return "inapprpriate operands"
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
point1=Point(1,2)
point2=Point(5,7)
plus=point1+point2
print(plus)

double_equal=point1==point2
print(double_equal)
"""