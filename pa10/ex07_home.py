from ex05_06 import Fish, Ant, Bird


class AnimalsFabric:
    def __init__(self, a_type, name, age, weight, **kwargs):
        self.a_type = a_type
        self.name = name
        self.age = age
        self.weight = weight
        self.kwargs = kwargs
        self.__animals_classes = [Fish, Bird, Ant]
        # print(globals())
        self.animals_names = [i.__name__ for i in self.__animals_classes]

    def create_animal(self):
        if self.a_type in self.animals_names:
            return globals()[self.a_type](self.name, self.age, self.weight, **self.kwargs)
        else:
            raise ValueError("Unsupported animal type")


def main():
    a = AnimalsFabric(a_type='Ant', name='Tom', age=10, weight=100)
    a.antenna_length = 50
    x = a.create_animal()
    x.antenna_length = 120
    print(type(x), x)


if __name__ == '__main__':
    main()
