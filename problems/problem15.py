from math import factorial
"""
Going from the top left vertex to another, counting how many paths exist, I noticed it resembled a Pascal's triangle
in the form

1   1   1   1   1   1   1

1   2   3   4   5   6

1   3   6   10  15

1   4   10  20

1   5   15

1   6

1

The bottom right vertex is at the level 2n where n is numbers of rows and columns in the nxn grid

"""

def binomial_coeficient(n, k):
    """
    n over k
    :return:
    """
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

def lattice_paths(grid_size):
    n = grid_size * 2
    max_value = 0
    for k in range(n+1):
        max_value = max(binomial_coeficient(n, k), max_value)
    return max_value

def solution():
    print(lattice_paths(20))