# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os
import sys


def get_tuple(string: str = '', this_file: bool = False) -> tuple | None:
    """
    :param string: Строка содержит абсолютный путь к файлу,
    :param this_file: True - если необходимо получить кортеж от исполняемого файла.
    :return: Возвращает кортеж из трех элементов - путь, имя файла, расширение файла.
    """
    if this_file:
        string = os.path.abspath(sys.argv[0])
    #     print(type(string), string)
    div = None
    if string.find('//') > -1:
        div = '//'
    elif string.find('\\\\') > -1:
        div = '\\\\'
    elif string.find('/') > -1:
        div = '/'
    elif string.find("\\") > -1:
        div = '\\'
    elif div is None:
        return None
    *path, file = string.split(div)
    *file_name, ext = file.split('.')
    path = div.join(path)
    file_name = '.'.join(file_name)
    return path, file_name, ext


print(get_tuple('c:/234/papka/df.txt'))
print(get_tuple(this_file=True))
