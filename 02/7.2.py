import random
from fractions import Fraction


def evklid_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def get_num(string: str) -> list:
    lst = string.replace(' ', '').split('/')
    if len(lst) == 2 and lst[0].isdigit() and lst[1].isdigit():
        return [int(i) for i in lst]
    else:
        return [None]


def divide_by_a_common_divisor(div_lst: list) -> list:
    gcd = evklid_gcd(div_lst[0], div_lst[1])
    if gcd > 1:
        return [int(i / gcd) for i in div_lst]
    else:
        return div_lst


def mathematical_operations(lst1: list, lst2: list) -> dict:
    if lst1 is not None or lst2 is not None:
        lst1_denominator = [lst1[0] * lst2[1], lst1[1] * lst2[1]]
        lst2_denominator = [lst2[0] * lst1[1], lst2[1] * lst1[1]]
        temp_result_sum = [lst1_denominator[0] + lst2_denominator[0],
                           lst1_denominator[1]]
        summa = divide_by_a_common_divisor(temp_result_sum)
        temp_result_multiplication = [lst1_denominator[0] * lst2_denominator[0],
                                      lst1_denominator[1] * lst2_denominator[1]]
        multiplication = divide_by_a_common_divisor(temp_result_multiplication)
        return {'summa': summa, 'multiplication': multiplication}


def show_fractions(fr_dict: dict) -> str:
    return f"Сумма дробей: {fr_dict['summa'][0]}/{fr_dict['summa'][1]}, " \
           f"произведение: {fr_dict['multiplication'][0]}/{fr_dict['multiplication'][1]}"


def test_my_fractions(rep: int) -> bool:
    counter = 0
    for _ in range(0, rep):
        r1 = random.randint(1, 10000)
        r2 = random.randint(1, 10000)
        r3 = random.randint(1, 10000)
        r4 = random.randint(1, 10000)
        my_res = mathematical_operations([r1, r2], [r3, r4])
        frac1 = Fraction(r1, r2)
        frac2 = Fraction(r3, r4)
        fr_mult = frac1 * frac2
        fr_sum = frac1 + frac2
        if fr_mult.numerator == my_res['multiplication'][0] and fr_mult.denominator == my_res['multiplication'][1]:
            if fr_sum.numerator == my_res['summa'][0] and fr_sum.denominator == my_res['summa'][1]:
                counter += 1
    return True if counter == rep else False


f1 = get_num(input('Введите дробь в формате 1/2: '))
f2 = get_num(input('Введите дробь в формате 1/2: '))

d = mathematical_operations(f1, f2)
# d = mathematical_operations([4, 5], [4, 8])
print(show_fractions(d))
fr1 = Fraction(f1[0], f1[1])
fr2 = Fraction(f2[0], f2[1])
sum = fr1 + fr2
mult = fr1 * fr2
print(sum, mult)
print(test_my_fractions(5000))
