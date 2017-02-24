"""
Goal: print a list of pet names in alpha order
"""

from __future__ import print_function

# https://docs.python.org/3/library/csv.html
import csv

with open('../data/animal-data.csv', 'r') as data_file:

    # read the file into a DictReader object
    reader = csv.DictReader(data_file)

    # sort data by animal name
    # https://docs.python.org/3/library/functions.html#sorted
    sorted_list = sorted(reader, key=lambda row: row['Name'])

    # loop over the data
    for animal in sorted_list:

        # skip blank names
        if animal['Name']:
            print(animal['Name'])
