import random

def get_random_code():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)

    # Generate a list of operators
    ops = ['+', '-', '*', '/']

    # Choose a random operator from the list
    op = random.choice(ops)

    # Generate two random numbers to use in the expression
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Use the chosen operator to create a math problem
    problem = f'{num1} {op} {num2} = '

    # Solve the problem and get the answer
    answer = eval(problem)

    return problem + str(answer)