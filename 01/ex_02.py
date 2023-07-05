import math


def check_prime_numbers(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True


def prime_numbers():
    n = input('Укажите целое число n от 0 до 100000: ')
    if n.isdigit() and (0 <= int(n) <= 100000):
        return f'Число {n} является простым: {check_prime_numbers(int(n))}'


print(prime_numbers())
