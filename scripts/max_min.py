"""
Goal: Find the largest and smallest mixed-beverage tax collection
"""

from __future__ import print_function

# https://docs.python.org/3/library/csv.html
import csv

with open('../data/tax-data.csv', 'r') as data_file:

    # read the file into a DictReader object
    reader = csv.DictReader(data_file)

    # use a list comprehension to get a list of payments as floats
    # replace commas and dollar signs with nothing
    payments = [float(x['Payment Year to Date']
                .replace(',', '')
                .replace('$', '')) for x in reader]

    # get min
    tax_min = min(payments)

    # get max
    tax_max = max(payments)

    # print formatted min
    print('\nMin: $' + '{:,.2f}'.format(tax_min))

    # print formatted max
    print('Max: $' + '{:,.2f}'.format(tax_max))
