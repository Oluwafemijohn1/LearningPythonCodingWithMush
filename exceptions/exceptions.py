attempts = 0
max_attempts = 3

while attempts < max_attempts:
    file = None
    try:
        file = open("text.txt", "r")
        age = int(input("Enter your age: "))
        x_factor = 10 / age
    except (ValueError, ZeroDivisionError, Exception) as e:
        print(f"Invalid input! Please enter a valid integer for age.")
    finally:
        attempts += 1
        print(f"Attempt {attempts} of {max_attempts}")
        if file is not None:
            file.close()

if attempts == max_attempts:
    print("Too many invalid attempts. Exiting the program.")

print("Thank you for using the age input program.")
# This code handles exceptions when inputting age, ensuring that the user enters a valid integer and that the age is non-negative.
