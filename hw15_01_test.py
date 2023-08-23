# в терминале: python.exe .\hw15_01_test.py -r 50.0
import logging

from pa15 import par


def main():
    logging.basicConfig(filename='circle.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')
    a = par()
    print(a.get_area())


if __name__ == '__main__':
    main()
