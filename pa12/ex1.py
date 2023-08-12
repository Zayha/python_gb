class Factorial:
    def __init__(self, k):
        self.k = k
        self.history = {}
        self.a = 0

    def factorial(self):
        if self.a in self.history.keys():
            result = self.history[self.a]
        else:
            if self.a == 1 or self.a == 0:
                result = 1
            else:
                result = 1
                for i in range(2, self.a + 1):
                    result *= i
        if len(self.history) <= self.k:
            self.history[self.a] = result
        else:
            self.history.popitem()
            self.history[self.a] = result
        return result

    def __str__(self):
        return f'{self.a}! = {self.history[self.a]}'

    def show_history(self):
        return '\n'.join(f'{k}! = {v}' for k, v in self.history.items())

    def __call__(self, *args, **kwargs):
        if isinstance(args[0], int) and args[0] > 0:
            self.a = args[0]
            return self.factorial()
        else:
            raise ValueError(f'{args[0]} - недопустимое значение!')



def main():
    f1 = Factorial(5)
    print(f1(3))
    f1(1)
    f1(101)
    # print(f1.show_history())
    f1(2)
    f1(2)
    f1(2)
    f1(222)
    print(f1.show_history())


if __name__ == '__main__':
    main()
