# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def get_dict(**kwargs):
    result = {}
    for k, v in kwargs.items():
        if not isinstance(v, (int, float, str, tuple)):
            v = str(v)
        result[v] = k
    return result


print(get_dict(gerasim='za4em', mumu='utopil', test=['set']))
