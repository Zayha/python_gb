import datetime
import logging
from functools import wraps
from typing import Callable


def log_to_file(func: Callable):
    logging.basicConfig(filename='func_log.log', level=logging.INFO, encoding='utf-8')

    def time_now(form: str = " %d-%m-%Y %H:%M:%S > ") -> str:
        return datetime.datetime.now().strftime(form)

    @wraps(func)
    def wrapper(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        arg_info = ', '.join([f'arg{i} = {arg}' for i, arg in enumerate(args)])
        kwarg_info = ', '.join([f'{key = }{value}' for key, value in kwargs.items()])
        all_args = ', '.join([arg_info, kwarg_info])

        logger.info(' *' * 50)
        logger.info(f'{time_now()} Была вызвана функция {name} с аргументами: {all_args}')

        try:
            result = func(*args, **kwargs)
            logger.info(
                f'{time_now()} Функция {name} вернула: {result}')
        except Exception as ex:
            logger.error(f'{time_now()} Функция {name} вернула исключение {ex}')

    return wrapper


@log_to_file
def divider(a: int, b: int) -> float:
    result = a / b
    return result


def main():
    divider(12, 0)


if __name__ == '__main__':
    main()
