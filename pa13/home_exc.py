class BaseExceptions(Exception):
    pass


class NegativeValue(BaseExceptions):
    def __init__(self, value):
        self.__value = value

    def __str__(self):
        if isinstance(self.__value, int):
            return f'Value {self.__value} negative and unacceptable to use!'
        else:
            return f'Sorry, bro, but the value "{self.__value}" must be of type int!'


class CreationTimeChangeError(BaseExceptions):
    def __init__(self, var_name):
        self.var_name = var_name

    def __str__(self):
        return f"Cannot change '{self.var_name}' after creation"


class IncorrectMatrixDimensions(BaseExceptions):
    def __init__(self, value):
        self.matrix = value

    def find_max_len_row(self):
        max_len = 0
        for row in self.matrix:
            if len(row) > max_len:
                max_len = len(row)
        return max_len

    def __str__(self):
        for row in self.matrix:
            if len(row) < self.find_max_len_row():
                for _ in range((self.find_max_len_row() - len(row))):
                    row.append('*')
        return 'Incorrect Matrix DimensionsSome! Values are missing in the matrix, they are highlighted with stars(*)\n' + "\n".join(
            f"[{' '.join(str(x) for x in row)}]" for row in self.matrix)
