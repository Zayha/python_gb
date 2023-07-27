__all__ = ['mass_changes', 'clean_file_name']

import os
import shutil
from pathlib import Path
import re


def clean_file_name(file_name: str) -> str:
    """
    удаляет недопустимые символы в имени файла
    :param file_name: исходное имя файла
    :return: возвращает строку из оставшихся допустимых символов
    """
    return re.sub(r'[\\/:"*?<>|]', '', file_name)


def mass_changes(get_file_ext: str = 'txt', num_format: int = 7, out_ext: str = 'xtx',
                 slice_from: int = 0, slice_to: int = 4, path: str = 'new', new_path: str = 'new', **kwargs):
    """
    Функция группового переименования файлов
    :param get_file_ext: расширение файлов для массового переименования (по умолчанию: 'txt')
    :param num_format: форматирование, сколько знаков, т.е. при 3, формат '001' (по умолчанию: 7)
    :param out_ext: новое расширение файлов (по умолчанию: 'xtx')
    :param slice_from: начало диапазона символов от исходного имени (по умолчанию: 0)
    :param slice_to: окончание диапазона символов от исходного имени (по умолчанию: 4)
    :param path: тут можно задать папку относительно исполняемого файла для работы в ней, прим 'new'(по умолчанию: 'new')
    :param new_path: задать каталог, куда будут перенесены переименованные файлы, прим. 'new/out' (по умолчанию: 'new')
    :param kwargs: new_part_name: необязательный параметр, задает часть имени нового файла
    """
    counter = 0
    if path is not None and Path(path).exists():
        files = [file for _, _, files in os.walk(Path(Path.cwd() / path)) for file in files]
        for file in files:
            # *f_part_name, ex = file.split(".")
            # name = ''.join(f_part_name)
            name = Path(file).stem
            ex = Path(file).suffix[1:]
            if kwargs.get('new_part_name'):
                new_part_name = clean_file_name(kwargs.get('new_part_name'))
            else:
                new_part_name = ''
            if ex == get_file_ext:
                num_form = f'0{num_format}d'
                new_name = f'{name[slice_from:slice_to]}_{new_part_name}_{counter:{num_form}}.{out_ext}'
                print(file, '   >>>>   ', new_name)
                new_path_full = Path(Path.cwd() / new_path / new_name)
                new_path_full.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(Path(Path.cwd() / path / file), new_path_full)
                counter += 1
                if len(str(counter)) > num_format:
                    num_format += 1


if __name__ == '__main__':
    mass_changes(new_part_name='op:', new_path='out_mass2', get_file_ext='doc', num_format=15)
