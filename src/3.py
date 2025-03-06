import random

def get_random_math_problem():
    numbers = [1, 2, 3, 4, 5]
    operators = ['+', '-', '*', '/']
    problem = ''
    for i in range(random.randint(2, 4)):
        num1 = random.choice(numbers)
        num2 = random.choice(numbers)
        op = random.choice(operators)
        if op == '+':
            solution = num1 + num2
        elif op == '-':
            solution = num1 - num2
        elif op == '*':
            solution = num1 * num2
        elif op == '/' and num2 != 0:
            solution = num1 / num2
        else:
            continue
        problem += f'{num1} {op} {num2} = ?\n'
    return problem