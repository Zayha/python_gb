def check_exception():
    num = ''
    flag = True
    while flag:
        num = input('Введите число типа int или float: ')
        try:
            float(num)
            num = False
        except ValueError as e:
            print(e, 'try again!')
    return int(num) if num.isdigit() else float(num)


def main():
    print(check_exception())


if __name__ == '__main__':
    main()
