# -*- coding: utf-8 -*-

import os
import random
import csv

DEFAULT_OUTPUT_FILENAME = 'dataset_output.csv'
DEFAULT_ROWS = 10000
DEFAULT_DELIMITER = ','


class python_dataset_generator:

    def __init__(self, rows=10000, delimiter=',', filename='dataset_output.csv'):
        self._rows = rows
        self._delimiter = delimiter
        self._filename = filename

    def add_factor(self, name, good_range, bad_range, ratio, mixed=False):
        pass

    def _generate(self):
        pass

    def save(self):
        self._generate()

        with open(self._filename, 'w') as file:
            file.write('')


if __name__ == "__main__":
    generator = python_dataset_generator()
    generator.add_factor('photo_width', [1024, 5000], [10, 1000], 50)
    generator.save()




'''



'''


"""

   - the mixed data can be from the lower and upper boundaries of the good/bad
   - accommodate floating vs int
   - accountmodate the good being -numbers
   - accommodate when the bad values are above the good values when doing the mixed thing
   - allow for a default file?


"""