import operator
import sys

items = {
    'горелка': 0.2,
    'зажигалка': 0.05,
    'топорик': 1.0,
    'тапки': 0.3,
    'плавки': 0.15,
    'шапка': 0.15,
    'дошик': 0.3,
    'тушенка': 0.45,
    'лопатка': 1.5,
    'аптечка': 0.6,
    'трос': 0.5,
    'спирт': 0.6,
    'аккумулятор': 2.2,
    'гиря': 16.0,
    'котелок': 1.1,
    'дождевик': 0.8,
    'мачете': 1.5,
    'стакан': 0.15,
}


def collect_backpack(weight: float, collect: dict) -> tuple:
    total: float = 0.0
    total_lst = []
    if sys.version_info.major >= 3 and sys.version_info.minor >= 7:
        sorted_dict = dict(sorted(collect.items(), key=operator.itemgetter(1)))
        for k, v in sorted_dict.items():
            total_temp = total + v
            if total_temp <= weight:
                total += v
                total_lst.append(k)
            else:
                break
    free_weight = weight - total
    return total, total_lst, free_weight


pack = collect_backpack(10.0, items)
print(f'Общий вес груза составит: {pack[0]}, комплектация: {pack[1]}, осталось свободного: {pack[2]:.2f}кг')
