"""
Goal: print a list of pet names in alpha order
"""

from __future__ import print_function

# https://docs.python.org/3/library/csv.html
import csv

with open('../data/animal-data.csv', 'r') as data_file:

    # read the file into a DictReader object
    # turn it into a list so we don't have to worry about hitting reset
    reader = csv.DictReader(data_file)

    animal_list = list(reader)

    # sort data by animal name
    # https://docs.python.org/3/library/functions.html#sorted
    sorted_list = sorted(animal_list, key=lambda row: row['Name'])

    # loop over the data
    for animal in sorted_list:

        # skip blank names
        if animal['Name']:
            print(animal['Name'])
