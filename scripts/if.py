"""
Goal: Print only the names of beagle/beagle mixes
"""

from __future__ import print_function

# https://docs.python.org/3/library/csv.html
import csv

with open('../data/animal-data.csv', 'r') as data_file:

    # read the file into a DictReader object
    reader = csv.DictReader(data_file)

    # loop over the rows in your data
    for row in reader:

        animal_name = row['Name'].replace('*', '')
        animal_type = row['Animal Type']
        animal_breed = row['Breed']

        # get dogs with "beagle" in the breed somewhere
        # https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
        if animal_type.upper() == 'DOG' and 'BEAGLE' in animal_breed.upper():
            if animal_name:
                print("WHO'S A GOOD BOY:", animal_name,)
