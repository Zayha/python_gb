from ex01 import remove_non_latin_chars
import pytest


def test_no_changes():
    assert remove_non_latin_chars('hello world') == 'hello world'


def test_change_case():
    assert remove_non_latin_chars('Hello World') == 'hello world'


def test_remove_punctuation():
    assert remove_non_latin_chars('hello world!') == 'hello world'


def test_remove_non_latin_chars_n_sp():
    assert remove_non_latin_chars('hello worldЫ') == 'hello world'


def test_combi_mode():
    assert remove_non_latin_chars('Ю!Hello World!') == 'hello world'


def main():
    pytest.main()


if __name__ == '__main__':
    main()
