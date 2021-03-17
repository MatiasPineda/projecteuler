from math import sqrt

def n_th_triangular_number(n):
    return (n*(n+1))//2

def factors(number: int) -> dict:
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


def highly_divisible_triangular_number(total_divisors):
    i = 1
    divisors = 0
    while divisors <= total_divisors:
        divisors = 1
        number = n_th_triangular_number(i)
        all_factors = factors(number)
        for k in all_factors:
            divisors *= all_factors[k] + 1
        i+=1
    return number




def solution():
    print(highly_divisible_triangular_number(500))