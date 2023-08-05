from datetime import datetime


class Human:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name') if kwargs.get('name') else None
        self.patronymic = kwargs.get('patronymic') if kwargs.get('patronymic') else None
        self.surname = kwargs.get('surname') if kwargs.get('surname') else None
        self._date_format = '%d.%m.%Y'
        if kwargs.get('date_of_birth'):
            self.date_of_birth = datetime.strptime(kwargs['date_of_birth'], self._date_format)
        else:
            self.date_of_birth = None
        self.__age = self.get_age()

    def get_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    def __str__(self):
        return f'{self.name} {self.patronymic} {self.surname}, d of birth {self.__age}'

    def birthday(self):
        self.__age += 1


def main():
    h1 = Human(name='Andrew', date_of_birth='11.07.1984')
    print(h1)
    h1.date_of_birth = '11.09.1984'
    print(h1)
    h1.birthday()
    print(h1)


if __name__ == '__main__':
    main()
