import random


def decimal_to_hex(decimal_number):
    hex_digits = "0123456789ABCDEF"

    if decimal_number == 0:
        return '0'
    hex_number = ''
    while decimal_number > 0:
        temp = decimal_number % 16
        hex_dig = hex_digits[temp]
        hex_number = hex_dig + hex_number
        decimal_number = decimal_number // 16
    return hex_number


def test_my_hex(rep: int) -> list:
    result_true = 0
    result_false = 0
    for _ in range(rep):
        r = random.randint(1, 100000)
        # print(decimal_to_hex(r), hex(r)[2:].upper())
        if decimal_to_hex(r) == hex(r)[2:].upper():
            result_true += 1
        else:
            result_false += 1
    return [result_true, result_false]


a = 500000
res = test_my_hex(a)
print(f'Пройдено тестов {a}, успешно {res[0]}, провалено {res[1]}')
