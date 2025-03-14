# Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК. Соберите информацию о содержимом в виде объектов
# namedtuple. Каждый объект хранит: имя файла без расширения или название
# каталога, расширение, если это файл, флаг каталога, название родительского
# каталога. В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import argparse
import logging
from pathlib import Path
from collections import namedtuple

logging.basicConfig(filename='tack_5_fileinfo.log', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

File = namedtuple('File', 'name, extension, dir, parent')

def read_dir(path: Path) -> None:
    for file in path.iterdir():
        obj = File(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        logger.info(obj)
        if obj.dir:
            read_dir(Path(obj.parent)/obj.name)

def walker():
    parser = argparse.ArgumentParser(
        description='Сохраняем данные о каталоге в файл',
        prog='read_dir()'
    )
    parser.add_argument('-p', '--path', type=Path, required=True, help='Укажите путь: ')
    args = parser.parse_args()
    return read_dir(args.path)


if __name__ == '__main__':
    walker()

# запуск из терминала
# (.venv) PS C:\Users\likar\PycharmProjects\Python> cd cerification
# (.venv) PS C:\Users\likar\PycharmProjects\Python\cerification> python task_5.py -p C:\Users\likar\PycharmProjects\Python\cerification
# (.venv) PS C:\Users\likar\PycharmProjects\Python\cerification>

