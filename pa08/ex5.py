__all__ = ["json_to_pickle", 'json_files_list']

import json
import os
import pickle
from pathlib import Path


def json_files_list(files_lst: list) -> list:
    return [file for file in files_lst if file.endswith('.json')]


def json_to_pickle(path: str):
    files = next(os.walk(path))[2]
    files = json_files_list(files)
    print(files)
    for file in files:
        print(file)
        new_file = Path(Path().cwd() / path / Path(file).stem).with_suffix('.pkl')
        with (open(new_file, 'wb') as f_pickle,
              open(Path(Path().cwd() / path / file), 'r', encoding='utf-8') as f_json):
            pickle.dump(json.load(f_json), f_pickle)


def main():
    json_to_pickle('json_for_test')


if __name__ == '__main__':
    main()
