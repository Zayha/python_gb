import unittest
from unittest.mock import patch
from pa10 import Circle


class TestCircle(unittest.TestCase):

    def setUp(self) -> None:
        self.x = 5
        self.y = 10
        self.z = 0
        self.c = Circle(self.x)
        self.pi = 3.1415926

    def test_get_area(self):
        area = self.pi * (self.x ** 2)
        self.assertAlmostEqual(self.c.get_area(), area, places=5)
        self.assertNotAlmostEqual(self.c.get_area(), area, places=7)

    def test_ex(self):
        with self.assertRaises(TypeError) as ex:
            Circle('hello')
        self.assertEqual(str(ex.exception), "Radius must be an integer or float")

    # @patch
    # def test_ex2(self):



def main():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()
