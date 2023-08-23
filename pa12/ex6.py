from pa10 import Rectangle


class DescriptorTest:

    @classmethod
    def check_value(cls, value):
        if not isinstance(value, int):
            raise TypeError("Должно быть задано целое число")
        if value < 0:
            raise ValueError("Значение должно быть положительным")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)


class NRec(Rectangle):
    length = DescriptorTest()
    width = DescriptorTest()


# class Rectangle:
#     """
#     Класс для обработки прямоугольников
#     """
#     length = DescriptorTest()
#     width = DescriptorTest()
#
#     def __init__(self, *args):
#         """
#         :param args: принимает 2 параметра ширину и высоту или 1 если это квадрат
#         """
#         if len(args) == 1:
#             self.length = args[0]
#             self.width = args[0]
#         else:
#             self.length, self.width, *_ = args
#
#     def get_perimeter(self):
#         return 2 * self.length + 2 * self.width
#
#     def get_area(self):
#         return self.length * self.width
#
#     def __str__(self):
#         return f'Rectangle area: {self.get_area()}, perimeter: {self.get_perimeter()}'


def main():
    x = Rectangle(1, 2)
    x.length = 5
    x.length = 3
    print(x.__dict__)


if __name__ == '__main__':
    main()
