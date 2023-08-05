from ex03 import Human


class Employee(Human):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._id = kwargs.get('id', 0)
        self.access_level = sum(int(digit) for digit in str(self._id)) % 7


def main():
    e1 = Employee(id=177, name='John Doe', date_of_birth='11.07.1984')
    print(e1.access_level)
    print(e1.get_age())


if __name__ == '__main__':
    main()
