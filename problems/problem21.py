from resources.utils import prime_factors, prod
from itertools import product

def all_divisors(n):
    prime_factor = prime_factors(n)
    primes = dict()
    for p in prime_factor:
        primes[p] = [p**i for i in range(prime_factor[p]+1)]
    all_combinations = product(*primes.values())
    divisors = {prod(x) for x in all_combinations}

    return divisors - {n}


def amicable_numbers(n):
    amicable = set()
    for number in range(1,n):
        if number not in amicable:
            sum_div = sum(all_divisors(number))
            if sum(all_divisors(sum_div)) == number and sum_div!=number:
                amicable.update({sum_div, number})
    return sum(amicable -{0,1})


def solution():
    print(amicable_numbers(10000))