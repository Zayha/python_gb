import argparse
import logging
from collections import namedtuple
from pathlib import Path


def collect_directory_info(directory_path):
    logging.basicConfig(filename='directory_info.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')
    directory = Path(directory_path)
    FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

    if not directory.exists() or not directory.is_dir():
        logging.error(f"Директория '{directory_path}' не существует или не является директорией.")
        return

    directory_info = []
    for item in directory.iterdir():
        name = item.stem
        extension = item.suffix[1:] if item.is_file() else None
        is_directory = item.is_dir()
        parent_directory = directory.name

        file_info = FileInfo(name, extension, is_directory, parent_directory)
        directory_info.append(file_info)

    logging.info(f"Информация о директории {directory}:")
    for i in directory_info:
        logging.info(f">>>>>> {str(i)}")


def main():
    parser = argparse.ArgumentParser(description='Передайте путь к директории')
    parser.add_argument('--path', type=str, help='ожидает к директории!',
                        default=Path.cwd())
    args = parser.parse_args()
    collect_directory_info(args.path)


if __name__ == '__main__':
    main()
