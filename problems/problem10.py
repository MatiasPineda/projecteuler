def sumation_of_primes(num):
    i = 2
    all_nums = set(range(2,num+1))
    while i*i < num:
        composites = set()
        if i in all_nums:
            composites = {x for x in all_nums if (x % i == 0 and x != i)}
        all_nums -= composites
        i += 1

    return sum(all_nums)


def solution():
    print(sumation_of_primes(2*10**6))
