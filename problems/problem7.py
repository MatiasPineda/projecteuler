def n_th_prime(num:int):
    primes = [2]
    is_prime = True
    number = 3
    while len(primes) < num:
        for i in primes:
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
        number += 2
        is_prime = True
    return primes[num-1]


def solution():
    print(n_th_prime(10001))