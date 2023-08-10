class Rectangle:
    """
    Класс для обработки прямоугольников
    """
    def __init__(self, *args, **kwargs):
        """
        :param args: принимает 2 параметра ширину и высоту или 1 если это квадрат
        """
        if len(args) == 1:
            self.length = args[0]
            self.width = args[0]
        else:
            self.length, self.width, *_ = args

    def get_perimeter(self):
        return 2 * self.length + 2 * self.width

    def get_area(self):
        return self.length * self.width

    def __str__(self):
        return f'Rectangle area: {self.get_area()}, perimeter: {self.get_perimeter()}'


def main():
    r = Rectangle(10, 20)
    r1 = Rectangle(10)
    print(r, '\n', r1)


if __name__ == '__main__':
    main()
