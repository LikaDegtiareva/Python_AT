# Напишите скрипт, который принимает два аргумента командной строки: число и строку.
# Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.

import argparse


def main():
    parser = argparse.ArgumentParser(description='Это скрипт, который принимает: число и строку '
                                                 'и обладает дополнительными опциями')
    parser.add_argument('number', type=int, help='Число для вывода')
    parser.add_argument('text', type=str, help='Строка для вывода')
    parser.add_argument('--verbose', action='store_true', help='Вывод дополнительной информации')
    parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки')
    args = parser.parse_args()
    if args.verbose:
        print(f'Полученные аргументы: number={args.number}, text="{args.text}", repeat={args.repeat}')

    print(f'Число: {args.number}, Строка: {args.text *args.repeat}')


if __name__ == '__main__':
    main()

# запуск из терминала!
# (.venv) PS C:\Users\likar\PycharmProjects\Python> cd cerification
# (.venv) PS C:\Users\likar\PycharmProjects\Python\cerification> python task_4.py 5 Hellow --repeat 10
# Число: 5, Строка: HellowHellowHellowHellowHellowHellowHellowHellowHellowHellow
# (.venv) PS C:\Users\likar\PycharmProjects\Python\cerification> python task_4.py 5 Hellow --verbose --help
# usage: task_4.py [-h] [--verbose] [--repeat REPEAT] number text
#
# Это скрипт, который принимает: число и строку и обладает дополнительными опциями
#
# positional arguments:
#   number           Число для вывода
#   text             Строка для вывода
#
# options:
#   -h, --help       show this help message and exit
#   --verbose        Вывод дополнительной информации
#   --repeat REPEAT  Количество повторений строки


