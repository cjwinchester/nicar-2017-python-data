from __future__ import print_function

import csv
from itertools import groupby

with open('../data/animal-data.csv', 'r') as data_file:
    reader = csv.DictReader(data_file)
    sorted_list = sorted(reader, key=lambda row: row['Name'])
    grouped_list = groupby(sorted_list, key=lambda row: row['Name'])
    for grouper, item in grouped_list:
        print(grouper, list(item))
