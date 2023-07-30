__all__ = ["json_to_csv"]

import csv
import json
from pathlib import Path


def json_to_csv(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    name = Path(file_name).stem
    with open(f'{name}.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["Уровень доступа", "ID", "Имя"])

        for access_level, user_data in data.items():
            for user_id, user_name in user_data.items():
                writer.writerow([access_level, user_id, user_name])


def main():
    json_to_csv('access_levels.json')


if __name__ == '__main__':
    main()
