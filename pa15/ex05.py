import argparse
import logging
import re
import calendar
from datetime import datetime, timedelta


def collect_day_num(year: int, month: int, weekday: int, counter: int) -> datetime | None:
    days_in_month = calendar.monthrange(year, month)[1]
    interval_24h = timedelta(days=1)
    start_day = datetime(year, month, 1)
    day_counter = 0
    for _ in range(1, days_in_month + 1):
        if start_day.weekday() == weekday:
            day_counter += 1
            if day_counter == counter:
                return start_day
        start_day = start_day + interval_24h


def convert_text_to_date(text: str) -> datetime:
    logging.basicConfig(filename='date_conv.log', level=logging.ERROR, encoding='utf-8')
    logging.error(' *' * 50)
    month_dict = {
        'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,
        'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
        'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
    }

    weekday_dict = {
        'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3,
        'пятница': 4, 'суббота': 5, 'воскресенье': 6
    }

    n_year = datetime.now().year

    pattern = r'(\d)-[йя] ([а-я]+) ([а-я]+)'
    match = re.match(pattern, text)
    if not match:
        logging.error('Ошибка обработки исходных данных из строки')
        raise ValueError('Из исходной строки не удалось собрать данные')

    weekday = weekday_dict.get(match.group(2), None)
    month = month_dict.get(match.group(3), None)
    c_day_num = int(match.group(1))
    if not 0 < c_day_num < 6:
        logging.error(f'Данные в порядковом положении дня недели недопустимы')
    if weekday is None:
        logging.error(f'Ошибка обработки данных из строки, не удалось собрать данные о дне недели - {match.group(2)}')
    if month is None:
        logging.error(f'Ошибка обработки данных из строки, не удалось собрать данные о месяце {match.group(3)}')

    result_date = collect_day_num(n_year, month, weekday, c_day_num)
    if result_date is None:
        logging.error('Недопустимый набор параметров для вычисления даты')
        raise ValueError

    return result_date


def main():
    parser = argparse.ArgumentParser(description='Принимаем дату в различных форматах')
    parser.add_argument('-s', type=str, help='ожидает ввод даты формата: “1-й четверг ноября"')
    parser.add_argument('-m', type=int, help='передайте номер месяца', default=datetime.now().month)
    parser.add_argument('-w', type=int, help='передайте номер дня недели, понедельник 0',
                        default=datetime.now().weekday())
    parser.add_argument('-c', type=int, help='передайте порядковый номер если вам нужен второй понедельник,'
                                             ' укажите 2', default=1)
    args = parser.parse_args()
    if args.s is not None:
        print(convert_text_to_date(args.s))
    else:
        print(collect_day_num(datetime.now().year, args.m, args.w, args.c))


if __name__ == '__main__':
    main()
