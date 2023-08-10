import time


class MyString(str):
    """
    MyString class, same str, but better
    """

    def __new__(cls, value, *args, **kwargs):
        """
        :param kwargs: принимает именованный параметр author, строка для авторства текста
        """
        instance = super().__new__(cls, value)
        instance.author = kwargs.get('author', None)
        instance._creation_time = time.time()

        return instance

    def __str__(self):
        return f"{super().__str__()}\tauthor='{self.author}')"

    def __repr__(self):
        return f"{__class__.__name__}({super().__repr__()}, author='{self.author}')"


def main():
    t1 = MyString('Lalala', author='Ku')
    t2 = MyString('Tralala', author='Ku')
    # print(f'{t1 = }\t{t2 = }\t{t1 + t2 = }\t{t1.author}/{t1._creation_time}')
    print(t1)
    print(repr(t1))


if __name__ == '__main__':
    main()
