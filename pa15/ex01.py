import logging


def divider(a: int, b: int) -> float:
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        logging.error(f"Error: Division by zero - {e}")


def main():
    logging.basicConfig(filename='error_log.txt', level=logging.ERROR)
    divider(10, 0)


if __name__ == '__main__':
    main()
