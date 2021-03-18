import string
file = 'resources/p022_names.txt'

def read_file(file):
    with open(file) as f:
        data = f.readline().replace('"', '').split(',')
    data.sort()
    return data

sample = ['AARON', 'ABBEY', 'ABBIE', 'ABBY', 'ABDUL', 'ABE', 'ABEL', 'ABIGAIL', 'ABRAHAM', 'ABRAM', 'ADA', 'ADAH', 'ADALBERTO', 'ADALINE', 'ADAM', 'ADAN', 'ADDIE', 'ADELA', 'ADELAIDA', 'ADELAIDE', 'ADELE', 'ADELIA', 'ADELINA', 'ADELINE', 'ADELL', 'ADELLA', 'ADELLE', 'ADENA', 'ADINA', 'ADOLFO', 'ADOLPH', 'ADRIA', 'ADRIAN', 'ADRIANA', 'ADRIANE', 'ADRIANNA', 'ADRIANNE', 'ADRIEN', 'ADRIENE', 'ADRIENNE', 'AFTON', 'AGATHA', 'AGNES', 'AGNUS', 'ZACH']


def score_word(word: str) -> int:
    all_letters = string.ascii_uppercase
    score = 0
    for letter in word:
        score += all_letters.index(letter) + 1
    return score

def names_scores(namelist: list):
    total_score = 0
    for i, name in enumerate(namelist):
        total_score += (i+1) * score_word(name)
    return total_score


def solution():
    print(names_scores(read_file(file)))