values = list(range(5))  # Generator expression
print("List of values: ", values)
values = [*values, *"Hello"]  # Unpacking operator
print("Unpacking operator: ", values)


# To unpack a dictionary
dict_values = {"a": 1, "b": 2, "c": 3}
dict_values2 = {**dict_values, "d": 4}  # Unpacking operator for dictionaries
combine = {**dict_values, **dict_values2}  # Combine two dictionaries
print("Unpacking operator for dictionaries: ", dict_values2)
