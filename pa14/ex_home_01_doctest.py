import doctest

from pa10 import Circle


def test_circle():
    """
    >>> c = Circle(5)
    >>> c.get_area()
    78.53981633974483
    >>> c.get_length()
    31.41592653589793
    >>> print(c)
    Circumference: 31.41592653589793
    Area: 78.53981633974483
    >>> ex = Circle('hello')
    Traceback (most recent call last):
        ...
    TypeError: Radius must be an integer or float
    """
    pass


def main():
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()
