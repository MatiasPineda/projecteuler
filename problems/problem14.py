
class CollatzSequence:
    def __init__(self, number):
        self.start = number
        self.sequence = self.generate_sequence()
        self.steps = len(self.sequence)

    def generate_sequence(self):
        n = self.start
        sequence = [n]
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            sequence.append(n)
        return sequence

    def __str__(self):
        result = ''
        for s in self.sequence:
            chain = f'{s}'
            if s!= 1:
                chain += ' -> '
            result += chain
        return result[:60]


def longest_collatz_sequence(n):
    longest = 0
    for i in range(n, 1, -1):
        if i % 2 != 0:
            seq = CollatzSequence(i)
            if seq.steps > longest:
                longest = seq.steps
                start = i
    return start


def solution():
    print(longest_collatz_sequence(10**6))