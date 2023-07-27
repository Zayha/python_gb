__all__ = ['sorting_files']

import os
import shutil
from pathlib import Path


def sorting_files(**kwargs):
    video = ['mp4', 'avi', 'mpeg']
    audio = ['mp3', 'wav', 'flac', 'aac', 'ogg', 'wma']
    text = ['txt', 'word', 'doc', 'docx']
    ext = {'video': video, 'audio': audio, 'text': text}

    path = kwargs.get('path')
    # print(path)
    if path is not None and Path(path).exists():
        files = [file for _, _, files in os.walk(Path(Path.cwd() / path)) for file in files]
        # print(files)
        for file in files:
            print(file)
            *_, ex = file.split(".")
            for k, v in ext.items():
                if ex in v:
                    new_path = Path(Path.cwd() / path / k / file)
                    new_path.parent.mkdir(parents=True, exist_ok=True)
                    print(new_path)
                    shutil.move(Path(Path.cwd() / path / file), new_path)


if __name__ == '__main__':
    sorting_files(path='new')