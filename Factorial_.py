# Factorial function

# The factorial of a number is the product of all the values from 1 to the 
# number, inclusive.

# Thus 4 factorial, which is written as 4!, is calculated as
# 1 * 2 * 3 * 4 = 24
# 5! is
# 1 * 2 * 3 * 4 * 5 = 120

# The convention is that 0! = 1 (not zero, as you might expect).

# Write a function called factorial, that will return the factorial of the 
# number passed as its argument.

# You must include a Docstring, and function annotations, in your function.


def factorial(n: int) -> int:
    """_summary_

    Args:
        n (int): _description_

    Returns:
        int: _description_
    """
    fact = 1
    if n > 1:       # factorial of 0 or 1 is 1
        for i in range(1, n+1):
            fact = fact * i

    return fact


for x in range(11):
    print(f"Factorial of {x} is: {factorial(x)}")
