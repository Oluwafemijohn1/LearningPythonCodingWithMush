from collections import namedtuple
from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

if not queue:
    print("Queue is empty")


# Turple
point = (1, 2, 3)
print(point)
# Named tuple
Point = namedtuple("Point", ["x", "y", "z"])
point = Point(1, 2, 3)
print(point)
print(point.x, point.y, point.z)

point2 = 1,  # This is also a typle
print(point2)
point2 = ()  # Empty tuple

# Tuple concatination
concat = (1, 2) + (3, 4)
print(concat)

# Multiplication
multiply = (1, 2) * 3
print(multiply)

print()
# List -> Tuple convertion
print("List -> Tuple convertion")
convert = tuple([1, 2])
print(convert)
convert = tuple("Hello world")
print(convert)

three_point = (1, 2, 3)
print(three_point[0:2])


print()
# Swapping variables
print("Swapping variables")
a, b = 1, 2
a, b = b, a
print(a, b)  # 2, 1
