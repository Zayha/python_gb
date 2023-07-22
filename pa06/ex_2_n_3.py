__all__ = ['check_your_luck']

import random
from sys import argv


def check_your_luck(n1: int = 1, n2: int = 10, rep: int = 10) -> bool:
    if len(argv) > 1:
        arg_gen = [int(x) for x in argv[1:] if x.isdigit()]
        if len(arg_gen) == 1:
            arg_gen.append(arg_gen[0] + random.randint(1, 1000))
            arg_gen.append(10)
        elif len(arg_gen) == 2:
            arg_gen.append(10)
        print(arg_gen)
        if len(arg_gen) >= 3:
            n1, n2, rep, *_ = arg_gen
    rnd_num = random.randint(n1, n2)
    counter = 0
    win = False
    while counter <= rep and not win:
        counter += 1
        attempt = input(f'Угадай целое число в диапазоне от {n1} до {n2}: ')
        if attempt.isdigit():
            if int(attempt) == rnd_num:
                win = True
            else:
                if int(attempt) > rnd_num:
                    print('Меньше! ')
                else:
                    print('Больше! ')
        else:
            print('Нужно указать целое число, попытка потеряна')
    return win
