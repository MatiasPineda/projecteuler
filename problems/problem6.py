
def sum_of_squares(num):
    return (num*(num+1)*(2*num +1))//6

def square_of_sums(num):
    return ((num*(num + 1))//2)**2

def sum_square_difference(number):
    return abs(square_of_sums(number) - sum_of_squares(number))


def solution():
    print(sum_square_difference(100))