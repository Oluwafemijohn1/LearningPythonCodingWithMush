letters = ["a", "b", "c", "d"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combine = zeros + letters
print(combine)

# list with iterable
numbers = list(range(20))
print(numbers)

chars = list("Hello world")
print(chars)

letters[0] = "A"
print(letters)
print(letters[0:3])  # ['A', 'b', 'c']
print(letters[:3])  # ['A', 'b', 'c']
print(letters[2:])  # ['c', 'd']

# Copy the original list
print(letters[:])  # ['A', 'b', 'c', 'd']

# Every second item in the lis
print(letters[::2])  # ['A', 'c']
print(numbers[::2])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(numbers[::3])  # [0, 3, 6, 9, 12, 15, 18]

# reverse the element
# [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[::-1])
print(numbers[::-2])  # [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]


# Unpacking
num = [1, 2, 3]
first, second, third = num
print(first)

nums = [1, 2, 3, 4, 5, 5, 5, 5, 5, 7]
first, second, *others = nums
print(others)

first, *others,  last,  = nums
print(first, last)


# Looping through list
for letter in letters:
    print(letter)

# Looping with index. enumerate returns a turple e.g (o, "a")
for letter in enumerate(letters):
    index, item = letter
    print(index, item)

print()

# or
for index, letter in enumerate(letters):
    print(index, letter)

print()
# Adding or removing an item
print("Adding or removing an item")
letters.append("e")  # At the end
print(letters)

# Addin at a specific position
letters.insert(0, "-")
print(letters)

# remove at the end
letters.pop()
print(letters)

# At a specific
letters.pop(0)
print(letters)
# Remove an item
letters.remove("A")
print(letters)

# Delete a range
del letters[0:1]
print(letters)

# Delete all
letters.clear()
print(letters)

print()
# Finding items
print("Finding items")
letters = ["a", "d", "c", "d"]
print(letters.index("a"))
if "f" in letters:
    print(letters.index("f"))
print(letters.count("a"))

print()
# Sorting List
print("Sorting list")
numbers = [3, 2, 5, 7, 4, 2]
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(numbers)
numbers.sort()
print(numbers)

# Sorting for complex list
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


def sort_item(item):
    return item[1]


# items.sort(key=sort_item)
# print(items)

# Lamda fuction
items.sort(key=lambda item: item[1])
print(items)


print()
# Mapping
print("Mapping")
mapped = list(map(lambda item: item[1], items))
print(mapped)

print()
# Filtered
print("Filtered list ")
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

print()
# List comprehensions.
print("List comprehensions")
mapped = [item[1] for item in items]  # Mapping
print(mapped)
filtered = [item for item in items if item[1] >= 10]  # Filtered
print(filtered)


print()
# Zip Functions
print("Zip Functions ")
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))


# Stack. LIFO
browsing_sesion = []
browsing_sesion.append(1)
browsing_sesion.append(2)
browsing_sesion.pop()

if not browsing_sesion:
    browsing_sesion[-1]


# QUEUE. FIFO
