def solve_math_problem(problem):
    # Check if the problem is a valid equation
    if not problem.endswith('='):
        raise ValueError('Invalid math problem')

    # Get the left and right sides of the equation
    left, right = problem.split('=')

    # Evaluate the expression on the right side of the equation
    result = eval(right)

    # Return the solution to the problem
    return result
