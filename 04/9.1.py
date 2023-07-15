# Напишите функцию для транспонирования матрицы
def check_matrix(matrix: list) -> bool:
    if isinstance(matrix, list):
        if len(matrix) < 2:
            return True if len(matrix) == 1 else False
        else:
            row_lengths = [len(row) for row in matrix]
            return all(length == row_lengths[0] for length in row_lengths)
    return False


def transpose_matrix(matrix: list) -> list | None:
    return list(zip(*matrix)) if check_matrix(matrix) else None


print(transpose_matrix([['a', 1, 4], ['b', 2, 5], ['c', 3, 6]]))
