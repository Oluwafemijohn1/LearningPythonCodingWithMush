from sys import getsizeof

values = (x * 2 for x in range(1000))  # Generator expression
print("Generator expression: ", values)

print("Size of generator expression: ", getsizeof(values))

values = [x * 2 for x in range(1000)]  # Generator expression


print("Size of generator expression: ", getsizeof(values))
