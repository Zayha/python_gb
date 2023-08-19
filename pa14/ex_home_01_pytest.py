import math

from pa10 import Circle
import pytest


def area():
    x = 5
    pi = 3.1415926
    return pi * (x ** 2)


def setup():
    return Circle(5)


def test_get_area():
    assert math.isclose(area(), setup().get_area(), rel_tol=1e-5)


def test_raise_ex():
    with pytest.raises(TypeError):
        c_ex = Circle('hello')


def main():
    pytest.main(['-v'])


if __name__ == '__main__':
    main()
