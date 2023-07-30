__all__ = ['file3_to_json']

import json


def file3_to_json(file_inp: str, file_out: str):
    with (
        open(file_inp, 'r', encoding='utf-8') as input_file,
        open(file_out, 'w', encoding='utf-8') as output_file,
    ):
        my_dict = {k.title(): v for line in input_file for k, v in [line.split()]}
        json.dump(my_dict, output_file, ensure_ascii=False, indent=2)


def main():
    file3_to_json('out.txt', 'out.json')


if __name__ == "__main__":
    main()
