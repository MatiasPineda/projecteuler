file = 'resources/problem18.txt'

def read_file(file):
    triangle = []
    with open(file) as f:
        data = f.readlines()
    string_data = [line.replace('\n', '').split() for line in data]
    for level in string_data:
        triangle.append([int(n) for n in level])
    return triangle


def maximum_path_sum_1(triangle):
    i = -2
    while triangle[i] != triangle[0]:
        for j, n in enumerate(triangle[i]):
            triangle[i][j] = triangle[i][j] + max(triangle[i+1][j], triangle[i+1][j+1])
        i -= 1
    total = max(triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1])
    return total

def solution():
    print(maximum_path_sum_1(read_file(file)))