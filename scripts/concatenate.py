"""
Goals: Print each pet's name, a colon, and its DOB

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
        animal_dob = row['Date of Birth']

        # skip blank names/dobs
        if animal_name and animal_dob:

            # print name and DOB
            print(animal_name + ': ' + animal_dob)
