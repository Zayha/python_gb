class BaseExceptions(Exception):
    pass


class LevelException(BaseExceptions):
    def __init__(self, value: str, min_level: int, max_level: int):
        self._value = int(value)
        self._min_level = min_level
        self._max_level = max_level

    def __str__(self):
        return f'Недопустимый уровень доступа(level = {self._value}), подходящие [{self._min_level}, {self._max_level}]'


class AccessException(BaseExceptions):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value = }, в доступе отказано'


def test():
    min_level = 3
    max_level = 10
    l = input('Select your level: ')
    if not l.isdigit():
        raise AccessException(l)
    elif not min_level <= int(l) <= max_level:
        raise LevelException(l, min_level, max_level)


def main():
    test()


if __name__ == '__main__':
    main()
