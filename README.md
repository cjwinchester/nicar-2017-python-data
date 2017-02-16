# Data crunching in Python (for people who only know Excel)

NICAR 2017 / March 3, 9 a.m. / City Terrace 8

This is an intro-level session for people who are comfortable with spreadsheets but want to start working with data in Python.

We won't be using pandas, Agate or any other popular data analysis library. Instead, we shall find inspiration by looking at some common Excel tasks and and the equivalent functionality in Python's standard library.

(It's cool if you already know how to make a Python script go but nbd if you don't.)

### Why tho

* Repeatability!
* Gateway to more advanced analyses

### Data

We'll mostly be working with a CSV of animal outcome data from the [Austin Animal Center](https://data.austintexas.gov/Health/Austin-Animal-Center-Outcomes/9t4d-g238); find it at `data/animal-data.csv`.

### Scripts
* FILTER: `scripts/filter.py`
* COUNT: `scripts/count.py`
* CONCATENATE: `scripts/concatenate.py`
* MAX/MIN: `scripts/max_min.py`
* LEFT/RIGHT/MID: `scripts/left_right_mid.py`
* SORT: `scripts/sort.py`
* SUM: `scripts/sum.py` (uses tax data)

### Loading data

Each script loads data using Python's built-in [`csv`](https://docs.python.org/3/library/csv.html) module.

```python
import csv

with open('data/animal-data.csv', 'rb') as data_file:
	reader = csv.DictReader(data_file)
    for row in reader:
    	animal_id = row['Animal ID']
    	animal_name = row['Name']
    	intake_date = row['DateTime']
    	intake_monthyear = row['MonthYear']
    	animal_dob = row['Date of Birth']
    	animal_outcome['Outcome Type']
    	animal_outcome_subtype = row['Outcome Subtype']
    	animal_type = row['Animal Type']
    	animal_sex = row['Sex upon Outcome']
    	animal_age = row['Age upon Outcome']
    	animal_breed = row['Breed']
    	animal_color = row['Color']

```


### Also check out
* Friday, 11:30 a.m. in City Terrace 8: [Data wrangling with Python](https://ire.org/events-and-training/event/2702/2948/) (Anthony DeBarros)

### Hit me up!

Cody Winchester
Austin American-Statesman
cjwinchester@gmail.com
@cody_winchester