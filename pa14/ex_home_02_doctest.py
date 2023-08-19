import doctest

from pa10 import AnimalsFabric


def animals_fabric_test():
    """
    >>> f1 = AnimalsFabric(a_type='Ant', name='Big Djo', age=5, weight=33)
    >>> an = f1.create_animal()
    >>> print(an)
    Big Djo is 5 years old and 33 kg and antenna length is None mm
    >>> f2 = AnimalsFabric(a_type='Wife', name='Big Bro', age=5, weight=33)
    >>> f2.create_animal()
    Traceback (most recent call last):
        ...
    ValueError: Unsupported animal type
    >>> print(an.antenna_length)
    None
    """
    pass

    def main():
        doctest.testmod(verbose=True)

    if __name__ == '__main__':
        main()
