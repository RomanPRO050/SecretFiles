# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
# stat = {'а': {'т': 500, 'х': 5, }, 'т': {'о': 100, 'у': 50, },}
import zipfile
from pprint import pprint

# zip_file_name = 'voyna-i-mir.txt.zip'
#
# zfile = zipfile.ZipFile(zip_file_name, 'r')
# for filename in zfile.namelist():
#     zfile.extract(filename)
# from random import randint

import zipfile
from operator import itemgetter
from pprint import pprint


class CharMeter:

    def __init__(self, file_name):
        self.file_name = file_name
        self.count = {}
        self.overall = 0

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha() is True:
                        self.overall += 1
                        if char in self.count:
                            self.count[char] += 1
                        else:
                            self.count[char] = 1

    def dict_to_tuple(self):
        self.list_count = list(self.count.items())

    def sort_by_values_low_to_high(self):
        self.list_count.sort(key=lambda char: char[1])

    def sort_by_values_high_to_low(self):
        self.list_count.sort(key=lambda char: char[1], reverse=True)

    def sort_by_alphabet_high_to_low(self):
        self.list_count = sorted(self.list_count, key=itemgetter(0))

    def sort_by_alphabet_low_to_high(self):
        self.list_count = sorted(self.list_count, key=itemgetter(0), reverse=True)

    def print_result(self):
        print('+{txt:^10}'.format(txt='-----------'), '{txt:^1}'.format(txt='+'), '{txt:^10}+'.format(txt='-----------'))
        print('|{txt:^11}'.format(txt='Буква'), '{txt:^1}'.format(txt='|'), '{txt:^11}|'.format(txt='частота'))
        print('+{txt:^10}'.format(txt='-----------'), '{txt:^1}'.format(txt='+'),
              '{txt:^10}+'.format(txt='-----------'))
        for char in self.list_count:
            print('|{txt:^12}|'.format(txt=char[0]), '{txt:^11}|'.format(txt=char[1]))
        print('+{txt:^10}'.format(txt='-----------'), '{txt:^1}'.format(txt='+'),
              '{txt:^10}+'.format(txt='-----------'))
        print('|{txt:^11}'.format(txt='Итого'), '|{txt:^12}|'.format(txt=self.overall))
        print('+{txt:^10}'.format(txt='-----------'), '{txt:^1}'.format(txt='+'),
              '{txt:^10}+'.format(txt='-----------'))


program = CharMeter(file_name='voyna-i-mir.txt')
program.collect()
program.dict_to_tuple()
program.sort_by_alphabet_high_to_low()
program.print_result()
