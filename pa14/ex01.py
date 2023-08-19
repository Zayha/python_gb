import doctest
import re
import unittest


def remove_non_latin_chars(text: str) -> str:
    """
    Функция удаляет все кроме букв латинского алфавита и пробелов.
    :param text: Любая строка.
    :return: Возвращается строка в нижнем регистре без лишних символов.

    >>> remove_non_latin_chars('hello world')
    'hello world'

    >>> remove_non_latin_chars('Hello World')
    'hello world'

    >>> remove_non_latin_chars('hello world!')
    'hello world'

    >>> remove_non_latin_chars('hello world на')
    'hello world '

    >>> remove_non_latin_chars('Hello World! где')
    'hello world '
    """
    latin_pattern = r'[^a-zA-Z\s]'
    return re.sub(latin_pattern, '', text).lower()


class TestRemoveNonLatinChars(unittest.TestCase):
    def test_no_changes(self):
        self.assertEqual(remove_non_latin_chars('hello world'), 'hello world')

    def test_change_case(self):
        self.assertEqual(remove_non_latin_chars('Hello World'), 'hello world')

    def test_remove_punctuation(self):
        self.assertEqual(remove_non_latin_chars('hello world!'), 'hello world')

    def test_remove_non_latin_chars_n_sp(self):
        self.assertEqual(remove_non_latin_chars('hello world на'), 'hello world ')

    def test_combi_mode(self):
        self.assertEqual(remove_non_latin_chars('Hello World! где'), 'hello world ')


# print(remove_non_latin_chars(' Ах ты грязное животнаеhello'))
# doctest.testmod()


def main():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()
