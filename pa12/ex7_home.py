import csv
import pickle
import re


class NameDescriptor:

    @classmethod
    def check_name(cls, name: str) -> bool:
        if isinstance(name, str):
            if name[0].isupper() and not bool(re.search(r'\d', name)):
                return True
            else:
                raise ValueError
        else:
            raise TypeError

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        self.check_name(value)
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __str__(self):
        return self.name


class Student:
    first_name = NameDescriptor()
    patronymic = NameDescriptor()
    last_name = NameDescriptor()

    def __init__(self, first_name: str = 'A', patronymic: str = 'A', last_name: str = 'A'):
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        self._subject_taught = self._read_csv()

    def __str__(self):
        return f'ФИО: {self.first_name}\t{self.patronymic}\t{self.last_name}\n' \
               f'Предметы: {", ".join(self._subject_taught.keys())}\n' \
               f'Средний балл: {self.average_grade_score[1]:.2f}'

    def __eq__(self, other):
        return self.average_grade_score == other.average_grade_score

    def __lt__(self, other):
        return self.average_grade_score < other.average_grade_score

    def __le__(self, other):
        return self.average_grade_score <= other.average_grade_score

    def __gt__(self, other):
        return self.average_grade_score > other.average_grade_score

    def __ge__(self, other):
        return self.average_grade_score >= other.average_grade_score

    @staticmethod
    def _read_csv(file_name: str = 'st.csv'):

        with open(file_name, 'r', encoding='utf-8', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            c = 0
            lst = []
            for row in csv_reader:
                if c == 0:
                    # header = row
                    c += 1
                else:
                    lst.append(row)
        return {i[0]: {'grade': [], 'test': []} for i in lst}

    def __add_score(self, subject: str, grade: int, score_type: str):
        if isinstance(subject, str):
            if subject in self._subject_taught.keys():
                if isinstance(grade, int):
                    if score_type == 'test':
                        if 0 <= grade <= 100:
                            self._subject_taught[subject]['test'].append(grade)
                        else:
                            raise ValueError('grade in test [0 to 100]')
                    elif score_type == 'grade':
                        if 2 <= grade <= 5:
                            self._subject_taught[subject]['grade'].append(grade)
                        else:
                            raise ValueError('grade in [2 to 5]')
                    else:
                        raise ValueError(f'{score_type = } must be "test" or "grade"')
                else:
                    raise TypeError
            else:
                raise ValueError(f"Haven't subject {subject = }, just subject = {self._subject_taught}")
        else:
            raise ValueError

    def add_test(self, subject: str, score: int):
        self.__add_score(subject, score, 'test')

    def add_grade(self, subject: str, score: int):
        self.__add_score(subject, score, 'grade')

    @property
    def average_rating(self):
        result = {i[0]: {'grade': None, 'test': None} for i in self._subject_taught.items()}
        for k, v in self._subject_taught.items():
            grade_lst = v['grade']
            test_lst = v['test']
            if len(grade_lst) > 0:
                average = sum(grade_lst) / len(grade_lst)
                result[k]['grade'] = average
            if len(test_lst) > 0:
                average = sum(test_lst) / len(test_lst)
                result[k]['test'] = average
        return result

    @property
    def average_grade_score(self):
        lst = []
        for _, v in self._subject_taught.items():
            lst += v['grade']
        if len(lst) > 0:
            s = sum(lst) / len(lst)
            return [f'Average score for all subjects = {s:.2f}', s]
        else:
            return [f"Haven't average score!", 0]

    def save_student(self, file_name: str):
        with open(f'{file_name}.pkl', 'wb') as pkl_file:
            pickle.dump(self, pkl_file)

    def load_student(self, file_name: str):
        with open(f'{file_name}.pkl', 'rb') as pkl_file:
            obj = pickle.load(pkl_file)
            self.__dict__.update(obj.__dict__)


def main():
    x = Student('Vasya', 'Ivanovich', 'Pupkin')

    print(x.patronymic)
    x.add_test('химия', 100)
    x.add_test('химия', 50)
    x.add_test('химия', 30)
    x.add_grade('матан', 5)
    x.add_grade('матан', 3)
    x.add_grade('матан', 4)

    print(x.average_rating)
    print(x.average_grade_score)
    print(x)
    x.save_student('x1')
    x1 = Student()
    x1.load_student('x1')
    print(x1)
    print(x1.average_rating)
    print(x == x1)
    x1.add_grade('матан', 5)
    print(x1 > x)


if __name__ == '__main__':
    main()
