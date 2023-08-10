from pa10 import Rectangle


class RectanglePro(Rectangle):
    """
    Класс расширяющий возможности класса Rectangle,
    добавлены математические операции сложения и вычитания.
    """

    def __add__(self, other):
        return RectanglePro(self.length + other.length, self.width + other.width)

    def __sub__(self, other):
        return RectanglePro(abs(self.length - other.length), abs(self.width - other.width))


def main():
    rp1 = RectanglePro(10, 20)
    rp2 = RectanglePro(20, 30)
    rp3 = rp1 - rp2
    print(rp3.get_perimeter())


if __name__ == '__main__':
    main()
