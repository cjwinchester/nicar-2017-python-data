"""
Goals: Print the first letter of each pet's name
       Print the 2nd through 4th letters of each pet's name, if exists
       Print the last letter of each pet's name

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

        # skip blank names
        if animal_name:

            print('\n-----')

            # print first letter
            print('first:', animal_name[0])

            # try to print chars 2, 3, 4
            # do nothing if those chars don't exist
            # https://docs.python.org/3/tutorial/errors.html#handling-exceptions
            # (n.b. python is "zero-indexed," which means 0 = "first")
            try:
                print('2-4:', animal_name[1:4])
            except:
                pass

            # print last letter
            print('last:', animal_name[-1])
