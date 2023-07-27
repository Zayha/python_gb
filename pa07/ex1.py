__all__ = ['add_num']

import random


def add_num(name: str, many_lines: int) -> None:
    while many_lines > 0:
        with open(name, 'a', encoding='utf-8') as f:
            rnd_int = random.randint(-1000, 1000)
            rnd_float = random.uniform(-1000, 1000)
            string = f'{rnd_int} | {rnd_float}\n'
            f.write(string)
        many_lines -= 1


if __name__ == '__main__':
    add_num('ff1.txt', 8)
