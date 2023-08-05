import json
import os
import pickle
from pathlib import Path

from pa08 import pickle_dict_to_csv, pic_print


class CsvJson:
    def __init__(self, **kwargs):
        self.in_path = kwargs.get('in_path', None)
        self.out_path = kwargs.get('out_path', None)

    def csv_to_json_string(self):
        return pic_print(self.in_path)

    def pickle_dict_to_csv(self):
        pickle_dict_to_csv(self.in_path, self.out_path)

    # немного переписал для удобства
    def json_to_pickle(self):
        files = next(os.walk(self.in_path))[2]
        print(files)
        for file in files:
            if Path(file).suffix == '.json':
                new_file = Path(Path().cwd() / self.in_path / Path(file).stem).with_suffix('.pkl')
                with (open(new_file, 'wb') as f_pickle,
                      open(Path(Path().cwd() / self.in_path / file), 'r', encoding='utf-8') as f_json):
                    pickle.dump(json.load(f_json), f_pickle)


def main():
    CsvJson(in_path='.').json_to_pickle()
    CsvJson(in_path='test_modified.pkl', out_path='access_levels.csv').pickle_dict_to_csv()
    print(CsvJson(in_path='access_levels.csv').csv_to_json_string())


if __name__ == '__main__':
    main()
