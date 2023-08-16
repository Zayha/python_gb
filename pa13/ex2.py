def my_get(get_dict: dict, key, default_value=None):
    result = default_value
    try:
        result = get_dict[key]
    except KeyError as e:
        print(f'Dict haven\'t {key = },\t{default_value = }')
    return result


def main():
    d = {'ok': 33, 'uz': 'ej'}
    print(my_get(d, 'ik', 'ololo'))


if __name__ == '__main__':
    main()
