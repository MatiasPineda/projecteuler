def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


days_by_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 31, 12: 31}


def counting_sundays(start, end):
    start_date = tuple(map(int, start.split('/')))
    end_date = tuple(map(int, end.split('/')))

    all_day_count = []
    for y in range(start_date[2], end_date[2] +1):
        for i in days_by_month:
            ammount = days_by_month[i]
            if is_leap_year(y) and i == 2:
                ammount += 1
            all_day_count.append(ammount)
    remainder = 0
    total = 0
    for d in all_day_count:
        remainder = (d + remainder) % 7
        if remainder == 1:
            total += 1
    return total


def solution():
    print(counting_sundays('1/01/1901', '31/12/2000'))
