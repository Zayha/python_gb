from ex2 import Factorial2


class Factorial3(Factorial2):

    def __init__(self, *args, **kwargs):
        super().__init__(k=kwargs.get('k', 5), filename=kwargs.get('filename', 'factorial3'))
        if len(args) == 1:
            step = 1
            start = 1
            stop = args[0]
        elif len(args) == 2:
            step = 1
            stop = args[0]
            start = args[1]
        else:
            start = args[0]
            stop = args[1]
            step = args[2]
        if start > stop:
            start, stop = stop, start
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.a == 0:
            self.a = self.start
        if self.a < self.stop:
            result = self.factorial()
            self.a += self.step
            return result
        else:
            raise StopIteration


def main():
    fa3 = Factorial3(1, 11, 2)
    for i in fa3:
        print(i)
    fa3(5)
    print(fa3)


if __name__ == '__main__':
    main()
