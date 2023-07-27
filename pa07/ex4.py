__all__ = ['file_generator', '_get_files']

import os
import random
from pathlib import Path

from . import pseudo_name


def file_generator(file_ext: str = 'txt', min_f_name_len: int = 6, max_f_name_len: int = 30, byte_min: int = 256,
                   byte_max: int = 4096, file_qty: int = 42, work_dir: str = 'out_ex4', **kwargs):
    file_names = set()
    while len(file_names) != file_qty:
        file_name = f'{pseudo_name(min_f_name_len, max_f_name_len, False)}.{file_ext}'
        if file_name not in _get_files(work_dir):
            file_names.add(file_name)
    for file in file_names:
        raw_data = os.urandom(random.randint(byte_min, byte_max))
        with open(f'./{work_dir}/{file}', 'wb') as f:
            f.write(raw_data)


def _get_files(path: str) -> set:
    # my_dir = Path(Path.cwd() / path)
    # result = []
    # for _, _, file in os.walk(Path(Path.cwd() / path)):
    #     result.append(file)
    # return set(result)
    return set(file for _, _, files in os.walk(Path(Path.cwd() / path)) for file in files)


if __name__ == '__main__':
    file_generator()
