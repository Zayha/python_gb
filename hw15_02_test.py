import logging

from pa15 import MatrixLog, MyMatrixArgParser


def main():
    logging.basicConfig(filename='matrix.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

    a = MyMatrixArgParser()
    oth = [[1, 2, 4], [3, 4, 6]]
    m1 = MatrixLog(matrix=oth)
    m2 = MatrixLog(matrix=a.get_matrix())
    m_m = m1 * m2
    print(m_m)


if __name__ == '__main__':
    main()

# В терминале: python.exe .\hw15_02_test.py --matrix 1 2 3 4 5 6 --row 3 --col 2
