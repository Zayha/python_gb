from .ex05 import RectanglePro


class RectanglePro2(RectanglePro):
    """
    Класс расширяющий возможности класса RectanglePro,
    добавлены методы сравнения (>, <, >=, <=, !=).
    """

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()


def main():
    r1 = RectanglePro2(10)
    r2 = RectanglePro2(20, 20)
    r3 = RectanglePro2(30)
    print(r1 + r2 == r3)
    print(r1 + r2 >= r3)
    print(r1 + r2 > r3)
    print(r1 != r3)


if __name__ == '__main__':
    main()
