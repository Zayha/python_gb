__all__ = ['solving_quadratic_equation', 'get_params', 'count_params', 'generator_trio_to_csv']

import csv
import random
from functools import wraps
from typing import Callable

from ex5 import fu_to_json


def get_params(func):
    @wraps(func)
    def wrapper():
        lst = []
        with open('trio.csv', 'r', encoding='utf-8', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                lst.append(row)
                func(float(row[0]), float(row[1]), float(row[2]))
            return True

    return wrapper


def count_params():
    lst = []
    with open('trio.csv', 'r', encoding='utf-8', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # print(row)
            lst.append(row)

    def decor(func: Callable):
        res = []

        @wraps(func)
        def wrapper():
            # print(lst)
            for i in lst:
                a, b, c = i
                result = func(float(a), float(b), float(c))
                res.append(result)
            return res

        return wrapper

    return decor


@get_params
# @count_params()
@fu_to_json
def solving_quadratic_equation(a: float, b: float, c: float) -> None | float | tuple[float, float]:
    if a == 0:
        if b != 0:
            return -(c / b)
        else:
            return None
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    if d == 0:
        return -(b / 2 * a)
    return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)


def generator_trio_to_csv(lines: int = 100):
    # lst = []
    if lines < 100:
        lines = 100
    if lines > 1000:
        lines = 1000
    with open('trio.csv', 'w', encoding='utf-8', newline='') as file:
        for _ in range(100):
            csv_writer = csv.writer(file)
            csv_writer.writerow([random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)])


def main():
    print(solving_quadratic_equation())
    # generator_trio_to_csv(500)
    pass


if __name__ == '__main__':
    main()
