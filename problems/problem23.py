from resources.utils import divisors


def is_abundant(n):
    return sum(divisors(n)) > n


def all_abundants(n):
    abundant = set()
    for i in range(12,n):
        if is_abundant(i):
            abundant.add(i)
    return abundant


def non_abundant_sums(n):
    abundants = all_abundants(n)
    abundants_sum = {(x+y) for x in abundants for y in abundants if x+y <= n}
    all_numbers = set(range(1,n+1))

    return sum(all_numbers-abundants_sum)


def solution():
    print(non_abundant_sums(28123))