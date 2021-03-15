
def opt_fib(n):
    fibs = [1, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]

def opt_fib2(n):
    fibs = [1, 1]
    sum_even = 0
    for i in range(2, n+1):
        r = fibs[-1] + fibs[-2]
        if r > 4*10**6:
            break
        if r % 2 == 0:
           sum_even += r
        fibs.append(r)

    return sum_even


def solution():
    print(opt_fib2(100))