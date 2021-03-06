from typing import Union
from math import factorial

def prime_factors(number: int) -> dict:
    """
    Takes an integer and returns every prime factor and their quantity
    :param number: Integer
    :return: dict of prime numbers as keys and their ammount as values
    """
    f = {}
    i = 2
    while number > 1 and number >= i:
        if number % i == 0:
            if i not in f:
                f[i] = 1
            else:
                f[i] += 1
            number //= i
        else:
            i += 1
    return f


def divisors(n):
    '''return divisors of n'''
    d = {1}
    for i in range(2, int(pow(n,.5))+1):
        if (n % i) == 0:
            other = n // i
            if other == i:
                pair = {i}
            else:
                pair = {i,other}
            d.update(pair)
    return d


def prod(num_list: Union[list, tuple, set]) -> int:
    product = 1
    for i in num_list:
        product *= i
    return product


def binomial_coeficient(n, k):
    """
    n over k
    :return:
    """
    return int(factorial(n)/(factorial(k)*factorial(n-k)))