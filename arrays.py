from array import array

numbers = array('i', [1, 2, 3, 4, 5])
print(numbers)
# Accessing elements
print(numbers[0])  # First element

print(numbers[-1])  # Last element
# Slicing
print(numbers[1:4])  # Elements from index 1 to 3
print(numbers[:3])  # First three elements

# Modifying elements
numbers[0] = 10  # Change first element
print(numbers)

# Adding elements
numbers.append(6)  # Add at the end
print(numbers)

# Inserting elements
numbers.insert(1, 20)  # Insert 20 at index 1
print(numbers)

print()
# Removing elements
numbers.remove(20)  # Remove first occurrence of 20
print(numbers)

# Popping elements
popped_element = numbers.pop()  # Remove and return last element
print(f"Popped element: {popped_element}")
print(numbers)
