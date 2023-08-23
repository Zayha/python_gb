from pa13 import IncorrectMatrixDimensions
from pa11 import Matrix
import logging
import argparse


class MyMatrixArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Подсчет площади и длины окружности')
        self.parser.add_argument('--matrix', nargs='+', type=int, help='передайте радиус, приоритет',
                                 required=True)
        self.parser.add_argument('--row', type=int, help='кол-во строк', required=True)
        self.parser.add_argument('--col', type=int, help='кол-во столбцов', required=True)
        self.args = self.parser.parse_args()
        if self.check_len():
            self.matrix = self._split_list_into_matrix()
            print(self.matrix)

    def check_len(self):
        return True if (self.args.row * self.args.col) == len(self.args.matrix) else False

    def _split_list_into_matrix(self):
        return [self.args.matrix[i:i + self.args.row] for i in range(0, len(self.args.matrix), self.args.row)]

    def get_matrix(self):
        return self.matrix


class MatrixLog(Matrix):

    def __init__(self, matrix: list):
        self.matrix_logger = logging.getLogger()
        self.matrix_logger.info(f'Matrix:\n {Matrix(matrix=matrix).__str__()}')
        if not self.is_valid_matrix(matrix=matrix):
            self.matrix_logger.error(f'{IncorrectMatrixDimensions(value=matrix)}')
        super().__init__(matrix=matrix)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            self.matrix_logger.error(
                f'Error from multiple\n {self}  \n*MUL*\n  {other}\nNumber of columns in the first matrix '
                f'must match the number of rows in the second matrix')
            raise ValueError(
                "Number of columns in the first matrix must match the number of rows in the second matrix")

        rows = len(self.matrix)
        cols = len(other.matrix[0])
        result = self._create_zero_matrix(rows, cols)

        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        self.matrix_logger.info(f'Mult, Result:\n {Matrix(matrix=result)}')
        return Matrix(matrix=result)


def main():
    a = MyMatrixArgParser()


if __name__ == '__main__':
    main()
