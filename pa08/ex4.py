__all__ = ["csv_modifier"]

import csv
import json


def csv_modifier(file_name: str, new_file_name: str):
    result = []
    with open(file_name, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for line in enumerate(reader):
            if line[0] == 0:
                headers = line[1]
            else:
                temp_tuple = zip(headers, line[1])
                temp_dict = dict(temp_tuple)
                result.append(temp_dict)
        print(result)
    for d in result:
        d['hash'] = hash(d['Имя'] + d['ID'])
        d['Имя'] = d['Имя'].title()
    print(result)
    with open(new_file_name, 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=2)


def main():
    csv_modifier('access_levels.csv', 'test_modified.json')


if __name__ == "__main__":
    main()
