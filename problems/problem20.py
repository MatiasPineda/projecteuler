
def factorial_digit_sum(n):
    fac = 1
    for i in range(n):
        fac *= i+1

    return sum(list(map(int, str(fac))))

def solution():
    print(factorial_digit_sum(100))