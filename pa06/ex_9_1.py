__all__ = ['check_date']

import sys


def check_date(date: str = '') -> bool:
    if sys.argv[1]:
        date = sys.argv[1]
    lst = [int(x) for x in date.split('.') if x.isdigit()]
    print(lst)
    if len(lst) == 3:
        dd, mm, yyyy = lst
        if 1 <= yyyy <= 9999 and 1 <= mm <= 12 and 1 <= dd <= __day_in_month(mm, yyyy):
            return True
        else:
            return False
    else:
        return False


def __check_leap_year(year: int) -> bool:
    # if year % 4 == 0:
    #     if year % 100 == 0:
    #         if year % 400 == 0:
    #             return True
    #         return False
    #     return True
    # else:
    #     return False
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def __day_in_month(month: int, year: int) -> int:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and __check_leap_year(year):
        return 29
    return days_in_month[month - 1]


def main():
    print(check_date('29.02.2023'))


if __name__ == '__main__':
    main()
