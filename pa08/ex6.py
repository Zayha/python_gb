__all__ = ['pickle_dict_to_csv']

import csv
import pickle


def pickle_dict_to_csv(path_to_file: str, csv_file_name: str):
    with (
        open(path_to_file, 'rb') as f,
        open(csv_file_name, 'w', encoding='utf-8', newline='') as csv_file
    ):
        data = pickle.load(f)
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    pickle_dict_to_csv('json_for_test/test_modified.pkl', 'test_data.csv')


if __name__ == '__main__':
    main()
