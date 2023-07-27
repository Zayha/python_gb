__all__ = ['pseudo_name']

import random


def pseudo_name(len_min: int = 4, len_max: int = 7, file: bool = True) -> str:
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    rand_length = random.randint(len_min, len_max)
    result = f'{random.choice(vowels).upper()}{random.choice(vowels)}'
    while rand_length > 2:
        vow_or_cons = random.choice(vowels + consonants)
        result += vow_or_cons
        rand_length -= 1
    if file:
        with open('ex2_out.txt', 'a', encoding='utf-8') as f:
            f.write(f'{result}\n')
    return result


if __name__ == '__main__':
    for _ in range(121):
        pseudo_name()
