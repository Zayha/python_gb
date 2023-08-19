import unittest

from pa11 import RectanglePro2


class TestRectanglePro2(unittest.TestCase):

    def setUp(self) -> None:
        self.rect1 = RectanglePro2(4, 5)
        self.rect2 = RectanglePro2(5, 6)
        self.rect3 = RectanglePro2(5, 4)
        self.rect4 = RectanglePro2(4, 4)
        self.rect5 = RectanglePro2(2, 7)
        self.square = RectanglePro2(4)

    def test_equal(self):
        self.assertTrue(self.rect1 == self.rect1)
        self.assertTrue(self.rect2 == self.rect2)
        self.assertTrue(self.rect1 == self.rect1)
        self.assertTrue(self.rect1 == self.rect3)
        self.assertTrue(self.square == self.square)
        self.assertTrue(self.square == self.rect4)

    def test_not_equal(self):
        self.assertFalse(self.rect1 == self.rect4)
        self.assertFalse(self.rect2 == self.rect3)
        self.assertTrue(self.rect4 != self.rect1)

    def test_S(self):
        self.assertEqual(self.square.get_area(), self.rect4.get_area())
        self.assertEqual(self.rect1.get_area(), self.rect3.get_area())
        self.assertNotEqual(self.rect1.get_area(), self.rect2.get_area())

    def test_p(self):
        self.assertEqual(self.rect1.get_perimeter(), self.rect3.get_perimeter())
        self.assertEqual(self.rect1.get_perimeter(), self.rect5.get_perimeter())
        self.assertEqual(self.rect3.get_perimeter(), self.rect5.get_perimeter())
        self.assertEqual(self.rect4.get_perimeter(), self.square.get_perimeter())
        self.assertNotEqual(self.square.get_perimeter(), self.rect5.get_perimeter())


def main():
    unittest.main()


if __name__ == '__main__':
    main()
