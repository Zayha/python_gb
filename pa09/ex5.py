from ex2 import riddle
from ex3 import fu_to_json
from ex4 import count


@count(2)
@riddle
@fu_to_json
def check(num: int, attempt: int):
    print(f'Необходимо угадать число в диапазоне от 1 до 100 за {attempt} попыток')
    flag = True
    counter = 0
    while flag and counter != attempt:
        n = input(f'Введите число для отгадывания, осталось {attempt - counter} попыток:')
        counter += 1
        if n.isdigit():
            n = int(n)
        else:
            print(f'Указанное значение "{n}" не соответствует параметрам загадки!')
            continue
        if n == num:
            print('WIN!!!')
            return 'WIN'
        else:
            if n < num:
                print(f'Загаданное число больше {n}')
            else:
                print(f'Загаданное число меньше {n}')
    return 'LOSE'


def main():
    check()


if __name__ == '__main__':
    main()
