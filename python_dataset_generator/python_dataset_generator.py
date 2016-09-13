# -*- coding: utf-8 -*-

import os
import random
import csv
from collections import namedtuple

DEFAULT_OUTPUT_FILENAME = 'dataset_output.csv'
DEFAULT_ROWS = 10000
DEFAULT_DELIMITER = ','


class python_dataset_generator:

    def __init__(self, rows=10000, delimiter=',', filename='dataset_output.csv'):
        self._rows = rows
        self._delimiter = delimiter
        self._filename = filename
        self._factors = list()
        self._last_factor = 0
        self._generated_rows = 0
        self._positive_ratio = 50
        self._enable_incremental_id = True

    def add_factor(self, name, good_range, bad_range, ratio=33, mixed=False):
        factor = namedtuple('Factor', 'name good_range bad_range ratio mixed current_ratio current_amount')

        factor.name = name
        factor.mixed = mixed
        factor.good_range = good_range
        factor.bad_range = bad_range
        factor.ratio = ratio

        factor.current_amount = 0
        factor.current_ratio = 0

        self._factors.append(factor)

        # self._factors.append({
        #     'name': name,
        #     'good_range': good_range,
        #     'bad_range': bad_range,
        #     'ratio': ratio,
        #     'mixed': mixed,
        #     'current_amount': 0
        # })

    def _go_to_next_factor(self):
        self._last_factor += 1
        if self._last_factor > len(self._factors)-1:
            self._last_factor = 0

    def _create_positive_factor_row(self):
        row = list()
        for factor in self._factors:
            positive_range_min = factor.good_range[0]
            if len(factor.good_range) > 1:
                positive_range_max = factor.good_range[1]
                val = random.randint(positive_range_min, positive_range_max)
            else:
                val = positive_range_min

            row.append(val)
        return row

    def _create_negative_factor_row(self):
        row = list()
        for factor in self._factors:
            positive_range_min = factor.bad_range[0]
            if len(factor.bad_range) > 1:
                positive_range_max = factor.bad_range[1]
                val = random.randint(positive_range_min, positive_range_max)
            else:
                val = positive_range_min

            row.append(val)
        return row

    def _get_factor_names(self):
        names = list()
        for factor in self._factors:
            names.append(factor.name)
        return names

    def _generate(self):
        if not self._factors:
            return

        with open(self._filename, 'w', newline='\n') as file:
            writer = csv.writer(file,
                                delimiter=',',
                                quotechar='|',
                                quoting=csv.QUOTE_MINIMAL)
            writer.writerow(self._get_factor_names())

            weighted_random = [True] * self._positive_ratio + [False] * (100-self._positive_ratio)

            for id, row in enumerate(range(self._rows)):
                data_choice = random.choice(weighted_random)

                if data_choice:
                    output_row = self._create_positive_factor_row()
                else:
                    output_row = self._create_negative_factor_row()

                if self._enable_incremental_id:
                    output_row.insert(0, id+1)

                writer.writerow(output_row)

    def save(self):
        self._generate()



if __name__ == "__main__":
    generator = python_dataset_generator()
    generator.add_factor('photo_width', [2000, 5000], [1, 1000])
    generator.add_factor('photo_colours', [12000, 55886], [1, 9000])
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