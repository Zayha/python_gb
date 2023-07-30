__all__ = ['pic_print']

import csv
import pickle


def pic_print(path_tj_file: str) -> bytes:
    with open(path_tj_file, 'r', newline='', encoding='utf-8') as f:
        data = csv.reader(f, delimiter=',')
        result_dict = {}
        for row in enumerate(data):
            if row[0] == 0:
                headers = row[1]
            else:
                result_dict.update(dict(zip(headers, row[1])))
    return pickle.dumps(result_dict)


def main():
    print(pic_print('access_levels.csv'))


if __name__ == "__main__":
    main()
