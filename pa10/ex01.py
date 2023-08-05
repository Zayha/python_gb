import math


class Circle:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('Radius must be an integer or float')
        else:
            self.radius = abs(radius)

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_length(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f'Circumference: {self.get_length()}\nArea: {self.get_area()}'


def main():
    c1 = Circle(10)
    print(c1)


if __name__ == '__main__':
    main()
