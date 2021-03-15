def is_palindrome(n):
    number = str(n)
    return number == number[::-1]


def digits(num_digits: int) -> tuple:
    first = 10**(num_digits-1)
    last = 10**num_digits - 1
    return first, last


def largest_palindrome_product(num_digits: int):
    first, last = digits(num_digits)    # 100, 999
    max_number = 0
    for i in range(last, first, -1):
        for j in range(last, first, -1):
            if is_palindrome(i*j):
                max_number = max(max_number, i*j)
    return max_number


def solution():
    print(largest_palindrome_product(3))
