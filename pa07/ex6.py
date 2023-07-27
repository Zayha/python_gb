__all__ = ['file_generator_3', '_check_dir']

import os
from pathlib import Path
from . import file_generator_2

"""
file_ext: str, min_f_name_len: int = 6, max_f_name_len: int = 30, byte_min: int = 256,
                   byte_max: int = 4096, file_qty: int = 42, work_dir: str = 'out_ex4'"""


def file_generator_3(**kwargs):
    _check_dir(kwargs.get('work_dir'))
    file_generator_2(**kwargs)


def _check_dir(dir_name: str | None) -> bool:
    if dir_name is None:
        return False
    elif Path(dir_name).exists():
        return True
    else:
        Path(dir_name).mkdir(parents=True)
        return True


# def _get_files(path: str) -> set:
#     return set(file for _, _, files in os.walk(Path(Path.cwd() / path)) for file in files)


if __name__ == '__main__':
    # _check_dir('sholom/poc')
    file_generator_3(files=[('mp3', 2), ('mp4', 30), ('txt', 10), ('doc', 11)], work_dir='new')
    # _get_files('new')
