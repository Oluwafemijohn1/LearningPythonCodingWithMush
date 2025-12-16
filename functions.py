def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Hello ")


greet("Oluwafemi", "Ogundipe")


def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"


print(get_full_name("Oluwafemi", "Ogundipe"))

file = open("test.txt", "w")
file.write(get_full_name("Oluwafemi", "Ogundipe"))
file.close()


# Default arguments
def increament(number, by=1):
    return number + by


# Ketword arguments
print(increament(2, by=3))

# Unpacking arguments or *args


def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(add(1, 2, 3, 4, 5))
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Unpacking arguments or **kwargs.
# This is used to pass a variable number of keyword arguments to a function that can be accessed as a dictionary.


def save_user(**user):
    print(user)
    print(user["name"])
    print(user["age"])


save_user(name="Oluwafemi", age=30, country="Nigeria")
# {'name': 'Oluwafemi', 'age': 30, 'country': 'Nigeria'}


# scope
message = "A"


def greet2():
    global message
    message = "B"


greet2()
print(message)

# Debugging


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3))


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "Fizz Buzz"
    if (input % 5 == 0):
        return "Buzz"
    if (input % 3 == 0):
        return "Fizz"
    return input


print(fizz_buzz(1))
