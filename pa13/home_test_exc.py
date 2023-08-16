import datetime
import time

from pa12.ex1 import Factorial
from pa11 import MyString, Matrix
from home_exc import NegativeValue, CreationTimeChangeError, IncorrectMatrixDimensions


class FactorialWBE(Factorial):
    def __call__(self, *args, **kwargs):
        if isinstance(args[0], int) and args[0] > 0:
            self.a = args[0]
            return self.factorial()
        else:
            raise NegativeValue(args[0])


class MyStringWBE(MyString):

    def __new__(cls, value, *args, **kwargs):
        """
        :param kwargs: принимает именованный параметр author, строка для авторства текста
        """
        instance = super().__new__(cls, value)
        instance.author = kwargs.get('author', None)
        instance._creation_time = time.time()
        instance.__dict__["__creation_time_set"] = False
        return instance

    @property
    def creation_time(self):
        formatted_time = datetime.datetime.fromtimestamp(self._creation_time).strftime('%H:%M:%S')
        formatted_date = datetime.datetime.fromtimestamp(self._creation_time).strftime('%d/%m/%Y')
        return f'{formatted_time}\t{formatted_date}'

    # Защита от изменений =)
    def __setattr__(self, name, value):
        if name == "_creation_time" and hasattr(self, "__creation_time_set"):
            raise CreationTimeChangeError('_creation_time')
        super().__setattr__(name, value)


class MatrixWBE(Matrix):
    def __init__(self, matrix: list):
        if self.is_valid_matrix(matrix=matrix):
            self.matrix = matrix
        else:
            raise IncorrectMatrixDimensions(matrix)
        super().__init__(matrix=matrix)


def main():
    # f1 = FactorialWBE(5)
    # print(f1(-5))

    # ms = MyStringWBE('Trololo')
    # print(ms.creation_time)
    # ms._creation_time = 123

    ma1 = [[1, 2, 3, 4, 5], [3, 4, 5, 6, 7, 10, 11], [3, 4, 5, 6, 7]]
    m1 = MatrixWBE(matrix=ma1)


if __name__ == '__main__':
    main()
