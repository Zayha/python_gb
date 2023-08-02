import random


def riddle():
    num = input("Загаданное число в диапазоне от 1 до 100: ")
    attempt = input('Укажите кол-во попыток от 1 до 10: ')
    if num.isdigit():
        num = int(num)
        if not 1 <= num <= 100:
            num = random.randint(1, 100)
    if attempt.isdigit():
        attempt = int(attempt)
        if not 1 <= attempt <= 10:
            attempt = random.randint(1, 10)

    def check():
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
                flag = False
            else:
                if n < num:
                    print(f'Загаданное число больше {n}')
                else:
                    print(f'Загаданное число меньше {n}')

    return check()


f1 = riddle()
f2 = riddle()

print(f2)
print(f1)
