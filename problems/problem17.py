

def numbers_to_letter(n):
    base_numbers_to_letter = {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand'
    }

    num_list = [int(x) for x in str(n).rjust(4,'0')]

    word = ''
    if num_list[0] != 0:
        word += base_numbers_to_letter[num_list[0]]+base_numbers_to_letter[1000]
    if num_list[1] != 0:
        word += base_numbers_to_letter[num_list[1]]+base_numbers_to_letter[100]
    if num_list[0]+num_list[1] != 0 and num_list[2] + num_list[3] != 0:
        word += 'and'
    if num_list[2] == 1:
        word += base_numbers_to_letter[int(num_list[2]*10+num_list[3])]
    else:
        word += base_numbers_to_letter[num_list[2]*10]
        word += base_numbers_to_letter[num_list[3]]

    return word



def number_letter_counts(last):
    count = 0
    for i in range(1, last+1):
        count += len(numbers_to_letter(i))
    return count

def solution():
    print(number_letter_counts(1000))