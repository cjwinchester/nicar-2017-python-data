"""
Goal: Sum the amount of mixed-beverage taxes collected in TX year to date
"""

from __future__ import print_function

# https://docs.python.org/3/library/csv.html
import csv

with open('../data/tax-data.csv', 'r') as data_file:

    # read the file into a DictReader object
    # turn it into a list so we don't have to worry about hitting reset
    reader = csv.DictReader(data_file)

    tax_list = list(reader)

    # use a list comprehension to get a list of payments as floats
    # replace commas and dollar signs with nothing
    payments = [float(x['Payment Year to Date']
                .replace(',', '')
                .replace('$', '')) for x in tax_list]

    # sum the list
    tax_sum = sum(payments)

    # print formatted sum
    print('\nSum: $' + '{:,.2f}'.format(tax_sum))
