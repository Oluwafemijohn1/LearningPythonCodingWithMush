numbers = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]

first = set(numbers)  # Convert list to set to remove duplicates
print(first)
# Convert set back to list if needed
unique_list = list(first)
print(unique_list)

second = {16, 7, 8, 9, 10}

# Union of two sets
union_set = first.union(second)  # or first | second
print("Union:", union_set)

print("Union with | ", first | second)

# Intersection of two sets
intersection_set = first.intersection(second)  # or first & second
print("Intersection:", intersection_set)
print("Intersection with & ", first & second)

# Difference of two sets
difference_set = first.difference(second)  # or first - second
print("Difference:", difference_set)
print("Difference with - ", first - second)

# Symmetric difference of two sets
symmetric_difference_set = first.symmetric_difference(
    second)  # or first ^ second
print("Symmetric Difference:", symmetric_difference_set)
print("Symmetric Difference with ^ ", first ^ second)

# Subset and Superset
print("Is first a subset of second? ",
      first.issubset(second))  # or first <= second
print("Is first a superset of second? ",
      first.issuperset(second))  # or first >= second
# Disjoint sets
print("Are first and second disjoint? ", first.isdisjoint(
    second))  # or first.isdisjoint(second)
# Adding elements to a set
first.add(11)
print("After adding 11: ", first)

# Removing elements from a set
first.remove(11)  # Raises KeyError if 11 is not present

print()
# Set comprehension
set_values = {x for x in range(5)}
print("Set comprehension: ", set_values)
