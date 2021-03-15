def multiples_3_and_5():
    sum = 0
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

def solution():
    print(multiples_3_and_5())