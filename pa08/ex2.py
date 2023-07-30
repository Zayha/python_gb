__all__ = ['save_access_level']

import json
import os


def save_access_level(name: str, personal_id: str, access_level: int, file_name: str) -> bool:
    if os.path.exists(file_name):
        with open(file_name, "r", encoding='utf-8') as f:
            my_dict = json.load(f)
            temp_dict = {}
            for i, v in my_dict.items():
                temp_dict[int(i)] = v
            ids = set()
            for _, v in temp_dict.items():
                for id_in, _ in v.items():
                    ids.add(id_in)
            if personal_id not in ids:
                temp_dict[access_level].update({personal_id: name})
                with open(file_name, "w", encoding='utf-8') as f:
                    json.dump(temp_dict, f)
                return True
            else:
                return False

    else:
        my_dict = {i: {} for i in range(1, 8)}
        my_dict[access_level].update({personal_id: name})
        print(my_dict)
        with open(file_name, "w", encoding='utf-8') as f:
            json.dump(my_dict, f)
        return True


def main():
    x = [0]
    while x[0] != 'exit':
        x = input("Укажите имя/ID пользователя/уровень доступа, через /(или exit для выхода): ").split('/')
        if len(x) != 3:
            continue
        x[2] = int(x[2])
        save_access_level(*x, file_name="access_levels.json")


if __name__ == "__main__":
    main()
