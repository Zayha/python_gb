__all__ = ['create_new_file_ex3']

import math


def __result_formatter(num1: str, num2: str, name: str) -> str:
    num1 = int(num1)
    num2 = float(num2)
    num_multi = num1 * num2
    if num_multi < 0:
        return name.lower() + " " + str(abs(num_multi))
    if num_multi > 0:
        return name.upper() + " " + str(round(num_multi))
    if num_multi == 0:
        return name + " " + str(num_multi)


def create_new_file_ex3(name_f: str, name_s: str, name_out: str) -> None:
    with open(name_f, encoding='utf-8') as f1, open(name_s, encoding='utf-8') as f2:
        str_f = [i.strip() for i in f1.readlines()]
        str_s = [i.strip() for i in f2.readlines()]
    if len(str_f) > len(str_s):
        str_s = __formatter_list(str_f, str_s)
    if len(str_f) < len(str_s):
        str_f = __formatter_list(str_s, str_f)
    with open(name_out, 'w', encoding='utf-8') as f:
        for name, string_f_parse in zip(str_f, str_s):
            temp_lst = [i.strip() for i in string_f_parse.split('|')]
            f.write(f'{__result_formatter(*temp_lst, name)}\n')


def __formatter_list(big_list: list, small_list: list) -> list:
    # div = math.ceil(len(big_list) / len(small_list))
    # result = small_list * div
    # return result[:len(big_list)]
    return (small_list * math.ceil(len(big_list) / len(small_list)))[:len(big_list)]


if __name__ == '__main__':
    create_new_file_ex3('ex2_out.txt', 'ff1.txt', 'out.txt')
