class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return f'{self.name} is {self.age} years old and {self.weight} kg'

    def get_data(self):
        return f'{self.name} is {self.age} years old and {self.weight} kg'


class Fish(Animal):
    def __init__(self, name, age, weight, **kwargs):
        super().__init__(name, age, weight)
        self.fish_scales = True if kwargs.get('fish_scales', None) is not None else False

    def __str__(self):
        return f'{self.name} is {self.age} years old and {self.weight} kg and fish scales is {self.fish_scales}'


class Bird(Animal):
    def __init__(self, name, age, weight, **kwargs):
        super().__init__(name, age, weight)
        self.flight_altitude = kwargs.get('flight_altitude', None)
        self.flight_speed = kwargs.get('flight_speed', None)

    def __str__(self):
        return f'{self.name} is {self.age} years old and {self.weight} kg and flight altitude is {self.flight_altitude} and flight speed is {self.flight_speed}'


class Ant(Animal):
    def __init__(self, name, age, weight, **kwargs):
        super().__init__(name, age, weight)
        self.antenna_length = kwargs.get('antenna_length', None)

    def __str__(self):
        return f'{self.name} is {self.age} years old and {self.weight} kg and antenna length is {self.antenna_length} mm'


def main():
    b = Bird('Bird', 1, 100, fish_scales=True)
    print(b)
    f = Fish('Fish', 1, 100, fish_scales=100, )
    print(f, f.get_data())


if __name__ == '__main__':
    main()
