from pa10 import Rectangle


class Rectangle2(Rectangle):
    __slots__ = ['length', 'width']

    @property
    def rectangle_length(self):
        return self.length

    @rectangle_length.setter
    def rectangle_length(self, value):
        if isinstance(value, int) and value >= 0:
            self.length = value
        else:
            raise ValueError

    @property
    def rectangle_width(self):
        return self.width

    @rectangle_width.setter
    def rectangle_width(self, value):
        if isinstance(value, int) and value >= 0:
            self.width = value
        else:
            raise ValueError


def main():
    r = Rectangle2(1, 2)
    print(r)
    r.rectangle_width = 10
    print(r)
    r.rectangle_length = 11
    print(r)
    r.rectangle_length = 1
    print(r)
    r.rectangle_length = 10000
    print(r)
    print(r.__dict__)


if __name__ == '__main__':
    main()
