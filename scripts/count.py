"""
Goal 1: Print the 10 most common names of animals surrendered to the shelter
Goal 1: Print a sorted breakdown of pet types
"""

from __future__ import print_function

# https://docs.python.org/3/library/csv.html
import csv

# https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter

with open('../data/animal-data.csv', 'r') as data_file:

    # create Counter objects
    name_counter = Counter()
    pet_type_counter = Counter()

    # read the file into a DictReader object
    # turn it into a list so we don't have to worry about hitting reset
    reader = csv.DictReader(data_file)

    animal_list = list(reader)

    # loop over the rows in the data
    for row in animal_list:

        # replace asterisks with nothing
        # https://docs.python.org/3/library/stdtypes.html#str.replace
        animal_name = row['Name'].replace('*', '')
        animal_type = row['Animal Type']

        # skip blank names
        if animal_name:

            # add name to counter
            name_counter[animal_name] += 1

        pet_type_counter[animal_type] += 1

    print('\nPopular names:')

    # print 10 most common animal names
    for name, count in name_counter.most_common(10):
        print(name, count)

    print('\nPopular animals:')

    # print animal types + counts
    for pet_type, count in pet_type_counter.most_common():
        print(pet_type, count)
