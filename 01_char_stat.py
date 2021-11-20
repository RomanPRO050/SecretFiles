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

from operator import itemgetter, attrgetter, methodcaller

file_name = 'voyna-i-mir.txt'

count = {}

with open(file_name, 'r', encoding='cp1251') as file:
    for line in file:
        # line = line[:-1]
        # print(line)
        for char in line:
            if char.isalpha() is True:
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1

list_count = list(count.items())
# сортировка по частоте возрастанию
# list_count.sort(key=lambda char: char[1])

# сортировка по частоте убыванию
# list_count.sort(key=lambda char: char[1], reverse=True)

# сортировка по алфавиту убыванию
# list_count = sorted(list_count, key=itemgetter(0))

# сортировка по алфавиту возрастанию
list_count = sorted(list_count, key=itemgetter(0), reverse=True)

for char in list_count:
    print(char[0], ':', char[1])
