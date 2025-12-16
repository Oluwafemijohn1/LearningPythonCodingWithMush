point = {"x": 1, "y": 2}
point2 = dict(x=1, y=3, name="femi")
print("points " + str(point))
print("points2 " + str(point2))
# Accessing elements
print(point["x"])  # Accessing by key
print(point2["name"])  # Accessing by key

print(point.get("x"))  # Accessing with get method
print(point2.get("x", -1))  # Accessing with get method and default value

# Adding elements
point["z"] = 3  # Adding a new key-value pair

print("After adding z: " + str(point))

# Modifying elements
point["x"] = 10  # Modifying an existing key-value pair
print("After modifying x: " + str(point))

# Removing elements
point.pop("y")  # Removing a key-value pair
print("After removing y: " + str(point))

# Deleting elements
del point["z"]  # Deleting a key-value pair
print("After deleting z: " + str(point))

#  Clearing the dictionary
point.clear()  # Removing all key-value pairs
print("After clearing: " + str(point))

# Itterating through a dictionary
for key, value in point2.items():
    print(f"Key: {key}, Value: {value}")

#  or
for key in point2:
    print(f"Key: {key}, Value: {point2[key]}")


# Dictionary comprehension
values = {x: x*2 for x in range(5)}
print("Dictionary comprehension: ", values)
values = {x: x**2 for x in range(5)}
print("Dictionary comprehension with squares: ", values)
