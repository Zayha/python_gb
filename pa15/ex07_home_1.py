# При Запуске из корневой папки проекта main.py

from pa10 import Circle
import logging
import argparse


class CircleWL(Circle):

    def __init__(self, radius, log=True):
        self.circle_logger = logging.getLogger()
        self.circle_logger.info(' *' * 40)
        self.circle_logger.info(f'Radius = {radius}, type = {type(radius)}')
        if log:
            if not isinstance(radius, (int, float)):
                self.circle_logger.error(f'Radius must be an integer or float, now Radius = {radius}')
        super().__init__(radius)
        if log:
            self.circle_logger.info(self.__str__())

    def __str__(self):
        return f'Radius = {self.radius}\tCircumference: {self.get_length()}\t Area: {self.get_area()}'


def par():
    parser = argparse.ArgumentParser(description='Подсчет площади и длины окружности')
    parser.add_argument('-r', type=float, help='передайте радиус, приоритет')
    parser.add_argument('-d', type=float, help='передайте диаметр')
    args = parser.parse_args()
    if args.r:
        return CircleWL(args.r)
    else:
        return CircleWL(args.d / 2)


def main():
    par()


if __name__ == '__main__':
    main()
