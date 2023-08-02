__all__ = ['fu_to_json']

import json
import random
from functools import wraps
from pathlib import Path
from typing import Callable


def fu_to_json(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # print(args, '\n', kwargs, func.__name__)
        file_name = f'{func.__name__}.json'
        my_json = []
        my_data = {}
        if Path(file_name).exists():
            with open(file_name, encoding='utf-8') as f:
                my_json = json.load(f)
        for i in range(len(args)):
            my_data[f'arg{i}'] = args[i]
        for k, v in kwargs.items():
            my_data[k] = v
        result = func(*args, **kwargs)
        my_data['result'] = result
        my_json.append(my_data)
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(my_json, f)
        return result

    return wrapper


@fu_to_json
def my_fu(*args, **kwargs):
    return random.randint(1, 10000)


if __name__ == '__main__':
    my_fu(1, 2, 3, kepka='ohe')
