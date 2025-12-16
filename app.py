import math
x = 1
unit_price = 4
print("Running... " * 2)
is_published = True
course = "Python programming language"
print(len(course))

print(course[0])
print(course[0:4])
print(course[4:])
print(course[:3])

course2 = " python \"programming Language "
print(course2)

first = "Oluwafemi"
last = "Ogundipe"
full = f"{first} {last}"
print(full)
print(course2.replace("P", "J"))
print(course2.lower())
print(course2.upper())
print(course2.title())
print(course2.strip())
print(course2.lstrip())
print(course2.find("Pro"))
print("pro" in course2)
print("swift" not in course2)

# Numbers
x = 1
y = 1.1
m = 1 + 2j

# number Operations
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # Integer division
print(10 % 3)  # Modulus
print(10 ** 3)  # Exponent


x = 10
x = x + 3
x += 3  # Augumented assignemnt operator

# Working with numbers
print(round(2.9))
print(abs(-2.9))

# Type convertion
# x = input("X: ")
# y = int(x) + 1

int(x)
float(x)
bool(x)
str(x)
print(type(x))


# Truty and Falsy values
# Falsy
# "", 0, null, []
# Truety


# Conditional Statements
temperature = 32
if (temperature > 30):
    print("It is warm")
    print("Drink Water")
else:
    print("Not so")
print("Done")


# Logical operators are:
# and, or and not

# Loan eligibility logic
high_income = True
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
print("DOne")

# CHaining comparison operator
age = 22

if age >= 18 and age < 65:
    print("Eligible 1")
if 18 <= age < 65:  # These two are the same. The second is call Chaining comparison operator
    print("Eligible 2")


# For loop
for number in range(3):
    print("Attempting: ", number + 1, (number + 1) * ".")

print()

# For loop simplified
for number in range(1, 4):
    print("Attempting: ", number, (number) * ".")
print()
# For loop with a step
for number in range(1, 10, 2):
    print("Attempting: ", number, (number) * ".")

print()
# For ..Else
successful = True
for number in range(1, 4):
    print("Attempt: ", number)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


# Nexted - for loop
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

print()

# Iterables
for x in range(5):
    print("X=", x)
for y in "Python":
    print(y)
for z in [2, 3, 4, 2, 4, 5]:
    print(z)

print()

# While loop
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input("> ")
    print("ECHO", command)
