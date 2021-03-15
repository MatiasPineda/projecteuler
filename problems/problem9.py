from math import sqrt

def special_pythagorean_triplet(num):
    all_nums = tuple(range(1, num+1))
    for a in all_nums:
        for b in all_nums:
            c = sqrt(a**2 + b**2)
            if a+b+c == num:
                return a*b*c, a, b, c
    return f'No triplet a,b,c results in a+b+c={num}'


def solution():
    print(special_pythagorean_triplet(1000))