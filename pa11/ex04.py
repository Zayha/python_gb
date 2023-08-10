from ex02 import Archive


class NewArch(Archive):
    """
    Класс расширяющий возможности класса Archive, вывод экземпляра на печать и отображение класса с параметрами.
    """

    def __repr__(self):
        return f'{__class__.__name__}({self.pr1},{self.pr2})'

    def __str__(self):
        t = self.kwargs.items()
        gen = (f'{k} = "{v}"' if isinstance(v, str) else f'{k} = {v}' for k, v in t)
        return f'Экземпляр класса {__class__.__name__} с параметрами {", ".join(gen)}'


def main():
    na1 = NewArch(pr1=123, pr2='lalala')
    print(na1)


if __name__ == '__main__':
    main()
