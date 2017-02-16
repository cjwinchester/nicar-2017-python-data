"""
Goal 1: Print out the percentage of dogs euthanized during this period
Goal 2: Print out the records of other dogs named Jetta

EXTRA CREDIT: Print out the percentage of cats that were spayed or neutured

"""

from __future__ import print_function

# https://docs.python.org/3/library/csv.html
import csv

with open('../data/animal-data.csv', 'r') as data_file:

    # read the file into a DictReader object
    # turn it into a list so we don't have to worry about hitting reset
    reader = csv.DictReader(data_file)

    animal_list = list(reader)

    # use a list comprehension to get just dogs
    dogs = [x for x in animal_list if x['Animal Type'].upper() == 'DOG']

    # use a list comprehension to get just dogs that were euthanized
    ded = [x for x in dogs if x['Outcome Type'].upper() == 'EUTHANASIA']

    # divide # of dead dogs into all dogs to get the pct euthanized
    # float: https://docs.python.org/3/library/functions.html#float
    # len: https://docs.python.org/3/library/functions.html#len
    pct_euthanized = (float(len(ded)) / float(len(dogs))) * 100

    # string formatting: https://docs.python.org/3/library/string.html
    print('\n{:2f} pct of dogs were euthanized'.format(pct_euthanized))

    # filter to get animals named Jetta
    jettas = list(filter(lambda x: 'JETTA' in x['Name'].upper(), dogs))

    # check to see if there are any
    if jettas:

        # if there are, print out some basic details
        print("\nJettas:", len(jettas))
        for jetta in jettas:
            print('-----')
            print('DOB:', jetta['Date of Birth'])
            print('Breed:', jetta['Breed'])
            print('Color:', jetta['Color'])
            print('-----')
