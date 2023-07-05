from random import randint


def num_game():
    win = False
    counter = 1
    num = randint(0, 1000)
    print(num)
    get_num = input('Я загадал целое число, попробуй угадать, значение лежит в пределе 0 - 1000: ')
    msg = 'Ты проиграл из за своей глупости, научить читать!'
    msg_win = 'Тебе повезло на этот раз! Ты угадал...'
    while not win:
        print(f'cou = {counter}')
        if get_num.isdigit():
            n = int(get_num)
            if n < 0 or n > 1000:
                break
            else:
                if n == num:
                    win = True
                    break
                elif n > num:
                    print(f'Загаданное число меньше чем {n}')
                else:
                    print(f'Загаданное число больше чем {n}')
                #
                counter += 1
                if counter < 10:
                    get_num = input(f'Попробуй ещё угадать(это попытка № {counter} из 10 доступных): ')
        else:
            break
    print(msg_win if win else msg)


num_game()