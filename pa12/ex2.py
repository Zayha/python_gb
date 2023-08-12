import json
import random

from ex1 import Factorial


class Factorial2(Factorial):

    def __init__(self, k, filename='factorial2'):
        super().__init__(k)
        self.filename = f'{filename}.json'

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        json.dump(self.history, self.file)
        self.file.close()


def main():
    f1 = Factorial2(5)
    with f1 as fa:
        for _ in range(7):
            x = random.randint(1, 1000)
            fa(x)


if __name__ == '__main__':
    main()
