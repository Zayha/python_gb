class Matrix:
    """
    Класс для операций с матрицами: сложение, умножение, проверка валидности, сравнение матриц.
    """

    def __init__(self, matrix: list):
        if self.is_valid_matrix(matrix=matrix):
            self.matrix = matrix
        else:
            raise ValueError('Invalid matrix dimensions!!!')

    @staticmethod
    def _create_zero_matrix(rows: int, cols: int) -> list:
        """
        Создает матрицу нужного размера с ячейками заполненными нулями
        :param rows: кол-во строк
        :param cols: кол-во столбцов
        :return: возвращает матрицу в виде списка со списками.
        """
        return [[0 for _ in range(cols)] for _ in range(rows)]

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrix dimensions must match for addition")

        rows = len(self.matrix)
        cols = len(self.matrix[0])
        result = self._create_zero_matrix(rows, cols)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError(
                "Number of columns in the first matrix must match the number of rows in the second matrix")

        rows = len(self.matrix)
        cols = len(other.matrix[0])
        result = self._create_zero_matrix(rows, cols)

        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(matrix=result)

    def __eq__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return False

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __str__(self):
        return "\n".join(f"[{' '.join(str(x) for x in row)}]" for row in self.matrix)

    def __repr__(self):
        return f'{__class__.__name__}(matrix={self.matrix})'

    @staticmethod
    def is_valid_matrix(matrix: list) -> bool:
        if not matrix:
            return False

        num_columns = len(matrix[0])
        for row in matrix:
            if len(row) != num_columns:
                return False

        return True


def main():
    ma1 = [[1, 2, 3, 4, 5], [3, 4, 5, 6, 7], [3, 4, 5, 6, 7]]
    ma2 = [[0, 10, 3, 4], [20, 50, 3, 4], [20, 50, 3, 4], [20, 50, 3, 4], [20, 50, 3, 4]]
    m1 = Matrix(matrix=ma1)
    m2 = Matrix(matrix=ma2)
    m_mult = m1 * m2
    print(m_mult)
    print(ma1 == ma2)
    m5 = Matrix(matrix=[[1, 2, 3], [1, 2, 3]])
    m6 = Matrix(matrix=[[1, 2, 3], [1, 2, 3]])
    print(m5 != m6)
    print(repr(m6))
    print(repr(m_mult))


if __name__ == '__main__':
    main()
