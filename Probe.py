import zipfile
from pprint import pprint



# zip_file_name = 'voyna-i-mir.txt.zip'
#
# zfile = zipfile.ZipFile(zip_file_name, 'r')
# for filename in zfile.namelist():
#     zfile.extract(filename)
from random import randint

file_name = 'voyna-i-mir.txt'

stat = {}

# stat = {'а': {'т': 500, 'х': 5, }, 'т': {'о': 100, 'у': 50, },}

analize_count = 4
sequence = ' ' * analize_count

with open(file_name, 'r', encoding='cp1251') as file:
    for line in file:
        line = line[:-1]
        #print(line)
        for char in line:
            if sequence in stat:
                if char in stat[sequence]:
                    stat[sequence][char] += 1
                else:
                    stat[sequence][char] = 1
            else:
                stat[sequence] = {char: 1}
            sequence = sequence[1:] + char

# pprint(stat)
pprint(len(stat))

totals = {}
stat_for_generate = {}
for sequence, char_stat in stat.items():
    totals[sequence] = 0
    stat_for_generate[sequence] = []
    for char, count in char_stat.items():
        totals[sequence] += count
        stat_for_generate[sequence].append([count, char])
    stat_for_generate[sequence].sort(reverse=True)

N = 1000

printed = 0
sequence = ' ' * analize_count
spaces_printed = 0
while printed < N:
    char_stat = stat_for_generate[sequence]
    total = totals[sequence]
    dice = randint(1, total)
    pos = 0
    for count, char in char_stat:
        pos += count
        if dice <= pos:
            break
    print(char, end='')
    if char == ' ':
        spaces_printed += 1
        if spaces_printed >= 10:
            print()
            spaces_printed = 0
    printed += 1
    sequence = sequence[1:] + char
