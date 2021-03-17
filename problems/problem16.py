def power_digit_sum(n):
    exp = str(2**n)
    total = 0
    for digit in exp:
        total += int(digit)
    return total

def solution():
    print(power_digit_sum(1000))