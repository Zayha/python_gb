# Создайте функцию генератор чисел Фибоначчи (см. Википедию).
import time
from functools import lru_cache


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time} секунд.")
        return result

    return wrapper


def fibo_gen(num: int):
    a, b = 0, 1
    count = 0
    while count <= num:
        yield a
        a, b = b, a + b
        count += 1


def fibonacci_generator(num: int):
    @lru_cache(maxsize=None)
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    count = 0
    while count <= num:
        yield fibonacci(count)
        count += 1


@timer
def check1(n: int):
    for i in fibo_gen(n):
        pass


@timer
def check2(n: int):
    for i in fibonacci_generator(n):
        pass


nu = 35000
check1(nu)
check2(nu)

print(list(fibo_gen(5)))
print(list(fibonacci_generator(5)))