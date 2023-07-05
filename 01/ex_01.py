def check_triangle(a: int, b: int, c: int) -> bool:
    return True if a + b > c and a + c > b and c + b > a else False


def get_triangle_type(a: int, b: int, c: int) -> str:
    if check_triangle(a, b, c):
        lst = [a, b, c]
        lst.sort()
        return 'равносторонний' if a == b == c else \
            'прямоугольный' if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2 else \
                'равнобедренный' if lst[1] == lst[2] else 'разносторонний'
    else:
        return 'не существует'


a = 3
b = 4
c = 5
print(f'Треугольник со сторонами {a}, {b}, {c}: {get_triangle_type(a, b, c)}')
