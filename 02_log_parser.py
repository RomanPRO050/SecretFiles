# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

# file_name = 'events.txt'
# with open(file_name, 'r', encoding='cp1251') as log:
#     line2 = ''
#     k = 1
#     nok = 0
#     for line in log:
#         if k == 1:
#             line1 = line[1:17]
#         if k > 1:
#             line1 = line[1:17]
#             if line1 == line2:
#                 search = line[28:]
#                 if search.find('NOK') > -1:
#                     nok += 1
#             elif line1 != line2:
#                 write_str = '[' + line2 + ']' + f' {nok}' + '\n'
#                 with open('out_log.txt', 'r+', encoding='utf8') as writing:
#                     file_eof = int(len(writing.read()))
#                     writing.write(write_str)
#                 nok = 0
#                 search = line[28:]
#                 if search.find('NOK') > -1:
#                     nok += 1
#         # print(line[1:17])
#         line2 = line1
#         k += 1


class LogParser:

    def __init__(self, file_name):
        self.file_name = file_name
        self.nok = 0
        self.line2 = ''
        self.k = 1

    def file_clear(self):
        null_str = ''
        with open('out_log.txt', 'w', encoding='utf8') as writing:
            writing.write(null_str)

    def group_by_minute(self):
        with open(self.file_name, 'r', encoding='cp1251') as log:
            for line in log:
                if self.k == 1:
                    line1 = line[1:17]
                if self.k > 1:
                    line1 = line[1:17]
                    self.comparison_and_writing(line, line1)
                self.line2 = line1
                self.k += 1

    def group_by_hour(self):
        with open(self.file_name, 'r', encoding='cp1251') as log:
            for line in log:
                if self.k == 1:
                    line1 = line[1:14]
                if self.k > 1:
                    line1 = line[1:14]
                    self.comparison_and_writing(line, line1)
                self.line2 = line1
                self.k += 1

    def group_by_day(self):
        with open(self.file_name, 'r', encoding='cp1251') as log:
            for line in log:
                if self.k == 1:
                    line1 = line[1:11]
                if self.k > 1:
                    line1 = line[1:11]
                    self.comparison_and_writing(line, line1)
                self.line2 = line1
                self.k += 1

    def comparison_and_writing(self, line, line1):
        if line1 == self.line2:
            search = line[28:]
            if search.find('NOK') > -1:
                self.nok += 1
        elif line1 != self.line2:
            self.writing_result()
            self.nok = 0
            search = line[28:]
            if search.find('NOK') > -1:
                self.nok += 1

    def group_by_month(self):
        with open(self.file_name, 'r', encoding='cp1251') as log:
            for line in log:
                if self.k == 1:
                    line1 = line[1:8]
                if self.k > 1:
                    line1 = line[1:8]
                    if line1 == self.line2:
                        search = line[28:]
                        if search.find('NOK') > -1:
                            self.nok += 1
                self.line2 = line1
                self.k += 1
            write_str = '[' + self.line2 + ']' + f' {self.nok}' + '\n'
            self.writing_result()

    def group_by_year(self):
        with open(self.file_name, 'r', encoding='cp1251') as log:
            for line in log:
                if self.k == 1:
                    line1 = line[1:5]
                if self.k > 1:
                    line1 = line[1:5]
                    if line1 == self.line2:
                        search = line[28:]
                        if search.find('NOK') > -1:
                            self.nok += 1
                self.line2 = line1
                self.k += 1
            self.writing_result()

    def writing_result(self):
        write_str = '[' + self.line2 + ']' + f' {self.nok}' + '\n'
        with open('out_log.txt', 'r+', encoding='utf8') as writing:
            file_eof = int(len(writing.read()))
            writing.write(write_str)


parser = LogParser(file_name='events.txt')
parser.file_clear()
parser.group_by_day()
