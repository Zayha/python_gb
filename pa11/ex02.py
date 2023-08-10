def is_float(f: str | float | int) -> bool:
    try:
        float(f)
        return True
    except ValueError:
        return False


class Archive:
    """
    Best class - Archive
    """
    _arc_1 = []
    _arc_2 = []

    def __init__(self, *args, **kwargs):
        """
        :param kwargs: принимает два именованных параметра pr1: int или float и pr2: str
        """
        pr1 = kwargs.get('pr1', None)
        pr2 = kwargs.get('pr2', None)
        self.args = args
        self.kwargs = kwargs
        if pr1 is not None:
            if is_float(pr1):
                self.pr1 = float(pr1)
            else:
                raise TypeError('Incorrect pr1')
        else:
            raise ValueError('Incorrect pr1')
        if isinstance(pr2, str):
            self.pr2 = pr2
        else:
            raise TypeError('Incorrect pr2')
        self._arc_1.append(pr1)
        self._arc_2.append(pr2)

        # self.a1 = self._arc_1[::]
        # self.a2 = self._arc_2[::]

    def __str__(self):
        return str(self._arc_1) + '\t' + str(self._arc_2)

    def __repr__(self):
        return f"{__class__.__name__}({self.pr1}, '{self.pr2}')"

    def get_arc(self):
        """
        :return: возвращает строку с раскладкой двух списков _arc_1 и _arc_2 через табуляцию
        """
        return str(self._arc_1) + '\t' + str(self._arc_2)


def main():
    a1 = Archive(pr1=123, pr2='123')
    a2 = Archive(pr1=1234, pr2='acb')
    print(a1.get_arc())
    print(a2.get_arc())
    print(a2.get_arc())
    print(repr(a2))


if __name__ == '__main__':
    main()
