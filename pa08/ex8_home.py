__all__ = ['get_directory_size', 'what_is_that', 'dir_walker', 'pickle']

import csv
import json
import os
import pickle
from pathlib import Path


def get_directory_size(directory: str) -> int:
    total_size = 0
    for dir_path, dir_names, file_names in os.walk(directory):
        for filename in file_names:
            filepath = os.path.join(dir_path, filename)
            total_size += os.path.getsize(filepath)
    return total_size


def what_is_that(path: str) -> str:
    if os.path.isfile(path):
        return 'file'
    elif os.path.isdir(path):
        return 'directory'
    elif os.path.islink(path):
        return 'symlink'
    else:
        return 'unknown'


def dir_walker(directory: str) -> dict:
    result = {}
    for dir_path, dir_names, file_names in os.walk(directory):
        files = [''] + file_names
        temp_dict = {}
        for objs in files:
            obj_path = os.path.join(dir_path, objs)
            temp_dict['type'] = what_is_that(obj_path)
            if Path(Path().cwd() / directory) == Path(Path().cwd() / obj_path):
                temp_dict['parent'] = '.'
            else:
                temp_dict['parent'] = dir_path
            if temp_dict['type'] == 'file':
                temp_dict['size'] = os.path.getsize(obj_path)
            if temp_dict['type'] == 'directory':
                temp_dict['size'] = get_directory_size(obj_path)
            if temp_dict['type'] == 'symlink':
                temp_dict['size'] = os.path.getsize(os.readlink(obj_path))
            if temp_dict['type'] == 'unknown':
                temp_dict['size'] = 0
            result[obj_path] = dict(temp_dict)
    return result


def dir_walker_to_files(directory_path: str, file_name: str):
    my_dict = dir_walker(directory_path)
    with (
        open(f'{file_name}.plk', 'wb') as pkl_file,
        open(f'{file_name}.json', 'w', encoding='utf-8') as json_file,
        open(f'{file_name}.csv', 'w', encoding='utf-8', newline='') as csv_file
    ):
        pickle.dump(my_dict, pkl_file)

        json.dump(my_dict, json_file, indent=4)

        headers = ['path'] + list(list(my_dict.values())[0].keys())
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)
        for k, v in my_dict.items():
            data_lst = [f'{k}'] + list(v.values())
            csv_writer.writerow(data_lst)


def main():
    dir_walker_to_files('json_for_test', 'dl')


if __name__ == "__main__":
    main()
