__all__ = ['file3_to_json']

import json

from pa07 import create_new_file_ex3, pseudo_name, add_num


def file3_to_json(file_inp: str, file_out: str):
    with (
        open(file_inp, 'r', encoding='utf-8') as input_file,
        open(file_out, 'w', encoding='utf-8') as output_file,
    ):
        my_dict = {k.title(): v for line in input_file for k, v in [line.split()]}
        json.dump(my_dict, output_file, ensure_ascii=False, indent=2)


def main():
    # add_num('file1.txt', 50)
    # for _ in range(60):
    #     pseudo_name()
    # create_new_file_ex3('ex2_out.txt', 'file1.txt', 'out.txt')
    file3_to_json('out.txt', 'out.json')


if __name__ == "__main__":
    main()
