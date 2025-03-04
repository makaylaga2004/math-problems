import random

def get_random_math_problem():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Choose a random operation (+, -, x, /)
    op = random.choice(["+", "-", "*", "/"])
    
    # Return the problem and solution as a tuple
    return (f"{num1} {op} {num2} = ?", num1 + num2)
