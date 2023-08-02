__all__ = ['count']

import random
from functools import wraps
from typing import Callable
from ex3 import fu_to_json


def count(num: int = 1):
    def decor(func: Callable):
        res = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                res.append(result)
            return res

        return wrapper

    return decor


@count(5)
@fu_to_json
def my_fu(*args, **kwargs):
    return random.randint(1, 10000)


def main():
    print(my_fu(1, 2, 44))


if __name__ == '__main__':
    main()
