__all__ = ['find_pos', 'find_pos_backtrack', 'check_queens_not_attack', 'positions_generator']

import random


# возвращает True, когда расстановка без атаки
def check_queens_not_attack(positions: list) -> bool:
    for i in range(8):
        for j in range(i + 1, 8):
            q_x_pos_1, q_y_pos_1 = positions[i]
            q_x_pos_2, q_y_pos_2 = positions[j]
            if q_x_pos_1 == q_x_pos_2 or q_y_pos_1 == q_y_pos_2 or abs(q_x_pos_1 - q_x_pos_2) == abs(
                    q_y_pos_1 - q_y_pos_2):
                return False
    return True


# генерируем случайную расстановку 8 ферзей
def positions_generator() -> list:
    result = []
    while len(result) < 8:
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        temp_tup = (x, y)
        if temp_tup not in result:
            result.append(temp_tup)
    return result


# проверяем является ли расстановка безопасной и собираем список вариаций
def find_pos(n: int) -> list:
    result = []
    # counter = 0
    # lst_lose_variants = []
    while len(result) < n:
        pos = positions_generator()
        # if counter % 1000 == 0:
        #     print(f'{counter = :_}')
        # temp_set = set(pos)
        # if temp_set not in lst_lose_variants:
        if check_queens_not_attack(pos):
            result.append(pos)
        # lst_lose_variants.append(temp_set)
        # counter += 1
    return result


# выше приведен вариант, получения случайных позиций и проверки на условия расположения без взаимной атаки,
# перебор занимает огромное время, даже для n=2

# возвращает True если под атакой
def check_attack(x1: int, y1: int, x2: int, y2: int) -> bool:
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)


# проверяем, можно ли безопасно добавить
def check_if_add_new(positions, row, col):
    for x, y in positions:
        if check_attack(x, y, row, col):
            return False
    return True


# рекурсивно ищем уникальные варианты, проверяя расстановку после смещения на одну позицию(в сторону)
def find_pos_backtrack(n: int):
    def backtrack(row):
        if row == 8:
            solutions.append(list(queens))
            return
        for col in range(8):
            if check_if_add_new(queens, row, col):
                queens.append((row, col))
                backtrack(row + 1)
                queens.pop()

    solutions = []
    queens = []
    backtrack(0)
    return solutions[:n]


# if __name__ == '__main__':
#     # print(find_pos(1))
#     # print(check_queen_attack([(8, 1), (4, 2), (1, 3), (3, 4), (6, 5), (2, 6), (7, 7), (5, 8)]))
#     lst = find_pos_backtrack(5)
#     print(len(lst))
