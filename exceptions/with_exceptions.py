attempts = 0
max_attempts = 3

while attempts < max_attempts:
    file = None
    try:
        with open("text.txt", "r") as file, open("target.txt", "w") as file_write:
            print("File opened successfully.")
        age = int(input("Enter your age: "))
        x_factor = 10 / age
    except (ValueError, ZeroDivisionError, Exception) as e:
        print(f"Invalid input! Please enter a valid integer for age.")
    finally:
        attempts += 1
        print(f"Attempt {attempts} of {max_attempts}")

if attempts == max_attempts:
    print("Too many invalid attempts. Exiting the program.")

print("Thank you for using the age input program.")
