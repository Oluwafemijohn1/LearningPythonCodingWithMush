import time
from timeit import timeit


code1 = """
def calculate_xFactor(age):
    if age <= 0:
        raise ValueError("Age must be a positive integer.")
    return 10 / age


try:
    calculate_xFactor(-1)
except ValueError as e:
    pass
    
"""

code2 = """
def calculate_xFactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xFactor(-1)
if xfactor == None:
    pass  
"""

print("First code= ", timeit(code1, number=10000))
print("Second code= ", timeit(code2, number=10000))
