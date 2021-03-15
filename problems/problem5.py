
def factors(number: int) -> dict:
    f = {1: 1}
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


def smallest_multiple(start, finish) -> int:
    all_factors = dict()
    for i in range(start, finish+1):
        local_factors = factors(i)
        for f in local_factors:
            if f not in all_factors:
                all_factors[f] = local_factors[f]
            else:
                all_factors[f] = max(all_factors[f], local_factors[f])
    total = 1
    for f in all_factors:
        total *= f**all_factors[f]
    return total


def solution():
    print(smallest_multiple(1, 20))
