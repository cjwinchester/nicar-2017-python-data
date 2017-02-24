"""
Goal: Print the ~current~ age, in days, of each animal with a DOB

EXTRA CREDIT 1: Add the logic to exclude animals that were euthanized,
                because their current age is ~dead~

EXTRA CREDIT 2: Find the record of the oldest animal surrendered
                to the shelter during this time period
"""

from __future__ import print_function

# https://docs.python.org/3/library/csv.html
import csv

# https://docs.python.org/3/library/datetime.html
from datetime import datetime

with open('../data/animal-data.csv', 'r') as data_file:

    # read the file into a DictReader object
    reader = csv.DictReader(data_file)

    # loop over the rows in your data
    for row in reader:

        animal_dob = row['Date of Birth']

        # skip blank DOBs
        if animal_dob:

            # turn string into datetime object
            formatted_dob = datetime.strptime(animal_dob, '%m/%d/%Y')

            # get today's date as datetime object
            today = datetime.now()

            # get the difference
            diff = today - formatted_dob

            # print difference in days
            print(diff.days)
