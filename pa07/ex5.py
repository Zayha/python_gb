from . import file_generator


def file_generator_2(**kwargs):
    for file_ext, file_qty in kwargs['files']:
        kwargs['file_ext'] = file_ext
        kwargs['file_qty'] = file_qty
        file_generator(**kwargs)


if __name__ == '__main__':
    file_generator_2(files=[('txt', 2), ('dock', 3), ('word', 10)], work_dir='new')
    pass
