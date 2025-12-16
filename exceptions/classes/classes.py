class Point:
    defualt_color = "red"

    def __init__(self, x, y):  # Constructor, one of the magic methods
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordinates must be numeric values.")
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, value) -> bool:
        return self.x == value.x and self.y == value.y

    def __gt__(self, value) -> bool:
        return (self.x, self.y) > (value.x, value.y)

    def __lt__(self, value) -> bool:
        return (self.x, self.y) < (value.x, value.y)

    def __ge__(self, value) -> bool:
        return (self.x, self.y) >= (value.x, value.y)

    def __le__(self, value) -> bool:
        return (self.x, self.y) <= (value.x, value.y)

    def __ne__(self, value) -> bool:
        return not self.__eq__(value)

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# Magic Mthods here https://rszalski.github.io/magicmethods/

point = Point(1, 2)
print("str", point)  # This will call the __str__ method
point.draw()
point_zero = Point.zero()
print(point_zero.draw())

# Magic Method
point = Point(1, 2)
print("str", point)  # This will call the __str__ method

# Object comparison
point1 = Point(1, 2)
point2 = Point(3, 4)
# This will call the __eq__ method if defined
print("point1 == point2:", point1 == point2)
print("point1 != point2:", point1 != point2)
print("point1 > point2:", point1 > point2)
print("point1 < point2:", point1 < point2)
print("point1 >= point2:", point1 >= point2)
print("point1 <= point2:", point1 <= point2)


# Arithmetic operations
point3 = Point(5, 6)
point4 = Point(2, 3)
print("point3 + point4:", point3 + point4)  # This will call the __add__ method
