def calculate_xFactor(age):
    if age <= 0:
        raise ValueError("Age must be a positive integer.")
    return 10 / age


try:
    calculate_xFactor(-1)
except ValueError as e:
    print(f"An error occurred: {e}")
